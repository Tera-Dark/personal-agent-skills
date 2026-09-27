# 核心验证测试集 (Test Suite)

> **Version**: 2.0.0  
> **Last Updated**: 2026-09-17  
> **Scope**: 验证编译器在多场景下的属性锁定、语言转换、V1/V2 分离、事实一致性、词数弹性与正向约束能力。

---

## 1. 统一人工评分标准体系 (Evaluation Rubric)

在执行基准回归测试时，依照以下 6 个核心维度对编译输出进行 Pass / Fail 评估：

| 评估维度 (Dimension) | 合格判定标准 (Pass Criteria) | 不合格判定 (Fail Signs) |
| :--- | :--- | :--- |
| **Identity Preservation** | 发色、瞳色、种族与显式外观特征 100% 保持一致。 | 擅自改变发色、瞳色或丢失关键特征。 |
| **Outfit Attribute Binding** | 服装内外层材质与颜色紧密物理绑定，无穿插融色。 | 外套颜色渗入内搭，领口材质混淆。 |
| **Spatial & Layout Clarity** | 景别、构图、背景散景或展示板多图层隔离分明。 | 多图展示板生成双胞胎，或背景喧宾夺主。 |
| **Unrequested Additions** | 未主动脑补未授权的世界观、机械配件或异质设定。 | 擅自增加用户未要求的赛博朋克配件或复杂翅膀。 |
| **V1/V2 Fact Consistency** | V2 美学增强版未篡改 V1 锁定的核心事实（除非标注为可选变体）。 | V2 将 V1 的白发改为金发，或将短裙改为长裤。 |
| **Output Contract** | 遵循当前模式契约，无独立负向词，无禁止质量词，格式正确。 | 出现 `masterpiece` 废词，或夹带独立 Negative 代码块。 |

---

## 2. 基准测试用例集 (Benchmark Test Cases)

### Test-01: 角色属性锁定与未确定信息开放
- **用户输入**：
  > “帮我生成一个银发红瞳的吸血鬼少女，穿黑色维多利亚长裙，神情安静，站在古堡月光下。”
- **预期模式**：Standard Mode
- **评分记录表 (Evaluation Record)**：
  ```markdown
  - [ ] Identity Preservation: Pass / Fail
  - [ ] Outfit Attribute Binding: Pass / Fail
  - [ ] Spatial Clarity: Pass / Fail
  - [ ] Unrequested Additions: Pass / Fail
  - [ ] V1/V2 Fact Consistency: Pass / Fail
  - [ ] Output Contract: Pass / Fail
  - Notes:
  ```

---

### Test-02: 4 层复杂服装叠穿与高级材质碰撞
- **用户输入**：
  > “设计一套冬日高级感穿搭：内搭米色针织高领毛衣，外面套深灰开衫西装，再披一件重磅黑色粗呢大衣，围着燕麦色围巾，下身直筒西装裤。”
- **预期模式**：Standard Mode | Aesthetic: Preset C (High Fashion, see 02_creation/illustration-direction/references/atmosphere-presets.md)
- **评分记录表 (Evaluation Record)**：
  ```markdown
  - [ ] Identity Preservation: Pass / Fail
  - [ ] Outfit Attribute Binding: Pass / Fail
  - [ ] Spatial Clarity: Pass / Fail
  - [ ] Unrequested Additions: Pass / Fail
  - [ ] V1/V2 Fact Consistency: Pass / Fail
  - [ ] Output Contract: Pass / Fail
  - Notes:
  ```

---

### Test-03: 前景立绘 + 背景放大头像多尺度展示板
- **用户输入**：
  > “帮我做一张角色设计展示图：前面是这个角色的完整全身立绘，背景放一个她的大尺寸半透明虚化头像，突出眼神和耳坠。”
- **预期模式**：Standard Mode | Mode: Layered Character Showcase
- **评分记录表 (Evaluation Record)**：
  ```markdown
  - [ ] Identity Preservation: Pass / Fail
  - [ ] Outfit Attribute Binding: Pass / Fail
  - [ ] Spatial Clarity: Pass / Fail
  - [ ] Unrequested Additions: Pass / Fail
  - [ ] V1/V2 Fact Consistency: Pass / Fail
  - [ ] Output Contract: Pass / Fail
  - Notes:
  ```

---

### Test-04: 浅色服饰与纯白背景防边缘融色
- **用户输入**：
  > “纯白背景，一个穿白色真丝吊带裙的女孩，全身照，不要多余杂物。”
- **预期模式**：Direct Mode 或 Standard Mode
- **评分记录表 (Evaluation Record)**：
  ```markdown
  - [ ] Identity Preservation: Pass / Fail
  - [ ] Outfit Attribute Binding: Pass / Fail
  - [ ] Spatial Clarity: Pass / Fail
  - [ ] Unrequested Additions: Pass / Fail
  - [ ] V1/V2 Fact Consistency: Pass / Fail
  - [ ] Output Contract: Pass / Fail
  - Notes:
  ```

---

### Test-05: 双角色站位与色彩属性隔离
- **用户输入**：
  > “两个少女并排坐着：左边的金发双马尾穿浅蓝水手服，右边的黑长直穿红白巫女服，彼此微笑着。”
- **预期模式**：Standard Mode
- **评分记录表 (Evaluation Record)**：
  ```markdown
  - [ ] Identity Preservation: Pass / Fail
  - [ ] Outfit Attribute Binding: Pass / Fail
  - [ ] Spatial Clarity: Pass / Fail
  - [ ] Unrequested Additions: Pass / Fail
  - [ ] V1/V2 Fact Consistency: Pass / Fail
  - [ ] Output Contract: Pass / Fail
  - Notes:
  ```

---

### Test-06: 极简社交头像与弹性词数规划
- **用户输入**：
  > “简单画个推特头像，粉色短发微卷的元气少女，眨眼浅笑，背景简单点。”
- **预期模式**：Direct Mode | Aesthetic: Preset B (Sweet Vibrant)
- **评分记录表 (Evaluation Record)**：
  ```markdown
  - [ ] Identity Preservation: Pass / Fail
  - [ ] Outfit Attribute Binding: Pass / Fail
  - [ ] Spatial Clarity: Pass / Fail
  - [ ] Unrequested Additions: Pass / Fail
  - [ ] V1/V2 Fact Consistency: Pass / Fail
  - [ ] Output Contract: Pass / Fail
  - Notes:
  ```

---

### Test-07: 电影海报叙事与胶片质感路由
- **用户输入**：
  > “想要一张王家卫风格的雨夜剧照，短发女人坐在老旧咖啡馆窗边，隔着带雨滴的玻璃看外面，很有故事感。”
- **预期模式**：Standard Mode | Aesthetic: Preset E (Cinematic Auteur)
- **评分记录表 (Evaluation Record)**：
  ```markdown
  - [ ] Identity Preservation: Pass / Fail
  - [ ] Outfit Attribute Binding: Pass / Fail
  - [ ] Spatial Clarity: Pass / Fail
  - [ ] Unrequested Additions: Pass / Fail
  - [ ] V1/V2 Fact Consistency: Pass / Fail
  - [ ] Output Contract: Pass / Fail
  - Notes:
  ```

---

### Test-08: 排除意图转换为正向场景约束
- **用户输入**：
  > “画一个女剑士，不要现代背景，不要复杂的光污染，不要有多余的路人，不要露骨擦边。”
- **预期模式**：Standard Mode
- **评分记录表 (Evaluation Record)**：
  ```markdown
  - [ ] Identity Preservation: Pass / Fail
  - [ ] Outfit Attribute Binding: Pass / Fail
  - [ ] Spatial Clarity: Pass / Fail
  - [ ] Unrequested Additions: Pass / Fail
  - [ ] V1/V2 Fact Consistency: Pass / Fail
  - [ ] Output Contract: Pass / Fail
  - Notes:
  ```

---

## 3. 设计层回归用例 (Design-Layer Cases, v2.0.0)

以下用例不测 Anima 语法，测 `aesthetic-director-core` → `character-design-engine` 这条链有没有真的做决定。任何模型适配器都适用。
评分只看四项，缺三项以上判 Fail：**有带动词的命题 / 有被否决的方向 / 有删掉的东西 / 有一处怪**。

### Design-01: 开放式 OC
- **用户输入**：「设计一个有创意的原创女性角色。」
- **Fail 信号**：输出以职业/种族标签开头（"月光祭司"、"精灵弓箭手"）；发色瞳色服装全是众数；没有【否决的方向】；出现手表 / 蝴蝶 / 玫瑰 / 粒子 / 魔法阵。
- **Pass 参照**：`aesthetic-director-core/references/taste-calibration-pairs.md` Pair 1。
- **记录**：
  ```markdown
  - [ ] 命题含动词: Pass / Fail
  - [ ] 否决的方向 ≥2: Pass / Fail
  - [ ] 删掉的东西 ≥2: Pass / Fail
  - [ ] 一处怪（且只有一处）: Pass / Fail
  - Notes:
  ```

### Design-02: "更高级一点"
- **用户输入**：「白衬衫 + 黑长裙，帮我做得更高级一点。」
- **Fail 信号**：高级 = 加蕾丝 / 珍珠 / 刺绣 / 缎面 / 项链 / 手链；没有任何结构或比例决定。
- **Pass 参照**：Pair 2。至少一个大结构决定 + 一个比例决定 + 一个材质决定，且有删除清单。

### Design-03: "太平淡"反馈轮
- **上下文**：上一版是「墨绿军装长外套女骑士，短发，持剑，白底」。
- **用户输入**：「太平淡了。」
- **Fail 信号**：加肩章 / 勋章 / 披风 / 军帽 / 枫叶 / 光效；回复没有"诊断：失败在 X 层"这一行。
- **Pass 参照**：Pair 6。只动命题层与由它引起的轮廓；装饰不增加。

### Design-04: 参考图原创
- **用户输入**：一张参考图 + 「参考这张的感觉，但要原创。」
- **Fail 信号**：换名词当原创（蛇 → 龙）；输出 `white background, anime, intricate` 类无结构词。
- **Pass 参照**：Pair 5。先列出 3–5 条"真正在起作用的结构"，再换掉全部具体物件。

### Design-05: 适配器拒收需求
- **用户输入**：「帮我写个 NAI5 提示词，一个赛博巫女。」
- **Fail 信号**：适配器直接产出 prompt。
- **Pass**：适配器识别出这不是 blueprint，走 identity → director → character-design-engine 后再编译；赛博元素以签名方式处理（有理由的结构、一处怪、一个刺点），而不是拒绝用户要求。
