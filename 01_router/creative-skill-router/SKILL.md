---
name: creative-skill-router
description: Intent router for creative requests: character and illustration design, NAI5/Anima prompts, reference analysis, feedback learning, ComfyUI and LoRA. Dispatches to the correct owner without redesigning or encoding model syntax.
metadata:
  author: Tera-Dark
  version: "4.9.0"
  layer: "01_router"
  load: "always"
  status: "active"
  triggers: "any request, 设计, 提示词, prompt, 反推, 分析, ComfyUI, LoRA, NAI5, Anima"
---

# Creative Skill Router

## 定位

**按意图分类 → 选模式与正确 owner**。不执行设计、Tag 验证或模型语法。

## 执行模式选择

- **FULL CREATIVE**：新 OC、服设、插画、海报；简单肖像紧凑处理，复杂叙事充分设计。
- **FAST VARIANT**：已认可设计仅改指定变量，其余锁定。
- **PROMPT ONLY**：内部仍做必要设计和校验；仅交付可复制 Prompt，不展示内部 Brief。
- FAST VARIANT 改身份、命题或主构图则升级 FULL；生图许可仅由 Kernel 决定。

## 主路由

### 1. 创作请求

未完成的角色 / 服装 / 插画想法：

identity → Aesthetic Gate FULL → specialist → Blueprint Gate

### 1.1 小画师脑（按需）

触发“小画师脑 / 蒸蒸 / 女性向作者感插画”时：

identity → Aesthetic Gate → **small-artist-brain**（独立审美 Decision Sheet，按 SIMPLE / BALANCED / ORNATE）→ character-design-engine / illustration-direction → Blueprint Gate。

- 按需读取小画师模块和相关 reference；它只提供审美证据与决策增量，不是第二套 Director/Renderer，不强制繁花化；原版服设、白底和用户锁定事实优先。

### 1.2 「鱼的库洛牌」摄影思维（按需）

「鱼的库洛牌 / 摄影脑 / 摄影思维 / NAI5 摄影电影感 / 纪实抓拍、生活流」→ **yu-de-kuluopai-photography-brain** 生成摄影 Decision Sheet（机位、瞬间、触点、光、空间）→ **illustration-direction** 统一 Blueprint Gate → Prompt Core / Tag Gate / NAI5 Renderer。

仅真实观察型电影感调用；史诗海报不强制。与小画师脑可叠加但不另设构图 owner；不复制参考图中的校服、海边、黄伞，不更改用户锁定人设，不自动生图。详见摄影模块按需引用。

### 2. 已完成设计 → 模型提示词

完整设计 / blueprint / 明确锁定事实：

identity → Aesthetic Gate AUDIT → Blueprint Gate → visual-prompt-core → danbooru-tag-gate → renderer

### 3. 目标模型

| 目标 | Renderer |
|---|---|
| Anima | anima-renderer |
| NAI5 / NovelAI | nai5-renderer |
| 其它图像模型 | general-image-prompt-adapter |

NAI5 / Anima 共享 Prompt Core；NAI5 专属控制器留 Renderer 按需读取。

### 4. 参考图

- “参考这张做原创” → image-reverse-analysis → Aesthetic Gate FULL → specialist。
- “忠实反推这张” → image-reverse-analysis → Aesthetic Gate AUDIT → Prompt Core / renderer。

### 5. 现有 Prompt

existing prompt → prompt-analysis；设计问题回 specialist，语法问题进 target renderer。

### 6. 反馈

生成图、版本比较、用户说“太平淡 / 太乱 / 不像 / 这版可以 / 哪里不对”：

→ evaluation-loop（诊断 + 拆分好/坏反馈）→ 当前轮锁定 / 身份模块学习候选 → 失败层 owner。

评价反馈按需读取 `00_core/personal-identity-profile/references/feedback-learning-loop.md`：先拆分 signal 并锁住当轮成功维度，持久记录才写 `data/learning/events.jsonl`；由 `scripts/learn.py` 去重、评审、晋升、撤销，禁止直接把 candidate 写成 Taste Core。**写 GitHub 要有连接和许可；无权限只导出 JSON**。短句/接力按需读 `references/conversation-qol.md`，只修第一个失败层。

### 7. 技术

ComfyUI / LoRA / dataset → 对应 technical module；planned 不得伪装为已加载。

## 路由原则

按意图而非关键词；目标模型只决定 renderer；共享规则仅一个 owner。未知目标影响语法时最多问一个问题。设计 + Prompt + LoRA 按阶段执行。Router 不展示路由长文，直接处理任务。

## References
- `references/conversation-qol.md` — **按需：高频短句、一框复制、继续/回退、口语化偏好学习入口**。
- `references/task-classification.md`
- `references/routing-rules.md`
- `references/model-selection.md`
- `references/execution-flow.md`
- `references/skill-map.md`
