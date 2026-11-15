# Bank: Framing — Vertical Narrative, Widescreen, and Sheet Canvas

Aspect ratio is not a delivery detail. It decides how much of the figure the viewer sees, where the focal point can live, and whether the image survives the interface it will be shown in.

This file covers the **narrative canvas** — the images that carry a story: portraits, first frames, key art, scene plates. Sheet canvas is owned by [../contract/visual.md](../contract/visual.md) §10 and [../pipeline/sheet.md](../pipeline/sheet.md).

Read the section for the target canvas before choosing a composition. Do not take a ratio from an attached reference unless that reference is the target frame.

## 1. Choose the canvas by use, not by habit

| Canvas | Ratio | Use |
| --- | --- | --- |
| **Vertical narrative** | 9:16 | short drama, manhua drama, vertical mobile drama, phone-first key art, 追更 covers |
| **Portrait** | 3:4 | character portrait, half body, character intro card in a feed |
| **Widescreen** | 16:9 | scene base, cinematic key art, desktop cover, cutscene still |
| **Square** | 1:1 | social tile, face sheet, avatar |
| **Sheets** | 16:9 / 3:2 / 1:1 | see the sheet canvas rules, [../contract/visual.md](../contract/visual.md) §10 |

The  value and preset suffix for each canvas are in [../contract/visual.md](../contract/visual.md) §3. This file decides **which** canvas a shot needs; that file decides how to write it.

**The most common framing error in this pack's own subject matter** is producing a 16:9 seven-panel sheet for a vertical drama, then trying to crop it. A sheet is a specification document; a first frame is a shot. They have different canvases and neither converts into the other.

## 2. Vertical 9:16 — the narrative default for short drama

Vertical is not widescreen rotated. The frame has a different centre of gravity, a different information budget, and a different relationship with text.

### 2.1 Figure occupancy

| Shot | Figure occupies | Frame edges fall | Prompt language |
| --- | --- | --- | --- |
| **Full figure** | 70–80% of frame height, feet clear of the bottom safe area | above the crown, below the feet | `full body, head near the top third, feet clear of the lower edge` |
| **Cowboy / mid** | head to mid-thigh, 55–65% of height | above the crown, through the thigh | `three-quarter framing, cropped at the mid-thigh` |
| **Bust** | head and shoulders, 40–50% of height, placed in the upper half | through the chest | `bust framing, shoulders and collarbone in frame` |
| **Face** | head fills 55–70% of the width | through the shoulders, crown near the top | `close framing, the head filling most of the width` |

In vertical, a centred figure with a straight-on axis reads as a product photo. The vertical frame wants either a deliberate turn or a deliberate off-centre placement.

### 2.2 The vertical composition line

Three bands, and the face must sit in the top one:

| Band | Height | Holds |
| --- | --- | --- |
| **Top** | top 10–35% | the face, the headpiece, the one readable expression |
| **Middle** | 35–75% | the chest ornament, the hands, the silhouette's turning point |
| **Bottom** | 75–100% | hem, boots, floor contact, and the safe area for captions |

- The face belongs in the upper third. A vertically centred face wastes the frame and reads like a passport photo.
- Below 78% is caption space. Keep it quiet: a plain run of fabric, a floor, a shadow. Do not put the hero ornament or the hem's detail there.
- The grain of a vertical frame is vertical. Vertical elements — a column silhouette, hanging hair, a train, a sword line, a falling sleeve — read twice as strong here. Horizontal breadth is wasted.

### 2.3 Vertical information budget

A vertical frame holds less than a widescreen of the same pixel count, because the eye scans it in a single downward pass. Consequences:

- **One focal point, and one supporting element.** A widescreen can carry three readable groups. A vertical cannot.
- **Depth comes from layering, not width.** Foreground occlusion, a mid-ground figure, a distant silhouette stack vertically. There is no room for a wide foreground frame element.
- **Detail density should fall down the frame**, which happens to be the same gradient as ornament density. Vertical and the density gradient reinforce each other.
- **Wide sleeve volume and horizontal shoulder breadth** cost frame and return little. If a design's hero feature is horizontal, it wants 16:9.

### 2.4 Text and safe area

Most vertical platforms overlay captions, a progress bar, and UI. Assume they exist.

- Keep the bottom **12–15%** free of critical content.
- Keep the top **8–10%** free of the crown's tallest element if the platform puts a title there.
- Do not ask for readable lettering in a vertical frame that will also carry captions; the two compete. When signage is required, put it in the middle band.

### 2.5 Vertical scene plates

| Element | Widescreen habit | Vertical requirement |
| --- | --- | --- |
| Horizon | anywhere | **low**, in the lower third — a centred horizon halves the frame |
| Leading lines | converge horizontally | run vertically: roads away from camera, stairs, a corridor, a waterfall |
| Foreground frame | wide branches, an arch | a vertical occluder: a pillar, a doorway edge, a hanging banner |
| Depth cue | atmospheric haze across width | haze by height, and one silhouetted layer behind another |
| Character space | left or right third | upper-middle, with the lower frame free |

## 3. Widescreen 16:9

Use for scene bases, cinematic key art, and cutscene stills. Its strength is horizontal breadth and layered depth; its weakness is that a single figure gets lost.

- **Scene plates** default here. Landscape establishes place; vertical establishes person.
- **Figures** should occupy one third, not the centre, and the frame should show environment on both sides. Horizontally centred single figures in 16:9 read as a stock photo.
- **Multi-character staging** is where 16:9 earns its keep: two figures in conversation, a group, a crowd with reading order left to right.
- **Do not** put seven panels of orthographic views in a 9:16 frame. The panels compress below the resolution the eye design needs — see [../contract/visual.md](../contract/visual.md) §10.

## 4. Portrait 3:4

The default for a one-off character portrait. It holds a head-to-waist figure with room around the head and is the right shape for a feed thumbnail.

- Frame head to waist, centred or slight three-quarter.
- Leave air above the crown — roughly one head height — or the figure reads as cramped.
- The bottom edge cuts at the waist, not at the hip joint.
- Background stays simple; this canvas is small, and background detail competes with the face.

## 5. Canvas and consistency across a sequence

When several images belong to one production:

- **Lock one canvas per shot type** and record it. A vertical drama does not mix 9:16 and 16:9 across its own shots.
- **Sheets and narrative frames are different product families.** The sheet is 16:9 for panel resolution reasons; the first frame is 9:16 for the interface. Converting between them is a recomposition, not a crop.
- **A reference's ratio is not a target's ratio.** An attached portrait is 3:4 because it is a portrait; that does not make the scene 3:4.
- When the user supplies a source frame to extend or edit, **inherit that frame** rather than resetting to 16:9. See [../pipeline/scene-edit.md](../pipeline/scene-edit.md).

## 6. Framing diagnosis

| Symptom | Cause | Fix |
| --- | --- | --- |
| Figure reads as a product photo | centred, straight-on, even light, full symmetry | turn 15–30°, move off centre, add one asymmetry |
| Vertical frame feels empty at the bottom | the figure is vertically centred | raise the face into the upper third, let a quiet hem or floor take the lower band |
| Vertical frame feels crowded | three or more competing groups in the top band | cut to one focal plus one support |
| Widescreen figure gets lost | single figure centred in a wide frame | move to a third, raise silhouette contrast against the background |
| Text collides with content | hero ornament in the bottom band | clear the lower 12–15% |
| Sheet panels too soft to read the eyes | seven panels in a frame too small for them | split the sheet, or raise the canvas — never add detail words |
| Scene and character look pasted together | character lighting independent of the scene | one key direction, shared exposure, contact shadows — see [../contract/visual.md](../contract/visual.md) §7 |
| A crop was expected to produce a new shot | the request was a recomposition | re-frame and re-describe; a crop changes framing, not the camera |
