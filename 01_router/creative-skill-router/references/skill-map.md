# Skill Map

Skill 之间按**名字**引用（不是相对路径），因为它们可能被分别安装到不同位置。

## 00_core — 身份与审美

- `personal-identity-profile` — 品味签名、否决清单、工作方式。唯一的品味来源。
- `aesthetic-director-core` — 九个创作动作 → Creative Brief。所有创作任务的第一站。

## 01_router

- `creative-skill-router` — 本 Skill。

## 02_creation — 设计与模型适配

设计（模型无关）：
- `character-design-engine` — Brief → 角色 blueprint（命题、轮廓、服装工程、配色层级、姿势因果、展示方式）
- `illustration-direction` — Brief → 画面 blueprint（瞬间、构图、光源、密度、氛围预设）

适配器（模型相关，只翻译不设计）：
- `anima-prompt-compiler` — Tag + Natural Language 格式，Anima 系列
- `nai5-community-prompt-engineering` — 社区格式：artist stack / char blocks / 权重，NovelAI
- `general-image-prompt-adapter` — 自然语言 prompt，Midjourney / DALL-E / Imagen / Flux / SD / 未命名目标；带证据标签

## 03_analysis

- `image-reverse-analysis` — 参考图 → 设计语言（结构，不是物件）
- `prompt-analysis` — 现有 prompt → 意图 / 结构 / 问题 / 改法

## 04_tools — 技术（status: planned，无可加载内容）

- `comfyui-workflow`
- `lora-training`
- `dataset-management`

## 05_evaluation

- `evaluation-loop` — 六维评分 + 反馈诊断 + 单变量迭代

## 06_extensions — owner 通过聊天新增的模块

目前为空。规则见 `kernel/EXTENSION-PROTOCOL.md`。

## kernel/ — 不是 Skill

`kernel/KERNEL.md` 是运行契约（操作循环、加载协议、视觉协议、会话状态、命令、扩展协议）。build 会把它和 always-on 模块合成 `bundle/HARNESS.md`。
