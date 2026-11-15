# Bank: Face System — Parameters, Register Presets, Charm

Layer 6 material, and the highest-leverage file in this pack. The eye hierarchy is the first fixation and the design signature; everything else in a character is ranked behind it. Yet the face is the part most often left as adjectives. This file turns it into parameters.

Read this when designing a face, building a sheet, or diagnosing a face that came out wrong. The hard band limits that must never be violated are in [../contract/visual.md](../contract/visual.md) §4; this file supplies the dials inside those limits.

**The one rule that outranks every parameter here:** two renders are the same person when the eye design matches — lid line, crease, iris fibre, limbal ring, the shape of the cupid's bow, and the hairline. Those are identity. Everything else is mood, register, or drift.

## 1. Measuring unit

Use **eye width (EW)** — the width of one open palpebral fissure — as the unit for every face measurement. It scales with the face, so the ratios hold at any head count.

Do not write measurements into the English prompt. Use them here to decide, then write the visible consequence: `close-set eyes` / `wide-set eyes` / `a positive canthal tilt` / `a full iris that nearly fills the lid opening`.

## 2. The parameters

| # | Parameter | Measured as | Neutral band | Reads beyond the band |
| --- | --- | --- | --- | --- |
| 1 | **Inter-canthal distance** | inner corner to inner corner | 1.0–1.15 EW | < 0.9: intense, predatory, close-set. > 1.3: childlike, naive, or nonhuman |
| 2 | **Eye width to face width** | one eye ÷ face width at cheekbone | 1/5 each side, 1.05–1.2× stylized | > 1.3: chibi drift. < 0.9: small-eyed realism |
| 3 | **Fissure ratio** | eye height ÷ eye width | 0.42–0.48 | > 0.55: doe, round, vulnerable. < 0.35: fox, narrow, cold |
| 4 | **Canthal tilt** | inner→outer canthus angle | 0 to +3° | +5 to +8: feline, seductive, dangerous. −3 to −6: mournful, gentle, tired |
| 5 | **Iris fill** | iris diameter ÷ fissure height | 0.75–0.85 | 0.9–1.0: full iris, youthful and glamour. < 0.7 with sclera above: sanpaku, unsettling |
| 6 | **Upper lid coverage** | % of iris top covered by lid | 10–20% | 25–35%: heavy-lidded, languid, bored. < 10%: wide-eyed, alarmed |
| 7 | **Brow–eye distance** | brow base to upper lid | 0.5–0.7 EW | Tighter: intense, masculine, angry. Wider: open, youthful, spacious |
| 8 | **Brow angle** | inner end vs outer end height | near-flat, outer 1–2° higher | Inner lower: worried, gentle. Inner higher: imperious, sharp |
| 9 | **Nose length** | bridge to tip ÷ face length | 1/3, minimal bridge | Longer with a defined tip: aristocratic, mature. Short and small: youthful |
| 10 | **Philtrum** | ÷ upper lip height | 0.5–0.6 | Longer: mature, patrician. Very short: childlike |
| 11 | **Mouth width** | ÷ interpupillary distance | 0.75–0.85 | Narrower: restrained, cool, cruel. Wider: expressive, generous |
| 12 | **Lip ratio** | upper ÷ lower | 1 : 1.4–1.6 | 1 : 1.8 plus a glossed centre: glamour. Near 1 : 1: thin, cool, severe |
| 13 | **Facial index** | face length ÷ face width | 1.35–1.45 | > 1.5: long and narrow, aloof, aristocratic. < 1.3: wide, grounded, warm |
| 14 | **Chin width** | ÷ mouth width | 0.8–1.0 | Pointed: delicate, fragile. Square or broad: strong, androgynous |
| 15 | **Cheekbone** | height and forward projection | mid-height, restrained | High and flat: operatic, alien. Low and soft: soft, unformed |
| 16 | **Lower lid fullness** | aegyo-sal volume | present, 2–4 mm | Absent and tight: cold, sleepless. Heavy: exhausted, or very young |

**Identity or mood.** Parameters 1, 2, 5, 9, 10, 11, 12, 13, 14, 15 are **identity** — lock them in the identity block and never let them drift. Parameters 3, 4, 6, 7, 8, 16 carry **mood**: a design can move its lid coverage, brow angle, canthal tension, and lower-lid tightness per shot without recasting the character.

This split is the practical answer to "how do I look different without looking like a different person." Change the mood set. Never change the identity set.

## 3. Register presets

Two full settings inside the band limits of [../contract/visual.md](../contract/visual.md) §4. These are starting positions, not quotas.

| Parameter | Editorial face | Glamour face |
| --- | --- | --- |
| Eye width to face | 1.05–1.1× | 1.15–1.2× |
| Iris fill | 0.78–0.85 | 0.88–0.95 |
| Upper lid coverage | 12–20% | 22–30% |
| Canthal tilt | 0 to +3°, or −2 to 0 for a tragic read | +5 to +8° |
| Fissure ratio | 0.42–0.46 | 0.48–0.54 |
| Brow–eye distance | 0.55–0.65 EW | 0.6–0.7 EW |
| Lip ratio | 1 : 1.4 | 1 : 1.7 plus a glossed centre |
| Facial index | whatever the character demands | 1.4–1.45, harmonised |
| Cheekbone | mid, restrained | high but rounded, catching one specular |
| Asymmetry | two life traces may sit on the face | one deliberate asymmetry only |

**Why glamour moves where it does.** A larger iris with heavier lid coverage and a positive canthal tilt is the cartoon grammar for "warm, available, feline". Editorial's lower lid coverage and neutral tilt is the grammar for "present but unreadable". Neither is better; using one in the other's context is the failure.

## 4. Archetype presets — the mood set

Six temperaments, each expressed through the mood parameters. The identity set comes from the character; this table only sets what moves.

| Archetype | Canthal tilt | Lid coverage | Brow angle | Lower lid | Mouth | Net read |
| --- | --- | --- | --- | --- | --- | --- |
| **Aloof / divine-demonic** | +5° | 25% | flat, outer slightly high | full, one specular | level, glossy centre | untouchable, watching |
| **Imperial / ruthless** | +2° | 18% | inner 2° higher | tight | flat, no gloss | decided, unamused |
| **Languid / world-weary** | −2° | 32% | inner 2° lower | heavy | parted 2 mm | present but elsewhere |
| **Fierce / unruly** | +6° | 8% | inner 3° higher | tight, one frown line | one corner up | about to move |
| **Avant-garde / cool** | +7° | 14% | flat, asymmetric | tight | flat, matte | evaluating you |
| **Labour / grounded** | −4° | 15% | inner 1° lower | fine, dry | pressed, shut | tired, not asking |

Any of these can be re-gendered or age-shifted. They are temperament, not biology.

## 5. Charm — what the audience is actually reading

The register system calls glamour "desirability". It is easy to misread that as luxury: more silver, more gauze, more filigree. Expense is not charm. A perfectly expensive face can read as a mannequin, and this is the most common glamour failure after chibi drift.

What the viewer is actually reading, in order:

1. **Feature harmony beats feature intensity.** Features near the population mean read attractive; one strong feature reads as character. A face with six striking features reads as a mask. Aim for harmony across parameters 1–16, then spend the single striking feature on the eyes.
2. **One alive detail.** Perfect symmetry reads as a doll or a render error. A single asymmetry — one mouth corner three millimetres higher, one brow two millimetres lower, one strand crossing the brow — converts a model into a person. This is the cheapest credibility available and the one most often skipped.
3. **Gaze engagement.** The largest single lever, and it costs no words. Direct gaze with a slight lower-lid tension reads warm and present. Direct gaze with level lids reads cold and appraising. Gaze off-frame reads mysterious but disengaged — fine for a cover, wrong for a first-frame.
4. **The catchlight pair.** Two reflections: the upper (key) brighter, the lower (fill) dimmer, both inside the iris. One catchlight reads dead. Three or more reads glass. This is a rendering instruction with a strong emotional effect; treat it as non-negotiable.
5. **One matte zone.** Subsurface glow plus one area of matte — usually the cheek — is what separates porcelain from plastic. All-over gloss is the mobile-game failure; all-over matte is the sticker failure.
6. **The turn.** 15–30° three-quarter is the flattering angle. Full front is confrontational and flattens volume; full profile is graphic rather than charming. For a glamour hero, specify the turn and the slight head tilt that goes with it.
7. **Dimorphism calibration.** Glamour heroines sit around 60–65% feminine on a stylized scale: enough brow and jaw to avoid an infantile read, enough softness to avoid androgyny. Push either direction and the audience reads "child" or "statue".

**Charm is not more.** It is fewer competing signals plus one alive detail, held on a face whose parameters are in harmony.

## 6. Gaze, turn, and tilt

A small system, because these three carry most of the emotional load at zero cost.

| Element | Setting | Reads as |
| --- | --- | --- |
| **Gaze** | level, direct | present, challenging |
| | level, slightly down | appraisal, dominance |
| | down-left | introspection, memory |
| | off-frame | mystery, disengagement |
| | over the shoulder | invitation, departure |
| **Turn** | full front | confrontational, flat, product-like |
| | 15–30° three-quarter | flattering, dimensional — the default |
| | 45–60° | guarded, in motion |
| | full profile | graphic, silhouette-first |
| **Tilt** | level | dominant, formal |
| | 3–6° toward the low shoulder | approachable, curious |
| | 8°+ | playful, or unwell — context decides |
| | away from the low shoulder | resistant, cold |

In a 2×2 sheet grid, the top-right cell is where the turn does its work: a three-quarter bust with a slight tilt and a directional gaze. The top-left stays neutral by rule, so the difference between the two cells is almost entirely this table.

## 7. Face drift diagnosis

| Symptom | Parameter out of band | Fix |
| --- | --- | --- |
| Reads as a child | eye width to face > 1.3, iris fill > 1.0, philtrum very short | pull eye width back to 1.15–1.2, add a defined jaw, lengthen the philtrum |
| Reads as a mask or mannequin | symmetry perfect, one catchlight, zero asymmetry | add one asymmetry and the second catchlight; add one matte zone |
| Reads as plastic | all-over gloss, no matte zone | `matte cheek with a controlled specular`, keep subsurface only at the edges |
| Reads as uncanny half-realism | facial index pushed realistic, pores at full-body distance | restore `minimal nose bridge`, `defined upper lid line`, `refined anime facial design` |
| Reads as a recast | the eye design changed between renders | restate lid line, crease, iris fibre, limbal ring, and the cupid's bow verbatim |
| Reads cold when it should read warm | level lids, neutral tilt, no lower-lid tension | raise lid coverage to 22–28%, tilt +4 to +6, add lower-lid fullness |
| Reads childish when it should read seductive | canthal tilt negative, iris too round | positive tilt, elongate the fissure, narrow the iris fill slightly |
| Reads dead-eyed | gaze off-frame, one catchlight, no meniscus | direct the gaze, add the wet lower meniscus, pair the catchlights |
| Beauty reads expensive but not desirable | charm delivered as ornament, not as face | remove one ornament group; spend the budget on parameters 1–7 and one alive detail |

The last row is the one to check first in glamour work. If the design is expensive and nobody would keep looking at it, the problem is not the gown.
