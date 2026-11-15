#!/usr/bin/env python3
"""Mechanical half of the design preflight.

Parses a finished English prompt and reports the checks that can be counted:
word budget, colour and material term frequencies against the role caps, banned
words, whether the required identity elements are present, whether the identity
set was derived rather than defaulted, and — with --ledger — whether the batch
vector actually differs from the characters already designed.

It does not judge silhouette readability, value hierarchy, "face wins", charm,
commercial read, or whether the face looks like a different person. Those need
an eye. See references/pipeline/design.md §6A.

Usage:
    python -I preflight.py prompt.txt --register editorial
    python -I preflight.py prompt.txt --register glamour --palette
    python -I preflight.py prompt.txt --register glamour --ledger batch.txt
    python -I preflight.py prompt.txt --register glamour --identity "facial index 1.52; mouth 0.76"

Input may be a bare prompt or a fenced code block copied verbatim; fences and a
trailing --ar/--no suffix are stripped before counting.

Exit code is 0 when every counted check passes, 1 otherwise, so it can gate a
pipeline. Judged checks are never part of the exit code.
"""

import argparse
import re
import sys

# Caps from references/bank/form.md §3B and pipeline/design.md §6C/6D.
CAPS = {
    "editorial": {"accent": 2, "anchor": 4, "base": 8, "material": 5},
    "glamour": {"accent": 2, "anchor": 4, "base": 8, "material": 5},
}

# Word budget from references/pipeline/design.md §4.
BUDGET = {
    "editorial": (500, 540),
    "glamour": (540, 585),
    "compact": (270, 310),
    "portrait": (0, 400),
    "scene": (0, 400),
}

# Banned words from references/contract/gates.md §6.
BANNED = [
    "gorgeous", "masterpiece", "breathtaking", "stunning", "very detailed",
    "highly detailed", "beautiful texture", "ultra detailed",
    "elaborate", "intricate", "ornate", "richly decorated", "lavishly detailed",
    "hero ornament", "primary open area", "design thesis", "aesthetic order",
    "gravity topology", "design evidence",
]

# Numeric quality tags. Not \b-delimited on the left because they start with a
# digit, which \b does not place between " " and "8". See gates.md §6.
BANNED_NUMERIC = [(r"(?<![A-Za-z0-9])8k(?![A-Za-z0-9])", "8k"),
                  (r"(?<![A-Za-z0-9])4k(?![A-Za-z0-9])", "4k")]

# Engine settings that do not belong in an image prompt.
SHADER = ["roughness", "metallic 1", "ior 1", "sss radius", "specular 0"]

# Terms forbidden in Midjourney --no, from contract/visual.md §11.
NO_FORBIDDEN = ["doll", "seams", "skin", "figure"]

# Elements the prompt must name, from contract/visual.md §5 and §8.
# These are CRAFT strings: shared by every character, reused verbatim. They are
# not evidence that the face is specific to this character — that is
# IDENTITY_DERIVED below. See gates.md §8.
IDENTITY_REQUIRED = {
    "anime eye design": [r"upper lid", r"\bcrease\b", r"iris"],
    "second catchlight": [r"secondary reflection|second catchlight|two catchlight"],
    "porcelain skin": [r"porcelain"],
    "hair clumps": [r"strand clump|sculpted lock|grouped lock"],
    "one key direction": [r"\bkey\b.*(left|right)|from the (left|right)|side-back|overhead"],
}

# The ten identity parameters from bank/face.md §2. Each must be decided by a
# character fact (§2A-1), so the identity block has to state a value for at
# least the three anchoring ones — facial index, mouth width, inter-canthal
# distance — or the face was defaulted. Written as patterns for the visible
# consequence, because measurements stay out of the English prompt (§1).
IDENTITY_ANCHORS = {
    "anchoring face value (facial index / mouth width / eye spacing)": [
        r"long narrow face", r"broad short face", r"narrow mouth", r"wide mobile mouth",
        r"close-set eyes", r"widely spaced eyes", r"broad jaw", r"narrow jaw",
    ],
    "one body proportion band, not a default": [
        r"7-to-7\.5-head", r"7\.5-to-8-head", r"8\.5-head", r"\d(\.\d)?[- ]head",
    ],
}

# The nine batch axes from contract/gates.md §9, in the order the ledger stores
# them. Axis 1 and 2 are hard failures; five of nine must differ.
LEDGER_AXES = [
    "silhouette", "key colour", "topology", "register+gear",
    "contradiction", "light", "trim", "motif", "face anchor",
]
LEDGER_MANDATORY = {0, 1}   # silhouette, key colour
LEDGER_MIN_DIFFERENT = 5


def strip_prompt(text):
    """Return the prompt body, dropping fences, trailing parameters, and headings."""
    text = text.replace("\r\n", "\n")
    # If it contains fenced blocks, take the longest one: that is the prompt.
    blocks = re.findall(r"```(?:text|txt|markdown)?\n(.*?)```", text, re.S)
    if blocks:
        text = max(blocks, key=len)
    # Cut the parameter tail so flags are not counted as prose.
    text = re.split(r"\s--(?:ar|raw|s|hd|no|style|niji)\b", text)[0]
    return text.strip()


def words(text):
    return re.findall(r"[A-Za-z][A-Za-z'-]*", text)


def count_term(low, term):
    """Count a term, splitting hyphenated compounds so bone-white matches bone too."""
    return len(re.findall(r"\b" + re.escape(term) + r"\b", low))


def parse_palette(text):
    """Read a blueprint palette line, if one was pasted above the prompt."""
    roles = {}
    for role in ("base", "anchor", "accent"):
        m = re.search(rf"{role}\s*[:=]\s*([^\n;/|]+)", text, re.I)
        if m:
            roles[role] = [t.strip().lower() for t in re.split(r"[,+]", m.group(1)) if t.strip()]
    return roles


def check(args):
    raw = open(args.path, encoding="utf-8").read()
    prompt = strip_prompt(raw)
    low = prompt.lower()
    nwords = len(words(prompt))
    failures, notes = [], []

    # --- word budget ---
    lo, hi = BUDGET[args.register]
    if hi and not (lo <= nwords <= hi):
        failures.append(f"word budget: {nwords} words, expected {lo}-{hi}")
    else:
        notes.append(f"word count: {nwords} (budget {lo}-{hi})")

    # --- banned words ---
    hits = [b for b in BANNED if re.search(r"\b" + re.escape(b) + r"\b", low)]
    numeric_hits = [label for pat, label in BANNED_NUMERIC if re.search(pat, low)]
    if hits or numeric_hits:
        failures.append("banned words: " + ", ".join(hits + numeric_hits))

    # --- shader parameters ---
    shader = [s for s in SHADER if s in low]
    if shader:
        failures.append("engine settings in prompt: " + ", ".join(shader))

    # --- required identity elements (craft) ---
    missing = []
    for label, pats in IDENTITY_REQUIRED.items():
        if not any(re.search(p, low) for p in pats):
            missing.append(label)
    if missing:
        failures.append("missing required craft elements: " + ", ".join(missing))

    # --- identity set derived, not defaulted (decision) ---
    # The craft strings above can all be present while every character still
    # has the same face. These anchors are what the CRAFT check cannot see.
    missing_id = []
    for label, pats in IDENTITY_ANCHORS.items():
        if not any(re.search(p, low) for p in pats):
            missing_id.append(label)
    if missing_id:
        failures.append(
            "identity set not derived — no anchoring value or proportion band found: "
            + ", ".join(missing_id)
            + " (see bank/face.md §2A)"
        )
    else:
        notes.append("identity set: anchoring face value and proportion band both present")

    # --- --no policy ---
    no_match = re.search(r"--no\s+([^\n]+)", raw)
    if no_match:
        words_in_no = [w.strip(" ,.") for w in no_match.group(1).split(",")]
        bad = [w for w in words_in_no if w.lower() in NO_FORBIDDEN]
        if bad:
            failures.append(f"--no contains forbidden terms: {', '.join(bad)}")
        multi = [w for w in words_in_no if len(w.split()) > 1]
        if multi:
            failures.append(f"--no has multi-word entries: {', '.join(multi)}")
        notes.append(f"--no entries: {len(words_in_no)}")

    # --- palette token frequencies ---
    roles = parse_palette(raw) if args.palette else {}
    if roles:
        caps = CAPS[args.register]
        for role, terms in roles.items():
            total = sum(count_term(low, t) for t in terms)
            cap = caps.get(role)
            status = "ok" if cap is None or total <= cap else "OVER"
            notes.append(f"colour {role}: {total} (cap {cap}) [{status}] for {terms}")
            if status == "OVER":
                failures.append(f"colour {role} over cap: {total} > {cap} ({terms})")
        base = sum(count_term(low, t) for t in roles.get("base", []))
        accent = sum(count_term(low, t) for t in roles.get("accent", []))
        if accent and base < accent * 2:
            failures.append(f"base barely outnumbers accent: base {base} vs accent {accent}")
    else:
        notes.append("palette roles not declared; pass --palette with base/anchor/accent lines")

    # --- generic frequency table, so the numbers are visible either way ---
    colourish = ["white", "bone", "pearl", "ivory", "silver", "gold", "black",
                 "crimson", "cinnabar", "oxblood", "celadon", "jade", "rust",
                 "violet", "grey", "gray", "cyan", "amber"]
    materialish = ["silk", "organza", "gauze", "jacquard", "filigree", "lace",
                   "velvet", "satin", "wool", "linen", "leather", "chiffon",
                   "brocade", "crystal", "bronze", "lacquer"]
    freq = sorted(((t, count_term(low, t)) for t in colourish + materialish if count_term(low, t)),
                  key=lambda x: -x[1])

    # --- structural counts the prompt can reveal ---
    layers = re.search(r"\b(three|four|five|six|seven)\s+(?:visible\s+)?layers\b", low)
    # Node counts are written as digits in the blueprint and as a count in prose.
    # Matching "shaped node" (as the old \b(\w+)\s+nodes?\b did) reports a false
    # clause; require a number or a count word.
    nodes = re.search(r"\b(\d+|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|fifteen)\s+(?:ornament\s+)?nodes\b", low)
    if layers:
        notes.append(f"layer clause: {layers.group(0)}")
    if nodes:
        notes.append(f"node clause: {nodes.group(0)}")
    else:
        notes.append("node clause: no explicit node count in the prompt (count it from the blueprint)")

    # --- batch differentiation against the ledger ---
    differ, ledger_fail = [], []
    if args.ledger:
        try:
            rows = read_ledger(args.ledger)
        except OSError as exc:
            ledger_fail.append(f"ledger unreadable: {exc}")
            rows = []
        if not rows:
            notes.append("ledger supplied but holds no rows; this is the first character")
        else:
            # The blueprint's declared vector always wins. A prompt-derived
            # vector can only see the axes that were written into prose, so
            # diffing on it under-reports and would fail a compliant design.
            declared = args.vector
            if declared:
                vector, source = parse_vector(declared), "declared (--vector)"
            else:
                vector, source = ledger_vector_from_prompt(low), "derived from prompt"
            comparable = [i for i, v in enumerate(vector) if v]
            notes.append(f"batch vector [{source}]: " + " · ".join(
                f"{LEDGER_AXES[i]}={vector[i]}" for i in comparable))
            if not args.vector:
                notes.append(
                    f"only {len(comparable)}/{len(LEDGER_AXES)} axes are visible in the prompt; "
                    "pass --vector from the blueprint to check the full nine"
                )
            for name, row in rows:
                res = compare_vector(vector, row)
                differ.append(
                    f"vs {name}: {res['different']}/{res['comparable']} comparable axes differ"
                    + (f" — SAME mandatory {', '.join(res['same_mandatory'])}" if res["same_mandatory"] else ""))
                if res["same_mandatory"]:
                    ledger_fail.append(
                        f"batch: {name} shares a mandatory axis ({', '.join(res['same_mandatory'])})")
                # The five-of-nine rule is stated over nine axes. Apply it only
                # when all nine were actually declared, otherwise require every
                # comparable axis to differ and say the rest is unchecked.
                need = LEDGER_MIN_DIFFERENT if args.vector else res["comparable"]
                if res["comparable"] and res["different"] < need:
                    ledger_fail.append(
                        f"batch: {name} differs on {res['different']}/{res['comparable']} comparable axes, "
                        f"needs {need}")
    else:
        notes.append("no --ledger supplied; batch differentiation not checked")

    failures.extend(ledger_fail)
    return failures, notes, freq, nwords, differ


def parse_vector(text):
    """Read a declared batch vector, nine axes in LEDGER_AXES order."""
    parts = [p.strip().lower() for p in re.split(r"[·|,;]", text) if p.strip()]
    return (parts + [""] * len(LEDGER_AXES))[: len(LEDGER_AXES)]


def read_ledger(path):
    """Read a batch ledger written to the format in contract/records.md §8.

    A row is `<name> | axis · axis · ...` with the nine axes in LEDGER_AXES
    order. Blank lines, the header word, and prose are ignored.
    """
    rows = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if "|" not in line:
                continue
            name, _, rest = line.partition("|")
            name = name.strip().lstrip("-* ").strip()
            if not name or name.lower().startswith("批次账本"):
                continue
            parts = [p.strip().lower() for p in re.split(r"[·|]", rest) if p.strip()]
            if len(parts) < 2:
                continue
            rows.append((name, parts))
    return rows


def ledger_vector_from_prompt(low):
    """Detect the axes a finished prompt actually declares, so it can be diffed.

    Only axes with a detectable marker are filled; an undetected axis is left
    empty and is not counted as a difference, because the script cannot read a
    design intent that was never written down.
    """
    sil = [("cocoon", r"cocoon|uncinched oversized"), ("column", r"\bcolumn\b|narrow vertical"),
           ("bell", r"bell silhouette|a-line"), ("trapeze", r"trapeze"),
           ("hourglass", r"hourglass"), ("asymmetric", r"asymmetric silhouette")]
    topo = [("top-peak", r"top-peak|crown, hair and chest|density sits high"),
            ("bottom", r"bottom-anchored|heavy drapery from the hip"),
            ("single-side", r"single-side|diagonal architectural cut"),
            ("languid", r"languid|negative space"),
            ("bone", r"bone-sculpted|spinal axis")]
    light = [("high-key", r"high-key|pearlescent"), ("chiaroscuro", r"chiaroscuro|side-back key"),
             ("warm-gi", r"warm directional global illumination|warm tactile"),
             ("overcast", r"overcast diffuse|diffuse mist")]
    key = [("bone", r"\bbone\b|\bivory\b"), ("obsidian", r"obsidian|blue-black"),
           ("celadon", r"celadon|\bjade\b"), ("cinnabar", r"cinnabar|oxblood|iron rust"),
           ("glacier", r"glacier|titanium"), ("pearl", r"\bpearl\b|\bsilver\b")]

    def first(table):
        for label, pat in table:
            if re.search(pat, low):
                return label
        return ""
    return [first(sil), first(key), first(topo), "", "", first(light), "", "", ""]


def compare_vector(vector, row):
    """Diff a detected vector against one ledger row on the axes both declare."""
    differing, same_mandatory, comparable = 0, [], 0
    for i, mine in enumerate(vector):
        if not mine or i >= len(row) or not row[i]:
            continue
        comparable += 1
        theirs = row[i]
        if mine not in theirs and theirs not in mine:
            differing += 1
        elif i in LEDGER_MANDATORY:
            same_mandatory.append(LEDGER_AXES[i])
    return {"different": differing, "comparable": comparable, "same_mandatory": same_mandatory}


def main():
    ap = argparse.ArgumentParser(description="Mechanical half of the design preflight.")
    ap.add_argument("path", help="file containing the prompt")
    ap.add_argument("--register", default="editorial",
                    choices=["editorial", "glamour", "compact", "portrait", "scene"])
    ap.add_argument("--palette", action="store_true",
                    help="also read base/anchor/accent lines from the file and check caps")
    ap.add_argument("--ledger", default=None,
                    help="batch ledger file; check this character's axes against it (records.md §8)")
    ap.add_argument("--vector", default=None,
                    help="this character's nine-axis vector from the blueprint, '·'-separated; "
                         "give it whenever --ledger is used so all nine axes are checked")
    ap.add_argument("--budget", default=None, help="override the upper word budget")
    args = ap.parse_args()

    if args.budget:
        BUDGET[args.register] = (0, int(args.budget))

    failures, notes, freq, nwords, differ = check(args)

    print("=" * 62)
    print(f"PREFLIGHT  {args.path}  [{args.register}]")
    print("=" * 62)
    print("\nCounted:")
    for n in notes:
        print("  " + n)
    if differ:
        print("\nBatch differentiation (gates.md §9):")
        for d in differ:
            print("  " + d)
    if freq:
        print("\nTerm frequencies (colour and material):")
        for term, c in freq:
            flag = "  <-- check cap" if c > 5 else ""
            print(f"  {term:<12} {c}{flag}")
    print("\nJudged (not checked here — see design.md §6A):")
    print("  silhouette at 10% / value hierarchy / face wins / charm /")
    print("  commercial read / density gradient / no accidental clutter /")
    print("  whether the face is visibly a different person from the batch's last")
    if failures:
        print("\nFAILURES:")
        for f in failures:
            print("  - " + f)
        print()
        sys.exit(1)
    print("\nAll counted checks passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
