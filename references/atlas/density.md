# Atlas: Ornament Density — Layers, Edges, Nodes, Pattern, and Batch Spread

Layer 4 coordinate system. Richness cannot be requested with adjectives (`elaborate, intricate, ornate` are banned per [../contract/gates.md](../contract/gates.md) §6); it must be **enumerated across four independent structural factors**.

| Factor | What it fixes | Visual cost | Where it reads |
| --- | --- | --- | --- |
| **1. Layering** | flatness, thinness, "one plain dress" | high (changes silhouette) | full-body outline |
| **2. Edge treatment** | unfinishedness, cheap cosplay look | **lowest cost per unit of gain** | medium shot, every boundary |
| **3. Ornament nodes** | lack of focal hardware / memory points | high (competes with the face) | throat, chest, crown, waist |
| **4. Pattern coverage** | empty bare cloth expanses | low (reads as material texture) | across garment fields |

**All four factors are required, and none substitutes for another:**
`Richness = (Layers in band) AND (Edge rate in band) AND (Nodes in band with mechanical jobs) AND (Pattern at 3 scales)`.

---

## 1. Factor 1: Layering

A high-status or glamour figure layers **4–6 visible garments**; a working or low-status figure layers **2–3**. Enumerate them in order in blueprint point 5.

| Layer slot | Structural role | Where its edge must show |
| --- | --- | --- |
| **1. Skin-adjacent** | inner shift, high-neck under-collar, wrist liner, bodice lining | 1–3cm line at throat, cuff, or side slit |
| **2. Structural core** | fitted waistcoat, corset stay, chest guard, bound mid-robe | establishes torso proportion; usually the darkest or most matte value |
| **3. Main field** | primary robe, coat, or pleated skirt | carries the 70% hue and the micro/mid pattern |
| **4. Outer shell** | translucent over-robe, split mantle, short cape, structured jacket | cut 5–15cm shorter or longer than Layer 3 so both hems read |
| **5. Floating layer** | long waist-tassels, trailing shoulder stole, split back-streamers, hanging chains | mandatory in glamour/ceremonial; exists to catch light and motion |
| **6. Binding / pinch** | wide waist-corset, leather harness, metal girdle, knotted sash | defines the waist-cut height ([../engine/03-costume-and-craft.md](../engine/03-costume-and-craft.md) §2.1) |

Three hard rules:
1. **Every counted layer must show a visible edge.** A completely hidden inner shirt is padding, not a visual layer. State the centimetre offset (`an outer smoke-gauze coat cut ten centimetres shorter than the matte linen skirt beneath`).
2. **Adjacent layers must contrast in value, opacity, or light behaviour.** Never stack matte white silk on matte white silk. Put translucent over matte, dark under light, or coarse weave against tight specular.
3. **Name the physical support** for any rigid or voluminous layer per Operator 2.5.

---

## 2. Factor 2: Edge Treatment (Highest Return on Budget)

Every garment has **6–12 boundaries** (collar, front placket, 2 cuffs, 2 shoulder seams, waist edge, 1–3 layer hems, 2–4 slit edges, boot tops). Leaving them raw by default is why renders look unfinished.

Six edge treatments (pick **one primary trim language** per character and repeat it across 60–90% of the edges in a single clause):

1. **Contrast piping (窄滚边)**: a 3–5mm cord or folded bias strip in a contrasting value/temperature.
2. **Woven/embroidered band (宽镶边)**: a 2–4cm structured border carrying the mid-scale motif.
3. **Rigid metal/mineral rim (金属/玉石压边)**: hammered bronze, tarnished silver, or dark iron binding along a stiff collar, shoulder guard, or corset edge — buys an immediate tight specular highlight.
4. **Raw/frayed/fused edge (刻意毛边/焦边)**: unhemmed selvedge, salt-stiffened fray, or heat-sealed edge.
5. **Pendant fringe/link edge (垂穗/链边)**: short metal links, seed-beads, or knotted cords hanging from a mantle or hem.
6. **Stepped layer reveal (叠边外露)**: inner lining folded back over the outer cuff or lapel.

**The Deliberately-Raw Set (未处理边集):**
Treat **60–80% of edges in editorial** and **80–90% in glamour**. The remaining **10–40% deliberately untreated edges** are where character truth lives (e.g. `collar, placket, and shoulder yoke bound in riveted dark-iron rim, while the lower hem and left working cuff are left raw and unhemmed`). Always name both the treated set and the raw set in blueprint point 5.

---

## 3. Factor 3: Ornament Nodes

A **node** is a 3D hardware or jewellery object with its own silhouette, volume, and specular highlight (clasp, buckle, brooch, hairpin cluster, harness ring). It is not flat surface embroidery.

Four rules that separate design from clutter:
1. **Every node must have a mechanical or structural job.** It must close a placket, pin a fold, weight a hem, or join two straps. If deleting a node does not cause a garment piece to fall open or lose tension, delete it ([../engine/04-critique-and-repair.md](../engine/04-critique-and-repair.md) §2, Mode 6).
2. **Nodes sit at structural junctions, never floating in the middle of empty cloth.** Place them at the throat hollow, clavicle notch, belt cinch, slit apex, or shoulder hinge.
3. **Strict descending scale (Rule of Three):** The hero node is the largest; supporting nodes step down to **at most one-third the visual weight** of the hero. Equal-sized nodes read as buttons on a uniform.
4. **Register caps:**
   - **Editorial:** maximum **4 nodes total** (`1 hero + up to 3 supporting`).
   - **Glamour:** **8–15 nodes**, clustered heavily at the crown/head and chest, thinning strictly downward (`head > chest > waist > hem`, zero nodes on the lower hem).

---

## 4. Factor 4: Pattern Coverage at Three Scales

A single motif family (grown from the seed in [../engine/03-costume-and-craft.md](../engine/03-costume-and-craft.md) §1) must appear at **three scales simultaneously**:

1. **Macro scale (Structural / Node):** the motif cast as the 3D shape of the hero clasp, crown frame, or cut-out contour.
2. **Mid scale (Border / Band):** the motif repeated along the collar band, waist girdle, or cuff trim.
3. **Micro scale (Field texture):** the motif worked **tone-on-tone** (jacquard weave, blind embossing, quilted stitch, or low-contrast thread) across a large fabric expanse, catching light only at grazing angles.

Coverage levels:
- **Bare:** zero pattern, weave texture only (strict ascetic or impoverished working character — must be deliberate).
- **Banded:** pattern confined to 2–4 structural borders (minimum for designed figures).
- **Fielded:** one major garment panel (e.g. the main skirt or outer coat) carries the micro repeat across its field, while adjacent panels stay plain (**one primary open area is mandatory**).
- **Allover / Layered:** multiple layers carry different scales of the motif (glamour / ceremonial).

---

## 5. The Density Gradient & Prompt Translation

> **Law of Vertical Descent:** `Head / Crown > Chest / Throat > Waist / Hands > Lower Hem`.
> Within each zone, **3D nodes drop to zero before surface pattern does** (at the hem, embroidery may continue, but hardware/jewellery stops).

### The 80–110 Word Four-Clause Prompt Template

Write all four factors into Block 4 of the English prompt as four concrete construction sentences — never as adjectives:
1. **Layer sentence (~25 words):** count + order + centimetre offset + opacity/value contrast + physical understructure.
2. **Edge sentence (~20 words):** one shared trim language across the treated boundaries + explicit mention of the 1–3 raw boundaries.
3. **Node sentence (~25 words):** hero node + supporting nodes in descending size, naming the exact closure or junction job of each.
4. **Pattern sentence (~25 words):** the motif family named at macro, mid, and tone-on-tone micro scales, plus the location of the **unpatterned open breathing area**.

---

## 6. Register Bands & Batch Band-Spread (§6A)

| Setting | Visible Layers | Treated Edge Rate | Ornament Nodes | Pattern Level |
| --- | --- | --- | --- | --- |
| **Editorial — Working / Low-Status** | 2–3 | 60–70% | 2–4 (1 hero + 1–3 functional clasps) | Bare or Banded |
| **Editorial — High-Status / Formal** | 4–5 | 70–80% | 4 (1 hero + 3 supporting) | Banded or Fielded |
| **Glamour** | 5–6 (incl. 1 floating) | 80–90% | 8–15 (descending head → waist) | Fielded or Allover |
| **Ceremonial / Imperial** | 6 (incl. 2 floating) | 85–90% | 12–18 (clustered at crown/yoke) | Layered pattern |

### 6A. Batch Band-Spread Rule

Treating the table above as a single fixed target (e.g. giving every editorial character `4 layers, 73% edges, 4 nodes, fielded`) creates structural clones.

- **Two characters in the same register may not match on more than two of the four density numbers.** If Character A is `glamour: 5 layers · 82% edges · 8 nodes · fielded`, Character B in `glamour` must move to e.g. `6 layers · 88% edges · 12 nodes · allover`.
- **The Untreated Raw Edge Set must differ between adjacent characters.** If Character A leaves cuffs and boot-tops raw, Character B must finish the cuffs and leave the side-slits or inner collar raw instead.
- Report the four density numbers against the previous ledger row in blueprint point 5.
