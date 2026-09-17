# Anima Composition Patterns & Layout Protocols

本文档为 `anima-prompt-compiler` 的构图与版式排版参考协议。定义了全身立绘、半身肖像、角色展示板、特别是**“前景完整角色 + 背景放大头像”**等多尺度混合构图的稳定引导策略。

---

## 1. 基础景别与视平线协议 (Camera Framing & Eye-Levels)

| 景别类型 | 适用目标 | 画面范围与视觉焦点 | 核心编译短语 (Core Tags & Phrases) |
| :--- | :--- | :--- | :--- |
| **全身立绘 (Full Body)** | OC 设定立绘、鞋袜与服装整体剪影展示。 | 从头顶到鞋底完整呈现，保留脚底着地阴影。 | `full length full body standing, feet visible on ground with grounded shadow drop, complete character silhouette, generous vertical framing` |
| **大半身/牛仔景别 (Cowboy Shot / Three-Quarter)** | 日常插画、动作表现、腰部手部细节与上装层次。 | 从大腿中部至头顶，兼顾神态、手势与腰部服设。 | `cowboy shot, three-quarter portrait, captured from mid-thigh up, natural hand placement, dynamic torso posture` |
| **半身肖像 (Upper Body / Medium Close-up)** | 社交头像、对话立绘、领口叠穿与微表情。 | 胸部至头部，突出面部微观肌理与眼眸反光。 | `upper body portrait, focus on expressive eyes and neckwear, shallow depth of field softly blurring the background` |
| **电影特写 (Tight Cinematic Close-up)** | 情绪爆发、故事高潮、局部微观细节。 | 聚焦面部局部或眼神微动作，边缘利落裁切。 | `cinematic close-up, cropped forehead, deep eye reflection, macro facial texture, emotional storytelling` |

---

## 2. 特色高阶构图：多尺度分层展示 (Layered Showcase: Foreground + Background Portrait)

这是角色设计与高级海报中最受欢迎的构图模式：**前景为一个完整的全身或大半身全身立绘，背景叠加一个大尺寸半透明或柔焦的人物放大特写肖像**。

### 2.1 结构解耦原则 (Decoupling Rules)
若不加约束直接生成，模型容易将两个人像混淆成双胞胎或出现肢体黏连。必须严格通过**焦点深度、对比度衰减与色彩明度差**进行硬隔离：

```text
[视觉层级分布]
Layer 1 (Foreground Foreground): 主体角色 (Sharp, Full Color, 100% Contrast)
Layer 2 (Background Backdrop): 放大头像 (Soft, Enlarged, Low Contrast, Semi-transparent/Muted)
Layer 3 (Ambient Canvas): 留白背景场 (Subtle Grain, Minimalist Gradient, Negative Space)
```

### 2.2 核心编译模板 (Prompt Blueprint)
```text
layered character design presentation layout,
[FOREGROUND]: a sharp full-body shot of the 1girl standing in the front right, dynamic silhouette, crisp edges, rich detailed garment textures and natural shadows,
[BACKGROUND]: a dramatically enlarged soft-focus close-up portrait of the same character's face in the upper background, semi-transparent fade, lowered contrast, gentle monochrome or muted wash,
[LAYOUT]: clean minimalist graphic design sensibility, elegant negative space separation between layers, no cluttered icons, unified lighting direction
```

---

## 3. 角色设定展示板与表情差分 (Character Presentation Sheets)

### 3.1 设定三视图 / 多姿态展示板 (Model Sheet / Multi-View)
适用于完整的服装与角色设计归档：
- **编译策略**：强调“同同一角色的设计参考图（Reference Sheet）”，使用网格化或留白排版。
- **模板词**：
  `character design sheet, reference model sheet, showing multiple poses of the same 1girl, front view, side profile, neat presentation layout on clean muted grey background, minimal typography space, consistent character features and hair styling`

### 3.2 表情差分研究板 (Expression Study Sheet)
适用于游戏立绘或表情包设计：
- **编译策略**：锁定核心发型与服装，仅微调五官与情绪，通常限定为 3~4 个独立头像。
- **模板词**：
  `expression study sheet, clean organized layout featuring 4 distinct facial expressions of the same character, subtle smirk, contemplative gaze, gentle smile, surprised wide eyes, neatly arranged with generous whitespace, crisp lineart`

---

## 4. 空间景深衰减与非对称布局 (Spatial Depth & Asymmetry)

### 4.1 三分法黄金偏置 (Rule of Thirds Offset)
打破无趣的居中大头证件照：
- `character positioned strictly along the right third grid line, facing toward the open empty space on the left, dramatic compositional balance, extensive negative space`

### 4.2 前景虚化框架构图 (Sub-Framing / Dirty Foreground)
通过前景遮挡物营造第一人称窥视感与纪实电影感：
- `viewed through a blurred foreground frame, shallow focus, out-of-focus window frame and translucent rain droplets in the near edge, character sharply focused in the midground`

### 4.3 视平线戏剧落差 (Extreme Angles)
- **低机位仰拍 (Low-Angle Hero Shot)**：
  `dramatic low-angle shot from knee level looking up, soaring perspective, character silhouetted against a vast pale overcast sky, powerful grounded presence`
- **高机位俯拍 (High-Angle Narrative Shot)**：
  `bird's-eye perspective looking down, top-down tilted framing, character curled softly or seated, foreshortened limbs, delicate vulnerable mood`
