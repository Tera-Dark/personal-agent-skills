# NAI5 控制矩阵 — 可执行短路由（2026-10-14）

> **读取策略**：NAI5 创作/改词先读本文件；仅在遇到复杂专项或需核查数字时，按标题读取 `nai-v5-usage-guide.md` 对应 A/B/C/E 章节。**不是第二套审美 Skill**：画面设计归 illustration-direction，模型通用空间关系归 visual-prompt-core，具体 NAI5 语法由 renderer 独占。
>
> **证据级别**：本表来自用户转述的《小克 NovelAI V5 实测图鉴》对照，属于 [Community / source-reported experiment]，**不是本仓库自己跑过的复现实验，不是官方保证**。样本 2/2、3/3、6/6 受画师/种子/参数影响。用户当轮要求和锁定事实始终高于本表。

## 1. 入口：先分任务，再选控制器

| 意图 / 常见失败 | 第一个动作 | NAI5 落地 | 禁止 |
|---|---|---|---|
| 肖像脸太远 | 先改景别 | `portrait, close-up` / `upper body` / `cowboy shot` / `full body` 选其一 | 用“beautiful”补景别 |
| 机位平、没张力 | 设计层先定观看点与时间帧 | `from below`、`from above`、`fisheye` 任选匹配；附**可见**近/远/遮挡描述 | 只堆 `cinematic, dramatic, powerful` |
| 仰拍高度失真 | 描述可见内容 | 腰部/鞋在近景更大，脸在远处、可见下巴底面、身后是天花板；主体挺直 | 罗列胸/腰/膝高度标签期待区分 |
| 人物错误弯腰 | 保持身姿与观看方向分离 | `standing upright` + 画面里可见什么 | “looking down at the viewer”让角色弯腰 |
| POV 被画成摄影器材 | POV 的观众身体入框 | `pov`、观众的手/脚/膝在前景；说 `the viewer` | 在正向里提 `camera` 实物名词 |
| 悬浮但像站着 | 诊断默认姿态冲突 | `2::floating in sky::, -1::standing::`（案例） | 每图预置一串负权重 |
| 强透视踢腿无近大远小 | 指明最近物体 | 脚占最大前景，头/躯干退后，`kicking at viewer, foreshortening` | 单靠 `high kick`；无脑权重 2 遮脸 |
| 舞蹈/托举/互相接触出错 | 设计层验重心和接触 | 每人的手、腰背、重心位置写成一句关系；多人另用角色槽位 | 仅加形容词或靠 action tag 保证关节 |
| 逆光丢脸 | 补光与可见脸同时锁定 | 背后边缘光，**正面有柔和补光能看清双眼** | 只写 `silhouette, backlighting` |
| 颜色不准 | 稳定颜色范围 | `spot color, red accent, monochrome` 等成熟 tag 或明确服装部件配色 | 用 `red theme` 当精确部件着色 |
| 假署名 | 首先定位 3D/写实/画师偏差 | 针对性 `-2::signature, watermark, username, artist name, text, logo::` A/B | 每张图默认负权重长串 |
| 角色不认得 | 查准 canonical 角色标签与数据年代 | 完整 tag + 作品名 + 发衣视觉锚点；新/冷角色加外貌描述 | 编短名，凭空保证 NAI5 认得 |
| 原服装被画师篡改 | 明确服装可见部件 | `alternate costume`（换装）或原作服装具体描述（还原） | 仅角色名 + artist 1.6 |
| 双人动作发错对象 | 拆分动作归属 | Base + Character Prompt，各角色 `source#` / `target#` / `mutual#`（适用时） | 全局只写“她抱她”不明确方向 |
| 风景太照片化 | 检查数据集标签 | `background dataset` 仅当目标确实是较写实景观 | 所有插画自动附加 |
| 画面变暗 | 查 `complexity` | 先移除 `medium complexity` 等再对照 | 把 complexity 当细节开关 |
| 画面堆字/乱码 | 区分海报和需准确文字的设计 | 仅简短文字贴在载体：`a sign that says "..." ` | `Text:` 后接画面控制词 |

## 2. 镜头句式：镜头标签 + 可见空间证据

> 镜头语法的审美选择由 illustration-direction 决定。这里**只负责转译成 V5 更易执行的视图**。两个部分必须一起出现：*镜头 tag* + *画面内可见的证据*。

- **低机位的英气 OC 海报**：`from below, foreshortening`。例：`One polished shoe and the black gown hem dominate the lower foreground; her upright torso narrows toward her smaller face above; the cathedral ceiling rises behind her shoulders.` 鞋和裙摆需要服从总体人物比例，不能吞脸。
- **从肩后见证双人关系**：`over-the-shoulder view`。前景明确是 A 的半个肩/头发，B 侧过脸，确保目标脸可见；若不转脸容易变成纯背影。
- **手拉手 POV**：`pov` + `the viewer's hand is visible in the near foreground, held by her hand; her body recedes farther ahead`，观众手入画增强视点稳定性。
- **水面倒影肖像**：水洼是画幅主要可见平面；“她只出现在倒影里”，不额外画站在水洼旁的第二个人。
- **画面很远的小人物**：`very wide shot, tiny figure`；想控制占比可试对比例句单独加权，但**数字比例本身不稳定**。
- **服设立绘**：使用 `cowboy shot` 锁七分身；若肩颈细节最重要则用 `upper body`，如果要求鞋靴和完整结构则用 `full body`。不与 `close-up` 互相冲突。
- **朝向**：`from front`、`from side, profile`、`from behind` 分开使用；避免单独 `back` 触发“裸背”语义。
- **近景效果**：`blurry foreground`、`fading border` 可按目标使用；不要为了“电影感”擅自加黑边/暗角。

**主次优先：** 人物美型与身份识别 > 关键动作的物理可信度 > 镜头空间证据 > 题材环境 > 可删的装饰。镜头导致脸过远时必须返回设计层调整机位，不把失败说成艺术选择。

## 3. 正向负权重的独立决策

- **触发条件**：已有实际失败、或明确的默认姿态竞争，且一个相反概念能直接描述错误。
- **写法**：`-1::standing::` 与正向 `2::floating in sky::` 同处**Positive Prompt**，不是另开 Negative 输入框。
- **范围**：先一个小的局部负权重；若有 `standing` 被抑制可能影响其它承重动作，需检视相关设计锁。
- **强度**：源案例常用 -1；-2 只在特定故障（如假水印）有来源对照；绝不预设 -1/-2 到每张图。
- **验收**：固定画师、seed、尺寸、CFG、steps，对比不加 / 负权重后的可见错误是否减少。只改一个变量。

## 4. 光、色、媒介快速映射

- **具体光源优先**：`neon lighting`、`candlelight`、彩窗光斑、树影、池底焦散可直接触发；如果具体来源和入射方向重要，用一句可见关系而不是 `hard shadows` 空话。
- **脸部优先**：强背光时补一句“soft fill illuminates her face and both eyes”，否则 silhouette 易改成背影。
- **冷暖**：`split lighting, orange light, blue light` 可试；写“左右各有一盏灯”可能把灯实体画出，优先只描述脸上颜色。
- **单点彩色**：`monochrome, greyscale, spot color, red accent` 比“其它都无彩度”的长句更稳（源测试）。
- **色相主题**：`red/blue/green/purple theme` 主要影响整体色调，不能取代服装件级颜色绑定。
- **年份 / 质量 / medium**：年份不是可靠画风开关；泛用 `masterpiece`、`anime screencap` 带强画师时可能几乎无效；媒介样式及画师原作选择更重要。
- **`complexity`**：报告 low 会显著压暗、medium 次之；默认全部省略，除非专门做 A/B；不等于“华丽程度”。
- **`background dataset`**：倾向真实风景，仅场景有明确需求时加；`fur dataset` 可能引入假签名，默认不要加。

## 5. IP 身份与服装优先级

1. **先查 canonical tag**：Danbooru Tag Gate 确认 exact/alias；不能因为英文看着像正确写法就冒充已验证。
2. **再判断可识别性风险**：已存在的标签 ≠ NAI5 肯定学会该角色。作者报告约百张可大致认识、50 张以下困难、2026 年 5–6 月附近或以后建的标签可能超出 V5 数据（**只是实验推断，非 V5 官方训练截止声明**）。
3. **冷门/较新角色**：完整身份与系列、可见发型/服设/标志物；如果 reference 能用则按当前模型真实功能选择；若无法保证，明确还原风险，而不是编外观。
4. **画师权重 1.6**：来源说明能明显换画风同时保留身份，但也可能改变服饰；对用户个人画师池，仍以现有权重范围（通常最高 1.2）为准，越界只做用户批准的单画师实验。
5. **换装**：`[character], alternate costume, [specific garment details]`；官方还原则逐项锁衣领、袖、腰、裙裤等可见部件。
6. **数字结尾画师标签**：加权 token 关闭的 `::` **前恰好一格空格**：`0.3::artist:mgong520 ::`。不修改硬 tag canonical identity；不要无故禁用全部数字结尾画师。

## 6. 双人和高难动作

- NAI5 多人优先 Base Prompt（共用人数/镜头/光）+ **各自独立 Character Prompt**（各自身份、衣服、动作）；区分主动方与接受方用 `source#` / `target#` / `mutual#`，不当作万能保障。
- 一张海报有角色双重曝光或同角色巨幅底图时，属于**有意重复**，设计层要锁定，否则渲染层不能擅自增加第二个人。
- 跑图弱点：拉小提琴等精密手部/器物接触，源测试 0/3；双人托举部分腕肘不自然。明确位置只能提高机会，不能保证结构准确；优先后期局部修复或简化动作，不无限加 NL。
- 文字：短英文/日文可绑定载体并用引号，中文及长句仍可能错；严格品牌、长文案交由后期排版。

## 7. 反向诊断 → 最小实验

按“**画面设计失败 / NAI5 控制选择失败 / 外部数据认识不足**”分开：
1. 如果换个普通正面镜头同样成立、缺乏决定性时刻 → 回 illustration-direction，不能用权重补审美。
2. 如果设计已完整但角度/前景/光/动作没画出来 → 只换一个高价值 tag 或一句可见空间关系，固定其它设置进行 A/B。
3. 如果角色标签可用而身份依然不符 → 检查完整 canonical、样本量/年代风险及服装锚点；不要把“Tag 存在”误当“训练认识”。
4. 如果画面突然变灰/暗/写实/带假署名 → 优先检查 complexity、dataset、画师及媒介偏差。
5. 每轮保留：任务目标、locked facts、prompt、画师、seed、尺寸、steps、CFG、变化点、可见结果、结论级别；没跑图时标**待验证**，不能虚构 PASS。

## 8. 快速输出协议

在不违反当前用户明确要求的前提下：
- 默认只交付一个可复制英文 NAI5 Prompt；不自动生成图片；无作者/质量/年份/complexity/Negative。
- 结构顺序：主体身份 → **景别 / 朝向 / 核心机位** → 形象和具体可见服饰 → 姿态与关节 → 前中后关系 → 来源明确的光/色 → 少数风格/材质词。
- 只选最有画面控制力的 8–15 个事实簇；不要因文档覆盖 30 个技巧就输出 30 组修饰。
- 单人默认一个 prompt；多人物独立角色槽位；如用户要单块才 pipe 合并。
- A/B 需要说清“基于教程样本的预期，仍待用户出图验证”。

## 9. 查阅完整档案的索引

- `nai-v5-usage-guide.md` A1–A3：语法、负权重、复杂度、画师、材质。
- B1–B4：构图、视角、动作、光色（具体种子、成功率）。
- B5–B8：文本/特殊画面效果与模型擅长项。
- B9–B13：原创 OC、编辑工具、极端画幅与任务流程。
- C1–C4：模型局限、数量/文字/服务端限制。
- E1–E6：与当前用户美学和素材生产方式的集成规则。
