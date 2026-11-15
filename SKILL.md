---
name: drama-visual-studio
description: Design bold, high-aesthetic characters and costumes in a unified semi-realistic 3DCG house style (refined anime face, high-grade BJD porcelain surface, commercial animation art direction), then turn the design into production-ready prompts. Use for character design from a concept, genre/subgenre/risk/register selection, motif seeds derived from the script's conflict, ornament density, derived identity sets, three-view plus 2x2 concept sheets, GPT Image 2 minor-character sheets, scene bases, scene variations, viewpoint changes, controlled outpainting, two-stage Midjourney-to-GPT-Image-2 asset chains, and checking returned images to write correction prompts. Also use when characters or costumes converge on one look across a project, since it carries a batch ledger and nine differentiation axes. Delivers prompt text and design specs only; it does not generate or edit images. Triggers include 角色设计、人设、三视图、服装设计、装饰密度、角色同质化、场景底图、场景一致性、扩图、返图修正、角色设定图.
---

# Drama Visual Studio

One skill, three modes. Design the character, then produce the prompts its production needs — or start from a design that already exists.

The pack is engine-agnostic by structure. Midjourney is the default engine for art direction and first images, GPT Image 2 for structured sheets and scene edits, with SD/Flux and CN engines supported through the same exclusion policy. Midjourney is the default, not the requirement.

## Load contract

Files are grouped by how they load, not by topic. Read the required set, open the optional set only when the task needs it, and do not read a bank file end to end when a section reference will do.

- `contract/` — binding on every output. One rule, one home. Never restated elsewhere.
- `pipeline/` — numbered procedures. They reference the contract and the bank; they do not redefine them.
- `bank/` — lookup and diagnosis. Read sections on demand.

| Task | Required | Optional | Do not load |
| --- | --- | --- | --- |
| Character design | [contract/visual.md](references/contract/visual.md), [contract/gates.md](references/contract/gates.md) §8–9, [contract/records.md](references/contract/records.md) §8, [pipeline/design.md](references/pipeline/design.md), [bank/truth.md](references/bank/truth.md), [bank/face.md](references/bank/face.md) §2A–6, [bank/costume.md](references/bank/costume.md) §1, [bank/form.md](references/bank/form.md), [bank/material.md](references/bank/material.md), [bank/density.md](references/bank/density.md) | [bank/boldness.md](references/bank/boldness.md), [references/demos.md](references/demos.md) | — |
| Identity or costume sheet | [contract/visual.md](references/contract/visual.md), [contract/records.md](references/contract/records.md), [pipeline/sheet.md](references/pipeline/sheet.md), [bank/face.md](references/bank/face.md) | [bank/costume.md](references/bank/costume.md) §5A | design bank, scene files |
| GPT Image 2 sheet | [contract/visual.md](references/contract/visual.md), [contract/records.md](references/contract/records.md), [pipeline/gpt-sheet.md](references/pipeline/gpt-sheet.md), [bank/face.md](references/bank/face.md) | [pipeline/sheet.md](references/pipeline/sheet.md) | MJ parameter columns |
| Vertical frame or portrait | [contract/visual.md](references/contract/visual.md), [bank/framing.md](references/bank/framing.md) | [bank/face.md](references/bank/face.md) | design bank |
| Scene base | [contract/visual.md](references/contract/visual.md), [pipeline/scene.md](references/pipeline/scene.md) | [bank/material.md](references/bank/material.md) §3, [bank/framing.md](references/bank/framing.md) §3 | design bank |
| Scene variation or viewpoint change | [contract/visual.md](references/contract/visual.md), [contract/records.md](references/contract/records.md), [pipeline/scene-edit.md](references/pipeline/scene-edit.md) | [pipeline/outpaint.md](references/pipeline/outpaint.md) | design bank |
| Outpainting | [contract/visual.md](references/contract/visual.md), [pipeline/outpaint.md](references/pipeline/outpaint.md) | [contract/records.md](references/contract/records.md) §1 | design bank |
| Asset chain | [contract/visual.md](references/contract/visual.md), [contract/records.md](references/contract/records.md), [pipeline/asset-chain.md](references/pipeline/asset-chain.md) | [bank/framing.md](references/bank/framing.md) §5 | design bank |
| Review a returned image | [contract/records.md](references/contract/records.md), the repair table in the matching pipeline file | [bank/face.md](references/bank/face.md) §7 for face drift | everything else |

## Choose the mode

### Design mode — create a character or outfit

Use when the user supplies a character concept, a race/profession/archetype, a costume idea, a new outfit for an existing character, or asks for a new design sheet, and the requested design or outfit is not yet confirmed.

Follow [pipeline/design.md](references/pipeline/design.md). It owns the batch layer, the 6-layer design stack, the 7-point blueprint, the prompt budget, the single preflight, and drift repair.

Deliver, in order:

1. The lock line: `[genre] / [subgenre] / [pigment family] / [silhouette family] / [gear] / [register]`.
2. **All 7** blueprint points in Chinese — including point 5, ornament density, **counted** (layers, edge rate, node count, pattern coverage), never described as an adjective, and placed at a different point in the band than the batch's previous character.
3. The preflight result for the locked register, as a short list of counts, including the batch vector.
4. One copy-ready prompt for the selected design output (portrait, Midjourney sheet, or GPT Image 2 sheet), in a fenced code block.
5. Engine-appropriate exclusions, a short note on inferred details, and the target canvas.

For a reusable character that later shots will reuse, finish with the compact character record from [contract/records.md](references/contract/records.md) §1.

**Before designing anything, read the batch ledger** ([contract/records.md](references/contract/records.md) §8). A single character designed in isolation passes every check and can still be the previous character with a different name — silhouette and key colour must differ from every existing row, and five of the nine axes must differ from any other character. When there is no ledger, this is the first character: create one.

**Two things are decided, not copied.** The seed comes from the script's conflict ([bank/costume.md](references/bank/costume.md) §1C), not from the seed library, which is calibration. The identity set of ten face parameters comes from the character's Position facts ([bank/face.md](references/bank/face.md) §2A), not from a register preset. Craft strings — the eye design, the iris fibre, the porcelain finish — are reused verbatim; those are how a thing renders, not who this person is. [Contract/gates.md](references/contract/gates.md) §8 is the distinction and §9 is the batch check.

Keep the work proportional: a one-off portrait may abbreviate to the lock line, thesis, identity block, and palette. A design sheet or a recurring character gets the full 7 points.

### Production mode — turn a design into an output prompt

Use when a character design already exists — from design mode, another design skill, or the user — and the request is for a specific downstream prompt.

1. Build or read the character record in [contract/records.md](references/contract/records.md) §1. Reuse its identity block word-for-word.
2. Route by requested output using the load contract table above.
3. Keep the work proportional: a recurring, identity-critical character gets a full record; a one-off background figure gets a short identity clause, not a design pass.

### Review mode — check a returned image

Use when the user supplies a generated image and asks whether it matches its source.

- Compare only images actually supplied. Do not declare a visual pass without seeing them.
- For scenes, use the returned-image checks in [pipeline/scene-edit.md](references/pipeline/scene-edit.md) §6.
- For character sheets, use the drift-repair table in [pipeline/design.md](references/pipeline/design.md) §7.
- Report observed differences and, when requested, one focused correction prompt from the selected version. If the drift is broad, recommend returning to the last suitable version and reapplying the still-required changes.

## Output contract

- **Design mode**: lock line, 7-point blueprint, preflight counts, one prompt per selected sheet mode, engine-appropriate exclusions, and a short inferred-detail note.
- **Production mode**: a short handoff note when useful (source, locked fields, inferred fields), then one copy-ready prompt per requested output.
- **Review mode**: observed findings first; a focused correction prompt only when requested.

Universal rules — each is owned by one file, so read it there rather than expecting a restatement here:

| Rule | Owner |
| --- | --- |
| House style, medium selection, parameters, version facts | [contract/visual.md](references/contract/visual.md) §1–3 |
| Face craft vs face decision, the six required elements | [contract/visual.md](references/contract/visual.md) §5 |
| Lighting — character modes, scene modes, interiors, night, multi-source | [contract/visual.md](references/contract/visual.md) §8 and §8A |
| Background, resolution, split protocol | [contract/visual.md](references/contract/visual.md) §9–10 |
| Exclusion policy per engine | [contract/visual.md](references/contract/visual.md) §11 |
| Register, risk gear, conflict order, no-props | [contract/gates.md](references/contract/gates.md) §1–5 |
| Banned prompt language | [contract/gates.md](references/contract/gates.md) §6 |
| Capability limits and what never to promise | [contract/gates.md](references/contract/gates.md) §7 |
| **Craft versus decision — what is reused and what is derived** | [contract/gates.md](references/contract/gates.md) §8 |
| **Batch differentiation — the nine axes and the five-of-nine rule** | [contract/gates.md](references/contract/gates.md) §9 |
| Character and location records, reference roles, output delta | [contract/records.md](references/contract/records.md) |
| **Batch ledger — the project's axis vector** | [contract/records.md](references/contract/records.md) §8 |
| Canvas choice, vertical composition, safe areas | [bank/framing.md](references/bank/framing.md) |
| Face parameters, register presets, charm, **identity-set derivation** | [bank/face.md](references/bank/face.md) §2A, §3–7 |
| **Motif seed derivation from the script** | [bank/costume.md](references/bank/costume.md) §1C |

Two rules that apply everywhere and are worth stating once at the top level:

1. **Put the finished prompt in a fenced code block** so it is easy to copy. Add analysis or layout guidance only when the workflow or the user asks for it.
2. **Deliver prompt text.** Do not generate an image unless the user separately asks for one, and do not claim a mask, structure guide, reference binding, or renderer has been configured or executed.

## Run the counted checks

`scripts/preflight.py` is the mechanical half of the preflight in [pipeline/design.md](references/pipeline/design.md) §6. It parses a finished prompt and reports word count, colour and material term frequencies against the caps, banned words, `--no` policy, whether the required identity elements are present, whether the identity set was derived rather than defaulted, and — with `--ledger` — whether the batch vector actually differs from the characters already designed. It exits non-zero on failure, so it can gate a pipeline.

```bash
python -I scripts/preflight.py prompt.txt --register editorial
python -I scripts/preflight.py prompt.txt --register glamour --palette
python -I scripts/preflight.py prompt.txt --register glamour     --ledger batch.txt --vector "cocoon · umber · languid · glamour gear 2 · dir2 · warm-gi · rope piping · rope-knot · facial 1.30"
```

Pass `--vector` whenever you pass `--ledger`. The vector comes from the blueprint's own nine axes; without it the checker can only see the three or four axes that happen to be visible in the prompt prose, and it will report fewer differences than the design actually has.

Use it for the counted lines, then judge the rest yourself. It cannot see silhouette readability, value hierarchy, whether the face wins, whether the design is charming, or whether it reads as a product. It also cannot see whether the face looks like the batch's last character — it checks that ten values were derived from facts, which is a procedure and not a result. Those are judged checks, and reporting them as though a script passed them is the one thing the preflight forbids.

## Files

Contract — binding, one home per rule:

- `references/contract/visual.md` — house style, style selection, engine parameters and version facts, proportions, character and environment rendering, integration, lighting, background, resolution and split, exclusion policy, prompt discipline.
- `references/contract/gates.md` — genre and subgenre lock, register, risk gear and lever cap, no-props rule, conflict order, banned prompt language, capability limits, **craft versus decision**, **batch differentiation**.
- `references/contract/records.md` — character record, location record, source and version selection, reference roles, output delta, delivery shape, **batch ledger**.

Pipeline — procedures, numbered, reference the contract:

- `references/pipeline/design.md` — batch layer, 6-layer design stack, 7-point blueprint with per-point sources, prompt budget and its counting method, **the single preflight**, drift repair.
- `references/pipeline/sheet.md` — identity sheet, costume sheet, asset sheet; layout, occupancy, assembly scaffolds.
- `references/pipeline/gpt-sheet.md` — GPT Image 2 sheet design, layout reuse, MJ-syntax conversion.
- `references/pipeline/scene.md` — first scene base, character placement, composition, signage.
- `references/pipeline/scene-edit.md` — fixed-view variations, new views, available control, returned-image checks.
- `references/pipeline/outpaint.md` — controlled crop completion.
- `references/pipeline/asset-chain.md` — Midjourney style base to GPT Image 2 structured assets and first frames.

Bank — lookup and diagnosis sections:

- `references/bank/face.md` — 16 face parameters in eye-width units, **identity-set derivation**, editorial and glamour presets, six archetype mood sets, charm, gaze and turn, face drift diagnosis.
- `references/bank/framing.md` — canvas choice by use, vertical 9:16 composition and safe areas, widescreen, portrait, sequence consistency.
- `references/bank/truth.md` — three questions, ten dimensions, contradictions, thesis, posture, identity layers, ensemble differentiation, prompt-ready blocks.
- `references/bank/costume.md` — motif seeds, **seed derivation from the script**, gravity topologies, texture matrices, persona makeup, glamour hair, ensemble matrix.
- `references/bank/form.md` — silhouette, value hierarchy, colour system, palette saturation discipline, token-frequency quota, render-vocabulary budget, reference synthesis.
- `references/bank/material.md` — material system and light behaviours, composition and restraint, genre aesthetic modules, diagnostic checks.
- `references/bank/boldness.md` — ten levers, anti-conservative rules, under- and over-shoot detection, bold palettes and silhouettes.
- `references/bank/density.md` — layers, edges, nodes, pattern coverage, density gradient, four-clause template, **band spread across a batch**.

Calibration:

- `references/demos.md` — three worked demos (two editorial, one glamour) that clear the batch check against each other, all with 7 blueprint points and a counted preflight.

Tooling:

- `scripts/preflight.py` — the mechanical half of the preflight: word budget, colour and material caps, banned words, required craft elements, identity-set derivation, and batch differentiation against a ledger. Does not judge.
