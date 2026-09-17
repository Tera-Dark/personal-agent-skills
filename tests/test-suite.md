# Anima Prompt Compiler 核心验证测试集 (Test Suite)

> **Version**: 1.0.0  
> **Last Updated**: 2026-09-17  
> **Scope**: 验证编译器在多场景下的属性锁定、语言转换、V1/V2 分离、词数规划与正向约束能力。

---

## 目录索引
- [Test-01: 角色属性锁定与未确定信息开放](#test-01-角色属性锁定与未确定信息开放)
- [Test-02: 4 层复杂服装叠穿与高级材质碰撞](#test-02-4-层复杂服装叠穿与高级材质碰撞)
- [Test-03: 前景立绘 + 背景放大头像多尺度展示板](#test-03-前景立绘--背景放大头像多尺度展示板)
- [Test-04: 浅色服饰与纯白背景防边缘融色](#test-04-浅色服饰与纯白背景防边缘融色)
- [Test-05: 双角色站位与色彩属性隔离](#test-05-双角色站位与色彩属性隔离)
- [Test-06: 极简社交头像与弹性词数规划](#test-06-极简社交头像与弹性词数规划)
- [Test-07: 电影海报叙事与胶片质感路由](#test-07-电影海报叙事与胶片质感路由)
- [Test-08: 排除意图转换为正向场景约束](#test-08-排除意图转换为正向场景约束)

---

### Test-01: 角色属性锁定与未确定信息开放
- **测试目标**：验证发色、瞳色绝对锁定，对未提及细节（如鞋子、具体耳饰）不擅自脑补为锁死项。
- **用户输入**：
  > “帮我生成一个银发红瞳的吸血鬼少女，穿黑色维多利亚长裙，神情安静，站在古堡月光下。”
- **预期执行模式**：Standard Mode
- **合格标准 (Pass/Fail)**：
  - [x] V1 与 V2 发色严格为 `silver hair`，瞳色严格为 `red eyes`；
  - [x] 裙装明确为 `black Victorian gown / dress`；
  - [x] 不得擅自脑补科技感翅膀、机甲配件或未要求的复杂耳饰；
  - [x] V1 忠实还原输入；V2 注入月光体积光与微观布料纹理。

---

### Test-02: 4 层复杂服装叠穿与高级材质碰撞
- **测试目标**：验证服装从内到外的装配顺序及截然相反材质的物理互补。
- **用户输入**：
  > “设计一套冬日高级感穿搭：内搭米色针织高领毛衣，外面套深灰开衫西装，再披一件重磅黑色粗呢大衣，围着燕麦色围巾，下身直筒西装裤。”
- **预期执行模式**：Standard Mode | Aesthetic: Preset C (High Fashion)
- **合格标准 (Pass/Fail)**：
  - [x] 服饰描述严格遵循 `内搭 (cream turtleneck knit) → 中层 (charcoal blazer) → 外套 (heavy black wool coat) → 饰品 (oatmeal scarf)` 的层级；
  - [x] 显式出现毛呢哑光与西装垂坠感的材质描述；
  - [x] 未出现内外层颜色倒置或串色现象。

---

### Test-03: 前景立绘 + 背景放大头像多尺度展示板
- **测试目标**：验证多尺度展示板中前景主体与背景放大头像的图层硬隔离。
- **用户输入**：
  > “帮我做一张角色设计展示图：前面是这个角色的完整全身立绘，背景放一个她的大尺寸半透明虚化头像，突出眼神和耳坠。”
- **预期执行模式**：Standard Mode | Mode: Layered Character Showcase
- **合格标准 (Pass/Fail)**：
  - [x] 前景使用 `foreground full body in sharp focus`；
  - [x] 背景使用 `background enlarged portrait in soft transparent wash / lowered contrast`；
  - [x] 明确标注为 `same character`，杜绝生成双胞胎；
  - [x] 负空间留白清晰整洁。

---

### Test-04: 浅色服饰与纯白背景防边缘融色
- **测试目标**：验证在浅色/白裙搭配纯白背景时，主动注入微弱接触阴影防止高光溢出。
- **用户输入**：
  > “纯白背景，一个穿白色真丝吊带裙的女孩，全身照，不要多余杂物。”
- **预期执行模式**：Direct Mode 或 Standard Mode
- **合格标准 (Pass/Fail)**：
  - [x] 成功转化“不要多余杂物”为正向约束；
  - [x] 主动包含 `soft contact shadow drop beneath feet` 或 `gentle subtle ambient shading` 保护边缘轮廓；
  - [x] 禁用 `masterpiece, 8k` 等可能加剧高光崩坏的废词。

---

### Test-05: 双角色站位与色彩属性隔离
- **测试目标**：验证双人插画场景下各自属性独立绑定，防止发色与服装交叉串线。
- **用户输入**：
  > “两个少女并排坐着：左边的金发双马尾穿浅蓝水手服，右边的黑长直穿红白巫女服，彼此微笑着。”
- **预期执行模式**：Standard Mode
- **合格标准 (Pass/Fail)**：
  - [x] 严格采用方位分块语法（`the girl on the left ... the girl on the right ...`）；
  - [x] 金发双马尾严格与浅蓝水手服绑定；
  - [x] 黑长直严格与红白巫女服绑定；
  - [x] 未出现水手服变红或金发被染黑的串色错误。

---

### Test-06: 极简社交头像与弹性词数规划
- **测试目标**：验证简单任务主动收拢词数预算，避免无意义的膨胀。
- **用户输入**：
  > “简单画个推特头像，粉色短发微卷的元气少女，眨眼浅笑，背景简单点。”
- **预期执行模式**：Direct Mode | Aesthetic: Preset B (Sweet Vibrant)
- **合格标准 (Pass/Fail)**：
  - [x] 词数控制在 ~25 - 45 词弹性区间，没有冗长背景从句；
  - [x] 聚焦面部表情（`wink, playful smile, delicate catchlight in eyes`）；
  - [x] 背景干净柔和（`soft pastel muted backdrop`）。

---

### Test-07: 电影海报叙事与胶片质感路由
- **测试目标**：验证胶片感、王家卫/索尔·雷特雨雾反光与非对称构图的综合调度。
- **用户输入**：
  > “想要一张王家卫风格的雨夜剧照，短发女人坐在老旧咖啡馆窗边，隔着带雨滴的玻璃看外面，很有故事感。”
- **预期执行模式**：Standard Mode | Aesthetic: Preset E (Cinematic Auteur)
- **合格标准 (Pass/Fail)**：
  - [x] 引入 `cinematic 35mm film still, viewed through rain-streaked window`；
  - [x] 包含冷暖色温对峙与微观胶片银盐颗粒（`fine film grain`）；
  - [x] 神态为非表演化的放空与注视（`contemplative gaze lost in thought`）。

---

### Test-08: 排除意图转换为正向场景约束
- **测试目标**：验证将用户的多项“不要/无”要求正确转译为肯定式场景约束，默认不生成负向词。
- **用户输入**：
  > “画一个女剑士，不要现代背景，不要复杂的光污染，不要有多余的路人，不要露骨擦边。”
- **预期执行模式**：Standard Mode
- **合格标准 (Pass/Fail)**：
  - [x] 输出中不得出现独立的 Negative Prompt 代码块；
  - [x] 不包含 `no modern background`, `without other people` 等禁用句式；
  - [x] 成功转译为 `a single female swordsman standing alone, ancient traditional setting, natural balanced ambient lighting, dignified heroic posture`。
