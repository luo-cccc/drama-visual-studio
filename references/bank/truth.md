# Bank: Character Truth

Layer 1 of the design stack. Use this file for a character concept, a portrait, or the character-truth layer of a design sheet.

For a direct GPT Image 2 minor-character sheet, reuse these design decisions and then follow [../pipeline/gpt-sheet.md](../pipeline/gpt-sheet.md); the portrait composition and Midjourney parameters here do not apply to that sheet. For an existing design, use the character record in [../contract/records.md](../contract/records.md) §1 instead of redesigning.

## 1. Design decisions

- Derive hairstyle, hair colour, facial features, costume, accessories, silhouette, and a coherent palette from the character's identity and world.
- Make the design recognizable through one or two strong visual motifs. Keep costume construction plausible and consistent with the role.
- For adult characters, use mature natural facial proportions; do not make them childlike.
- For fantasy characters, make racial traits readable: ears, tail, horns, wings, markings, or nonhuman eyes.
- Do not add random props, unrelated companion characters, or decorative clutter. Props are shot-level assets; a character sheet stays prop-free per [../contract/gates.md](../contract/gates.md) §4.

## 2. The three questions

Every costume answers three questions, visibly at full-body distance:

1. **How do they live?** Income, work, climate, mobility — shown in fabric, fit, wear, and repair.
2. **What do they care about?** One place of care (immaculate collar, polished boots, exact pleat) and one place of compromise (frayed cuff, mismatched button, scuffed heel).
3. **What is their current state?** What happened today or this period: rain, sleeplessness, a fight, a ceremony, a long journey — shown in wrinkles, stains, dampness, loose hair, missing pieces.

Bad: an office worker after a sleepless night in a crisp shirt — that is an ad, not a person. Good: the same shirt with a coffee stain, a loosened tie, one button done wrong, and a jacket carried over the arm.

The face stays idealized, so damage reads as designed damage — a scar is a design element, not a medical record. Make the evidence physically specific: `a mud splash across the left calf` renders; `a bit dirty` does not.

## 3. The ten dimensions

Write one chosen formulation plus one alternative for each dimension. Every line must be a visible noun or action.

| Dimension | What to specify | Example tokens |
| --- | --- | --- |
| **Position** | age band, gender presentation, class/income, whether the body has done manual work | `late 40s, masculine presentation, owned-class clerk, soft hands with one ink callus` |
| **Face and features** | bone structure, eye shape/colour, brows, nose, lips, skin texture, marks | `narrow long face, low cheekbones, phoenix eyes with pale-gold irises, thin cool lips, faint silver scar on the right jaw` |
| **Hair** | mass, hairline, styling, wear, one loose strand | `waist-length blue-black hair, high hairline, loose centre part, one strand crossing the left brow, silver inner streaks` |
| **Body and posture** | head proportion, shoulder-waist-hip, weight distribution, shoulder line, hands, gaze, chin | `8.5-head, narrow shoulders, long waist, weight on the left leg, right hand loose at the side, chin level, gaze down-left` |
| **Life traces** | calluses, scars, tan lines, ink stains, occupational wear, repaired items | `ink-stained fingertips, a burn scar across the right knuckles, a frayed sash` |
| **Clothing construction** | cut, fabric, layers, closures, fit, tucking, distressing | `double-breasted charcoal wool coat, waist suppressed two centimetres, one cufflink missing, left sleeve pushed to the forearm` |
| **Worn accessories** | material × form × wearing method; hero vs supporting; no held objects | `single black pearl on an oxidized silver chain at the open collar; one geometric ear cuff` |
| **Micro-expression** | muscle action + intensity + what stays still | `lower lids tighten, one mouth corner lifts three millimetres and settles, chin dips five degrees, eyes relaxed` |
| **Habit and gesture** | what the hands do, how they stand, how they wear the garment | `thumb hooked in the pocket, shoulders slightly uneven, sleeve pulled over the fingers` |
| **State** | fatigue, injury, weather, recent events | `wet hem, raw fingertips, hair loosened by wind, one glove lost` |

**Position comes first.** Age, gender presentation, and class are the three axes a model defaults hardest on: unprompted, it returns a young, slender, high-status figure regardless of the brief. Specify Position for every character, including the ones the brief does not mention, and vary it deliberately across a cast.

Register exception — glamour: the class axis usually collapses to "high". Replace class/income with **what they command** — a title, a lineage, a rank, or a power — written as a visible status marker. Manual-labour traces belong in editorial sheets. Register definitions are in [../contract/gates.md](../contract/gates.md) §2.

**Visible-distance tiers**: full shot carries silhouette, palette, major garment shapes, and posture; medium carries layers, closures, fabric texture, accessories, wear; close-up carries pore hint, scars, lip texture, iris fibre, double catchlight, and micro-expression. Write only what the target panel can see.

## 4. Adjectives to nouns

Adjectives do not point at anything; the model falls back to the average image. One professional noun carries more information than a string of adjectives.

| Umbrella word | Split into |
| --- | --- |
| `帅气 / 高级感 / 清冷` | face bone structure, brow angle, eye shape, lip tension, posture, fabric, palette |
| `轻佻` | centre-parted curtain hair, one strand over the brow, open collar, one hand in the pocket, weight on one leg, gaze sliding sideways |
| `温柔` | soft inner brow corners, relaxed lower lids, level mouth corners, rounded shoulder line, low-contrast oatmeal/ivory palette, soft knit texture |
| `有设计感` | named construction: asymmetric lapel, bias-cut panel, exposed seam, godet hem, sculpted shoulder |
| `五官精致` | narrow nose bridge, defined philtrum, upper-lip bow, lower-lid support, clear jawline |
| `复古` | decade + garment archetype + fabric + closure: 1930s bias-cut satin slip, 1970s wide-lapel wool coat, 1990s minimal column dress |
| `电影感 / 次世代感` | a named key direction, a named material light behaviour, a named depth cue |

Rule: if a word can describe ten different images, split it into at least three dimensions. Style words are adjectives too: `cinematic`, `game CG`, `BJD`, `anime`, and `8k` describe a production standard, not this character.

## 5. Imperfections and one contradiction

Specificity comes from controlled imperfection, not from adding more ornament.

- **Visible imperfections**: editorial two; glamour zero or one.
- **One deliberate contradiction**, named from the seven directions below.

| Direction | Formula | Reads as | Example |
| --- | --- | --- | --- |
| **1. Sacred / Desecrated** | high status + visible damage | grief, fall from grace | a pearl gown with a stained hem and a chipped petal |
| **2. Cheap / Exact** | low status + one immaculate detail | dignity, discipline, pride | a starched collar above a re-sewn coat |
| **3. Clean / Wrong** | zero damage + one thing that should not be there | threat, the uncanny | an unstained white robe whose cuffs are dusted in dried chalk |
| **4. Function / Inversion** | an object used against its purpose | survival, obsession | armour worn for sleeping |
| **5. New / Unfitting** | nothing worn out + nothing fits | displacement, forced change | new tailoring over one unchanged old item |
| **6. Time / Reversed** | the surface improves as the object ages | maintenance as love or denial | a mended coat whose patches come from different decades |
| **7. Sacred / Dangerous** | flawless surface + one lethal signal; zero damage | unapproachable, not broken | a snow-white gown with blood-crimson irises |

Directions 1–6 are editorial; direction 7 is glamour. Do not use direction 7 in an editorial sheet — it reads as an empty character. Do not use 1–6 in glamour — the audience reads damage as a defect. If a brief wants both, that is a two-deliverable job: a glamour sheet for the cover and an editorial sheet for the bible.

Name the direction explicitly in the blueprint. An unnamed contradiction drifts back to Sacred/Desecrated by default. Two characters in one project should not share a direction.

## 6. Design thesis

Write one sentence before the prompt. It links the character's situation to a silhouette and material, so the model has a priority.

Formula: **[Role] who [situation] wears [silhouette/material] as [evidence].**

The thesis has two halves: a **situation** the model cannot draw, and an **anchor** it can. The anchor must be a physical noun — a garment, a material, a condition, a gesture. If the situation half stands alone as a metaphor without an anchor, models render the metaphor literally.

| Thesis | Verdict |
| --- | --- |
| `a deposed goddess wearing her ruined temple` | fails — "wearing a ruined temple" is a building |
| `a deposed goddess wearing the temple she outlived: thorns grown through water-stained lotus silk` | passes — anchored to silk and thorns |
| `an immortal who has stopped performing: oversized raw silk, ink-stained fingers, a plum branch holding his hair` | passes — three physical nouns follow the action |
| `a man who dresses like a closed museum` | borderline — needs a physical clause |

Every thesis must name at least one physical noun after the colon. The anchor should also carry a light behaviour or a weight when possible. Put this sentence at the start of the free narrative, not at the end.

## 7. Posture grammar

For a turnaround, the pose must be neutral enough to read from three angles, but specific enough to belong to the character.

- **Weight**: left/right leg, hip shift, one knee soft.
- **Shoulders**: level, dropped, raised, uneven.
- **Hands**: loose at the side, thumb hooked in a pocket, holding a sleeve, fist, open palm, raised to the hair. Hands never hold an object.
- **Gaze**: level, down-left, distant, direct.
- **Chin**: level, lifted, tucked.
- **Feet**: parallel, turned out, one heel raised.

Three recipes:

- **Poised**: weight on the back leg, shoulders level, hands loose, chin level, gaze direct.
- **Languid**: weight on one leg, one shoulder slipped, hands hidden in sleeves, chin slightly tucked, gaze distant.
- **Guarded**: weight forward, shoulders squared, one hand at the hip, chin lifted, gaze fixed.

Avoid extreme action poses in Mode A; they break the orthographic read and the fold structure.

## 8. Identity, look, state

| Layer | Contents | Changes? |
| --- | --- | --- |
| **Identity** | bone structure, eye shape/colour, hairline, scars, moles, body ratio, permanent accessories | never |
| **Look** | hair styling, clothing, makeup, temporary accessories | per outfit |
| **State** | wet, injured, tired, dirty, recent events | per shot |

Test: if they change clothes, what remains? That is the identity layer. Write it first.

The invariant layer is literal. It holds the things that make two renders the same person in a 3D pipeline: the exact eye design (lid line, crease, iris fibre, limbal ring), the shape of the cupid's bow, the position of a scar relative to the jawline, and the hairline. A re-used character whose eye design drifts between shots reads as a recast, because the eyes are the largest feature on the face.

## 9. Prompt-ready blocks

### A. Identity block (invariant, under ~70 words)

```text
[Age band + gender presentation + class read], [head proportion] with [shoulder-waist-hip]. [Face: bone structure, eye shape/colour, brows, nose, lips, skin]. [Hairline and permanent hair length/colour]. [Permanent marks or scars]. [Permanent accessories].
```

- Visible facts only; no value words.
- Reuse word-for-word across outfits, shots, and both images of a split delivery.
- `[shoulder-waist-hip]` is not optional. "8.5-head with a narrow long face" bundles a proportion with a face shape and drops the body; the model then invents the torso.
- Include the Position triple — age band, gender presentation, class read.
- Put skin in the invariant block, in one clause: `smooth porcelain skin with a soft subsurface glow`. The pore hint is added separately in the macro cell.

Example: `A woman in her late twenties, patrician, 8.5-head with narrow shoulders, a long waist, and narrow hips, a narrow long face with low cheekbones, large almond eyes with a defined upper lid line and a clear crease, ruby-glass irises with radial fibre, a darker limbal ring and a bright secondary reflection, a soft gradient berry lip with a visible cupid's bow, one crimson tear-mole beneath the right eye, a faint scar along the right jaw, and smooth porcelain skin with a soft subsurface glow. Waist-length blue-black hair with white inner streaks and a high hairline.`

### B. Design evidence block (this look, under ~100 words)

```text
[Weight distribution, shoulder line, hands, gaze, chin]. [Editorial: two life traces | Glamour: one status marker]. [One contradiction, named direction]. [Clothing construction, layers, closures, fit, wear]. [Worn accessories: material × form × wearing method].
```

- This is the look/state layer, not the identity layer.
- Editorial: two life traces and the contradiction must be visible at full-body distance. Glamour: one status marker and the Sacred/Dangerous signal.
- Name the contradiction's direction in the blueprint; do not repeat the label in the English prompt.
- Give one garment its weight or its light behaviour in this block: `the coat's wool dragging the hem low`, `the lacquer catching a hard edge along the lapel`.

## 10. Ensemble differentiation

Use the eight-axis matrix in [costume.md](costume.md) §6. At least four axes must differ between any two characters; silhouette and key colour are mandatory. Test the cast in wide shot, in grayscale, and after simulated desaturation.

## 11. Default portrait composition and output

- Use a centred half-body portrait from head to waist, shown from the front or a slight three-quarter angle.
- Show the complete head, hairstyle, accessories, both shoulders, and upper-body clothing.
- Use a simple background that separates the character without competing for attention.
- Default to the refined semi-realistic 3DCG finish in [../contract/visual.md](../contract/visual.md) §1 and §5.
- Keep mature facial proportions and grounded anatomy; avoid plastic or waxy skin, visible mechanical joints, excessive smoothing, flat lighting, and generic low-detail game-model aesthetics, per [../contract/visual.md](../contract/visual.md) §11.
- An explicitly requested painting or named medium replaces this default under the shared style rules in [../contract/visual.md](../contract/visual.md) §2.
- Do not turn the portrait into a full-body image unless the user asks for one.

Write one coherent English prompt covering subject, identity, face, hair, costume, accessories, pose, framing, background, style, lighting, and camera treatment. Prevent failures by describing the wanted result; put only single-word exclusions that materially reduce likely failures in `--no`.

Portrait parameters (`--ar 3:4 --raw --s 150`) are in [../contract/visual.md](../contract/visual.md) §3. User-specified values and alternative media follow the shared rules there.

When the user supplies the target character's identity reference, preserve its character identity and requested art direction. A different character's style reference supplies only the assigned visual treatment, per [../contract/records.md](../contract/records.md) §4. When the user requests a revision, keep every other confirmed design detail unchanged.
