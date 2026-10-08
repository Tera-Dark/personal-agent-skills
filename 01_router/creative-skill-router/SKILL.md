---
name: creative-skill-router
description: Entry point for all creative requests. Classifies intent and sends the task to design, analysis, shared prompt compilation, target-model rendering, evaluation, or technical modules. Use for 设计, OC, 人设, 立绘, 插画, 提示词, prompt, NAI, NovelAI, Anima, 反推, 分析图片, ComfyUI, LoRA, or ambiguous creative tasks.
metadata:
  author: Tera-Dark
  version: "4.0.0"
  layer: "01_router"
  load: "always"
  status: "active"
  triggers: "any request, 设计, 提示词, prompt, 反推, 分析, ComfyUI, LoRA, NAI5, Anima"
---

# Creative Skill Router

## 定位

Router 只负责：**分类 → 选择入口 → 判断设计是否就绪 → 把任务交给正确 owner**。

Router 不负责：
- 审美决策；
- 角色设计；
- Prompt Packet 细节；
- Danbooru 验证细节；
- Anima / NAI5 内部语法。

## 主路由

### 1. 创作请求

未完成的角色 / 服装 / 插画想法：

identity → Aesthetic Gate FULL → specialist → Blueprint Gate

### 2. 已完成设计 → 模型提示词

完整设计 / blueprint / 明确锁定事实：

identity → Aesthetic Gate AUDIT → Blueprint Gate → visual-prompt-core → danbooru-tag-gate → renderer

### 3. 目标模型

| 目标 | Renderer |
|---|---|
| Anima | anima-renderer |
| NAI5 / NovelAI | nai5-renderer |
| 其它图像模型 | general-image-prompt-adapter |

NAI5 与 Anima **共享 Prompt Core，不各自重新做设计**。

### 4. 参考图

- “参考这张做原创” → image-reverse-analysis → Aesthetic Gate FULL → specialist。
- “忠实反推这张” → image-reverse-analysis → Aesthetic Gate AUDIT → Prompt Core / renderer。

### 5. 现有 Prompt

existing prompt → prompt-analysis

如果问题是设计层：
→ Aesthetic Gate / specialist

如果问题只是模型语法：
→ Prompt Core / target renderer

### 6. 反馈

生成图、版本比较、用户说“太平淡 / 太乱 / 不像 / 这版可以 / 哪里不对”：

→ evaluation-loop → 失败层 owner

只修第一个实际失败层，不借 renderer 堆词掩盖设计问题。

### 7. 技术

ComfyUI / LoRA / dataset：
→ 对应 technical module

若模块仍为 planned：
→ [no module]，不得伪装为已加载的专项知识。

## 路由原则

1. 按意图，不按关键词。
2. NAI5 / Anima 名称只决定 renderer，不决定设计方式。
3. 共享知识只经过 shared owner；不要把同一规则重新复制到 renderer。
4. 不确定 target model 且语法会显著改变输出 → 只问一个问题。
5. 混合任务拆成阶段：例如“设计 OC + 生成 NAI5 + 训练 LoRA”应先完成设计，再进入 Prompt Renderer，再进入训练工具。

## 路由结果

Router 不向用户输出长篇架构说明。内部决定路径后直接执行下一步。

## References

- references/task-classification.md
- references/routing-rules.md
- references/model-selection.md
- references/execution-flow.md
- references/skill-map.md


## References
- `references/execution-flow.md` — bundled reference for this module.
- `references/model-selection.md` — bundled reference for this module.
- `references/routing-rules.md` — bundled reference for this module.
- `references/skill-map.md` — bundled reference for this module.
- `references/task-classification.md` — bundled reference for this module.
