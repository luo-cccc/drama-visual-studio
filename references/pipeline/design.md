# Pipeline: Design Mode

Read [../contract/visual.md](../contract/visual.md) and [../contract/gates.md](../contract/gates.md) first. This file owns the design-mode process: the batch layer, the 6-layer design stack, the 7-point blueprint, prompt assembly, the single preflight, and drift repair.

Layer content lives in the bank: character truth in [../bank/truth.md](../bank/truth.md); costume systems in [../bank/costume.md](../bank/costume.md); density in [../bank/density.md](../bank/density.md); form judgement in [../bank/form.md](../bank/form.md), material and restraint in [../bank/material.md](../bank/material.md) and [../bank/boldness.md](../bank/boldness.md). Layout details live in [sheet.md](sheet.md).

Design mode answers two questions in order: **who is this person**, then **what are they wearing**. The failure to avoid is a beautiful mannequin — a couture look with no one inside it. The visual base is a floor, not a subject: render vocabulary tells the model how to render, never who is standing there.

## 1. Select the design output mode

| Mode | What it is | When |
| --- | --- | --- |
| **Mode A — identity sheet** (default) | one 16:9 sheet: three full-body orthographic views left, 2×2 bust grid right | new character, concept sheet, gameplay or drama asset |
| **Mode A-Split** | turnaround sheet + face sheet, identity block reused word-for-word | identity-critical characters reused across many shots, or an engine that cannot hold seven panels |
| **Mode A-Compact** | the single-sheet layout trimmed to 270–310 words | engines with hard prompt limits, or a draft; never a delivery asset |
| **Mode B — exploration** | 3 contrasting Genre + Truth + Motif + Silhouette combinations at one locked gear | broad or ambiguous briefs |
| **Mode C — costume variant** | a second look for an existing character: identity block reused verbatim, only the look layer is designed | new outfit, hairstyle, ornament set, or occasion change on a character that already exists |
| **Portrait** | head-to-waist half body | a one-off look, a quick read, no costume structure needed |

Mode A layout, body occupancy, per-cell scoping, and backgrounds are specified in [sheet.md](sheet.md). Do not invent a different layout here. State the target canvas and engine with the mode.

### Mode C — design a variant, not a person

Mode C is the one mode whose subject already exists. Run it when the request is a new outfit rather than a new character: 换装、换发型、加饰品、场合变更.

**What changes:**

1. **Start from the character record, not from layer 1.** The identity block, palette roles, and confirmed finish come from [../contract/records.md](../contract/records.md) §1 and are reused word for word. Layers 2–5 design the look; layer 6 styles it inside the inherited identity.
2. **Do not run [../bank/face.md](../bank/face.md) §2A.** That procedure derives an identity set from Position facts, and re-running it for an outfit change returns a different person. Restate the record's ten values instead.
3. **Derive the seed from this outfit's occasion, not the character's whole life.** A variant's seed answers "what is this look for", so a night crossing and a wedding produce different seeds from the same person. The procedure is [../bank/costume.md](../bank/costume.md) §1C, applied to the occasion.
4. **Keep the silhouette family and key colour family by default.** They are how the viewer recognizes the character — [../contract/gates.md](../contract/gates.md) §9A. Change them only when the character's status or role has actually changed, and state the reason in the blueprint.
5. **Clear the look-separation test.** At least three of four look factors — trim language, motif family, gravity topology, node distribution — must differ from that character's previous look. Two outfits sharing all four are one outfit with a different name.

**What the delivery drops:** the batch-differentiation vector against other characters. A variant is not compared to the cast on axes 1 and 2. It carries `identity locked` and its four look factors instead, recorded as a `↳` line in the ledger per [../contract/records.md](../contract/records.md) §8.

## 2. The design stack

Build in this order. Do not start with the costume. Layer 0 is the batch, and the six design layers follow it.

**Layer 0, before layer 1: read the batch ledger.** The ledger format is [../contract/records.md](../contract/records.md) §8 and the axes are [../contract/gates.md](../contract/gates.md) §9. Design in isolation and the checks in §6 will pass on a character who is the previous one with a different name, because every single-character check is satisfied. Layer 0 costs one read and one line of comparison, and it is the only mechanism in this skill that can see the project rather than the sheet.

| Layer | Question | Output | Source |
| --- | --- | --- | --- |
| **0. Batch ledger** | Which design values are already spent in this project? | The nine-axis vector to clear, and the axes already taken | [../contract/records.md](../contract/records.md) §8; [../contract/gates.md](../contract/gates.md) §9 |
| **1. Character truth** | Who is this, and what evidence do they wear? | Three answers + imperfections + one contradiction + design thesis + posture | [../bank/truth.md](../bank/truth.md) |
| **2. Motif growth** | What single metaphor grows the outfit? | One seed derived from the script's conflict by §1C, grown by the three growth rules | [../bank/costume.md](../bank/costume.md) §1 |
| **3. Gravity topology** | Where does detail concentrate? | One of five topologies + back-view resolution | [../bank/costume.md](../bank/costume.md) §2 |
| **4. Ornament density** | Is there enough material in it? | Layers, treated edges, node count, pattern coverage — placed at a point in the band that differs from the batch | [../bank/density.md](../bank/density.md) §1–4, §8A |
| **5. Aesthetic order** | Why does it look good? | Silhouette, value, palette, material, restraint, levers | [../bank/form.md](../bank/form.md), [../bank/material.md](../bank/material.md) §1–2, [../bank/boldness.md](../bank/boldness.md) |
| **6. House render** | How does it read as game CG with an anime face? | Anime eye/lip craft, the derived identity set, BJD porcelain finish, sculpted hair, persona light, engine + resolution | [../contract/visual.md](../contract/visual.md) §4–8; [../bank/face.md](../bank/face.md) §2A |

**Layer 4 is the answer to "it came out plain".** Layers 1–3 decide what the design means; Layer 5 decides whether it looks good; Layer 4 decides whether there is anything in it to look at. Skipping it and reaching for `elaborate` is the most common cause of a tasteful, correct, boring sheet.

**Layer 2 derives the seed from the script.** A genre-to-seed routing table would narrow the library to two or three entries per subgenre and hand the same subgenre the same motif. The seed comes from the character's conflict instead — see [../bank/costume.md](../bank/costume.md) §1C — and the library is calibration only.

**Layer 6 carries two kinds of instruction.** Craft strings (`radial iris fibre with a darker limbal ring`) are reused verbatim; identity values (iris fill, facial index, lip ratio) are derived per character by [../bank/face.md](../bank/face.md) §2A. Mixing the two is the mechanism behind a cast of identical faces — [../contract/gates.md](../contract/gates.md) §8.

## 3. The 7-point blueprint — and where each point comes from

Present the blueprint in Chinese, in this order. **Each point has exactly one source file. Do not invent a point's content from memory, and do not omit a point.**

| # | Point | Must contain | Read from |
| --- | --- | --- | --- |
| 1 | 题材、子类型与风险档 | lock line, aesthetic module, pigment family, silhouette family, gear | [../contract/gates.md](../contract/gates.md) §1–3; [../bank/material.md](../bank/material.md) §3 |
| 2 | 角色事实与设计论点 | three answers, age/gender/status read, imperfections (editorial two; glamour zero or one), one contradiction and its direction, one-sentence thesis with a physical anchor | [../bank/truth.md](../bank/truth.md) |
| 3 | 核心视觉母题 | the seed **derived from the script's conflict** (§1C), plus the three growth answers — what supports it, where pressure lands, what the hands do (empty, never holding); if a library seed was used instead, say so | [../bank/costume.md](../bank/costume.md) §1A, §1C |
| 4 | 视觉重心与背部叙事 | topology, back resolution, hero and supporting zones, understructure for extreme volume; the topology must clear ledger axis 3 | [../bank/costume.md](../bank/costume.md) §2; [../contract/gates.md](../contract/gates.md) §9 |
| 5 | **装饰密度（计数）** | visible layers in order and where each shows its edge; the edge inventory with one trim language and the deliberately-raw set; node count with each node's structural job and descending scale; the motif family at three scales and its coverage level — **all four factors counted, and placed at a different point in the band than the batch's previous character** | [../bank/density.md](../bank/density.md) §1–4, §8A |
| 6 | 审美秩序 | silhouette family, three-value plan, palette relationship with HEX for every colour, material contrasts and their light behaviours, focal point, open area, one chromatic anchor, gear, levers used, one rule deliberately broken | [../bank/form.md](../bank/form.md) §1–3 and [../bank/material.md](../bank/material.md) §2; [../bank/boldness.md](../bank/boldness.md) |
| 7 | 半写实渲染与微妆 | proportions with shoulder-waist-hip; the **derived identity set** (§2A) named as values, not adjectives; the anime eye and lip craft strings; BJD porcelain finish; hair clump structure and wisps; the one alive asymmetry; the bottom-right macro expression; persona light; engine and target canvas | [../contract/visual.md](../contract/visual.md) §4–8; [../bank/face.md](../bank/face.md) §2A–6; [../bank/costume.md](../bank/costume.md) §4 |

Rules for the blueprint:

- **HEX belongs in point 6 and only there.** The English prompt uses plain-language colour names.
- **A blueprint missing any point is not a finished design.** Point 5 is the one most often skipped; see §6 preflight.
- **Point 7 names parameters, not adjectives.** "Refined anime face" is not a design decision; "iris fill 0.9, upper lid coverage 24%, canthal tilt +6°" is. Write the visible consequence in the prompt, the parameter here.
- **A blueprint may not claim more than the prompt contains.** §6B checks this before delivery.
- Keep the work proportional: a one-off portrait may abbreviate to the lock line, thesis, identity block, face parameters, and palette. A design sheet or a recurring character gets all seven points.

**Mode C changes what points 2 and 7 contain, and nothing else.**

| Point | Mode A / B | Mode C variant |
| --- | --- | --- |
| 1 锁定 | lock line with silhouette and key colour chosen for a new character | same fields; **silhouette and key colour inherited**, and the line says so |
| 2 角色事实与设计论点 | three answers about who this person is | the **occasion** the outfit is for, plus a thesis about this look; the person is already established |
| 3 核心视觉母题 | seed from the character's conflict | seed from **this occasion's** conflict |
| 4 视觉重心与背部叙事 | topology for this character | topology for **this look**, differing from the previous look |
| 5 装饰密度（计数） | four factors at a point in the band | same counting, **placed differently** from the previous look |
| 6 审美秩序 | full aesthetic order | same, with palette roles inherited and only the accent allocation re-decided |
| 7 半写实渲染与微妆 | identity set **derived** per §2A | identity set **restated verbatim** from the record; do not re-derive |

A Mode C blueprint that re-derives the identity set, or that changes the silhouette without a status reason, is not a variant — it is a recast, and it should be delivered as a new character with a new lock line instead.

See [../demos.md](../demos.md) for three calibrated examples with all seven points filled.

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

**Which word count is the budget measured against.** `scripts/preflight.py` counts alphabetic words before the engine flags, so `16:9`, `2x2`, and `two-centimetre` contribute zero, one, and one. A whitespace token count of the same prompt reads 10–15 words higher, because it counts the numerals and flags. Both numbers are correct measurements of different things: the budget is on **prose words**, which is the script's count. When reporting a word count, say which method produced it, and do not compare a script count against a whitespace count as though the difference were an error.

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
| **Counted** | blueprint completeness; layers; edge rate; node count; pattern coverage; palette token frequencies; accent cap; material count; lever count; prompt word count; blueprint-to-prompt traceability; identity-set derivation; batch differentiation | report the numbers |
| **Judged** | silhouette at 10%; value hierarchy; face wins; commercial read; density gradient; no accidental clutter; whether the one risk actually reads as a risk; whether the face is visibly a different person from the batch's previous character | name what you saw, and what you would change if it is wrong |

**The last judged line has no counted substitute.** `Identity set derived` and `Batch differentiation` are counted *procedures* — they check that ten values were derived from facts and that nine axes were compared. Neither proves the resulting face looks different, because a derived set can still land on a near neighbour. When the batch is large enough to matter, say that the visual comparison is pending until the images exist.

**Where the numeric bands come from.** The bands in 6C and 6D are a *compilation*, not an authority: they restate one register's column of the tables in [../bank/density.md](../bank/density.md) §8 and [../contract/gates.md](../contract/gates.md) §3 so the check can run without opening those files. If a band ever disagrees with its source, **the source wins and this table is the bug.** The sources are the four-factor minima in [../bank/density.md](../bank/density.md) §8, the band-spread rule in §8A, the node caps in §3, the colour caps in [../bank/form.md](../bank/form.md) §3B, the lever cap in [../contract/gates.md](../contract/gates.md) §3, and the batch axes in [../contract/gates.md](../contract/gates.md) §9.

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
| Face parameters in band | counted | identity-set parameters inside [../contract/visual.md](../contract/visual.md) §4; no parameter pushed past the chibi or uncanny guard | pull back to the band, not to the preset; derive the value with [../bank/face.md](../bank/face.md) §2A |
| **Identity set derived, not defaulted** | counted | each of the ten identity parameters traces to a Position fact per [../bank/face.md](../bank/face.md) §2A-1; the anchoring three (facial index, mouth width, inter-canthal distance) are named in the blueprint as values | run §2A-1 and §2A-3; a parameter with no fact behind it is a default |
| **Batch differentiation** (Mode A/B) | counted | axes 1–2 (silhouette, key colour family) differ from every ledger row; axes 3–9 clear at least five of nine total; the vector is reported against the ledger | return to Layer 0; redesign the repeating axis, not the whole character — [../contract/gates.md](../contract/gates.md) §9 |
| **Variant integrity** (Mode C) | counted | identity block is the record's, word for word — no re-derived value; silhouette and key colour inherited, or a stated status change; **three of four look factors** (trim, motif, topology, node distribution) differ from that character's previous look | restore the record's identity block verbatim; change a look factor — [../contract/gates.md](../contract/gates.md) §9A |
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
| Density factors | counted | layers 5–6; edge rate 80%+; nodes 8–15 descending; pattern fielded or allover; at least one floating layer — **and the four values sit at a different point in the band than the previous character in this register** | add the missing factor, not another node; then move a value within the band per [../bank/density.md](../bank/density.md) §8A |
| Top-zone richness | counted | the head carries at least two distinct ornament groups | add one head group before anything lower |
| Hair as a system | counted | mass and length, crown volume, face framing, texture behaviour, inner streaks, headpiece inventory with hanging depth — all six written | see [../bank/costume.md](../bank/costume.md) §5A |
| Face parameters in band | counted | glamour values inside [../bank/face.md](../bank/face.md) §3 and [../contract/visual.md](../contract/visual.md) §4; iris fill ≤ 0.95, eye width to face ≤ 1.2; no chibi drift | pull into the band; derive the value, do not re-run the preset |
| **Identity set derived, not defaulted** | counted | each of the ten identity parameters traces to a Position fact per [../bank/face.md](../bank/face.md) §2A-1; facial index is derived, never assumed 1.4–1.45 | run §2A-1; the glamour preset's facial index is a slot, not a value |
| **Batch differentiation** (Mode A/B) | counted | axes 1–2 differ from every ledger row; at least five of nine differ; the vector is reported against the ledger | return to Layer 0 — [../contract/gates.md](../contract/gates.md) §9 |
| **Variant integrity** (Mode C) | counted | identity block is the record's, word for word; silhouette and key colour inherited or a stated status change; **three of four look factors** differ from that character's previous look | restore the identity block; change a look factor — [../contract/gates.md](../contract/gates.md) §9A |
| No props | counted | hands empty, in hair, or resting | see [../contract/gates.md](../contract/gates.md) §4 |
| Accent cap | counted | 2, binding | cut to 2 |
| Density gradient | judged | head > chest > waist > hem, each zone strictly lighter than the one above; at least one plain run or bare skin below the waist | move ornament upward; never add more below to even it out |
| Face wins | judged | the face holds the frame at thumbnail size | quieten or raise the competing group |
| **Charm present** | judged | one alive detail (asymmetry, gaze, tilt); two catchlights; one matte zone; the turn specified. Expense is not charm — see [../bank/face.md](../bank/face.md) §5 | add the asymmetry and the second catchlight; remove one ornament group and spend it on the face |
| Contradiction | judged | one direction-7 **signal**, and it differs from the batch's other direction-7 characters; zero damage. Directions 1–6 are legal for a deliberately fallen or working glamour character | replace damage with a lethal signal, and make the signal unlike the ledger's |
| Specular near the face | judged | one glossed element in the head or chest zone | add a glossed lip, wet lower lid, or polished metal near the cheek |
| No accidental clutter | judged | every node has a structural job | give each node a closure or junction, or remove it |

### 6E. Both registers

The face is the first fixation. Everything else is ranked behind it.

Report the preflight as a short list: the counted numbers, then the judged observations in one line each. Do not claim a visual pass on the strength of a count. A prompt does not lock geometry — passing the preflight is a check on the design and the wording, not a guarantee of the render.

**Two lines of the report are about the project, not the sheet** — `Identity set derived` and `Batch differentiation`. Report them against the ledger by name: `silhouette cocoon（账本 A 为 column）· key 土金宝石（A 骨白）· topology 4（A 5）· light 温和实用灯（A 高调珠光）· trim 铜棕皮革压边（A 窄银掐丝）· motif 蛇蜕鳞纹（A 五瓣星花）· face anchor 面部指数 1.52 / 眼裂 0.44（A 1.38 / 0.50）`. Without that line, "differentiated" is an assertion and not a check.

Run the mechanical half with the checker rather than by eye where possible: `scripts/preflight.py` parses a finished prompt and reports word count, colour and material term frequencies against the caps, the banned-word list, whether the named identity elements are present, and — with `--ledger --vector` — whether the batch vector actually differs from the rows supplied. Pass the vector from the blueprint; the prompt prose alone exposes only three or four of the nine axes, so a ledger check without it under-reports and cannot clear the five-of-nine rule. Use it for the counted lines, then judge the rest yourself. **It cannot judge whether the face is the same person as last time; only the derived values and your eye can.**

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
| **Every character looks like the same person** | the identity set was never derived; craft strings are standing in for decisions | run [../bank/face.md](../bank/face.md) §2A: take the Position triple, push the anchoring three (facial index, mouth width, inter-canthal distance) to different values, then re-derive the rest |
| **Every costume is the same outfit in a different colour** | the seed came from the library rather than the script's conflict; density sits at the same point in the band | derive the seed per [../bank/costume.md](../bank/costume.md) §1C; move layers, edges, nodes, and pattern to a different point per [../bank/density.md](../bank/density.md) §8A |
| **The whole cast reads as one design system** | no ledger was read at Layer 0 | build the ledger from [../contract/records.md](../contract/records.md) §8, then redesign the repeated axes — axes 1 and 2 are hard failures |

If the drift is broad, recommend returning to the last suitable version and reapplying the still-required changes, rather than patching a drifted result.

Record which fix worked in the project's own notes, not in this file.

## 8. Delivery

- Lock line; 7-point blueprint; one English prompt; engine-appropriate exclusions; a short note on inferred details; engine and target canvas.
- For a recurring character, attach the compact character record from [../contract/records.md](../contract/records.md) §1.
- Do not promise exact identity, proportion, layout, pixel, or multi-view consistency.
