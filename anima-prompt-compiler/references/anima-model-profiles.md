# Anima Model Profiles & Tuning Reference

本文档记录 **Anima 系列动漫图像生成模型** 的版本特性、质量词语法、权重敏感度以及出图工作流参数实验沉淀。供 `anima-prompt-compiler` 在面对不同部署环境和模型变体时精准编译。

---

## 1. 模型族特性对比矩阵 (Model Variants)

| 模型变体 | 核心训练导向 | 提示词敏感度 | 构图服从度 | 典型适用场景 |
| :--- | :--- | :--- | :--- | :--- |
| **Anima Base** | 通用动漫基础底模，泛化性极佳，擅长标准立绘与角色基础特征还原。 | 偏向 Tag 列表 + 短句混合。对自然语言长从句服从度中等。 | 良好。标准大景深与居中构图极其稳定，复杂非对称需要强词引导。 | OC 基础立绘、简单日常插画、通用动画角色生成。 |
| **Anima Aesthetic** | 专精于插画级艺术感、光影层次与高级笔触，经过高审美微调。 | **极高**。擅长识别光影方向（如 `rim light`, `chiaroscuro`）与氛围词，减少了对质量硬词的依赖。 | 极强。对景深、负空间、电影裁切与多尺度展示板响应极佳。 | 艺术插画、电影感海报、高定服设、画册级概念图。 |
| **Anima Turbo / Lightning** | 极速蒸馏版本（4~8 步收敛），牺牲了少量微观纹理以换取极致生成速度。 | 中等偏脆。容易受到过多形容词冲突的干扰；建议精简高效的 Tag 链。 | 中等。建议采用单一主视角，避免极度复杂的局部多图拼接。 | 概念草图快速摸索、表情差分批量产出、实时交互迭代。 |

---

## 2. 质量词体系与有效性实验记录 (Quality Tags & Cleaning)

Anima 经历了对动漫美学与真实物理渲染的双向训练，传统 SD1.5 时代的“词海堆叠法”在 Anima 中往往会造成**过拟合、高对比色块崩坏和过度锐化**。

### 2.1 推荐保留的“有效渲染描述” (Effective Render Anchors)
这些词汇在 Anima 内部具有明确的特征引导，能提升质感而不会破坏画面结构：

- `fine anime lineart`：强化干净纯正的动漫线稿与边缘闭合度。
- `detailed fabric texture`：增强衣物织物微观经纬、呢料微绒感，消除塑料磨皮感。
- `soft volumetric lighting` / `subsurface scattering`：赋予皮肤通透感与柔和的体积光穿透。
- `delicate eye highlight`：精细刻画瞳孔反光与折射层级，避免眼神死板空洞。
- `clean cel shading with soft gradients`：平滑的赛璐璐与柔和渐变过渡，兼具动漫感与层次感。

### 2.2 强烈建议废弃的“无效垃圾词” (Dirty Flooding Tokens)
以下词汇**已被主编译器过滤列表默认拦截**，禁止加入编译输出：

```text
[BANNED TOKENS]
masterpiece, best quality, ultra high quality, 8k, 4k, insanely detailed, award winning,
perfect anatomy, perfect quality, incredible visual, wallpaper, trend on artstation
```
> **实验结论**：在 Anima Aesthetic 中输入 8 个无意义质量最高级修饰词，会导致画面对比度虚高（Burned High Contrast），人物脸部受光面失去阶调，暗部细节大量死黑。

---

## 3. 提示词权重与语法兼容性 (Syntax & Weights)

不同前端工具（WebUI、ComfyUI、NovelAI、Civitai Generator）对权重的解析方式有所不同：

### 3.1 标准通用权重格式 (Universal Syntax)
- **圆括号线性权重**：`(keyword:1.1)` 到 `(keyword:1.25)` 为安全有效区间。
- **阈值警示**：超过 `1.3` 极易引发肢体畸形、边缘撕裂或色彩溢出；低于 `0.8` 基本被全局平均化忽略。
- **默认原则**：在 `anima-prompt-compiler` 默认编译中，**优先依赖语序前置（Word Order Priority）** 而非滥用数值权重。前置 15% 的词拥有天然的最高注意力。

### 3.2 标签与自然语言混合模式 (Hybrid Grammar)
Anima 模型表现最佳的语法结构为 **“锚点 Tag + 紧密视觉短语 + 氛围从句”**：

```text
[结构示范]
1girl, [Core Appearance], wearing [Layered Fashion], [Pose & Camera], [Lighting & Shadow], [Atmospheric Environment]
```
- **核心身份区**（前 1~20 词）：保持 Tag 简练，锁定发色、瞳色、种族特征。
- **服设与构图区**（20~60 词）：采用连贯的形容词短语（如 `oversized charcoal wool coat over high-collar white linen shirt`）。
- **光影与空间区**（60~90 词）：采用自然语言短句赋予留白与空间感。

---

## 4. 推荐生成参数基准 (Recommended Generation Presets)

| 参数项 | Anima Base / Aesthetic | Anima Turbo | 避坑与说明 |
| :--- | :--- | :--- | :--- |
| **Sampler** | DPM++ 2M Karras / Euler a | Euler / DPM++ SDE Karras | 复杂服设与光影优先选择 DPM++ 2M Karras。 |
| **Steps** | 24 - 32 | 4 - 8 | 步数超过 40 会导致线稿过度锐化与杂色。 |
| **CFG Scale** | 5.0 - 7.0 (推荐 5.5 - 6.0) | 1.5 - 2.5 | **CFG 严禁超过 8.0**，否则引发全局发光塑料病与脸部崩坏。 |
| **Clip Skip** | 2 | 2 | 动漫类模型的行业标准设置，跳过最后一层保证画风纯正。 |
| **分辨率建议** | 832x1216 (3:4), 896x1152 (1:1.3) | 832x1216 | 避免非标准长宽比导致的断肢多头问题。 |

---

## 5. 持续调优与实测日志 (Empirical Log)

- **[Log-01] 浅色系服饰溢出**：当角色服装指定 `pure white silk dress` 时，若背景未设定暗部支撑，易导致整体画面过曝失真。**解决方案**：追加 `soft shadow drop behind, balanced ambient tone` 形成对比度锚点。
- **[Log-02] 双人/多图展示板混乱**：在编译“前景全身 + 背景放大头像”展示板时，未明确定义景深易导致两个头像融合。**解决方案**：严格使用 `foreground subject with crisp focus, semi-transparent blurred background portrait` 进行层级切分。
- **[Log-03] 负向提示词依赖消除**：无需在 Negative Prompt 填写大量 anatomy 标签，只需在正向提示词中精准指明姿态（如 `relaxed arms, hand resting on hip, clear finger definition`）即可大幅提升肢体稳定性。
