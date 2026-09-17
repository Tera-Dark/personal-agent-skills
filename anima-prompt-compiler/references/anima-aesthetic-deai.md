# Anima Aesthetic & De-AI Engine Reference

本文档为 `anima-prompt-compiler` 的美学增强与“去 AI 塑料感”决策知识库。将人类大师级美学思维解耦为**模块化、按需调用**的策略池，彻底告别“无论什么需求都强制套用 30% 留白 + 单一刺点色 + 失焦沉思”的单一呆板套路。

---

## 1. 核心去 AI 味六大美学维度 (The 6 Master Aesthetic Pillars)

AI 绘图最致命的通病是**“平庸工业味”**：全局无衰减的塑料反光、细节均分无视线落脚点、无机磨皮假人、僵硬居中迎合镜头的微笑。以下六大维度作为美学底层逻辑，供主编译器按需抽取与注入：

```text
       ┌───────────────────────┐
       │   Master De-AI Pillars│
       └───────────┬───────────┘
   ┌───────────────┼───────────────┬───────────────┐
   ▼               ▼               ▼               ▼
[光学与明暗衰减]  [微观材质与瑕疵]  [负空间呼吸律]  [色彩阶级与刺点]
   ▼               ▼
[电影作者机位]    [去表演化真实神态]
```

1. **明暗对照与光学真实衰减 (Chiaroscuro & Natural Falloff)**：
   - 确立明确的物理主光源（侧窗自然光、顶光漫射、低角度夕阳），坚决废除无处不在的发光轮廓与全局光污染。
   - 允许画面存在自然的**阴影沉降区 (Shadow Drop)**，暗部敢于压暗以形成深度。
2. **侘寂美学与微观真实瑕疵 (Wabi-sabi & Tactility)**：
   - 拒绝千篇一律的无机磨皮塑料质感。显式引入真实的物理触感：微小的发丝凌乱、织物经纬微绒、空气微尘、受光面半透明红润感（SSS 透光）。
3. **负空间与留白呼吸律 (Negative Space & Visual Respite)**：
   - 画面必须有“视觉休止区”（低密度色场、大光圈散景融化区或暗色过渡），形成“密不透风 vs 疏可走马”的节奏。
4. **色彩统治阶级与刺点理论 (Color Hierarchy & The Punctum)**：
   - 建立约 70% 的基底色调统摄全场，辅以 25% 结构色，严控 ≤5% 的高对比刺点色作为视觉第一锚点，杜绝杂乱高饱和。
5. **电影作者意识构图 (Auteur Framing)**：
   - 突破死板证件照。运用三分黄金偏置、前景遮挡虚化（Sub-framing）、非对称裁切等镜头语言。
6. **去表演化与真实定格 (Unperformed Candid Stance)**：
   - 角色脱离对镜头的刻意迎合与做作假笑，进入沉思、专注动作、或自然的微表情切片。

---

## 2. 五大模块化美学风格预设 (Modular Aesthetic Presets)

编译器在执行任务时，**根据用户需求与画风偏好动态路由**，匹配最恰当的美学方案：

### Preset A · 商业头像与社交立绘 (Commercial & Clean Avatar)
- **设计诉求**：亲和、明亮清爽、构图端庄、适度对比、面部结构清晰。
- **美学调节**：
  - *光影*：柔和侧前方三点布光，轻微眼神光，阴影极柔和过渡。
  - *色彩*：明快干净的自然肤色，主色调明亮统一。
  - *神态*：自然灵动的微表情（自信从容的温和注视、嘴角微扬），脱离呆板假人微笑。
  - *负空间*：背景为极简浅灰/米白柔焦色场，让视觉 100% 聚焦于面部和领口。
- **推荐 Prompt 编译片段**：
  `commercial studio portrait, soft key light with gentle ambient fill, crisp facial features, delicate catchlight in eyes, natural gentle expression, subtle smile, clean muted backdrop, shallow depth of field`

---

### Preset B · 元气甜美与清新日系 (Sweet, Vibrant & Kawaii)
- **设计诉求**：生动活泼、通透空气感、青春元气、避免沉重阴暗。
- **美学调节**：
  - *光影*：高调光（High-Key Lighting），清晨日光漫射，发丝透光金边（Rim light），无死黑重阴影。
  - *色彩*：奶油色、草莓粉、奶杏、薄荷绿等马卡龙低饱和微温色系，轻盈灵动。
  - *微瑕与质感*：空气感蓬松发丝、少女面颊微透血色、软糯针织或轻薄棉麻质感。
  - *神态*：动态抓拍感（歪头轻笑、吹泡泡、双手抱膝、微风吹乱刘海的瞬间），生动不油腻。
- **推荐 Prompt 编译片段**：
  `bright high-key daytime lighting, airy atmosphere, soft pastel and cream color palette, wind-blown fluffy hair wisps, natural lively smile, blushing translucent cheeks, candid snapshot moment, cheerful charming energy`

---

### Preset C · 高级时尚服设与冷淡极简 (Atelier Fashion & Sartorial Minimal)
- **设计诉求**：大牌秀场感、冷峻利落、突出服装廓形结构与面料对抗。
- **美学调节**：
  - *光影*：雕塑感硬质侧光或阴天极度平滑漫射，精确勾勒衣服剪影。
  - *色彩*：黑白灰、驼色、炭灰统治全局（Morandi / Monochrome），仅以金属拉丝银或皮革作为点缀。
  - *构图与非对称*：全身或大半身站姿，单侧垂坠、解构落肩，大面积几何留白。
  - *神态*：冷峻、疏离放空、高级厌世脸、视线投向画外。
- **推荐 Prompt 编译片段**：
  `high-fashion editorial lookbook, architectural garment silhouette, structured tailoring, matte wool contrasting with lustrous satin, monochrome palette with charcoal and ivory, distant aloof gaze, sculptural lighting, generous minimalist negative space`

---

### Preset D · 暗黑叙事插画与戏剧张力 (Dark Narrative & Tenebrism)
- **设计诉求**：故事感厚重、张力拉满、神秘、深刻、电影质感。
- **美学调节**：
  - *光影*：**卡拉瓦乔式极端暗色调（Tenebrism）**，单束强光如刀割般切开纯黑暗场，大面积阴影自然吞没下半身。
  - *色彩*：深墨绿、玄黑、曜石灰占 80%，唯一一处鲜红（如玫瑰、伤痕、红瞳或发饰）作为**刺点色（The Punctum）**。
  - *质感*：破损、风化、微湿水痕、金属反光与粗糙呢料对抗。
  - *神态*：沉重思索、眼神警惕、防备、或疲惫的松弛。
- **推荐 Prompt 编译片段**：
  `tenebrism chiaroscuro, single dramatic shaft of light cutting through heavy deep shadows, 80% pitch black and charcoal base, lone crimson punctum accent, weary intense gaze, moody atmospheric dust particles, cinematic narrative tension`

---

### Preset E · 电影感作者海报 (Cinematic Auteur Poster)
- **设计诉求**：王家卫/索尔·雷特式电影剧照、生活碎片、胶片复古叙事。
- **美学调节**：
  - *光影*：雨夜街灯反光、隔窗水汽折射、车灯冷暖色温对抗（Teal & Orange）。
  - *构图*：2.39:1 或 16:9 横画幅，前景水珠玻璃遮挡偷窥构图（Sub-framing），人物偏置三分线。
  - *质感*：35mm 胶片细腻银盐颗粒感、微润反光地表。
  - *神态*：失焦出神、注视雨滴滑落、不表演的纯粹时间切片。
- **推荐 Prompt 编译片段**：
  `cinematic 35mm film still, Saul Leiter atmospheric style, viewed through rain-streaked window with soft chromatic reflections, moody teal and warm amber tone contrast, character lost in thought, cinematic frame crop, fine film grain`

---

## 3. 编译器策略选择决策流 (Compiler Decision Flow)

```text
[用户输入意图]
       │
       ├─► 想要日常甜美/可爱/元气角色？ ────► 激活 Preset B (High-key, Pastel, Air-light)
       ├─► 想要商业头像/推特头像/OC正脸？ ──► 激活 Preset A (Clean, Gentle catchlight, Studio)
       ├─► 想要高定穿搭/高级服装展示？ ────► 激活 Preset C (Architectural, Matte vs Lustrous)
       ├─► 想要厚重世界观/黑深残/情绪张力？ ─► 激活 Preset D (Tenebrism, Single Punctum)
       ├─► 想要电影故事/剧照抓拍/复古氛围？ ─► 激活 Preset E (Film grain, Sub-framing, Candid)
       └─► 未明确指定美学倾向？ ──────────► 保持中立均衡，仅注入基础物理主光与材质微瑕
```
