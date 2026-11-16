---
name: drama-visual-studio
description: Design bold, high-aesthetic characters and costumes in a unified semi-realistic 3DCG house style (refined anime face, high-grade BJD porcelain surface, commercial animation art direction), then turn the design into production-ready prompts. Uses a 4D derivation engine (Truth & Orthographic Pose, Cranial Bone & Facial Surface Signifiers, Conflict-to-Seed + IFV Triple, and 5 Craft Operators) plus an Adversarial Critique Gate (Swap Test) and a 10-axis batch ledger to prevent facial, pose, and costume homogenization. Covers character design, costume variants, three-view plus 2x2 concept sheets, GPT Image 2 sheets, scene bases, scene variations, viewpoint changes, controlled outpainting, two-stage Midjourney-to-GPT-Image-2 asset chains, and returned-image drift repair. Delivers prompt text and design specs only; it does not generate or edit images. Triggers include 角色设计、人设、三视图、服装设计、装饰密度、角色同质化、场景底图、场景一致性、扩图、返图修正、角色设定图.
---

# Drama Visual Studio

One skill, four modes. Derive a character across four orthogonal dimensions, design a second look for an existing character, produce downstream production prompts, or diagnose a returned image.

The pack is engine-agnostic by structure. Midjourney is the default engine for art direction and first images, GPT Image 2 for structured sheets and scene edits, with SD/Flux and CN engines supported through the same exclusion policy.

## Load contract

Files are grouped by how they load:

- `contract/` — binding on every output. One rule, one home. Never restated elsewhere.
- `engine/` — 4D derivation procedures, inline craft operators, adversarial critique, and drift repair.
- `atlas/` — orthogonal coordinate systems, unbundled physical lexicon, and subgenre cliché blacklists. Read after `engine/01`–`02` have established the character's facts.
- `pipeline/` — numbered workflow procedures and syntactic assembly wireframes.

| Task | Required | Optional | Do not load |
| --- | --- | --- | --- |
| **Character design (Mode A / B / Portrait)** | [contract/visual.md](references/contract/visual.md), [contract/gates.md](references/contract/gates.md), [contract/records.md](references/contract/records.md) §8, [pipeline/design.md](references/pipeline/design.md), [engine/01-truth-and-pose.md](references/engine/01-truth-and-pose.md), [engine/02-face-derivation.md](references/engine/02-face-derivation.md), [engine/03-costume-and-craft.md](references/engine/03-costume-and-craft.md), [engine/04-critique-and-repair.md](references/engine/04-critique-and-repair.md) §1–2, [atlas/genre-traps.md](references/atlas/genre-traps.md), [atlas/density.md](references/atlas/density.md), [atlas/lexicon.md](references/atlas/lexicon.md) | [atlas/coordinates.md](references/atlas/coordinates.md), [pipeline/sheet.md](references/pipeline/sheet.md) | scene files |
| **Costume variant (Mode C)** | [contract/visual.md](references/contract/visual.md), [contract/gates.md](references/contract/gates.md) §9A, [contract/records.md](references/contract/records.md) §1 & §8, [pipeline/design.md](references/pipeline/design.md) §1 Mode C, [engine/03-costume-and-craft.md](references/engine/03-costume-and-craft.md), [atlas/density.md](references/atlas/density.md), [atlas/lexicon.md](references/atlas/lexicon.md) | [engine/04-critique-and-repair.md](references/engine/04-critique-and-repair.md) §1–2 | `engine/02-face-derivation.md` §1A (never re-derive face) |
| **Identity or costume sheet** | [contract/visual.md](references/contract/visual.md), [contract/records.md](references/contract/records.md), [pipeline/sheet.md](references/pipeline/sheet.md), [engine/01-truth-and-pose.md](references/engine/01-truth-and-pose.md) §7 | [engine/03-costume-and-craft.md](references/engine/03-costume-and-craft.md) §3.2 | scene files |
| **GPT Image 2 sheet** | [contract/visual.md](references/contract/visual.md), [contract/records.md](references/contract/records.md), [pipeline/gpt-sheet.md](references/pipeline/gpt-sheet.md), [pipeline/sheet.md](references/pipeline/sheet.md) | [engine/01-truth-and-pose.md](references/engine/01-truth-and-pose.md) | MJ parameter columns |
| **Vertical frame or portrait** | [contract/visual.md](references/contract/visual.md), [atlas/coordinates.md](references/atlas/coordinates.md) §4 | [engine/02-face-derivation.md](references/engine/02-face-derivation.md) §4–5 | sheet files |
| **Scene base** | [contract/visual.md](references/contract/visual.md), [pipeline/scene.md](references/pipeline/scene.md) | [atlas/coordinates.md](references/atlas/coordinates.md) §4, [atlas/genre-traps.md](references/atlas/genre-traps.md) | character design engine |
| **Scene variation or viewpoint change** | [contract/visual.md](references/contract/visual.md), [contract/records.md](references/contract/records.md), [pipeline/scene-edit.md](references/pipeline/scene-edit.md) | [pipeline/outpaint.md](references/pipeline/outpaint.md) | character design engine |
| **Outpainting** | [contract/visual.md](references/contract/visual.md), [pipeline/outpaint.md](references/pipeline/outpaint.md) | [contract/records.md](references/contract/records.md) §1 | character design engine |
| **Asset chain** | [contract/visual.md](references/contract/visual.md), [contract/records.md](references/contract/records.md), [pipeline/asset-chain.md](references/pipeline/asset-chain.md) | [atlas/coordinates.md](references/atlas/coordinates.md) §4, [engine/03-costume-and-craft.md](references/engine/03-costume-and-craft.md) §3.3 | — |
| **Review a returned image** | [contract/records.md](references/contract/records.md), [engine/04-critique-and-repair.md](references/engine/04-critique-and-repair.md) §4 (for characters) or [pipeline/scene-edit.md](references/pipeline/scene-edit.md) §6 (for scenes) | — | everything else |

## Choose the mode

### Design mode — derive a new character or outfit

Use when the user supplies a character concept, a script conflict, or asks for a new design sheet. A second outfit for a character who already exists is [Variant mode](#variant-mode--a-second-outfit-for-a-character-who-already-exists), not Design mode.

Follow [pipeline/design.md](references/pipeline/design.md). Read the batch ledger ([contract/records.md](references/contract/records.md) §8) first; if none exists, create one. Deliver, in order:

1. **Lock line + IFV Triple** (`Invariant / Free / Forbidden`, blocking 3 subgenre reflexes from [atlas/genre-traps.md](references/atlas/genre-traps.md)).
2. **All 7 blueprint points in Chinese**:
   - Point 1: genre/risk lock and the **4D Orthographic Pose Vector** (`weight axis · shoulder-neck line · empty-hand action · chin & gaze`).
   - Point 2: Position triple, Step 0 daily body cost (if thin brief), life traces, contradiction signal, and physical-anchor thesis.
   - Point 3: conflict-derived motif seed and the three growth answers (Support, Pressure, Empty Hands).
   - Point 4: gravity topology, **vertical cut proportions** (§2.1), **physical understructure/grounding** (§2.5), and back-view resolution.
   - Point 5: **all four density factors counted** (layers, edge rate + raw edge set, node count with mechanical jobs, 3-scale motif) plus the **open breathing area and rhythmic breakpoint** (§2.2).
   - Point 6: **10% grayscale Notan 70/25/5 masses** (§2.3), HEX codes, **counter-temperature clash** (§2.4), and material light behaviours.
   - Point 7: head-count band + shoulder-waist-hip, **§1A ten derived bone values**, **§1B five derived surface signifiers** (iris optics, periocular weight, lip state, specular/matte map, **0-mark default**), hair architecture, bottom-right macro shift, light mode, and canvas.
3. **The 3-line Adversarial Critique Gate** ([engine/04-critique-and-repair.md](references/engine/04-critique-and-repair.md) §1): `Generic Accusation` vs `Specific Rebuttal (3 drawable nouns)` + `Swap Verdict`.
4. **Preflight & 10-Axis Batch Vector report**.
5. **One copy-ready English prompt** assembled via the 5-block syntactic wireframe ([pipeline/design.md](references/pipeline/design.md) §4) in a fenced code block, plus engine exclusions and a brief note on any `[inferred biography]`.
6. For recurring characters, finish with the compact **Character Record** and updated **10-Axis Batch Ledger row** ([contract/records.md](references/contract/records.md) §1, §8).

### Variant mode — a second outfit for a character who already exists

Follow [pipeline/design.md](references/pipeline/design.md) §1 Mode C and [contract/gates.md](references/contract/gates.md) §9A:

1. **Read the character record** ([contract/records.md](references/contract/records.md) §1) and reuse its identity block (§1A bone + §1B surface/iris/mark), palette roles, and confirmed finish word for word. **Do not re-run `engine/02-face-derivation.md` §1A.**
2. **Derive the seed from this outfit's specific occasion** ([engine/03-costume-and-craft.md](references/engine/03-costume-and-craft.md) §1).
3. **Clear the look-separation test:** at least **three of four** look factors (`gravity topology · trim language · motif family · node distribution`) must differ from that character's previous look.
4. **Keep silhouette and key colour** unless their status or role has actually changed.
5. Record the result as a `↳` variant line under its character in the ledger.

### Production mode — turn a design into an output prompt

1. Build or read the character record in [contract/records.md](references/contract/records.md) §1. Reuse its identity block word-for-word.
2. Route by requested output using the load contract table above.
3. Deliver one copy-ready prompt in a fenced code block.

### Review mode — check a returned image

- Compare only images actually supplied ([contract/gates.md](references/contract/gates.md) §7).
- For character sheets and portraits, use [engine/04-critique-and-repair.md](references/engine/04-critique-and-repair.md) §4.
- For scenes, use [pipeline/scene-edit.md](references/pipeline/scene-edit.md) §6.
- Report observed differences first; provide a focused correction prompt only when requested.

## Output contract & rule ownership

Universal rules — each is owned by one file:

| Rule | Owner |
| --- | --- |
| House style, medium selection, engine parameters, version facts | [contract/visual.md](references/contract/visual.md) §1–3 |
| Semi-real proportions & the six required face craft vs decision elements | [contract/visual.md](references/contract/visual.md) §4–5 |
| Character/scene lighting, background value, split protocol, exclusions | [contract/visual.md](references/contract/visual.md) §8–11 |
| Genre lock + IFV triple, register, risk gear, no-props, conflict order | [contract/gates.md](references/contract/gates.md) §1–5 |
| Banned prompt language & capability limits | [contract/gates.md](references/contract/gates.md) §6–7 |
| **Craft vs decision & The Swap Test** | [contract/gates.md](references/contract/gates.md) §8 |
| **10-axis batch differentiation & Mode C variant rules** | [contract/gates.md](references/contract/gates.md) §9, §9A |
| Character/location records, reference roles, output delta, **10-axis ledger** | [contract/records.md](references/contract/records.md) §1–8 |
| Step 0 Thin-Brief compiler, contradiction directions, **4D orthographic pose** | [engine/01-truth-and-pose.md](references/engine/01-truth-and-pose.md) §1, §5, §7 |
| **§1A ten bone parameters & §1B five facial surface signifiers** | [engine/02-face-derivation.md](references/engine/02-face-derivation.md) §1A, §1B |
| Conflict-to-seed compiler, IFV triple, **5 inline Craft Operators** | [engine/03-costume-and-craft.md](references/engine/03-costume-and-craft.md) §1–2 |
| **Adversarial Critique Gate, 12 Generic Autopsies, drift repair** | [engine/04-critique-and-repair.md](references/engine/04-critique-and-repair.md) §1–4 |
| 16 face dials (EW), 6 silhouettes, 5 topologies, canvas framing (`9:16` / `16:9` / `3:4`) | [atlas/coordinates.md](references/atlas/coordinates.md) §1–4 |
| 4-factor ornament density, 4-clause template, **batch band-spread** | [atlas/density.md](references/atlas/density.md) §1–6A |
| Unbundled physical lexicon, mineral pigments, token-frequency caps | [atlas/lexicon.md](references/atlas/lexicon.md) §1–5 |
| 15 subgenre cliché blacklists (`Forbidden` sources) & physical pressure anchors | [atlas/genre-traps.md](references/atlas/genre-traps.md) §1–3 |

Two rules apply everywhere:
1. **Put the finished prompt in a fenced code block** so it is easy to copy.
2. **Deliver prompt text only.** Do not generate an image unless separately requested, and do not claim a mask, control map, reference binding, or renderer has been executed.

## Run the counted checks

`scripts/preflight.py` checks word budget, colour/material caps, banned words, bare generic pose strings, required house craft elements, all four 4D decision anchors, cliché N-gram traps, 10-axis batch ledger differentiation, and cross-cast non-craft lexical overlap:

```bash
python -I scripts/preflight.py prompt.txt --register editorial
python -I scripts/preflight.py prompt.txt --register glamour --palette
python -I scripts/preflight.py prompt.txt --register editorial \
    --ledger batch.txt \
    --vector "asymmetric · 玄黑+幽冥紫黑 · topology 3 单侧异化 · editorial gear 2 · dir1/墨玉指尖与乌金护指 · 明暗伦勃朗侧逆 · 乌金掐丝包边 · 幽冥骨铃脊椎纹 · 面部指数1.48+深渊血珀瞳+眼尾魔纹 · 重心落右腿+左手搭腰玉+微抬下巴垂眸" \
    --compare-prompt prev_character.txt
python -I scripts/preflight.py variant.txt --register glamour \
    --ledger batch.txt --variant-of "A 九幽魔宗左护法" --inherit \
    --vector "topology 1 顶峰下泻 · 暗绯鎏金宽镶边 · 业火红莲暗纹 · 节点聚于乌金高冠与双肩垂链"
```

## Files

Contract:
- `references/contract/visual.md` — house style, engine parameters, proportions, face craft vs decision, environments, lighting (§8 & §8A), background, split protocol, exclusions.
- `references/contract/gates.md` — genre lock + IFV triple, register, risk gear, no-props rule, banned language, capability limits, craft vs decision + Swap Test, 10-axis batch differentiation & Mode C variants.
- `references/contract/records.md` — character record, location record, version selection, reference roles, output delta, 10-axis batch ledger.

Engine:
- `references/engine/01-truth-and-pose.md` — Step 0 Thin-Brief compiler, three questions, ten dimensions, seven contradiction directions, design thesis, 4D orthographic pose vector.
- `references/engine/02-face-derivation.md` — §1A ten bone geometry parameters + §1B five facial surface signifiers (iris optics, periocular weight, lip state, specular/matte map, 0-mark default), mood dials, charm, gaze/turn/tilt.
- `references/engine/03-costume-and-craft.md` — conflict-to-seed compiler, three growth rules, IFV triple, 5 inline Craft Operators (Proportion, Rhythm, Notan, Colour, Grounding), ten boldness levers, glamour hair system, I2V adaptation.
- `references/engine/04-critique-and-repair.md` — Adversarial Critique Gate (Swap Test), 12 Generic Failure Autopsies, under/over-shoot detection, returned-image drift repair.

Atlas:
- `references/atlas/coordinates.md` — 16 face parameters (EW), 6 silhouette families, 5 gravity topologies, narrative & sheet canvas framing (`9:16`, `16:9`, `3:4`).
- `references/atlas/density.md` — 4 density factors (layers, edges + raw set, nodes with mechanical jobs, 3-scale pattern), gradient, 4-clause template, batch band-spread (§6A).
- `references/atlas/lexicon.md` — unbundled atomic physical lexicon (4 light behaviours, fabric weight/drape, historical tailoring & hardware, patina & wear, mineral pigments, token-frequency caps).
- `references/atlas/genre-traps.md` — 15 subgenre cliché blacklists & world physical pressure anchors.

Pipeline:
- `references/pipeline/design.md` — modes, 4D derivation stack, 7-point blueprint, content-free 520–585 word syntactic wireframe, dual preflight + critique gate.
- `references/pipeline/sheet.md` — identity, costume, and asset sheets.
- `references/pipeline/gpt-sheet.md` — GPT Image 2 character sheets.
- `references/pipeline/scene.md` — first scene base.
- `references/pipeline/scene-edit.md` — fixed-view variations, camera moves, returned-image scene checks.
- `references/pipeline/outpaint.md` — controlled crop completion.
- `references/pipeline/asset-chain.md` — two-stage Midjourney-to-GPT-Image-2 asset chain.

Tooling:
- `scripts/preflight.py` — mechanical preflight, 4D anchor checker, cliché N-gram trap scanner, 10-axis ledger comparator, and cross-cast non-craft lexical overlap checker.
