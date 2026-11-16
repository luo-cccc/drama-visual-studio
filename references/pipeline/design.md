# Pipeline: Design Mode

Read [../contract/visual.md](../contract/visual.md) and [../contract/gates.md](../contract/gates.md) first. This file owns the design-mode compiler: the 10-axis batch layer, the 4-dimension derivation stack, the IFV + 7-point blueprint, the content-free syntactic wireframe, and the dual acceptance gate (Counted Preflight + Adversarial Critique).

Derivation engines live in `../engine/`:
- Character truth, Thin-Brief compiler, and 4D pose vector: [../engine/01-truth-and-pose.md](../engine/01-truth-and-pose.md)
- Face bone geometry (§1A) and facial surface signifiers (§1B): [../engine/02-face-derivation.md](../engine/02-face-derivation.md)
- Conflict-to-seed compiler, IFV triple, and the 5 Craft Operators: [../engine/03-costume-and-craft.md](../engine/03-costume-and-craft.md)
- Adversarial critique, 12 generic autopsies, and drift repair: [../engine/04-critique-and-repair.md](../engine/04-critique-and-repair.md)

Coordinate systems and unbundled physical terms live in `../atlas/`:
- 16 face dials, 6 silhouettes, 5 topologies, canvas framing: [../atlas/coordinates.md](../atlas/coordinates.md)
- 4-factor density bands and batch spread: [../atlas/density.md](../atlas/density.md)
- Unbundled material, tailoring, patina, and pigment lexicon: [../atlas/lexicon.md](../atlas/lexicon.md)
- 15 subgenre cliché blacklists (`Forbidden` sources): [../atlas/genre-traps.md](../atlas/genre-traps.md)

---

## 1. Select the design output mode

| Mode | What it is | When |
| --- | --- | --- |
| **Mode A — identity sheet** (default) | one 16:9 sheet: three full-body orthographic views left, 2×2 bust grid right | new character, concept sheet, gameplay or drama asset |
| **Mode A-Split** | turnaround sheet (`3:2`) + face sheet (`1:1`), identity block reused verbatim | identity-critical characters reused across many shots, or an engine that cannot hold seven panels |
| **Mode A-Compact** | single-sheet layout trimmed to 270–310 words | engines with hard prompt limits, or a quick draft; never a final asset |
| **Mode B — exploration** | 3 contrasting Subgenre + Truth + Seed + Silhouette + Pose combinations at one locked gear | broad or ambiguous briefs |
| **Mode C — costume variant** | a second look for an existing character: identity block reused verbatim, only the look layer is derived | new outfit, hairstyle, ornament set, or occasion change on a character that already exists |
| **Portrait** | head-to-waist half body (`3:4`) | a one-off look, a quick read, no full-body turnaround needed |

Mode A layout, occupancy, and per-cell scoping are specified in [sheet.md](sheet.md). State the target canvas and engine with the mode.

### Mode C — design a variant, not a new person

Run Mode C when the request is a wardrobe, hairstyle, or occasion change for an existing character:

1. **Start from the character record ([../contract/records.md](../contract/records.md) §1).** Reuse its identity block (bone geometry §1A, iris/mark surface §1B, body ratio, hairline, porcelain finish) word for word. **Do not re-run [../engine/02-face-derivation.md](../engine/02-face-derivation.md) §1A or §1B** — re-deriving them creates a recast.
2. **Derive the seed from this outfit's specific occasion**, not the character's whole biography ([../engine/03-costume-and-craft.md](../engine/03-costume-and-craft.md) §1.1).
3. **Keep the silhouette family and key colour family by default** ([../contract/gates.md](../contract/gates.md) §9A). Change them only when the character's status or role has actually changed, and state why in the blueprint.
4. **Clear the look-separation test:** at least **three of four** look factors (`gravity topology · trim language · motif family · node distribution`) must differ from that character's previous look.
5. Record the result as a `↳` variant line under its parent character in the batch ledger ([../contract/records.md](../contract/records.md) §8).

---

## 2. The 4D Derivation Stack (Strict execution order)

Never open `atlas/coordinates.md` or `atlas/lexicon.md` before completing Layers 0, 1, and 2. Derive the character's physical truth first; use the atlas only to locate coordinates and select unbundled physical nouns.

| Layer | Dimension | Question | Mandatory Output | Engine / Atlas Owner |
| --- | --- | --- | --- | --- |
| **0. Batch Ledger** | Project Cast | Which silhouette, colour, topology, face anchor, and pose values are already spent? | 10-axis clearance targets | [../contract/records.md](../contract/records.md) §8; [../contract/gates.md](../contract/gates.md) §9 |
| **1. Truth & Pose (D1 & D3)** | Person & Kinetics | Who is this, what does their daily action cost their body, and how do they stand? | Position triple + Step 0 biography (if thin brief) + 2 traces + 1 contradiction + Thesis + **4D Pose Vector** | [../engine/01-truth-and-pose.md](../engine/01-truth-and-pose.md) §1–§7 |
| **2. Face Bone & Surface (D2)** | Cranial & Optical Identity | What bone proportions (§1A) and what iris/periocular/lip/mark signifiers (§1B) belong uniquely to this person? | 10 bone values (3 pushed anchors) + 5 surface decisions (**0-mark default**) | [../engine/02-face-derivation.md](../engine/02-face-derivation.md) §1A, §1B |
| **3. Seed, IFV & Topology (D4a)** | Structural Concept | What conflict metaphor builds the garment, what is banned, and where does weight sit? | Derived seed + 3 growth answers + **IFV Triple** (`Invariant / Free / Forbidden`) + Gravity topology | [../engine/03-costume-and-craft.md](../engine/03-costume-and-craft.md) §1; [../atlas/genre-traps.md](../atlas/genre-traps.md) |
| **4. Density & 5 Craft Operators (D4b)** | Aesthetic Order & Grounding | Is there enough material, how is it supported physically, and why does the proportion/value/colour look high-end? | 4 density counts + open area + Operators 2.1–2.5 (waist/hem cut, rhythm breakpoint, 10% Notan, temperature clash, understructure) | [../atlas/density.md](../atlas/density.md); [../engine/03-costume-and-craft.md](../engine/03-costume-and-craft.md) §2–§3; [../atlas/lexicon.md](../atlas/lexicon.md) |
| **5. House Render** | Production Finish | How do the 4 pillars, 6 verbatim face craft strings, and sheet-safe lighting assemble? | Verbatim craft strings + persona light mode + engine flags | [../contract/visual.md](../contract/visual.md) §4–§11 |

---

## 3. The Upgraded 7-Point Blueprint (with IFV & Swap Test)

Present the header and all **7 blueprint points in Chinese**, in this exact order. Every point is mandatory.

### Header: Lock Line & IFV Triple

```text
锁定行: [genre] / [subgenre] / [pigment family] / [silhouette family] / [gear] / [register]
IFV 声明:
  - Invariant (不变量): [1 physical structural rule locked to carry the thesis]
  - Free (自由变量): [2–3 garment/construction axes explored in this design]
  - Forbidden (题材禁令): [3 specific clichés from atlas/genre-traps.md banned from this character]
```

### The 7 Points

| # | Point | Must contain (Zero lookup presets allowed) | Source |
| --- | --- | --- | --- |
| **1** | **题材、风险档与四维静态姿态** | Lock summary, chosen risk levers ([../engine/03-costume-and-craft.md](../engine/03-costume-and-craft.md) §3.1), and the **4D Orthographic Pose Vector**: `重心轴 (Weight) · 肩颈线 (Shoulder-Neck) · 空手行为 (Empty-Hand Action) · 下巴与视线 (Chin & Gaze)`, explicitly differentiated against the previous ledger row (axis 10). | [../contract/gates.md](../contract/gates.md) §1–3; [../engine/01-truth-and-pose.md](../engine/01-truth-and-pose.md) §7 |
| **2** | **角色事实与设计论点** | Position triple, Step 0 daily body cost (if thin brief), three answers, imperfections (editorial 2; glamour 0–1), one contradiction direction + **concrete physical signal** (axis 5), and a **one-sentence thesis with a physical garment/material anchor after the colon**. | [../engine/01-truth-and-pose.md](../engine/01-truth-and-pose.md) §1–§6 |
| **3** | **冲突母题与生长法则** | The motif seed **derived from the script's conflict** + the three mandatory growth answers: **Support** (which load-bearing piece holds it), **Pressure** (where stress/wear lands), **Empty Hands** (how hands interact with the garment). | [../engine/03-costume-and-craft.md](../engine/03-costume-and-craft.md) §1.1–§1.2 |
| **4** | **视觉重心、落地承重与背部叙事** | Gravity topology (axis 3), hero and supporting zones, **Operator 2.1 vertical cut points** (waist-cut height + hem/cuff termination), **Operator 2.5 physical understructure & historical tailoring mechanics** (what holds the collar/skirt/armour up), and how the back view resolves the front. | [../atlas/coordinates.md](../atlas/coordinates.md) §3; [../engine/03-costume-and-craft.md](../engine/03-costume-and-craft.md) §2.1, §2.5 |
| **5** | **装饰密度（四因素计数）与节奏破律** | **All four factors counted and spread against the batch** ([../atlas/density.md](../atlas/density.md) §6A): (1) visible layers in order with cm offsets and value/opacity contrast; (2) treated edge rate (`X/Y = Z%`) in one shared trim language + **named raw edge set** (axis 7); (3) node count (`1 hero + N supporting`, descending scale) with **each node's mechanical closure/junction job**; (4) motif family at macro/mid/micro scales (axis 8) + **Operator 2.2 primary open breathing area & one rhythmic breakpoint**. | [../atlas/density.md](../atlas/density.md) §1–§6A; [../engine/03-costume-and-craft.md](../engine/03-costume-and-craft.md) §2.2 |
| **6** | **审美秩序（明暗块与冷暖对抗）** | Silhouette family (axis 1), **Operator 2.3 grayscale 70/25/5 value masses** with HEX and focal contrast locked at face/throat, **Operator 2.4 colour relationship + mandatory counter-temperature chromatic anchor**, 2–3 material light behaviours ([../atlas/lexicon.md](../atlas/lexicon.md) §1), and **the one restraint rule deliberately broken**. | [../engine/03-costume-and-craft.md](../engine/03-costume-and-craft.md) §2.3–§2.4; [../atlas/lexicon.md](../atlas/lexicon.md) §1, §5 |
| **7** | **半写实渲染、骨相参数（§1A）与表皮符号（§1B）** | Head-count band + shoulder-waist-hip; **§1A ten derived bone parameters** named as numbers (highlighting the 3 pushed anchors); **§1B five derived surface signifiers**: (1) iris optics & gaze reason, (2) periocular weight direction, (3) functional lip state, (4) skin matte/specular map, (5) **0-or-1 mark with earned origin** (axis 9); 6-layer hair architecture; one alive asymmetry; bottom-right macro muscle shift; persona light mode (axis 6); engine & target canvas. | [../engine/02-face-derivation.md](../engine/02-face-derivation.md) §1A, §1B, §3–§5; [../contract/visual.md](../contract/visual.md) §4–§10 |

**Mode C (Variant) blueprint adjustments:**
- Point 1 marks silhouette and key colour as `inherited from [Character]`.
- Point 2 states the **new occasion's conflict** rather than re-deriving the person's life.
- Point 7 **restates the character record's §1A and §1B identity values verbatim** — never re-derives them.

---

## 4. The Content-Free 520–585 Word Syntactic Wireframe

Continuous English prose, **zero bracketed section headers, zero numeric percentages, zero shader numbers, zero HEX codes** (HEX stays in blueprint point 6).

Word budget (measured by `scripts/preflight.py` alphabetic prose words before `--ar/--no` flags):
- **Editorial full 7-panel sheet:** **500–540 words**
- **Glamour / Ceremonial full 7-panel sheet:** **540–585 words**
- **Mode A-Compact:** **270–310 words**
- **Portrait / Scene:** **≤ 400 words**

### The Five-Block Assembly Wireframe (Slot Grammar — fill every slot from your blueprint, never from a template)

```text
[BLOCK 1: CANVAS, 4-PILLAR BASE & LIGHTING HEADER (~75–90 words)]
Character concept design sheet on a seamless [pure white | warm off-white] background, premium 3D game CG character render, semi-realistic shading with hand-authored material response, refined anime facial design fused with high-grade BJD porcelain material quality, sculptural surface relief, commercial animation art direction, [selected Persona Light Mode tokens from contract/visual.md §8], sheet-safe soft directional key from the [left/right] with a broad bounce fill, clean rim separation, and a soft grounded contact shadow.

[BLOCK 2: 7-PANEL ORTHOGRAPHIC LAYOUT & 4D POSE SCOPING (~105–115 words)]
Left zone, borderless: full-body front view, left-facing pure 90-degree side profile, and pure back view, orthographic, on one shared ground line at identical scale, standing with [Pose Vector 1: weight axis], [Pose Vector 2: shoulder-neck line], [Pose Vector 3: specific empty-hand action interacting with garment/body], [Pose Vector 4: chin angle and gaze direction], head to toe uncropped. Right zone: a thin-line 2x2 grid of bust cells, where the top-left is a symmetrical front bust with a fully neutral baseline face, the top-right is a three-quarter bust with a [tilt/turn and directional gaze from engine/02 §5], the bottom-left is a pure left profile bust, and the bottom-right is a tight macro of the eyes, nose and lips only, crown and shoulders deliberately cropped out of that cell, carrying [3-part muscle micro-expression: what tightens/lifts by how many millimetres, and what stays still].

[BLOCK 3: THESIS, IDENTITY BLOCK (§1A BONE + §1B SURFACE) & HAIR (~120–140 words)]
[One-sentence Design Thesis with physical garment/material anchor]. A [Position triple: age band, gender presentation, class/command read], [head-count band] with [shoulder-waist-hip line and waist-cut height], [visible consequences of the §1A bone parameters: facial index, cheekbone plane, jaw/chin width], large almond eyes with a defined upper lid line and a clear double-lid crease, [eye spacing and canthal tilt consequence], [derived §1B-1 iris colour and value] irises with radial fibre, a darker limbal ring, a bright secondary reflection and a wet meniscus on the lower lid, [derived §1B-2 periocular weight], a minimal nose bridge with [derived §1A nose tip/length], [derived §1A mouth width and §1B-3 lip ratio/finish] with a visible cupid's bow, [omit entirely if 0 marks; or state the 1 earned mark from §1B-5], and smooth porcelain skin with a soft subsurface glow and [derived §1B-4 matte cheek / specular break]. [Hair mass, hairline, parting, grouped locks with sculpted strand clumps, a soft anime-style highlight band across the crown, individual flyaway strands catching the light, linear value interruption, and 1 alive asymmetry].

[BLOCK 4: 4-CLAUSE DENSITY, GROUNDING, TOPOLOGY & RISK (~175–220 words)]
[Editorial: 2 physical life traces | Glamour: status marker + direction-7 signal]. [Layer clause: 3–6 layers in order from skin-adjacent to outer/floating, naming centimetre offsets, matte-vs-translucent/value contrasts, historical tailoring mechanics, and physical understructure/stays]. [Edge clause: 60–90% of boundaries finished in one shared trim language, plus explicit naming of the 1–3 boundaries left raw]. [Node clause: hero node + descending supporting nodes at structural junctions, stating the exact closure, pinning, or load-bearing job of each, with jeweller-grade fittings on the hero piece]. [Pattern & Open-Area clause: the single motif family carried at macro hardware, mid border band, and tone-on-tone micro field weave, contrasted against one named unpatterned primary open area and one rhythmic breakpoint]. [Gravity topology and back-view resolution: how the rear view resolves the front's structural tension, plus the one deliberate risk/broken rule].

[BLOCK 5: CROSS-VIEW CONSISTENCY FOOTER (~15–20 words)]
Identical costume construction, seam placement, hair streaks, and surface markings repeated consistently across all seven panels, with empty hands throughout.
```

---

## 5. Exclusions and Engine Attachment

Follow [../contract/visual.md](../contract/visual.md) §3 and §11. For Midjourney sheets, append:
`--ar 16:9 --raw --s 150 --no text, labels, logos, watermarks, plastic, waxy, low-poly, cutout`
Never put `doll`, `seams`, `skin`, `figure`, or multi-word phrases into Midjourney `--no`.

---

## 6. Dual Acceptance Gate: Counted Preflight + Adversarial Critique

A design ships **only** when it passes **both** §6B/C/D (the mechanical counts via `scripts/preflight.py` and per-register thresholds) **and** §6E (the Adversarial Critique Gate in [../engine/04-critique-and-repair.md](../engine/04-critique-and-repair.md) §1).

### 6A. Blueprint-to-prompt traceability (Run first)

Every layer, treated edge, raw edge, ornament node, motif scale, bone anchor, iris colour, and pose component named in the blueprint must appear in the English prompt with matching wording, and palette token counts must match the declared 70/25/5 hierarchy (`base > anchor ≥ accent`, `accent ≤ 2`).

### 6B. Mechanical preflight (`scripts/preflight.py`)

Run `scripts/preflight.py` against the prompt, the 10-axis ledger vector, and (when available) the previous character's prompt:

| Check | Requirement |
| --- | --- |
| **Word budget** | 500–540 editorial · 540–585 glamour · 270–310 compact |
| **Banned words & shader tags** | zero hits from [../contract/gates.md](../contract/gates.md) §6 |
| **Palette & material caps** | `accent ≤ 2`, `anchor ≤ 4`, `base ≤ 8`, `base ≥ 2× accent`, `single material ≤ 5` ([../atlas/lexicon.md](../atlas/lexicon.md) §5.3) |
| **6 House craft elements** | upper lid/crease, iris, second catchlight, porcelain skin, hair strand clumps, key light direction all present |
| **4D Decision anchors** | (1) bone anchor consequence, (2) head-count proportion band, (3) specific iris/lip surface decision, (4) explicit static pose vector (weight + hand action + gaze; no bare `neutral balanced stance`) |
| **Cliché N-gram trap check** | zero unapproved hits on stock combinations (`tear-mole`, `starflower + silver filigree`, etc.) |
| **10-Axis batch differentiation** | axes 1 (silhouette) and 2 (key colour) differ from **every** ledger row; axes 9 (face bone+surface) and 10 (pose vector) differ from adjacent rows; **at least 6 of 10 axes** differ overall |
| **Cross-cast lexical overlap** | non-craft design vocabulary Jaccard overlap **≤ 28%** against previous character prompts |

### 6C. Editorial register preflight

| Check | Kind | Pass condition | If it fails |
| --- | --- | --- | --- |
| **Density factors** | counted | layers 2–3 working / 4–5 high-status; edge rate 60–80% + named raw set; nodes ≤ 4 (`1 hero + up to 3 supporting`) with mechanical closure jobs; pattern bare/banded/fielded, spread from previous cast row ([../atlas/density.md](../atlas/density.md) §6A) | add the missing layer or shared trim clause; delete any unemployed node |
| **Transcendent traces & contradiction** | counted | 1–2 poetic/power-derived traces + one contradiction from the 7 high-aesthetic directions | return to [../engine/01-truth-and-pose.md](../engine/01-truth-and-pose.md) §2, §5 |
| **Materials & couture grounding** | counted | at least two light behaviours (e.g. matte velvet + sheer siren-gauze + tight metal specular); haute-couture corsetry/armature named; ≤ 4 named fabric types | add a tight-specular or translucent element; name the waist-girdle/shoulder-yoke structure ([../engine/03-costume-and-craft.md](../engine/03-costume-and-craft.md) §2.5) |
| **Restraint & open area** | counted | one hero node + ≤ 3 supporting; one primary unpatterned open breathing area named | delete the weakest node; clear one expanse of cloth |
| **Face §1A + §1B** | counted | 10 bone values in band with 3 pushed anchors; 5 surface variables derived from facts; **0 facial marks by default** unless earned | run [../engine/02-face-derivation.md](../engine/02-face-derivation.md) §1A & §1B |

### 6D. Glamour register preflight

| Check | Kind | Pass condition | If it fails |
| --- | --- | --- | --- |
| **Density factors** | counted | layers 5–6 (incl. ≥ 1 floating); edge rate 80–90% + named raw set; nodes 8–15 descending head → waist with mechanical jobs; pattern fielded/allover, spread from previous glamour row ([../atlas/density.md](../atlas/density.md) §6A) | add the floating layer or pattern field; move density numbers within the band |
| **Top-zone & 6-layer hair** | counted | head carries ≥ 2 distinct ornament groups; all 6 hair layers written ([../engine/03-costume-and-craft.md](../engine/03-costume-and-craft.md) §3.2) | add one head group before anything lower; complete the 6 hair clauses |
| **Density gradient & quiet zone** | judged | strict descent `head > chest > waist > hem`; zero nodes at the hem; at least one plain run or bare skin below the waist | strip nodes below the waist; clear one lower-body breathing zone |
| **Contradiction & charm** | judged | Direction-7 lethal signal (or earned 1–6) differing from the batch; one alive asymmetry; two catchlights; one matte cheek zone + one specular break near the face | replace generic "red eyes" with a conflict-derived signal; add the matte/specular contrast |
| **Face §1A + §1B** | counted | iris fill ≤ 0.95, eye width ≤ 1.20×; facial index derived via §1A (never defaulted to 1.42); §1B iris/lip/mark derived with **0-mark default** | pull into band and derive from Position & gaze facts |

### 6E. Adversarial Critique Gate (Mandatory in delivery text)

Immediately after the 7-point blueprint and before the preflight numbers, write the 3-line **Adversarial Critique** from [../engine/04-critique-and-repair.md](../engine/04-critique-and-repair.md) §1:
1. **最强套路指控 (Generic Accusation)**
2. **专属物证反驳 (Specific Rebuttal — 3 physical nouns)**
3. **换人测试结论 (Swap Verdict)**

Plus the 1-line **Judged Visual Read**: 10% silhouette outline, 70/25/5 grayscale Notan separation, whether the face wins first fixation, and density gradient descent.

---

## 7. Delivery Order

1. **Lock line + IFV Triple** (`Invariant / Free / Forbidden`).
2. **All 7 blueprint points** in Chinese (with counted point 5, HEX in point 6, and §1A + §1B values in point 7).
3. **The 3-line Adversarial Critique** (`Generic Accusation / Specific Rebuttal / Swap Verdict`).
4. **Preflight & 10-Axis Batch Vector report** (counted results + 1-line judged notes).
5. **One copy-ready English prompt** in a fenced code block, plus engine exclusions and a brief note on any `[inferred biography]` or unseen structure.
6. For recurring characters, append the compact **Character Record** and updated **10-Axis Batch Ledger row** ([../contract/records.md](../contract/records.md) §1, §8).
