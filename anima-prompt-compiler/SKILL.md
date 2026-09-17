---
name: anima-prompt-compiler
description: Compile character concepts, fashion designs, OC settings, composition briefs, and visual blueprints into concise, expressive, positive English prompts for the Anima anime image model. Features modular architecture with model profiles, fashion patterns, composition protocols, troubleshooting diagnostics, and flexible de-AI aesthetic engines.
---

# Anima Prompt Compiler (模块化动漫提示词编译器)

## 1. Mission & System Architecture

将用户的自然语言需求、OC 设定、服装设计案、中文视觉蓝图或已有粗糙 Prompt，精准编译为专为 **Anima 动漫图像模型** 优化的高水准英文提示词。

本编译器采用**解耦与模块化体系架构**，由五大知识库作为支撑支柱：

```text
               ┌───────────────────────────────────────┐
               │         anima-prompt-compiler         │
               │       (核心调度与语法编译中枢)        │
               └───────────────────┬───────────────────┘
                                   │
       ┌───────────────────────────┼───────────────────────────┬───────────────────────────┐
       ▼                           ▼                           ▼                           ▼
【模型知识库】               【构图排版协议】             【去AI味美学引擎】           【服设与材质模式】
anima-model-profiles        anima-composition           anima-aesthetic-deai        anima-fashion-patterns
(负责模型兼容性与证据溯源)  (负责画面稳定性与展示板)    (负责审美自由增强)          (负责穿搭与材质碰撞)
       │
       └──────────────► 【异常诊断手册】 ◄──────────────┘
                         anima-troubleshooting
                         (负责常见崩图与冲突消解)
```

- **模型知识库** (`references/anima-model-profiles.md`)：基于证据分级（Official / Compatibility Guidance / Community Practice / Experiment）掌控模型特性、语法权重与有效渲染词，负责**兼容性**。
- **构图排版协议** (`references/anima-composition-patterns.md`)：掌控全身立绘、牛仔景别、多尺度展示板（前景立绘+背景放大头像），负责**稳定性**。
- **去 AI 味美学引擎** (`references/anima-aesthetic-deai.md`)：掌控六大人性化美学思维与 5 大风格预设（商业头像、甜美可爱、高级服设、暗黑叙事、电影海报），负责**审美按需增强，拒绝单一固定模板**。
- **服设与材质模式** (`references/anima-fashion-patterns.md`)：掌控 4 层叠穿架构、非对称剪裁与物理材质对抗，负责**视觉质感**。
- **异常诊断手册** (`references/anima-troubleshooting.md`)：基于 4 步诊断流掌控肢体崩坏、内外层服装融合、背景抢主体与多角色串线的排查与归因不确定性处理。

---

## 2. Core Principles (编译原则)

### 2.1 锁定信息与不确定性处理
- **忠实保留已明确特征**：发色、瞳色、种族特征、指定服装配色与关键道具属于不可侵犯锁死项，严禁擅自篡改。
- **未确定信息保持开放**：对输入或参考图中无法明确确认的细节，**严禁脑补后列为锁定项**。保持描述的包容性，将探索空间留给画面本身。

### 2.2 多角色身份隔离 (Multi-Subject Isolation)
画面中出现多于一个角色时，必须按角色独立绑定属性块（`Character A: appearance + clothing + action`），严禁混合散落形容词以防止色彩与肢体串线。

### 2.3 正向优先输出协议 (Positive-First Output)
Prefer positive visual descriptions over standalone negative prompts.

Convert exclusions into affirmative scene constraints whenever possible, such as:
- "a single character centered in the composition" (替代不要出现其他人)
- "a clean white studio background" (替代不要有复杂背景)
- "an uncluttered environment with low visual density" (替代不要让背景抢主体)

Do not generate a separate negative prompt by default.
If the user explicitly requests negative prompts or a specific frontend requires them, explain the compatibility trade-off first.

### 2.4 全面净化空泛质量词 (Purge Low-Information Tokens)
默认拦截过滤 `masterpiece, best quality, ultra-detailed, 8k, insane quality` 等词，以具体的空间、光影、微观织物纹理代替。

---

## 3. 弹性词数规划策略 (Flexible Planning Targets)

> 💡 **核心准则**：Prompt length budgets are flexible planning targets, not hard limits. Prioritize information density, subject identity, spatial clarity, and user intent over reaching a fixed word count.  
> 词数预算仅用于规划输出密度，不是硬性限制。当角色身份、服装层级或空间关系需要更多信息时，可以适当超出预算；当任务简单时，应主动缩短。  
> **注意：以下区间用于帮助模型规划信息层次与密度，不得将其作为判断输出是否合格的生硬死线（These ranges serve to guide information density, not as criteria for judging pass/fail）。**

| 任务类型 | 弹性规划参考值 (Planning Target) | 结构重心 |
| :--- | :--- | :--- |
| **头像 / 表情研究 / 快速原型** | **~20 - 45 词** | 极简高敏 Tag 锁定五官、发型、眼神光与基础柔光。 |
| **日常穿搭 / OC 标准立绘** | **~45 - 75 词** | 聚焦服装 4 层叠穿、材质物理特性、站立姿态与接地阴影。 |
| **多尺度展示板 / 多角色插画** | **~70 - 100 词** | 严格区分前景清晰主体与背景放大淡化头像，防止图层混乱。 |
| **电影感叙事场景 / 高定概念图** | **~80 - 120 词** | 融入景深衰减、非对称构图、主光源方向、空气微尘与电影颗粒。 |

---

## 4. Dynamic Aesthetic Routing (美学风格路由)

查阅 `references/anima-aesthetic-deai.md`，按用户明确意图或隐含风格匹配：

- **Preset A · 商业与社交头像**：干净明澈、柔和漫射三点光、自然微表情、浅灰米白柔焦背景。
- **Preset B · 元气甜美与清新日系**：高调漫射光、马卡龙与奶油低饱和暖色、发丝透光金边、生动抓拍神态。
- **Preset C · 高级时尚与极简冷淡**：雕塑感硬侧光、秀场黑白灰/驼色系、非对称解构剪裁、高级厌世疏离视线。
- **Preset D · 暗黑叙事与戏剧张力**：卡拉瓦乔极端暗色调（Tenebrism）、纯黑暗场单束光撕裂、≤5% 唯一刺点色。
- **Preset E · 电影感角色海报**：索尔·雷特雨雾隔窗反光、冷暖色温对抗、35mm 胶片质感、失焦生活时间切片。
- **Default · 中立自然**：用户无特定风格要求时，仅注入物理主光源与布料微观纹理，保持画面干净通透。

---

## 5. Output Modes & Contract (输出模式与契约)

根据用户交互场景选择输出模式：

### 5.1 Direct Mode (单版本直接模式)
- **触发条件**：用户明确要求快速输出、单版提示词或简单快速请求。
- **输出格式**：
  1. 一行策略说明（任务模式 + 美学预设）。
  2. 一个纯英文 Prompt 代码块。

### 5.2 Standard Mode (双版本标准模式 - 推荐默认)
- **触发条件**：用户提供参考图、要求重构还原已有设想、或需要兼顾还原与艺术升华时。
- **输出格式**：
  1. **Strategy Line**：说明当前任务类型与匹配的美学预设。
  2. **V1 Faithful Prompt (忠实还原版)**：尽可能忠实保留用户明确表达的主体、特征、服装、动作和场景信息；允许进行必要的语言转换、顺序整理、消解歧义和结构化装配，但不得主动进行美学升级或添加未经请求的关键设定。
  3. **V2 Enhanced Prompt (美学增强版)**：在 V1 基础上，注入去 AI 味光影、微观物理瑕疵、高级叠穿或电影构图的审美升华版。
     > ⚠️ **关键事实锁定约束**：**V2 不得修改 V1 的关键事实（如发色、瞳色、服装核心款式、指定动作等），除非明确标注为“可选创作变体”。**
  4. **V2 Enhancement Notes**：简述 V2 相较于 V1 在光影/材质/空间上所做的关键艺术优化。

### 5.3 Deep Mode (深度企划模式)
- **触发条件**：复杂 OC 企划、全新世界观角色创立或高定服设。
- **输出格式**：
  1. Input Interpretation (输入理解与核心意图提炼)
  2. Locked Information (锁定的核心信息清单)
  3. Composition Decision (构图与景别决策)
  4. V1 Faithful Prompt 代码块
  5. V2 Enhanced Prompt 代码块（遵循关键事实锁定约束）
  6. Enhancement Notes (增强点解析)
  7. Potential Ambiguity Warnings (潜在冲突或建议实测项)

---

## 6. Verification Checklist (自检清单)

- [ ] 角色核心特征（发色、瞳色、种族）是否与用户输入严格一致？
- [ ] 未确定的细节是否保持了开放，未擅自补全为锁定项？
- [ ] V2 是否忠实守住了 V1 的核心事实，未擅自篡改？
- [ ] 是否根据任务正确选择了美学策略，避免了强行套用阴暗留白模板？
- [ ] 是否执行了 Positive-First 协议，避免无意义的否定修饰？
- [ ] 词数是否合理服务于信息密度与画面清晰度，避免生硬死凑数字？
- [ ] 多角色场景是否做了属性物理绑定与隔离？
- [ ] 输出格式是否严格符合当前选定的 Direct / Standard / Deep 模式契约？
