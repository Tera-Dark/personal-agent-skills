# Anima Prompt Compiler 核心验证测试集 (Test Suite)

> **Version**: 1.1.0  
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
- **预期模式**：Standard Mode | Aesthetic: Preset C (High Fashion)
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
