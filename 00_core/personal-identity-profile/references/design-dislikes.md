# Design Dislikes — 否决清单

> 每一条都是历史反馈里反复出现过的。这不是"永远禁止"清单，是"没有因果链就默认不出现"清单。
> 判断标准只有一个：**能不能说出她为什么会有这个**（`aesthetic-director-core/references/creative-moves.md` M4）。一只怀表在"以记忆为燃料的钟表裁缝"身上是命题本身；挂在随便哪个少女腰上就是 AI 味。
> 升格规则：某样东西被否决 ≥3 次，或用户明确说"以后都不要"，才写入本文件。写入时注明日期。

## General Principle

Avoid adding elements only because they are considered "cool".

Every element should have a design reason and contribute to character identity.

## 最高优先级否决项（2026-09 之前已反复确认）

- **手表 / 怀表 / 钟表** —— 除非与时间、职业、剧情或服装主题高度适配，否则禁止主动加入。这是历史上最高频的否决。
- **无来源的饰品作为"高级感补丁"** —— 随机金属链、随机宝石、随机蝴蝶、随机玫瑰、魔法阵、荧光粒子。

---

# Newly promoted anti-patterns — 2026-10-04

These are now explicit dislikes when they appear without a strong reason:

- Beauty-filter face — mirrored eyes, identical eyelid geometry, excessive iris sparkles, porcelain-smooth skin and zero painterly irregularity.
- Soft-light soup — the whole image dissolved into bloom, haze, bokeh and floating particles with no decisive cast shadow.
- Surface-only hair — large hairstyles rendered as a shell covered in random flyaway strands, with no readable roots, mass, wrapping or fastening.
- Accessory wallpaper — flowers, pearls, chains, tassels and ornaments accumulated for luxury without visible attachment points or shared construction logic.
- Atmosphere as background — using fog, light spots, petals or dreamy color wash instead of a designed environment or a clean white field.
- Detail without hierarchy — uniformly high detail everywhere, so the image has no dominant mass, quiet field or visual route.

These are defaults to reject because they repeatedly weaken identity and authored design; explicit current-turn requests can override them.

---

## 2026-10-15 · 镜头/角色专项修正（作用域限制）

- **NAI5 电影感/叙事**：重复雨夜车站、玻璃水滴、蓝橙工业灯、文件/纸张和没有行动职责的黄伞等，会变成「漂亮背景 + 摆拍」；默认撤掉这些模板，人物既有剧情/任务/生活动作先行。用户指定题材允许合理出现。
- **古风小画师肖像**：被用户明确指出「不要拿纸」「没有互动」「单纯炫技」。当没有特殊道具要求，优雅姿势靠肩颈/手臂/转身/身体重心/与环境或人动物的具体回应；避免把折信/卷轴强塞进所有造型。
- **IP 同人**：跨作品串角色、无依据杜撰正典剧情、泛漂亮脸导致身份不明，均须优先纠正；剧情不确定则注明同人解读。**两格情绪近景**仅在请求分镜时用，不拿重复泪眼特写冒充情绪推进。
- 单次「参考图喜欢」并不构成永久禁用其他美学的理由。具体证据与作品作用域见 `session-feedback-2026-10-14-15.md`（由 Identity 按需载入）。

# Overused AI Elements

Avoid unless specifically requested:

- random watches
- unnecessary necklaces
- meaningless earrings
- decorative belts
- excessive straps
- arbitrary accessories

Reason:
These often create artificial complexity without improving the design.

---

# Mechanical / Cyber Elements

Avoid excessive use of:

- cyberpunk aesthetics
- techwear
- mechanical armor
- futuristic machinery
- glowing interfaces

Small mechanical details are acceptable when they support the theme.

Preferred direction:
Fantasy, fashion, elegance, personality.

---

# Complexity Problems

Avoid complexity for its own sake.

Bad:

- random decorations everywhere
- unrelated patterns
- too many competing elements
- excessive asymmetry
- overloaded color schemes

Preferred:

Complex but organized.
Rich but readable.

---

# Character Problems

Avoid:

- generic fantasy girl
- emotionless beauty model
- empty standing pose
- no personality
- no story implication

A character should feel like a person, not a mannequin.

---

# Style Problems

Avoid:

- generic AI fantasy aesthetics
- male-oriented armor fantasy
- meaningless sexy elements
- visual noise
- trend chasing without identity

Design priority:

Character identity > decoration.
