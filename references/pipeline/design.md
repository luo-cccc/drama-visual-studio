# Pipeline: Design Mode

Read [../contract/visual.md](../contract/visual.md) and [../contract/gates.md](../contract/gates.md) first. This file owns the design-mode process: the 6-layer stack, the 7-point blueprint, prompt assembly, the single preflight, and drift repair.

Layer content lives in the bank: character truth in [../bank/truth.md](../bank/truth.md); costume systems in [../bank/costume.md](../bank/costume.md); density in [../bank/density.md](../bank/density.md); form judgement in [../bank/form.md](../bank/form.md), material and restraint in [../bank/material.md](../bank/material.md) and [../bank/boldness.md](../bank/boldness.md). Layout details live in [sheet.md](sheet.md).

Design mode answers two questions in order: **who is this person**, then **what are they wearing**. The failure to avoid is a beautiful mannequin — a couture look with no one inside it. The visual base is a floor, not a subject: render vocabulary tells the model how to render, never who is standing there.

## 1. Select the design output mode

| Mode | What it is | When |
| --- | --- | --- |
| **Mode A — identity sheet** (default) | one 16:9 sheet: three full-body orthographic views left, 2×2 bust grid right | new character, concept sheet, gameplay or drama asset |
| **Mode A-Split** | turnaround sheet + face sheet, identity block reused word-for-word | identity-critical characters reused across many shots, or an engine that cannot hold seven panels |
| **Mode A-Compact** | the single-sheet layout trimmed to 270–310 words | engines with hard prompt limits, or a draft; never a delivery asset |
| **Mode B — exploration** | 3 contrasting Genre + Truth + Motif + Silhouette combinations at one locked gear | broad or ambiguous briefs |
| **Portrait** | head-to-waist half body | a one-off look, a quick read, no costume structure needed |

Mode A layout, body occupancy, per-cell scoping, and backgrounds are specified in [sheet.md](sheet.md). Do not invent a different layout here. State the target canvas and engine with the mode.

## 2. The 6-layer design stack

Build in this order. Do not start with the costume.

| Layer | Question | Output | Source |
| --- | --- | --- | --- |
| **1. Character truth** | Who is this, and what evidence do they wear? | Three answers + imperfections + one contradiction + design thesis + posture | [../bank/truth.md](../bank/truth.md) |
| **2. Motif growth** | What single metaphor grows the outfit? | One seed, grown by the three growth rules | [../bank/costume.md](../bank/costume.md) §1 |
| **3. Gravity topology** | Where does detail concentrate? | One of five topologies + back-view resolution | [../bank/costume.md](../bank/costume.md) §2 |
| **4. Ornament density** | Is there enough material in it? | Layers, treated edges, node count, pattern coverage | [../bank/density.md](../bank/density.md) |
| **5. Aesthetic order** | Why does it look good? | Silhouette, value, palette, material, restraint, levers | [../bank/form.md](../bank/form.md), [../bank/material.md](../bank/material.md) §1–2, [../bank/boldness.md](../bank/boldness.md) |
| **6. House render** | How does it read as game CG with an anime face? | Anime eye/lip design, BJD porcelain finish, sculpted hair, persona light, engine + resolution | [../contract/visual.md](../contract/visual.md) §4–8 |

**Layer 4 is the answer to "it came out plain".** Layers 1–3 decide what the design means; Layer 5 decides whether it looks good; Layer 4 decides whether there is anything in it to look at. Skipping it and reaching for `elaborate` is the most common cause of a tasteful, correct, boring sheet.

## 3. The 7-point blueprint — and where each point comes from

Present the blueprint in Chinese, in this order. **Each point has exactly one source file. Do not invent a point's content from memory, and do not omit a point.**

| # | Point | Must contain | Read from |
| --- | --- | --- | --- |
| 1 | 题材、子类型与风险档 | lock line, aesthetic module, pigment family, silhouette family, gear | [../contract/gates.md](../contract/gates.md) §1–3; [../bank/material.md](../bank/material.md) §3 |
| 2 | 角色事实与设计论点 | three answers, age/gender/status read, imperfections (editorial two; glamour zero or one), one contradiction and its direction, one-sentence thesis with a physical anchor | [../bank/truth.md](../bank/truth.md) |
| 3 | 核心视觉母题 | the seed, plus the three growth answers — what supports it, where pressure lands, what the hands do (empty, never holding) | [../bank/costume.md](../bank/costume.md) §1 |
| 4 | 视觉重心与背部叙事 | topology, back resolution, hero and supporting zones, understructure for extreme volume | [../bank/costume.md](../bank/costume.md) §2 |
| 5 | **装饰密度（计数）** | visible layers in order and where each shows its edge; the edge inventory with one trim language; node count with each node's structural job and descending scale; the motif family at three scales and its coverage level — **all four factors counted, never described as an adjective** | [../bank/density.md](../bank/density.md) §1–4, §8 |
| 6 | 审美秩序 | silhouette family, three-value plan, palette relationship with HEX for every colour, material contrasts and their light behaviours, focal point, open area, one chromatic anchor, gear, levers used, one rule deliberately broken | [../bank/form.md](../bank/form.md) §1–3 and [../bank/material.md](../bank/material.md) §2; [../bank/boldness.md](../bank/boldness.md) |
| 7 | 半写实渲染与微妆 | proportions with shoulder-waist-hip; the **identity-set** face parameters in band; anime eye and lip design; BJD porcelain finish; hair clump structure and wisps; the one alive asymmetry; the bottom-right macro expression; persona light; engine and target canvas | [../contract/visual.md](../contract/visual.md) §4–8; [../bank/face.md](../bank/face.md) §2–6; [../bank/costume.md](../bank/costume.md) §4 |

Rules for the blueprint:

- **HEX belongs in point 6 and only there.** The English prompt uses plain-language colour names.
- **A blueprint missing any point is not a finished design.** Point 5 is the one most often skipped; see §6 preflight.
- **Point 7 names parameters, not adjectives.** "Refined anime face" is not a design decision; "iris fill 0.9, upper lid coverage 24%, canthal tilt +6°" is. Write the visible consequence in the prompt, the parameter here.
- **A blueprint may not claim more than the prompt contains.** §6B checks this before delivery.
- Keep the work proportional: a one-off portrait may abbreviate to the lock line, thesis, identity block, face parameters, and palette. A design sheet or a recurring character gets all seven points.

See [../demos.md](../demos.md) for two calibrated examples with all seven points filled.

## 4. Compose the free-flow English prompt

Continuous prose, no bracketed headers, no numeric percentages. Budget for the full single-sheet prompt:

| Block | Words | Notes |
| --- | --- | --- |
| Canvas, render base, layout header | 185–205 | background, four-pillar base, lighting, posture, seven-panel layout with per-cell scoping |
| Visual narrative — editorial | 300–335 | thesis, identity block incl. anime face, evidence, hair, motif and outfit, gravity/back, palette, risk |
| Visual narrative — glamour / ceremonial | 340–380 | the same, plus the density block: layer, edge, node, pattern |
| Consistency footer | ~17 | cross-view consistency line |
| **Total — editorial** | **500–540** | |
| **Total — glamour / ceremonial** | **540–585** | |

- The density block takes 80–110 words and comes after the face and hair. Write it with the four-clause template in [../bank/density.md](../bank/density.md) §6. If you must cut, cut palette elaboration first, then the back-view ornament description; never cut the face, the per-cell scoping, or the edge/pattern clauses.
- The four-pillar base costs roughly 40 words of header. Take them from palette elaboration, never from the face, the motif, or the per-cell scoping.
- Mode A-Split budgets: turnaround header 100–120 + narrative 170–210; face-sheet header 90–110 + narrative 130–170.
- Mode A-Compact: keep the layout sentence, the four-pillar base, the eye design, and the thesis; cut palette and material elaboration to one clause each; 270–310 words.
- The eye design lives in the identity block: lid line, crease, iris fibre, limbal ring, secondary reflection, meniscus. It is the invariant that makes two renders the same person.

Narrative order:

1. Thesis and character truth: thesis with a physical anchor, invariant identity block (including shoulder-waist-hip and skin), look-specific evidence.
2. Face, hair, micro-makeup: bone structure, iris fibre, eye/lip tinting, one loose strand, strand separation.
3. Motif and outfit: construction, layers, closures, fabric behaviour and weight, the seed growing through edges and ornaments.
4. Gravity and back view: where density concentrates, what the back resolves.
5. Genre lock embedded: the subgenre shows in silhouette, material, and pigment; no scene or world description.
6. Aesthetic order embedded: silhouette family, value masses, palette relationship and accent, material contrasts, one primary open area — woven into garment sentences, never appended as a summary.
7. One deliberate risk: the rule broken and the unexpected element; the face stays the focal point.

Transport review vocabulary into visible description, per [../contract/gates.md](../contract/gates.md) §6. Banned in the English prompt: bracketed section headers, numeric percentages, review vocabulary, empty fluff adjectives, richness adjectives, value words used as evidence, shader parameters.

## 5. Exclusions and engine attachment

Follow [../contract/visual.md](../contract/visual.md) §11 for the canonical policy. The engine table is in §3; the `--no` word rules and the per-engine forms are in §11. Do not restate them here.

## 6. Preflight — the single acceptance gate

This is the only acceptance check in this skill. The tables in [../bank/material.md](../bank/material.md) §4 and [../bank/boldness.md](../bank/boldness.md) §3 and §7 are **diagnostic** tools for finding what is wrong; they are not delivery thresholds and do not override this section.

### 6A. Two kinds of check, and be honest about which is which

Some lines below are **counted** — a number can be produced and compared. Others are **judged** — they need a viewer's eye. Do not present a judged line as though a count proved it. Where a line is judged, the honest report names the specific thing observed, not the word "passed".

| Kind | Lines | How to report |
| --- | --- | --- |
| **Counted** | blueprint completeness; layers; edge rate; node count; pattern coverage; palette token frequencies; accent cap; material count; lever count; prompt word count; blueprint-to-prompt traceability | report the numbers |
| **Judged** | silhouette at 10%; value hierarchy; face wins; commercial read; density gradient; no accidental clutter; whether the one risk actually reads as a risk | name what you saw, and what you would change if it is wrong |

**Where the numeric bands come from.** The bands in 6C and 6D are a *compilation*, not an authority: they restate one register's column of the tables in [../bank/density.md](../bank/density.md) §8 and [../contract/gates.md](../contract/gates.md) §3 so the check can run without opening those files. If a band ever disagrees with its source, **the source wins and this table is the bug.** The sources are the four-factor minima in [../bank/density.md](../bank/density.md) §8, the node caps in §3, the colour caps in [../bank/form.md](../bank/form.md) §3B, and the lever cap in [../contract/gates.md](../contract/gates.md) §3.

### 6B. Blueprint-to-prompt traceability — run this first

A blueprint is a promise; the prompt is the delivery. Every element counted in point 5 must appear in the prompt body with matching wording. This check exists because a blueprint can pass while the prompt silently omits an item — the failure mode is real and has occurred in this pack's own demos.

For each layer, each treated edge, each ornament node, and each pattern scale named in point 5:

1. Find the clause in the prompt that carries it.
2. If it is missing, either add it to the prompt or remove it from the blueprint. **Do not deliver a blueprint claiming more than the prompt contains.**
3. Count once more after editing; edits move the numbers.

The same applies to point 6's palette: the colour named as base, anchor, and accent in the blueprint must be the colours the prompt actually repeats most, second-most, and least. Run the token count, do not estimate it.

### 6C. Editorial preflight

| Check | Kind | Pass condition | If it fails |
| --- | --- | --- | --- |
| Blueprint complete | counted | all 7 points present, point 5 counted | fill the missing point before writing the prompt |
| **Blueprint traced into prompt** | counted | every layer, edge, node, and pattern scale from point 5 appears in the prompt; palette roles match measured token order | add the missing clause or cut the unfulfilled promise |
| **Palette token count** | counted | accent ≤ 2; anchor ≤ 4; base ≤ 8; no single material term > 5; base terms outnumber the accent | cut to the role's cap, keeping the accent on the focal point |
| **Prompt word budget** | counted | 500–540 editorial | cut palette elaboration first, then back-view ornament; never the face, the per-cell scoping, or the edge/pattern clauses |
| Density factors | counted | layers 2–3 working / 4–5 high-status; edge rate 60%+; nodes 4 (1 hero + 3 supporting); pattern bare or banded — and banded at minimum for any high-status figure | add the floating layer, one trim language across several edges, a metal edge band, or one tone-on-tone band |
| Life traces | counted | two visible at full-body distance, plus one contradiction from directions 1–6, named in the blueprint | return to [../bank/truth.md](../bank/truth.md) |
| Materials | counted | at least two light behaviours; one material surprise; no more than four named fabric types | add a translucent or heavy element; if five materials, remove two |
| Restraint | counted | one hero node plus three supporting; one primary open area named | delete the weakest node |
| Face parameters in band | counted | identity-set parameters inside [../contract/visual.md](../contract/visual.md) §4; no parameter pushed past the chibi or uncanny guard | pull back to the editorial preset in [../bank/face.md](../bank/face.md) §3 |
| Silhouette | judged | identifiable at 10% size, one family, one contrast shape | change the family or widen the hem/shoulder contrast |
| Value | judged | clear dark / light / focal hierarchy in grayscale; focal contrast at face, chest, or hands | increase value separation; move the contrast off the hem |
| Palette reads as named | judged | one relationship visibly present; one chromatic anchor legible at thumbnail after desaturation; dark mass has a named temperature | name the relationship, delete extra hues, give the dark mass a temperature |
| Face wins | judged | the face is the first fixation at thumbnail size | quieten the loudest competing ornament |
| Render integrity | counted | the prompt names the anime eye design, the BJD skin finish, one material light behaviour, and one key-light direction | add the missing block and one weight clause; if render tokens outnumber character facts, cut render vocabulary |
| Commercial read | judged | at thumbnail size it reads as a product — cover, key art, figure box | add or strengthen the chromatic anchor, raise silhouette contrast, add one iconographic element |
| Canvas fits the use | judged | the ratio matches the shot's job per [../bank/framing.md](../bank/framing.md) §1; figure occupancy and safe areas match the canvas | change the canvas and recompose; do not crop a sheet |

### 6D. Glamour preflight

| Check | Kind | Pass condition | If it fails |
| --- | --- | --- | --- |
| Blueprint complete | counted | all 7 points present, point 5 counted | fill the missing point |
| **Blueprint traced into prompt** | counted | every layer, edge, node, and pattern scale from point 5 appears in the prompt | add the missing clause or cut the promise |
| **Palette token count** | counted | accent ≤ 2 (binding); base terms outnumber the accent at least 2:1; **silver and other dual colour-and-material words counted once as colour and once as material**, and both caps applied | cut the accent to 2; if a metal word is doing both jobs, convert some uses to a different material name |
| **Prompt word budget** | counted | 540–585 glamour / ceremonial | cut palette elaboration first, then back-detail ornament |
| Density factors | counted | layers 5–6; edge rate 80%+; nodes 8–15 descending; pattern fielded or allover; at least one floating layer | add the missing factor, not another node |
| Top-zone richness | counted | the head carries at least two distinct ornament groups | add one head group before anything lower |
| Hair as a system | counted | mass and length, crown volume, face framing, texture behaviour, inner streaks, headpiece inventory with hanging depth — all six written | see [../bank/costume.md](../bank/costume.md) §5A |
| Face parameters in band | counted | glamour preset in [../bank/face.md](../bank/face.md) §3; iris fill and lid coverage raised, canthal tilt positive; no chibi drift | re-run the preset; check eye width to face ≤ 1.2 and iris fill ≤ 0.95 |
| No props | counted | hands empty, in hair, or resting | see [../contract/gates.md](../contract/gates.md) §4 |
| Accent cap | counted | 2, binding | cut to 2 |
| Density gradient | judged | head > chest > waist > hem, each zone strictly lighter than the one above; at least one plain run or bare skin below the waist | move ornament upward; never add more below to even it out |
| Face wins | judged | the face holds the frame at thumbnail size | quieten or raise the competing group |
| **Charm present** | judged | one alive detail (asymmetry, gaze, tilt); two catchlights; one matte zone; the turn specified. Expense is not charm — see [../bank/face.md](../bank/face.md) §5 | add the asymmetry and the second catchlight; remove one ornament group and spend it on the face |
| Contradiction | judged | one Sacred / Dangerous signal (direction 7); zero damage | replace damage with a lethal signal — crimson irises, one impossible detail |
| Specular near the face | judged | one glossed element in the head or chest zone | add a glossed lip, wet lower lid, or polished metal near the cheek |
| No accidental clutter | judged | every node has a structural job | give each node a closure or junction, or remove it |

### 6E. Both registers

The face is the first fixation. Everything else is ranked behind it.

Report the preflight as a short list: the counted numbers, then the judged observations in one line each. Do not claim a visual pass on the strength of a count. A prompt does not lock geometry — passing the preflight is a check on the design and the wording, not a guarantee of the render.

Run the mechanical half with the checker rather than by eye where possible: `scripts/preflight.py` parses a finished prompt and reports word count, colour and material term frequencies against the caps, the banned-word list, and whether the named identity elements are present. Use it for the counted lines, then judge the rest yourself.

## 7. Drift repair

When a returned sheet is wrong, diagnose and issue a targeted fix. Do not regenerate blind. Report observed differences first; give the correction prompt only when asked.

| Symptom | Cause | Fix |
| --- | --- | --- |
| Four busts look identical | expression not scoped per cell | restate `top-left fully neutral baseline` and `bottom-right only: ...` |
| Panels merge into one figure | grid dividers suppressed by an outer-frame ban | add `thin internal dividers between the four cells` in the positive; keep the outer-frame ban |
| Outfit differs across views | too much detail per view | switch to Mode A-Split; shorten the outfit sentence; raise the consistency line |
| Face lost its identity | detail words spent on full-body panels | move pores/scar/lip detail into the face cells; keep only silhouette facts in the body copy |
| Extra or missing panel | layout sentence ambiguous | state the count without numbers: `three views on the left, four bust cells on the right` |
| Glassy mobile-game skin | BJD finish described as gloss rather than porcelain | add `smooth porcelain skin with a soft subsurface glow, matte cheek with a controlled specular`; cut `glossy, dewy, wet-look` |
| Blown highlights, lost costume detail | light described as "bright" instead of as a direction and a value | name the key direction, add `clean luminance rolloff`, move the light mass off pure white |
| Everything reads grey | palette built from neutral black; no chromatic anchor | give the dark mass a temperature bias; add one structural anchor colour |
| Cloth looks like a stiff shell | no weight or fold structure | add `physically-plausible cloth simulation` and one hang clause |
| Hair reads as plastic cards | mass described, clump structure omitted | add `grouped locks with sculpted strand clumps, a soft anime-style highlight band, no card-like clumping` |
| Too clean, no character | design-stage failure | return to Layer 1 — add the second life trace or the status marker |
| Looks like one plain robe | layer count too low; no floating or translucent layer | add the outer translucent layer and one floating sash/veil; name where the inner layer shows |
| Ornament requested but reads simple | richness written as an adjective | delete `elaborate/intricate/ornate`; rewrite with the four-clause template in [../bank/density.md](../bank/density.md) §6 |
| Every edge looks raw | no trim language | one clause across several edges: `collar, cuffs and hems banded in the same silver filigree` |
| Fabric looks printed | pattern at one scale only | carry the motif at three scales — node, band, micro field |
| Technically perfect, nobody home | render vocabulary substituted for character facts | return to Layer 1; restore the thesis and one life trace; cut render repeats |
| Drifted chibi | eye ratio or head count out of band | restate the head count and `large almond eyes` without `very large`; check against [../contract/visual.md](../contract/visual.md) §4 |
| Drifted uncanny half-realism | the face was pushed realistic | restate `defined upper lid line`, `minimal nose bridge`, and add `refined anime facial design` |

If the drift is broad, recommend returning to the last suitable version and reapplying the still-required changes, rather than patching a drifted result.

Record which fix worked in the project's own notes, not in this file.

## 8. Delivery

- Lock line; 7-point blueprint; one English prompt; engine-appropriate exclusions; a short note on inferred details; engine and target canvas.
- For a recurring character, attach the compact character record from [../contract/records.md](../contract/records.md) §1.
- Do not promise exact identity, proportion, layout, pixel, or multi-view consistency.
