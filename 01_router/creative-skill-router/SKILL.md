---
name: creative-skill-router
description: Entry point for all creative requests in this skill hub. Classifies intent (OC/character design, illustration, fashion, NAI5 prompt, Anima prompt, image reverse analysis, prompt review, ComfyUI/LoRA/dataset), loads identity + aesthetic direction first, then hands off to the right specialist and model adapter. Use whenever a request involves 设计, OC, 人设, 立绘, 插画, 服装, 提示词, prompt, NAI, NovelAI, Anima, 反推, 分析图片, ComfyUI, LoRA, or when it is unclear which skill should handle a creative task.
metadata:
  author: Tera-Dark
  version: "3.0.1"
  layer: "01_router"
  load: "always"
  status: "active"
  triggers: "any request; 设计, 提示词, prompt, 反推, 分析, ComfyUI, LoRA"
---

# Creative Skill Router

## Purpose

把用户请求送进正确的创作管线。Router 不产出最终 prompt，只做：**分类 → 设计就绪判定 → Aesthetic Gate → specialist → Blueprint Gate → tag verification → adapter / evaluation**。

```
Request
  ↓
Task Classification            (references/task-classification.md)
  ↓
personal-identity-profile      (always, for any creative task)
  ↓
aesthetic-director-core        (always for creative tasks → produces a Creative Brief)
  ↓
Specialist                     (character-design-engine / illustration-direction / image-reverse-analysis / prompt-analysis)
  ↓
Blueprint Gate
  ↓
Anima: anima-tag-gate           (verify hard anchors only)
  ↓
Model Adapter                  (anima-prompt-compiler / nai5-community-prompt-engineering)
  ↓
evaluation-loop                (on feedback rounds)
```

## Gate Model

### Aesthetic Gate
Every creative request passes the gate.
- FULL: unfinished idea or requested redesign; produce real creative decisions.
- AUDIT: finished design/specification; check structure and generic drift without redesigning locked facts.
- ESCALATE: missing core decision in AUDIT; return to FULL.

### Blueprint Gate
Before any model adapter, verify a type-specific blueprint or a verified finished-design packet. Adapters never fill missing design decisions.

### Anima Tag Gate
For Anima only, hard anchors are validated after the blueprint is ready and before prompt compilation.
- `exact` and `alias` may become verified hard tags.
- `missing` becomes NL; it is never fabricated.
- fuzzy matches and candidate pools never become hard tags.
- canonical Danbooru identity remains separate from Anima syntax escaping.

## Core Rules

1. **创作类请求不得绕过 Aesthetic Gate。** 未完成请求走 FULL；完成设计走 AUDIT。只有 AUDIT PASS 或 FULL 产出通过 Blueprint Gate 后，才允许进入 adapter。
2. **按意图分类，不按关键词。** 用户提到"NAI5"不代表任务是"写 tag"，可能是"设计一个角色然后用 NAI5 出"。
3. **设计决策与模型语法分离。** 适配器不重新设计；设计层不写模型语法。
4. **用户明确要求 > 身份档案 > 审美方向 > 专家 Skill > 模型语法。**
5. **混合请求拆开。** "设计 OC + 训 LoRA" → `character-design-engine` 完成后再进 `dataset-management` / `lora-training`。
6. **反馈轮走 `evaluation-loop` + `aesthetic-director-core/references/feedback-diagnosis.md`**，不是直接改 prompt。
7. **Anima hard tags 必须经过 `anima-tag-gate`。** 不得因为模型记忆、搜索引擎近似结果或语义相似而跳过验证。

## Quick Routing Table

| 意图 | 触发词示例 | 管线 |
|---|---|---|
| 角色 / OC / 服装设计 | OC, 人设, 角色设计, 服装设计, 立绘, 高定, 二游角色 | identity → Aesthetic Gate FULL → `character-design-engine` → Blueprint Gate → adapter |
| 插画 / 氛围图 / 故事感 | 插画, 氛围图, 竖屏, 半留白, 印象风, 故事感, key visual | identity → Aesthetic Gate FULL → `illustration-direction` → Blueprint Gate → adapter |
| 已有设计 → Anima 提示词 | 提示词, prompt, tag, Anima（且设计已完整） | identity → Aesthetic Gate AUDIT → verified design packet → `anima-tag-gate` → `anima-prompt-compiler` |
| 已有设计 → NAI5 提示词 | NAI5, NovelAI（且设计已完整） | identity → Aesthetic Gate AUDIT → verified design packet → `nai5-community-prompt-engineering` |
| 参考图反推 | 反推, 分析图片, 提取提示词, 还原风格, 参考这张 | identity → `image-reverse-analysis` → Aesthetic Gate FULL（原创）/ AUDIT（忠实）→ specialist/adapter |
| 提示词审查 / 优化 | 优化提示词, 这个 prompt 哪里有问题 | `prompt-analysis` → (adapter if rewrite needed) |
| 反馈 / 迭代 | 太平淡, 太乱, 不像, 这版可以, 换个方向 | `evaluation-loop` → feedback-diagnosis → 回到失败层 |
| 其它图像模型 → 提示词 | Midjourney, DALL-E, Imagen, Flux, SD, 通用, 没说模型 | identity → Aesthetic Gate AUDIT/FULL → `general-image-prompt-adapter` |
| 技术 | ComfyUI, LoRA, dataset, 训练, 打标 | `comfyui-workflow` / `lora-training` / `dataset-management`（status: planned → 以通用知识作答，标 `[no module]`，提议 `/new-module`） |
| 扩展模块 | 命中 `06_extensions/*` 或其它模块 description 里的触发词 | 该模块 |
| 非创作、无模块命中 | 闲聊、问答、杂务 | 不加载模块；直接按 kernel §6 的语气回答 |

模型选择规则见 `references/model-selection.md`。完整模块索引以 harness 的 KERNEL §5（由 `bundle/manifest.json` 生成）为准；`docs/skill-registry.md` 是同一份数据的可读版本。

## 触发词来自模块自己

Router 不维护一份手写的触发词总表。每个模块的 frontmatter `description` 和 `metadata.triggers` 就是它的触发条件，build 会把它们汇总进索引。新增模块只要把自己的触发词写好，Router 就能路由到它。

## What the Router Outputs

Router 本身不对用户输出长篇内容。它在内部决定管线后直接开始执行第一步。如果分类有歧义（例如"帮我做一个角色"没说要不要 prompt、要什么模型），**用一个问题**确认，不要列一堆选项。

## References

- `references/task-classification.md` — 分类规则与触发词
- `references/routing-rules.md` — 优先级与冲突解决
- `references/model-selection.md` — 何时选 Anima / NAI5 / 通用模型
- `references/execution-flow.md` — 标准管线与失败恢复
- `references/skill-map.md` — 各层 Skill 一览
