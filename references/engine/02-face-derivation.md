# Engine 02: Face Derivation — Bone Geometry (§1A) & Surface Signifiers (§1B)

Layer 6 derivation engine. The eye hierarchy is the first fixation and the design signature; everything else in a character is ranked behind it.

This file owns **both halves of facial identity**:
- **§1A Bone & Proportion Geometry** (the 10 structural parameters)
- **§1B Facial Surface & Signifiers** (the 5 surface variables: iris optics, periocular weight, lip state, skin specular/matte map, and the single-mark rule)

Read [../atlas/coordinates.md](../atlas/coordinates.md) §1 for the 16 parameter definitions in **eye-width (EW)** units, and [../contract/visual.md](../contract/visual.md) §4–5 for the hard proportion bands and the verbatim house craft strings.

**The invariant rule:** two renders are the same person when the eye design, bone anchors, iris optics, cupid's bow, and hairline match. Those are identity. Everything else is mood, register, or drift.

---

## 1A. Deriving the 10 bone & geometry parameters

**Scope: runs once, for a new character.** Do not run §1A for a costume variant (Mode C); a variant restates the character record's ten values verbatim ([../contract/gates.md](../contract/gates.md) §9A).

**Five steps, in order:**

1. **Take the Position triple** from [01-truth-and-pose.md](01-truth-and-pose.md) §3 — age band, gender presentation, and class or domain of command.
2. **Push the three anchoring parameters off the mean first:** Facial index (13), Mouth width (11), and Inter-canthal distance (1). These three carry the silhouette read at thumbnail size. Two characters whose anchoring three all sit at the midpoint are one face.
3. **Derive the framing parameters** from age and physical history: Philtrum (10), Nose length (9), Chin width (14), Cheekbone (15).
4. **Set the eye geometry pair** — Eye width to face (2) and Iris fill (5) — from how guarded or emotionally legible the character is.
5. **Lock the ten values in blueprint point 7 and check ledger axis 9.** Push two or three parameters decisively; keep the remaining seven inside the neutral band so the face stays harmonious rather than turning into a mask.

### 1A-1. Parameter → character fact mapping

Write the numerical value in the blueprint; write only the **visible consequence** in the English prompt.

| # | Parameter | Decided by (Character Fact) | Direction & Value | Visible consequence for the prompt |
| --- | --- | --- | --- | --- |
| **13** | **Facial index** (length ÷ width) | ratio of bone to soft tissue — age band, hunger, austerity, or physical labour | **Long/narrow (1.48–1.55)**: patrician, ascetic, withheld, older · **Wide/short (1.26–1.33)**: grounded, physical, well-fed, very young | `a long narrow face drawn down through the jaw` / `a broad short face with weight in the lower half` |
| **11** | **Mouth width** (÷ IPD) | whether they speak to command, persuade, or withhold speech | **Narrow (0.74–0.77)**: secretive, severe, compressed · **Wide (0.84–0.88)**: expressive, performative, generous, loud | `a narrow mouth held closed at the corners` / `a wide mobile mouth` |
| **1** | **Inter-canthal** (eye spacing) | how predatory or unguarded their attention is | **Close (< 0.98 EW)**: evaluating, predatory, calculating · **Wide (> 1.18 EW)**: open, naive, protected, or eerie/nonhuman | `close-set eyes under a focused brow` / `widely spaced eyes giving the face an unguarded openness` |
| **2** | **Eye width to face** | formality of presentation and register bandwidth | **Restrained (1.02–1.08×)**: adult, editorial, severe · **Stylized (1.14–1.20×)**: glamour, cover-facing, youthful | `proportionate almond eyes in a formal adult face` / `large luminous eyes taking up a stylized share of the cheek` |
| **5** | **Iris fill** (÷ fissure height) | how much feeling the character allows the viewer to read | **High (0.88–0.95)**: glamour, open, seductive, young · **Guarded (0.74–0.80)**: guarded, cold, sleepless, calculating | `a full iris that nearly fills the lid opening` / `a smaller iris leaving a clear line of sclera` |
| **9** | **Nose length** | age, lineage formality, and profile authority | **Long + defined tip**: mature, aristocratic, commanding · **Short + high tip**: youthful, approachable | `a long straight nose bridge ending in a defined tip` / `a short small nose set high` |
| **10** | **Philtrum** (÷ upper lip) | biological age and vertical poise | **Long (0.58–0.64)**: mature, patrician, unyielding · **Short (0.42–0.48)**: youthful, delicate | `a lengthened philtrum above a level mouth` / `a short philtrum under a small nose` |
| **12** | **Lip ratio** (upper : lower) | structural fullness vs compression | **1 : 1.4**: balanced adult · **1 : 1.7+**: plush glamour · **1 : 1.0**: thin, compressed, severe | `a full lower lip under a crisp upper bow` / `nearly equal thin lips held level` |
| **14** | **Chin width** (÷ mouth) | structural stubbornness vs fragility | **Pointed (0.78–0.82)**: fragile, courtly, sharp · **Broad/square (0.95–1.02)**: immovable, martial, grounded | `a narrow tapered chin` / `a broad square chin and firm jaw angle` |
| **15** | **Cheekbone** | whether bone planes or soft tissue lead the light | **High & flat**: sculptural, severe, operatic · **Low & soft**: gentle, youthful, unformed | `high flat cheekbones cutting a clean shadow plane` / `low soft cheekbones over rounded cheeks` |

---

## 1B. Deriving the 5 facial surface & signifier variables

Bone geometry (§1A) only sets the wireframe. Two characters with different jaw widths who share the same iris colour, eyeshadow, lip finish, and facial mark still read as the same face.

Every character's facial surface is derived across five independent variables from their specific script facts, and audited by **The Swap Test** ([../contract/gates.md](../contract/gates.md) §8).

| # | Variable | Derived from (Script Fact) | Never decided by | Spectrum of physical choices |
| --- | --- | --- | --- | --- |
| **1** | **Iris optics** (hue, value, chroma, internal texture) | **How this person looks at others** — what their gaze does to a room, their environment's light, or the physical cost of their craft | ✗ Archetype label ("aloof = red/ice-blue", "villain = crimson", "immortal = gold") | **Cold/analytic**: slate-grey, tarnished silver-olive, pale celadon-glass, deep ink-indigo · **Warm/enduring**: burnt ochre, smoked amber, raw umber, muted hazel · **High-voltage/costly**: oxidized copper-green, sulfur-gold, blood-agate, milky cataract-white. State both hue and value. |
| **2** | **Periocular weight** (where pigment/shadow sits around the eye) | **Direction of attention & sleep state** — whether they project outward to intimidate/perform, or pull inward to conceal/endure | ✗ Generic "dusty-rose lower-lid eyeshadow" on every character | **Outward projection** (performer/predator): sharp outer-corner extension, darkened lower lash line · **Inward containment** (ascetic/schemer): shadow concentrated in the inner canthus and upper socket crease, bare lower lid · **Physiological trace** (working/sleepless): faint bluish-taupe vascular tint under the inner lower lid, zero cosmetic pigment, wind-flushed outer corner. |
| **3** | **Lip state & finish** | **How they use their mouth** — silent endurance, rapid orders, ritual perfection, outdoor exposure | ✗ Register reflex ("always glossy berry") | **Tool of speech/endurance**: matte muted clay or pale rose-taupe, pressed tight at the corners, one dry vertical crease · **Ceremonial/glamour mask**: deliberate lacquer-red or plum-wine stain concentrated at the inner lip with a sharp glassy centre highlight · **Weathered/unadorned**: natural blood-warmth, chapped lower edge, zero gloss. |
| **4** | **Skin specular & matte map** | **Daily environment & light exposure** — indoor incense/oil, high-altitude wind, forge heat, damp rain | ✗ Uniform unspecified "porcelain" | All characters share the house BJD porcelain base (`smooth porcelain skin with a soft subsurface glow`), but **where the highlight breaks** must differ: `cool matte cheeks with a razor-thin specular line only along the nose bridge` vs `warm sun-flushed cheekbones with a broad soft sheen at the temple` vs `velvet-matte bone planes with a wet highlight only at the lower lid and inner eye corner`. |
| **5** | **Single mark rule** (scars, moles, ritual/occupational marks) | **Default = ZERO.** A mark is added *only* when a specific wound, occupational hazard, or lineage rite in the brief demands it | ✗ **Examples or habit** (`tear-mole` under the eye is banned as a default) | **0 marks (Default)**: clean unbroken facial planes; let bone and gaze carry the character · **1 mark (Earned)**: a faded blade nick across the left brow bone, a heat-blister trace on the jaw, a flaking vermilion ordination dot between the brows, a freckle bridge from high-altitude sun, or a single mole placed somewhere *other* than the last character's. **Hard cap: at most 1 facial mark per character.** |

### 1B-1. Hard rules for facial surface derivation

1. **The Zero-Mark Default:** If you cannot point to a sentence in the brief or Step 0 biography that explains *why* a mole, scar, or forehead mark exists, **the character has zero facial marks**.
2. **No Repeated Iris + Mark Pair:** Across a project ledger ([../contract/records.md](../contract/records.md) §8, axis 9), no two characters may share the same iris colour family, and no two characters may place a facial mark in the same zone (e.g. if Character A has an under-eye mark, under-eye marks are locked out for the rest of the cast).
3. **Pass the Swap Test:** Write one clause in blueprint point 7 explaining why this iris colour and lip state belong to this character's daily life and would fail on another character.

---

## 2. Unbriefed register fallbacks (use ONLY when Position is absent)

When a brief supplies a character concept, **§1A and §1B outrank this table completely**. Use these bands only to check hard register limits or for an unnamed background figure:

| Parameter | Editorial bandwidth | Glamour bandwidth |
| --- | --- | --- |
| Eye width to face | 1.02–1.10× | 1.14–1.20× |
| Iris fill | 0.76–0.85 | 0.88–0.95 |
| Upper lid coverage | 12–22% | 20–30% |
| Canthal tilt | −3° to +4° | +4° to +8° |
| Fissure ratio | 0.40–0.46 | 0.46–0.54 |
| Lip ratio | 1 : 1.0 to 1 : 1.5 | 1 : 1.5 to 1 : 1.8 |
| Facial index | **derive via §1A** (1.26–1.55) | **derive via §1A** (never default to 1.42) |
| Facial marks | 0, or 1–2 occupational/life traces | 0 by default; at most 1 deliberate asymmetry |

---

## 3. Mood dials (what moves per shot or expression cell)

Parameters 3, 4, 6, 7, 8, and 16 in [../atlas/coordinates.md](../atlas/coordinates.md) §1 are **mood dials**, not identity locks. They govern the character's baseline temperament and the **bottom-right macro cell** shift on a sheet, and carry **zero pre-bundled colours**:

| Temperament read | Canthal tension | Upper lid coverage | Brow angle | Lower lid (16) | Mouth tension | Bottom-right macro shift (muscle + mm + still) |
| --- | --- | --- | --- | --- | --- | --- |
| **Withheld / Sovereign** | +4° to +6° | 24% | flat, outer slightly high | full, one specular | level, corners closed | one mouth corner lifts 3mm and settles; lower lids tighten; gaze stays unblinking |
| **Decided / Severe** | +2° | 16% | inner 2° higher | tight, flat | compressed, unglossed | lower lids narrow 2mm; jaw sets; one brow lowers slightly; mouth stays flat |
| **Detached / Exhausted** | −2° | 30% | inner 2° lower | heavy | parted 2mm, relaxed | inner brows lift slightly; lips part on a slow exhale; eyes stay half-lidded |
| **Coiled / Confrontational** | +6° | 8–10% | inner 3° higher | tight, crease visible | one corner pulled up | one mouth corner pulls back; nose bridge tenses slightly; eyes stay locked on camera |
| **Calculating / Analytic** | +5° | 14% | flat, asymmetric | tight | level, matte | chin lifts 4°; lower lids narrow; pupils stay fixed while one brow rises 2mm |
| **Enduring / Burdened** | −4° | 18% | inner 1° lower | fine, dry | pressed shut | one nostril flares slightly; corners of the mouth pull down 1mm; eyes do not move |

---

## 4. Charm mechanics (why a face holds the viewer)

Expense is not charm. Adding more silver hairpins or brighter eyeshadow to a symmetrical face produces a mannequin. What the viewer's eye actually responds to, in priority order:

1. **Bone harmony + one pushed anchor:** Keep seven of the ten §1A parameters near the neutral band, and push two or three anchors decisively. Six extreme features read as a mask.
2. **One alive asymmetry:** Perfect symmetry reads as a render artifact. Spend one asymmetry on the face: `one strand of hair crossing the left brow`, `one mouth corner sitting two millimetres higher`, `a slight 4-degree head tilt toward the lower shoulder`, or `one askew temple pin`.
3. **Gaze engagement:** Direct gaze with slight lower-lid tension reads warm and present; direct gaze with level lids reads cold and appraising; gaze down-left reads guarded or reflective.
4. **The catchlight pair (non-negotiable craft):** Two reflections inside every iris — upper key brighter, lower fill dimmer, plus a wet lower meniscus. One catchlight reads dead; three reads glass.
5. **The matte/specular contrast (§1B-4):** Subsurface porcelain glow needs **one explicit matte zone** (usually the cheek plane) so the specular highlight on the nose bridge, lower lid, or lip reads as sculpted form rather than mobile-game oil.
6. **Dimorphism calibration:** Keep adult faces around 60–65% stylized dimorphism — enough brow bone and jaw structure to avoid an infantile chibi read, enough plane refinement to hold the anime pillar.

---

## 5. Gaze, turn, and tilt coordinates

In a 2×2 bust grid, the top-left cell is locked to a symmetrical front neutral baseline, so the **top-right cell** carries the character's charm through this three-part combination:

| Axis | Setting | Emotional read |
| --- | --- | --- |
| **Gaze** | level, direct | present, challenging |
| | level, slightly down through lashes | appraisal, sovereignty |
| | down-left | memory, withholding |
| | over the shoulder | departure, invitation |
| **Turn** | full front (top-left cell only) | clinical baseline |
| | 15–30° three-quarter (top-right cell) | dimensional, flattering |
| | 45°+ | guarded, kinetic |
| **Tilt** | level | formal, immovable |
| | 3–6° toward low shoulder | curious, approachable |
| | away from low shoulder | resistant, cold |
