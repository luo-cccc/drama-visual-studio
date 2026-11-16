# Gates: Lock, IFV, Register, Risk, No-Props, Swap Test, 10-Axis Batch

This file holds the cross-cutting constraints that apply in **every** mode and register. A rule appears here once. Other files reference the section number and never restate the text.

## 1. Lock and IFV triple before design

Lock one genre, one subgenre, one risk level, and one register **before** choosing a motif, and immediately declare the character's **IFV triple** (Invariant / Free / Forbidden).

| Genre | Subgenres (all peers — none is the default) |
| --- | --- |
| Xianxia | Sect-Ranked / Rogue / Clan-Born / Tribulation-Marked / Demonic-Path / Beast-Blood |
| Xuanhuan | Cultivation-sect politics / beast-tamer / imperial-ascension / wasteland |
| Wuxia | Grounded martial / tragic swordsman / sect intrigue |
| Dark Fantasy / Gothic | Sacred ruin / courtly horror / death cult |
| Modern / Contemporary Couture | Noir fixer / corporate / street / service work |
| Sci-fi / Cyber | Neo-oriental / hard-tech / biotech |
| Republican / Modern Historical | 1930s / wartime / old-money / working class |

**No subgenre is the default.** If the brief names only a genre, the subgenre is undetermined: infer it from the story's actual state and say so, or offer two contrasting subgenres in Mode B. Read [../atlas/genre-traps.md](../atlas/genre-traps.md) for the locked subgenre's **Training-Mean Traps** and **Physical Pressure Anchors** — never as a menu of ready-made outfits.

Write the lock and the **IFV triple** before any design work:

```text
锁定行: [genre] / [subgenre] / [pigment family] / [silhouette family] / [gear: risk level] / [register]
IFV 声明:
  - Invariant (不变量): [1 physical structural rule locked to carry the character's thesis]
  - Free (自由变量): [2–3 garment/construction axes left open to explore in this design]
  - Forbidden (题材禁令): [3 concrete clichés from atlas/genre-traps.md or character logic strictly banned here]
```

Rules for the IFV triple:

- **Invariant** must be a physical structure or posture lock derived from the script (e.g. `collar locked rigid and high to hide a throat scar; shoulder line strictly horizontal`), never a vague mood.
- **Free** proves the design was not retrieved as a pre-packaged row. If Free is empty, the design is a template.
- **Forbidden** blocks the model's training-mean reflex for that subgenre before any garment line is written (e.g. `no floating ribbons, no lotus hair crown, no under-eye tear-mole`).

Name exactly one silhouette family. Name the palette as pigments, not moods.

## 2. Register

`gear` sets how far a design deviates. `register` sets what it is optimising for. They are independent.

| Register | Optimises for | Typical use |
| --- | --- | --- |
| **editorial** (default) | credibility — a person who could exist, with evidence worn on them | character bibles, game assets, IP pitch, key art |
| **glamour** | desirability — a figure the audience wants to be, or wants to keep looking at | manhua-drama, short drama, vertical mobile drama, cover art, weekly episodes |

Infer from the brief: 漫剧人设 / 短剧 / 封面 / 头图 / 追更 → glamour; 概念稿 / 设定集 / 游戏资产 / 概念片 → editorial. When still unclear, ask — the two registers produce incompatible acceptance criteria.

Glamour overrides five constraints; everything else still applies:

| Constraint | editorial | glamour |
| --- | --- | --- |
| Imperfections | two required, visible at full-body distance | zero to one, zero preferred; flawlessness is the product |
| Contradiction | one from directions 1–6 | direction 7 is the native direction; directions 1–6 are legal for a deliberately fallen, working, or paying-for-it character. See the batch rule in §9 — the **signal** must differ even when the direction does not |
| Ornament nodes | one hero + at most three supporting | no cap inside the [../atlas/density.md](../atlas/density.md) §6 density band, but density must descend: head > chest > waist > hem |
| Hero node | one ornament node, never a prop | hair or a headpiece may be the hero |
| Palette | avoid moon white / celadon / ink / cinnabar unless the brief asks | the category's native range, so it is legal and common — but it is **not a default**. Choose it or don't; the batch rule in §9 means not every character in one project may sit in it |

**Direction 7 in glamour is a family, not a single look.** `flawless surface plus one lethal signal` is the formula; the signal is the design decision. A wire-thin collar chain, impossible symmetry, a hairline port, a breath of frost, ash-stained fingertips — pick one derived from the character's conflict, and make it the only one. Two glamour characters in one project may both be direction 7 as long as the signal is visibly different; they may not share the signal.

**The native-range trap.** Glamour's palette column reads as permission, and repeated over a project it becomes a single look: pearl white, silver, moon white, one saturated accent, high-key light, Top-Peak Cascade, direction 7. Five characters designed under that column are one character five times. The register picks acceptance criteria; it does not pick the design. §9 exists because this column is the most common cause of a homogenised cast.

Glamour's one material obligation: flawlessness is not featurelessness. Damage is absent; BJD surface perfection carries the credibility — porcelain clarity, a controlled specular, sculpted strand clumps, a wet lower lid, a bright secondary eye reflection.

## 3. Risk gear

| Level | Name | What changes | Levers allowed | Use |
| --- | --- | --- | --- | --- |
| **1** | **Polished** | current system; no rule broken; commercial-safe | 0 | IP-safe briefs only |
| **2** | **Signature** | one strong concept, one unexpected material or colour, one proportion exaggeration; still wearable | 2–3 | **default for original characters** |
| **3** | **Avant-garde** | distorted proportion, extreme volume, deconstruction, one "wrong" element; runway/experimental | 3–4 | hero looks, villains, icons |
| **4** | **Surreal / Theatrical** | garment as object, body extension, impossible physics, grotesque or camp | up to 5 | gods, demons, concept pieces |

Choose a level before the motif, together with the genre lock. **Default to Signature.** Polished only when the brief demands commercial safety. Avant-garde and Surreal must still keep the face as the first focal point.

**The gear is also a batch axis.** A project where every character resolves at gear 2 Signature has a system, not a cast. Grade the cast: most characters at 2, one or two at 1 (the ones the world has flattened), the dangerous or iconic ones at 3. A single character carrying the project's only gear-3 design reads as the protagonist even if they are not.

Gear names are risk levels, not registers. Signature, Avant-garde, and Surreal can each be delivered in either the editorial or the glamour register: the level says how far the design deviates, the register says what it optimises for.

**The lever count is a cap, not a target.** A gear-3 design that uses six levers is not more avant-garde than one that uses four; it is unreadable, and the extra levers cancel each other.

### Risk calibration for the house style

Semi-real 3D game CG with an anime face changes what each lever costs:

- **Anything at or above the neck is cheap risk.** Proportion distortion, oversized ornament, jewel-scale exaggeration, extreme hair volume — the anime pillar makes these read as intentional design. Spend levers at the head and silhouette first.
- **Anything material is expensive risk.** Cloth weight, drape, attachment, and physical support still have to hold up, because the game-CG pillar renders them honestly. A bustle, crinoline, or shoulder frame must name its understructure or it reads as a modelling bug.
- **Impossible physics is available again, in BJD terms.** A floating blade halo, a garment that holds a shape with no support, hair that ignores gravity — these read as stylization. Use it deliberately and keep the face as the anchor.
- **Material transgression is strong.** Glass, resin, moss, living vine, paper pulp, liquid metal all work; the BJD finish makes them read as high-end product.
- **"Shouldn't be there" elements are cheap.** A material from another world costs less here than in realism; it still needs a design reason.
- **The one thing that never gets cheap**: the face must stay inside the proportion band in [visual.md](visual.md) §4. Push the eye ratio past 1.6× or the head count past 9 and the sheet drifts to chibi — a different product, not a bolder one.

The ten levers themselves live in [../engine/03-costume-and-craft.md](../engine/03-costume-and-craft.md) §3.1.

## 4. No-props rule

Design the person, not their inventory. **No held or carried objects in a character sheet**, in either register: no weapons, artifacts, fans, flutes, lanterns, or floating sigils. Hands stay empty, touch the hair, or engage the garment.

- **Worn ornaments are in scope**: crowns, earrings, hairpins, hair chains, belts, bracelets, collars, veil pins, jewellery. The test is held/carried → out; worn → in.
- **A script-required weapon is designed in the shot prompt**, as a shot-level asset. It is matched to the sheet's palette and motif, and must never occlude the torso or back in the sheet. Say so once in the delivery.
- **If removing the object makes the design collapse, the load was never in the character.** Migrate it into posture, wear, a stain, a bracing stance, or an ornament built into the garment.
- **Ornament attachment is strict on the body and free at the head**: a blade fragment, chain, or plate on a load-bearing part of the garment shows how it is fixed — welded, riveted, cord-bound, or pierced through the fabric. At the crown and shoulders a levitating piece is legal; on a load-bearing garment it is not.
- **Never force a clothing checklist** onto a persona that calls for simplicity, asymmetry, or languid negative space. Density is a tool for the chosen design, not a quota imposed on every character.

| Instead of this | Design this |
| --- | --- |
| a prop grown from the same motif as the outfit | ornaments grown from the seed; the held object is a separate shot asset |
| a weapon held at arm's length | hands empty, touching the hair, or braced on the garment |
| a blade hovering beside one shoulder | a blade-fragment ornament attached to a pauldron by chain |
| a scabbard at the hip | shot-level only; keep the hip line clean in the sheet |
| a needle held mid-air | a threaded needle kept in the collar as a worn ornament |

## 5. Conflict resolution

Use this order:

1. The user's current explicit request.
2. The character or location record's locked fields ([records.md](records.md)).
3. The selected workflow's defaults.

Within a record:

- **Identity** beats style, layout, and engine syntax.
- **Confirmed style and finish** beat this skill's default 3DCG language.
- **Current accepted version** beats an older image for state; an older image can support structure but must not restore removed objects or undo later changes.
- **Engine syntax** is always the downstream workflow's: a Midjourney prompt keeps `--ar`, `--raw`, `--s`, and a short `--no`; a GPT Image 2 prompt uses natural language and no MJ flags.
- If the record and the selected scene version conflict materially, ask one focused question; do not silently merge incompatible designs.

Revise only what the request changes. Preserve explicit user choices, identity details, requested canvas shape, and confirmed revisions.

## 6. Banned prompt language

One list, binding in every register and every engine.

**Empty fluff adjectives:** `gorgeous`, `masterpiece`, `breathtaking`, `stunning`, `very detailed`, `highly detailed`, `beautiful texture`, `ultra detailed`, `8k`, `4k`.

**Richness requested as an adjective:** `elaborate`, `intricate`, `ornate`, `richly decorated`, `lavishly detailed`. Enumerate layers, edges, nodes, and pattern coverage instead, per [../atlas/density.md](../atlas/density.md) §5.

**Review vocabulary in the English prompt:** `hero ornament`, `primary open area`, `design thesis`, `aesthetic order`, `gravity topology`, `design evidence`. Translate each into visible description: "hero ornament" becomes the loudest element, "primary open area" becomes the one quiet area, "gravity topology" becomes the density sitting high or low. A model reading "the filigree is the hero ornament" learns nothing about pixels.

**Engine settings dressed as images:** `roughness 0.4`, `metallic 1.0`, `IOR 1.5`, and any shader parameter.

**Structure noise:** bracketed section headers, numeric percentages, comma-spliced lists of three ideas standing in for one design.

**Bare generic pose strings:** `neutral balanced stance` written without a concrete weight-bearing leg, shoulder line, empty-hand action, and chin/gaze vector.

Also banned as evidence: a style word used in place of an observation. `cinematic`, `game CG`, `BJD`, `anime`, `cinematic lighting` describe a production standard, not this character. Replace each with a named light direction, a named material behaviour, or a named depth cue.

## 7. Capability limits

State these plainly when they bear on the request. They are not hedging; they are the difference between a promise and a prompt.

- **This skill delivers text.** Prompt text, design specs, records, and review findings. It does not generate or edit images, and does not configure a renderer, mask, structure guide, ControlNet input, API field, or reference binding. Describing a mask or a reference binding does not execute it.
- **A prompt does not lock geometry.** Prompts, reference images, seeds, and style codes do not guarantee identity, proportion, layout, pixel preservation, or cross-image consistency. Do not promise those outcomes.
- **Visual claims require an actual image.** Do not declare a sheet, scene, or variation visually correct without inspecting a supplied image. Do not claim to have made an overlay, measurement, or comparison unless you did.
- **No invented observations.** When only text exists, use it provisionally and say the visual check is pending. When a reference is missing, say matching awaits it rather than describing an attachment that is not there.
- **No invented parameters.** Do not invent pixel dimensions, stylization values, API settings, version IDs, filenames, or measurements. If a source ratio is unavailable, say to retain that frame and leave its numeric flag unspecified.
- **Engine behaviour is version-dependent.** Version claims live only in [visual.md](visual.md) §3 and carry a verify-before-relying marker. Do not restate them as settled fact elsewhere.
- **Technical vocabulary describes a target appearance.** PBR, subsurface scattering, and global illumination do not configure a pipeline and do not prove one ran.

## 8. Craft versus decision — and The Swap Test

Every line this skill asks you to write is one of two kinds. Confusing them is the mechanism behind a cast of identical faces and costumes.

| Kind | What it is | How to write it | Example |
| --- | --- | --- | --- |
| **Craft** | how to render a thing so it reads as the house style | **verbatim, every time, never varied** | `radial iris fibre with a darker limbal ring`; `smooth porcelain skin with a soft subsurface glow`; `grouped locks with sculpted strand clumps` |
| **Decision** | what this particular character is across all four dimensions (Bone, Surface, Pose, Garment) | **derived from the character's specific facts, never defaulted** | facial index `1.38` vs `1.52`; iris optics `smoke-grey matte` vs `amber-ochre`; pose `weight on locked left leg, thumb hooked in belt` vs `weight forward, hands clasped behind back` |

- **Craft is invariant.** Reuse the exact wording; drift here produces a different production standard, not a different character.
- **Decision is what makes two characters different.** Every decision must pass **The Swap Test (换人测试)**:
  > *"If I transplant this exact decision (iris colour, facial mark, motif seed, posture, or colour relationship) onto another character of the same genre and status, does it still make sense?"*
  - If **yes** (e.g. "she is an aloof sword immortal, so she has ice-blue irises and a tear-mole"), the decision is a **genre cliché**, not a character derivation. Reject it and re-derive from a non-sharable personal fact (daily physical cost, specific wound, occupational habit).
  - If **no** (it breaks immediately on anyone else because it is tied to her specific daily action or conflict), it passes.

## 9. Batch differentiation — the ten axes

A design is not judged alone. The unit that homogenises is the **project**, and no single-character check can see it, because each character passes on its own merits.

**Read the batch ledger before designing, write to it after.** The ledger format is in [records.md](records.md) §8. If there is no ledger, this is the first character: create one.

The **ten axes** below cover all four orthogonal dimensions (Silhouette/Form, Garment System, Face Bone + Surface, and Static Pose):

| # | Axis | Values to distinguish | Mandatory? |
| --- | --- | --- | --- |
| 1 | **Silhouette family** | column / bell / trapeze / cocoon / hourglass / asymmetric ([../atlas/coordinates.md](../atlas/coordinates.md) §2) | **must differ** from every other character |
| 2 | **Key colour family** | bone-white / obsidian / celadon / cinnabar-rust / glacier-grey / earth-jewel / other | **must differ** from every other character |
| 3 | **Gravity topology** | the five in [../atlas/coordinates.md](../atlas/coordinates.md) §3 | must differ from the previous character |
| 4 | **Register + gear** | editorial or glamour, at gear 1–4 | grade the cast; do not resolve all at one value |
| 5 | **Contradiction direction & signal** | directions 1–7, plus the concrete physical signal | the **signal** must always differ; the direction may repeat if the signal and one structural axis differ |
| 6 | **Persona light mode** | the four in [visual.md](visual.md) §8 | must differ from the previous character |
| 7 | **Trim language & raw set** | the one edge treatment shared across edges + which edges stay raw | must differ; two characters banded in narrow silver filigree are one character |
| 8 | **Motif family (3 scales)** | the seed's macro / mid / micro instantiation | must differ |
| 9 | **Face anchor (Bone + Surface)** | the 2–3 pushed bone parameters (§1A) **plus** iris colour/optics and the 0-or-1 surface mark (§1B) | **both bone anchor and iris/mark must differ** from the previous character; see [../engine/02-face-derivation.md](../engine/02-face-derivation.md) |
| 10 | **Orthographic pose vector** | `weight axis · empty-hand action · chin & gaze` ([../engine/01-truth-and-pose.md](../engine/01-truth-and-pose.md) §7) | **at least two of the three components must differ** from every adjacent character |

Rules:

- **Axes 1 and 2 are hard failures.** Two characters sharing a silhouette family or a key colour family must be redesigned, even if everything else differs.
- **Axes 9 (Surface) and 10 (Pose) have sub-rules that never relax:** two characters in one project may not share the same iris colour + facial mark combination, and may not share more than one component of `weight · hands · gaze`.
- **At least six of the ten axes must differ** between any two characters. Axes 1 and 2 count toward that six.
- **"Different colour" means different family, not different name.** Bone-white and pearl-white are one family; cinnabar-rust and oxblood are one family. A name swap is not a variation.
- **Lexical overlap cap:** stripping out the ~111 words of fixed house craft strings, any two character prompts in the same project must have a **non-craft design word Jaccard overlap ≤ 28%** (checked via `scripts/preflight.py --compare-prompt`).
- **Report the vector, don't assert difference.** Name the comparison explicitly against the ledger rows.

### 9A. Same-character variants are exempt from axes 1, 2, and 9 (Bone)

**These ten axes govern different characters. They do not govern a second outfit for one character.** A new costume, hairstyle, or ornament set on an existing character is a **variant**, not a cast member.

A variant is judged on two things:

| Test | Requirement | If it fails |
| --- | --- | --- |
| **Identity integrity** | the identity block is reused **word for word** from the character's record — bone parameters, iris colour, hairline, permanent marks, body ratio, skin finish. No re-derivation. | recast: restore the record's identity block verbatim, discard the derived values |
| **Look separation** | at least **three of four** look factors differ from that character's previous look: `gravity topology · trim language · motif family · node distribution` | the variant reads as the same outfit recoloured; change a look factor, not the identity |

Look factors are the ones the look layer owns per [../engine/01-truth-and-pose.md](../engine/01-truth-and-pose.md) §8 — hair styling, clothing, makeup tint, temporary accessories. Silhouette and key colour are **preserved by default** and may change only when the character's situation has actually changed their status or role, and the change is stated in the blueprint.

- **A variant is not a new ledger row competing with its character.** Record it as a `↳` variant line under its character per [records.md](records.md) §8.
- **Do not re-derive the identity set for a variant.** [../engine/02-face-derivation.md](../engine/02-face-derivation.md) §1A is the procedure for a new character. Running it again for an outfit change generates a different person and calls it a wardrobe update.
- **Ornaments are look, not identity.** A permanent accessory named in the record stays; added pieces are per-outfit. The no-props rule (§4) still holds.
