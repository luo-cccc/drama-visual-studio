# Gates: Register, Risk, Conflict Order, No-Props, Discipline, Limits

This file holds the cross-cutting constraints that apply in **every** mode and register. A rule appears here once. Other files reference the section number and never restate the text.

## 1. Lock before design

Lock one genre, one subgenre, one risk level, and one register **before** choosing a motif. The lock sets the default palette, materials, silhouette, clichés, and how far the design may deviate.

| Genre | Subgenres (all peers — none is the default) |
| --- | --- |
| Xianxia | Sect-Ranked / Rogue / Clan-Born / Tribulation-Marked / Demonic-Path / Beast-Blood |
| Xuanhuan | Cultivation-sect politics / beast-tamer / imperial-ascension / wasteland |
| Wuxia | Grounded martial / tragic swordsman / sect intrigue |
| Dark Fantasy / Gothic | Sacred ruin / courtly horror / death cult |
| Modern / Contemporary Couture | Noir fixer / corporate / street / service work |
| Sci-fi / Cyber | Neo-oriental / hard-tech / biotech |
| Republican / Modern Historical | 1930s / wartime / old-money / working class |

**No subgenre is the default.** If the brief names only a genre, the subgenre is undetermined: infer it from the story's actual state and say so, or offer two contrasting subgenres in Mode B. The genre modules in [../bank/material.md](../bank/material.md) §3 are listed for lookup, not in order of preference.

Write the lock as one line before any design work:

```text
[genre] / [subgenre] / [pigment family] / [silhouette family] / [gear: risk level] / [register]
```

Example: `Xianxia / Tribulation-Marked / low-chroma storm violet with molten gold and a warm iron-black anchor / asymmetric / gear 3 Avant-garde / editorial`.

Name exactly one silhouette family. Name the palette as pigments, not moods. The lock line is the first line of the blueprint and the first decision of the design.

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
| Contradiction | one from directions 1–6 | Sacred / Dangerous (direction 7): flawless surface plus one lethal signal |
| Ornament nodes | one hero + at most three supporting | no cap, but density must descend: head > chest > waist > hem |
| Hero node | one ornament node, never a prop | hair or a headpiece may be the hero |
| Default palette | avoid moon white / celadon / ink / cinnabar | allowed and preferred; pearl white, silver, moon white, plus one saturated accent |

Glamour's one material obligation: flawlessness is not featurelessness. Damage is absent; BJD surface perfection carries the credibility — porcelain clarity, a controlled specular, sculpted strand clumps, a wet lower lid, a bright secondary eye reflection.

## 3. Risk gear

| Level | Name | What changes | Levers allowed | Use |
| --- | --- | --- | --- | --- |
| **1** | **Polished** | current system; no rule broken; commercial-safe | 0 | IP-safe briefs only |
| **2** | **Signature** | one strong concept, one unexpected material or colour, one proportion exaggeration; still wearable | 2–3 | **default for original characters** |
| **3** | **Avant-garde** | distorted proportion, extreme volume, deconstruction, one "wrong" element; runway/experimental | 3–4 | hero looks, villains, icons |
| **4** | **Surreal / Theatrical** | garment as object, body extension, impossible physics, grotesque or camp | up to 5 | gods, demons, concept pieces |

Choose a level before the motif, together with the genre lock. **Default to Signature.** Polished only when the brief demands commercial safety. Avant-garde and Surreal must still keep the face as the first focal point.

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

The ten levers themselves live in [../bank/boldness.md](../bank/boldness.md) §2.

## 4. No-props rule

Design the person, not their inventory. **No held or carried objects in a character sheet**, in either register: no weapons, artifacts, fans, flutes, lanterns, or floating sigils. Hands stay empty, touch the hair, or hang.

- **Worn ornaments are in scope**: crowns, earrings, hairpins, hair chains, belts, bracelets, collars, veil pins, jewellery. The test is held/carried → out; worn → in.
- **A script-required weapon is designed in the shot prompt**, as a shot-level asset. It is matched to the sheet's palette and motif, and must never occlude the torso or back in the sheet. Say so once in the delivery.
- **If removing the object makes the design collapse, the load was never in the character.** Migrate it into posture, wear, a stain, a bracing stance, or an ornament built into the garment.
- **Ornament attachment is strict on the body and free at the head**: a blade fragment, chain, or plate on a load-bearing part of the garment shows how it is fixed — welded, riveted, cord-bound, or pierced through the fabric. At the crown and shoulders a levitating piece is legal; on a load-bearing garment it is not.
- **Never force a clothing checklist** onto a persona that calls for simplicity, asymmetry, or languid negative space. Density is a tool for the chosen design, not a quota imposed on every character.

| Instead of this | Design this |
| --- | --- |
| a prop grown from the same motif as the outfit | ornaments grown from the seed; the held object is a separate shot asset |
| a weapon held at arm's length | hands empty, touching the hair, or braced on the body |
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

One list, binding in every register and every engine. This is the union of what the individual files previously enforced.

**Empty fluff adjectives:** `gorgeous`, `masterpiece`, `breathtaking`, `stunning`, `very detailed`, `highly detailed`, `beautiful texture`, `ultra detailed`, `8k`.

**Richness requested as an adjective:** `elaborate`, `intricate`, `ornate`, `richly decorated`, `lavishly detailed`. Enumerate layers, edges, nodes, and pattern coverage instead, per [../bank/density.md](../bank/density.md) §6.

**Review vocabulary in the English prompt:** `hero ornament`, `primary open area`, `design thesis`, `aesthetic order`, `gravity topology`, `design evidence`. Translate each into visible description: "hero ornament" becomes the loudest element, "primary open area" becomes the one quiet area, "gravity topology" becomes the density sitting high or low. A model reading "the filigree is the hero ornament" learns nothing about pixels.

**Engine settings dressed as images:** `roughness 0.4`, `metallic 1.0`, `IOR 1.5`, and any shader parameter.

**Structure noise:** bracketed section headers, numeric percentages, comma-spliced lists of three ideas standing in for one design.

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
