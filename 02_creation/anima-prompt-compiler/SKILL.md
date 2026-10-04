---
name: anima-prompt-compiler
description: Model adapter that compiles a finished character or illustration blueprint into Anima-ready English prompts in a disciplined Tag block + Natural Language block format. Handles Anima-specific format contract, length budgets, positive-first output, V1 faithful / V2 enhanced modes, model profiles and artifact troubleshooting. Use when the user asks for Anima prompts, Anima 提示词, or names an Anima checkpoint. Does not design — if no blueprint exists, route through aesthetic-director-core and character-design-engine / illustration-direction first.
metadata:
  author: Tera-Dark
  version: "2.3.0"
  layer: "02_creation"
  load: "on-demand"
  status: "active"
  triggers: "Anima, Anima 提示词, Anima checkpoint"
---

# Anima Prompt Compiler

## Adapter Blueprint Boundary

This skill is an adapter, not a design engine. It may compile only a finished blueprint that has already passed the aesthetic and blueprint gates. If the input lacks a concrete proposition, silhouette, four-layer outfit structure, punctum, or locked facts, route back through `creative-skill-router` instead of inventing design decisions here.

## 1. 定位（v2.0.0 起）

本 Skill 是**适配器**：把已经做完设计决定的 blueprint 翻译成 Anima 能理解的英文。

它不再持有设计方法和品味规则。那些已经上移：
- 品味签名与否决清单 → `personal-identity-profile`
- 九个创作动作、反馈诊断、成对示例 → `aesthetic-director-core`
- 六层角色结构、服装词汇 → `character-design-engine`
- 构图协议、氛围预设 → `illustration-direction`

**输入检查**：收到的东西有没有一句带动词的命题、明确的轮廓、四层服装、一个刺点、锁定事实？没有 → 这不是 blueprint，退回 `creative-skill-router`。用户直接说"帮我写个 Anima 提示词，一个月光祭司"时，**不要**在这里补设计。

保留在本 Skill 的只有 Anima 相关的东西：格式契约、长度预算、输出模式、模型档案、伪影排查，以及对已验证 tag packet 的序列化。

## 2. 默认行为

- 用户要提示词时只输出提示词，不主动生图。
- 英文 Tag block + Natural-language block 两段式（§4）。
- 默认只输出正向提示词。需要排除某物时优先用正向约束翻译（"no jewelry" → 在 NL 段写 `bare neck and wrists`），只有正向无法表达时才给一个简短的独立 Negative，并说明原因。
- 不加 `masterpiece, best quality, 8k, ultra-detailed` 等空泛质量词（禁用清单见 `references/anima-model-profiles.md` § 5.2）。
- 不加权重、CFG、steps、采样器、Clip Skip 等工作流参数，除非用户要。
- 不改动 blueprint 的**锁定事实**。
- **任何进入 Tag block 的 Danbooru hard anchor 必须先通过 `anima-tag-gate`。**

## 3. Pre-compile Tag Gate

在组装最终 prompt 前，先把 blueprint 中准备进入 Tag block 的硬锚点交给 `anima-tag-gate`。

Gate 只允许三种结果：

- `exact` → 使用 canonical tag。
- `alias` → 使用 alias 对应的 canonical tag；alias 只保留为内部 provenance，不重复写入 prompt。
- `missing` / `unverified` → 不进入 Tag block；将原意翻译成 Natural Language。

禁止：

- 用 fuzzy / semantic similarity 结果直接当 hard tag。
- 为了"看起来更像 Danbooru"而自行改写未验证 tag。
- 把 candidate pool 当 confirmed tag。
- 让 Tag Gate 改变角色设计、服装设计、动作、构图或审美决策。

### Canonical vs serialized syntax

Tag Gate 输出的是 **canonical identity**，不是最终 Anima 字符串。序列化发生在本 Compiler 的最后一步。

例如：

`37_(reverse:1999)` → `37\\(reverse1999\\)`

不得在验证阶段把它拆成 `37`, `reverse`, `1999`，也不得让 canonical 数据层承担 Anima 权重语法转义。

## 4. 格式契约：Tag + Natural Language

### Part A — Tag block

逗号分隔的英文短标签，承担稳定锁定信息：

- 主体数量：`1girl`, `solo`, `2girls`
- 展示类型与景别：`full body`, `upper body`, `cowboy shot`, `white background`, `vertical composition`
- 外观事实：发色、发型（**写形状分布**，如 `long hair on the left side only, cropped short behind the right ear`）、瞳色、种族特征
- 服装单品：按 base → structural → signature extension → accessory 顺序
- 道具与动作：`holding curved scissors`, `tucking hair behind ear`
- 角色身份（如果 blueprint 有）
- **角色 / 系列触发词优先按 Anima 的 Danbooru 训练集实际 token 写法输出**，不要把角色名和作品名拆成多个 token。
- 只有 Tag Gate `exact` / `alias` 通过的 Danbooru hard anchors 才能进入这里。

Tag block 简洁、可扫描、不重复同义词。设计逻辑不塞进标签。

### Canonical Prompt Skeleton

Anima is compiled in one stable skeleton:
1. Tag Lock — subject, framing, identity, appearance, hair/face, clothing, props and action.
2. Natural-language Relations — garment hierarchy, asymmetry, spatial placement, pose causality, environment relation, light/material response, density and punctum.
3. Optional Negative — only when positive constraints cannot express the exclusion.

The compiler may compress within the model profile, but it does not redesign the concept.

### Part B — Natural-language block

一到两个连贯英文段落，承担标签表达不了的**关系**：

- 服装层级、剪裁、内外关系（`open coat over`, `hem showing beneath`）
- 轮廓的空间位置（`behind the head`, `descending from one shoulder`）
- 不对称的具体分布
- 姿势如何影响衣摆、袖子、头发、道具（blueprint 的因果链）
- 密度分布（`ornament concentrated around ___; ___ left plain`）
- 光源方向、衰减、材质响应
- 刺点的精确位置（`the only saturated color is ___ at ___`）
- 所有未通过 Tag Gate 的硬锚点含义

NL 段不是 Tag 段的同义词复述。它必须补充关系和层级。

### 模板

```text
[comma-separated verified tags]

[One or two paragraphs: garment hierarchy, silhouette placement, asymmetry, pose causality, density, light, palette hierarchy, punctum location.]
```

## 5. 长度预算（规划用，不是及格线）

| 任务 | Tag + NL 合计词数 |
|---|---|
| 头像 / 半身 | 30–50 |
| 角色立绘 / 时装 | 50–80 |
| 多层展示板 | 70–100 |
| 叙事场景插画 | 80–120 |

超预算时的删除顺序：重复形容词 → 次要配饰 → 背景枝节 → 材质细节。**不删**：命题结构、主锚点、刺点、锁定事实、因果链里的关键词。

验证不会增加预算：即使有更多 verified tags，也只保留对当前 blueprint 有价值的少数硬锚点。

## 6. 输出模式

### Direct Mode（用户要求直接给）
只输出最终提示词代码块，不加设计说明、策略线或解释。

### Standard Mode（默认）
1. 一行 Strategy Line（来自 blueprint 的命题）
2. **V1 Faithful**：忠实翻译 blueprint，只做语言转换、消歧、结构化排版，不做审美升级
3. **V2 Enhanced**：在 V1 基础上加入光影、材质行为、构图细化。**V2 不得改动 V1 的核心事实**（发色、瞳色、服装件、指定姿势）；如需变体，单独标注为 optional variant
4. Enhancement Notes：三行以内，说明 V2 加了什么

### Deep Mode（用户要完整分析时）
1. 命题、锁定信息、构图与服设决策（引用 blueprint）
2. Tag + NL
3. 简短校验说明

默认不输出冗长推理和审美宣言。

## 7. 多主体与歧义

- 多角色：按方位分块（`[LEFT]: ... [RIGHT]: ...`），每块内颜色紧贴名词。见 `references/anima-troubleshooting.md` 诊断项 04。
- Blueprint 里未锁定的细节：保持开放，不擅自补全（不给未指定的角色加上耳环、腰带、手表）。

## 8. 反馈轮

生图结果有问题时：
- **画面伪影**（手、融色、背景抢戏、串线、白底融边）→ `references/anima-troubleshooting.md`，单变量最小修复。
- **设计问题**（太平淡、太乱、不像 OC、没人味）→ **不在这里修**。退回 `evaluation-loop` → `aesthetic-director-core/references/feedback-diagnosis.md`。改 prompt 词治不了设计层的病。

## 9. 输出前检查

- [ ] 输入已通过 Aesthetic/Blueprint Gate？
- [ ] Anima hard anchors 已通过 `anima-tag-gate`？
- [ ] 每个 Tag 都有 `exact` / `alias` 证据，或已降级到 NL？
- [ ] 没有 fuzzy / candidate tag 混入 hard_tags？
- [ ] Tag 段简洁、具体、无同义重复？
- [ ] NL 段写了关系（层级 / 位置 / 因果 / 密度 / 刺点位置），不是复述 tag？
- [ ] 锁定事实一字未改？
- [ ] 无空泛质量词、无参数、无默认负面？
- [ ] 长度在预算内，且删的是次要项？
- [ ] V2 没有改 V1 的事实？
- [ ] canonical tag 与 Anima serialized syntax 分离？
- [ ] 遵守用户要求的输出格式？

## References

- `references/anima-model-profiles.md` — 证据分级、来源溯源、模型变体、文本编码器兼容、质量词清单、参数参考、实验日志
- `references/anima-troubleshooting.md` — 伪影诊断目录、最小修复、不确定性处理
- `anima-tag-gate` — Web-first exact → alias → missing gate
- 测试集：`tests/test-suite.md`
