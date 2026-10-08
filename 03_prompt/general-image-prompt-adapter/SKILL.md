---
name: general-image-prompt-adapter
description: Model adapter that compiles a finished character or illustration blueprint into a natural-language image prompt for models that are not Anima or NAI5 — Midjourney, DALL-E / GPT Image, Google Imagen / Gemini image, Flux, SDXL-style checkpoints, or an unnamed target. Keeps parameters out of the prompt unless the target officially supports them, and labels every model-specific claim with an evidence level. Use when the user names any other image model, says 通用提示词, MJ, Midjourney, DALL-E, Imagen, Flux, SD, 或没说用什么模型. Does not design — if no blueprint exists, route through aesthetic-director-core first.
metadata:
  author: Tera-Dark
  version: "0.2.0"
  layer: "03_prompt"
  load: "on-demand"
  status: "active"
  triggers: "Midjourney, MJ, DALL-E, GPT Image, Imagen, Gemini image, Nano Banana, Flux, SDXL, Stable Diffusion, 通用提示词, 其他模型, 不知道用什么模型"
---

# General Image Prompt Adapter

## 定位

输入：blueprint（来自 `character-design-engine` / `illustration-direction`）+ 目标模型名（可缺省）。
输出：一段英文自然语言 prompt（代码块），以及——仅当目标官方支持时——放在 prompt 外的参数行。
不做：设计。收到的不是 blueprint（没有带动词的命题、轮廓、四层服装、一个刺点、锁定事实）就退回 `aesthetic-director-core`。
不做：编造模型行为。本 Skill 覆盖的模型很多、变化很快；**不确定就写 `[Unverified]`**，不要猜参数。

## Blueprint boundary

This module is a target-model adapter. It accepts only a validated blueprint or Visual Prompt Packet and **does not design**. Missing design decisions must route upstream.

## Blueprint boundary

This module is a target-model renderer. It accepts only a validated Visual Prompt Packet and does not design. If the Packet is missing or incomplete, route upstream to visual-prompt-core and the appropriate design gate.

## 硬规则

- 目标模型未知且会影响格式 → 问**一个**问题："用哪个模型出图？不确定就按通用自然语言写。" 不列选项清单。
- prompt 正文只放视觉描述。`--ar`、权重、采样器、负面词等**不进正文**，除非该目标的官方文档支持且 owner 要。
- 任何"某模型对 X 更敏感"的说法带证据标签。`references/target-notes.md` 里的每条都已标注；表里没有的目标一律 `[Unverified]`。
- 不加 `masterpiece, 8k, ultra-detailed, award-winning` 一类空泛质量词。
- 不改锁定事实。被 blueprint 删掉的东西不得以任何形式回来。

## 执行流程

```
Step 1  确认目标        owner 指定 / 从 Session State 读 / 问一个问题 / 缺省为 generic
Step 2  查目标笔记      references/target-notes.md：格式偏好、长度、是否支持参数，逐条看证据标签
Step 3  组织顺序        主体与景别 → 命题结构（轮廓的空间关系）→ 外观 → 服装四层（形状+位置+行为）
                        → 姿势因果与瞬间 → 环境（只留解释光/动作的一层）→ 主光源与衰减 → 配色三级与刺点位置
Step 4  写 prompt       连贯英文段落（不是逗号 tag 串，除非目标笔记说 tag 更稳）。
                        关系词优先：over / beneath / descending from / wrapping / weighed down by / the only saturated color is
Step 5  参数行          仅当目标官方支持：单独一行，放在代码块外或代码块末尾单独一行，标注 [Official]
Step 6  长度            compact default：50–90 词；Direct / Standard 硬上限 110 词。超了先删解释性句子、重复形容词、次要配饰、背景枝节；不删命题、主轮廓、主动作、锚点、刺点、因果、锁定事实
Step 7  自检
```

## 输出契约

```
方向：<blueprint 的命题，一行>
目标：<模型名 或 generic>

```text
<English natural-language prompt>
```
参数（如适用）：<e.g. --ar 3:4 --no jewelry>  [Official] / 不适用

丢失与补救：<这个格式丢了什么关系，怎么补的，一到两行>
```

Standard mode 下同 `anima-prompt-compiler`：V1 忠实 + V2 增强，V2 不改 V1 事实。

## 翻译 blueprint 时的取舍

自然语言格式保留关系的能力最强，主要风险是**模型改写**（部分服务会在生成前重写 prompt）和**长度衰减**（尾部信息被忽略）：

- 把锁定事实和刺点放在前 40 词内。
- 每个颜色词紧贴它的名词，只出现一次。
- "留下的怪"用一个完整短句写，不用单词——单词会被改写掉。
- 不写"no X"（很多模型把否定词当正向）；用正向约束翻译：`bare neck and wrists` 而不是 `no jewelry`。目标官方支持排除参数时（如 MJ `--no`）再用参数。

## 自检

- [ ] 输入是 blueprint？
- [ ] 目标已确认或明确标 generic？
- [ ] 正文无参数、无质量词、无否定句？
- [ ] 锁定事实和刺点在前 40 词？
- [ ] 每个模型断言有证据标签？
- [ ] 被删的东西没回来？
- [ ] 有"丢失与补救"一行？

## References

- `references/target-notes.md` — 常见目标的格式笔记，逐条带证据标签；表外目标一律 [Unverified]
