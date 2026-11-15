# Pipeline: GPT Image 2 Character Sheet

Use this workflow when a minor or non-key character should be designed directly as a complete sheet for GPT Image 2, or when the user explicitly requests a GPT Image 2 sheet. Deliver one copy-ready prompt. Image generation still requires the user's separate request.

## 1. Design source and reference roles

- For a new character, take identity, age cues, species, build, role, face, hairstyle, costume, and palette from the user's concept and established world. Reuse the design decisions in [../bank/truth.md](../bank/truth.md) and [../bank/costume.md](../bank/costume.md), not their half-body framing. Fill gaps coherently and preserve explicit choices. Do not require a portrait, outpainting, full-body approval, or separately generated views first. For a designed look rather than a quick sketch, apply the relevant layers from [design.md](design.md) and the density settings for the character's status; minor importance lowers design exploration, not image finish.
- A main-character sheet assigned as a style reference supplies visual treatment: actual medium, degree of stylization, form modelling, brushwork, edge treatment, material detail, lighting, and colour handling. Describe the observed treatment concretely. The new character's face, hair, clothing construction, personal symbols, body shape, and exclusive colours come from its own design. Shared uniforms or faction motifs transfer only when requested or established by the world.
- If the target character also has an identity image, identify it separately and apply the source-preservation and conservative-completion rules in [sheet.md](sheet.md). A style-only image is never evidence of the target's original proportions or hidden costume.
- Describe each attachment by its actual image order and role, or by a clear distinguishing description when order is unavailable. Do not invent an attachment or claim to have extracted an unseen image's style. Without the requested style image, use confirmed textual art direction or the sheet default, and briefly state that matching awaits the reference.
- Minor narrative importance changes the amount of design exploration, not image finish. Costume complexity and ornament density follow occupation, status, and the user's choices. Keep the style reference's level of finish and material clarity rather than automatically making every minor character plain or low-detail.

Reference roles are defined once in [../contract/records.md](../contract/records.md) §4.

## 2. Reuse the sheet's visual logic

Read [sheet.md](sheet.md) §1–§6 for sheet modes, layout, body occupancy, per-cell scoping, dynamic description, and the default finish. Apply those rules to the newly designed target, rather than treating the style-reference character as the subject. Read [../contract/visual.md](../contract/visual.md) for style priority and medium-specific language; skip its Midjourney parameter columns.

Default to the **identity sheet** layout for a new character: one 16:9 landscape sheet, left ~58% three full-body orthographic views (front, exact 90-degree side, back), head to toe uncropped on one shared ground line; right ~42% a 2×2 grid of bust cells — top-left symmetrical front bust, top-right 45-degree bust, bottom-left exact 90-degree profile bust, bottom-right tight macro on eyes, nose, and lips with crown and shoulders deliberately cropped out of that cell. Use the **costume sheet** layout when the face is already established and the task is costume presentation: left 55% neck-to-foot views with reserved head space and hair hidden only there, right 45% portraits.

For the identity sheet:

- Keep the reserved head space rule only for the costume-sheet variant; on the identity sheet the full body is visible and uncropped.
- Name the top-left bust cell neutral and attach the one physical micro-expression to the bottom-right macro cell only.
- Keep identical costume details, hair streaks, markings, and palette across all panels. No held or carried object appears in any panel, per [../contract/gates.md](../contract/gates.md) §4; worn ornaments stay.
- Set the background by the costume's value per [../contract/visual.md](../contract/visual.md) §9. Keep it seamless; no scenery, horizon, or outer frame.
- State the target canvas. If the engine cannot hold seven panels at the target size, use the split protocol in [../contract/visual.md](../contract/visual.md) §10.

For a new concept, establish one coherent anatomy and complete costume, then repeat them across all views. Do not describe the new design as recovered from the main-character sheet. A belt, armour edge, garment waist, or robe hem does not determine anatomical waist position or leg length. For an existing target, preserve its visible identity and build and briefly disclose inferred hidden structure. User-requested proportions, anatomy, poses, layout, and garment lengths take priority.

## 3. Convert the Midjourney prompt logic

- Keep the visual requirements: character identity, reference roles, canvas and panels, body occupancy, view alignment, costume construction, materials, selected medium, and lighting.
- Write the aspect ratio as a natural-language composition request, such as "16:9 landscape canvas." It is a requested composition, not a claim that output pixel dimensions or UI settings were configured.
- Remove Midjourney parameters, reference codes, URL prefixes used as command syntax, and weights. Omit `--ar`, `--raw`, `--s`, `--sref`, `--cref`, `--oref`, `--no`, and similar suffixes. Do not translate a stylization number into an invented GPT Image setting.
- Express exclusions in natural language and scope them to the correct panel, per [../contract/visual.md](../contract/visual.md) §11. For example, hide hair in the left costume views while keeping it in the portraits; request a clean sheet without text, labels, logos, or watermarks when labels were not requested. Do not globally exclude heads, hair, or clothing needed elsewhere.
- Keep the actual reference medium. A painted reference does not acquire PBR or skin-shader terminology just because the source workflow supports CG. Describe observed lighting rather than overwriting an explicit style match with default studio lighting.

## 4. Prompt assembly and output

Use the language requested by the user, otherwise the language of their request. Write one self-contained prompt in a fenced code block, ordered as: generation goal and input-image roles; target identity and complete design; canvas and panel layout; view and proportion consistency; style and lighting; local visibility and other exclusions. Produce one character and one sheet per prompt unless the user requests a group or batch.

The following scaffold shows the identity-sheet structure for a new character with a style attachment. Replace every bracketed field with the actual brief; omit absent inputs and irrelevant traits. For an existing target, replace the new-design language with identity-preservation instructions. For a costume sheet, replace the layout paragraph with the costume-sheet layout from [sheet.md](sheet.md) §3.

When a promised style or identity reference was not actually attached, leave the reference clause out of the prompt so it stays self-contained and copy-ready, and say outside the prompt that the attachment is missing and style matching is still pending. A sheet can be generated from text alone, whereas a scene edit has nothing to act on without its target image.

```text
生成一张完整的[目标角色]角色设定图。附件[实际编号或明确描述]中的重要角色设定图作为画风参考，借鉴其中的[实际观察到的媒介、造型风格、笔触、材质表现与光照]。本张图的角色身份、五官、体型、发型、服装和专属配色依据以下文字设计。

角色设计：[年龄特征、种族、体型、职业与世界观；具体五官和发型；完整服装层次、结构、鞋履、配色与实际存在的材质]。各个视角表现同一个角色，服装结构、层次、扣件、装饰位置与配色保持一致。

[纯白或按服装明度选择的暖白]无缝背景，16:9横版画布。左侧约58%为正面、严格90度侧面、背面的全身三视图，头到脚完整不裁切，共用一条地面线和统一比例；右侧约42%为2×2头像网格，依次展示正面、45度、严格侧面和正脸近景。

右侧左上角为正面对称头像，表情完全中性；右上角为45度头像，头部轻微偏转；左下角为严格90度侧脸；右下角只拍眼、鼻、唇的紧特写，该格刻意裁掉头顶和肩部，承载[一个身体化微表情]。左侧三个人物保持同一套解剖结构、中性站姿、空手、统一弱透视和一致的接触基线。

右侧头像保留本角色的发型设计与识别特征，头发在此区域正常显示，保持同一张脸和相同的头颈肩关系。放大只改变展示倍率，按各视角合理取景。所有区域采用一致的[选定画风、材质处理、光照和完成度]。

画面保持无缝背景，不出现景物、地平线或外框；角色手中不持握任何道具，佩戴式首饰与发饰保留。所有面板的服装结构、纹样位置、配色与材质一致。画面[按实际要求填写局部排除项及文字要求]。
```

After the prompt, briefly identify newly designed details or inferred structure and explain which attachment supplies style versus identity. Do not append Midjourney settings, API configuration, or promises of exact layout, identity isolation, or multi-view consistency. Corrections to an individual result remain local unless the user requests a general rule.
