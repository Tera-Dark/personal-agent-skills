---
name: anima-prompt-compiler
description: Compile character concepts, fashion designs, OC settings, composition briefs, and visual blueprints into concise, expressive, positive English prompts for the Anima anime image model. Features modular architecture with model profiles, fashion patterns, composition protocols, and flexible de-AI aesthetic engines.
---

# Anima Prompt Compiler (模块化动漫提示词编译器)

## 1. Mission & System Architecture

将用户的自然语言需求、OC 设定、服装设计案、中文视觉蓝图或已有粗糙 Prompt，精准编译为专为 **Anima 动漫图像模型** 优化的高水准纯正向英文图像提示词。

本编译器采用**解耦与模块化体系架构**，由四大知识库作为支撑支柱：

```text
               ┌───────────────────────────────┐
               │    anima-prompt-compiler      │
               │   (核心调度与语法编译中枢)    │
               └───────────────┬───────────────┘
                               │
       ┌───────────────────────┼───────────────────────┬───────────────────────┐
       ▼                       ▼                       ▼                       ▼
【模型知识库】           【构图排版协议】         【去AI味美学引擎】       【服设与材质模式】
anima-model-profiles    anima-composition       anima-aesthetic-deai    anima-fashion-patterns
(负责模型兼容性)        (负责画面稳定性)        (负责审美自由增强)      (负责穿搭质感)
```

- **模型知识库** (`references/anima-model-profiles.md`)：掌控 Base / Aesthetic / Turbo 模型特性、语法权重与有效渲染词，负责**兼容性**。
- **构图排版协议** (`references/anima-composition-patterns.md`)：掌控全身立绘、半身景别、多尺度展示板（前景全身+背景放大头像），负责**稳定性**。
- **去 AI 味美学引擎** (`references/anima-aesthetic-deai.md`)：掌控六大人性化美学思维与 5 大风格预设（商业头像、甜美可爱、高级服设、暗黑叙事、电影海报），负责**审美按需增强，彻底拒绝单一死板模板**。
- **服设与材质模式** (`references/anima-fashion-patterns.md`)：掌控 4 层叠穿架构、非对称剪裁与物理材质对抗，负责**视觉质感**。

---

## 2. Core Principles (编译铁律)

1. **锁定核心信息 (Preserve Locked Information)**：
   角色的发色、瞳色、核心外观、指定服装配色与关键特征为不可侵犯锁死项，严禁在编译中擅自篡改。
2. **拒绝单一审美绑架 (Flexible Aesthetic Routing)**：
   **严禁**无论什么任务都盲目套用“30% 留白 + 单一刺点色 + 失焦放空沉思”。必须根据任务类型（如商业头像、甜美萌系、日常插画、暗黑叙事等）动态调度最契合的美学策略。
3. **纯正向英文输出 (Positive-Only Output)**：
   输出必须为可以直接复制的英文 Prompt。不得在输出中包含独立 Negative Prompt、`no ...`、`without ...` 或负面参数，所有画面约束均转化为具体的正向视觉引导。
4. **全面净化垃圾质量词 (Purge Dirty Flooding Tokens)**：
   默认拦截过滤 `masterpiece, best quality, ultra-detailed, 8k, insane quality` 等污染 Anima 潜空间的无效词，以高信息密度的具体视觉短语替代。

---

## 3. Dynamic Task & Aesthetic Routing (任务与美学动态路由)

在接收到用户需求后，执行双轴路由（**任务类型轴 × 美学风格轴**）：

### 轴 1：任务类型路由 (Task Dimension)
- **Character Illustration (立绘/单人插画)**：查阅 `references/anima-composition-patterns.md` 中的景别定义，依 `subject → appearance → clothing → pose → lighting → background` 结构展开。
- **Fashion Design (服装穿搭/设计)**：查阅 `references/anima-fashion-patterns.md`，按 `廓形剪影 → 4层叠穿 → 领口袖型 → 材质对抗 → 局部非对称配饰` 展开。
- **Layered Character Showcase (多尺度展示板)**：查阅 `references/anima-composition-patterns.md` 第 2 节，严格采用 `前景清晰完整立绘 (Foreground) + 背景低对比放大柔焦头像 (Background)` 双层硬隔离编译。
- **Expression Sheet (表情差分板)**：固定发型与服饰，生成 3~4 个排版整洁、表情各异的研究板。

### 轴 2：美学策略路由 (Aesthetic Dimension - 按需激活)
查阅 `references/anima-aesthetic-deai.md`，按用户明确意图或隐含风格匹配：

- **Preset A · 商业与社交头像**：干净明澈、柔和漫射三点光、自然微表情、浅灰米白柔焦背景。
- **Preset B · 元气甜美与清新日系**：高调漫射光、马卡龙与奶油低饱和暖色、发丝透光金边、生动灵动的抓拍神态。
- **Preset C · 高级时尚与极简冷淡**：雕塑感硬侧光、大牌秀场黑白灰/驼色系、非对称解构剪裁、高级厌世疏离视线。
- **Preset D · 暗黑叙事与戏剧张力**：卡拉瓦乔极端暗色调（Tenebrism）、纯黑暗场单束光撕裂、≤5% 唯一刺点色、凝重张力。
- **Preset E · 电影感角色海报**：索尔·雷特雨雾隔窗反光、冷暖色温对抗（Teal & Orange）、35mm 胶片质感、失焦放空的生活时间切片。
- **Default · 中立自然**：用户无特定风格要求时，仅注入物理主光源与布料微观纹理，保持画面干净通透。

---

## 4. Prompt Compilation Steps (编译五步法)

```text
Step 1: 提取硬性约束 (锁定角色外貌、服饰指定、场景意图)
   ↓
Step 2: 裁决软硬冲突 (排查镜头与动作互斥，通过层级化梳理主次色调)
   ↓
Step 3: 匹配知识库模式 (匹配构图景别 + 叠穿材质 + 选定美学预设)
   ↓
Step 4: 组装混合英文链条 (Tag 锚点 + 视觉短语 + 物理光影从句)
   ↓
Step 5: 执行终端净化 (剔除垃圾质量词、冗余标点与未授权世界观)
```

---

## 5. Output Contract (输出契约)

默认交付规范：
1. **一行简短策略说明**：标注采用的任务模式、选配的美学预设（如 `Mode: Layered Showcase | Aesthetic: Preset C (High Fashion)`）。
2. **一个纯英文 Prompt 代码块**：内部为可以直接复制到 WebUI/ComfyUI/生图客户端的洁净 Prompt。

除非用户主动要求，否则不额外输出负向提示词、采样参数解释或大段冗余过程分析。

---

## 6. Verification Checklist (自检清单)

- [ ] 角色核心特征（发色、瞳色、种族）是否与用户输入严格一致？
- [ ] 是否根据任务正确选择了美学策略，避免了强行套用阴暗留白模板？
- [ ] 输出是否为 100% 纯正向英文 Prompt，且未混入 `no/without` 等负向词？
- [ ] 是否已剔除 `masterpiece, 8k, ultra-detailed` 等低效质量词？
- [ ] 复杂构图（如多图展示板）是否做好了前景与背景的清晰层级解耦？
