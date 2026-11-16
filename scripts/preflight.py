#!/usr/bin/env python3
"""Mechanical half of the design preflight.

Parses a finished English prompt and reports the checks that can be counted
and scanned mechanically:
  1. Word budget (prose words before engine flags)
  2. Colour and material term frequencies against role caps
  3. Banned fluff/review words, shader settings, and bare generic pose strings
  4. Required verbatim house craft elements (6 pillars)
  5. 4D Decision anchors:
     - D1 Bone geometry consequence & body proportion band
     - D2 Facial surface decision (iris optics, lip state, matte/specular zone)
     - D3 Orthographic static pose vector (weight axis + hand action + chin/gaze)
  6. Cliché N-gram trap detector (catches copied tear-moles, stock combos, and
     genre reflexes unless explicitly permitted via --allow-cliche)
  7. 10-Axis batch differentiation against a project ledger (or Mode C variant
     integrity with --variant-of and --inherit)
  8. Cross-cast non-craft lexical overlap (--compare-prompt): strips invariant
     house craft/layout boilerplate and fails if two characters share > 28% of
     their non-craft design vocabulary.

It does not judge silhouette readability at 10%, grayscale Notan hierarchy,
whether the face wins, or whether the Adversarial Critique (Swap Test) is
honest. See references/pipeline/design.md §6 and engine/04-critique-and-repair.md.

Usage:
    python -I scripts/preflight.py prompt.txt --register editorial
    python -I scripts/preflight.py prompt.txt --register glamour --palette
    python -I scripts/preflight.py prompt.txt --register glamour \
        --ledger batch.txt \
        --vector "asymmetric · 玄黑+幽冥紫黑 · topology 3 单侧异化 · editorial gear 2 · dir1/墨玉指尖与乌金护指 · 明暗伦勃朗侧逆 · 乌金掐丝包边 · 幽冥骨铃脊椎纹 · 面部指数1.48+深渊血珀瞳+眼尾魔纹 · 重心落右腿+左手搭腰玉+微抬下巴垂眸"
    python -I scripts/preflight.py prompt2.txt --register editorial \
        --compare-prompt prompt1.txt
"""

import argparse
import re
import sys

# Caps from references/atlas/lexicon.md §5.3 and pipeline/design.md §6.
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
    "gravity topology", "design evidence", "neutral balanced stance",
]

BANNED_NUMERIC = [
    (r"(?<![A-Za-z0-9])8k(?![A-Za-z0-9])", "8k"),
    (r"(?<![A-Za-z0-9])4k(?![A-Za-z0-9])", "4k"),
]

# Engine settings that do not belong in an image prompt.
SHADER = ["roughness", "metallic 1", "ior 1", "sss radius", "specular 0"]

# Terms forbidden in Midjourney --no, from contract/visual.md §11.
NO_FORBIDDEN = ["doll", "seams", "skin", "figure"]

# House CRAFT strings: shared by every character, reused verbatim.
# See contract/visual.md §5 and contract/gates.md §8.
IDENTITY_REQUIRED = {
    "anime eye design": [r"upper lid", r"\bcrease\b", r"iris"],
    "second catchlight": [r"secondary reflection|second catchlight|two catchlight"],
    "porcelain skin": [r"porcelain"],
    "hair clumps": [r"strand clump|sculpted lock|grouped lock"],
    "one key direction": [r"\bkey\b.*(left|right)|from the (left|right|front-left|front-right)|side-back|overhead"],
}

# 4D Decision Anchors: proves that Bone (D1), Proportion (D1), Surface (D2),
# and Orthographic Pose (D3) were each explicitly stated as consequences in prose.
IDENTITY_ANCHORS = {
    "D1 bone geometry anchor (facial index / mouth width / eye spacing / jaw / cheekbone)": [
        r"slender tapered oval face", r"compact heart-shaped face", r"long narrow face",
        r"broad short face", r"delicately proportioned mouth", r"narrow mouth",
        r"wide mobile mouth", r"expressive mouth", r"sharply focused almond eyes",
        r"close-set", r"widely spaced", r"wide-set", r"tapered v-shaped chin",
        r"tapered chin", r"pointed chin", r"chiseled resolute chin", r"square chin",
        r"high sculpted cheekbone", r"high flat cheekbone", r"smoothly contoured cheek",
        r"low soft cheekbone",
    ],
    "D1 body proportion band": [
        r"7-to-7\.5-head", r"7\.5-to-8-head", r"8-to-8\.5-head", r"8\.5-head", r"\d(\.\d)?[- ]head",
    ],
    "D2 facial surface decision (specific iris optics + lip state + matte/specular zone)": [
        r"[a-z-]+ irises with radial fibre",
        r"matte cheek|specular break|specular line|velvet-matte|pearl-sheen",
    ],
    "D3 orthographic static pose (explicit weight axis + empty-hand action + chin/gaze)": [
        r"weight (?:on|planted|shifted|settled|forward|locked|cocked|across)",
    ],
}

POSE_COMPONENTS = {
    "weight axis": [r"weight (?:on|planted|shifted|settled|forward|locked|cocked|across)"],
    "empty-hand action": [
        r"\bhand\b", r"\bhands\b", r"\bthumb\b", r"\bfingers\b", r"\bpalms?\b",
        r"clasped", r"tucked into", r"hooked in",
    ],
    "chin & gaze": [r"\bchin\b", r"\bgaze\b"],
}

# Cliché N-gram traps: catches reflexive stock combinations and genre training means.
CLICHE_TRAPS = [
    ("under-eye mole reflex (tear-mole / mole beneath eye)",
     r"tear-mole|mole beneath (?:her|his|the|one) (?:left |right )?eye|tiny mole under one eye"),
    ("stock lotus-thorn reflex (ruby-glass irises + thorns through lotus silk)",
     r"ruby-glass irises.*lotus|thorns grown through water-stained lotus"),
    ("stock starflower-filigree reflex (snow-crowned + starflower silver filigree)",
     r"snow-crowned.*starflower|starflower.*narrow silver filigree"),
    ("default pose reflex (weight on left leg, shoulders uneven, right hand loose)",
     r"weight on the left leg, shoulders slightly uneven, right hand loose at (?:her|his) side"),
    ("mundane peasant/butcher downgrade trap (rawhide/surgical apron or tarred oilskin)",
     r"surgical apron|rawhide apron|butcher apron|tarred oilskin"),
]

# Boilerplate house craft & sheet layout words excluded when computing
# cross-cast non-craft lexical overlap (--compare-prompt).
CRAFT_STOPWORDS = {
    "the", "and", "with", "from", "that", "this", "into", "over", "under", "across",
    "through", "between", "where", "while", "only", "both", "each", "every", "same",
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "character", "concept", "design", "sheet", "seamless", "background", "premium",
    "game", "render", "semi", "realistic", "shading", "hand", "authored", "material",
    "response", "refined", "anime", "facial", "fused", "high", "grade", "bjd",
    "porcelain", "quality", "sculptural", "surface", "relief", "commercial",
    "animation", "art", "direction", "studio", "lighting", "soft", "directional",
    "key", "front", "left", "right", "broad", "bounce", "fill", "clean", "rim",
    "separation", "grounded", "contact", "shadow", "zone", "borderless", "full",
    "body", "view", "views", "facing", "pure", "degree", "side", "profile", "back",
    "orthographic", "shared", "ground", "line", "identical", "scale", "standing",
    "head", "toe", "uncropped", "thin", "grid", "bust", "cells", "cell", "top",
    "bottom", "symmetrical", "fully", "neutral", "baseline", "face", "quarter",
    "slight", "tilt", "gaze", "tight", "macro", "eyes", "nose", "lips", "crown",
    "shoulders", "deliberately", "cropped", "out", "carrying", "large", "almond",
    "defined", "upper", "lid", "clear", "double", "crease", "tapered", "inner",
    "outer", "corners", "irises", "radial", "fibre", "darker", "limbal", "ring",
    "glassy", "depth", "bright", "secondary", "reflection", "wet", "lower",
    "meniscus", "minimal", "bridge", "visible", "cupid", "bow", "smooth", "skin",
    "subsurface", "glow", "grouped", "locks", "sculpted", "strand", "clumps",
    "style", "highlight", "band", "individual", "flyaway", "strands", "catching",
    "light", "identical", "costume", "construction", "seam", "placement", "hair",
    "streaks", "markings", "repeated", "consistently", "throughout", "panels",
    "empty", "hands", "proportion", "slender", "frame", "waist", "hips", "neck",
    "chin", "mouth", "cheekbones", "jaw", "brows", "brow", "layers", "layer",
    "edges", "edge", "collar", "cuffs", "cuff", "hem", "hems", "placket", "belt",
    "skirt", "sleeves", "sleeve", "cloth", "fabric", "centimetres", "millimetres",
    "tone", "repeat", "field", "macro", "mid", "micro", "jeweller", "fittings",
}

# The ten batch axes from contract/gates.md §9.
LEDGER_AXES = [
    "silhouette", "key colour", "topology", "register+gear",
    "contradiction", "light", "trim", "motif", "face anchor", "pose vector",
]
LEDGER_MANDATORY = {0, 1}       # silhouette, key colour must differ from EVERY row
LEDGER_ADJACENT_MANDATORY = {8, 9}  # face anchor and pose vector must differ from previous
LEDGER_MIN_DIFFERENT_10 = 6
LEDGER_MIN_DIFFERENT_9 = 5

# Mode C looks: contract/gates.md §9A.
LOOK_AXES = ["topology", "trim", "motif", "node distribution"]
LOOK_MIN_DIFFERENT = 3
LOOK_AXES_CAST = ["silhouette", "key colour"]


def strip_prompt(text):
    """Return the prompt body, dropping fences, trailing parameters, and headings."""
    text = text.replace("\r\n", "\n")
    blocks = re.findall(r"```(?:text|txt|markdown)?\n(.*?)```", text, re.S)
    if blocks:
        text = max(blocks, key=len)
    text = re.split(r"\s--(?:ar|raw|s|hd|no|style|niji)\b", text)[0]
    return text.strip()


def words(text):
    return re.findall(r"[A-Za-z][A-Za-z'-]*", text)


def count_term(low, term):
    return len(re.findall(r"\b" + re.escape(term) + r"\b", low))


def parse_palette(text):
    roles = {}
    for role in ("base", "anchor", "accent"):
        m = re.search(rf"{role}\s*[:=]\s*([^\n;/|]+)", text, re.I)
        if m:
            roles[role] = [t.strip().lower() for t in re.split(r"[,+]", m.group(1)) if t.strip()]
    return roles


def design_vocab(prompt_text):
    """Extract non-craft design words (length >= 4) from a prompt."""
    tokens = [w.lower().strip("'-") for w in words(prompt_text)]
    return {t for t in tokens if len(t) >= 4 and t not in CRAFT_STOPWORDS}


def check(args):
    raw = open(args.path, encoding="utf-8").read()
    prompt = strip_prompt(raw)
    low = prompt.lower()
    nwords = len(words(prompt))
    failures, notes = [], []

    # --- 1. word budget ---
    lo, hi = BUDGET[args.register]
    if hi and not (lo <= nwords <= hi):
        failures.append(f"word budget: {nwords} words, expected {lo}-{hi}")
    else:
        notes.append(f"word count: {nwords} (budget {lo}-{hi})")

    # --- 2. banned words & bare neutral pose ---
    hits = [b for b in BANNED if re.search(r"\b" + re.escape(b) + r"\b", low)]
    numeric_hits = [label for pat, label in BANNED_NUMERIC if re.search(pat, low)]
    if hits or numeric_hits:
        failures.append("banned words / generic pose: " + ", ".join(hits + numeric_hits))

    # --- 3. shader parameters ---
    shader = [s for s in SHADER if s in low]
    if shader:
        failures.append("engine settings in prompt: " + ", ".join(shader))

    # --- 4. required house craft elements ---
    missing = []
    for label, pats in IDENTITY_REQUIRED.items():
        if not any(re.search(p, low) for p in pats):
            missing.append(label)
    if missing:
        failures.append("missing required craft elements: " + ", ".join(missing))

    # --- 5. 4D decision anchors (Bone, Proportion, Surface, Pose) ---
    missing_id = []
    for label, pats in IDENTITY_ANCHORS.items():
        if not any(re.search(p, low) for p in pats):
            missing_id.append(label)
    missing_pose = [
        comp for comp, pats in POSE_COMPONENTS.items()
        if not any(re.search(p, low) for p in pats)
    ]
    if missing_pose and args.register not in ("scene",):
        failures.append(
            "orthographic pose vector incomplete — missing: "
            + ", ".join(missing_pose)
            + " (see engine/01-truth-and-pose.md §7)"
        )
    if missing_id and args.register not in ("scene",):
        failures.append(
            "4D derivation incomplete — missing in prose: "
            + "; ".join(missing_id)
            + " (see engine/02-face-derivation.md §1A & §1B)"
        )
    elif args.register not in ("scene",):
        notes.append("4D derivation anchors: Bone (§1A), Proportion, Surface (§1B), and Pose Vector all present")

    # --- 6. Cliché N-gram trap detector ---
    if not args.allow_cliche:
        traps_hit = [label for label, pat in CLICHE_TRAPS if re.search(pat, low, re.S)]
        if traps_hit:
            failures.append(
                "cliché trap triggered: " + "; ".join(traps_hit)
                + " (pass --allow-cliche only if explicitly requested by user)"
            )
        else:
            notes.append("cliché scan: zero stock N-gram traps triggered")

    # --- 7. --no policy ---
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

    # --- 8. palette token frequencies ---
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

    colourish = ["white", "bone", "pearl", "ivory", "silver", "gold", "black",
                 "crimson", "cinnabar", "oxblood", "celadon", "jade", "rust",
                 "violet", "grey", "gray", "cyan", "amber", "ochre", "umber",
                 "verdigris", "azurite", "malachite", "sulfur", "bronze", "pewter",
                 "plum", "agate", "vermilion", "wisteria", "obsidian"]
    materialish = ["silk", "organza", "gauze", "jacquard", "filigree", "lace",
                   "velvet", "satin", "wool", "linen", "leather", "chiffon",
                   "brocade", "crystal", "bronze", "lacquer", "damask", "tulle",
                   "obsidian", "horn", "ceramic", "iron", "steel"]
    freq = sorted(((t, count_term(low, t)) for t in dict.fromkeys(colourish + materialish) if count_term(low, t)),
                  key=lambda x: -x[1])
    if args.register in CAPS:
        mat_cap = CAPS[args.register]["material"]
        over_mat = [f"{t} ({count_term(low, t)})" for t in materialish if count_term(low, t) > mat_cap]
        if over_mat:
            failures.append(f"material term over cap ({mat_cap}): {', '.join(over_mat)}")

    # --- 9. structural counts in prompt ---
    layers = re.search(r"\b(two|three|four|five|six|seven)\s+(?:visible\s+)?layers\b", low)
    nodes = re.search(r"\b(\d+|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|fifteen)\s+(?:ornament\s+)?nodes\b", low)
    if layers:
        notes.append(f"layer clause: {layers.group(0)}")
    if nodes:
        notes.append(f"node clause: {nodes.group(0)}")
    else:
        notes.append("node clause: no explicit 'N nodes' phrase in prose (verify count in blueprint point 5)")

    # --- 10. Cross-cast non-craft lexical overlap (--compare-prompt) ---
    if args.compare_prompt:
        mine_vocab = design_vocab(prompt)
        for other_path in args.compare_prompt:
            try:
                other_raw = open(other_path, encoding="utf-8").read()
            except OSError as exc:
                failures.append(f"compare-prompt unreadable ({other_path}): {exc}")
                continue
            other_vocab = design_vocab(strip_prompt(other_raw))
            union = mine_vocab | other_vocab
            shared = sorted(mine_vocab & other_vocab)
            jaccard = (len(shared) / len(union)) if union else 0.0
            pct = jaccard * 100.0
            notes.append(
                f"non-craft lexical overlap vs {other_path}: {pct:.1f}% "
                f"({len(shared)}/{len(union)} design words; cap {args.max_overlap:.0f}%)"
            )
            if pct > args.max_overlap:
                sample = ", ".join(shared[:18])
                failures.append(
                    f"lexical overlap too high vs {other_path}: {pct:.1f}% > {args.max_overlap:.0f}% "
                    f"(shared design terms: {sample})"
                )

    # --- 11. 10-Axis batch differentiation or Mode C variant integrity ---
    differ, ledger_fail = [], []
    if args.variant_of:
        differ, ledger_fail = check_variant(args, low, notes)
    elif args.ledger:
        try:
            cast, _variants = read_ledger(args.ledger)
        except OSError as exc:
            ledger_fail.append(f"ledger unreadable: {exc}")
            cast = []
        if not cast:
            notes.append("ledger supplied but holds no cast rows; this is the first character")
        else:
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
                    "pass --vector from the blueprint to check all ten axes"
                )
            for idx, (name, row) in enumerate(cast):
                is_adjacent = (idx == len(cast) - 1)
                res = compare_vector(vector, row)
                differ.append(
                    f"vs {name}: {res['different']}/{res['comparable']} comparable axes differ"
                    + (f" — SAME mandatory {', '.join(res['same_mandatory'])}" if res["same_mandatory"] else "")
                    + (f" — SAME adjacent {', '.join(res['same_adjacent'])}" if is_adjacent and res["same_adjacent"] else "")
                )
                if res["same_mandatory"]:
                    ledger_fail.append(
                        f"batch: {name} shares a mandatory axis ({', '.join(res['same_mandatory'])})")
                if is_adjacent and res["same_adjacent"]:
                    ledger_fail.append(
                        f"batch: adjacent character {name} shares face/pose axis ({', '.join(res['same_adjacent'])})")
                if args.vector:
                    need = LEDGER_MIN_DIFFERENT_10 if res["comparable"] >= 10 else LEDGER_MIN_DIFFERENT_9
                else:
                    need = res["comparable"]
                if res["comparable"] and res["different"] < need:
                    ledger_fail.append(
                        f"batch: {name} differs on {res['different']}/{res['comparable']} comparable axes, "
                        f"needs {need}")
            notes.append(
                "mode: cast (Mode A/B) — axes 1-2 binding across cast, axes 9-10 binding against adjacent. "
                "For a costume variant, pass --variant-of <name>; see gates.md §9A"
            )
    else:
        notes.append("no --ledger supplied; batch differentiation not checked")

    failures.extend(ledger_fail)
    return failures, notes, freq, nwords, differ


def check_variant(args, low, notes):
    """Variant integrity for a second look on an existing character (gates.md §9A)."""
    differ, fails = [], []
    parent = args.variant_of.strip()
    try:
        cast, variants = read_ledger(args.ledger) if args.ledger else ([], [])
    except OSError as exc:
        return [], [f"ledger unreadable: {exc}"]

    notes.append(f"mode: variant (Mode C) of {parent} — axes 1-2 exempt, look separation applies")

    has_identity = any(
        re.search(p, low)
        for pats in IDENTITY_ANCHORS["D1 bone geometry anchor (facial index / mouth width / eye spacing / jaw / cheekbone)"]
        for p in [pats]
    )
    if not has_identity:
        fails.append(
            "variant: no identity anchoring value found — a variant must restate the "
            "record's identity block verbatim (engine/02-face-derivation.md §1A scope)"
        )
    else:
        notes.append("identity integrity: identity block present (values must match the record verbatim)")

    parent_row = next((row for name, row in cast if name.strip().lower() == parent.lower()), None)
    if parent_row is None:
        notes.append(
            f"variant: {parent} not found in the ledger cast rows — inherited silhouette and "
            "key colour cannot be verified; add the character's cast row first"
        )
    elif len(parent_row) >= 2:
        mine = [lexical_family(parent_row[0], low), lexical_family(parent_row[1], low)]
        if args.inherit:
            stated = ["present" if ok else "absent" for ok in mine]
            differ.append(
                f"inherited axes vs {parent}: silhouette {stated[0]}, key colour {stated[1]} "
                f"(ledger: {parent_row[0]} / {parent_row[1]})"
            )
            changed = [LOOK_AXES_CAST[i] for i, ok in enumerate(mine) if not ok]
            if changed:
                fails.append(
                    "variant: silhouette or key colour differs from "
                    f"{parent} ({', '.join(changed)}). A variant inherits both by default (gates.md §9A)"
                )
        else:
            notes.append(
                "variant: pass --inherit to also verify silhouette and key colour still match "
                f"{parent} ({parent_row[0]} / {parent_row[1]})"
            )

    look = parse_look_vector(args.vector)
    if not look:
        fails.append(
            "variant: no look vector — pass --vector \"topology · trim · motif · nodes\" "
            "so look separation can be checked (gates.md §9A)"
        )
        return differ, fails

    baseline = variant_baseline(parent, cast, variants)
    if baseline is None:
        notes.append(f"variant: no previous look recorded for {parent}; look separation not comparable")
        return differ, fails

    for label, prior in baseline:
        res = compare_look(look, prior)
        differ.append(f"vs {label}: {res['different']}/{res['comparable']} look factors differ")
        if res["comparable"] < LOOK_MIN_DIFFERENT:
            notes.append(
                f"  only {res['comparable']} look factors comparable against {label}; "
                f"{LOOK_MIN_DIFFERENT} of four is the rule — record the missing factor"
            )
        if res["different"] < LOOK_MIN_DIFFERENT:
            fails.append(
                f"variant: {label} differs on {res['different']}/{res['comparable']} look factors, "
                f"needs {LOOK_MIN_DIFFERENT} of four ({', '.join(LOOK_AXES)})"
            )
    return differ, fails


FAMILY_SYNONYMS = {
    "cocoon": ["cocoon", "uncinched", "松弛", "茧"],
    "column": ["column", "narrow vertical", "立柱", "直筒"],
    "bell": ["bell", "a-line", "钟形", "伞"],
    "trapeze": ["trapeze", "梯形"],
    "hourglass": ["hourglass", "沙漏"],
    "asymmetric": ["asymmetric", "不对称"],
    "bone-white": ["bone", "ivory", "pearl", "chalk", "oyster", "骨白", "象牙", "珠白"],
    "obsidian": ["obsidian", "blue-black", "lampblack", "iron-black", "黑曜", "墨黑"],
    "celadon": ["celadon", "jade", "青瓷", "玉青"],
    "cinnabar": ["cinnabar", "oxblood", "rust", "madder", "朱砂", "铁锈"],
    "glacier": ["glacier", "titanium", "pewter", "冰川", "钛"],
    "earth-jewel": ["umber", "verdigris", "ochre", "earth", "土金", "铜绿", "赭"],
}


def lexical_family(needle, text):
    needle = (needle or "").strip().lower()
    if not needle:
        return True
    candidates = set()
    candidates.update(FAMILY_SYNONYMS.get(needle, []))
    for key, aliases in FAMILY_SYNONYMS.items():
        if needle == key or needle in aliases:
            candidates.add(key)
            candidates.update(aliases)
    candidates.add(needle)
    for token in re.split(r"[\s·/]+", needle):
        if len(token) >= 2:
            candidates.add(token)
            candidates.update(FAMILY_SYNONYMS.get(token, []))
    return any(c and c in text for c in candidates)


def parse_look_vector(text):
    if not text:
        return []
    parts = [p.strip().lower() for p in re.split(r"[·|,;]", text) if p.strip()]
    return (parts + [""] * len(LOOK_AXES))[: len(LOOK_AXES)]


def variant_baseline(parent, cast, variants):
    out = []
    for name, row in cast:
        if name.strip().lower() == parent.lower():
            look = ["", "", "", ""]
            if len(row) > 2:
                look[0] = row[2]
            if len(row) > 6:
                look[1] = row[6]
            if len(row) > 7:
                look[2] = row[7]
            out.append((f"{name}（正装）", look))
    for label, par, look in variants:
        if par.strip().lower() == parent.lower():
            out.append((label, look))
    return out or None


def compare_look(look, prior):
    differing, comparable = 0, 0
    for i, mine in enumerate(look):
        if not mine or i >= len(prior) or not prior[i]:
            continue
        comparable += 1
        theirs = prior[i]
        if mine not in theirs and theirs not in mine:
            differing += 1
    return {"different": differing, "comparable": comparable}


def parse_vector(text):
    """Read a declared batch vector (up to 10 axes in LEDGER_AXES order)."""
    parts = [p.strip().lower() for p in re.split(r"[·|,;]", text) if p.strip()]
    return (parts + [""] * len(LEDGER_AXES))[: len(LEDGER_AXES)]


def read_ledger(path):
    """Read a 10-axis (or 9-axis) batch ledger written per contract/records.md §8."""
    cast, variants = [], []
    parent = None
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if "|" not in line:
                continue
            raw_name, _, rest = line.partition("|")
            name = raw_name.strip().lstrip("-* \t").strip()
            if not name or name.lower().startswith("批次账本") or name.lower().startswith("[角色"):
                continue
            parts = [p.strip().lower() for p in re.split(r"[·|]", rest) if p.strip()]
            if len(parts) < 2:
                continue

            is_variant = raw_name.strip().startswith("↳")
            if is_variant:
                label = name.lstrip("↳").strip()
                look = parse_variant_look(parts)
                variants.append((label, parent or "", look))
            else:
                cast.append((name, parts))
                parent = name
    return cast, variants


def parse_variant_look(parts):
    look = ["", "", "", ""]
    for clause in parts:
        if "identity locked" in clause or "identity" in clause:
            continue
        if look[0] == "" and ("topology" in clause):
            look[0] = clause
        elif look[1] == "" and ("trim" in clause or "压边" in clause or "镶边" in clause or "包边" in clause or "滚边" in clause):
            look[1] = clause
        elif look[2] == "" and ("motif" in clause or "花" in clause or "纹" in clause or "刻度" in clause or "裂纹" in clause):
            look[2] = clause
        elif look[3] == "" and ("node" in clause or "节点" in clause):
            look[3] = clause
    return look


def ledger_vector_from_prompt(low):
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
    key = [("bone", r"\bbone\b|\bivory\b|\bchalk\b"), ("obsidian", r"obsidian|blue-black|lampblack|iron-black"),
           ("celadon", r"celadon|\bjade\b"), ("cinnabar", r"cinnabar|oxblood|iron rust"),
           ("glacier", r"glacier|titanium|pewter"), ("earth-jewel", r"\bumber\b|\bochre\b|\bverdigris\b"),
           ("pearl", r"\bpearl\b|\bsilver\b")]
    pose = re.search(r"weight (?:on|planted|shifted|settled|forward|locked)[^.,;]+", low)

    def first(table):
        for label, pat in table:
            if re.search(pat, low):
                return label
        return ""
    return [first(sil), first(key), first(topo), "", "", first(light), "", "", "", pose.group(0) if pose else ""]


def compare_vector(vector, row):
    differing, same_mandatory, same_adjacent, comparable = 0, [], [], 0
    for i, mine in enumerate(vector):
        if not mine or i >= len(row) or not row[i]:
            continue
        comparable += 1
        theirs = row[i]
        if mine not in theirs and theirs not in mine:
            differing += 1
        else:
            if i in LEDGER_MANDATORY:
                same_mandatory.append(LEDGER_AXES[i])
            if i in LEDGER_ADJACENT_MANDATORY:
                same_adjacent.append(LEDGER_AXES[i])
    return {
        "different": differing,
        "comparable": comparable,
        "same_mandatory": same_mandatory,
        "same_adjacent": same_adjacent,
    }


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Mechanical half of the design preflight.")
    ap.add_argument("path", help="file containing the prompt")
    ap.add_argument("--register", default="editorial",
                    choices=["editorial", "glamour", "compact", "portrait", "scene"])
    ap.add_argument("--palette", action="store_true",
                    help="also read base/anchor/accent lines from the file and check caps")
    ap.add_argument("--ledger", default=None,
                    help="batch ledger file; check this character's 10-axis vector against it (records.md §8)")
    ap.add_argument("--variant-of", dest="variant_of", default=None, metavar="NAME",
                    help="Mode C: second look for character NAME; checks identity integrity + look separation (gates.md §9A)")
    ap.add_argument("--inherit", action="store_true",
                    help="Mode C: verify silhouette and key colour still match the parent character (gates.md §9A)")
    ap.add_argument("--vector", default=None,
                    help="this character's 10-axis vector from the blueprint, '·'-separated "
                         "(or 4 look factors with --variant-of)")
    ap.add_argument("--compare-prompt", dest="compare_prompt", action="append", default=[],
                    metavar="PROMPT_FILE",
                    help="compare non-craft design vocabulary against a prior character's prompt (repeatable)")
    ap.add_argument("--max-overlap", dest="max_overlap", type=float, default=28.0,
                    help="max allowed non-craft Jaccard lexical overlap percentage (default: 28%%)")
    ap.add_argument("--allow-cliche", dest="allow_cliche", action="store_true",
                    help="suppress cliché N-gram trap failures when user explicitly requested a trope")
    ap.add_argument("--budget", default=None, help="override the upper word budget")
    args = ap.parse_args()

    if args.budget:
        BUDGET[args.register] = (0, int(args.budget))

    failures, notes, freq, nwords, differ = check(args)

    print("=" * 66)
    print(f"PREFLIGHT  {args.path}  [{args.register}]")
    print("=" * 66)
    print("\nCounted & Scanned:")
    for n in notes:
        print("  " + n)
    if differ:
        print("\nBatch differentiation (gates.md §9 — 10 axes):")
        for d in differ:
            print("  " + d)
    if freq:
        print("\nTerm frequencies (colour and material):")
        for term, c in freq:
            flag = "  <-- check cap" if c > 5 else ""
            print(f"  {term:<12} {c}{flag}")
    print("\nJudged & Adversarial Critique (required in delivery — see engine/04 §1):")
    print("  1. Generic Accusation vs Specific Rebuttal (3 drawable nouns)")
    print("  2. The Swap Test verdict (breaks if transplanted to a peer character)")
    print("  3. 10% silhouette / 70-25-5 Notan / face wins / density gradient")
    if failures:
        print("\nFAILURES:")
        for f in failures:
            print("  - " + f)
        print()
        sys.exit(1)
    print("\nAll mechanical & anti-cliché checks passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
