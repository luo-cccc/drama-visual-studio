# Records: Character, Location, Version, Reference Roles, Delta, Ledger

Two records, one abstraction. A **character record** holds identity and costume; a **location record** holds place and state. Both exist for the same reason: one place to keep what must stay fixed while cameras, outfits, and states change.

Keep a record in the conversation, or deliver it as text when useful; do not create project files unless requested. A one-off background figure or a one-off edit does not need one — keep the work proportional.

## 1. Character record

Build it in production mode, and at the end of design mode for a character that later outputs will reuse. It turns a design — from this skill or from an external design skill — into one compact record that every downstream prompt reads. It is not a copy of the design prompt, not a redesign, and not a substitute for the derivation engine.

Extract; do not re-invent. Mark every field as **observed** (visible in a supplied image), **confirmed** (stated in text or adopted by the user), or **inferred** (missing, completed conservatively).

When only an image is supplied, record what is visible — face, hairline, permanent marks, build, costume layers, palette, worn ornaments — and mark occluded areas and unseen backs as unknown. Do not infer a full costume from a portrait and present it as observed.

| Field | What to take | Why |
| --- | --- | --- |
| **Lock & IFV** | genre / subgenre / pigment family / silhouette family / gear / register + Invariant / Free / Forbidden | locks acceptance criteria and blocks cliché regression |
| **Identity block** | age band, gender presentation, status read; head count with waist-cut and shoulder-waist-hip; derived face bone structure (§1A), iris colour/optics, brows, nose, lip state, specular/matte map, and 0-or-1 mark (§1B); hairline and permanent hair; permanent accessories | copied word-for-word into every prompt; this is what keeps renders the same person |
| **Look layer** | current costume: layers in order with physical understructure, closures, materials, trim language + raw set, motif family, palette roles (base / anchor / accent, with HEX when supplied), worn ornaments | sheet, scene, asset, and edit prompts |
| **Pose vector** | `weight axis · shoulder-neck line · empty-hand action · chin & gaze` | prevents turnaround sheets from collapsing into a generic neutral stance |
| **State layer** | current condition, imperfections, contradiction signal, recent events | scene placement and variation prompts |
| **Palette** | 70/25/5 roles, plain-language names, HEX from the blueprint, one chromatic anchor | prevents the render from inverting the palette |
| **Evidence status** | observed / confirmed / inferred, plus unknown areas | controls what may be asserted |
| **Reference roles** | which image supplies identity, style, layout, or edit target | prevents a style reference from becoming an identity source |
| **Target output** | which downstream prompt is requested | selects the workflow |

Rules:

- Reuse the identity block exactly. Paraphrasing it is how identity drifts across images.
- Do not carry review vocabulary into the English prompt; [gates.md](gates.md) §6 lists what is banned.
- Do not copy an upstream negative block verbatim. Use it to diagnose likely failures, then write exclusions in the target engine's own form — see [visual.md](visual.md) §11.
- Do not import held or carried props into a character sheet; they are shot-level assets per [gates.md](gates.md) §4.
- Do not redesign the face, body, costume construction, or palette. A confirmed medium or finish is not a default to be normalized.
- Do not invent HEX values, measurements, hidden anatomy, or unseen views. When a missing field changes the result, ask one focused question.

### Template

```text
角色记录
锁定行：[genre / subgenre / pigment family / silhouette family / gear / register]
IFV 声明：Invariant [...] · Free [...] · Forbidden [...]
身份块：[verbatim identity block: Position, proportion + waist-cut, §1A bone + §1B surface/iris/lip/mark, hairline]
姿态向量：[weight axis · shoulder-neck line · empty-hand action · chin & gaze]
外观层：[current costume layers, physical support, closures, materials, trim + raw edges, motif, worn ornaments]
状态层：[current condition, imperfections, contradiction signal, recent events]
配色：[70% base / 25% anchor / 5% accent + HEX + chromatic anchor]
证据状态：[observed / confirmed / inferred / unknown]
参考图角色：[identity image / style reference / layout reference / edit target]
目标产物：[portrait / identity sheet / costume sheet / GPT sheet / scene / variation / outpainting / asset / correction]
```

## 2. Location record

Keep one for a place reused across several edits or viewpoints, or when drift needs correction. Reuse an existing record or summarize only the facts the task needs.

Include the source and selected version, a few distinguishing structures and supported spatial connections, the current accepted state, and relevant unknown areas. Separate what is visible, what the user specified as design, and what was inferred. The initial prompt expresses design intentions; the actual image shows which details were realized. An overlap alone does not prove an object's location behind another, and image-left does not establish a compass direction.

```text
地点：[已知名称或简短描述]
结构依据：[实际图片或用户确认的文字设计；未见图片时注明]
当前版本：[本次选定的编辑图或文字状态]
已观察：[可见的建筑特征、尺度关系、道路连接；不从遮挡臆测]
设计指定：[用户明确给定、但图中未显示的关系或造型]
当前状态：[仍需继承的人物、道具、灯光、天气、损坏及已移除内容]
未知或推断：[未观察的背面、遮挡区，以及本次需要补全的部分]
```

Update only the facts affected by an adopted result or the user's explicit revision. Reuse confirmed views that help the requested shot, rather than requiring a full turnaround, comparison grid, or additional approval images. Do not invent a version ID or filename and imply that a saved asset exists.

When both records are active, the identity block is reused word-for-word and the place's current accepted state is preserved. Keep them separate: one holds identity and costume, the other holds place and state.

## 3. Source and version selection

- Identify the edit target by its actual attachment order, filename, or a clear description. It supplies the current visible scene and state. Separate it from an original structural reference, another view, a character identity image, and a style reference. A reference name identifies an image, not a calibrated place or camera.
- For independent alternatives such as day, night, and snow, start each from the designated base. For cumulative changes, edit the selected current version and retain its accepted changes. An older image can support structure but must not restore removed props or undo later damage, lighting, people, or signage changes.
- Using the image the user selects requires no extra approval step. Treat their adoption or selection of a result as acceptance; incidental additions in unadopted outputs do not become requirements for the place. A new explicit design change supersedes the corresponding earlier constraint.
- Distinguish a fixed-view state edit, a crop, a canvas extension, and a new camera view. A combined request replaces only the affected locks: cropping changes framing; extension adds outside the original region; moving the camera changes projection and occlusion. Do not keep contradictory framing or pixel-position requirements.
- If the source is unavailable, use confirmed text for a provisional prompt and state that it has not been checked against the image. Keep unknown geometry unspecified. Do not invent attachments, observations, measurements, or claims of achieved consistency.

## 4. Reference roles

Assign every input a role. When one image serves several roles, declare each separately. Use the smallest relevant set of inputs.

| Input | Supplies | Must not carry in |
| --- | --- | --- |
| **Identity image** | face, bone structure, build, hair, permanent marks, costume construction | its background, studio lighting, out-of-frame objects |
| **Design sheet or blueprint** | confirmed design decisions and evidence | another character's identity or proportions |
| **Design prompt** | stated intentions | proof that the rendered image shows every intended detail |
| **Style reference** | medium, surface quality, lighting tendency, palette relationships | the target's face, body, costume, or exclusive palette |
| **Layout reference** | panel division and arrangement | its characters, scene content, palette |
| **Scene edit target** | the current visible place and state | a new character's identity |
| **Scene structure image** | visible structure, landmarks, paths, scale | its people, its weather and time of day |
| **Midjourney style base** | medium, surface quality, lighting tendency, palette relationships | its composition, pose, background, aspect ratio |

Tell the model what each input supplies and which image receives the edit. If the current version and an older base differ, keep the current accepted state and use the older image only for the intended structural evidence. If a material conflict cannot be resolved from the request or the selected version, ask one focused question; do not silently merge incompatible layouts.

An upstream prompt records design intentions; the actual image shows which details were realized. Similar colour or style alone is insufficient evidence of the same place or character.

## 5. Output delta

For each requested output, decide what is preserved, what may change, and what must be re-derived. This is the difference between adapting a design and redesigning it.

| Output | Preserve | May change | Re-derive or infer |
| --- | --- | --- | --- |
| **Portrait** | identity, costume, palette, confirmed finish | framing, background, light | lower body outside the crop |
| **Identity sheet** | identity, build, costume construction, palette, pose vector | layout, panel count, background value | hidden anatomy, back details, footwear |
| **Costume sheet** | identity, costume construction, palette, pose vector | display magnification, background value | hidden head space, costume back |
| **Costume variant** | identity **verbatim**, palette roles, confirmed finish, silhouette family (unless status changed) | garment layers, construction, closures, materials, trim, motif, topology, ornament set, hair styling | the new look's hidden backs, footwear, and the support for any new volume |
| **GPT Image 2 sheet** | identity, design, palette, medium, pose vector | layout language, exclusion form | newly designed minor-character details |
| **Character in a scene** | identity, costume, palette, register | pose, scale, camera, environmental light | contact shadows, bounce light, occlusion |
| **Scene variation** | scene structure, current accepted state | time, weather, characters, props | new lighting, reflections, surface state |
| **Outpainting** | the original region's design, scale, perspective | canvas, framing | cut-off anatomy or background |
| **Asset chain** | identity, costume, palette, finish | background (mid-gray), layout | hidden structure, first-frame state |
| **Correction** | the selected source's unaffected content | the observed defect only | local revealed background |

## 6. Cross-record prohibitions

- If the design already delivered the same sheet, do not regenerate it. Convert it, place the character in a scene, extend it, or correct it. State clearly when the requested output changes the layout, canvas, or presentation.
- If only text exists, use it provisionally and state that the visual check is pending.
- Preserve the confirmed finish during scene edits and outpainting unless a restyle is explicitly requested.
- Keep this skill's output discipline: one copy-ready prompt per requested output in a fenced code block, no invented parameters or pixel dimensions.

## 7. Delivery shape

- An optional 2–4 line handoff note: the actual source, the locked fields, the inferred fields, and any missing input. Example: `依据：设定图与设计提示词；身份块与服装逐字沿用；背面未提供，正面之外为保守推断；目标为雨夜场景入景。`
- One copy-ready prompt per requested output, in the language and engine form its workflow specifies.
- If asked only to review or extract, stop at the record and findings.

## 8. Batch ledger (10 axes)

One ledger per project. It holds the **ten differentiation axes** from [gates.md](gates.md) §9 so a new character can be differentiated against the cast across silhouette, colour, topology, register, contradiction, lighting, trim, motif, **face bone+surface**, and **orthographic pose vector**.

Keep it in the conversation or deliver it as text; do not create project files unless asked. A single one-off character does not need one.

**Before designing:** read the ledger and pick values that clear the mandatory axes. **After adoption:** append one row. Do not append a character the user rejected.

```text
批次账本
[角色名或编号] | silhouette · key colour family · topology · register+gear · contradiction+signal · light · trim language · motif family · face anchor (bone + iris/mark) · pose vector (weight/hands/gaze)
    ↳ [variant label] | identity locked · topology · trim language · motif family · node distribution
[角色名或编号] | ...
```

A **variant line** sits under its character with a `↳` marker. It records only the four look factors, because a variant's identity is locked and its silhouette and key colour are inherited — see [gates.md](gates.md) §9A. A variant never consumes a silhouette or key colour slot in the cast, and it is never compared against other characters on axes 1 and 2.

Worked rows, one project, showing all ten axes separating cleanly across high-aesthetic Oriental fantasy characters:

```text
批次账本
A 九幽魔宗左护法 | asymmetric · 玄黑+幽冥紫黑 · topology 3 单侧异化 · editorial gear 2 · dir1/墨玉化指尖与乌金骨刺护手 · 明暗伦勃朗侧逆 · 乌金掐丝包边(烟纱外袖与开衩毛边留空) · 幽冥骨铃脊椎纹 · 面部指数1.48+眼角+6°+深渊血珀瞳+左眼尾暗金魔纹 · 重心落右腿微曲+左手乌金护指轻搭腰玉+微抬下巴垂眸睨视
    ↳ A 血海祭典盛装 | identity locked · topology 1 顶峰下泻 · 暗绯鎏金宽镶边 · 业火红莲暗纹 · 节点聚于乌金高冠与双肩垂链
B 太虚剑宗首座 | column · 月白+天青 · topology 5 骨相紧束 · editorial gear 2 · dir4/金丝修补的半碎寒玉剑冠 · 高调珠光 · 冷银窄压边(素白内衬袖口留空) · 冰裂剑气几何纹 · 面部指数1.50+口宽0.76+霜银琉璃瞳+无面部印记 · 双足并立修长挺拔+双手拢入广袖+平视清冷直视
C 妖族凰血少主 | hourglass · 绛红+鎏金 · topology 2 底重下坠 · glamour gear 3 · dir6/蝉翼金纱下紧锁心口的玄铁锁灵甲 · 暖调全局光 · 鎏金羽鳞滚边(层叠拖尾纱边留空) · 烬羽凰尾纹 · 面部指数1.36+眼距1.12+熔金竖瞳+眉心赤金凤羽印 · 重心前倾压步+右手微抬轻触锁骨金链+侧首4°挑眉邪笑
```

Rules:

- **The ledger is a diff tool, not a design tool.** It never supplies a design; it tells you which values are already spent.
- **Record what was adopted, not what was proposed.** An unadopted draft does not occupy an axis.
- **A repeat on a non-mandatory axis is allowed only with a stated reason.** Six of ten differing is the floor; if a character must share the trim language (a uniformed faction), say so and take a different axis instead.
- **Do not invent a row for a character who has no record.** The ledger and the character record in §1 are separate: §1 holds one character's identity, §8 holds the cast's spread.
- **A variant line is not a cast row.** It inherits silhouette and key colour from its character, carries only the look factors, and is exempt from the axis 1/2 hard rule per [gates.md](gates.md) §9A.
- **Do not restate the axis definitions here.** They live in [gates.md](gates.md) §9 and this file only stores the values.
