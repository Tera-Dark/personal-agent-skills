# personal-agent-skills

> v4.6 architecture: mandatory Aesthetic/Blueprint Gates + shared Visual Prompt Core + shared Danbooru verification + thin Anima / NAI5 renderers + Web-first runtime. Runtime bundle optimization: compact identity, selective tag shards, reference-level fetching, and explicit FULL / FAST VARIANT / PROMPT ONLY modes.

> ## ⚡ AI bootstrap
>
> 1. Fetch and read: https://raw.githubusercontent.com/Tera-Dark/personal-agent-skills/main/bundle/HARNESS.md
> 2. Operate under it. Do not clone, install, summarize, or describe the repository during normal web use.
> 3. Follow the handshake specified by the harness, then work on the user's task.
>
> If URLs are inaccessible, reply exactly: \`我无法访问链接。请把 bundle/HARNESS.md 的内容粘贴给我。\`

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

\`\`\`
Kernel
  │
  ▼
Identity ── persistent taste / dislikes / artist pool
  │
  ▼
Router
  │
  ├───────────────┬─────────────────┐
  ▼               ▼                 ▼
Design          Analysis        Technical
  │               │
  ├─ Character    ├─ Image Reverse
  └─ Illustration └─ Prompt Analysis
  │
  ▼
Visual Prompt Core
  ├─ Style / Quality
  ├─ Visual facts
  ├─ Composition / Scene
  ├─ Relations
  ├─ Compression
  ├─ Design Lock
  └─ Output Policy
  │
  ▼
Danbooru Tag Gate
  │
  ├───────────────┬────────────────┐
  ▼               ▼                ▼
Anima          NAI5             Generic
Renderer       Renderer         Renderer
  │               │
Tag + NL      Community Tags
\`\`\`

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
