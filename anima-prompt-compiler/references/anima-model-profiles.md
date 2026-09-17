# Anima Model Profiles & Tuning Reference

> **Version**: 1.2.0  
> **Last Updated**: 2026-09-17  
> **Maintainer**: Tera-Dark  
> **Scope**: Anima 模型族各版本特性、提示词语法、文本编码器兼容性与来源溯源

本文档为 `anima-prompt-compiler` 提供模型底层特性参考。所有规则均采用**证据分级与可溯源体系**，避免将偶然实验或未经充分验证的经验固化为绝对法则。

---

## 1. 证据分级体系与措辞规范 (Evidence Levels & Phrasing Standards)

为了确保知识库的严谨性与可复现性，本文档将内容严格划分为三级，并采用对应梯度的措辞：

| 证据级别 | 级别定义 | 规范化措辞标准 | 溯源要求 |
| :--- | :--- | :--- | :--- |
| 🟢 **Official** | 由模型发布者官方卡片、技术文档或官方提供的工作流明确确认的参数与架构规范。 | “官方文档明确指出... / Officially documented” | 必须包含来源 URL、对应版本号与核验日期。 |
| 🟡 **Community Practice** | 社区（Civitai, Discord, Hugging Face Discussions）大量创作者高频验证的常规经验，适用于多数常规场景，但无官方绝对保证。 | “在多个社区工作流中常见... / Commonly observed across community workflows” | 需注明适用场景与潜在例外。 |
| 🔵 **Personal Experiment** | 在特定本地硬件、特定前端（WebUI/ComfyUI）、单一 Checkpoint 与固定参数下观察到的实测现象。 | “在当前测试环境中观察到... / Observed under tested conditions” | 必须注明环境、参数、复现次数 (Replication Count) 与泛化范围。 |

---

## 2. 证据来源与溯源清单 (Sources & Provenance)

### Source-01 · 官方基础模型配置 (Official Baseline)
- **Type**: 🟢 Official
- **Model Family**: Anima Anime Foundation Models (Hugging Face / Civitai)
- **Verified On**: 2026-09-17
- **Officially Documented Points**:
  - 推荐 CFG Scale 范围为 **4.0 - 5.0**（过高易导致面部色块与对比度异常）；
  - 采用现代文本编码器架构，支持混合语法；
  - 严禁在 Prompt 文本内部输入模型调度参数。

### Source-02 · 社区多模型工作流经验汇总 (Community Synthesized)
- **Type**: 🟡 Community Practice
- **Source Context**: ComfyUI / SD-WebUI Anima 创作者社区日常反馈
- **Verified On**: 2026-09-17
- **Commonly Observed Patterns**:
  - 语序前置（Word Order Priority）比单纯提升括号数值权重更具稳定性；
  - 适度权重范围一般在 `(keyword:1.05)` 至 `(keyword:1.20)` 之间；
  - 空泛质量词（如 `masterpiece`, `8k`）在 Anima 中容易占用注意力预算，降低具体视觉描述的服从度。

---

## 3. 模型族特性参考矩阵 (Model Variants)

*注：特性表现为社区工作流综合表现总结，不同微调版本可能存在差异。*

| 模型变体 | 核心定位与训练导向 | 提示词敏感度 `[Community]` | 构图服从度 `[Community]` | 常见应用场景 |
| :--- | :--- | :--- | :--- | :--- |
| **Anima Base** | 动漫通用底模，泛化性良好，强调基础角色特征还原。 | 对 Tag 列表与短句组合适应良好；对复杂多重从句服从度中等。 | 居中立绘与标准景别表现稳定；复杂非对称构图需更明确的方位引导。 | OC 基础立绘、简单日常插画、通用动画角色生成。 |
| **Anima Aesthetic** | 专精于插画级艺术感、光影层次与高级笔触的微调版本。 | 对光影方向词（`rim light`, `volumetric lighting`）与负空间描述有良好响应。 | 在合理引导下，对浅景深、非对称偏置与展示板排版呈现良好适应力。 | 艺术插画、电影感海报、高定服设、画册级概念图。 |
| **Anima Turbo / Lightning** | 蒸馏高速版本，牺牲极少量微观细节换取快速收敛。 | 对提示词冲突较敏感，建议精炼高信息密度的 Tag 链。 | 适合单一主视角；多图分屏排版时需更严格的层级限定。 | 概念草图快速摸索、表情差分批量产出、快速原型迭代。 |

---

## 4. 文本编码器与前端兼容性 (Text Encoder & Frontend Compatibility)

> 🟢 **Official / Community Practice**

Do not assume traditional CLIP settings such as Clip Skip 2 apply to every Anima workflow. Follow the text encoder and frontend configuration supplied by the selected Anima checkpoint or workflow.

Do not place sampler, CFG, steps, or Clip Skip values inside the prompt unless the user explicitly asks for generation settings.

### 关键兼容性准则
1. **文本编码器差异**：部分现代 Anima 变体或衍生工作流采用 Qwen、T5 或双文本编码器架构，其对自然语言从句的解析能力强于早期单 CLIP 模型。不要机械套用传统 SD1.5 的“必须全逗号纯 Tag 语法”或“强制 Clip Skip 2”。
2. **生成参数隔离**：除非用户在输入中明确要求输出运行参数，否则**编译器严禁在输出的 Prompt 代码块内夹带 `--cfg`, `--steps`, `Sampler:` 等参数文本**。

---

## 5. 质量词与有效渲染描述 (Quality Tags & Cleaning)

### 5.1 推荐保留的有效渲染描述 `[Community Practice]`
在多个社区工作流中常见以下物理与视觉特征描述能有效增强细节：
- `fine anime lineart`：引导清晰利落的边缘线稿与闭合。
- `detailed fabric texture`：引导布料织物经纬与呢料肌理。
- `soft volumetric lighting` / `subsurface scattering`：引导皮肤半透明通透感与柔和光影过渡。
- `delicate eye highlight`：刻画瞳孔反光与折射层次，避免眼神呆板。

### 5.2 默认净化的空泛词 (Low-Information Tokens) `[Community Practice]`
以下词汇缺乏明确的空间、物理与色彩定义，已被主编译器过滤列表默认拦截：
```text
[BANNED TOKENS]
masterpiece, best quality, ultra high quality, 8k, 4k, insanely detailed, award winning,
perfect anatomy, perfect quality, incredible visual, wallpaper, trend on artstation
```
> **依据**：在社区实践中，大量堆叠上述词汇不仅无法带来确定的质感提升，反而容易挤占有效描述的注意力权重。

---

## 6. 工作流推荐参数参考 (Workflow Reference Presets)

*注：以下数值为常见基础设置参考，实际生产请以具体 Checkpoint 与发布者说明为准。*

| 参数项 | Anima Base / Aesthetic | Anima Turbo / Lightning | 证据分级与说明 |
| :--- | :--- | :--- | :--- |
| **CFG Scale** | **4.0 - 5.0** (官方推荐) | **1.5 - 2.5** | `[Official]` 官方文档明确建议保持在 4~5 区间，避免因过高对比导致画面生硬。 |
| **Steps** | 20 - 30 | 4 - 8 (视具体蒸馏模型) | `[Community Practice]` 步数通常取决于具体 Scheduler，超过 35 步后视觉差异通常较小。 |
| **Sampler** | Euler a / DPM++ 2M Karras | Euler / DPM++ SDE | `[Community Practice]` 依具体 Checkpoint 与环境习惯选用。 |
| **Clip Skip** | 由具体工作流配置决定 | 由具体工作流配置决定 | `[Official]` 遵循所选 Checkpoint 与文本编码器的官方推荐，严禁硬编码默认值。 |

---

## 7. 标准化实测日志 (Experiment Log)

所有个人测试记录均按统一标准化格式归档，明确复现次数与泛化边界：

### Log-001 · 浅色丝绸在纯白环境中的边缘溢出
- **Environment**: ComfyUI (Torch 2.4 + cu121)
- **Checkpoint**: Anima Aesthetic v2.0 FP16
- **Prompt condition**: `1girl, pure white silk dress, white background`
- **Parameter condition**: Steps: 28, CFG: 4.5, Sampler: DPM++ 2M Karras, Res: 832x1216
- **Observation**: 在当前测试环境中观察到角色裙摆边缘与高光背景发生融色，边缘对比度降低。
- **Resolution**: 补充 `soft subtle shadow drop behind character, warm ambient lighting` 后轮廓分离明显。
- **Confidence**: High
- **Replication Count**: 4
- **Generalizability**: Limited (主要适用于浅色衣物配浅色/纯白背景构图)

### Log-002 · 前景角色与背景放大头像图层黏连
- **Environment**: ComfyUI
- **Checkpoint**: Anima Aesthetic v2.0
- **Prompt condition**: 未添加分层焦点限定词的展示板 prompt
- **Parameter condition**: Steps: 25, CFG: 4.0, Sampler: Euler a
- **Observation**: 模型尝试将两个角色头像物理连接或绘制为双胞胎并排站立。
- **Resolution**: 显式加入 `foreground subject in sharp focus` 与 `background enlarged portrait in soft transparent wash` 建立景深阶级后分离成功。
- **Confidence**: High
- **Replication Count**: 5
- **Generalizability**: Broad (适用于多尺度分层展示板场景)

### Log-003 · 极端质量词堆叠对色彩阶调的影响
- **Environment**: WebUI
- **Checkpoint**: Anima Base v1.1
- **Prompt condition**: 8 个以上 `masterpiece, 8k, ultra detailed, award winning` 前置
- **Parameter condition**: Steps: 30, CFG: 6.5, Sampler: Euler a
- **Observation**: 在当前测试环境中观察到阴影发灰，受光面高光区出现明显色斑。
- **Confidence**: Medium
- **Replication Count**: 2
- **Generalizability**: Limited (在特定高 CFG 与大量修饰词条件下更易观察到)
