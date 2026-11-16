# Pipeline: Reference Sheets

Use this workflow for a model sheet, turnaround, asset sheet, multi-view presentation, or costume presentation of one character. Read [../contract/visual.md](../contract/visual.md) for style priority, lighting, background, resolution, split protocol, and parameters — all of which are defined there and not repeated here. For GPT Image 2, follow [gpt-sheet.md](gpt-sheet.md) and reuse the layout, body occupancy, pose rule, and multi-view consistency rules here.

## 1. Choose the sheet mode

| Mode | Purpose | Layout | Background |
| --- | --- | --- | --- |
| **Identity sheet** (default for a new design) | establish face, body, pose, and costume across views | 16:9; left ~58% three full-body orthographic views, head to toe; right ~42% 2×2 bust grid | by costume value, [../contract/visual.md](../contract/visual.md) §9 |
| **Costume sheet** | present the costume when face and identity are already established | 16:9; left 55% three neck-to-foot costume views with reserved head space and hair hidden; right 45% 2×2 portraits | by costume value, §9 |
| **Asset sheet** | structured asset for a video pipeline | mid-gray; front/side/back plus portraits, single-pass | neutral mid-gray, §9 |

Default to the identity sheet when designing a character. Use the costume sheet when the identity is fixed and the task is costume presentation. Use the asset sheet only for a video-production chain, per [asset-chain.md](asset-chain.md).

Sheets reward fine facial, hair, and material detail. Mention `--hd` as an option when the user wants 2048px output, per [../contract/visual.md](../contract/visual.md) §3; do not add it by default, and state that it returns a new image rather than upscaling an existing one.

## 2. Identity sheet

A 16:9 landscape canvas. Background by costume value, per [../contract/visual.md](../contract/visual.md) §9.

### Left: three full-body orthographic views (~58%, borderless)

- Front (far left), exact 90-degree side, and back views side by side.
- One shared ground line, identical scale, head to toe uncropped inside the left zone.
- **Orthographic alignment is mandatory; a generic neutral mannequin stance is forbidden.** State the character's **4D Orthographic Pose Vector** ([../engine/01-truth-and-pose.md](../engine/01-truth-and-pose.md) §7):
  1. **Weight axis** (which leg locks or bears weight, stance width, or forward/back balance on the shared baseline)
  2. **Shoulder-neck line** (level, dropped on one side, squared, craned)
  3. **Empty-hand action** (adjusting collar/cuff, thumb hooked in belt, clasped behind back, resting on sternum — never holding a prop and never occluding the chest hero node)
  4. **Chin & gaze** (lifted, level, tucked; direct or off-frame)
- Front: torso faces straight-on so placket and waist construction remain clear, while carrying the character's weight axis and empty-hand action.
- Side: pure 90-degree profile showing posture carriage, drape depth, hair flow, and footwear profile.
- Back: pure 180-degree rear showing how the core motif and gravity topology ([../atlas/coordinates.md](../atlas/coordinates.md) §3) resolve across the spine and hem.
- Consistent weak perspective across all three views. Avoid extreme lunging or twisting action poses that break orthographic alignment.

### Right: four bust cells (~42%, thin internal 2×2 dividers)

| Cell | Content | Expression |
| --- | --- | --- |
| **Top-left** | symmetrical front bust; headgear, ear ornaments, collar framing | **fully neutral baseline** |
| **Top-right** | three-quarter angled bust, slight head tilt, directional gaze ([../engine/02-face-derivation.md](../engine/02-face-derivation.md) §5) | near-baseline charm |
| **Bottom-left** | pure 90-degree profile bust; brow-nose-lip-jaw contour, side ornaments | near-baseline |
| **Bottom-right** | tight macro on eyes, nose, and lips; crown and shoulders deliberately cropped out of this cell only | one physical muscle micro-expression |

**Per-cell scoping is mandatory.** Attach the micro-expression to the bottom-right cell by name, and name the top-left cell as neutral. A single un-scoped expression sentence makes all four cells share one mood, which destroys the purpose of the sheet.

All four cells are bust or facial close-ups. Never use a cell for a fabric swatch or a detail crop; the fourth cell is locked on eyes, nose, and lips.

Consistency: identical costume details, hair streaks, and markings across all seven panels. No held or carried object appears in any panel, per [../contract/gates.md](../contract/gates.md) §4. Worn ornaments remain.

### Canvas and split

Target canvases and the split protocol are in [../contract/visual.md](../contract/visual.md) §10. Use the split when the engine cannot hold seven panels at the target size, rather than adding more detail words.

## 3. Costume sheet

Use when the character's face is established and the task is to present costume construction.

- A 16:9 landscape canvas: left 55% costume views, right 45% portraits.
- Left: front, exact 90-degree side, and back **neck-to-foot** views, side by side. Place each in an equally sized complete-figure presentation area that reserves the space its omitted head would occupy. Leave that upper space clean, with a neck-level crop below it.
- The neck-to-foot figure retains its scale and position within the complete figure. Fit views by uniform scaling and spacing, not stretching the body upward into the omitted head space or narrowing it to fit columns.
- Show the collar or upper costume boundary, a short neck section, torso, arms, lower garments, and footwear where applicable. Preserve garment length, trains, and the design's relationship to feet; do not shorten clothing just to expose shoes.
- Hide hair and hair ornaments only in these costume views, including hanging locks, so shoulders and costume backs remain readable. Preserve capes, collars, and all clothing layers. This is local display visibility, not a hairstyle change or anatomical cutaway.
- Right: a 2×2 grid of frontal head-and-shoulders, 45-degree head-and-shoulders, exact 90-degree side profile, and a closer frontal facial portrait.
- Preserve intrinsic head, neck, and shoulder relationships; only display magnification changes. Keep face identity, features, skin tone, hairstyle, and identifying accessories consistent.
- Use a composed neutral expression unless the user specifies another. Adapt framing to the design rather than prescribing a fixed face-to-chest ratio.
- Repeat the same garment overlaps, structural seams, fastenings, and accessory attachment points across angles. Honor explicit removals instead of restoring objects from the reference.

## 4. Direct generation from the available design

- Produce one English prompt for one complete sheet directly from the supplied portrait, extended image, full-body image, or confirmed design. Do not require a separate full-body generation, approval image, or per-view generation and compositing stage.
- When no image exists yet and the design is confirmed in text, write the sheet from that confirmed design. Refer to the design itself rather than naming a supplied image, and note that no portrait has been rendered yet. Do not request a portrait first, and do not describe an attachment that does not exist.
- Extract the character's identity, visible head-neck-shoulder relationships, upper-body shape, costume construction, and palette. Preserve the visible build and requested stylization rather than imposing a universal head count, height, age, or build.
- Complete unseen anatomy and costume conservatively, consistent with visible anatomy, established age, build, and function. State briefly after the prompt what was inferred; do not claim exact recovery of hidden proportions.
- Separate anatomy from costume: a high belt, armour edge, high-waisted garment, robe hem, or long canvas is not a measurement of anatomical waist position, leg length, or body height. Use this clarification in the finished prompt only when relevant.
- Keep the same underlying anatomy across views, with a **character-specific static pose** (stated weight leg, shoulder line, empty-hand action, and chin/gaze) and consistent weak perspective. Align corresponding neck-base, shoulder, waist, hip, and knee levels, and the supporting feet on one shared contact baseline.

## 5. Dynamic character description

Describe only the particular reference's actual or established features:

1. **Face and visible anatomy**: age cues, derived bone structure (§1A), eye design and iris optics (§1B), skin specular/matte map, 0-or-1 permanent mark.
2. **Hair or equivalent silhouette**: colour, clump structure, arrangement, identifying ornaments.
3. **Costume**: major layers, physical understructure, neckline, shoulder volume, waist-cut construction, lower garments, fastenings, treated vs raw edges.
4. **Palette and materials actually present**, with matching ornament placement and structural logic across angles.

Do not transfer example-specific traits or materials to other characters. A separate style or layout reference supplies only its assigned role, per [../contract/records.md](../contract/records.md) §4. Complete hidden backs and footwear with necessary functional structure rather than new decorative focal points; generated additions remain inferred until adopted.

## 6. Default finish

Use the refined semi-realistic 3DCG finish in [../contract/visual.md](../contract/visual.md) §1 and §5: sculptural three-dimensional form, clearly modelled facial planes, BJD-grade surface refinement with resin-like translucency over living skin, natural subsurface scattering and soft light transitions, volumetric eyes with detailed irises, distinct hair locks with controlled highlights, and physically believable costume materials.

A three-view on white is the layout most likely to drift toward a figurine product shot, so carry the counter-guard into the prompt as a positive description rather than a negation: continuous unbroken anatomy, skin that flexes naturally at every joint, and stitching only where the garments are actually sewn. Keep `doll` and `seams` out of `--no`, per [../contract/visual.md](../contract/visual.md) §11.

A sheet is a presentation render, so its canvas uses sheet-safe studio illumination with coherent light-and-shadow separation and subtle ground contact shadows, rather than a scene's time-of-day lighting. Keep the character's own refinement and material behaviour identical to the in-scene finish.

Explicit media such as ink wash, watercolour, or a painted concept-art finish replace this default according to [../contract/visual.md](../contract/visual.md) §2; drop the PBR and subsurface-scattering terms when they do. Preserve character proportions while changing presentation lighting or finish.

## 7. Assembly and output

Use this order: identity source and proportion anchor; conservative completion and any relevant costume/anatomy distinction; overall canvas; left occupancy, orthographic views, and 4D static pose; right portraits; character-specific face and costume; finish; parameters.

### Identity sheet scaffold

Replace bracketed fields from the current reference, omit inapplicable features, and deliver a complete copy-ready prompt without placeholders:

```text
A professional identity reference sheet of [character], [from the supplied portrait / extended image / full-body reference, OR from the confirmed design when no image exists]. Preserve [identity, head-neck-shoulder relationships, build, costume, palette]. Complete unseen anatomy conservatively, consistent with the established character design.

[Pure white or warm off-white] seamless background chosen by the costume's value, 16:9 landscape canvas: left 58% full-body views, right 42% portraits.

LEFT: front, exact 90-degree side, and back full-body orthographic views, head to toe uncropped inside the left zone, on one shared ground line at identical scale. Standing in a character-specific static pose with [weight-bearing leg/axis], [shoulder-neck line], [empty-hand action], and [chin & gaze direction], differentiated from the rest of the cast. Consistent weak perspective and one shared contact baseline.

RIGHT: a 2x2 grid of bust cells: top-left symmetrical front bust with a fully neutral baseline face, top-right three-quarter bust with a slight tilt and directional gaze, bottom-left pure 90-degree profile bust, bottom-right tight macro of the eyes, nose and lips only, crown and shoulders deliberately cropped out of that cell, carrying [one physical muscle micro-expression].

[Reference-specific face (§1A bone + §1B surface), hair, costume construction with physical understructure, palette and materials. Conservative completion of hidden design details, consistently repeated across views.]

[Selected finish and sheet-safe lighting.] --ar 16:9 --raw --s 150 --no text, labels, logos, watermarks, plastic, waxy, low-poly, cutout
```

### Costume sheet scaffold

```text
A professional costume reference sheet of [character], [from the supplied reference or confirmed design]. Preserve [identity, build, costume construction, palette]. Complete unseen anatomy conservatively.

[Pure white or warm off-white] seamless background, 16:9 landscape canvas: left 55% costume views, right 45% portraits.

LEFT: front, exact 90-degree side, and back neck-to-foot costume views. Place each in an equally sized complete-figure presentation area, leaving clean space for the omitted head above the neck crop. Retain the body's scale within the complete character. Fit views by uniform scaling and spacing, preserving width-to-height relationships. Hide hair and hair ornaments only in these costume views; preserve clothing layers. Standing with [weight-bearing leg/axis], [shoulder line], and [empty-hand action]. Consistent weak perspective, corresponding anatomical levels, and one shared contact baseline.

RIGHT: a 2x2 portrait grid: frontal, 45-degree, exact side profile, and closer frontal facial portrait. Preserve the same intrinsic head, neck and shoulder relationships; only display magnification changes. Frame identifying features appropriately.

[Reference-specific face, hair, costume construction, palette and materials. Conservative completion of hidden design details, consistently repeated across views.]

[Selected finish and sheet-safe lighting.] --ar 16:9 --raw --s 150 --no text, labels, logos, watermarks, plastic, waxy, low-poly, cutout
```

Parameter presets and the aspect-ratio table are in [../contract/visual.md](../contract/visual.md) §3.

## 8. Notes after the prompt

- Briefly identify inferred anatomy or costume and how to attach the supplied reference.
- Do not add a full-body approval checkpoint, fixed measurement claims, or promises of exact identity, proportion, and layout fidelity.
- Corrections to an individual result remain local unless the user requests a general rule.
- For returned-sheet drift, use the repair table in [../engine/04-critique-and-repair.md](../engine/04-critique-and-repair.md) §4.
