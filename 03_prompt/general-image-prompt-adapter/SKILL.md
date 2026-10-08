---
name: general-image-prompt-adapter
description: Generic target renderer that converts a Visual Prompt Packet into a natural-language image prompt for models that are not Anima or NAI5 — Midjourney, DALL-E / GPT Image, Google Imagen / Gemini image, Flux, SDXL-style checkpoints, or an unnamed target. Use after the shared Prompt Core. Does not design.
metadata:
  author: Tera-Dark
  version: "0.3.0"
  layer: "03_prompt"
  load: "on-demand"
  status: "active"
  triggers: "Midjourney, MJ, DALL-E, GPT Image, Imagen, Gemini image, Nano Banana, Flux, SDXL, Stable Diffusion, 通用提示词, 其他模型, 不知道用什么模型"
---

# General Image Prompt Renderer

## 定位

输入：通过 Aesthetic / Blueprint Gate 的设计 → visual-prompt-core 生成的 Visual Prompt Packet；目标模型名可缺省。
输出：一段英文自然语言 prompt，以及仅在目标模型官方支持且用户要求时给出的参数行。
上游：visual-prompt-core
下游：目标图像模型
不做：不设计、不重新整理 Blueprint、不另建一套通用 Prompt Core、不凭记忆编造模型行为。

## 硬规则

- 没有 Visual Prompt Packet 时不得自行补设计；退回 Prompt Core / 上游设计层。
- 目标模型未知且目标语法会显著改变输出时，只问一个问题；否则按 generic 自然语言格式。
- prompt 正文只表达视觉内容和关系。参数、权重、采样器、负面参数不混入正文，除非目标官方明确支持且用户要求。
- 空泛质量词不是默认填充物；只输出 Packet 中真正需要的 quality intent。
- 锁定事实、主轮廓、构图、动作、刺点和被删内容边界必须保持。
- 任何模型行为断言带 [Official] / [Community] / [Personal experiment] / [Unverified]。

## 执行流程

1. 确认目标模型与输出模式。
2. 读取 references/target-notes.md，只采纳有证据标签的目标-specific规则。
3. 按 Packet 组织：subject / framing → visual structure → appearance → outfit → action / relation → scene / light → palette / punctum。
4. 保持关系词和空间因果；不要把 Packet 重新压成无关系的关键词串。
5. 默认输出 50–90 词，标准模式上限约 110 词；超限先删解释、同义词、次要装饰，不删锁定事实和结构锚点。
6. 如果目标官方支持参数且用户要求，把参数放在 prompt 外单独输出，并附证据标签。
7. 做 Design Lock：Packet 中的 locked facts / framing / silhouette / action / punctum / environment relation 全部保留。

## 输出契约

```
<English natural-language prompt>
```
参数（如适用）：<target-specific parameter line> [Evidence] / 不适用

## 自检

- [ ] 输入确实来自 Visual Prompt Core。
- [ ] 没有重新设计。
- [ ] 关系没有被扁平成关键词。
- [ ] 锁定事实、主轮廓和刺点仍在。
- [ ] 模型-specific claims 有证据标签。
- [ ] 没有为了“完整”而回填质量词或装饰词。

## References

- `references/target-notes.md` — 常见目标的格式笔记，逐条带证据标签；表外目标一律 [Unverified].
