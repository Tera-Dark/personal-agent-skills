# 个人常用 AI Agent Skill 库 (Personal Agent Skills Hub)

> 🚀 模块化、结构化、跨平台通用的个人常用 AI Agent 技能资产库。专为不同 AI 环境（Claude Code / Desktop, Google Antigravity, Cursor, ChatGPT 等）无缝载入与高效调用而设计。

---

## 📖 项目愿景与设计哲学

在不同 AI 平台和日常工作流中，往往面临以下痛点：
1. **技能提示词臃肿硬编码**：将成百上千行的知识硬塞进单一 Prompt，导致 AI 注意力涣散、输出僵化呆板。
2. **多平台移植割裂**：平台间机制各异，缺乏统一的可移植设计。
3. **缺乏持续演进与证据体系**：主观偶发经验与客观模型规律混为一谈，导致规则失真。

本项目采用**现代 Agent 架构标准**：
- **中枢与参考解耦**：`SKILL.md` 专精于调度逻辑、任务路由、分级输出契约；专业词表、模型特性与美学策略下沉至 `references/` 按需加载。
- **证据分级体系 (Evidence Levels)**：知识库清晰标明 Official（官方确认）、Community Practice（社区共识）与 Personal Experiment（特定实验），拒绝将单一条件下的偶然结果固化为模型定律。
- **模块化审美增强**：拒绝单一模板绑架，提供多样化风格预设（商业头像、元气甜美、高级时尚、暗黑戏剧、电影海报等）。
- **生产级 V1 / V2 输出机制**：提供忠实还原版 (V1) 与美学增强版 (V2) 对照输出，满足多场景出图需求。

---

## 🗂 目录架构与技能索引

```text
.
├── README.md                          # 项目全景与跨 AI 接入指引
├── LICENSE                            # MIT 开源协议
├── CHANGELOG.md                       # 版本与规则演进记录
├── docs/
│   └── skill-specification.md         # 通用 Skill 编写与贡献标准
├── tests/
│   └── test-suite.md                  # 核心测试集（8组覆盖构图、叠穿、隔离与约束的验证样例）
│
├── anima-prompt-compiler/             # 【已就绪】Anima 动漫图像提示词编译器
│   ├── SKILL.md                       # 主调度中枢（任务路由、V1/V2契约）
│   └── references/                    # 配套专业参考知识库
│       ├── anima-model-profiles.md    # 模型特性、语法权重与实测参数指南 (含证据分级)
│       ├── anima-fashion-patterns.md  # 4层叠穿、非对称剪裁与高级材质碰撞
│       ├── anima-composition-patterns.md # 全身/半身景别与多尺度分层展示板协议
│       ├── anima-aesthetic-deai.md    # 六大去AI味思维与五大风格预设矩阵
│       └── anima-troubleshooting.md   # 常见崩图、服装融合与多主体串线排查
│
└── [预留未来扩展分类]
    ├── midjourney-prompt-compiler/    # Midjourney 专业摄影与插画提示词编译器 (规划中)
    ├── video-director-engine/         # 视频生成分镜与运镜控制编译器 (规划中)
    └── audio-music-generator/         # AI 音乐与音效结构化生成器 (规划中)
```

---

## ⚡ 跨 AI 平台接入指南

> **关于平台兼容性的说明**：  
> 本项目采用 Markdown + YAML 的便携式设计，但不同 AI 客户端对技能的自动发现、加载路径和执行机制可能存在差异，请根据具体平台进行验证。  
> *(The skill is designed around portable Markdown and YAML conventions. Platform-specific discovery and automatic loading behavior may vary. Users should verify the installation path and loading behavior of their chosen client.)*

### 1. Google Antigravity
本仓库遵循标准技能结构设计：
- 将需要的技能目录（如 `anima-prompt-compiler`）软链接或复制到全局技能路径：
  ```bash
  # Windows 示例
  mklink /D "%USERPROFILE%\.gemini\config\skills\anima-prompt-compiler" "path\to\anima-prompt-compiler"
  ```
- 或直接在 Antigravity 工作区中打开本仓库，即可引用相关技能。

### 2. Claude Desktop & Claude Code
- **Claude Code**：在项目根目录启动 `claude`，Agent 可按需阅读 `SKILL.md` 与参考文档。
- **Claude Desktop (Projects)**：
  1. 创建新 Project。
  2. 将 `SKILL.md` 及对应 `references/*.md` 添加至 Project Knowledge。
  3. 系统指令中配置：“请作为提示词编译专家，依照知识库中的 SKILL.md 与 references 协议执行编译。”

### 3. Cursor / Windsurf
- 可将技能配置加入 `.cursorrules` / `.windsurfrules`，或在需要时直接通过 `@anima-prompt-compiler/SKILL.md` 引用上下文。

### 4. ChatGPT / 自定义 System Prompt
- 将 `SKILL.md` 作为 Custom Instructions 或 GPTs System Prompt 载入。

---

## 🎯 核心技能介绍：anima-prompt-compiler

专为 **Anima 动漫图像模型** 设计的高阶提示词编译器。

### 架构支柱
| 模块 | 引用文件 | 职责定位 |
| :--- | :--- | :--- |
| **模型知识** | `anima-model-profiles.md` | **兼容性**：掌握 Base/Aesthetic/Turbo 特性，引入证据分级与客观参数建议。 |
| **构图协议** | `anima-composition-patterns.md` | **稳定性**：支持全身、半身及特色的“前景立绘 + 背景放大头像”展示板。 |
| **去AI味模块** | `anima-aesthetic-deai.md` | **审美自由增强**：提供 5 大风格预设，拒绝千篇一律的固定模板。 |
| **服设模式** | `anima-fashion-patterns.md` | **质感与穿搭**：提供 4 层叠穿、非对称平衡与高级材质碰撞。 |
| **异常排查** | `anima-troubleshooting.md` | **排查与修正**：排查肢体崩溃、服装融合、背景抢主体与多角色串线。 |

### 输出调用展示

**Standard Mode 示例（双版本标准模式）**：

> **Mode**: Character Illustration | **Aesthetic**: Preset E (Cinematic Auteur)
>
> **V1 (Faithful)**:
> ```text
> 1girl, pale blonde short hair, wearing a dark coat and cream scarf, standing outdoors, street background
> ```
>
> **V2 (Enhanced)**:
> ```text
> 1girl, pale blonde bob haircut, gentle contemplative gaze, wearing an oversized charcoal wool tailored overcoat layered over a cream knit sweater, chunky beige scarf loosely draped around neck, candid stance along the right third of the frame, soft natural overcast daylight, subtle rim lighting on hair strands, muted urban street background softly dissolved in shallow depth of field, warm amber and slate tone balance, fine 35mm film grain
> ```
>
> **V2 Enhancement Notes**:
> - 将基础外套升级为重呢大衣与针织内搭的质感叠穿；
> - 采用右侧三分偏置构图与大光圈浅景深，压低背景密度；
> - 注入阴天漫射侧光与 35mm 胶片微观颗粒，提升电影叙事张力。

> ⚠️ **关于示例的说明 (Illustrative Note)**：  
> 本示例仅作为格式与视觉呈现参考，非强制性固定提示词模板。编译器会根据用户输入的具体诉求，动态调整 Tag 密度、句式结构、构图景别与美学处理方案。  
> *(The example is illustrative rather than a mandatory prompt template. The compiler may change tag density, sentence structure, composition, and aesthetic treatment according to the user's request.)*

---

## 🛠 如何扩展新 Skill

欢迎扩充自己的常用技能。请遵循 [Skill 编写与扩展规范](docs/skill-specification.md)：
1. 新建 `[skill-name]/` 目录；
2. 编写具备清晰 YAML 头部的 `SKILL.md`，明确路由、任务类型与输出契约；
3. 建立 `references/` 目录将庞大知识、语法和经验下沉解耦；
4. 在根目录 `README.md` 中登记索引。

---

## 📄 开源许可证

本项目基于 [MIT License](LICENSE) 开源。
