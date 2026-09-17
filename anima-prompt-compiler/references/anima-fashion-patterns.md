# Anima Fashion Patterns & Garment Library

本文档为 `anima-prompt-compiler` 的专用服设参考知识库。提供日常女装、叠穿层级、非对称解构剪影与高级材质组合的可视化英文模式与词汇库。

---

## 1. 穿搭风格原型与剪影范式 (Style Archetypes & Silhouettes)

| 风格原型 | 核心剪影特征 (Silhouette) | 常用色彩与层次 | 典型英文引导短语 |
| :--- | :--- | :--- | :--- |
| **松弛高级日常 (Elevated Casual)** | 宽适垂坠（Oversized drape）、落肩茧形、上宽下窄或直筒松弛感。 | 低饱和度单色系（燕麦色、烟熏灰、鼠尾草绿、奶白）。 | `relaxed silhouette, drop-shoulder loose tailoring, effortless layered casual wear` |
| **都市高智轻职场 (Modern Sartorial)** | 利落平直肩线、收腰线条微收、垂直垂顺的长裤或中长裙。 | 炭黑、藏青、驼色、象牙白、冷灰。 | `crisp structured tailoring, tailored longline blazer, pleated wide-leg trousers` |
| **甜酷解构少女 (Street Deconstructed)** | 紧身内搭 × 夸张膨胀外披，短款露脐/不对称短裙 × 战术工装细节。 | 灰粉配纯黑、冷白配水泥灰、局部金属扣件反光。 | `cropped silhouette paired with oversized outerwear, utility straps, street deconstructed` |
| **新中式克制雅致 (Neo-Oriental Chic)** | 斜襟微盘扣、极简立领、不对称交领、开叉水袖。 | 浅赭、竹青、墨黑、月白。 | `mandarin collar accent, modern asymmetrical crossover flap, flowing elongated sleeves` |
| **高级晚宴/概念礼服 (Atelier Couture)** | 建筑感雕塑轮廓、鱼尾延展、大面积负空间露背或深 V、不对称垂褶。 | 曜石黑、香槟金、极夜深蓝、真丝哑光象牙色。 | `architectural drape, asymmetric one-shoulder evening gown, sculptural fabric folds` |

---

## 2. 四层叠穿架构模型 (4-Tier Layering System)

叠穿是消除 AI 服装“平涂塑料片假感”最有效的手段。Prompt 编译应依序遵循从内到外的物理装配逻辑：

```text
Tier 1: Base Layer (贴身内搭)
   ↓
Tier 2: Mid Layer (中间调和层/开衫/马甲)
   ↓
Tier 3: Outer Shell (外套廓形/风衣/大衣)
   ↓
Tier 4: Micro Accessories (五金扣件/围巾/束带/首饰)
```

### 2.1 实战叠穿组合模式 (Layering Presets)
- **模式 A · 慵懒冬日叠穿**：
  `wearing a fitted cream ribbed knit turtleneck under an open oversized charcoal wool blazer, layered with an ivory chunky cable-knit scarf loosely draped over the shoulder`
- **模式 B · 解构街头层次**：
  `wearing a sheer black mesh long-sleeve crop top under an asymmetric cropped utility vest, paired with high-waisted pleated wide trousers cinched with a buckled leather strap`
- **模式 C · 春夏轻盈通透叠穿**：
  `wearing a delicate white silk camisole under a semi-sheer sage-green organza button-up shirt with rolled cuffs, leaving the top collar buttons unfastened`

---

## 3. 非对称平衡与破规解构 (Asymmetry & Deconstruction)

避免居中对称造成的僵硬假人感，通过局部单侧失衡制造高级灵动视觉张力：

- **单肩与领口不对称 (Asymmetrical Neckline)**：
  - `one-shoulder off-the-shoulder neckline exposing one collarbone`
  - `slanted asymmetric lapel with uneven button placket`
  - `single draped cowl neck falling gently to the left`
- **下摆与开衩剪裁 (Uneven Hemlines & Slits)**：
  - `high-low staggered hemline with raw finished edge`
  - `deep side thigh slit revealing inner pleated underskirt`
  - `diagonal wrap skirt with asymmetrical fabric overlap`
- **饰品与装饰失衡 (Displaced Accents)**：
  - `a single statement silver drop earring on the left ear only`
  - `single leather arm belt wrapped twice around the right bicep`
  - `half-tucked shirt front with one side falling naturally long`

---

## 4. 高级感材质碰撞矩阵 (Material Juxtaposition)

质感源自两种截然相反的物理表面特性在同一画面上的对话：

| 材质对抗组 | 核心物理特质 | 视觉互补效果 | 编译推荐词 |
| :--- | :--- | :--- | :--- |
| **吸光重呢 × 灵动丝缎** | 极黑粗纺羊毛（0 反光）× 珍珠光泽桑蚕丝（微镜面） | 压住画面的同时赋予流动的高光焦点。 | `matte heavy boiled wool coat against lustrous pearl-white silk inner slip` |
| **粗粝针织 × 平滑硬质皮革** | 粗棒针浮雕罗纹（起伏阴影）× 细腻油蜡牛皮（利落硬边） | 软硬碰撞，丰富微观空间层次。 | `chunky ribbed cable-knit sweater paired with sleek waxed leather pencil skirt` |
| **半透欧根纱 × 哑光金属五金** | 半透明雾化透光（轻盈飘逸）× 磨砂拉丝银/古铜扣件（重量感） | 既有空灵呼吸感，又有工业严谨度。 | `delicate sheer organza puff sleeves fastened with brushed matte titanium buckle cuffs` |
| **水洗旧棉麻 × 漆面光泽配饰** | 自然植物纤维褶皱与微结 × 高亮镜面漆皮手袋或切面树脂 | 人文生活真实度与现代设计感的融合。 | `washed wrinkled linen tunic complemented by polished patent leather shoulder strap` |

---

## 5. 服装饰品与微观部件词汇速查 (Garment Lexicon)

### 领型 (Necklines & Collars)
- `boat neckline (一字领)` · `mock turtleneck (半高领)` · `peter pan collar with rounded edges (彼得潘圆领)` · `structured notched lapel (西装平驳领)` · `mandarin stand collar (中式立领)`

### 袖型 (Sleeves)
- `bishop sleeves gathered at cuffs (主教袖)` · `extended lantern sleeves (灯笼袖)` · `dropped shoulder seam (落肩线)` · `raglan sleeves with contrast piping (插肩袖)` · `tailored slim sleeves reaching mid-palm (微盖手背修长袖)`

### 腰部与裙身 (Waist & Skirts)
- `paperbag high waist with soft gather (纸袋高腰)` · `knife-pleated midi skirt (工整风琴褶中长裙)` · `tailored high-waisted cigarette pants (九分烟管裤)` · `balloon silhouette volume skirt (气球花苞廓形裙)`
