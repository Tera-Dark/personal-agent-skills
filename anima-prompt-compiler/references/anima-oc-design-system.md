# Anima OC Design System

本文件用于解决“看似有细节、实际没有角色设计”的低质量 OC 提示词问题。目标不是给角色堆更多装饰，而是先建立可识别的**角色设计命题、轮廓系统、视觉锚点、服装结构、动作叙事与展示方式**，再将其编译成 Anima 可执行的英文 prompt。

## 1. 先设计，再写 prompt

每个原创 OC 在输出前必须先回答以下问题：

1. **Design thesis / 设计命题**：角色最核心的身份冲突或幻想概念是什么？例如“被供奉的蛇神少女”“以记忆为燃料的钟表裁缝”，不能只写“漂亮的哥特少女”。
2. **Silhouette / 轮廓识别**：远看时靠什么认出她？优先确定一个主轮廓与一至两个辅助轮廓，例如蛇形环绕、巨大偏置头饰、单侧长披片、异常宽袖、悬浮裙撑。
3. **Visual anchor / 视觉锚点**：全身只设置 1 个主锚点、2 个次锚点。主锚点应是头部、胸口、腰部、背部或手中道具中的一个明确结构；避免所有部位都争夺注意力。
4. **Material contrast / 材质对抗**：至少形成一组可见对比，例如柔软长发 vs 硬质骨饰、哑光布料 vs 玻璃反光、洁白织物 vs 湿润鳞片。材质必须绑定到具体结构和受光行为。
5. **Behavioral pose / 行为姿势**：角色正在做什么，而不是“优雅地站着”。动作应能解释服装、道具和配件为何产生当前的拉伸、悬垂、摆动或遮挡。
6. **Narrative residue / 叙事残留**：通过一个道具、痕迹、环境或动作后果暗示角色经历，不用堆叙事说明。例如被咬断的红线、被翻开的药典、沾有花粉的手套、正在熄灭的灯。

## 2. 角色设计的六层结构

### Layer 1 — Core identity

先确定角色的职业、异质性、气质和幻想来源。避免把“少女、漂亮、神秘、高级”当作设计本身。

推荐格式：

`[role or social identity] + [non-human / symbolic element] + [behavioral contradiction]`

例：`a court archivist who cultivates poisonous flowers, gentle manners hiding predatory instincts`

### Layer 2 — Silhouette architecture

选择一个主轮廓策略，不要同时使用所有策略：

- **Halo / radial**：围绕头部或上半身形成环形、触手、羽片、枝条或悬浮结构。
- **Vertical spear**：高耸头饰、长杖、垂直披片或尖锐肩线，形成向上拉伸。
- **Asymmetric cascade**：单侧长发、链条、布片、花枝或装饰集中向一侧下坠。
- **Cocoon / volume**：宽袖、圆肩披肩、巨大裙撑或包裹性外套形成包覆体积。
- **Fragmented orbit**：围绕角色分布若干独立组件，但必须有共同的材质、形状或运动逻辑。

提示词必须写出轮廓的空间关系：`behind the head`, `wrapping around the torso`, `descending from one shoulder`, `orbiting the raised hand`，而不是只列名词。

### Layer 3 — Costume engineering

服装设计至少包含：

- **Base garment**：贴身基础服装与主要色块。
- **Structural garment**：束腰、骨架、胸甲、背架、肩部或裙撑，负责造型支撑。
- **Signature extension**：真正构成角色识别度的长带、尾状结构、异形袖、外翻裙片、悬浮装置或生物附肢。
- **Accessory system**：发饰、腰饰、手部、鞋履和道具必须遵循同一视觉语法。

服装应描述“形状 + 位置 + 功能/运动”，例如：

`a rigid rib-like corset framing the torso, long translucent side panels hanging from the waist, silver clasps connecting the fabric to a serpentine ornament`

避免只写：`beautiful detailed dress, many accessories, intricate design`。

### Layer 4 — Palette hierarchy

先确定颜色职责，而不是罗列颜色：

- **Dominant field**：约 60–75%，负责整体气质。
- **Structural color**：约 20–30%，负责轮廓分区和服装结构。
- **Punctum accent**：不超过约 5%，用于眼睛、宝石、丝带、灯火或伤痕等视觉锚点。

每个颜色应有明确落点，例如：`ivory fabric, ink-black structural pieces, restrained turquoise accents concentrated in the eyes, ribbons and reflected light`。

### Layer 5 — Pose and camera as one system

动作和镜头不能分开随机选择。根据动作选择镜头：

- **展示型动作**：三分之二侧身、手部展示、轻微俯拍，适合突出服装结构。
- **施法/操控型动作**：手部靠近镜头、道具形成前景，适合近景透视与环形动线。
- **回身/逃离型动作**：身体朝外、头部回望，适合斜向构图与飘带拖尾。
- **仪式/压迫型动作**：低机位、垂直构图、角色被巨大结构包围，适合建立神性或危险感。
- **脆弱/休息型动作**：高机位、收缩姿态、局部遮挡，适合生活感和情绪叙事。

至少明确：相机高度、视角方向、身体主轴、手部动作、视线、前景遮挡和动势终点。

### Layer 6 — Presentation format

根据目标选择展示方式：

- **Clean character plate**：白色或浅灰背景，完整轮廓，少量道具和接地阴影，适合商品化角色立绘。
- **Decorated key visual**：简单背景 + 2–4 个与设定相关的点缀物，适合展示角色气质和叙事。
- **Editorial design plate**：大面积留白、构成性道具、局部放大或图形化装饰，适合时尚/设计感角色。
- **Environmental vignette**：角色处于一个小型场景中，背景不抢主体，但能解释光源和动作。

“白色背景”不等于“空洞背景”。可以使用极淡的投影、纸张、线稿、花瓣、符号、器物轮廓或局部色块，但所有点缀都必须服务于角色命题。

## 3. 视觉复杂度控制

复杂度来自结构关系，而不是装饰数量：

- 先确定 1 个主形状、2 个辅助形状、1 个动作方向。
- 配件应成组出现，遵循共同形态语言，例如骨、贝壳、钟表、花枝、玻璃或丝带，不要无关元素混搭。
- 让装饰在头部、躯干、腰部、手部或背部形成**重心分布**，避免平均撒满全身。
- 复杂结构必须保留可读的皮肤、基础服装和主要关节，不让道具吞没人物。
- 允许局部遮挡，但脸、主手势和主锚点必须保持可辨识。

## 4. 反平庸检查

输出前逐项检查：

- 如果删掉颜色，角色的轮廓还能被识别吗？
- 如果删掉所有装饰，基础服装是否仍有独立剪裁？
- 主锚点是否只有一个，而不是每个部位都在抢戏？
- 动作是否会改变头发、衣摆、丝带、道具或光线？
- 背景点缀是否来自角色设定，而不是随机花瓣、粒子和光效？
- 角色是否具有一个可被复述的设计命题？
- 是否存在一处有意的留白或低密度区域，让复杂设计能够呼吸？
- 是否避免“高级、精致、神秘、华丽”等空泛词替代具体视觉信息？

## 5. Prompt 编译顺序

建议顺序：

1. 主体数量、展示类型、背景与景别
2. 设计命题与角色身份
3. 主轮廓和空间结构
4. 头发、脸部和关键外观
5. 基础服装、结构服装、标志性延伸结构
6. 主锚点与道具
7. 动作、视线、身体主轴和镜头关系
8. 背景点缀与叙事残留
9. 光源方向、色彩职责、材质对抗
10. 画面层级、留白和可读性约束

## 6. Reference image extraction

当用户提供参考图时，不要只提取“白底、二次元、复杂、精致”。应先拆解：

- **Silhouette**：角色外轮廓由哪些大形状组成？
- **Mass distribution**：装饰集中在头部、胸腰、背部还是四肢？
- **Motif grammar**：重复出现的是蛇、骨、花、链、贝壳、机械件还是纸张？
- **Color hierarchy**：主色、结构色、刺点色分别落在哪里？
- **Material language**：织物、骨骼、玻璃、金属、生物组织如何对比？
- **Pose logic**：角色如何与主道具或附属结构交互？
- **Negative space**：哪些区域保持空白，为什么？

提取后只借鉴设计逻辑，不复制参考图的具体角色、构图或专属标识。若用户要求“类似风格”，优先复用轮廓组织、材质对抗、色彩层级和展示方式，同时更换角色命题与形态语法。

## 7. Default behavior for open-ended OC requests

当用户只说“设计一个有创意的 OC”时：

- 先在内部生成 3 个互不重叠的设计命题，再选择差异最大且视觉可执行的一个。
- 不默认使用哥特、机械、蝴蝶、玫瑰、魔法阵、随机发光粒子或黑白加单一荧光色。
- 不把“职业 + 常规制服 + 一个道具”当作完整 OC 设计；必须增加独特轮廓、形态语法和行为动作。
- 优先输出少量但有辨识度的结构，确保角色可以作为游戏立绘、卡面或商品化 OC 被记住。
- 若用户要求多套设计，每套必须在设计命题、轮廓策略、主锚点、材质语言和动作逻辑上至少有两项明显不同。
