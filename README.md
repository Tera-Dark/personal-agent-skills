# 个人常用 AI Agent Skill 库 (Personal Agent Skills Hub)

> 🚀 开源、模块化、跨平台通用的个人常用 AI Agent 技能资产库。专为跨 AI 环境（Claude Code / Desktop, Google Antigravity, Cursor, ChatGPT 等）无缝载入与高效调用而设计。

---

## 📖 项目愿景与设计哲学

在不同 AI 平台和工作流中，往往面临以下痛点：
1. **技能提示词臃肿硬编码**：将成百上千行的知识硬塞进单一 Prompt，导致 AI 注意力涣散、生成呆板千篇一律。
2. **多平台割裂**：在 Claude 写好的 Skill，换到 Antigravity 或 GPT 无法复用。
3. **缺乏持续演进能力**：出图或编写中的实测经验无法结构化沉淀。

本项目采用**现代 Agent 架构标准**：
- **主中枢与知识解耦**：`SKILL.md` 仅负责调度逻辑、任务路由与输出契约；专业词表、模型特性与美学策略下沉至 `references/` 按需读取。
- **模块化审美增强**：拒绝单一模板绑架，提供多样化风格预设（商业头像、元气甜美、高级时尚、暗黑戏剧、电影海报等）。
- **纯正向与生产级契约**：保证输出可直接用于生产工作流，消除无效垃圾词。

---

## 🗂 目录架构与技能索引

```text
.
├── README.md                          # 项目全景与跨 AI 接入指引
├── LICENSE                            # MIT 开源协议
├── docs/
│   └── skill-specification.md         # 通用 Skill 编写与贡献标准
│
├── anima-prompt-compiler/             # 【已就绪】Anima 动漫图像提示词编译器
│   ├── SKILL.md                       # 主编译器调度契约与任务路由
│   └── references/                    # 配套专业参考知识库
│       ├── anima-model-profiles.md    # 模型特性、语法权重与实测参数指南
│       ├── anima-fashion-patterns.md  # 叠穿层级、非对称剪裁与高级材质组合
│       ├── anima-composition-patterns.md # 全身/半身景别与多尺度分层展示板协议
│       └── anima-aesthetic-deai.md    # 六大去AI味思维与五大风格预设矩阵
│
└── [预留未来扩展分类]
    ├── midjourney-prompt-compiler/    # Midjourney 专业摄影与插画提示词编译器 (规划中)
    ├── video-director-engine/         # 视频生成分镜与运镜控制编译器 (规划中)
    └── audio-music-generator/         # AI 音乐与音效结构化生成器 (规划中)
```

---

## ⚡ 跨 AI 平台接入指南

### 1. Google Antigravity
本仓库内的技能完全兼容 Antigravity 原生 Skill 协议：
- 将需要的技能目录（如 `anima-prompt-compiler`）软链接或复制到全局技能路径：
  ```bash
  # Windows 示例
  mklink /D "%USERPROFILE%\.gemini\config\skills\anima-prompt-compiler" "path\to\anima-prompt-compiler"
  ```
- 或直接在当前工作区打开本仓库，Antigravity 将自动识别并挂载技能。

### 2. Claude Desktop & Claude Code
- **Claude Code**：在项目根目录启动 `claude`，Agent 将自动阅读 `SKILL.md` 与参考文档。
- **Claude Desktop (Projects)**：
  1. 创建一个新 Project。
  2. 将 `SKILL.md` 及相关 `references/*.md` 添加到 Project Knowledge 中。
  3. 系统指令填入：“作为提示词编译专家，严格依照知识库中的 SKILL.md 与 references 协议执行编译。”

### 3. Cursor / Windsurf
- 将技能放入 `.cursorrules` 或 `.windsurfrules`，或在需要时直接使用 `@anima-prompt-compiler/SKILL.md` 引用当前上下文。

### 4. ChatGPT / 自定义 System Prompt
- 将 `SKILL.md` 内容直接粘贴作为 Custom Instructions 或 GPTs 的 System Prompt。

---

## 🎯 核心技能介绍：anima-prompt-compiler

专为 **Anima 动漫图像模型** 设计的高阶提示词编译器。

### 架构支柱
| 模块 | 引用文件 | 职责定位 |
| :--- | :--- | :--- |
| **模型知识** | `anima-model-profiles.md` | 负责**兼容性**：掌握 Base/Aesthetic/Turbo 差异，控制 CFG 与权重。 |
| **构图协议** | `anima-composition-patterns.md` | 负责**稳定性**：支持全身、半身及特色的“前景立绘 + 背景放大头像”展示板。 |
| **去AI味模块** | `anima-aesthetic-deai.md` | 负责**审美自由增强**：提供 5 大风格预设，拒绝千篇一律的固定模板。 |
| **服设模式** | `anima-fashion-patterns.md` | 负责**质感与穿搭**：提供 4 层叠穿、非对称平衡与高级材质碰撞。 |

### 快速调用示例

**输入示例（用户）**：
> “帮我设计一个浅金短发的少女，穿冬日大衣叠穿围巾，不要背景太乱，要高级一点、有故事感，像电影剧照一样，用 Anima Aesthetic 生成。”

**编译输出示例（Compiler）**：
> `Mode: Character Illustration | Aesthetic: Preset E (Cinematic Auteur)`
> ```text
> 1girl, pale blonde short bob hair, gentle distant gaze, wearing a heavy charcoal wool tailored overcoat over a cream cashmere knit sweater, loose beige cable-knit scarf draped around neck, candid snapshot stance, standing along the right third of the frame, soft natural overcast daylight, subtle rim lighting on hair strands, muted urban street background softly dissolved in shallow depth of field, warm amber and cool slate tone balance, fine 35mm film grain, delicate anime aesthetic lineart
> ```

---

## 🛠 如何扩展新 Skill

欢迎扩充自己的常用技能。请遵循 [Skill 编写与扩展规范](docs/skill-specification.md)：
1. 新建 `[skill-name]/` 目录。
2. 编写具备清晰 YAML 头部的 `SKILL.md`，定义路由与输出规范。
3. 建立 `references/` 目录将庞大知识、语法和经验下沉解耦。
4. 在根目录 `README.md` 中登记索引。

---

## 📄 开源许可证

本项目基于 [MIT License](LICENSE) 开源。
