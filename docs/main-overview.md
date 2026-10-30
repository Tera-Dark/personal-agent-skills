# Main Branch Overview · 模块地图

> 维护约定：本页为人工维护的**导航总览**；模块的精确注册状态与版本以构建生成的 [skill-registry.md](skill-registry.md) 和 [bundle/manifest.json](../bundle/manifest.json) 为准。更新日期：2026-10-30，目标版本：5.3.0。

## 快速入口（按使用频率）

| 目的 | 入口 | 说明 |
| --- | --- | --- |
| AI 聊天冷启动 | [bundle/HARNESS.md](../bundle/HARNESS.md) | L1 轻量内核、按需加载索引（由 CI 生成） |
| 完整离线阅读 | [bundle/HARNESS-FULL.md](../bundle/HARNESS-FULL.md) | 全量文本，体积较大 |
| UI / UX / 前端设计 | [chatgpt-inspired-ui](../02_design/chatgpt-inspired-ui/SKILL.md) | 软件界面任务，独立于绘画 Prompt |
| NAI5 / Anima / MOSS | [03_prompt](../03_prompt/) | 目标模型的专用编译器 |
| 创意插画与 OC | [02_design](../02_design/) | 人物 / 插画 / 摄影 / 海报图文 |
| 工具与技术 | [05_tools](../05_tools/) | ComfyUI、数据集、LoRA |
| 反馈学习 | [personal-identity-profile](../00_core/personal-identity-profile/SKILL.md) | 经过许可和审阅的偏好持久化 |

## 所有 Skill（21 个，7 层）

### 00_core · 主控与审美（2）
- [aesthetic-director-core](../00_core/aesthetic-director-core/SKILL.md) — 艺术方向、创意择优、审美证据
- [personal-identity-profile](../00_core/personal-identity-profile/SKILL.md) — 项目拥有者的偏好、禁区、状态和审阅后学习

### 01_router · 任务路由（1）
- [creative-skill-router](../01_router/creative-skill-router/SKILL.md) — 按任务决定 UI、艺术设计、模型 Prompt、分析或工具模块

### 02_design · 设计（6）
- [chatgpt-inspired-ui](../02_design/chatgpt-inspired-ui/SKILL.md) — 产品 UI/UX 与前端功能极简主义
- [character-design-engine](../02_design/character-design-engine/SKILL.md) — 人物、服装、角色可见特征
- [editorial-layout-design](../02_design/editorial-layout-design/SKILL.md) — 插画与海报的**图文排版**，不接管软件 UI
- [illustration-direction](../02_design/illustration-direction/SKILL.md) — 镜头、构图、插画叙事
- [japanese-cinematic-composition](../02_design/japanese-cinematic-composition/SKILL.md) — 摄影式电影画面研究
- [small-artist-brain](../02_design/small-artist-brain/SKILL.md) — 小画师风与作者感审美辅助

### 03_prompt · 图像提示词管线（6）
- [visual-prompt-core](../03_prompt/visual-prompt-core/SKILL.md) — 模型无关的画面事实与设计锁
- [danbooru-tag-gate](../03_prompt/danbooru-tag-gate/SKILL.md) — 已验证的标签索引和验证边界
- [nai5-renderer](../03_prompt/nai5-renderer/SKILL.md) — NovelAI V5 输出格式
- [anima-renderer](../03_prompt/anima-renderer/SKILL.md) — Anima 输出格式
- [moss-image-renderer](../03_prompt/moss-image-renderer/SKILL.md) — MOSS Caption/Tags/Layout
- [general-image-prompt-adapter](../03_prompt/general-image-prompt-adapter/SKILL.md) — 其他图像模型的通用适配

### 04_analysis · 分析（2）
- [image-reverse-analysis](../04_analysis/image-reverse-analysis/SKILL.md) — 图片可观察结构与可迁移语言
- [prompt-analysis](../04_analysis/prompt-analysis/SKILL.md) — 已有提示词结构分析

### 05_tools · 技术工具（3）
- [comfyui-workflow](../05_tools/comfyui-workflow/SKILL.md) — ComfyUI 工作流
- [dataset-management](../05_tools/dataset-management/SKILL.md) — 数据集整理
- [lora-training](../05_tools/lora-training/SKILL.md) — LoRA 训练辅助

### 06_evaluation · 反馈与评审（1）
- [evaluation-loop](../06_evaluation/evaluation-loop/SKILL.md) — 诊断失败层、回归比较与改进

### 07_extensions · 扩展区
- [README](../07_extensions/README.md) — 预留扩展，不计入已登记 Skill 总数

## 运行机制（按需加载）

1. 用户加载 [bundle/HARNESS.md](../bundle/HARNESS.md)：只读 L1 Core 和模块索引，不加载全部参考。
2. Router 根据意图选择一个主模块：软件 UI 直接走 `chatgpt-inspired-ui`；图像创作进入审美/画面/渲染链。
3. 复杂艺术创作按需要读取 L2 Task Cards、L3 深层引用；技术任务只选对应技术模块。
4. 需要精确模型语法的图像 Prompt 才进入 NAI5 / Anima / MOSS renderer；UI 设计不走生图管线。
5. [scripts/build.py](../scripts/build.py) 从 Skill 源文件生成 `bundle/` 和 `docs/skill-registry.md`，**不要直接手动修改生成产物**。

## 工程与数据目录

| 路径 | 职责 | 维护策略 |
| --- | --- | --- |
| `kernel/` | 主运行契约、轻量任务卡、扩展协议 | 核心规范，慎重修改 |
| `harness.json` | 编译入口、层级、pipeline 与加载设置 | 修改前评估兼容性 |
| `00_core/…06_evaluation/` | **Skill 源码**与按需引用 | 新功能优先在相应 owner 下扩展 |
| `data/learning/` | 经过定义的反馈事件、已审阅偏好 | 遵循权限与隐私边界 |
| `scripts/` | 构建、验证、标签索引、反馈工具 | Python 标准库脚本为主 |
| `tests/` | 回归验证 | 新路由和输出契约应有验证 |
| `docs/` | 使用、架构、版本、评审与导航文档 | 人工维护，registry 例外 |
| `bundle/` | **生成的 Web-first 运行时**和第三方 tag 分片 | CI 自动生成，勿手改 |
| `.github/workflows/harness.yml` | PR 验证及 main 自动重建 | 验证结果以 Actions 为准 |

### 关于仓库文件数量

当前仓库绝大多数文件来自 `bundle/tag-index/` 的标签分片（属于**自动生成/预置索引数据**），不代表仓库有数千个 Skill；主线复杂度应以 **21 个模块与可选 references** 衡量，而非总文件数。

## 后续整理方向（不自动执行破坏性重构）

1. **P1 文档首页**：README 比较长；保持主页为入口，长篇使用与历史细节优先链接到 `docs/`。
2. **P1 路由边界**：持续把应用 UI 与插画图文设计分开，并给交叉任务编写回归测试。
3. **P2 按需引用**：长期参考量较多，只加载当前任务必要资料；定期检查重复规则与过时来源。
4. **P2 生成产物**：标签分片数量巨大但按前缀索引读取；不应为了“整洁”而盲目合并或删除，先测性能和链接兼容性。
5. **P2 文档版本**：已存在旧日期或历史条目时保持来源追溯，避免把旧实验写成当前已验证的规则。

## 本地维护常用命令

```bash
python3 scripts/validate_skills.py
python3 scripts/build.py
python3 scripts/validate_skills.py --check-bundle
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

新模块优先 PR + squash merge；主分支上的构建 Action 另行产生生成文件同步提交（如果存在差异）。