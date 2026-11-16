# Visual Contract: House Style, Rendering, Light, Canvas, Exclusions

This file is the **only** source of truth for the house style, rendering language, lighting, background, resolution, engine parameters, and exclusion policy. Every other file references these sections and never restates them.

Read it with every workflow, in all four modes.

Every new image defaults to one unified semi-realistic 3DCG system with next-generation game-cinematic and commercial-animation production values. Characters are refined and stylized; environments are naturalistic and physically grounded. Both rest on the same art direction, rendering logic, material system, lighting behaviour, colour management, and cinematic post-processing. Different visual treatment is intended; looking like two different worlds is not.

## 1. The house style

Four pillars, all present, none dominant:

| Pillar | What it contributes | Prompt language |
| --- | --- | --- |
| Semi-real 3D game CG | plausible light, real cloth weight, game-grade shading | `premium 3D game CG character render, semi-realistic shading with hand-authored material response, game-trailer lighting` |
| Refined anime at the face | idealized bone structure, large luminous eyes, crisp feature design | `refined anime facial design, clean feature shapes, large expressive eyes with glass-like depth` |
| High-grade BJD material quality | porcelain clarity, sculptural relief, jeweller-grade fittings — without the joints | `high-grade BJD porcelain material quality, sculptural surface relief, hand-finished resin-and-porcelain sheen` |
| Commercial animation art direction | shape language, colour blocking, silhouette clarity, marketable iconography | `commercial animation art direction, strong readable silhouette, deliberate colour blocking, merchandisable design language` |

**The blend is the point.** Pure game CG goes anonymous and grey; pure anime flattens into a sticker; pure BJD turns into a doll on a stand; pure commercial polish turns into a mobile-game splash. Each pillar corrects a specific failure of the others.

Blend ratios:

- **Face**: anime-forward, at 3D material quality. This is where refinement is judged.
- **Skin and material**: BJD-forward. Porcelain clarity, subsurface glow, sculptural polish. The skin looks worked by hand, not photographed.
- **Body proportion and cloth**: game-CG-forward. Real weight, real drape, believable anatomy under stylization.
- **Whole-sheet read**: commercial-forward. Silhouette, colour blocking, and iconography decide whether the design survives a thumbnail.

When two pillars conflict in one sentence, the later zone wins: face detail follows anime, garment detail follows game CG. A sentence that tries to be both produces the plastic middle all four pillars exist to avoid.

**BJD is the material, never the mechanism.** Keep porcelain translucency, sculptural cheekbones, jeweller-grade filigree, a hand-finished sheen. Forbid visible ball joints, joint lines, seams, articulation, mannequin hands, and doll stands. The line is simple: BJD supplies the surface and the sculpture; the body is a living body.

## 2. Style selection

- The current request's explicit medium, visual style, and parameters take priority. Otherwise carry forward a style explicitly chosen by the user for the relevant character or world. Accepting a workflow default or attaching an image alone does not select its medium for a new image.
- When the user assigns another character's sheet as a style reference, extract its actual medium, stylization, form modelling, brushwork, material treatment, lighting, and colour handling. Keep the target character's identity, anatomy, costume, and palette independent. If the image is unavailable, use confirmed textual art direction or the workflow default and state that visual matching awaits the reference.
- If no style was chosen, use the unified 3DCG system for character concepts, reference sheets, and new scenes.
- An explicitly requested painting, anime illustration, or named medium such as ink wash or watercolour replaces the 3DCG default for that image. Use that medium's own language, and do not append PBR, subsurface-scattering, or global-illumination wording to a wholly painted image.
- Use one coherent medium unless the user explicitly asks for a blend. Within the 3DCG default, refined characters and more naturalistic environments are intentional and compatible.
- For revisions, keep the confirmed style unless asked to change it. An existing scene image assigned as the edit target establishes its actual medium, material treatment, and rendering finish. Preserve those during scene variations, including when they differ from this default. Changing time or weather can change lighting and colour response without changing the medium. Scene editing and outpainting never become style conversions merely because these defaults changed.

## 3. Engine parameters

One table, all outputs. User-specified values override every default here.

| Output | Aspect ratio | Preset suffix |
| --- | --- | --- |
| Character portrait (head to waist) | `--ar 3:4` | `--raw --s 150` |
| Vertical narrative frame — short drama, vertical key art | `--ar 9:16` | `--raw --s 150` |
| Identity sheet, costume sheet, scene base | `--ar 16:9` | `--raw --s 150` |
| Identity-sheet split — turnaround | `--ar 3:2` | `--raw --s 150` |
| Identity-sheet split — face sheet | `--ar 1:1` | `--raw --s 150` |
| Asset-chain stage one — character | `--ar 3:4` | `--raw --s 150` |
| Asset-chain stage one — scene or prop | `--ar 16:9` | `--raw --s 150` |
| Existing-scene revision | inherit the source frame | preserve confirmed style parameters |
| GPT Image 2 / Gemini | natural language, e.g. "16:9 landscape canvas" | no MJ flags at all |
| Stable Diffusion / Flux / ComfyUI | set in the UI | drop `--ar` and resolution tokens from the positive |

**Canvas is chosen by use, not by habit.** Composition, figure occupancy, safe areas, and the information budget differ per canvas and are specified in [../atlas/coordinates.md](../atlas/coordinates.md) §4. Vertical 9:16 is the narrative default for short drama; 16:9 is the scene-plate and sheet default; neither converts into the other by cropping.

Rules:

- The presets are starting positions; they do not guarantee a medium or a rendering method.
- `--s` accepts 0–1000 and defaults to 100, so 150 is a mild push toward art-directed interpretation.
- `--raw` is supported from V5.1.
- Aspect ratio comes from the current workflow or request, never from a previously attached portrait. Including the known ratio even when images are attached stops a character reference from supplying the scene frame.
- For an explicitly requested non-default medium, keep confirmed `--raw` and `--s` values associated with that medium, and add neither when none exist.
- Do not invent pixel dimensions, stylization values, API settings, or other unsupported parameters.

### Version facts — verify before relying on these

These are engine behaviours, not design rules. They are collected here so an outdated claim has exactly one place to be corrected. Confirm against the current engine documentation before asserting them to a user.

| Claim | Scope |
| --- | --- |
| `--hd` renders 2048px instead of standard resolution; it caps aspect ratio at 4:1, costs more GPU time | V8.1, V8.2 |
| Midjourney standard and `--hd` output top out at 2048px | V8.1, V8.2 |
| Midjourney's inpainting and outpainting return standard-resolution results, so an `--hd` source does not stay at 2048px through an extension | V8.1, V8.2 |
| `--hd` is a generation parameter, not an upgrade switch: rerunning a prompt with `--hd` returns a new image whose details differ | V8.1, V8.2 |
| The Edit Model replaced Character Reference and Omni Reference, so do not add `--cref` or `--oref` | V8.2 |
| `--niji 7` / `--niji 6` selects Midjourney's anime model; it replaces this 3DCG system rather than combining with it | V8.x |

`--niji` is used only on an explicit request, and the CG rendering clauses are dropped when it is.

## 4. Semi-real proportions

Semi-real is a specific set of proportions and a specific amount of texture, not a midpoint between realism and anime.

| Dimension | Semi-real target | Too realistic | Too anime |
| --- | --- | --- | --- |
| Head count | 7.0–8.5 heads, deliberate per character | < 7.0 naturalistic stock | 9+, doll-extreme |
| Eye size | large, 1.4–1.6× realistic socket fill | realistic, small | 2×+ realism, face mostly eye |
| Nose | minimal bridge line, defined tip | full bridge and nostril structure | single dot or line |
| Mouth | shaped, soft gradient or matte lip, visible cupid's bow | full lip texture, wet interior | two lines |
| Skin | fine pore hint at close range, BJD-smooth at full body | visible pores at all distances | zero texture, airbrushed |
| Hair | grouped locks with sculpted strand clumps and flyaways | individual hair simulation | single painted mass |
| Silhouette | idealized, deliberate waist/hem cut, readable | naturalistic | rubbery, unreadable |

Common proportion bands (derive via [../engine/03-costume-and-craft.md](../engine/03-costume-and-craft.md) §2.1):

- Detached / aristocratic / austere / haute couture: `8.5-head slender fashion proportion`.
- Grounded / martial / working / approachable: `7.5-to-8-head athletic proportion`.
- Youthful / compressed / compact: `7-to-7.5-head lithe youthful frame`.

State the proportion, the waist-cut height, and the shoulder-waist-hip line together. A head count without a body returns an invented torso.

**The band is a range, not a target.** `8.5-head` is the top of one band and it is the figure most often reached for; a cast in which every character is 8.5-head slender has a proportion system, not a cast. Use the band the character's Position earns: an exhausted elder is not 8.5-head, a labourer is not 8.5-head, and a child is not in these bands at all. The shoulder-waist-hip line is the second half of the decision and is never inherited from the previous character.

**The skin rule.** Semi-real keeps pore-level detail at the close-up tier only — normally the bottom-right macro cell — and lets full-body views read as polished porcelain. Heroes are meant to look flawless at distance.

## 5. Characters

- Use premium character-asset quality: sculptural three-dimensional form, art-directed body proportions, commercial-grade design.
- Build the face on real bone and muscle logic, then refine it with coherent anime-informed features. Keep mature natural proportions for adults.
- Borrow surface craft from high-grade ball-jointed-doll work: clean sculpting, resin-like translucency blended with living skin, natural subsurface scattering, soft light transitions, restrained microtexture. Never give a living character mechanical joints, seams, rigid plastic, wax, or toy materials.
- Eyes have detailed iris structure, real optical depth, and natural corneal highlights, without flat oversized cartoon eyes.
- Use individually groomed hair strands organized into designed locks, with highlights that follow the image's key light.
- Make costume materials specific: cloth thickness and weave, natural folds, embroidery, leather grain, jade or stone, controlled metal reflections. Include only materials present in the actual design.
- A character may be more refined and stylized than the environment, but keeps believable volume, lighting response, and physical material behaviour. A realistic environment does not turn the character into a live-action actor.

The anime face has six required elements. **Each element has two parts, and they are not the same kind of instruction** — see [gates.md](gates.md) §8. The craft string is reused verbatim in every prompt; the decision is derived per character across **both bone geometry (§1A) and facial surface (§1B)** in [../engine/02-face-derivation.md](../engine/02-face-derivation.md), and must never be borrowed from another character.

| Element | Craft — reuse verbatim every time | Decision — derive per character ([../engine/02-face-derivation.md](../engine/02-face-derivation.md) §1A & §1B) |
| --- | --- | --- |
| **1. Eye design** | `large almond eyes with a defined upper lid line, a clear double-lid crease, tapered inner and outer corners` | eye width to face (1.0–1.2×), inter-canthal distance, fissure ratio, canthal tilt, plus **periocular weight** (outward vs inward vs bare) |
| **2. Iris** | `radial iris fibre with a darker limbal ring, a glassy depth with a bright secondary reflection, a wet lower meniscus` — two catchlights, not one | iris fill (0.75–0.95), **derived iris hue/value/temperature from gaze intent**, and chroma contrast against the costume |
| **3. Nose** | `a minimal bridge` | bridge length to a defined tip vs a short high placement; nostril emphasis suppressed at full-body distance regardless |
| **4. Mouth** | `a visible cupid's bow`; vertical striation only in the macro cell | lip ratio (1:1.0 / 1:1.4 / 1:1.7), width against the interpupillary line, and **functional lip state** (glossed mask vs matte/pressed/chapped tool) |
| **5. Brow** | `thin, shaped, and legible at distance` | brow angle and brow–eye distance — both mood parameters, moved per shot |
| **6. Porcelain skin & marks** | `smooth porcelain skin with a soft subsurface glow`, visible fine pores only in the close-up macro cell | **specular/matte map** (where the matte zone and specular break sit) + **single mark rule** (default **zero** marks; at most 1 derived scar/ritual/occupational trace, never a copied mole) |

Rules:

- **Craft may be shared by the whole cast. Decision may not.** Two characters may both have `a visible cupid's bow`; they may not both have lip ratio 1:1.4, the same iris colour, and a mole beneath the eye, because that bundle is what a viewer reads as the same face.
- **Never let a craft string stand in for a decision.** Writing only the eye-design craft string describes how an anime eye is built, not whose eye it is — and every character described that way gets the same eyes.
- **The derivation procedures are [../engine/02-face-derivation.md](../engine/02-face-derivation.md) §1A (Bone) and §1B (Surface)**, and the parameter bands are [../atlas/coordinates.md](../atlas/coordinates.md) §1 and §4 above. The craft column here is the only part that must appear word-for-word.
- **The eye hierarchy is the single most important rule.** Anime eyes are the first fixation and the design signature. Any ornament, crown, or garment detail that competes with the eyes has to be quietened — and because the eyes carry identity, a decision changed there is a recast, not a variation.

Hair architecture — three tiers plus one linear interruption:

1. **Primary mass**: waist-length ink-black tresses, high ponytail, sleek bob, or loosely unbound waves.
2. **Sculpted strand clumps**: `grouped locks with sculpted strand clumps, a few individual strands breaking away at the crown, temple, and jaw`. Semi-real CG hair is clumped, not simulated.
3. **Anime specular band**: `a soft anime-style highlight band across the crown`, kept soft or it looks like plastic.
4. **Linear value interruption**: dyed inner streaks, silk tassels, thin braided chains, a weathered branch, geometric pins.

Flyaways are mandatory in every register: `a few flyaway strands catching the light` prevents the helmet look.

## 6. Environments

- Use full-scale cinematic 3D environments with plausible construction, true object scale, material thickness, and layered spatial depth.
- Do not give the environment the character's doll-grade finish. Architecture, rock, timber, vegetation, water, ground, sky, cloud, and interior furnishing keep their own physical material behaviour.
- Describe PBR-like behaviour through visible evidence: stone edge wear and roughness variation, timber grain depth, controlled metallic reflections, translucent foliage, or water response as relevant. Allow natural irregularity, repairs, weathering, and traces of use.
- Keep art-directed composition, architectural rhythm, visual paths, and colour organization, with detail density controlled across foreground, midground, and background. Aim for a high-budget game cutscene or animated feature rather than an uncomposed documentary photograph.
- The environment may be more naturalistic than the character while holding the same CG rendering quality, colour handling, and light logic.

## 7. Characters and environments in one frame

Describe the character and environment separately, then connect them with concrete shared conditions:

- One rendering base: PBR-like materials, global and indirect illumination, real reflection behaviour, ambient occlusion, and natural shadows.
- One key-light direction, intensity, and colour temperature, with compatible ambient fill, shadow direction, softness, and falloff. Skin, hair, costume, and accessories receive environmental bounce light and local colour spill. No independent character lighting, no warm character against a cool environment, no bright character in a dark scene.
- Shared material response and render finish. Skin may carry finer detail than stone, as long as highlight strength, reflection logic, and gloss obey the scene's lighting.
- One exposure, white balance, contrast response, black-and-white point relationship, highlight handling, and filmic grade. A focal character stands out through composition and motivated lighting, not separate colour processing.
- One camera position, perspective, focal-length logic, scale, and depth-of-field progression. Feet, hands, garments, and props have believable contact, occlusion, and contact shadows. The character occupies the space instead of sitting on the background like pasted artwork.
- Distance-consistent haze, atmosphere, edge softness, and detail falloff. A character may be sharper than the background without cutout outlines, separate sharpening, or a floating silhouette. Do not blur the environment heavily to hide a mismatch.
- One weather, time of day, and air condition for character and scene alike.

Example integration clause:

> the refined 3D character retains her facial proportions within the naturalistic environment, both lit by one warm key light from the left with cool ambient fill, environmental colour bounce on skin and clothing, grounded contact shadows, consistent scale and perspective, shared exposure and filmic colour grading

Choose details relevant to the scene; do not recite every rendering term. For a wide view, prioritize silhouette, proportions, and material response over invisible iris microdetail.

## 8. Lighting

Four persona-driven modes. Choose one as the character's signature and route it through the current workflow's setup.

| Mode | Best for | Prompt tokens |
| --- | --- | --- |
| **High-key pearlescent glow** | aloof deities, tragic or imperious heroines, bridal-gothic couture, ink-wash immortals | `high-key pearlescent studio lighting with a soft overhead bloom, gentle rim falloff through layered sheer fabric, luminous porcelain subsurface glow` |
| **Crisp chiaroscuro rim** | ruthless emperors, dark sword cultivators, gothic anti-heroes, syndicate bosses | `crisp side-back key with a cool silver rim response, clean luminous shadow transparency, sculpted facial planes` |
| **Warm tactile global illumination** | martial monks, desert wanderers, unruly prodigies, grounded fighters | `warm directional global illumination with crisp specular contrast, tactile response on raw fibre and oxidized bronze, natural skin warmth` |
| **Overcast diffuse mist** | battlefields, ruined sects, mourning, rain, exhausted or low-status characters | `overcast diffuse daylight, very large soft source, low contrast with intact material detail, thin atmospheric mist at ground level` |

**Choosing the mode is a decision, not a register lookup.** Editorial picks one of the four as the colour and quality signature, routed through sheet-safe exposure. Glamour most often takes high-key pearlescent, also routed through sheet-safe exposure so the back view stays readable — but `most often` is not `always`, and treating it as always is what gives a cast one light: a glamour schemer, a glamour antagonist, and a glamour character introduced at night all read better outside it.

Reach for high-key pearlescent only when the character is genuinely the aloof or imperious figure the first row describes. Chiaroscuro costs hair detail, so it is wrong for a hair-as-hero design and right for a character whose threat should be legible before their face is. Warm tactile is the correct choice for anyone whose life happens outdoors. Overcast is the only honest choice for mourning, defeat, and exhaustion — and it is the one mode glamour almost never spends. Any mode is legal in either register; the batch rule is in [gates.md](gates.md) §9, axis 6.

**Sheet-safe lighting** (identity and costume sheets): `sheet-safe soft directional key from the front-left, broad bounce fill, a clean rim separation, and a soft grounded contact shadow` across all panels. Chiaroscuro and hard rim are accents for the 2×2 close-ups by default. Sheet-safe is not flat: exposure stays even, but a real key direction and a real rim remain.

### 8A. Scene lighting

Sheet lighting is studio lighting; a scene is not a studio. Scene lighting follows the scene's time, weather, and light sources, and it is chosen in the same pass as the character's key direction, because §7 requires both to share one key.

**Three scene modes by light source count.**

| Mode | Light structure | Best for | Prompt tokens |
| --- | --- | --- | --- |
| **Single-source daylight** | one sun key, sky fill, bounce from the ground plane | exterior establishing, open landscape, day interiors lit by a window | `one low warm sun key from the left raking across the surface, cool sky fill on the shadow side, bounce from the pale ground warming the underside` |
| **Motivated practical** | named in-frame sources doing the keying; the ambient is a residue | night interiors, taverns, temples, streets at night, candlelit rooms | `a lamp on the right wall acting as key with a warm pool and a fast falloff, cold moonlight as the only fill, each flame reading as its own small source` |
| **Mixed ambient** | no single dominant source; multiple low-level sources with no clear key | overcast, fog, rain, ruins, twilight, interiors with many small windows | `flat overcast ambient with no directional key, a faint brighter patch where the sky breaks through, visible depth only from layered contrast` |

Most scene failures are a single-source lighting instruction applied to a multi-source place, or a night scene lit as though a sun still worked.

**Practical light sources and what each does.** Name the source, its position, its colour temperature, and its falloff.

| Source | Colour | Falloff | Behaviour to specify |
| --- | --- | --- | --- |
| Sun, direct | warm to neutral | very slow | hard shadow edge, high specular on any polished surface |
| Sun, through window | warm, shaped by the frame | fast inside, shaped | a projected light shape on the floor or wall — the cheapest depth cue available |
| Overcast sky | cool, neutral | almost none | no shadow direction; separate objects by value and material, not by shadow |
| Moon | very cool | slow | low intensity, no warm bounce; keep it as fill unless the design wants blue night |
| Fire, candle | warm orange, one source per flame | very fast | every flame is its own source with its own small pool; cheeks and film highlights will flicker red |
| Oil lamp, lantern | warm amber | fast | a visible hot point plus a lit volume within one to two metres |
| Torch, brazier | warm, unstable | fast, directional downward | smoke above, a hot floor below |
| Neon, screen | saturated, narrow band | medium | local colour spill on skin and cloth; the base ambient stays low |
| Underwater, fog, smoke | whatever the source is | heavily scattered | volumetric shafts only where a source is blocked; no shafts without a source |

**Night is not day darkened.** Three rules:

1. **Night has its own key.** Moonlight, a lamp, or a fire is the key; the correct exposure for that key leaves most of the frame dark. A night image where every surface is legible is a day image with a blue filter.
2. **Night keeps one warm human light.** A single warm practical inside a cool night is the most reliable way to make a night frame read as inhabited rather than empty.
3. **Night loses shadow detail, not colour.** Let the darks crush slightly; keep hue. A desaturated night reads as fog, not as night.

**Interior light is a box with one or two openings.**

- The window, door, or lamp is the key. The room's own bounce is the fill.
- Ceilings and the far wall receive the least light; do not let them read as evenly lit.
- Room fill is usually warm from wood and cool from glass. Name which one dominates, or the interior turns grey.
- Depth inside a room comes from one lit near-surface and one darker deeper-surface. Two evenly lit walls flatten the space.

**Multi-source scenes need a stated hierarchy.** Name which source is key, which is fill, and which is an accent. Three equal sources produce no direction, and the viewer cannot tell what time of day it is.

> Example hierarchy clause: `the wall lamp is the key at half the strength of daylight, the open door supplies cool fill from the left, and one candle near the table is an accent that lights only the hands`

**Colour temperature is the scene's mood, and it must be one decision.** Pick a dominant temperature and one counter-temperature (this mirrors the counter-temperature rule for palettes in [../atlas/lexicon.md](../atlas/lexicon.md) §5). A warm interior against one cold window, or a cool exterior against one warm lantern. Two dominant temperatures of equal strength cancel.

**Time of day changes more than colour.** Each band sets contrast, shadow length, and what is lit:

| Time | Key height | Contrast | What reads |
| --- | --- | --- | --- |
| **Dawn** | low, raking | low, soft | long shadows, mist at ground, cool ambient with one warm edge |
| **Morning** | rising | medium | crisp shadows, clear colour, everything legible |
| **Noon** | overhead | high, short shadows | flat verticals, hard pools, poor depth — the hardest to compose |
| **Golden hour** | low, raking, warm | high but soft-edged | long shadows, warm rim on every surface, the most forgiving key |
| **Dusk / blue hour** | below the horizon | very low | almost no direction; separate by value and by lit windows |
| **Night** | see the night rules | high against the key | small pools, deep darks, one warm practical |

**Character in scene.** The scene's key governs the character's key — this is the §7 rule, applied. Do not relight the character. The character's palette roles and materials respond to the scene's light: a warm lamp warms porcelain skin, a cold moon cools it, and the same character reads as a different person under each without any change to identity. Allow that, and say so when it happens.

**Do not use a scene's time-of-day lighting for a sheet, and do not use sheet lighting for a scene plate.** They answer different questions: a sheet asks "what is this design", a scene asks "what is happening here".

## 9. Background

The background is a function of the costume's value, not of mood or habit.

| Costume value | Editorial | Glamour |
| --- | --- | --- |
| near-white (ivory, pearl, silver, bone, chalk) | warm off-white `#F2EFE8` | pure white preferred when the hair is dark; `#F2EFE8` when the hair is light |
| mid-tone to dark | pure white, or warm off-white if the figure still separates | pure white |

- Pure white erases a white, ivory, or silver silhouette. A platinum-haired character in pale bone clothing on pure white is three near-white masses against near-white.
- Choose the background in the blueprint after the palette is named, and never override it for a cleaner look.
- The background stays seamless. Render quality comes from the light, the contact shadow, and the atmosphere around the figure — never from scenery, fog banks, ruins, or a horizon. A background with a landscape in it is a rejected character sheet.
- Add a soft grounded contact shadow so the figure does not float. Hairline dividers only; no outer frame.
- **Asset-chain character sheets** use a neutral mid-gray ground instead of white, to reduce high-contrast edge artefacts when the still is later read as a video reference frame. The background is neutral; the subject is not neutralized.
- **Scene plates** use the scene's environment, not a sheet background.

## 10. Resolution and split protocol

Seven panels in one 16:9 frame is a compression problem. An eye design — lid line, crease, iris fibre, two catchlights — needs pixels that a small panel does not have.

| Delivery | Target canvas | Notes |
| --- | --- | --- |
| Single identity sheet, 7 panels, editorial | 2560×1440 | below this the full-body faces are too small for the anime eye design |
| Single identity sheet, 7 panels, glamour | 3072×1728 preferred | glamour lives on hair: lock geometry, inner streaks, headpiece tassels |
| Identity-sheet split — turnaround | 2560×1707 (`--ar 3:2`) | three views share the frame |
| Identity-sheet split — face sheet | 2048×2048 (`--ar 1:1`) | four cells at full budget for eye, lip, and porcelain surface |

**Engine reality.** Midjourney standard and `--hd` output top out at 2048px (see §3). The 2560/3072 targets above are composition targets for engines that support them, or for a separate upscale step after generation; do not describe them as Midjourney's native output. If the engine cannot hold seven panels at the target size, use the split protocol instead of adding more detail words. Beyond the budget the words consume each other and the render gets mushier.

Split protocol:

1. **Sheet 1 — turnaround**: the three orthographic views only, `--ar 3:2`.
2. **Sheet 2 — face**: the 2×2 close-up grid only, `--ar 1:1`.
3. Reuse the identity block word-for-word in both prompts. Keep the same background token, key-light sentence, and consistency line.
4. The split also removes the panel-merge failure mode, because one frame is no longer doing two jobs.

## 11. Negative and exclusion policy

Prefer positive visual descriptions. State the wanted skin, material, and grounding qualities in the prompt body; that carries more weight than a long exclusion list.

**Midjourney.** `--no` reads each word separately, so keep only single words the image never needs. Starting list: `plastic, waxy, low-poly, cutout, collage`. Add concrete, correctly scoped exclusions only when the design actually calls for them. A workable ending for a character sheet:

```text
--no text, labels, logos, watermarks, plastic, waxy, low-poly, cutout
```

Do not write these into `--no`:

- `doll` — it cancels the intended BJD-grade refinement.
- `seams` — it cancels the garment seams a sheet must repeat across views.
- `skin`, `figure` — they negate the subject.
- clothing words — moderation reads each word separately and the wanted clothing is cancelled.
- people, heads, hair, or costume elements needed elsewhere in the frame.

**GPT Image 2 and other natural-language engines.** Express exclusions as natural language, scoped to the correct panel or region. Never globally exclude needed people, heads, hair, or costume elements. Use a closing "avoid" sentence rather than a tag list.

**Stable Diffusion / Flux / ComfyUI.** Use a separate `Negative prompt:` field; drop `--ar` and resolution tokens from the positive prompt and set them in the UI.

**Jimeng / Kling / other CN engines.** Use the negative field where available; otherwise compress to the six highest-value Chinese terms: `塑料手办感与球关节, 手机游戏宣传图油光, 二次元贴纸平涂, Q版比例, 塑料发片, 高光过曝与死黑`.

**Common failure guards** (use as positive descriptions first): mobile-game splash glare, glassy over-rendered skin, visible articulation and joint lines, anime sticker flatness, grey AAA anonymity, uncanny half-realism, photorealistic skin texture, plastic hair cards, chibi drift, blown highlights, crushed shadows, cropped head or feet in full-body views, duplicated or merged panels, inconsistent outfit across views, background scenery, outer frame or border.

At Avant-garde or Surreal risk levels, in a phrase-based negative field, replace `distorted anatomy` and `cluttered over-ornamented patterns` with `unintended anatomy errors` and `unintentional clutter` so deliberate distortion and accumulation are not suppressed. In glamour register both swaps apply at every gear, because the register's deliberate layering and stylized proportion would otherwise be suppressed. For Midjourney, keep `--no` to single words.

## 12. Prompt discipline

- Select a short subject-specific finish clause and, when needed, a short integration clause. Do not paste this whole document into a prompt.
- Technical terms describe a target appearance; they do not configure or prove a rendering engine, PBR pipeline, colour space, or exact physical simulation.
- Do not use empty fluff adjectives and do not request richness as an adjective; both lists are in [gates.md](gates.md) §6. Enumerate layers, edges, nodes, and pattern instead.
- Do not write shader parameters (`roughness 0.4`, `metallic 1.0`, `IOR 1.5`); they are engine settings, not images. Describe the surface instead.
- Do not put review vocabulary (`hero ornament`, `primary open area`, `design thesis`, `aesthetic order`) into the English prompt; translate it into visible description.
- Keep render vocabulary in the header and closing line. Name each render concept once.
- Backgrounds, defaults, and exclusions cannot guarantee identity, physical accuracy, or multi-view consistency. Do not promise those outcomes.
