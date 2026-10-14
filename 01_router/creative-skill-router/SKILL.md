---
name: creative-skill-router
description: Entry point for all creative requests. Classifies intent and sends the task to design, analysis, shared prompt compilation, target-model rendering, evaluation, or technical modules. Use for 设计, OC, 人设, 立绘, 插画, 提示词, prompt, NAI, NovelAI, Anima, 反推, 分析图片, ComfyUI, LoRA, or ambiguous creative tasks.
metadata:
  author: Tera-Dark
  version: "4.7.0"
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

## 执行模式选择

- **FULL CREATIVE**：新 OC、服设、插画、海报或核心命题未定；简单肖像使用紧凑 Brief，复杂高完成度插画才充分展开叙事、空间和专业审美参考。
- **FAST VARIANT**：用户基于已认可设计要求局部改动。先锁定原设计，只改当轮指定变量；不重新探索被锁定的部分。
- **PROMPT ONLY**：交付层覆盖规则，不是跳过审美设计的捷径。无论新创作还是完整设计，只要用户要求提示词，就私下做适用的设计与校验，仅交付可复制 Prompt；不得展示候选方向、Creative Brief 或路由过程。
- 模式由意图和设计完成度决定，不只靠关键词。如果 FAST VARIANT 涉及身份、主轮廓、核心命题或构图的重大改变，则升级 FULL CREATIVE。单纯“设计图片”只授权文本创作；生图工具的使用由 Kernel 授权规则单独判断。

## NAI5 高杠杆技巧的延迟加载

当用户要求 NAI5 的镜头增强、光照复现、权重纠偏、IP 精准还原、POV、双人互动、极端透视、画师覆盖等任务：**照常先完成设计与共享 Prompt Packet**，选 NAI5 Renderer 后优先查 `references/nai5-control-matrix.md`（通过渲染器的引用链接）。不因为含有“POV/正向负权重/复杂度”等术语而创建第二套审美设计引擎，也不把它们塞进 Anima 流程。

一般的简短肖像编辑只加载当前必需的小节；详细成功率/边界需要时再查 `nai-v5-usage-guide.md`。如果用户说“刚才网站的实测招数”，优先使用**该实测控制矩阵**而不是普通模板形容词。

## 主路由

### 1. 创作请求

未完成的角色 / 服装 / 插画想法：

identity → Aesthetic Gate FULL → specialist → Blueprint Gate

### 1.1 小画师脑：按需审美增强，不新建另一套通用设计引擎

若用户明确提到「小画师脑」「蒸蒸」「米画师风格分析」，或当前任务要求女性向作者感、活人互动、精美人物插画的专项审美提升：

identity → Aesthetic Gate → **small-artist-brain**（独立审美 Decision Sheet，按 SIMPLE / BALANCED / ORNATE）→ character-design-engine / illustration-direction → Blueprint Gate。

- 仅在触发时读取 `02_design/small-artist-brain/SKILL.md`，创作时按需读取 `02_design/small-artist-brain/references/zheng-transferable-grammar.md`；复盘出处时才读取 16 案例原始分析。
- 它是**审美证据与决策增强**，不是第二份 universal aesthetic gate、不是另一份 model renderer、不是所有日常/单人都自动繁花化。
- 用户指定原版服设、固定人设、白底或低彩时必须保留。Prompt Core 不复制这套逻辑，只接收已锁定 blueprint。

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

只修第一个实际失败层，不借 renderer 堆词掩盖设计问题。对于用户明确要求的局部变体，采用 FAST VARIANT，不重做未受影响的设计层。

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
- `references/task-classification.md`
- `references/routing-rules.md`
- `references/model-selection.md`
- `references/execution-flow.md`
- `references/skill-map.md`
