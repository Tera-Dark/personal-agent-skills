# Feedback Ledger — 个人偏好证据账本

> 更新策略参见 `feedback-learning-loop.md`。这里是**持久证据**，不是“全部生效的硬规则”；只把经晋升的短决策同步到 `taste-signature.md`、`design-dislikes.md` 或画师池。公开仓库不存用户原始图片与完整聊天。按新→旧排序，新增行不重复记同一成图试验。
>
> 状态：`candidate` 试探偏好；`confirmed` 明确评价但作用域有限；`promoted` 已进入正式规则；`superseded` 后续修正。可信来源：`TEXT-APPROVED`、`TEXT-REJECTED`、`USER-IMAGE-REPORT`、`USER-EXPLICIT-POLICY`、`TECHNICAL-CORRECTION`。这些不等于现场验证过的模型输出。

| ID / 日期 | 作用域 · 维度 | 来源与信号 | 解读与下一轮可操作约束 | 状态 / 归属 |
| --- | --- | --- | --- | --- |
| FB-20261015-01 · 10-15 | global · generation/output | USER-EXPLICIT-POLICY：「输出提示词给我就行，不要生成图片，以后都是这样」 | 只交 prompt 文字，不因「设计插画」擅自调用生图；实际要求生图才生成 | promoted → taste-core / kernel |
| FB-20261015-02 · 10-15 | model:NAI5 · output | USER-EXPLICIT-POLICY：「不用带画师串和质量词，我已固定」 | 普通 NAI5 内容版**默认不加 artist / quality / year / Negative**；用户专门要串才输出；英文 Tags + 简短 NL + 可复制单框 | promoted → taste-core / nai5-renderer |
| FB-20261015-03 · 10-15 | mode:cinematic · camera/narrative | TEXT-REJECTED + TEXT-APPROVED：「很丑很难看」「尽量内容少而明确」「俩分镜，都人物面部特写，情绪渲染很饱满」 | 双格剧情情绪稿用两张同场面部反应的**信息增量**而非堆环境；仅在用户指定双格时启用 | confirmed → illustration-direction / session study |
| FB-20261015-04 · 10-15 | mode:canonical-fanart · identity | USER-CORRECTION：「不是，我要方舟的人物ip的这种分镜」「要懂剧情的设计」 | 先核对 IP/canon 与角色传，再用行为/表情转译角色动机；故事推演要标同人而非官方事实 | confirmed → session study |
| FB-20261015-05 · 10-15 | mode:ancient-portrait · character-life | MIXED TEXT：「形象不错」「自然背景」「更具镜头感的肖像特写」「没有互动」「不要拿纸」 | 保留审美和服设，改成真实自然背景 + 意图性近景 + 有诱因的优雅转身/互动；无因果信纸道具禁止补丁 | confirmed → small-artist-brain / session study |
| FB-20261015-06 · 10-15 | mode:material-fusion · framing | TEXT-CORRECTION：「跑出来只有个头」 | 淡入式矿物/水墨肖像须锁**脸、肩、衣袖、躯干的可见性**，失边在下半部；不叠互斥景别 | confirmed → illustration-direction / session study (user-reported image behavior) |
| FB-20261015-07 · 10-15 | ip:Arknights-Suzuran · aesthetic | TEXT-APPROVED：「这个表现的感觉很不错」 | 铃兰春花枝头、粉乳白与浅青配色、服装/尾巴/自然花枝共享动势；保持美型、低噪声；**仅认可表现方向，不假定完成出图验证** | confirmed → taste-signature / session study |
| FB-20261015-08 · 10-15 | mode:experimental-portrait · material | REFERENCE-POSITIVE：「这种风格的高级设计感」 | 负空间、矿物侵蚀、版画颗粒与人物共形；是可选艺术肖像模式，不自动通用化 | candidate → session study |
| FB-20261015-09 · 10-15 | mode:cinematic · photography | TEXT-APPROVED：「哦，这个不错，有点学到位了」＋新增日系叙事摄影参考 | 摄影机位的实际几何与人物关系、光与密度先于模板词；用户认可方法方向，不是已证明每张 NAI5 稳定成功 | confirmed → photography-brain / session study |
| FB-20261015-10 · 10-15 | mode:SBR-poster · aesthetic | TEXT-APPROVED：「骚爆了。9分」「8分」等 | JOJO7 西部厚涂/荒木系美型、姿态张力、角色标志物/故事气质；不把评分等同于 NAI5 同 Seed 验证 | confirmed → session study |
| FB-20261014-01 · 10-14 | mode:cinematic · camera | TEXT-REJECTED：“电影感设计思路还是太狭隘”“出图都很难形容” | 不把“电影感”缩为雨夜、车站、逆光、人物三分线；先选受限视点、不同步动作与时间相位。多轮对模板化画面不满 | promoted → cinematic-12-frame-study / illustration-direction |
| FB-20261014-02 · 10-14 | mode:cinematic-couple · narrative | TEXT-APPROVED：“这个不错，再来个电影感互动画面”，对应旧便利店固定机位双格微动作设计 | 认可**同机位、微动作推进人物亲密关系**的机制；不是声明用户已跑图成功，更不代表所有场景都必须双格 | confirmed → taste-signature（样本 / 局部） |
| FB-20261014-03 · 10-14 | global · output | USER-EXPLICIT-POLICY：“把所有提示词放一块方便我复制” | 当前及后续类似提示词默认单框复制；遇 NAI5 多角色字段时交代实际兼容限制 | promoted → taste-core / renderers |
| FB-20261014-04 · 10-14 | model:Anima · syntax | TECHNICAL-CORRECTION：“Anima 模型的权重是数字::tag::这样吗？” | NAI5 `数字::tag::` 不属于普通 ComfyUI Anima 权重；按节点使用 `(tag:weight)`，不擅称任何 TE 都解析 | promoted → anima-renderer/anima-weight-syntax.md |
| FB-20261014-05 · 10-14 | model:NAI5 / style:Muse Dash · rendering | USER-IMAGE-REPORT：“实验完虽然还原但不太满意” | 官方风格近似 ≠ 审美满意；不能因为识别出游戏风格就把 hyperpop、Q 版、荧光色当默认偏好 | candidate → current task only |
| FB-20261014-06 · 10-14 | mode:cinematic-couple · composition | TEXT-REJECTED：“太丑了画面”“参考这个图，带有那种分镜感的设计” | 优先检查脸型/大形/故事相位，不靠随意拉近、滤镜和散景修复；参考机制，不复刻具体帧 | confirmed → evaluation-loop |

## 维护说明

- 以上是用户本轮可追溯**文本反馈**；没有附完整 Prompt / 图片内容、没有宣称实际生成质量通过。
- 在 scope 下更新既有 ID，不为同一张图反复增加独立票数。若用户否定解释，则将原行标 `superseded`，附新 ID。
- `feedback-ledger.md` 默认按需读取；冷启动 Harness 只带 compact taste，不自动加载全表。
