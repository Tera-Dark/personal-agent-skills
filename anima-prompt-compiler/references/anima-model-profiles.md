# Anima Model Profiles & Tuning Reference

> **Version**: 1.1.0  
> **Last Updated**: 2026-09-17  
> **Maintainer**: Tera-Dark  
> **Scope**: Anima 模型族各版本特性、提示词语法、文本编码器兼容性与实验记录

本文档为 `anima-prompt-compiler` 提供模型底层特性参考。所有结论均根据**证据分级体系**标注，防止将偶然实验或特定前端经验固化为绝对法则。

---

## 1. 证据分级体系 (Evidence Levels)

为了确保知识库的严谨性与可复现性，本文档中的所有经验与建议分为三级：

### 🟢 Official (官方规范)
由 Anima 官方模型卡片、官方发布公告或官方 ComfyUI/Diffusers 工作流直接确认的技术规范。
### 🟡 Community Practice (社区实践)
在 Civitai、Liblib、Discord 社区中被多位创作者高频验证的常规经验，适用于多数常规场景，但无官方绝对保证。
### 🔵 Personal Experiment (个人实验记录)
在特定硬件、前端、Checkpoint、Sampler 和特定提示词条件下观察到的现象。仅供参考，未在所有环境中复现前不作为普适定律。

---

## 2. 模型族特性对比矩阵 (Model Variants)

| 模型变体 | 核心训练导向 [Evidence] | 提示词敏感度 | 构图服从度 | 典型适用场景 |
| :--- | :--- | :--- | :--- | :--- |
| **Anima Base** | 通用动漫底模，泛化性强，擅长标准立绘与角色特征还原。`[Official]` | 偏向 Tag 列表与短句混合。对复杂复合长句服从度中等。 | 居中立绘与标准景别极其稳定，复杂非对称需要更清晰的层级引导。 | OC 基础立绘、简单日常插画、通用动画角色生成。 |
| **Anima Aesthetic** | 专精于插画级艺术感、光影层次与高级笔触的审美微调版。`[Official]` | **极高**。对光影物理方向词（`rim light`, `volumetric lighting`）与负空间响应灵敏。 | 极强。对景深衰减、非对称偏置与多尺度展示板响应优异。 | 艺术插画、电影感海报、高定服设、画册级概念图。 |
| **Anima Turbo / Lightning** | 蒸馏高速版本，牺牲极少量微观纹理换取快速收敛。`[Official]` | 对提示词冲突较敏感，建议精炼高信息密度的 Tag 链。 | 中等。建议采用单一主视角，避免过度复杂的图内分屏。 | 概念草图快速摸索、表情差分批量产出、快速原型迭代。 |

---

## 3. 文本编码器与前端兼容性 (Text Encoder & Frontend Compatibility)

> 🟢 **Official / Community Practice**

Do not assume traditional CLIP settings such as Clip Skip 2 apply to every Anima workflow. Follow the text encoder and frontend configuration supplied by the selected Anima checkpoint or workflow.

Do not place sampler, CFG, steps, or Clip Skip values inside the prompt unless the user explicitly asks for generation settings.

### 关键兼容性准则
1. **文本编码器差异**：部分现代 Anima 变体或整合工作流可能采用 Qwen、T5 或混合双文本编码器架构，其对自然语言从句的理解能力远超早期 CLIP 模型。不要机械套用传统 SD1.5 的“必须全逗号 Tag 语法”或“强制 Clip Skip 2”。
2. **生成参数隔离**：除非用户在输入中明确要求输出运行参数，否则**编译器严禁在输出的 Prompt 代码块内夹带 `--cfg`, `--steps`, `Sampler:` 等参数文本**。

---

## 4. 质量词与有效渲染描述 (Quality Tags & Cleaning)

### 4.1 推荐保留的有效渲染描述 `[Community Practice]`
这些词汇具有明确的物理与视觉特征引导，可提升质感：
- `fine anime lineart`：引导清晰利落的边缘线稿与闭合。
- `detailed fabric texture`：增强布料纹理、织物经纬与呢料质感。
- `soft volumetric lighting` / `subsurface scattering`：赋予皮肤微透光通透感与空间光束。
- `delicate eye highlight`：刻画瞳孔折射层次，避免眼神呆滞。

### 4.2 默认净化的空泛词 (Low-Information Tokens) `[Community Practice]`
以下词汇已被主编译器过滤列表默认拦截：
```text
[BANNED TOKENS]
masterpiece, best quality, ultra high quality, 8k, 4k, insanely detailed, award winning,
perfect anatomy, perfect quality, incredible visual, wallpaper, trend on artstation
```
> **设计理由**：空泛质量词缺乏具体的空间与材质信息，会白白占用注意力预算（Attention Tokens），且容易引发模型在不同画风之间的随机跳跃。

---

## 5. 提示词权重习惯 `[Community Practice]`

- **语序优先原则 (Word Order Priority)**：Anima 对靠前词汇分配天然更高的注意力权重。核心主体与关键特征置于前 20% 位置，比单纯加权重括号更自然稳定。
- **权重修饰建议**：如需微调，建议控制在 `(keyword:1.05)` 至 `(keyword:1.20)` 温和区间内。避免盲目拉高数值导致色彩失真或边缘锯齿。

---

## 6. 官方与工作流推荐参数参考 (Workflow Reference Presets)

*注：以下数值作为常规工作流调试起点，实际请以具体模型发布页说明为准。*

| 参数项 | Anima Base / Aesthetic | Anima Turbo / Lightning | 证据分级与说明 |
| :--- | :--- | :--- | :--- |
| **CFG Scale** | **4.0 - 5.0** (常规推荐) | **1.5 - 2.5** | `[Official]` 官方建议保持在 4~5 区间，过高易导致过度锐化与高对比。 |
| **Steps** | 20 - 30 | 4 - 8 (视具体蒸馏方案) | `[Community Practice]` 步数取决于具体 Scheduler，超过 35 边际效益递减。 |
| **Sampler** | Euler a / DPM++ 2M Karras | Euler / DPM++ SDE | `[Community Practice]` 依具体 Checkpoint 与 WebUI/ComfyUI 习惯选用。 |
| **Clip Skip** | 由具体工作流配置决定 | 由具体工作流配置决定 | `[Official]` 严禁武断套用固定值，依对应文本编码器决定。 |

---

## 7. 规范化实测日志 (Experiment Log)

所有个人测试记录均按统一标准化格式归档，注明复现范围：

### Log-001 · 浅色丝绸在纯白环境中的边缘溢出
- **Environment**: ComfyUI (Torch 2.4 + cu121)
- **Checkpoint**: Anima Aesthetic v2.0 FP16
- **Prompt condition**: `1girl, pure white silk dress, white background`
- **Parameter condition**: Steps: 28, CFG: 4.5, Sampler: DPM++ 2M Karras, Res: 832x1216
- **Observation**: 角色裙摆边缘与高光背景发生融色，边缘对比度丢失。
- **Resolution**: 补充 `soft subtle shadow drop behind character, warm ambient lighting` 后边缘轮廓清晰分离。
- **Confidence**: High
- **Scope**: 适用于浅色衣物配浅色/纯白背景构图。

### Log-002 · 前景角色与背景放大头像图层黏连
- **Environment**: ComfyUI
- **Checkpoint**: Anima Aesthetic v2.0
- **Prompt condition**: 未添加分层焦点限定词的 multi-view prompt
- **Parameter condition**: Steps: 25, CFG: 4.0, Sampler: Euler a
- **Observation**: 模型尝试将两个角色头像物理连接或绘制为双胞胎并排站立。
- **Resolution**: 显式加入 `foreground subject in sharp focus` 与 `background enlarged portrait in soft transparent wash` 建立景深阶级后分离成功。
- **Confidence**: High
- **Scope**: 适用于所有 Layered Showcase 多尺度排版任务。

### Log-003 · 极端质量词堆叠对色彩阶调的影响
- **Environment**: WebUI
- **Checkpoint**: Anima Base v1.1
- **Prompt condition**: 8 个以上 `masterpiece, 8k, ultra detailed, award winning` 前置
- **Parameter condition**: Steps: 30, CFG: 6.5, Sampler: Euler a
- **Observation**: 阴影过度变深且发灰，亮面高光出现色斑（Burned Artifacts）。
- **Confidence**: Medium
- **Scope**: 针对 CFG 处于 6.0 以上且质量修饰词过度堆叠的情况。
