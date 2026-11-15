#!/usr/bin/env python3
"""Mechanical half of the design preflight.

Parses a finished English prompt and reports the checks that can be counted:
word budget, colour and material term frequencies against the role caps, banned
words, and whether the required identity elements are present.

It does not judge silhouette readability, value hierarchy, "face wins", charm,
or commercial read. Those need an eye. See references/pipeline/design.md §6A.

Usage:
    python -I preflight.py prompt.txt --register editorial
    python -I preflight.py prompt.txt --register glamour --blocks 18

Input may be a bare prompt or a fenced code block copied verbatim; fences and a
trailing --ar/--no suffix are stripped before counting.

Exit code is 0 when every counted check passes, 1 otherwise, so it can gate a
pipeline. Judged checks are never part of the exit code.
"""

import argparse
import re
import sys

# Caps from references/bank/aesthetic.md §3B and pipeline/design.md §6C/6D.
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

# Engine settings that do not belong in an image prompt.
SHADER = ["roughness", "metallic 1", "ior 1", "sss radius", "specular 0"]

# Terms forbidden in Midjourney --no, from contract/visual.md §11.
NO_FORBIDDEN = ["doll", "seams", "skin", "figure"]

# Elements the prompt must name, from contract/visual.md §5 and §8.
IDENTITY_REQUIRED = {
    "anime eye design": [r"upper lid", r"\bcrease\b", r"iris"],
    "second catchlight": [r"secondary reflection|second catchlight|two catchlight"],
    "porcelain skin": [r"porcelain"],
    "hair clumps": [r"strand clump|sculpted lock|grouped lock"],
    "one key direction": [r"\bkey\b.*(left|right)|from the (left|right)|side-back|overhead"],
}


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
    if hits:
        failures.append("banned words: " + ", ".join(hits))

    # --- shader parameters ---
    shader = [s for s in SHADER if s in low]
    if shader:
        failures.append("engine settings in prompt: " + ", ".join(shader))

    # --- required identity elements ---
    missing = []
    for label, pats in IDENTITY_REQUIRED.items():
        if not any(re.search(p, low) for p in pats):
            missing.append(label)
    if missing:
        failures.append("missing required elements: " + ", ".join(missing))

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
    layers = re.search(r"\b(three|four|five|six)\s+layers\b", low)
    nodes = re.search(r"\b(\w+)\s+nodes?\b", low)
    if layers:
        notes.append(f"layer clause: {layers.group(0)}")
    if nodes:
        notes.append(f"node clause: {nodes.group(0)}")

    return failures, notes, freq, nwords


def main():
    ap = argparse.ArgumentParser(description="Mechanical half of the design preflight.")
    ap.add_argument("path", help="file containing the prompt")
    ap.add_argument("--register", default="editorial",
                    choices=["editorial", "glamour", "compact", "portrait", "scene"])
    ap.add_argument("--palette", action="store_true",
                    help="also read base/anchor/accent lines from the file and check caps")
    ap.add_argument("--budget", default=None, help="override the upper word budget")
    args = ap.parse_args()

    if args.budget:
        BUDGET[args.register] = (0, int(args.budget))

    failures, notes, freq, nwords = check(args)

    print("=" * 62)
    print(f"PREFLIGHT  {args.path}  [{args.register}]")
    print("=" * 62)
    print("\nCounted:")
    for n in notes:
        print("  " + n)
    if freq:
        print("\nTerm frequencies (colour and material):")
        for term, c in freq:
            flag = "  <-- check cap" if c > 5 else ""
            print(f"  {term:<12} {c}{flag}")
    print("\nJudged (not checked here — see design.md §6A):")
    print("  silhouette at 10% / value hierarchy / face wins / charm /")
    print("  commercial read / density gradient / no accidental clutter")
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
