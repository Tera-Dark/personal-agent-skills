---
name: nai5-community-prompt-engineering
description: Model adapter that compiles a finished character or illustration blueprint into NovelAI V5 community-format prompts — weighted artist stack, global style layer, scene base, char1/char2 blocks, source#/target#/mutual# interaction tags, and optional targeted negative steering with weight::tag:: syntax. Use when the user asks for NAI5, NovelAI, NAI提示词, tag prompt, Danbooru-style prompt. Does not design — if no blueprint exists, route through aesthetic-director-core and character-design-engine / illustration-direction first.
metadata:
  author: Tera-Dark
  version: "2.1.0"
  layer: "02_creation"
  load: "on-demand"
  status: "active"
  triggers: "NAI5, NovelAI, NAI提示词, tag prompt, Danbooru, artist stack, char1"
---

# NAI5 Community Prompt Engineering

## 1. 定位

本 Skill 是**适配器**：把已经做完设计决定的 blueprint 翻译成 NovelAI V5 社区格式。

v2.1.0 起补充 NAI5 实际使用习惯：用户通常已有自己的 Negative，因此默认不输出 Negative；用户提供画师池并要求随机生成时，优先做小规模随机混合，而不是一次堆叠大量画师；遇到用户原始 artist tag 的特殊转义、通配符或异常格式时，不擅自规范化，先保持原写法，避免破坏 NAI/用户工作流解析。

**输入检查**：同 `anima-prompt-compiler`。没有命题 / 轮廓 / 四层服装 / 刺点 / 锁定事实的输入不是 blueprint，退回 router。

## 2. 社区格式架构

默认输出：

```
[Artist Stack]

[Global Style Layer]

[Scene Base]

char1:
...

char2:
...
```

如果用户明确要求 Negative、需要针对当前问题调负面，或没有提供自己的 Negative，才追加：

```
Negative:
...
```

详见 `references/community-format.md`。

## 3. Artist Stack

```
0.6::artist:name::
```

- 每位画师承担一个明确职责：线条 / 上色 / 构图 / 角色设计感——不重复职责
- **随机画师生成默认抽 4–6 位**；除非用户明确要求大规模融合，不要一次堆 8–12 位
- 推荐默认分层：主画师约 `0.5–0.6`，第二画师约 `0.4–0.5`，其余约 `0.25–0.4`
- 随机混合时优先控制总权重在约 `1.5–2.0` 的温和区间；避免多个 `0.6+` 画师同时叠加
- 画师跨度很大时宁可减少人数，也不要用高权重硬压成“平均融合”
- 用户提供画师池时，从池中随机抽取并保留用户给出的原始 tag 语法；不要擅自删除转义、通配符、括号或特殊后缀
- 用户池里明显带有异常/不完整权重时，不要猜测其含义并直接加入高权重 stack；优先跳过该项或使用安全的低影响组合，并在必要时说明
- 必要时控制 `-1::artist collaboration::`
- 画师选择服务 blueprint 的视觉语言，不替代设计。见 `references/artist-stack.md`

## 4. Global Style Layer

风格与角色数据分离。见 `references/style-layer.md`。

**关于质量词的模型特例**：`personal-identity-profile/references/workflow-style.md` 说“避免通用质量词”——那是针对 Anima 等模型。NovelAI 的质量 / 美学标签是训练过的有效 token，在 NAI 上**保留**：quality（如 `masterpiece, best quality, very aesthetic`）、complexity、rendering 三组各取所需，不堆叠。这是适配器层面的合法例外，不是对上游规则的违反。

## 5. Character Block

```
char1:
girl, [identity], [hair], [eyes], [expression], [outfit base→structural→extension→accessory], [props], [pose/action]
```

- 身份 token 靠前；签名特征先于次要装饰
- 一个 block 一个人；两人不混块
- **blueprint 的因果和密度要落成 tag 的顺序和取舍**：主锚点相关 tag 靠前且完整，安静区只给一个大块面 tag（如 `plain ankle-length robe`），不给它加装饰 tag
- 发型写形状分布，不写众数（`asymmetrical hair, long hair on one side, undercut on the other` 而不是 `long hair`）
- 见 `references/character-block.md`、`references/tag-taxonomy.md`

## 6. Interaction Tags

多角色用 `source#` / `target#` / `mutual#`，动作紧跟所属角色。见 `references/interaction-tags.md`。

## 7. Scene Block

角色情绪与动作先于背景装饰。背景只保留能解释光或动作的一层。见 `references/scene-block.md`。

## 8. Weighting & Negative

```
1.5::tag::    -2::tag::
```

- 只给：画师混合、关键风格方向、关键角色特征、不想要的风格抑制
- 不给每个 token 都加权
- **不要为了“看起来专业”而给普通描述词批量加权**
- **随机画师 stack 尤其避免高权重堆叠**；多画师同时高权重可能导致风格冲突、画面脏乱甚至噪点/伪影
- Negative 只在用户需要时输出，并解决**具体问题**（风格抑制、伪影等），不复制大段通用负面表。见 `references/weighting.md`、`references/negative-strategy.md`

## 9. 翻译 blueprint 时的取舍

Tag 格式天然会丢失“关系”。补救：
- 因果链 → 用**复合 tag** 保留最关键的一环（`sleeve slipped to elbow`, `weight on left leg`）
- 密度图 → 用 tag **数量分布**表达：密集区 6–10 个 tag，安静区 1–2 个
- 刺点 → 颜色词只出现一次，紧贴它的落点名词（`red thread on spool`），其它地方不再出现该颜色
- 留下的怪 → 必须进 char block，且靠前；它是记忆点
- 删掉的东西 → 确认没有以 tag 形式偷偷回来（尤其 `jewelry`, `earrings`, `belt`, `petals`, `sparkles`）

## 10. 输出

用户要 NAI5 时默认输出社区格式代码块。

**默认不输出 Negative。** 用户已有自己的 Negative，除非用户明确要求，否则不要附带 `[Negative]` 段，也不要重复常见负面词。

不用 MJ 式长自然语言，除非用户要；但 Scene/Global Style 可以使用短复合短语保留构图关系和设计因果。

## 11. 反馈轮

- 伪影 / 串线 / 噪点 / 权重问题 → 本 Skill 内单变量调整，优先检查 Artist Stack 数量与权重，再动内容设计
- 设计问题（太平淡、太乱、不像）→ 退回 `evaluation-loop` → `aesthetic-director-core/references/feedback-diagnosis.md`
- 如果问题是“全是噪点/画面脏”，第一排查项是过量画师混合、过高 artist weight、冲突风格 tag；不要第一时间继续增加 prompt 细节

## 12. 输出前检查

- [ ] 输入是 blueprint？
- [ ] 画师栈每位有职责、无重复？
- [ ] 随机画师是否控制在 4–6 位，且没有不必要的高权重堆叠？
- [ ] 用户原始 artist tag 的转义/特殊语法是否被保留？
- [ ] char block 顺序反映了主锚点 / 安静区？
- [ ] 刺点颜色只出现一次？
- [ ] 被删掉的物件没有以 tag 回流？
- [ ] 权重只用在必要处？
- [ ] 默认没有附带 Negative？
- [ ] 锁定事实未改？

## References

- `references/community-format.md` — 整体格式
- `references/artist-stack.md` — 画师栈工程
- `references/style-layer.md` — 全局风格层（quality / complexity / rendering / 风格抑制）
- `references/character-block.md` — 角色块顺序与规则
- `references/tag-taxonomy.md` — tag 分类与服装描述法
- `references/interaction-tags.md` — 多角色交互
- `references/scene-block.md` — 场景块
- `references/weighting.md` — 权重系统
- `references/negative-strategy.md` — 负面策略
