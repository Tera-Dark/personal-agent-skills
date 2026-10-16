# MOSS-Image · 官方证据与使用范围（2026-10-16）

本文件是**模型参考**而非独立创意设计模块；官方确认只支撑**格式和建议配置**，不等于个人已在 NAI5/ComfyUI 跑图验证。

## 官方来源

- [Official · project site] https://openmoss.ai/MOSS-Image/ — 5B DiT；两种模型；4K prompt tokens；自然语言、文字/物件原生 Layout；二次元与摄影风格。
- [Official · English User Guide] https://github.com/OpenMOSS/MOSS-Image/blob/main/USERGUIDE.md
- [Official · 中文指南] https://github.com/OpenMOSS/MOSS-Image/blob/main/USERGUIDE_ZH.md
- [Official · Base model card] https://huggingface.co/OpenMOSS-Team/MOSS-Image-Base
- [Official · SFT model card] https://huggingface.co/OpenMOSS-Team/MOSS-Image-SFT
- [Official · Prompt Enhancer] https://github.com/OpenMOSS/MOSS-Image/blob/main/skills/moss-image-prompt-enhancer/SKILL.md
- [Official · Pixel Layout draft contract] https://github.com/OpenMOSS/MOSS-Image/blob/main/skills/moss-image-prompt-enhancer/references/layout.md
- [Official · ComfyUI] https://github.com/OpenMOSS/MOSS-Image/blob/main/comfyui/README.md

## Base / SFT

- Base 是基础图像模型，强调训练信息和 LoRA 可扩展性。
- SFT 源于 Base 的 curated-data 监督微调。官方展示它在一个白板案例的文字分组/排版改善，**不能据此断言 SFT 对所有二次元/摄影风格优于 Base**。
- 两种模型共享架构与推理接口；不把某个版本的个别出图质量当全局规律。
- 官方编码上限 4K prompt tokens，**不是**让普通 Caption 默认写满 4K。

## 官方推理基准（不是 Prompt）

| 设置 | 官方建议 |
|---|---|
| Sampler | Euler / flow-matching |
| Steps | 50 或更多 |
| CFG | 默认 3.0，官方建议 3–6；长提示词常用 3 |
| Shift | 默认 5 |
| SLG | negative-branch uncond skip layer 22（0-index），24/26 也可能有帮助 |
| Negative | Python 默认空；指南有可选负面标签 |
| Resolution | 推荐像素总数约 1M、1.5M、2M；部分更宽范围为外推 |
| Dimensions | Python/手动宽高必须为正且为 16 的倍数 |

[Official] 官方指出关闭 SLG 可能让图片更真实但部分细节崩坏：这属于模型设置，不是正面提示词“风格 token”的作用。

[Official · tag order] Quality → Score → Meta → Year → Character → Series → Artist → General；官方示例：`best quality, highres, hatsune miku, vocaloid, @foo bar, 1girl, blue hair`。`@foo bar` **只是形式示例**，不可当真实画师或个人默认串。Tag group 不能推导出诸如 `score_9`、`year 2026` 在本模型的稳定强度；想使用前必须另行验证。

[Official · language] 英文训练数据较多，推荐英文描述，但支持中文等语言；画面中的精确文字保持用户原本语言。

[Official · layout] 有 `summary.caption`、平铺 `items`，元素可用 label 为 `text`/`object`/`character`；默认模型直接接收 `abs_centralized + yxyx`。**官方 Prompt Enhancer 的 draft 是左上角 abs + xyxy，只有编译后才是模型正面提示词**。生成宽高和 Layout 草稿宽高必须一致。

[Official · memory] ComfyUI 插件可安装在 custom_nodes/MOSS-Image，推荐参数 50/3/5/uncond22，显存卸载模式与实际速度取决于硬件。不能保证 RTX 4060 8GB 可以直接常驻全部模型。

## 证据标签

- [Official]：以上官方站点、HF 模型卡或官方用户指南明确声明。
- [Candidate]：风格形容词、复合写法及其分配方法，是我们的待测设计策略。
- [Community]：非官方截图、教程或单张演示，只能作参考。
- [User-tested]：保留生成设置、模型 checkpoint、seed、截图或用户评价的真实 A/B 实验。
- 真实出图未发生时写 `IMAGE-PENDING`，不可升级为 `USER-APPROVED` 或“已稳定触发”。
