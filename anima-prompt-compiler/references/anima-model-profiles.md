# Anima Model Profiles & Tuning Reference

> **Version**: 1.3.0  
> **Last Updated**: 2026-09-17  
> **Maintainer**: Tera-Dark  
> **Scope**: Anima 模型族各版本特性、提示词语法、文本编码器兼容性与来源溯源

本文档为 `anima-prompt-compiler` 提供模型底层特性参考。所有规则均采用**证据分级与可溯源体系**，严格区分官方事实、兼容性工程规范与社区经验，严禁未经查证随意贴标。

---

## 1. 证据分级体系与措辞规范 (Evidence Levels & Phrasing Standards)

| 证据级别 | 级别定义 | 规范化措辞标准 | 溯源要求 |
| :--- | :--- | :--- | :--- |
| 🟢 **Official** | 由模型官方发布卡片、技术文档或官方工作流直接确认的规范。 | “官方文档明确指出... / Officially documented” | 必须包含来源 URL/Repository、对应版本与核验日期；**若无确切官方链接则不可标记为 Official**。 |
| 🔵 **Compatibility Guidance** | 保证多客户端与多前端工程兼容的约束规范（如参数隔离）。 | “遵循工作流兼容原则... / Follow compatibility guidance” | 说明工程解耦理由与目标前端。 |
| 🟡 **Community Practice** | 社区创作者在广泛实践中总结的通用模式，适用于多数常规场景，但无官方绝对保证。 | “在多个社区工作流中常见... / Commonly observed across community workflows” | 注明适用场景与潜在例外。 |
| 🟣 **Personal Experiment** | 在特定本地硬件、特定前端与固定参数下观察到的实测现象。 | “在当前测试环境中观察到... / Observed under tested conditions” | 必须注明环境、参数、复现次数 (Replication Count) 与泛化范围。 |

---

## 2. 证据来源与溯源清单 (Sources & Provenance)

### Source-01 · 官方模型卡片与基线 (Official Model Card Facts)
- **Type**: 🟢 Official
- **Source Repository**: [Hugging Face: Cirno/Anima](https://huggingface.co/Cirno/Anima)
- **Source Section**: Model Card & Release Notes
- **Verified On**: 2026-09-17
- **Applies To**: Anima Base / Aesthetic release checkpoints
- **Officially Documented Points**:
  - 基础模型推荐 CFG Scale 范围为 **4.0 - 5.0**（官方明确指出过高易导致过度对比与脸部高光色块）；
  - 核心架构基于高质量动漫插画与概念设计数据集微调；
  - 推荐分辨率基准以 832x1216 (3:4) 等为主。

### Source-02 · 工作流与工程兼容性指南 (Workflow Compatibility Guidance)
- **Type**: 🔵 Compatibility Guidance
- **Context**: 跨 ComfyUI, WebUI, Diffusers 前端集成标准
- **Verified On**: 2026-09-17
- **Engineering Principles**:
  - **参数与提示词解耦**：严禁在 Prompt 文本内部夹带 `--cfg`, `--steps`, `Sampler:` 等调度参数，保持提示词在不同 WebUI/API 间的纯净移植性；
  - **文本编码器自适应**：部分微调变体或自制工作流采用不同文本编码器（如 Qwen 系列、T5 或双 CLIP），不得将特定 SD1.5 的 Clip Skip 强制套用为全局必须项。

### Source-03 · 社区提示词通用实践 (Community Prompting Practices)
- **Type**: 🟡 Community Practice
- **Source Context**: Civitai / Liblib / Discord 创作者日常测试总结
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

> 🔵 **Compatibility Guidance**

Do not assume traditional CLIP settings such as Clip Skip 2 apply to every Anima workflow. Follow the text encoder and frontend configuration supplied by the selected Anima checkpoint or workflow.

Do not place sampler, CFG, steps, or Clip Skip values inside the prompt unless the user explicitly asks for generation settings.

### 关键兼容性准则
1. **文本编码器自适应**：现代衍生工作流若采用更强上下文能力的文本编码器（如 Qwen、T5），支持更自然的英文长句；若使用标准 CLIP，则对结构化视觉短语与前置 Tag 更敏感。
2. **生成参数隔离**：除非用户明确要求输出环境参数，否则**编译器输出的 Prompt 代码块仅包含视觉描述本身**。

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
| **CFG Scale** | **4.0 - 5.0** (官方推荐) | **1.5 - 2.5** | `[Official]` 官方模型发布说明建议保持在 4~5 区间，避免因过高对比导致画面生硬。 |
| **Steps** | 20 - 30 | 4 - 8 (视具体蒸馏方案) | `[Community Practice]` 步数通常取决于具体 Scheduler，多数情况下 25 步已足够收敛。 |
| **Sampler** | Euler a / DPM++ 2M Karras | Euler / DPM++ SDE | `[Community Practice]` 依具体 Checkpoint 与环境习惯选用。 |
| **Clip Skip** | 由具体工作流配置决定 | 由具体工作流配置决定 | `[Compatibility Guidance]` 遵循所选工作流与文本编码器官方推荐，严禁硬编码默认值。 |

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
