---
name: evaluation-loop
description: Evaluates a generated image or compiled prompt against the original Creative Brief and blueprint, using a fixed rubric (identity preservation, outfit binding, spatial clarity, unrequested additions, V1/V2 consistency, output contract) plus a design-layer read (thesis, silhouette, causality, density, punctum, one strange thing). Diagnoses which layer failed and routes the fix to that layer with a single-variable change. Use on any feedback round: 太平淡, 太乱, 不像, 没人味, 这版可以, 评价一下, 哪里不对, compare versions.
metadata:
  author: Tera-Dark
  version: "2.8.0"
  layer: "06_evaluation"
  load: "on-demand"
  status: "active"
  triggers: "太平淡, 太乱, 不像, 没人味, 这版可以, 评价一下, 哪里不对, compare"
---

# Evaluation Loop

## 定位

生成 → 评价 → 定位失败层 → 只修那一层 → 再生成。

本 Skill 不修 prompt。它决定**该谁修**：设计层问题回 `aesthetic-director-core` / `character-design-engine` / `illustration-direction`；语法与伪影问题回对应适配器。

## Evaluation Gate

先检查当前 artifact 是否仍符合上游 Creative Brief / Blueprint / finished-design packet。设计包失效时先回设计层，禁止用 adapter 词汇掩盖设计失败。

## 评价顺序（从上往下，第一个失败的层就是要修的层）

```
1. 命题        看图能不能说出"这是关于什么的"？有动词吗？
2. 身份一致    锁定事实（发色、瞳色、服装件、姿势）是否 100% 保留？
3. 轮廓        缩略图尺寸认得出吗？第一眼是否顺眼、比例是否自然？怪点不能靠破坏大形制造存在感。
4. 服装结构    四层是否可读？颜色是否绑定到正确的件？有没有融色？
5. 因果 / 瞬间 姿势有没有解释服装和道具？是状态还是时刻？
5a. 摄影机位    谁在看、机位在哪、哪一秒被拍到？有没有前中后遮挡与动机裁切？换成普通正面平视是否情绪/叙事几乎不损失？若是则标记 **Camera Failure** → `illustration-direction`，不要靠 renderer 补 `cinematic`。
5b. **反公式化 / 情绪演出**  是否又落回雨夜+车站+暖光+冷阴影+右三分线？人物是否只是“摆出情绪”，而非一个角色先知、另一角色后知，或两个独立动作发生关系？如是标记 **Narrative/Visual Formula Failure** → `illustration-direction`，不是新增氛围词。
6. 密度 / 刺点 有密集区和安静区吗？刺点是一个还是多个？
7. 那一处怪    在吗？只有一处吗？
8. 未授权添加  有没有出现 blueprint 里没有的东西（耳环、腰带、手表、粒子、翅膀）？
9. 空间 / 构图 景别对吗？多图层是否隔离？背景抢戏吗？
10. 光         有物理来源和衰减吗？
11. 输出契约   格式对吗？有没有模型特定的禁用词 / 多余负面 / 参数？**Anima 普通 ComfyUI 节点不得输出 NAI5 的 `数字::tag::` 权重；若加权需确认支持 `(tag:weight)`；NAI5 的 `数字::tag::` 不得被套用为 Anima 普通语法。**
12. Gate Result  只有通过 Blueprint Gate 才允许重新进入 adapter。
```

**技术质量（手、解剖、清晰度）排最后。** 一张技术正确的图仍然可以因为没有人而失败。

## Artist Eye · 创意批评（按需）

当本轮使用跨媒介参考、Artist Eye、三向竞争或用户评价「有无作者感」时，读取 `references/artist-eye-review-protocol.md`：先保留身份锁和已有六维技术检查，再判断命题、主图形、行为因果、观看立场、光色节奏、创作必要性。给每维 `PASS / WEAK / FAIL / N/A` 和一处可见证据，按第一个失败 owner 回退，只动一个变量。用 `tests/artist-eye-regression.md` 的跨题材测试思想检验反模板，但不要将设计自检称为 NAI5 成图通过。允许朴素生活图、极简白底和静态编辑图**没有**强制怪点。自动美感评分不代替用户判断。

## Evidence-Based Art Critique · 反「文字寓意冒充画面表达」

当用户指出「美商没进步」「没有理解人物动机」「构图没有表达」「一直把上一张场景换角色」时，优先加载 `references/evidence-based-art-critique.md`，对作品或文本方案分别核验三层：

- **OBSERVABLE**：画面是否真的具备想让观众感受到的可见形/光/手势/空间证据，还是把解释性故事写在了 prompt 结尾？
- **CHARACTER MOTIVATION**：角色心理和物件关系是用户明确指定、已核实正典、可理解推测，还是被擅自说成「她就是在拯救世界」？
- **SELECTION QUALITY**：方案之间是否真的比拼不同画面机制，还是共享前一张的群像、圣光、天使、满屏气氛，再换名？

一个失败就优先返回 `aesthetic-director-core`（错误命题或臆造角色动机）或 `illustration-direction`（无法可见呈现、构图弱）。**禁止直接通过增加寓意旁白、精致形容词、质量串或复杂画面元素修补。** 完整的修复路由与可复现反例见 `references/evidence-based-art-critique.md`。对纯美型/静态图，不强制悲剧、故事反转或「唯一怪点」。

## 六维评分表（与 `tests/test-suite.md` 一致）

| 维度 | Pass | Fail |
|---|---|---|
| Identity Preservation | 锁定事实 100% 一致 | 改了发色 / 瞳色 / 关键特征 |
| Outfit Attribute Binding | 材质与颜色紧贴对应服装件 | 外套颜色渗入内搭；领口材质混淆 |
| Spatial & Layout Clarity | 景别 / 构图 / 图层隔离清楚 | 展示板出双胞胎；背景喧宾夺主；摄影机与遮挡关系互相矛盾 |
| Unrequested Additions | 无未授权物件 / 世界观 | 出现赛博配件、翅膀、手表、粒子 |
| V1/V2 Fact Consistency | V2 未改 V1 事实 | V2 把白发改成金发 |
| Output Contract | 格式正确，无禁用词，无多余负面 | 出现 `masterpiece`；夹带独立 Negative |

外加一行 **Design Read**：命题 ___ / 轮廓 ___ / 因果 ___ / **机位 ___** / 密度 ___ / 刺点 ___ / 怪 ___（各一个词：成立 / 弱 / 缺失）。

摄影反平庸必检：给出一句相机在谁的哪一侧、处于什么高度/距离、捕捉哪一帧的具体描述；回答“为何不是正面平视”；核对锁定的原版服设/留白需求没有被机位改变。未提供图像时只评估 Prompt/Blueprint 的摄影规划，不能声称实测成图效果。

## NAI5 镜头与控制器故障定位（只在 NAI5 任务启用）

设计意图已成立而画面依旧平时，不再只说“加 cinematic”：

1. **没有空间因果**（前景到底是哪只鞋？人物弯了还是站直？脸是否可见？）→ `illustration-direction` 重新确立 `visible_geometry`。
2. **空间事实齐全，模型没执行**（low angle 仍平视、POV 画出器材、悬浮变站立）→ `nai5-renderer` 从 `nai5-control-matrix.md` 选择**一个**实验控制器，固定种子/画师/画幅/参数做 A/B。
3. **原 IP 人物变脸/换衣** → 先查 Gate canonical，确认标签是否存在，再由 renderer 补可见原版服饰；不能由 Gate 保证模型学过。
4. **加招数后反而变坏**（极端权重遮脸、复杂度压暗、轮廓失去美型）→ 回滚新增控制器，不自动加第二个控制器补丁。
5. 评价中区分 **SPEC（文本通过）/ IMAGE-PENDING（等待出图）/ PASS（有图和对照证据）/ FAIL**。未实测时不能声称模型成功率。

完整用例见 `tests/nai5-model-control-regression.md`；这个测试文档**不能**代替实际跑图结果。

## Feedback Learning Hand-off（2026-10-14）

收到可判断的评价时，本模块除了首次失败层诊断，还应产出 **最小反馈信号**：对每个单独维度记录 `scope / axis / polarity / evidence / TEXT-APPROVED 或 USER-IMAGE-REPORT / current locked facts`。例如“构图不错、脸不好”必须拆成两个 signal；“再来一版”不等于自动成功。已认可维度进入 Session State 锁定，失败只改一层。

**持久晋升不归评价模块**：转给 `00_core/personal-identity-profile/references/feedback-learning-loop.md`；用写入权限及用户许可决定是否记录到 `feedback-ledger.md`。单条 “太丑” 不升级全局审美禁令，用户明确“以后不要”可直接确认对应作用域。无 Github 写权限时提供 /learn export 可复制候选，而不是说已经写入。技术错误（如 Anima/NAI5 权重串用）修 Renderer，不污染 taste。

## Modern Key Visual evaluation

当当前任务属于现代二游 / Character Key Visual，额外检查：

- Impact：缩略图是否先读到强轮廓、主运动轴和大色块，而不是柔光；**同时保留第一眼吸引力，不能用奇怪比例换记忆点。**
- Density：是否存在 1–2 个局部高密度口袋与明确安静区。
- Construction：首饰、流苏、链条、服装延伸结构是否有固定、承重、衔接证据。
- Face：是否出现镜像双眼、过量虹膜高光、塑料皮肤。
- Hair：是否先读到发量结构，再看到少量发丝。
- Light：是否有明确主光、清晰阴影和接触阴影；不能用 bloom / bokeh 代替形体。
- Atmosphere：删除粒子、花瓣、光斑后构图是否仍成立。

任一项因为设计逻辑失败，优先回到 Aesthetic Director / specialist，不得用 adapter 增加词汇掩盖。

## 输出契约

```
诊断：失败在 [层]。原因一句话。
六维：IP ✓/✗ · OB ✓/✗ · SC ✓/✗ · UA ✓/✗ · VC ✓/✗ · OC ✓/✗
Design Read：命题 成立 / 轮廓 弱 / 因果 缺失 / 机位 缺失 / 密度 成立 / 刺点 多于一个 / 怪 缺失
下一步：交给 [skill]，只改 [一个变量]，锁定 [其它一切]。
```

不写长篇评语。不夸。不列十条建议——一条，最上面那层的。

## 反馈翻译

用户原话 → 失败层 → 动作，见 `aesthetic-director-core/references/feedback-diagnosis.md`。本 Skill 直接引用那张表，不另维护。

## 三条元规则

1. 一次一层，一次一个变量。
2. **怪点不是免死金牌**：若用户反馈“丑”，先撤回或重做怪点，再检查比例 / 轮廓 / 色块 / 剪裁；不能用“这是刻意的”拒绝回滚。
3. 用户认可的版本：记录成功维度到 `personal-identity-profile/references/taste-signature.md` § 5。
3. 一次否决不升格为永久规则；≥3 次或用户明说才写入 `design-dislikes.md`。

## References

- `references/evidence-based-art-critique.md` — 可见证据 / 角色诠释来源 / 方案差异判断；对应低审美反馈的修复路由与回归用例。
- `references/artist-eye-review-protocol.md` — 艺术性评审证据、反模板判断、单变量 A/B 与用户成图反馈等级。
