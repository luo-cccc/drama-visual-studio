# Atlas: Orthogonal Coordinates — Face, Silhouette, Topology, Framing

This file provides **coordinate systems only** — it answers "what are the axes and where am I on them", never "what should I pick".

Do not open this file to shop for a concept. Derive the character's truth, pose, face facts, and motif seed in `engine/01`–`03` first, then use these coordinates to locate and calibrate the result.

---

## 1. The 16 Face Parameters (in Eye-Width units)

Use **eye width (EW)** — the width of one open palpebral fissure — as the scale-invariant unit for every face measurement. Do not write numeric measurements into the English prompt; write the visible consequence per [../engine/02-face-derivation.md](../engine/02-face-derivation.md) §1A.

| # | Parameter | Role | Measured as | Neutral band | Reads beyond the band |
| --- | --- | --- | --- | --- | --- |
| 1 | **Inter-canthal distance** | **Identity (Anchor)** | inner corner to inner corner | 1.0–1.15 EW | < 0.98: intense, predatory, close-set · > 1.20: open, naive, or eerie |
| 2 | **Eye width to face width** | **Identity** | one eye ÷ face width at cheekbone | 1.05–1.20× stylized | > 1.30: chibi drift · < 0.95: small-eyed realism |
| 3 | **Fissure ratio** | Mood | eye height ÷ eye width | 0.42–0.48 | > 0.54: round, doe, unguarded · < 0.36: narrow, slit, cold |
| 4 | **Canthal tilt** | Mood | inner→outer canthus angle | 0° to +3° | +5° to +8°: sharp, feline, dangerous · −2° to −6°: heavy, mournful, enduring |
| 5 | **Iris fill** | **Identity** | iris diameter ÷ fissure height | 0.76–0.85 | 0.88–0.95: full glamour iris · < 0.74 with sclera: sanpaku, unsettling |
| 6 | **Upper lid coverage** | Mood | % of iris top covered by lid | 12–20% | 24–32%: heavy-lidded, languid · < 10%: wide-eyed, coiled |
| 7 | **Brow–eye distance** | Mood | brow base to upper lid | 0.50–0.70 EW | Tighter: intense, compressed, severe · Wider: open, spacious, patrician |
| 8 | **Brow angle** | Mood | inner end vs outer end height | near-flat, outer +1–2° | Inner lower: burdened, gentle · Inner higher: imperious, confrontational |
| 9 | **Nose length** | **Identity** | bridge to tip ÷ face length | ~1/3, minimal bridge | Longer + defined tip: mature, aristocratic · Shorter + high tip: youthful |
| 10 | **Philtrum** | **Identity** | ÷ upper lip height | 0.48–0.58 | > 0.60: mature, austere, patrician · < 0.45: youthful, delicate |
| 11 | **Mouth width** | **Identity (Anchor)** | ÷ interpupillary distance | 0.76–0.84 | < 0.76: restrained, secretive, severe · > 0.85: expressive, performative |
| 12 | **Lip ratio** | **Identity** | upper ÷ lower | 1 : 1.4–1.6 | 1 : 1.7+: plush glamour · 1 : 1.0: thin, compressed, unyielding |
| 13 | **Facial index** | **Identity (Anchor)** | face length ÷ face width | 1.35–1.45 | > 1.48: long, narrow, ascetic, patrician · < 1.32: broad, short, grounded |
| 14 | **Chin width** | **Identity** | ÷ mouth width | 0.82–0.96 | < 0.82: pointed, fragile · ≥ 0.96: square, broad, immovable |
| 15 | **Cheekbone** | **Identity** | height and forward projection | mid-height, restrained | High & flat: sculptural, operatic · Low & soft: rounded, gentle |
| 16 | **Lower lid fullness** | Mood | aegyo-sal / orbicularis volume | 2–4 mm | Tight/flat: cool, aloof, sharp · Full: youthful, gentle, alluring |

- **Identity parameters (1, 2, 5, 9, 10, 11, 12, 13, 14, 15):** derived once per character via [../engine/02-face-derivation.md](../engine/02-face-derivation.md) §1A, locked in the record, never varied across outfits.
- **Mood parameters (3, 4, 6, 7, 8, 16):** adjusted per shot or per 2×2 bust cell via [../engine/02-face-derivation.md](../engine/02-face-derivation.md) §3.

---

## 2. The 6 Silhouette Families (Ledger Axis 1)

At full-body thumbnail size (10%), the viewer reads outline before any fabric or ornament. Silhouette family ([../contract/gates.md](../contract/gates.md) §9, axis 1) is a **hard batch constraint**: no two characters in the same project may share a family.

| Family | Structural outline | Kinetic / psychological read | Counter-shape needed |
| --- | --- | --- | --- |
| **Column** | narrow, vertical, unbroken from shoulder to ankle/floor | austere, disciplined, self-contained, unyielding | one sharp horizontal break (belt bar, stiff yoke, or split hem) so it does not read as a tube |
| **Bell / A-line** | fitted upper torso expanding from waist or hip into a wide lower base | anchored, ceremonial, territorial, formal | a narrow shoulder or high collar so the triangle has a clear apex |
| **Trapeze** | narrow shoulders expanding outward continuously from collarbone or bust to hem | unstable, theatrical, expansive, untethered | exposed tight calves/boots or narrow wrists emerging from the wide base |
| **Cocoon** | rounded outer shell, draped through the midsection, tapering or pooling at the hem | languid, aloof, mysterious, untethered | one sharp structural anchor (sculpted collar, waist-jade, or exposed collarbone/forearm) |
| **Hourglass / X** | wide or constructed shoulder line, hard waist suppression, flared hip or skirt | high-tension, controlled, sculptural, couture | deliberate asymmetry in placket or hem to prevent mannequin stiffness |
| **Asymmetric** | radical left-right or diagonal outline difference (e.g. one side floor-length, one side cropped at thigh/hip) | unresolved, dangerous, fractured, kinetic | one calm continuous vertical axis (spine or standing leg) to keep the figure grounded |

**Shape grammar:** pair one dominant shape language (**vertical/elongated**, **horizontal/grounded**, **angular/sharp**, or **round/soft**) with one smaller contrast shape.

---

## 3. The 5 Gravity Topologies & Back-View Resolution (Ledger Axis 3)

Silhouette (§2) governs the outer contour; **gravity topology** governs where internal detail and weight concentrate, and how the **back view** resolves the front's tension. The two axes are completely independent: a `Column` silhouette can use `Single-Side Mutation`, and an `Asymmetric` silhouette can use `Top-Peak Cascade`.

| # | Topology | Front distribution rule | Back-view resolution (mandatory in 3-view sheets) |
| --- | --- | --- | --- |
| **1** | **Top-Peak Cascade** | ~80% of ornament and layer complexity sits at crown, hair, collar, and shoulders; clean vertical lines below the chest | high-collared yoke or cascading hair/chains pouring down an austere, unbroken back panel |
| **2** | **Bottom-Anchored Weight** | upper body stark, wrapped, or cropped; heavy drapery, armour plates, or pleated volume concentrated from hips to floor | clean or exposed upper back dropping into a massive rear waist-girdle, bustle armature, or multi-tiered train |
| **3** | **Single-Side Mutation** | strict left-right division: one half tailored and quiet, the other overtaken by structural hardware, layers, or the motif seed | bold diagonal seam, half-cape, or asymmetrical harness crossing from one shoulder to the opposite hip |
| **4** | **Languid & Uncinched Negative Space** | zero corsetry or tight waist cinch; loose, heavy drapery hanging from one or two pinning points with generous open cloth | billowing uncinched back folds hanging from the shoulder blades, gathered only at one low off-centre knot or strap |
| **5** | **Bone-Sculpted Tension** | strict high-tension enclosure (high collar, suppressed waist, long leg line) interrupted by a structural cutout spanned by hardware | continuous vertical spinal axis (linked clasps, boning seam, or chain) running from nape to rear split hem |

Rules:

- **Never distribute detail evenly.** Even top-to-bottom complexity turns into wallpaper.
- **Glamour trap warning:** Glamour defaults reflexively to Topology 1 (`Top-Peak Cascade`). In a multi-character project, axis 3 must move across the cast — use Topologies 2, 3, 4, or 5 while keeping the face and hair as the primary fixation.

---

## 4. Canvas & Framing Coordinate System

Aspect ratio decides how much of the figure the viewer sees, where the focal point can live, and whether the image survives its target interface.

### 4.1 Choose canvas by use, never by habit

| Canvas | Ratio | Primary use |
| --- | --- | --- |
| **Vertical narrative** | `9:16` | short drama, manhua drama, vertical mobile drama, phone-first key art |
| **Portrait** | `3:4` | character half-body portrait, intro card |
| **Widescreen** | `16:9` | scene base, cinematic key art, multi-character staging |
| **Sheets** | `16:9` (or `3:2` + `1:1` split) | 7-panel identity/costume sheet ([../contract/visual.md](../contract/visual.md) §10) |

**Never crop a 16:9 sheet into a 9:16 shot.** A sheet is an orthographic specification document; a first frame is a narrative camera shot.

### 4.2 Vertical 9:16 composition bands & safe areas

Vertical frames scan in a single downward pass:

| Vertical band | Frame height | What belongs here |
| --- | --- | --- |
| **Top band** | 10–35% (keep top 8–10% clear of title UI) | the face, headpiece, and primary expression — **face must sit in the upper third** |
| **Middle band** | 35–75% | chest ornament, empty-hand gesture, silhouette turning point, any required signage |
| **Bottom band** | 75–100% (keep bottom 12–15% caption-safe) | quiet hem, boots, ground contact shadow — **never place the hero ornament below 78%** |

Figure occupancy in 9:16:
- **Full figure**: 70–80% of frame height (`full body, head in the upper third, feet clear of the lower caption zone`). Turn the figure 15–30° or place slightly off-centre so it does not read as a passport photo.
- **Cowboy / mid**: head to mid-thigh, 55–65% of height.
- **Bust**: head and shoulders, 40–50% of height, placed in the upper half.

Vertical scene plates:
- **Horizon** sits in the **lower third** (a centred horizon cuts a vertical frame in half).
- **Leading lines** run vertically (stairs, narrow streets, waterfalls, pillars, hanging banners).
- **Information budget**: one focal point + one supporting element maximum.

### 4.3 Widescreen 16:9 & Portrait 3:4

- **Widescreen 16:9 (Scene plates):** Place single figures on the left or right third, never dead-centre, and let environment read on both sides. Ideal for two-character staging and horizontal breadth.
- **Portrait 3:4:** Frame head to waist (cut at the waist, not the hip joint), slight 15–30° three-quarter turn, leaving ~1 head-height of breathing space above the crown against a simple value-separated background.

### 4.4 Sequence consistency & framing diagnostics

- Lock one canvas ratio per shot type across a production.
- Do not inherit `--ar 3:4` into a scene prompt merely because a 3:4 portrait was attached as an identity reference.
- If a 16:9 seven-panel sheet renders the eyes too soft, **use the 3:2 + 1:1 split protocol** ([../contract/visual.md](../contract/visual.md) §10) rather than adding more detail words.
