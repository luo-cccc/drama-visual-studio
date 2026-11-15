# Bank: Material, Restraint, Genre Modules

How light lands, how much is enough, and what each genre expects. This file is a **lookup and diagnosis** bank. Its companion is [form.md](form.md) for silhouette, value, and colour.

The only delivery gate is the preflight in [../pipeline/design.md](../pipeline/design.md) §6. The checks in §4 below find what is wrong; they do not decide whether a design ships.

## 1. Material system

Materials decide how light lands, and therefore how believable the design is.

Three contrasts:

1. **Matte vs sheen vs translucent**: at least two, ideally three.
2. **Heavy vs light**: wool or armour vs organza or gauze.
3. **Structured vs fluid**: tailored shoulder vs bias-cut drape.

**Material is light behaviour.** Every material line should imply one of four:

| Behaviour | What to write | Typical Eastern materials |
| --- | --- | --- |
| **Broad soft specular** | light spreads across a rough surface with no sharp edge | raw silk, hemp, unglazed ceramic, chalk, raw lacquer |
| **Tight specular** | a small hot highlight, a mirror edge | polished bronze, jade, wet obsidian, lacquerware, tempered steel |
| **Translucent** | light passes and scatters, colour behind shows | xuan paper, sheer organza, cicada gauze, thin porcelain, horn |
| **Volumetric** | the material holds air and light inside it | fur, feather down, raw cotton wadding, ash, smoke-dyed gauze |

A design with four materials all in the first row renders as one flat matte mass. At least two behaviours must be present.

**The BJD layer is a fifth quality, not a fifth material.** It is a finish instruction: `jeweller-grade fittings, sculptural surface relief, hand-finished polish on metal and stone`. It appears once per prompt, usually on the hero ornament.

Texture at three scales: **macro** (appliqué, armour plates, sculpted relief), **mid** (jacquard, pleats, quilting, embroidery, lace), **micro** (thread, grain, pores, metallic weave, dust). Use one texture per scale, not five at the same scale. At sheet resolution the micro scale renders in the macro cell.

Material behaviour: specify how the fabric behaves, not just its name — `stiff silk that holds a sculpted shoulder`, `bias-cut satin whose weight pulls it into a pool at the ankle`, `sheer organza floating two centimetres off the skin, edge curling where it is cut`. Weight is the cheapest realism available.

One material surprise: give each main character one material slightly wrong for the genre — silver thorns piercing silk, woven paper in a formal robe, lacquered lace, gold seams in skin. This is the detail that makes the design memorable.

## 2. Composition and restraint

**This section is the editorial budget.** It is not the definition of good taste, and it must not be applied to glamour or ceremonial figures. Restraint is one discipline, not the only one. Register differences are in [../contract/gates.md](../contract/gates.md) §2; density counts in [density.md](density.md).

- **One focal point**: face or chest. Both registers, immutable.
- **One hero node**: the only worn object allowed to compete with the face. Editorial only; glamour may have several peers, with the hair often the hero.
- **One primary open area**: bare skin, plain fabric, or negative space. Both registers. In a rich design this is the safety valve that keeps fifteen nodes from reading as clutter; its size shrinks as density grows.
- **Ornament nodes**: editorial one hero plus at most three supporting — four total. Glamour and ceremonial take the counts in [density.md](density.md) §3.
- **Density gradient**: head > chest > waist > hem; nodes thin out faster than pattern. All registers.
- **Visual path**: face → chest → hands → hem. Place details along this path, not randomly.
- **Remove-one test**: remove one node; if the design still works, leave it removed. Editorial only. The glamour equivalent is the gradient test: does every zone strictly out-density the one below it?
- **Face wins**: no ornament, crown, or garment element should out-shout the face.

## 3. Genre aesthetic modules

Each module gives one possible thesis, silhouette, materials, palette, and clichés to avoid. **No module is the default**, and the order carries no preference. A module's palette is a starting position, not a prescription; the material language is always the house one from §1 and [form.md](form.md) §3A. Where a module lists a colour, read it as the pigment, kept below the face's chroma, and give the dark mass a named temperature bias.

| Module | Thesis | Silhouette and materials | Palette | Avoid |
| --- | --- | --- | --- | --- |
| **Xianxia — Sect-Ranked** | cultivation as a career inside a hierarchy; the robe records which exam you passed | column with closed formal shoulder; layered inner/outer robe, sleeve depth signals rank; starched silk, rank brocade, jade and bone clasps | mineral celadon-white and lampblack + one rank pigment (cinnabar or azurite) where rank is stated; blue-black dark mass | floating ribbons, unwearable sleeve volume, "more layers = more powerful", ornament without rank meaning |
| **Xianxia — Rogue** | no institution behind them, so every possession earns its place | asymmetric column, mismatched layers, travel-worn hem; raw hemp with slub, patched silk over canvas, cracked leather cord | dust ochre, faded indigo, iron rust + one salvaged saturated accent | "wanderer = brown rags", a clean silhouette with one artful stain, mystery-box clutter |
| **Xianxia — Clan-Born** | an inheritance worn on the body; the garment is a claim being defended | hourglass or bell, constructed shoulder, family motif at three scales; heavy patterned silk, woven metal thread, heirloom jade, black pearl | deep celadon, warm bone ivory, antique gold gone brown + one bloodline pigment | "noble = gold everywhere", symmetric hairpins with no meaning, wealth shown by quantity instead of age |
| **Xianxia — Tribulation-Marked** | a body that survived heaven's punishment; sacred ruin, not villainy | asymmetric column, one burned or armoured shoulder, torn train; charred silk with fused edges, storm-grey gauze, lightning-fused metal, gold-leaf scars | low-chroma storm violet, charred black with a warm bias, ash grey + one molten-gold accent at the heat point | "evil = black" without a sacred element, skulls, blood splatter, glowing aura, a clean white robe after a tribulation |
| **Xianxia — Demonic-Path** | a method that costs the body and pays in power; visible exchange, not visible evil | tight column or hourglass, bound construction; dark lacquered silk with a mirror edge, matte blood-thread embroidery, dry porous bone fittings | oxblood at low chroma, warm iron black, bruised plum + one sickly pale accent | "demon = red skin and horns", gratuitous gore, spikes as personality |
| **Xianxia — Beast-Blood** | a humanoid form that barely contains a beast lineage | broad shoulders, clawed hands, heavy lower body; bone, hide, fur with undercoat depth, iridescent scale, horn | blood crimson, ash, bone white + one venom-green accent | cute animal ears, random fur trim, excessive spikes, fur that renders as a solid lump |
| **Xuanhuan — Sect Politics** | power worn as protocol; the garment records a rank, not a taste | structured bell or column with a ranked shoulder; heavy rank-brocade, lacquered leather, cast metal emblems with casting flaws, seal wax | deep green-black, bronze, bone + one ranked vermilion whose amount is the rank | generic "ancient costume", unreadable rank hierarchy, random jade |
| **Xuanhuan — Beast-Tamer** | a body negotiating with something larger than itself | broad inverted triangle, reinforced forearm and thigh, open back; braided hide, horn and claw fittings, oiled canvas | umber, ash, bone + one venom or ember accent | cute animal motifs, random fur trim, losing the human silhouette to the creature |
| **Xuanhuan — Imperial Ascension** | a throne that intends to become a mountain; authority dressed beyond mortal rank | broad inverted triangle or full bell, extended shoulder line, heavy lower mass; gold-woven heavy silk, bronze scales with green-black patina, lacquered armature | black, antique gold, deep cinnabar + one jade accent | "emperor = dragon everywhere", gold on every surface, a silhouette as wide as it is tall |
| **Xuanhuan — Wasteland** | a survivor whose wardrobe is a repair record | asymmetrical column, layered salvage, bound joints; sun-bleached canvas, bone and sinew, mismatched corroded plate, tarred rope, dust | bleached bone, iron rust, ash + one faded indigo accent | clean post-apocalypse cosplay, random straps, "wasteland = brown mush", no visible repair logic |
| **Wuxia** | worn discipline; every garment has a reason to move | fitted column, split hem, forearm guard, narrow boot; weathered linen, hemp, leather, dull steel, bamboo, patched cotton | earth, indigo, rust, faded black + one dull red accent | shiny armour, neon colours, anime spikes, brand-new fabric, excessive belts |
| **Republican / Modern Historical** | tailored restraint under social pressure | qipao column, cheongsam, high collar, narrow shoulder, trench coat; wool with a nap, silk, brocade, tarnished brass, tortoiseshell | ink, tobacco, jade, oxblood, warm ivory | over-embroidered qipao, modern makeup, plastic buttons, fantasy hair |
| **Contemporary Couture** | one architectural idea, executed precisely | hourglass, cocoon, asymmetric; bonded wool, duchesse satin, organza, titanium, lacquer, crystal | monochrome + one saturated accent | random cutouts, logo bags, runway copy, too many trends in one look |
| **Cyber / Neo-Oriental** | tradition cut by technology; one warm human material against cold hardware | cropped jacket, exoskeleton rail, fitted boot, asymmetric panel; technical ripstop, carbon weave, liquid metal, translucent film, celadon jade | glacier grey, celadon, near-black + one cyan or magenta accent | neon everywhere, goggles, circuit tattoos, holographic stickers, excessive cables |
| **Dark Fantasy / Gothic** | sacred beauty with a visible wound | hourglass, corset, cape, train, high collar; velvet with a directional pile, obsidian, tarnished silver, bone, stained lace | oxblood, black, ivory, antique gold + one wound-red accent | skulls everywhere, blood splatter, bat wings, "evil = black" |

## 4. Diagnostic checks

Use these to find what is wrong with a design **before** running the preflight, or to explain a returned image. They are diagnosis, not acceptance: [../pipeline/design.md](../pipeline/design.md) §6 is the only delivery gate, and its per-register tables are authoritative where the two differ.

Answer every question and state what you would change if the answer is bad. A check with only a yes/no and no remedy is not a check.

| # | Check | If it fails | If it passes too easily |
| --- | --- | --- | --- |
| 1 | **Silhouette**: identifiable at 10% size? | change silhouette family or widen the hem/shoulder contrast | if two cast members pass identically, change one |
| 2 | **Value**: clear dark/light/focal hierarchy in grayscale? | increase value separation; move the focal contrast to the face | if everything is high-contrast, lower the hem |
| 3 | **Palette**: one named relationship, one saturated accent, one chromatic anchor that survives desaturation? | name the relationship, delete extra hues, strengthen the anchor | run the token quota and the anchor test — passing visually is not passing by count |
| 4 | **Material**: two contrasts and one surprise? | add a translucent or heavy element | if there are five materials, remove two |
| 5 | **Restraint** (editorial) / **richness** (glamour): does the design meet the budget in §2, or the four density factors in [density.md](density.md) §8? | editorial: delete the weakest node; glamour: add the missing factor, not another node | editorial: four is the ceiling, not a target; glamour: passing without pattern coverage is sparse, not restrained |
| 6 | **Face wins**: is the face the first thing you see? | quieten the loudest competing ornament | if the face wins only because everything else is dull, the design failed differently |
| 7 | **Motif**: can every major element be traced to the seed? | remove the untraceable element | if everything traces but nothing surprises, the seed is too literal |
| 8 | **Remove-one**: did you remove the weakest ornament? | remove it now | if removal changed nothing, the design had no focal point |
| 9 | **Render integrity**: does the prompt name the BJD skin finish, the anime eye design, one material behaviour, and one light direction? | add the missing block and one weight clause | if render tokens outnumber character facts, cut render vocabulary first |
| 10 | **Commercial read**: at thumbnail size, does this look like a product — cover, key art, figure box? | add or strengthen the chromatic anchor; increase silhouette contrast; give the design one iconographic element | if it reads as a product but you cannot say what it is selling, the iconography is generic |

Checks 1–8 catch under-design and over-design; check 9 catches the technically correct prompt with nobody in it; check 10 catches the good design that is not a product.
