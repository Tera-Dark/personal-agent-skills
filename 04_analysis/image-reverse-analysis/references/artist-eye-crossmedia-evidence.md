# Artist Eye · 跨艺术门类证据图谱（2026-10-16）

> 这是**可追溯的研究入口，不是图像数据集、LoRA 训练集或风格复制工具**。仅保存文字机制与官方/仓库链接；不下载或公开传播用户提供的图像或商业美术。区分 [User-visible observation]、[Primary source]、[GitHub project readme]、[Design hypothesis]、[Image-tested]，绝不将资料链接误当 NAI5 已出图测试。

## A. 当前对话中的四种可见案例（用户参考，不代表出处核实）

### U1 晾衣天台 · 橙色顶棚与白布

[User-visible observation] 两人做不同劳动：前者夹衣物，后者持衣篮等待；镜头从侧方看到真实手部支点。顶棚构成暖色重量，垂挂白布是天然留白兼前景剪切，砖墙与长阴影承接夕阳。脸部并非叙事必要条件。

**可迁移**：共享劳动形成关系、道具解释姿势、帘布与大色块同一功能。**不可迁移**：晾衣/黄昏/天台不是亲密互动的默认环境。**反事实**：移除衣篮/夹布动作，人物变成纯合照；换成正面特写损失共同劳动关系。

### U2 雪夜门槛 · 蜡烛与阴影

[User-visible observation] 人物几乎贴在门槛，室内黄光与外界紫蓝空地以墙角切开；单支蜡烛让人物的手势和照明来源相互解释；长影为画外空间增添未揭露的信息。

**可迁移**：阈限/跨界、主光源的双重叙事职责、空旷外侧产生悬念。**不可迁移**：雪、古堡、蜡烛不能自动等同于电影感。**反事实**：人物移到画面正中、均匀打光，失去危险/犹豫的阈值。

### U3 螺旋楼梯 · 高机位几何

[User-visible observation] 顶视导致栏杆反复变成深色旋线，浅色中心与绿黑大形强烈对比，红发人物只是尺度参照但依然可识别；曲线暗示时间与下坠，而非装饰边框。

**可迁移**：机位制造主图形，建筑成为叙述者，主体可以小。**不可迁移**：螺旋楼梯不是所有主题的通用高级构图。**反事实**：平视使旋线隐没，画面命题消失。

### U4 蓝调双人花海 · 编辑式幻想画

[User-visible observation] 双区相似而非完全对称；花束沿身体前景与轮廓生长，深蓝色静区容纳文字轴，局部花心暖光使脸/花/服装形成反复观看的路径。

**可迁移**：近似双生、局部亮度接力、画面密度向上衰减、字形与图形共同排序。**不可迁移**：默认蓝花、星空、竖轴标题或双人镜像。

用户图只用于当轮视觉观察。任何关于作者、IP、制作过程、生成模型的猜测都应标为未证实。

## B. 七门艺术与可信研究入口

| 门类 | 原始入口 / 证据级别 | 可迁移机制 | 明确的局限 |
|---|---|---|---|
| 故事板 & 动画 | 动画工作室官方 Story 流程 · [Primary source] https://www.disneyanimation.com/process/story/ | thumbnail→stage→emotion→timing，角色行动优先画风 | 官方制作流程不是 NAI5 参数 |
| 电影场面调度 | 动画工作室官方 Layout 流程 · [Primary source] https://www.disneyanimation.com/process/layout/ | 观看立场、镜头调整、动作与空间承重、镜头接续 | 单帧不能照搬连续镜头运动 |
| 动画美术开发 | 动画工作室官方视觉开发流程 · [Primary source] https://www.disneyanimation.com/process/visual-development/ | 角色/环境设计由剧本与情绪推动，单帧也要能抓住情绪 | 商业动画制作规模不可直接复制 |
| 光色脚本 | 动画工作室官方灯光流程 · [Primary source] https://www.disneyanimation.com/process/lighting/ | 设计类型化光与情绪化光的区别，明度范围随情绪改变 | 色彩映射非普适情绪公式 |
| 基础视觉结构 | 视觉叙事结构理论参考书（第 3 版） · [Publisher] https://www.routledge.com/The-Visual-Story-Creating-the-Visual-Structure-of-Film-TV-and-Digita/Block/p/book/9781138014152 | 七变量：空间/线条/形状/明度/色彩/运动/节奏；用反差和亲和搭建视觉结构 | 不是逐项堆料表 |
| 电影镜头维度数据 | CineTechBench · [GitHub readme] https://github.com/PRIS-CV/CineTechBench | 景别、机位、构图、机动、光色、焦距的结构化观察 | Benchmark≠生成美感证明；数据许可须单独核实 |
| 构图分析 | CADB & SAMP-Net · [GitHub readme] https://github.com/bcmi/Image-Composition-Assessment-Dataset-CADB | 常见构图类型及评分，可辅助训练识别大形 | 摄影构图分数不能代表艺术价值 |
| 色彩 | Colour Science · [GitHub readme] https://github.com/colour-science/colour | 色空间、明度、色差、受光材质研究；可核对色块分布 | 技术精确≠颜色有感情 |
| 剪辑/时间 | PySceneDetect · [GitHub readme] https://github.com/Breakthrough/PySceneDetect | 切分镜头用于研究前后帧之间的情绪/信息变化 | 只是工具，不自带导演知识 |
| 自动审美分数 | LAION Aesthetic Predictor · [GitHub readme] https://github.com/LAION-AI/aesthetic-predictor | 大量候选的辅助筛查/排序假说 | 训练分布/偏见风险、不能用分数否定刻意实验作品 |
| 版画与跨文化借鉴 | 博物馆艺术史资料：日式版画的跨文化影响 · [Museum curator essay] https://www.metmuseum.org/ja/essays/japonisme | 借鉴特殊裁切、非对称、抽象化色线而非照搬和服/器物；历史上也有跨文化转译 | 艺术史现象不是授权复制单幅作品 |
| 平面/唱片封面 | 设计机构：概念专辑视觉系统案例 · [Design studio portfolio] https://www.pentagram.com/work/the-national-1 | 专辑视觉语言可以跨封面、包装和宣传系统统一；图形概念先于炫技插画 | 并非所有封面都需要企业式视觉识别 |
| 音乐封面的概念反转 | 设计机构：音乐封面概念反转案例 · [Design studio portfolio] https://www.pentagram.com/work/lake | 创作者认为直接画湖不够令人惊讶，改用「洪水」作为标题概念的视觉回应；关键词→反直觉画面 | 不能把「湖→洪水」案例当所有封面的固定解法 |


**不确定时**：将工具的用途限制为分析辅助，避免把项目 README 的营销描述或数字当成人类审美定律。涉及作品原图，尊重网站许可与著作权。

## C. 跨媒介迁移不是照搬：五步过滤

1. **可见证据**：描述原参考图中实际看到的形、行为、颜色、空间；不脑补幕后故事。
2. **机制假说**：它为何让观众看向这里？为何会产生这类情绪？标 [Design hypothesis]，不是客观事实。
3. **剥离表皮**：去掉角色名字、色板、关键道具、舞台位置，剩下仍成立的结构关系才可能迁移。
4. **换领域并改变两项结构**：例如从天台劳动迁移到古风双人，保留「共同行为+先后动作」，但改观察位置和主要构图形；不要只换衣服。
5. **实际出图验证**：固定角色身份、画幅、模型设置，比较「加入机制」与「同条件基线」；记录视觉改进与负面效应，不把主观偏好硬升级为全局规则。

## D. 分层辨认失败：一个高度相似的色彩场景

- [Design hypothesis] 「两人身处暮色，温柔亲密」只有情绪形容词，弱。
- 迁移 U1 的行为机制：一人在窗台扶着大型纸板，另一人正把画好的线对齐纸板边沿；两人的视线都在实际接触点，人物共担重量。
- 迁移 U2 的光源机制：窗外唯一高角度光源透进来，光带照亮共同扶住的一小段板边，剩余空间压暗。
- 拒绝完全复制 U1 的日落、白布和衣篮；拒绝完全复制 U2 的蜡烛/雪。

此处只是说明如何跨领域抽象机制，不表示这种方案在用户 NAI5 中已跑出高分。

## E. 调研标记与审美知识晋升

- `OBSERVED`：原图可见事实。
- `SOURCE-VERIFIED`：已查阅发布者/仓库描述，支持所引述的技术、流程。
- `HYPOTHESIS`：对观看心理、叙事意义的可争论解释。
- `SPEC-PASS`：文本方案通过内部评审，但尚无图。
- `IMAGE-PENDING`：等待按规格跑图。
- `USER-RATED`：用户基于实际图像给出维度评价。
- `REJECTED`：某情境中无效；不自动上升为永久审美禁令。

短评必须标作用域：白底头像 / 二人生活 / 电影海报 / 极繁幻想 / 实验装帧；禁止将「某领域的局部成功」变成所有题材默认答案。
