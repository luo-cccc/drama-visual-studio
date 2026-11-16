# Engine 02: Face Derivation — High-Aesthetic Bone (§1A) & Surface Signifiers (§1B)

Layer 6 derivation engine. The eye hierarchy is the first fixation and the design signature; everything else in a character is ranked behind it.

**Core aesthetic law:** Every character's face must be derived **inside the high-appeal commercial animation & BJD beauty zone** (refined bone planes, luminous eyes, flawless porcelain skin). Differentiating a cast means separating them across **distinct beauty archetypes** (清冷谪仙 / 昳丽妖孽 / 威严冷峻 / 少年英气 / 柔美破碎) — **never** by making a face ugly, old-looking, weathered, or chapped.

Read [../atlas/coordinates.md](../atlas/coordinates.md) §1 for the 16 parameter definitions in **eye-width (EW)** units, and [../contract/visual.md](../contract/visual.md) §4–5 for the verbatim house craft strings.

---

## 1A. Deriving the 10 bone & geometry parameters (Inside the Beauty Band)

**Scope: runs once, for a new character.** Do not run §1A for a costume variant (Mode C); a variant restates the character record's ten values verbatim ([../contract/gates.md](../contract/gates.md) §9A).

**Five steps, in order:**

1. **Take the Position & Charisma Archetype** from [01-truth-and-pose.md](01-truth-and-pose.md) §3 (Aloof Celestial, Alluring Abyssal, Sovereign Imperious, Razor Youth, or Gentle/Fragile).
2. **Push the three anchoring parameters to distinct points in the beauty band:** Facial index (13), Mouth width (11), and Inter-canthal distance (1). These three separate faces at thumbnail size while keeping every face attractive.
3. **Set the profile and jaw framing parameters:** Nose length (9), Philtrum (10 — keep in the youthful/idealized `0.44–0.54` band unless designing an elderly master), Chin width (14), Cheekbone (15).
4. **Set the eye geometry pair:** Eye width to face (2) and Iris fill (5).
5. **Lock the ten values in blueprint point 7 and check ledger axis 9.**

### 1A-1. Parameter → High-Aesthetic Charisma Mapping

Write the numerical value in the blueprint; write only the **visible consequence** in the English prompt.

| # | Parameter | Decided by (Charisma & Temperament) | High-Aesthetic Spectrum | Visible consequence for the prompt |
| --- | --- | --- | --- | --- |
| **13** | **Facial index** (length ÷ width) | aloof elegance vs youthful approachability | **Slender V-tapered (1.44–1.50)**: aloof immortal, seductive demon, sovereign elder · **Compact heart/oval (1.32–1.38)**: youthful prodigy, gentle noble | `a slender tapered oval face with a refined jawline` / `a compact heart-shaped face with soft cheek contours` |
| **11** | **Mouth width** (÷ IPD) | cold restraint vs dangerous or warm expressiveness | **Delicate/restrained (0.75–0.78)**: cold, unspoken, stoic · **Defined/expressive (0.82–0.85)**: alluring half-smile, commanding, charismatic | `a delicately proportioned mouth held in cool restraint` / `a clearly defined expressive mouth` |
| **1** | **Inter-canthal** (eye spacing) | sharp focus vs ethereal openness | **Focused (0.96–1.02 EW)**: sharp, calculating, intense劍意/魔气 · **Spacious (1.10–1.18 EW)**: ethereal, divine, innocent, or dreamlike | `sharply focused almond eyes` / `widely spaced luminous eyes with an ethereal openness` |
| **2** | **Eye width to face** | mature elegance vs high-stylized glamour | **Refined adult (1.06–1.12×)**: noble, martial, sovereign · **High-glamour (1.14–1.20×)**: cover-art heroine, enchanting spirit | `proportionate sculpted almond eyes` / `large luminous eyes commanding the facial proportions` |
| **5** | **Iris fill** (÷ fissure height) | emotional warmth vs chilling dominance | **Full & luminous (0.86–0.94)**: desirable, expressive, radiant · **Poised/appraising (0.78–0.83)**: cool, unreadable, high-status | `a full jewel-like iris nearly filling the lid opening` / `a poised iris framed by clean sclera for an appraising gaze` |
| **9** | **Nose length** | regal profile vs delicate youth | **Straight sculpted bridge**: regal, aloof, sharp profile · **Delicate upturned tip**: youthful, charming | `a straight delicate nose bridge ending in a sculpted tip` / `a small refined nose with a softly lifted tip` |
| **10** | **Philtrum** (÷ upper lip) | keep idealized (`0.44–0.54`) for all young/prime characters | **Short & crisp (0.44–0.48)**: youthful, plush · **Balanced (0.50–0.54)**: poised, noble (only push > 0.58 for 50+ elders) | `a short crisp philtrum above a sculpted upper lip` / `a balanced poised philtrum` |
| **12** | **Lip ratio** (upper : lower) | sensual fullness vs cool composure | **1 : 1.6–1.8**: plush, alluring, glamour · **1 : 1.3–1.4**: balanced, noble, clean | `a plush lower lip beneath a crisp M-shaped cupid's bow` / `cleanly sculpted lips in balanced proportion` |
| **14** | **Chin width** (÷ mouth) | sharp V-line vs firm sword-like resolve | **Tapered V-chin (0.80–0.84)**: ethereal, fox-like, delicate · **Chiseled/firm (0.88–0.94)**: resolute, martial, commanding | `a delicately tapered V-shaped chin` / `a cleanly chiseled resolute chin and jawline` |
| **15** | **Cheekbone** | sculpted light-catching planes vs soft silk smoothness | **High & sculpted**: catches a dramatic rim highlight, alluring/imperious · **Smooth & gentle**: soft diffused transition | `high sculpted cheekbones catching a clean rim highlight` / `smoothly contoured cheeks with a gentle light transition` |

---

## 1B. Deriving the 5 Facial Surface & Signifier Variables (High-Aesthetic Styling)

Bone geometry (§1A) sets the structure; **§1B sets the colour, optical depth, and仙/魔 aura of the face**. Every character's surface variables must be derived from their **Dao, cultivation element, and temperament**, and must pass **The Swap Test** ([../contract/gates.md](../contract/gates.md) §8).

| # | Variable | Derived from (Dao, Element & Gaze) | Never decided by | High-Aesthetic Spectrum of Choices |
| --- | --- | --- | --- | --- |
| **1** | **Iris gem-optics** (hue, value, internal gradient) | **Their Dao, spiritual root, or how their gaze dominates a scene** | ✗ Unthinking default or ugly muddy browns | **Abyssal / Demonic**: deep blood-agate (`#7A1224`) with molten-gold core, phantom wisteria-violet, obsidian-ink with a silver ring · **Celestial / Sword**: frost-celadon glass, starlight silver-grey, clear amber-gold, deep azurite-blue · **Inhuman / Beast**: vertical slit molten-gold, heterochromatic ice-and-ember. Always write as **translucent gem/glass optics**. |
| **2** | **Periocular & eye-corner styling** (眼尾与眼妆张力) | **How they project allure, lethality, or purity** | ✗ Ugly tired eye-bags, or pasting the exact same dusty-rose shadow on everyone | **Lethal / Seductive (昳丽/魔道)**: razor-sharp winged outer liner swept upward with a faint smudge of cinnabar or dark-gold at the outer canthus · **Aloof / Pure (清冷/仙门)**: clean unadorned ivory upper lids with long frosty or ink-black lashes and a cool shadow in the socket crease · **Imperious / Dark (威严/深邃)**: smoky obsidian-taupe contouring along the upper crease and outer lower lash line. |
| **3** | **Lip tint & finish** (唇色与质感) | **Their temperament — cold restraint vs dangerous allure** | ✗ Ugly chapped/cracked/peeling lips | **Cool / Stoic (禁欲/清冷)**: soft velvet-matte pale rose-taupe or natural blossom tint, clean edges · **Alluring / Sovereign (昳丽/高定)**: gradient plum-wine, deep cinnabar, or berry-red stain with a glassy, hydrated highlight at the centre of the lower lip. |
| **4** | **Porcelain specular & matte map** (瓷肌高光切面) | **Lighting atmosphere & character temperature** | ✗ Greasy sweat sheen or flat sticker matte | All characters share `smooth porcelain skin with a soft subsurface glow`, differentiated by highlight placement: `velvet-matte cheek planes with a razor-sharp specular line along the nose bridge and lower lip` vs `luminous pearl-sheen across the high cheekbones and brow bone with matte jaw contours`. |
| **5** | **Single Dao / Aesthetic Mark** (唯一仙魔/美学印记) | **Default = ZERO.** Added *only* when their bloodline, cultivation art, or fate calls for one iconic mark | ✗ Copying an under-eye `tear-mole` onto every character | **0 marks (Default)**: pure, unbroken BJD porcelain planes · **1 mark (Iconic & Earned, max 1)**: a slender dark-gold sword/lotus sigil between the brows (眉心花钿/法印), a faint vermilion demon-pattern trailing from one outer eye corner, frost-crystalline lashes, or a fine silver scar line at the jaw angle. **No two characters in a project may share the same mark zone.** |

---

## 2. Register Bandwidths (Both High-Aesthetic)

Both `editorial` and `glamour` produce **attractive, commercial-grade faces**. The difference is stylization intensity, never attractiveness:

| Parameter | Editorial (Narrative / Concept Bible) | Glamour (Cover / Key Art / Awakening) |
| --- | --- | --- |
| Eye width to face | 1.06–1.12× | 1.14–1.20× |
| Iris fill | 0.78–0.86 | 0.88–0.95 |
| Upper lid coverage | 14–22% | 20–30% (feline / alluring) |
| Canthal tilt | 0° to +5° (or −2° for fragile tragic beauty) | +5° to +8° |
| Lip ratio | 1 : 1.3 to 1 : 1.5 (velvet-matte or soft satin) | 1 : 1.6 to 1 : 1.8 with a glassy centre highlight |
| Facial index | derive via §1A (`1.32–1.50`) | derive via §1A (`1.34–1.50`) |

---

## 3. Mood dials (2×2 bust grid & bottom-right macro shift)

Parameters 3, 4, 6, 7, 8, and 16 in [../atlas/coordinates.md](../atlas/coordinates.md) §1 govern expression shifts across the 2×2 bust cells:

| Charisma Read | Canthal tension | Upper lid coverage | Brow angle | Mouth tension | Bottom-right macro shift (muscle + mm + still) |
| --- | --- | --- | --- | --- | --- |
| **Aloof / Untouchable (清冷睥睨)** | +5° | 24% | flat, outer slightly high | level, composed | lower lids tighten 2mm; chin lifts slightly; gaze stays cool and unblinking |
| **Alluring / Dangerous (邪魅似笑非笑)** | +7° | 28% | arched, outer high | one corner subtly curved | one mouth corner lifts 3mm into a cold half-smile; lower lids narrow; eyes lock on camera |
| **Sovereign / Ruthless (威严裁决)** | +3° | 16% | inner 2° higher | flat, unyielding | lower lids narrow; jaw sets cleanly; one brow lowers 2mm; mouth stays level |
| **Languid / Poetic (慵懒倦怠)** | −2° | 30% | soft, inner slightly low | parted 2mm | inner brows lift slightly; lips part two millimetres on a quiet breath; eyes stay half-lidded |
| **Razor / Martial (凌厉剑意)** | +6° | 10% | sharp, upward-slanted | firm, corners set | pupils contract slightly; upper lid opens sharp; one brow rises 2mm in challenge |

---

## 4. Charm mechanics (Why the face wins first fixation)

1. **Bone harmony + one signature eye design:** Harmonious, idealized facial planes so the viewer's eye locks immediately onto the jewel-like irises.
2. **One alive asymmetry:** `one loose silk-fine hair strand crossing the brow or cheek`, `a 3mm asymmetrical half-smile`, `a 4-degree head tilt`, or `an asymmetrical ear-chain drop`.
3. **The catchlight pair (non-negotiable):** Two reflections inside every iris — a bright upper key reflection and a softer lower fill reflection, plus a wet lower meniscus.
4. **Porcelain subsurface + matte/specular contrast:** `smooth porcelain skin with a soft subsurface glow`, keeping the cheek plane velvet-matte so the nose-bridge and lip highlights pop like hand-finished BJD resin.

---

## 5. Gaze, turn, and tilt coordinates (Top-right 2×2 cell)

| Axis | Setting | Aesthetic Read |
| --- | --- | --- |
| **Gaze** | level, direct | commanding, present |
| | downward through half-lowered lashes | sovereign appraisal, dangerous allure |
| | sidelong over the cheek | mysterious, calculating |
| **Turn** | 15–30° three-quarter (top-right cell) | dimensional, most flattering bone contour |
| **Tilt** | 3–6° toward low shoulder | effortless grace, teasing or curious |
| | level or drawn back | untouchable authority |
