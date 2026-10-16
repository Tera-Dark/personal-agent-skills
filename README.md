# personal-agent-skills

> Web-first personal creative harness: Aesthetic / Blueprint Gates → shared Visual Prompt Core → target-model renderers. Includes optional Artist Eye research, reusable taste feedback, selective Danbooru verification, and FULL / AUDIT / FAST VARIANT / PROMPT ONLY modes.

> ## ⚡ AI bootstrap
>
> 1. Fetch and read: https://raw.githubusercontent.com/Tera-Dark/personal-agent-skills/main/bundle/HARNESS.md
> 2. Operate under it. Do not clone, install, summarize, or describe the repository during normal web use.
> 3. Follow the handshake specified by the harness, then work on the user's task.
>
> If URLs are inaccessible, reply exactly: \`我无法访问链接。请把 bundle/HARNESS.md 的内容粘贴给我。\`

## Defaults for this owner

- **Design / OC / illustration request → prompt or written design, not automatic image generation.** Only an explicit request to generate/edit an image authorizes an image tool.
- **NAI5 latest confirmed default (2026-10-15) → one copyable English positive prompt, no fixed artist stack / year / quality / Negative.** Users can still explicitly request an artist stack or complete configuration. Prompt-only: never generate images without clear instruction.
- **PROMPT ONLY** governs visible output rather than internal design depth. Simple edits use FAST VARIANT; substantive original work uses FULL.
- Web use needs only the GitHub URLs. Build scripts run locally or in CI.

## 🧭 工作流总览 · Workflow Map

> **一条共享创作主线，多种模型输出。** 设计在前、编译在后；参考研究和审美模块按需参与，不会替代最终设计负责人。下图由 GitHub 原生 Mermaid 渲染，无需额外图片或外部服务。

### ① 从想法到 Prompt

```mermaid
flowchart TB
    INPUT(["用户需求 · OC / IP · 参考图 · 锁定条件"])
    INPUT --> KERNEL["Kernel + Identity<br/>运行规则 · 个人审美 · 禁区"]
    KERNEL --> ROUTER{"Creative Router<br/>识别任务与执行模式"}

    ROUTER -->|"原创创作 · FULL"| DIRECTOR["Aesthetic Director<br/>创意命题 · 三案比较 · 淘汰平庸"]
    ROUTER -->|"现有方案 · AUDIT"| AUDIT["Design Audit<br/>审核方案 · 保留已定事实"]
    ROUTER -->|"定向修订 · FAST VARIANT"| FAST["Fast Variant<br/>只修改指定部分"]

    REFERENCE["Image Reverse Analysis<br/>参考图 → 可迁移的结构"] -.-> DIRECTOR
    EYE["Artist Eye · 按需<br/>电影 / 动画 / 绘画 / 版式跨媒介判断"] -.-> DIRECTOR

    DIRECTOR --> SPECIALIST{"Blueprint 类型"}
    AUDIT --> SPECIALIST
    FAST --> SPECIALIST
    SPECIALIST -->|"角色 / 服装"| CHARACTER["Character Design Engine<br/>外形 · 服设 · 动作因果"]
    SPECIALIST -->|"插画 / 海报 / 场景"| ILLUSTRATION["Illustration Direction<br/>机位 · 构图 · 叙事 · 光色"]

    SMALL["小画师脑 · 按需<br/>美型 · 关系 · 疏密"] -.-> ILLUSTRATION
    CAMERA["日系电影感构图思维摄影脑 · 按需<br/>观察立场 · 瞬间 · 触点"] -.-> ILLUSTRATION

    CHARACTER --> BLUEPRINT{"Blueprint Gate<br/>核对设计与身份锁"}
    ILLUSTRATION --> BLUEPRINT
    BLUEPRINT -->|"PASS"| CORE["Visual Prompt Core<br/>共享视觉事实 · 空间关系 · 压缩"]
    BLUEPRINT -.->|"需重做核心决定"| DIRECTOR

    CORE --> TARGET{"选择目标模型"}
    TARGET -->|"NAI5 / Anima"| GATE["Danbooru Tag Gate<br/>必要时校验身份与标签"]
    GATE -->|"NovelAI V5"| NAI5["NAI5 Renderer<br/>Tags · 多角色分槽"]
    GATE -->|"Anima"| ANIMA["Anima Renderer<br/>Tags + Natural Language"]
    TARGET -->|"其他图像模型"| GENERIC["General Adapter<br/>目标模型自然语言"]

    NAI5 --> OUTPUT(["交付 Prompt / 设计稿"])
    ANIMA --> OUTPUT
    GENERIC --> OUTPUT
```

**读图方式：** 实线表示主要执行顺序，虚线表示按需提供参考、增强决策或退回修改。**PROMPT ONLY 只是输出简化模式**，不会跳过 Aesthetic / Blueprint Gate；默认交付文本，只有明确要求生成或编辑图片时才调用生图工具。技术任务（ComfyUI、LoRA、数据集）由 Router 直接交给相应技术模块，不强行经过插画设计链路。

### ② 成图反馈如何改善下一次创作

```mermaid
flowchart TB
    FEEDBACK(["用户反馈 · 出图对比 · 修改要求"]) --> EVAL["Evaluation Loop<br/>识别第一个失败层 · 拆分好坏反馈"]
    EVAL --> FIX["对应设计 / 分析 / Renderer owner<br/>只改失败变量"]
    FIX --> NEXT(["下一版设计 / Prompt"])
    EVAL --> SESSION["Session State<br/>锁定本轮已经认可的部分"]
    SESSION --> NEXT

    EVAL -.->|"用户允许持久同步"| EVIDENCE["Feedback Evidence<br/>限定题材与作用域 · 记录来源"]
    EVIDENCE --> REVIEW{"Review<br/>证据足够且无反证？"}
    REVIEW -->|"暂不晋升"| CANDIDATE["候选规则 · 保留待验证"]
    REVIEW -->|"经审阅确认"| PROMOTE["Promote + Digest<br/>写入 Identity 的已批准偏好"]
    PROMOTE -.->|"新会话按需加载"| NEXT
```

**反馈闭环 ≠ 自动训练模型：** 当轮评价可以直接影响下一稿；跨会话持久化需要已授权的写入、证据审阅与显式晋升。实验性构图和个人喜好不会因为一次好评被自动升级为所有作品的默认规则。

### ③ 工作模式速览

| 模式 | 什么时候用 | 会做什么 |
|---|---|---|
| **FULL CREATIVE** | 新 OC、新插画、海报、需要新概念 | 研究 → 多方案比较 → Director → Blueprint → 模型编译 |
| **AUDIT** | 用户已经给出完整设计 / 原设 / 参考还原 | 尊重锁定事实，仅补足必要的校验 |
| **FAST VARIANT** | 「只改构图 / 表情 / 配色」 | 锁住其他变量，仅修指定部分；触及核心命题则升级 FULL |
| **PROMPT ONLY** | 「只给提示词，一整块复制」 | 隐藏内部方案和评审，仅显示最终可复制提示词；不跳关 |

## 版本与提交记录

建议按 [Changelog](CHANGELOG.md) 阅读功能版本演进。源代码集中维护在各 Skill 中，`bundle/` 为自动构建产物；主分支开发建议使用 **PR + squash merge**，减少连续小修和自动构建记录带来的干扰。历史提交保留可追溯性，详见 [版本管理规范](docs/versioning.md)。

## Latest cross-session taste sync (2026-10-15)

The owner's Oct 14–15 feedback is summarized in [scoped session evidence](00_core/personal-identity-profile/references/session-feedback-2026-10-14-15.md) and promoted where warranted into [Taste Signature](00_core/personal-identity-profile/references/taste-signature.md), [Dislikes](00_core/personal-identity-profile/references/design-dislikes.md), [Illustration Direction](02_design/illustration-direction/SKILL.md), and [NAI5 Renderer](03_prompt/nai5-renderer/SKILL.md). Crucial distinctions: prompt-only not images; externally fixed artist/quality; canon-first fan art; real camera geometry & interaction; optional experimental material-fusion; Suzuran floral reference as scoped positive evidence rather than universal cherry blossoms.

## 高度个人化 QoL：正常聊天就能学习

> v4.8 起增加“偏好证据 → 当前稿改进 → 持久晋升”的闭环；自然语言优先，不需要学一套命令。

| 你直接说 | Skill 应该做什么 |
|---|---|
| “这张 9 分，光影绝了但脸不好看” | 拆成正负反馈，下一稿保留光影，只修脸 |
| “这个不错，再来个别的情景” | 保留已认可的镜头机制，设计新的事件，而不是重复模板 |
| “只改镜头/衣服/配色” | FAST VARIANT，只变指定维度 |
| “上一版更好，退回去” | 回滚失败改动，保留上个好球版本 |
| “以后都这样，记住” | 优先更新当前规则；根据作用域进入持久偏好候选与晋升流程 |
| “同步今天的偏好到 Skill” / `/learn sync` | 有已授权 GitHub 写权限时更新证据账本与有效规则；没有权限就导出待同步补丁 |
| “最近学到了什么” / `/learn status` | 说明本会话候选、已经升级的规则，以及哪些尚未真正持久化 |
| “把偏好导出来” / `/learn export` | 给单块 Markdown，用于网页端跨对话续作 |

**边界：** 仅凭新对话贴 GitHub 链接，只能读取仓库已提交的长期偏好；它不会自动把所有聊天反馈写进 GitHub。真正跨会话持久化需要已连接、可写的 GitHub 工具及用户允许，或主动执行一次导出/同步。只存创作偏好的抽象摘要，不存个人私密信息或原始图片；模型参数/LoRA 不会自行训练。

详见 [反馈晋升协议](00_core/personal-identity-profile/references/feedback-learning-loop.md)、[反馈证据账本](00_core/personal-identity-profile/references/feedback-ledger.md)、[高频操作 QoL](01_router/creative-skill-router/references/conversation-qol.md)、[学习回归测试](tests/feedback-learning-regression.md)。

## v4.9 可执行的个人学习与跨会话接力

**不是自动训练模型，而是带证据、能撤销的审美学习引擎。** 现在可以将你跑图后的具体评价整理成一条 JSON，利用纯 Python 标准库进行去重、候选评审、偏好晋升、撤销和跨会话续作；下次创作时按需使用已经批准的偏好摘要。CI 会运行相关行为测试。

```bash
# 在仓库目录下。首次记录：feedback.json 放的是抽象化的短评价，不是完整聊天或图片
python3 scripts/learn.py record --file feedback.json
python3 scripts/learn.py review
# 达到“用户明确要求长期默认”或 >=3 份独立支持，且无反证，经过审核才能启用
python3 scripts/learn.py promote film.non_template_camera
python3 scripts/learn.py digest
python3 scripts/learn.py validate

# 跨会话保存/读取、对比锁定事实
python3 scripts/learn.py session-save my-oc-v1 --file state.json
python3 scripts/learn.py session-load my-oc-v1
python3 scripts/learn.py session-list
python3 scripts/learn.py session-diff my-oc-v1 my-oc-v2
```

不用本地 Python 的网页用户仍然可以通过**已授权的 GitHub 写入连接**让 AI 进行等价的读写与审阅；单独贴仓库链接只有读取能力，不代表会记录聊天。仓库可能公开，请勿提交密钥、完整聊天或私密图稿。详见 [学习引擎说明](data/learning/README.md) 和 [七维验收表](docs/experience-scorecard.md)。

## What this is

一个给 ChatGPT / Gemini / Claude 等对话模型使用的创作 harness：kernel 定义运行契约，设计层负责做决定，Prompt Core 把设计转换成模型无关的 Visual Prompt Packet，最后由 Anima / NAI5 / Generic renderer 做模型语法。

核心原则：

> **设计统一，提示词规划统一，模型语法最后才分叉。**

因此 Anima 与 NAI5 不再拥有两套平行的创作逻辑。两者共享：
- 用户长期审美
- Aesthetic / Blueprint Gate
- Character / Illustration Blueprint
- Style / Quality planning
- Danbooru identity verification
- Prompt compression
- Design Lock

只在最终 Renderer 层处理各自语法。

## Use it

| 场景 | 做法 |
|---|---|
| ChatGPT / Gemini / Claude | 新对话发仓库链接；入口加载精简 Harness，按任务读取模块契约与单独参考文件 |
| 无联网 / 粘贴 | 把 \`bundle/HARNESS.md\` 全文粘贴 |
| 自定义 GPT / Gemini Gem / Claude Project | 上传 \`bundle/HARNESS-FULL.md\` |
| Claude Code / Codex / Cursor | \`scripts/install.sh [target]\` |
| 加功能 | 使用 \`/new-module\`，遵循 \`kernel/EXTENSION-PROTOCOL.md\` |

## Architecture

完整图见上方 [工作流总览](#-工作流总览--workflow-map)。核心原则：**Identity / Director / Blueprint 分别负责偏好、决策与设计；Prompt Core 负责共享视觉事实，Tag Gate 负责标签证据，Renderer 只处理目标模型格式。**

### Source layers

\`\`\`
00_core      identity + aesthetic direction
01_router    intent → owner
02_design    character / illustration design
03_prompt    Visual Prompt Core + tag gate + renderers
04_analysis  reference / prompt analysis
05_tools     ComfyUI / dataset / LoRA
06_evaluation feedback diagnosis
07_extensions future owner-specific extensions
\`\`\`

### Xiao-artist aesthetic module (on demand)

`02_design/small-artist-brain/` is an independent taste-to-design decision module grounded in 16 user-supplied ZHENG (蒸蒸) illustration studies. It adds concrete character vitality, camera, color-mass, and density choices **between the Director and design specialists**; original images are not redistributed. It is not a renderer or a universal aesthetic gate. See [SKILL.md](02_design/small-artist-brain/SKILL.md) and its on-demand references.

### 日系电影感构图思维（按需）

 `02_design/japanese-cinematic-composition/` 从用户提供的九张及追加十三份摄影参考里提取通用镜头规律（注意重复与拼贴样本，绝不把它们算作独立验证），不保存或转载原图。**提炼观看立场、决定性瞬间、人体接触点、前景遮挡、物件因果、真实光源与大色块**，形成 Photography Decision Sheet。

示例对话：「用日系电影感构图思维，给我写一张 NAI5 古风恋人诀别的电影感提示词」。路由是 **摄影 Skill（机位与瞬间建议） → illustration-direction（设计与 Blueprint Gate） → Visual Prompt Core → Danbooru Tag Gate → NAI5 renderer**。最终仍遵守用户默认纯英文、紧凑正向提示词、无需画师串/质量词/Negative，以及不自动生成图像。模块也可为其他模型提供摄影思考，但不拥有任何模型语法。

- [Skill 入口](02_design/japanese-cinematic-composition/SKILL.md)
- [九张参考图逐帧分析](02_design/japanese-cinematic-composition/references/nine-frame-study-2026-10-14.md)\n- [追加十三份参考逐图研究](02_design/japanese-cinematic-composition/references/thirteen-frame-study-2026-10-15.md)\n- [镜头决策矩阵与 NAI5 提示词反污染](02_design/japanese-cinematic-composition/references/camera-decision-matrix.md)
- [跨题材镜头迁移与 A/B 验证](02_design/japanese-cinematic-composition/references/cross-genre-camera-recipes.md)

### NAI5 experiments → reliable controls

For NovelAI V5, use the fast `03_prompt/nai5-renderer/references/nai5-control-matrix.md` before the full long-form field guide. The matrix maps common failures to concrete camera evidence, motion/POV tags, optional **Positive Prompt** negative weights, light-source controls, identity risks, and A/B diagnostics. This adapter does **not** override creative design decisions or affect Anima syntax. Reported source experiments are not treated as our own verified generations.

### Ownership invariants

- **Taste has one home** — \`personal-identity-profile\`.
- **Design has one owner per level** — Director chooses the direction; Character / Illustration specialists expand it.
- **Shared prompt logic has one home** — \`visual-prompt-core\`.
- **Danbooru identity has one home** — \`danbooru-tag-gate\`.
- **Model syntax has one owner per target** — Anima / NAI5 / Generic renderer.
- **Evaluation diagnoses; it does not redesign.**
- **bundle/** is generated. Edit source files, then rebuild.

## Develop

\`\`\`bash
python3 scripts/validate_skills.py
python3 scripts/build.py
python3 scripts/validate_skills.py --check-bundle
\`\`\`

License: MIT


## Web runtime and selective references

- `bundle/HARNESS.md` is the compact cold-start contract, not the full knowledge archive.
- `bundle/modules/<name>.md` contains one module's execution contract plus links to its detailed references.
- `bundle/references/<module>/...` contains generated single-reference files. Fetch only those needed by the current task.
- `bundle/HARNESS-FULL.md` remains the complete self-contained option for a Custom GPT / Gem / Project that needs everything embedded.
- Danbooru hard tags use the generated root/group manifests and group-aware prefix shards under `bundle/tag-index/`; artists use three routing characters to control alias-heavy shard sizes, other groups use two. The full upstream index is a build-time input, not a web runtime dependency.
- The configured Core token estimate is a hard build gate. CI rejects a cold-start bundle that exceeds `harness.json:core_budget_tokens`.
