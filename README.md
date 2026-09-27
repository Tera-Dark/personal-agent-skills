# Personal Agent Skills Hub

> Personal AI Creative Operating System
>
> 面向长期创作工作流的模块化 Agent Skill 仓库。
> 目标：让 AI 先**做决定**，再写提示词——而不是把每个槽位填上最可能的值。

---

## Why this exists

AI 味不是渲染问题，是决策方式问题。模型在每个槽位里填最常见的答案：银发、红瞳、黑裙、优雅地站着、看向镜头、神秘的氛围。每一项都"对"，合起来没有人。

这个仓库把人类设计师的决策路径拆成可执行的步骤——找到一个痴迷点、否决自己的前几个想法、建立因果、做减法、留一处怪——并强制在任何 prompt 产生之前走完。模型适配器只负责翻译。

---

## Architecture

```
User Request
    │
    ▼
01_router      creative-skill-router          分类意图，组装管线
    │
    ▼
00_core        personal-identity-profile      这是给谁做的 → 品味签名、否决清单、说话方式
               aesthetic-director-core        这个设计是关于什么的 → Creative Brief
                                              （命题 / 矛盾 / 轮廓策略 / 因果 / 瞬间 / 密度图 / 刺点 /
                                                留下的怪 / 删掉的东西 / 否决的方向）
    │
    ▼
02_creation    character-design-engine        Brief → 角色 blueprint（与模型无关）
               illustration-direction         Brief → 画面 blueprint（与模型无关）
    │
    ▼
02_creation    anima-prompt-compiler          blueprint → Anima Tag + NL
               nai5-community-prompt-engineering   blueprint → NAI5 社区格式
    │
    ▼
05_evaluation  evaluation-loop                哪一层失败 → 只改那一层，单变量

side:  03_analysis  image-reverse-analysis · prompt-analysis
       04_tools     comfyui-workflow · lora-training · dataset-management  (placeholders)
```

核心不变量：

- **品味只有一个家**：`personal-identity-profile`。适配器不维护自己的"个人审美规则"。
- **适配器不设计**：收到的不是 blueprint（没有带动词的命题、轮廓、四层服装、一个刺点、锁定事实）就退回。
- **设计知识与模型无关**，放在 `00_core` / `02_creation` 的设计 Skill 里，所有适配器共用。
- **反馈是关于某一层的证据**，不是加装饰的许可。
- Skill 之间**按名字引用**，不按相对路径。

---

## Repository structure

```
.
├── 00_core/
│   ├── personal-identity-profile/     taste-signature · design-dislikes · visual-preferences · business-objectives · workflow-style
│   └── aesthetic-director-core/       creative-moves · taste-calibration-pairs · feedback-diagnosis · anti-ai-patterns · emotional-design · design-calibration-examples
├── 01_router/
│   └── creative-skill-router/
├── 02_creation/
│   ├── character-design-engine/       oc-design-system · garment-lexicon
│   ├── illustration-direction/        composition-patterns · atmosphere-presets
│   ├── anima-prompt-compiler/         anima-model-profiles · anima-troubleshooting
│   └── nai5-community-prompt-engineering/
├── 03_analysis/
│   ├── image-reverse-analysis/
│   └── prompt-analysis/
├── 04_tools/                          (placeholders)
├── 05_evaluation/
│   └── evaluation-loop/
├── docs/                              architecture · skill-registry · skill-specification · versioning
├── scripts/                           validate_skills.py · install.sh
└── tests/                             test-suite.md
```

---

## Install

Agent runtimes usually discover skills one directory deep. The numbered layers are for humans; `scripts/install.sh` flattens them with symlinks:

```bash
scripts/install.sh                    # → ~/.claude/skills
scripts/install.sh ~/.agents/skills   # → Codex
scripts/install.sh ./.claude/skills   # → project-local
```

Validate before committing:

```bash
python3 scripts/validate_skills.py
```

---

## How a request flows (example)

> 「设计一个有创意的原创女性角色，出 Anima 提示词。」

1. `creative-skill-router` → 创作类，且概念不存在 → 全管线。
2. `personal-identity-profile` → 签名：精致的基底上，一处怪，一点危险。
3. `aesthetic-director-core` → 三个方向，否决两个，输出 Brief：「守夜的女祭司正在用自己的头发给一盏快灭的灯添捻」。
4. `character-design-engine` → 轮廓策略、锚点、四层服装、材质对抗、配色层级、姿势因果、叙事残留、展示方式、减法。
5. `anima-prompt-compiler` → Tag block + NL block，V1 忠实 / V2 增强。
6. 用户说「太平淡」→ `evaluation-loop` 诊断在哪一层 → 回到那一层，只改一个变量。

完整对照示例见 `00_core/aesthetic-director-core/references/taste-calibration-pairs.md`。

---

## Documentation

- `docs/architecture.md` — 分层、优先级、不变量、"人味"的可操作定义
- `docs/skill-registry.md` — Skill 索引（validate 脚本会交叉检查）
- `docs/skill-specification.md` — Skill 编写规范（对齐 agentskills.io）
- `docs/versioning.md` — 版本与品味更新规则
- `CHANGELOG.md`

---

## License

MIT
