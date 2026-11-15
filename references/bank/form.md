# Bank: Form — Silhouette, Value, Colour

The three decisions that are read at full-body distance and at thumbnail size, before any material, edge, or ornament is legible.

This file is a **lookup and diagnosis** bank. Its companion is [material.md](material.md): material system, restraint, the diagnostic checks, and the genre modules. Pair both with [boldness.md](boldness.md) to choose a risk level and break one rule deliberately. The only delivery gate is the preflight in [../pipeline/design.md](../pipeline/design.md) §6.

## 1. Silhouette before detail

At full-body distance the viewer reads silhouette and colour blocks, not embroidery. Choose one silhouette family and one contrast shape.

| Family | Outline | Personality read | Best for |
| --- | --- | --- | --- |
| **Column** | narrow, vertical, unbroken | aloof, controlled, austere | sword cultivators, assassins, bureaucrats |
| **Bell / A-line** | fitted top, wide hem | classical, ceremonial, generous | goddesses, priestesses, court robes |
| **Trapeze** | narrow shoulders, expanding volume | playful, unstable, extravagant | prodigies, performers, decadent nobles |
| **Cocoon** | rounded, oversized, uncinched | languid, detached, protected | immortals, hermits, exhausted fighters |
| **Hourglass / X** | fitted waist, wide shoulders/hips | disciplined, seductive, high-fashion | couture heroines, duelists, consorts |
| **Asymmetric** | one side strict, one side broken | dangerous, modern, unresolved | syndicate bosses, rebels, anti-heroes |

Silhouette family and gravity topology ([costume.md](costume.md) §2) are independent: an asymmetric silhouette can use Top-Peak Cascade, and a column silhouette can use Single-Side Mutation. Choose each separately.

Shape language: use one dominant plus one contrast. **Round/soft** reads approachable, vulnerable; **angular/sharp** reads dangerous, decisive; **vertical/elongated** reads authority, distance, divinity; **horizontal/grounded** reads stability, weight, labour.

Silhouette tests:

- Shrink the sheet to 10%. Can you identify each character by outline alone?
- Cover the colour. Does the silhouette still read?
- In a cast, do any two characters share the same outline? Change one.

Rendered cloth adds weight, and weight reads in the outline. A "wide sleeve" written for a painterly sheet reads as a stiff tent in 3D cloth unless it is given a fold structure and a hang direction.

**Canvas changes what the silhouette can spend.** A vertical frame rewards vertical lines — a column, hanging hair, a train, a falling sleeve — and wastes horizontal breadth. A widescreen rewards breadth and layered depth. Check the target canvas before committing to a family; see [framing.md](framing.md) §2.

## 2. Value hierarchy

Plan three values before colour:

- **Dark mass**: hair, coat, boots, shadow side.
- **Light mass**: skin, shirt, train, light side.
- **Midtone bridge**: fabric midtones, metal, secondary garments.
- **One focal contrast**: the highest contrast belongs at the face, chest, or hands — not at the hem.

Rules:

- Pass the grayscale test. If it becomes one grey mass, increase value separation.
- Avoid pure black and pure white; use near-black `#1E1E22` and near-white `#F2EFE8`.
- Do not put equal contrast in every zone. One accent, then rest.
- Background follows the costume's value, per [../contract/visual.md](../contract/visual.md) §9. Decide it after the palette is named, never before.
- A game-CG highlight rolls off rather than clipping, so a bright white costume is a value at the top of the range, not a hole in the image. Name the light mass by its colour rather than declaring it white-hot.

## 3. Colour system

70/25/5 is a proportion, not a palette. Choose a relationship first, then apply the proportion.

| Relationship | Use when | Example |
| --- | --- | --- |
| **Monochrome + accent** | one mood, high control | ivory / pearl / silver + one crimson iris |
| **Analogous** | harmony, atmosphere | celadon / mist jade / pale teal + one gold accent |
| **Complementary** | conflict, desire, danger | oxblood / deep green + one gold accent |
| **Split-complementary** | richness without vibration | plum / amber / slate + one jade accent |
| **Earth + jewel** | grounded luxury | raw linen / umber / bronze + one emerald |
| **Neutral + one saturated** | modern, graphic | charcoal / grey / bone + one electric cyan |

Rules:

- **70% primary hue**: split into matte base + tone-on-tone weave + sheer or specular edge. Matrices in [costume.md](costume.md) §3.
- **25% anchor tone**: hair, leather, dark metal, boots.
- **5% focal colour**: irises, eye/lip makeup, one or two motif cores.
- In the design spec, name every colour twice: plain language + HEX. In the final English prompt, use the plain-language name only.
- One saturated accent per character. Scarcity creates focus.
- Avoid pure black and white; they crush or blow out under a bright key. Use `#1E1E22` and `#F2EFE8`.

### 3A. Palette discipline at applied saturation

The house style inherits a failure from both sides: too saturated becomes a mobile-game splash; too desaturated becomes anonymous grey AAA. The discipline is applied saturation.

- **Let the face carry full chroma; let the costume carry less.** Anime eyes and lips are the most saturated thing on the sheet. Garment and materials sit a clear step below.
- **Build the 70% from cultural pigments, but allow them to be clean.** Azurite, malachite, cinnabar, realgar, ochre, bone white, lampblack, oxidized bronze, slate celadon, iron red. Mineral names signal a designed palette rather than a random hue.
- **Protect one chromatic anchor.** Every character needs one colour still clearly itself at thumbnail size — a cinnabar seam, an azurite collar, a realgar cord. It is separate from the 5% iris accent because the iris is small and the anchor is structural.
- **Give the dark mass a temperature.** `ink black` reads as neutral grey. `blue-black`, `warm iron black`, `brown-black`, `green-black` keep their identity.
- **Never rely on saturation alone to separate two elements.** Separate with value and material — matte against specular, coarse against fine.
- **Counter-temperature is mandatory.** A cool world needs one warm material; a warm world needs one cold one. The same rule governs a scene's light: see [../contract/visual.md](../contract/visual.md) §8A.

Commercial read is a pass/fail criterion: shrink the sheet to a thumbnail and ask whether it looks like a product — a cover, key art, a figure box. If the answer is "a nice render", the palette has no anchor and the design has no iconography.

### 3B. Token-frequency quota

The proportion lives in the blueprint; the image is built from word frequency. A model does not divide by percentages; it weights tokens. If the 5% accent appears eight times and the 70% base appears twice, the render inverts the blueprint.

| Role | Max occurrences of its colour term | Notes |
| --- | --- | --- |
| **5% focal accent** | **2** | the accent name itself; irises + one motif core |
| **25% anchor tone** | **4** | hair mass, boots, structural metal |
| **70% primary hue** | **8** (saturation guard, not a quota) | beyond 8 the sentence has stopped describing and started chanting |
| **Material word (any role)** | **5** | beyond this the texture saturates and reads as clutter |

- Classify each term before counting: `crimson` is a 5% accent on a pearl gown and a 70% base on an oxblood-velvet character.
- Count mechanically: lowercase the finished prompt, split hyphenated compounds, tally each colour or material term once per occurrence. `scripts/preflight.py` does this — use it rather than estimating.
- A word can be both a colour and a material (`silver`, `gold`, `jade`, `bronze`). Count it once as colour and once as material, and apply both caps.
- Colour-clash palettes at gear 2+ with the colour-clash lever have two primary hues; both take the base cap (8), and the palette loses its 5% accent. Do not count one as an accent and then fail the design for exceeding 2.
- If the quota forces you to drop a desired accent occurrence, that is signal: the design was relying on repetition rather than one well-placed focal point.

### 3C. Render-vocabulary budget

- Rendering vocabulary stays in the header and closing line. It may not appear in the narrative body, where it displaces the character.
- Name each render concept once. `subsurface scattering` twice is a reminder; three times is a chant.
- Technical words outrank fluff, but not nouns. `volcanic glass` beats `beautiful texture`; `hand-hammered bronze kylix` beats both.
- The render budget does not grow the prompt. The house base costs roughly 30–40 words of header; take them from palette elaboration, not from the face, motif, or per-cell scoping.

## 4. Reference synthesis

Use three reference axes, then one unexpected reference:

1. **Era/culture**: Tang dynasty, 1930s Shanghai, 1990s Tokyo, Byzantine.
2. **Garment archetype**: qipao, kimono, trench, corset, tabard, flight suit.
3. **Material/colour**: raw silk, oxidized silver, celadon, oxblood.

Then add one unexpected reference: architecture, plant, instrument, machinery, painting, religious object. Example: `Tang dynasty + Issey Miyake pleating + oxidized silver`, or `1930s qipao + surgical steel + moth wing`.

Rules: synthesize, do not copy. No brand names, no living artist names, no copyrighted characters. If the reference is a real garment, change at least two of its three axes.
