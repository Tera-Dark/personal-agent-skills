---
name: small-artist-brain
description: Evidence-driven Xiao-artist visual decision overlay led by a 16-work study of illustrator 蒸蒸 ZHENG. Uses composition, character vitality, palette hierarchy, density, space, gesture and camera to raise illustration taste without copying works. Use for 小画师脑, 小画师审美, 米画师, 蒸蒸, ZHENG, 精美插画, 女性向视觉, 作者感, 人物活人感, 高完成度肖像, 双人互动设计, and visual taste refinement. Does not own character identity, generic aesthetic gates, renderer syntax or Danbooru tags.
metadata:
  author: Tera-Dark
  version: "1.0.0"
  layer: "02_design"
  load: "on-demand"
  status: "active"
  triggers: "小画师脑, 小画师, 米画师, 蒸蒸, ZHENG, 女性向, 作者感, 插画审美, 高定肖像, 双人活人感"
---

# Small Artist Brain / 小画师脑

## 定位与证据边界

这是**独立、按需加载的审美决策增强模块**，以用户提供的蒸蒸 ZHENG 16 张委托插画为主要观察依据。不是某位画师的模型 LoRA、不是画师 tag/画风复刻器，更不意味着所有图都要繁花、蝴蝶、绿紫高彩度。

**输入**：当轮意图 + identity 固定偏好 + 角色锁定事实 + `aesthetic-director-core` 的 Creative Brief（或已完成设计的 AUDIT 包）+ 可选参考图。  
**输出**：`Small Artist Decision Sheet`：可被 `illustration-direction` / `character-design-engine` 消费的具体画面约束、人物行为关系、配色与疏密方案及否决项。  
**上游**：`personal-identity-profile` / `aesthetic-director-core`；需要参考图提取时经 `image-reverse-analysis`。  
**下游**：`illustration-direction` 或 `character-design-engine` → Blueprint Gate → `visual-prompt-core` → 对应 renderer。  
**不做**：不取代基础通用审美层；不擅自改变官方角色外形、服设/性格；不重新定义通用 illustration blueprint；不编 NAI5/Anima 模型语法、不认定硬 Danbooru tag；不自行调用生图工具。

**独立职责**：将具象画师案例转成跨题材**可重复执行的画面选择与拒绝准则**。基础画面命题、视觉母题、场景/光源最终决策仍由 Director / Illustration owner 持有；本模块只给更审美化的具体候选和约束，以便现有 owner 做决定，**不得出现第二份平行画面 blueprint**。

## 理论来源与加载

- `references/zheng-16-work-study.md`：16 张用户上传图逐张证据、差异与跨作品验证。研究任务/质疑某条规则时必读。
- `references/zheng-transferable-grammar.md`：构图母型、色彩层级、人物气质、疏密、四种肖像模式、原创约束。实际创作优先加载。
- `references/style-tests.md`：五种原创跨题材压力测试、0–16 分自检与后续 A/B 记录方法。用户要求验收或纠偏时读取。

源码只写分析文字，不把私稿/委托画作原图、局部重绘、版权声明以外的图像资产复制进公开仓库。样本编号 Z01–Z16 指向本次会话上传顺序；若在另一会话不可见，必须说明只能读取研究结论而非再次查看原图。

## 不可妥协的审美判断

1. **先有角色生命，再有漂亮背景。** 必须明确角色性格如何改变他的眼、嘴、颈肩、手、重心；双人图不允许只用 `romantic tension` 代替交互因果。
2. **主体与环境构成画面结构，而非两张贴图。** 看第一眼大形如何被花枝/杯沿/栏杆/衣袖/道具参与构成，不先随机挑“繁花背景”。
3. **颜色以组织关系取胜，不是数值更艳。** 至少定义空气色、承重深色、面部/关键接触暖色和必要刺点，观察它们的面积与位置。
4. **人物焦点必须有呼吸区。** 面部、手、关键媒介附近须保持明确的轮廓或低干扰形状。高繁允许整体很满，但低对比区必须存在。
5. **细节跟随动作或母题生长。** 花叶随框景、衣料随承重、飘带随风和姿势、器物随行为；删掉不会伤害故事和大形的装饰。
6. **有色空间同样能留白。** 暗蓝、浅藤紫、淡青绿、纸白、虚化花群都可以成为安静区；留白不是背景永远纯白。
7. **至少设计一个不等价的微表情。** 眼神和嘴角、对视和肢体、主动与被动需要不完全一致，形成“活人感”。
8. **支持从极简到高繁的全部范围。** 观察 Z08 / Z14 / Z07 可知某一个固定复杂度不足以定义审美。不要强制给所有题材加花、动物、圆环、胶片、钟表或亮点。
9. **原创优先于临摹。** 引用机制，不复写任何一张委托作品的角色/具体道具/布局/主题组合。

## 工作流：8 次审美决策

```
S0 任务定调   确认官方服设/身份锁、画幅、情绪强度与是否允许场景；选 SIMPLE / BALANCED / ORNATE。
S1 活人机制   确定主体的性格态度与一秒内的具体行为；双人再定 A→B→A 的反应回路。
S2 大形       以人物肢体/发丝/衣料/场景物共同组织唯一大形；缩成图标仍有重心。
S3 机位       选一个真正让动作更有力的视角；先推导裁切和遮挡，再决定景物。
S4 色群       空气色、承重色、脸手亮区、一个有意义的刺点；允许多局部色但回归三大色群。
S5 视觉密度   标出主精、次精、弱精；主精只集中在眼/表情/手/关系媒介。
S6 作者取舍   从 `zheng-transferable-grammar.md` 选 1 个母型机制，不复制具象场景；主动否决 2 个俗套。
S7 验收交接   通过视觉命题、可见表情、动作承重、配色/疏密、角色身份与原创性检查，输出 Decision Sheet。
```

### 题材强度开关（最重要）

| 情况 | 默认强度 | 小画师脑应该加强 | **绝对不默认加入** |
|---|---|---|---|
| 极简白底半身 | SIMPLE | 非模板脸、头肩气质、手部微动作、轮廓、画幅留白 | 复杂花园、无关动物 |
| 日常抓拍 / BL / GL 双人 | BALANCED | 角色性格反差、A→B→A 行为回路、共同轮廓、脸手高优先级 | 强吻摆拍、统一红脸、花鸟滤镜 |
| 幻想高完成度插画 | ORNATE | 结构明确的繁复、层次框景、彩度冷暖组织、比例变化 | “高密度”无差别铺满 |
| 人物立绘/服装展示 | BALANCED | 服设独特体块、材质、人体重心、一个非标准动作 | 过度遮挡识别锚点 |
| 古风氛围肖像 | BALANCED | 器物引导的手眼行为、袖带有重力的流线、留白层次 | 无因果长袖/花海 |
| 高概念或极长竖版海报 | ORNATE | 视觉母题串联多尺度叙事、纵向焦点接力 | 把任何纪念图都变成胶片或钟表 |

如果用户明说“纯白背景/原版服装/更日常/不要花”，直接锁定，不能被 ORNATE 覆盖。

## 输出契约：Small Artist Decision Sheet

```yaml
mode: SIMPLE | BALANCED | ORNATE
source_mechanism: "借用 Zxx 的哪种可迁移构图/色彩机制（可空，不抄原画）"
character_life:
  temperament: "具体性格在这一秒如何表露"
  face: "眼/嘴/眉的一处非标准表情"
  gesture_and_cause: "由什么起因做出什么动作"
  response: "另一个角色/物件如何回应；无则省略"
macro_shape: "2–3 大质量、主要运动方向、人物与背景如何扣合"
camera_and_crop: "画幅、机位、景别、遮挡与理由"
color_mass: "空气色 / 承重色 / 人物焦点色 / 唯一刺点"
density: "主精 / 次精 / 弱精"
environment_function: "场景如何框住/承重/驱动/留下痕迹"
negative_space: "位置 + 材质 + 视觉作用"
identity_locks: "不能变更的角色与服装事实"
rejected: "至少两种已排除的公式化方向"
handoff_notes: "传给 Illustration/Character owner 的决定，renderer 不可重设计"
```

输出可以是极简中文简报，复杂情况下才展开字段；`PROMPT ONLY` 时仅在内部使用，不向用户展示。不能以这份 Sheet 绕开既有 Aesthetic Gate / Blueprint Gate。

## 验收标准（先设计自检，再等待出图验证）

- [ ] 不看题目也能从表情、肢体、道具认出当刻的态度/关系？
- [ ] 缩略图可辨人物主质量、动线、亮暗重心？
- [ ] 场景的至少一个部分确实参与动作/空间？
- [ ] 人脸/手周边是否有清楚的清晰度通道？
- [ ] 多色在三大色群下仍可管理；不是盲目饱和？
- [ ] 华丽模式里的每种装饰有依附的大形；极简模式不会被强制加料？
- [ ] 角色身份、原版服饰、CP 性格是否保持？
- [ ] 不会被指认为“把 Zxx 的某张构图原样换角色”？
- [ ] 经过删除测试后作品仍有核心视觉思想？
- [ ] 如无实测，不声称已“稳定还原画风”，只声称有可检验的设计规则？

## References

- `references/zheng-transferable-grammar.md` — 16 作品抽象出的构图、配色、活人表情、疏密与提示词转译规则。
- `references/zheng-16-work-study.md` — 16 张可见作品的逐张观察，含证据编号、差异和边界。
- `references/style-tests.md` — 白底、双人、幻想、深色冷感、古风的原创验收例与评价表。
