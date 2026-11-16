# Engine 04: Adversarial Critique Gate, 12 Generic Autopsies, and Drift Repair

This file owns the **second half of quality control** — the judgment half that `scripts/preflight.py` cannot automate — plus the **returned-image drift repair tables**.

Read §1–§2 before delivering any new design (Mode A, B, C, or Portrait). Read §4 in Review Mode when checking a returned image.

---

## 1. The Adversarial Critique Gate (Mandatory before delivery)

Counted checks (`scripts/preflight.py`) only prove a design is **legal** (right word count, right token caps, ten ledger axes filled). A design can pass every count and still be a soulless template.

Before delivering the prompt, execute this **three-line adversarial critique** and include it right after the 7-point blueprint:

```text
对抗性自检 (Adversarial Critique)
1. 最强套路指控 (Generic Accusation): [Write the harshest 1-sentence summary of why a cynical viewer would call this a generic genre template.]
2. 专属物证反驳 (Specific Rebuttal): [Name 3 concrete, physical decisions in the blueprint that make the generic accusation false — must be drawable nouns, not backstory.]
3. 换人测试结论 (Swap Verdict): [Name what immediately breaks if this face, pose, and outfit are put on another character of the same subgenre.]
```

**Gate rule:**
- If the **Generic Accusation** is more vivid or more accurate than the **Specific Rebuttal**, or if the **Swap Verdict** relies on invisible lore ("another character wouldn't have her sad memories") instead of visible physics ("another elder hasn't knelt at a furnace for ten years, so the heat-reddened lower lids, soot-ringed inner cuffs, and lead-weighted collar yoke would make no sense"), **the design fails**.
- Locate the exact failure mode in §2 below, apply its counter-action to the blueprint and prompt, and re-run the critique before outputting.

---

## 2. The 12 Generic Failure Autopsies

Positive examples get copied; failure autopsies get avoided. Use this diagnostic table during §1 Critique to identify why a draft feels generic and how to break it open.

| # | Failure Mode | Mechanism (Why it happened) | Visible Signal in Draft | Mandatory Counter-Action |
| --- | --- | --- | --- | --- |
| **1** | **默认网红脸 (Default Stock Face)** | Ran §1A bone geometry, but copied iris colour, eyeshadow, lip gloss, or a mole from memory | Ruby/ice-blue/amber irises + dusty-rose shadow + glossy berry lips + under-eye `tear-mole` | Run [02-face-derivation.md](02-face-derivation.md) §1B from scratch: delete the mole (Default = 0), derive iris optics from gaze habit, and change lip state to match speech habit. |
| **2** | **子类型直取 (Subgenre Reflex)** | Let the subgenre name dictate the silhouette, colour, and motif before reading the conflict | Xianxia = white/celadon silk + silver filigree + lotus/cloud; Demonic = black/red + spikes + gold cracks | Open [../atlas/genre-traps.md](../atlas/genre-traps.md), add the subgenre's top 3 reflexes to `IFV Forbidden`, and pick a key colour family from the opposite temperature. |
| **3** | **罚站木偶姿 (Orthographic Mannequin)** | Confused "orthographic alignment" with "neutral pose" | Prompt says `neutral balanced stance` or `weight on left leg, right hand loose` for the third time | Run [01-truth-and-pose.md](01-truth-and-pose.md) §7: assign a specific empty-hand interaction with the garment (adjusting collar, hooking belt, clasping behind back) and shift the weight axis. |
| **4** | **五五分麻袋 (Cheap Proportion Cut)** | Stated `8.5-head` in the identity block, then let the garment cut the body at the natural waist and ankle with equal spacing | Waistband bisects the figure 1:1; layer hems are spaced at equal intervals; cuff ends dead on the wrist joint | Apply Operator 2.1 in [03-costume-and-craft.md](03-costume-and-craft.md): move the visual waist-cut to high Empire (2:5) or dropped hip (5:3), and stagger layer hems at unequal ratios (2cm / 8cm / 25cm). |
| **5** | **死板全对称 (Safe Symmetry)** | Every collar, sleeve, cuff, earring, and sash is mirrored left-to-right | At 10% thumbnail, the left and right halves of the front view are identical | Apply Operator 2.2: introduce **one structural breakpoint** (one slipped shoulder, a single-side slit, an off-centre placket, or an asymmetrical worn trace) plus one facial asymmetry. |
| **6** | **零件堆砌症 (Unemployed Nodes)** | Hit the node count (4 or 8–15) by pasting brooches and chains onto flat cloth | Deleting any two ornament nodes leaves the garment construction completely intact | Give every single node a **mechanical job** (`closes the throat placket`, `weights the split train`, `rivets the shoulder strap to the yoke`). Delete any node that only "decorates". |
| **7** | **无重力纸片衣 (Weightless Shell)** | Named expensive fabrics (`organza, silk, brocade`) without physical support or fold gravity | Giant sleeves, standing collars, or heavy trains float in space with no armature or hang direction | Apply Operator 2.5: name the understructure (`interlined hemp`, `bronze collar stay`, `horsehair hem braid`) and state where gravity pulls the cloth into heavy folds. |
| **8** | **中灰糊成团 (Flat Grayscale Notan)** | Picked harmonious colours that all sit at the same mid-value in grayscale, or put the highest contrast at the boots | Desaturated thumbnail reads as one uniform grey silhouette; face does not pop first | Apply Operator 2.3: separate into 70/25/5 value blocks, push the dark anchor to `#1E1E22` or light mass to `#F2EFE8`, and lock the sharpest dark-light edge at the throat/face. |
| **9** | **同温无对抗 (Monotone Temperature)** | Every colour, metal, and light source sits on the same side of the temperature wheel | Cool blue-black + silver + ice-white under cool light (reads dead/cyan), or all warm brown/gold under warm light (reads muddy) | Apply Operator 2.4: inject **one counter-temperature chromatic anchor** (e.g. a warm cinnabar or raw brass hook inside a cold glacier-grey palette). |
| **10** | **墙纸式满铺 (Wallpaper Clutter)** | Met density requirements by putting equal ornament and high-contrast pattern from head to hem | No open breathing space; hem is as loud as the chest; viewer's eye wanders off the face | Enforce the density gradient (`head > chest > waist > hem`) and carve out **one primary open area** of plain unpatterned cloth or bare skin. |
| **11** | **泛东方大杂烩 (Pan-Oriental Blur)** | Used vague words like `ancient eastern robe, traditional tunic, fantasy hanfu` | Model blends incompatible eras and game clichés into generic AI costume | Replace with exact tailoring mechanics from [../atlas/lexicon.md](../atlas/lexicon.md) §3 (`overlap cross-collar tied at the right rib`, `deep box-pleated mamian apron`, `riveted brigandine plates`). |
| **12** | **先射箭后画靶 (Post-Hoc Rationalization)** | Picked a favourite cliché first, then invented a flimsy excuse to call it "derived" | The Swap Test fails: the "derived" reason ("she is noble so she wears gold") applies to 50 other characters | Strip the element and re-run Step 0 ([01-truth-and-pose.md](01-truth-and-pose.md) §1): link the visual choice to a physical action or wound that no other cast member shares. |

---

## 3. Bidirectional Under-Shoot and Over-Shoot Detection

Run this quick diagnostic when a design feels either too plain (under-designed) or too noisy (over-designed).

### 3.1 Under-shoot (Why it came out plain)

| Measure | Floor | Fix |
| --- | --- | --- |
| **Visible layers** | editorial working 2–3 · editorial high-status 4–5 · glamour 5–6 · ceremonial 6 | add the floating layer first, then a translucent or contrasting inner layer showing a 2–5cm edge |
| **Edge treatment rate** | 60% minimum (editorial) · 80% minimum (glamour) | apply one shared trim language across collar, cuffs, placket, and hem in a single clause |
| **Pattern coverage** | banded minimum for any high-status or glamour figure | carry one motif family at macro / mid / micro scales simultaneously ([../atlas/density.md](../atlas/density.md) §4) |
| **Tight specular** | at least one metal, jade, lacquer, or wet-stone edge | add a polished hardware clasp or metal rim band — the cheapest way to buy material richness |

### 3.2 Over-shoot (Why it came out noisy or muddled)

| Measure | Ceiling | Fix |
| --- | --- | --- |
| **Levers used** | gear 2: 3 · gear 3: 4 · gear 4: 5 | cut to the cap, keeping only levers that serve the seed |
| **Editorial ornament nodes** | 4 total (1 hero + 3 supporting) | delete the weakest node; never merge two into one |
| **Glamour distribution** | strict descent `head > chest > waist > hem` | if waist or hem competes with the head, strip nodes below the waist and leave pattern only |
| **Named fabric types** | 4 maximum in editorial | remove the least load-bearing material |
| **Colour & material token caps** | accent ≤ 2 · anchor ≤ 4 · base ≤ 8 · material ≤ 5 | run `scripts/preflight.py` and trim repeats |

---

## 4. Returned-Image Drift Repair (Review Mode)

When a user supplies a generated sheet or portrait and asks for a review or fix, **inspect only the supplied image** ([../contract/gates.md](../contract/gates.md) §7). Report observed differences first; provide a targeted correction prompt only when requested.

### 4.1 Sheet & rendering drift

| Observed Symptom | Mechanical Cause | Targeted Fix |
| --- | --- | --- |
| **Four busts look identical** | Expression was not scoped per cell | Restate `top-left symmetrical front bust with a fully neutral baseline face` and `bottom-right tight macro only: [micro-expression]`. |
| **Panels merge into one scene** | Grid dividers were suppressed by an outer-frame ban | Add `thin internal hairline dividers separating the four bust cells` in the positive prompt; keep the outer-frame ban. |
| **Outfit differs across views** | Too many competing clauses per view | Switch to Mode A-Split ([../contract/visual.md](../contract/visual.md) §10), shorten garment prose, and raise the cross-view consistency line. |
| **Face lost identity in full-body** | Close-up micro-tokens (pores, lip striation) spent in full-body copy | Move pore/scar/lip micro-texture strictly into the right-side bust cells; keep only bone silhouette and iris colour in the left full-body copy. |
| **Glassy mobile-game skin** | BJD finish misread as wet gloss | Add `smooth porcelain skin with a soft subsurface glow, velvet-matte cheek plane with a controlled specular break on the nose bridge`; remove `glossy, dewy`. |
| **Everything reads flat grey** | Neutral black anchor + no counter-temperature | Give the dark mass an explicit temperature bias (`blue-black`, `warm iron-black`, `green-black`) and add one chromatic anchor. |
| **Cloth looks like a stiff shell** | No weight, understructure, or hang direction | Add `physically-plausible cloth weight` and one gravity clause (`heavy wool dragging the hem low`, `linen gathering at the belt cinch`). |
| **Hair reads as plastic cards** | Mass named without clump architecture | Add `grouped locks with sculpted strand clumps, a soft anime-style highlight band across the crown, individual flyaway strands, no card-like clumping`. |
| **Every character looks like the same person** | Identity set (§1A) or surface set (§1B) was defaulted | Re-run [02-face-derivation.md](02-face-derivation.md) §1A & §1B: push the three bone anchors (13, 11, 1) to new values, change iris optics and periocular weight, and remove any copied mole. |
| **Pose is a generic mannequin** | Used `neutral balanced stance` | Replace with the 4D pose vector from [01-truth-and-pose.md](01-truth-and-pose.md) §7. |

### 4.2 Face parameter drift

| Observed Symptom | Parameter Out of Band | Targeted Fix |
| --- | --- | --- |
| **Reads as a child / chibi** | Eye width > 1.3×, iris fill > 0.98, philtrum too short, head count < 7 | Pull eye width back to 1.05–1.18×, lengthen the philtrum, define the jaw angle, restate the adult head-count band. |
| **Reads as a lifeless mask** | Perfect symmetry, single catchlight, zero muscle tension | Add one alive asymmetry (strand across brow, 3mm mouth corner lift) and the **second catchlight** with a wet lower meniscus. |
| **Reads as uncanny realism** | Nose bridge too heavy, pores visible at full-body distance | Restore `minimal nose bridge`, `defined upper lid line`, `refined anime facial design`, and restrict pores to the macro cell. |
| **Reads as a recast between shots** | Eye craft or bone anchors paraphrased instead of copied | Restore the character record's identity block **word-for-word** ([../contract/records.md](../contract/records.md) §1). |
