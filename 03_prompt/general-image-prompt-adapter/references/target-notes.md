# Target Notes — 常见图像模型的格式笔记

> 归属：`02_creation/general-image-prompt-adapter`。用途：Step 2 查目标格式。
> **每条都带证据标签。** 这些模型更新很快；标签是写下时的状态，不是永久事实。表外的目标一律按 `[Unverified]` 处理：用通用自然语言，不加参数。
> 标签含义：`[Official]` 官方文档可查 · `[Community]` 社区广泛实践 · `[Personal experiment]` owner 实测 · `[Unverified]` 未核实

| 目标 | 输入偏好 | 参数 | 注意 | 证据 |
|---|---|---|---|---|
| **Midjourney** | 自然语言短段落；前置信息权重更高 | `--ar W:H`、`--no <x>`、`--stylize`、`--chaos`、`--v` 等为官方参数，放在 prompt 末尾 | `--no` 是唯一可靠的排除方式；正文里的 "no X" 常被当正向 | 参数 `[Official]`；"前置权重更高" `[Community]` |
| **DALL-E 3 / GPT Image (OpenAI)** | 自然语言；接受长句 | 无正文参数；比例等由界面/API 设定 | 服务端可能改写 prompt（DALL-E 3 官方说明有改写机制）；关键事实放前面并写成完整句 | 无参数 `[Official]`；DALL-E 3 改写 `[Official]`；GPT Image 改写行为 `[Unverified]` |
| **Google Imagen / Gemini 图像生成** | 自然语言；支持对话式修改 | 无正文参数；比例由 API/界面设定 | 描述性长句表现好；用正向约束替代否定 | 自然语言 `[Official]`；其它 `[Community]` |
| **Flux (Black Forest Labs)** | 自然语言长描述 | 基础模型无正文权重语法；前端可能提供 | 对空间关系词响应好 | `[Community]` |
| **SDXL 及衍生 checkpoint** | tag + 短句混合 | `(word:1.2)` 权重是 WebUI/ComfyUI 的前端语法，不是模型的 | 各 checkpoint 差异大；owner 未指定 checkpoint 时按通用 NL | `[Community]` |
| **未命名 / generic** | 自然语言 60–120 词 | 无 | 前 40 词放锁定事实与刺点 | — |

## 通用顺序（所有目标）

```
[count + framing] [presentation/background]
[thesis structure: the big shape and where it sits]
[appearance: hair as shape distribution, eyes, skin]
[garment: base → structural → signature extension → accessory system; each as shape + position + behavior]
[pose causality + the moment]
[environment: the one layer that explains light or action]
[key light: source, direction, falloff; shadow region]
[palette: dominant / structural / the only saturated color is ___ at ___]
```

## 更新记录

- 2026-09-28 · 初版 · Midjourney 参数依据 docs.midjourney.com 参数页；DALL-E 3 改写依据 OpenAI 官方 DALL-E 3 说明；其余为社区实践或未核实。
