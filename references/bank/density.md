# Bank: Ornament Density — Layers, Edges, Nodes, Pattern

Layer 4 of the design stack. Why designs come out plain, and the general mechanics that fix it.

A model asked for "a white robe with ornaments" returns a white robe with ornaments. It does not invent layers, edge treatments, or pattern coverage, because those are construction decisions, not adjectives. Richness cannot be requested; it has to be enumerated.

Ornament is four independent systems, and they are not interchangeable. A design that adds nodes without layers looks like a costume hung with jewellery. A design that adds pattern without edges looks like printed fabric.

| Factor | Fixes | Cost | Where it shows |
| --- | --- | --- | --- |
| **1. Layering** | flatness, thinness, "one dress" | high (silhouette) | full-body silhouette |
| **2. Edge treatment** | unfinishedness, cheapness | lowest per unit of visible gain | medium shot, boundaries |
| **3. Ornament nodes** | lack of memory points | high (competes with the face) | face-to-chest, thumbnail |
| **4. Pattern coverage** | emptiness, bare cloth | lowest per unit of area | everywhere, reads as texture |

**All four factors are required, and none substitutes for another.** This is not a formula — the four are not independent (adding a layer adds two or three edges, so layering changes the edge rate's denominator), and coverage is a class rather than a number. Treat it as four separate gates:

```text
Richness requires: layers >= the register minimum
                   AND edge rate >= the register minimum
                   AND node count >= the register minimum
                   AND coverage >= banded
```

A design that passes only the easy factors reads as one plain garment wearing jewellery. The ordering below is by cost, not by importance.

Four layers with bare edges look cheaper than two layers with every edge finished, because an unfinished edge is a visible omission, and the eye reads omission faster than absence. That asymmetry is the practical takeaway: **edge treatment is the cheapest factor and the first one to fix.**

## 1. Layering

A ceremonial or high-status figure layers **4–6 visible garments**; a working or low-status figure layers **2–3**. Count them in the blueprint before writing anything. For a high-status figure, if you cannot name four garments, you have a dress, not a design.

| Layer | Function | Where it reads |
| --- | --- | --- |
| **Skin-adjacent** | 内衫 / 里衣 / 抹胸 / 底裙 | at the collar opening, the slit, the wrist — rarely fully visible, always partially |
| **Structural** | 中衣 / 束腰 / 胸挡 / 护腕 | the fitted layer that establishes the body; usually the darkest value |
| **Main** | 主袍 / 直领外衣 / 交领 | the largest area; carries the palette |
| **Outer** | 大袖衫 / 罩纱 / 披风 / 霞帔 | the translucent or flowing layer; what makes cloth look expensive |
| **Floating** | 披帛 / 长绶 / 腰侧飘带 / 垂链 | the layer with no structural purpose; it exists to move |
| **Belt/binding** | 腰封 / 系带 / 玉扣 | the pinch point; separates and defines the silhouette |

Three hard rules:

1. **Every layer shows an edge somewhere.** A completely hidden layer is padding. If you add an inner shirt, open the collar enough that a two-centimetre line reads. If you add a veil, make its hem 5–10cm shorter or longer than the layer beneath.
2. **Each layer differs from its neighbour in at least one of value, opacity, or material behaviour.** Two layers of the same white matte silk read as one thick white mass. Translucent over matte, dark under light, sheened over raw.
3. **The floating layer is mandatory for glamour and for any ceremonial figure.** It is the cheapest source of motion, verticality, and cost on the sheet, and it spends no ornament budget because it is cloth, not jewellery.

Prompt translation — never name a layer alone; always name its relationship to its neighbour:

- Bad: `a white gown with an underskirt and a veil`.
- Good: `a translucent pale-grey outer veil cut eight centimetres shorter than the matte white gown beneath it, so a band of the inner skirt reads as a separate layer at the hem`.

## 2. Edge treatment — the highest-return factor

Every garment has 6–12 boundaries. Each is a design decision; the default (leave it raw) is what produces a plain result. Enumerate them; treat most of them.

| Edge | Count on a typical figure |
| --- | --- |
| Collar / neck opening | 1 |
| Centre front closure (门襟) | 1 |
| Sleeve cuff (×2) | 2 |
| Sleeve seam / shoulder line | 2 |
| Waist / belt edge | 1 |
| Hem of each skirt layer | 1–3 |
| Slit edges (×2 per slit) | 2–4 |
| Vent, train edge, waist-sash tail | 1–3 |
| Boot/shoe top line | 2 |
| Veil or outer-layer edge | 1–2 |

Six treatments, in ascending cost:

1. **Contrast piping** (滚边): a 5mm line in a second colour. Cheapest; reads at full-body distance.
2. **Banded trim** (镶边): a 2–4cm woven or embroidered band.
3. **Metal edge** (压边): a thin polished metal or jade rim. Adds a tight specular along the line; reads expensive.
4. **Patterned band** (绣边): the motif repeated in embroidery along the edge.
5. **Dangle trimming** (穗边): short tassels, beads, or chains hanging from the edge. Adds motion and verticality.
6. **Layer reveal**: a contrasting layer deliberately visible past the edge.

**The reuse rule**: do not describe each edge separately. One edge treatment, applied across several edges, stated once:

`collar, cuffs and hem all edged in the same narrow silver filigree band`

That is seven words for three edges, and it buys coherence: one trim language repeated is what makes a costume look designed by one hand rather than assembled.

Treat at least 60% of the edges. Below that, the figure reads as unfinished; above 90% begins to read as upholstery. The 2–4 untreated edges should be the ones you want to read as humble — a working character's cuff, a monk's plain hem.

## 3. Ornament nodes

A node is an object with volume, an individual silhouette, and its own specular — a gem cluster, a filigree brooch, a crown, a chain junction, a jewelled clasp. It is not a pattern. Nodes and patterns do different jobs and cost different amounts:

| | Node | Pattern |
| --- | --- | --- |
| Reads as | an object you could pick up | a surface quality |
| Cost | high — competes with the face | low — reads as texture |
| Budget | capped by register | effectively uncapped |
| Count in a rich design | 4–8 (editorial), 8–15 (glamour) | one family, repeated |
| Failure if overused | clutter, gaudy | printed, flat |

Node placement rules:

- **Nodes belong at junctions, not on expanses.** The throat, the point of a V-neck, the centre of a belt, the shoulder seam, the join of a chain. A node floating in the middle of a plain panel looks pasted on.
- **Nodes form a descending scale.** The largest is at the head or chest; each subsequent node is measurably smaller. Equal-size nodes everywhere read as polka dots.
- **Each node needs a reason to exist.** A clasp closes something; a brooch marks a rank; a chain joins two pieces. A node with no structural job is decoration, and decoration without a job is the first thing the eye discounts.
- **The head may hold a cluster.** In glamour and ceremonial design, treating the crown as a dense group of many small nodes rather than one large one produces the expensive read.

Register caps:

| Register | Nodes | Notes |
| --- | --- | --- |
| **Editorial** | 4 total (1 hero + 3 supporting) | the cap in [material.md](material.md) §2 |
| **Glamour** | 8–15, no hard cap | must descend in size and density head → hem |
| **Ceremonial / royal** | +50% over the register cap | a coronation garment is supposed to be beyond practical |

## 4. Pattern coverage — the cheapest richness

This is the factor plain designs miss entirely. A fully embroidered field costs almost nothing in prompt budget — one clause — and fills the largest area on the sheet. It is also what the eye reads as "elaborate" at a distance, far more than a handful of metal objects.

**The three-scale rule**: carry one motif family at three scales simultaneously:

1. **Macro** — as a node or structural shape: the motif built into the crown, the shoulder, the belt buckle.
2. **Mid** — as a repeating band: an embroidered border, a woven jacquard repeat, a pleat pattern.
3. **Micro** — as scattered or allover texture: tiny embroidered motifs across the skirt field, a woven ground, a stamped repeat.

A single motif at three scales reads as a designed world. Three different motifs at one scale reads as shopping.

Coverage levels — choose one per design:

| Level | What it looks like | Use |
| --- | --- | --- |
| **Bare** | no pattern, material only | working characters, ascetics — must be a choice, never a default |
| **Banded** | 2–4 pattern bands at edges/waist/hem | the safe minimum for a designed-looking figure |
| **Fielded** | one large area fully patterned (a skirt, a sleeve) | the "elaborate" read; cheapest way to look expensive |
| **Allover** | pattern across most surfaces, varying scale | ceremonial, glamour, high-status |
| **Layered pattern** | pattern on pattern, different scale per layer | glamour at gear 3+, or any imperial figure |

Pattern must be tone-on-tone or low-contrast by default. High-contrast pattern everywhere turns into loud wallpaper. The pattern is read as material, not as image: `tone-on-tone silver thread woven in a five-petal repeat across the skirt, only visible where the light crosses the nap`.

## 5. The density gradient

Abundance and clutter are not distinguished by total amount. They are distinguished by distribution. Rich designs are almost always unevenly rich:

> **Density descends: head > chest > waist > hands > hem.**

and within each zone:

> **Nodes and pattern co-exist, but nodes decrease faster than pattern.**

That last rule is the difference between "ornate" and "gaudy": at the hem, a rich costume is still patterned but no longer node-bearing. The embroidery runs to the floor; the jewellery stops at the waist.

**The single failure that disqualifies a rich design**: even distribution. If the head, chest, waist, and hem are equally dense, the result is wallpaper. Move density up; never add more below to balance.

## 6. Prompt translation — all four factors in 80–110 words

The four factors are cheap when written as construction and expensive when written as adjectives.

**Banned**: the richness adjectives listed in [../contract/gates.md](../contract/gates.md) §6. They request richness without describing it, and the model answers with more surface noise on the same plain garment.

**The four-clause template** (roughly 25 words each):

1. **Layer clause** — name 3–5 layers and one relationship between two:
   `four layers: a dark inner gown, a fitted pale bodice over it, a translucent outer veil, and a long floating sash at each hip`
2. **Edge clause** — one trim language across several edges:
   `collar, cuffs and both hem edges banded in the same narrow silver filigree`
3. **Node clause** — 2–4 nodes with their structural job and descending scale:
   `a jewelled clasp at the throat, a smaller one at the belt, and chains running from the collar to the shoulders`
4. **Pattern clause** — one motif family, one coverage level, tone-on-tone:
   `a five-petal repeat worked tone-on-tone in silver thread across the whole skirt field, and again at a fifth of the size on the cuffs`

Worked comparison:

- Plain (26 words, and it will render plain): `She wears a white gown with a silver belt and some decorative hairpins.`
- Rich (94 words): `She wears four layers: a dark slate inner gown, a fitted pearl bodice over it, a translucent outer veil cut shorter than the gown beneath so the inner hem reads, and a floating sash at each hip. Collar, cuffs and both hems are banded in the same narrow silver filigree. A jewelled clasp closes the throat, a smaller one the belt, and thin chains run from the collar to both shoulders. A five-petal repeat is worked tone-on-tone in silver thread across the whole skirt field, and again at a fifth of the size on the cuffs.`

Both name the same garment. Only one has a design in it.

## 7. Why plain happens — a diagnostic

Run this before blaming the render.

| Symptom | Cause | Fix |
| --- | --- | --- |
| "It's a nice dress" | 1–2 layers, no floating layer | add layers 3 and 5 from §1 |
| "It looks unfinished" | bare edges | treat 60%+ of edges, one trim language |
| "It looks cheap" | no tight specular anywhere | add a metal or jade edge, or one polished node |
| "It's flat" | no translucency, no pattern | add one translucent outer layer + banded pattern |
| "It's plain but I can't say why" | zero pattern coverage | field or band one motif family |
| "It's gaudy" | even density, or nodes at the hem | fix the gradient, not the total |
| "The prompt said elaborate and it still looks simple" | richness requested as an adjective | rewrite with the four-clause template |
| "It reads as a costume, not a garment" | nodes with no structural job | give every node a closure or junction to sit on |

One more cause: under-layering is often a brief failure rather than a design failure. If the brief says "a female cultivator", the safe reading is one robe. Ceremony, rank, and occasion justify layers — name the occasion in the thesis. "A sect elder at her own investiture" gets you six layers; "a sect elder" gets you one.

## 8. Register and gear settings

| Setting | Layers | Edge rate | Nodes | Pattern |
| --- | --- | --- | --- | --- |
| **Editorial, working character** | 2–3 | 60–70% | 4 | bare or banded |
| **Editorial, high status** | 4–5 | 70–80% | 4 | banded or fielded |
| **Glamour** | 5–6 | 80%+ | 8–15, descending | fielded or allover |
| **Ceremonial / imperial** | 6, incl. two floating | 90% | 15+, clustered at head | layered pattern |

These settings stack on top of the risk dial in [../contract/gates.md](../contract/gates.md) §3 and never replace it: gear decides how far the design deviates; this table decides how much material is in it. A gear-2 glamour character can be very rich and still conventional; a gear-3 editorial character can be sparse and still strange.
