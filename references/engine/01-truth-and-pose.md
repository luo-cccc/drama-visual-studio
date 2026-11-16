# Engine 01: Character Truth, Thin-Brief Compiler, and Orthographic Pose

Layer 1 of the derivation stack. Use this file to extract or construct character facts, establish the design thesis, lock the contradiction signal, and derive the **4D orthographic pose vector**.

For a direct GPT Image 2 minor-character sheet, reuse these design decisions and then follow [../pipeline/gpt-sheet.md](../pipeline/gpt-sheet.md). For an existing design, use the character record in [../contract/records.md](../contract/records.md) §1 instead of redesigning.

## 1. Thin-Brief Compiler (Step 0)

When the user supplies a rich script with specific actions, scenes, and conflicts, extract facts directly and skip to §2.

When the user supplies only a **thin brief** (e.g. "design an aloof xianxia elder Sister, glamour, 3-view sheet"), **never fall back to a genre lookup table**. A thin brief is an uncompiled prompt; running it directly forces the model into its training mean. Instead, construct three concrete facts before touching any visual axis, and mark them as `[inferred biography]` in the delivery note:

| Step | Question to force | What it decides downstream | Bad (Cliché) | Good (Physical & Specific) |
| --- | --- | --- | --- | --- |
| **0A. Daily Body Cost** | What repetitive physical action does their duty or survival force their body to perform every single day? | Posture weight, hand state, where cloth wears down or stiffens, periocular fatigue | "She cultivates sword qi" (abstract, un-drawable) | "She spends four hours every dawn kneeling on cold stone to recopy burned sect ledgers with an iron stylus" |
| **0B. Compulsory / Forbidden Object-Class** | What one garment structure is she forced to wear by rank, or strictly forbidden from wearing? | `Invariant` and `Forbidden` in the IFV triple; the motif seed's physical support | "She wears a beautiful white immortal dress" | "She must wear the heavy lead-weighted archive yoke collar even over summer gauze; she is forbidden loose sleeves that would drag in ink" |
| **0C. Single Control Failure** | Where is the one place on her body or hem where her discipline slips? | The contradiction signal (§5), the bottom-right macro micro-expression, or the untreated raw edge | "A crimson tear-mole beneath her eye" (unearned decoration) | "Her right index knuckle is permanently stained grey-black from wiping the stylus, hidden inside a pulled-down cuff" |

## 2. The three questions

Every character design answers three questions, visibly at full-body distance:

1. **How do they live?** Income, work, climate, mobility — shown in fabric weight, fit, wear, and repair.
2. **What do they care about?** One place of obsessive care (immaculate stiffened collar, polished boots, exact pleat) and one place of compromise (frayed cuff, mismatched clasp, salt-stained hem).
3. **What is their current state?** What happened today or this period: rain, sleeplessness, a ritual, an interrogation, a long journey — shown in wrinkles, stains, dampness, loose hair, missing pieces.

The face stays idealized, so damage reads as designed evidence — a scar or stain is a compositional element, not a medical record. Make the evidence physically specific: `a dried salt ring across the lower calf` renders; `a bit dirty` does not.

## 3. Position and the ten dimensions

**Position comes first.** Age band, gender presentation, and class (or *what they command* in glamour) are the three axes a model defaults hardest on: unprompted, it returns a 22-year-old slender aristocrat every time.

| Dimension | What to specify (derive, never copy) | Physical evidence to name |
| --- | --- | --- |
| **1. Position** | age band, gender presentation, class/income (editorial) or specific domain of command (glamour), manual-labour history | e.g., `late 40s, masculine presentation, bonded wharf clerk, soft palms with one brass-scale callus` |
| **2. Face bone (§1A)** | head-to-face index, jaw/chin width, cheekbone height, eye spacing, mouth width, nose bridge/tip | derived strictly from Position via [02-face-derivation.md](02-face-derivation.md) §1A |
| **3. Face surface (§1B)** | iris optics, periocular weight, lip state, specular/matte map, 0-or-1 mark | derived strictly from gaze & speech habits via [02-face-derivation.md](02-face-derivation.md) §1B |
| **4. Hair architecture** | mass, hairline, parting, wear/restraint, one loose strand, inner value interruption | how the hair is bound for their daily action, where strands escape |
| **5. Body & proportion** | head-count band (`7.0–8.5`), anatomical waist vs garment waist-cut, shoulder-waist-hip line | see [03-costume-and-craft.md](03-costume-and-craft.md) §2.1 |
| **6. Orthographic pose** | weight-bearing leg/hip, shoulder-neck line, empty-hand action, chin & gaze | see §7 below; mandatory in blueprint point 1 and ledger axis 10 |
| **7. Life traces / status** | calluses, scars, tan lines, occupational stains, repaired items (editorial 2; glamour 0–1 + status marker) | visible at full-body distance |
| **8. Garment construction** | cut, layers, closures, physical understructure, tucking, raw vs treated edges | how it stays on the body and what supports its volume |
| **9. Worn ornaments** | material × form × mechanical attachment job; hero vs supporting; zero held objects | every node must close, pin, weight, or join two pieces |
| **10. Micro-expression** | bottom-right macro cell only: muscle action + millimetre intensity + what stays still | e.g., `one nostril flares slightly, mouth stays shut, eyes do not move` |

### Cast-wide anti-assembly-line rules (across 5+ characters)

No single-character check catches a cast of five 20-something aristocrats. Across a project of five or more characters:

- **At least one character aged 45+**, written with the lengthened philtrum, settled jaw, temple thinning, and torso weight that age produces.
- **At least one character whose work has marked their hands** — a callus, burn scar, flattened nail, or dye/soot in the skin creases.
- **At least one character wearing a garment they could not have bought new** — issued, inherited, outgrown, salvaged, or mended across decades.
- **At least two distinct head-count bands** across the cast (if heroes sit at `8.5-head`, someone sits at `7.5-head`).
- **In glamour**, replace class/income with **what they command** — and every glamour character must command a different domain (a dead lineage, a furnace monopoly, a border garrison, a debt ledger, a ritual choir). Five glamour characters who all command "noble blood" are one character.

**Visible-distance tiers**: full shot carries silhouette, palette, major garment shapes, and posture; medium carries layers, closures, fabric texture, accessories, wear; close-up carries pore hint, scars, lip texture, iris fibre, double catchlight, and micro-expression. Write only what the target panel can see.

## 4. Translate umbrella adjectives into physical nouns

Adjectives do not point at anything; the model falls back to the average image. If a word can describe ten different images, split it into at least three physical nouns or construction clauses.

| Umbrella word | Split into physical decisions |
| --- | --- |
| `帅气 / 高级感 / 清冷` | facial index, brow-to-eye distance, lip compression, shoulder line, matte vs specular fabric ratio, dark-mass temperature |
| `威严 / 霸气` | squared or extended shoulder yoke, weight planted across both heels, chin lifted 5°, high stiffened collar, low-chroma heavy cloth dragging the hem |
| `破碎感 / 隐忍` | asymmetrical shoulder drop, over-clean mended seam at a stress point, hands hidden or gripping own cuff, lower lids tightened while mouth stays level |
| `有设计感` | named construction: bias-cut overlap, exposed bone-stay, off-centre placket, godet pleat, riveted leather gusset |
| `复古 / 东方感` | exact historical/regional construction: Tang round-collar袍 with under-arm gusset, Ming horse-face deep box pleats, 1930s wide-lapel heavy wool coat |

## 5. Imperfections and the seven contradiction directions

Specificity comes from controlled contradiction, not from adding more ornament.

- **Visible imperfections**: editorial two; glamour zero or one.
- **One deliberate contradiction**, named by direction and concrete **physical signal** in the blueprint:

| Direction | Structural formula | Reads as | Derivation requirement |
| --- | --- | --- | --- |
| **1. Sacred / Desecrated** | ceremonial or high-status construction + one specific environmental/event damage | grief, exile, interrupted rite | name what caused the damage and where it hit the garment |
| **2. Cheap / Exact** | coarse or worn working garment + one obsessively maintained boundary | dignity, bureaucratic or martial discipline | name the one pressed, starched, or polished element |
| **3. Clean / Wrong** | immaculate surface + one physical trace that violates the role's claim | threat, hypocrisy, hidden trade | name the trace (chalk, soot, grease, filings) and why it is there |
| **4. Function / Inversion** | a garment class worn in the wrong state or for the opposite job | paranoia, survival habit, trauma | e.g., plate reinforcement sewn inside sleeping silk |
| **5. New / Unfitting** | brand-new tailoring + wrong scale or one unreplaced old anchor | forced promotion, imposture, mourning | state the centimetre mismatch at collar, cuff, or waist |
| **6. Time / Reversed** | a garment whose repairs are higher-grade or more deliberate than the base cloth | devotion, refusal to let go | name the visible repair material and stitch logic |
| **7. Sacred / Dangerous** | flawless BJD surface + one lethal or inhuman structural signal; zero dirt/wear | untouchable sovereignty, latent violence | **glamour native**; the signal must be derived from their power's cost, never defaulted to "red eyes" |

Two characters in one project should not share a contradiction direction; if two glamour characters both use Direction 7, their **concrete signals** must be completely different objects/phenomena ([../contract/gates.md](../contract/gates.md) §9, axis 5).

## 6. Design thesis

Write one sentence before the prompt. It links the character's conflict to a physical garment structure and material, giving the render a hierarchy.

Formula: **`[Role in conflict] who [daily action / situation] wears [specific construction & material] as [physical evidence].`**

The thesis has two halves: a **situation** the model cannot draw, and a **physical anchor** after the colon that it can. Every thesis must name at least one concrete garment structure and one material light/weight behaviour after the colon.

- Fails (un-drawable metaphor): `a sect leader carrying the weight of a dead mountain.`
- Passes (physically anchored): `a sect leader who still sweeps an empty ancestral hall: a double-layered raw hemp mourning mantle weighted at the hem with unpolished iron tablets.`

## 7. Orthographic pose vector

A character sheet requires **orthographic view alignment** (front, exact 90° side, 180° back on one shared ground line at identical scale). **It does not require a generic mannequin stance.**

Confusing "orthographic view" with "neutral balanced stance" is why every sheet renders with weight on one leg and one arm hanging limp. A character with weight planted forward, shoulders squared, and right thumb hooked into a belt clasp is **100% readable across front, 90° side, and back views**, while immediately reading as a specific person.

Specify all **four components** in blueprint point 1 and write them into the left-panel prompt sentence:

| Component | Options / Spectrum (derive from §1/§2 daily action) |Orthographic constraint |
| --- | --- | --- |
| **1. Weight axis** | locked on left leg with right knee soft / planted evenly across a wide stance / shifted forward onto the balls of the feet / settled back onto the heels / cocked into one hip | both feet stay on the shared ground contact baseline; no jumping or lunging |
| **2. Shoulder-neck line** | strictly level and squared / left or right shoulder dropped 2cm by habit or load / shoulders rolled slightly inward / neck craned slightly forward or drawn back | keep torso front-facing in view 1 so placket and chest construction remain unoccluded |
| **3. Empty-hand action** | one thumb hooked in belt or sash / two fingers adjusting collar or lapel / hands clasped loosely behind the lower back / one hand steadying the opposite cuff / palms open and slightly turned out at the sides / one hand resting high on the sternum or touching a hair ornament | **hands never hold a prop** ([../contract/gates.md](../contract/gates.md) §4) and must not cross over the central chest hero node in the front view |
| **4. Chin & gaze** | chin lifted 5° looking down the nose / chin level with gaze directed off-frame left / chin slightly tucked looking straight through the brow / head tilted 4° toward the low shoulder | keep head within 0–10° of frontal in view 1 so the 90° side profile stays true |

Three reference kinetic modes (starting coordinates, never copy verbatim without customizing the hand action):

- **Poised / Sovereign**: weight settled on the back heels, shoulders strictly level, one hand resting at the belt clasp or sleeve cuff while the other hangs clean, chin level or lifted 3°, gaze direct.
- **Languid / Detached**: weight shifted onto one leg with a soft hip offset, one shoulder slipped slightly lower, hands tucked into opposite sleeves or one touching a collar cord, chin slightly tucked, gaze distant down-left.
- **Guarded / Coiled**: weight forward on the balls of the feet, shoulders squared and tense, one thumb hooked into a harness or belt edge, chin lifted, gaze fixed and unblinking.

**Batch rule ([../contract/gates.md](../contract/gates.md) §9, axis 10):** Any two characters in the same project must differ on **at least two of `weight axis · empty-hand action · chin & gaze`**. Bare `neutral balanced stance` is banned in prompts.

## 8. Identity, look, and state layers

| Layer | Contents | Changes? |
| --- | --- | --- |
| **Identity** | Position triple, head-count band + shoulder-waist-hip, §1A ten bone parameters, §1B iris optics + periocular weight + lip state + specular map + 0/1 permanent mark, hairline and permanent hair structure | **never** (copied verbatim in Mode C and all downstream shots) |
| **Look** | hair styling, clothing layers, understructure, closures, trim language, motif family, temporary makeup tint, worn ornaments | per outfit (Mode C re-derives this layer only) |
| **State** | wet, injured, tired, stained, wind-loosened, recent events | per shot |

## 9. Prompt-ready block scaffolds (zero preset tokens)

### A. Invariant identity block (~65–75 words)

```text
[Age band + gender presentation + class/command read], [head-count band] with [waist-cut height and shoulder-waist-hip line], [derived bone consequences from 02-face-derivation.md §1A], large almond eyes with a defined upper lid line and a clear crease, [derived iris colour/optics from §1B] with radial fibre, a darker limbal ring, a bright secondary reflection and a wet meniscus on the lower lid, [derived periocular weight], a minimal nose bridge with [derived tip/length], [derived mouth width and lip ratio/state] with a visible cupid's bow, [0 or 1 derived permanent mark — omit clause entirely if 0], and smooth porcelain skin with a soft subsurface glow and [derived matte/specular zone]. [Hair mass, hairline, parting, permanent colour/streaks].
```

### B. Look and evidence block (~80–110 words)

```text
Standing with [weight axis], [shoulder-neck line], [empty-hand action], [chin & gaze]. [Editorial: two physical life traces | Glamour: one status marker + direction-7 lethal signal]. [Density 4-clause construction: layers in order with opacity/value contrast and physical support; 60–90% edges in one trim language + named raw edges; descending ornament nodes with mechanical closure jobs; motif family at macro/mid/micro scales]. [Material weight/drape behaviour + one counter-temperature chromatic anchor].
```
