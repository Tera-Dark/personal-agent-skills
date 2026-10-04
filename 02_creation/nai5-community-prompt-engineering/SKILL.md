---
name: nai5-community-prompt-engineering
description: Model adapter that compiles a finished character or illustration blueprint into NovelAI V5 community-format prompts — weighted artist stack, global style layer, scene base, char1/char2 blocks, source#/target#/mutual# interaction tags, and optional targeted negative steering with weight::tag:: syntax. Use when the user asks for NAI5, NovelAI, NAI提示词, tag prompt, Danbooru-style prompt. Does not design — if no blueprint exists, route through aesthetic-director-core and character-design-engine / illustration-direction first.
metadata:
  author: Tera-Dark
  version: "2.5.0"
  layer: "02_creation"
  load: "on-demand"
  status: "active"
  triggers: "NAI5, NovelAI, NAI提示词, tag prompt, Danbooru, artist stack, char1"
---

# NAI5 Community Prompt Engineering

## 1. 定位

本 Skill 是**适配器**：把已经做完设计决定的 blueprint 翻译成 NovelAI V5 社区格式。

v2.3.0 起进一步锁定 NAI5 质量词、复杂度、渲染层与 prompt 顺序，并保留 v2.2.0 的权重与 artist tag 规则：1.0 是数值 emphasis 基准；>1.0 加强，0.0–1.0 削弱；用户提供画师池时保留 artist: namespace，不擅自改成裸画师名；随机画师默认 1 名主画师约 0.95–1.10，其余全部 <=0.6；用户通常已有自己的 Negative，因此默认不输出。

**输入检查**：同 `anima-prompt-compiler`。没有命题 / 轮廓 / 四层服装 / 刺点 / 锁定事实的输入不是 blueprint，退回 router。

## 2. 社区格式架构

组织提示词时可以在内部按 artist stack / global style / scene / char1 / char2 分层，但这些只是编排说明，不是要直接输出到 NovelAI 提示框里的 tag。尤其不要把 [Artist Stack]、[Global Style]、[Scene] 这类方括号标题当成 Markdown 标题直接塞入 NAI prompt，因为 NovelAI 的 [] 本身具有 weakening 语义。

实际输出默认直接从有效 tag / 短复合描述开始。

如果用户明确要求 Negative、需要针对当前问题调负面，或没有提供自己的 Negative，才追加：

```
Negative:
...
```

详见 `references/community-format.md`。

## 3. Artist Stack

默认合法 artist 写法：

1.0::artist:name::

**不要删除 artist: 前缀。** NovelAI V5 官方 Explore 实例可以看到实际 prompt 使用 artist:name 形式，因此用户池中的 artist namespace 应视为有效输入；特殊形式也要保持原样。

### NAI5 数值权重语义

NovelAI 官方数值 emphasis 规则：
- 1.0 = 基准强度
- >1.0 = 加强
- 0.0–1.0 = 削弱

因此 0.8–0.95 不是“高权重”；它仍然是在削弱。用户若目标是增强 artist 影响，应从接近或略高于 1.0 的值开始。

### 用户画师池的默认随机策略

当用户提供一个画师池并要求随机生成：
- 默认抽 3–4 位；设计较轻时可只抽 2–3 位
- 主画师 1 位：约 0.95–1.10，通常从 1.0 或 1.05 开始
- 其余画师：全部 <=0.6，常用 0.35–0.6
- 不再默认使用多个 0.8+ artist 权重同时叠加
- 主画师承担主要 style prior，其他画师只做轻量混合，不与主画师争夺控制权
- 画师跨度很大时宁可减少人数，也不要通过高权重硬压成平均融合
- 如果出现噪点、脏图、风格撕裂，第一排查项是 artist 数量、主次权重与冲突 tag，而不是继续增加 prompt 内容

### Preserve user syntax

如果用户的池包含转义、通配符、括号、下划线、点号、后缀或其它特殊语法，保持原样；不要擅自规范化。

例如以下形式不要擅自改写：

artist:rei(sanbonzakura)
artist:sencha_(senchat)
artist:mr.owlish

其中明显异常/不完整的条目不要猜测含义并推到主画师位置；可跳过，或仅在低影响位置使用。

特殊条目 vlfdus 0 视为含义不明确，不要擅自猜测成某个画师名。

必要时控制：

-1::artist collaboration::

画师 Stack 服务 blueprint 的视觉语言，不替代角色设计或构图设计。见 references/artist-stack.md。
## 4. Canonical Prompt Skeleton

NAI5 is compiled as a compact community-style weighted tag sequence, not a long natural-language essay.

Order:
1. Subject / identity / framing anchor
2. Year / era when relevant
3. Weighted artist stack
4. Quality / aesthetic anchor
5. Complexity / illustration density
6. Rendering / material direction
7. Targeted style suppression / numeric control
8. Framing / scene / environment
9. Character detail
10. Expression / clothing / accessories / props / pose
11. Optional quality tail / no text

For a single subject, a flat comma-separated prompt is valid. Use char1/char2 blocks when multiple subjects or isolation needs them.

### 4A. Global Style + Quality Layer

风格与角色数据分离。见 `references/style-layer.md`。

**NAI5 需要显式保留质量词。** NovelAI 官方文档说明 V5 Full 的 Quality Tags 会自动加入 `very aesthetic, masterpiece, no text`；Light 质量预设还会使用 `amazing quality`。官方 Prompt Tips 也明确建议在成图质量不足时加入 `very aesthetic`、`best quality`、`high quality`。因此不要再把 quality tags 当成可有可无的废话。

### NAI5 推荐全局层级

按功能组织全局层，而不是把所有“看起来高级”的词混成一团：

1. **Quality / Aesthetic anchor**  
   常用：`masterpiece, best quality, high quality, very aesthetic, amazing quality, absurdres`
2. **Complexity / Illustration density**  
   V5 可用：`high complexity` / `ultra complexity`；辅助：`intricate details`、`best illustration`
3. **Rendering / Material**  
   按目标选择：`detailed shading`、`smooth gradients`、`realistic texture`、`anime coloring`、`painterly`、`ligne claire`、`cinematic lighting` 等
4. **Style suppression / control**  
   只在有明确冲突时使用数值负权重，例如 `-2::simple illustration::`、`-5::artist collaboration::`

允许有多个质量 token，但不是同义词越多越好；质量层应服务于目标渲染风格。

NovelAI 官方还说明 Quality Tags toggle 会把 V5 Full 的标准质量词加到 prompt 尾部。因此开启自动 Quality Tags 时，不必机械重复完全相同的一组词。

### 用户社区样例暴露出的有效结构

一个实用的 NAI5 prompt 结构可以是：

`subject → year/era → weighted artist stack → quality/aesthetic → complexity → rendering → targeted style control → framing/scene → character detail/action → quality tail`

这里每组词承担不同控制任务，而不是简单堆词。

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

## 7. Prompt Order / Scene Block

NAI5 prompt 应视为有优先级的控制序列，而不是 Markdown 文档。实用顺序：

1. subject / identity / framing anchor
2. year / era / major artist
3. quality / aesthetic / complexity / rendering
4. targeted style suppression
5. framing / scene / environment
6. character detail / expression / clothing / pose
7. optional quality tail / `no text`

**重要主体与构图锚点尽量放在前半段。** NovelAI 官方明确说明 prompt 顺序会影响结果，并建议把最重要的信息放在前半段。Scene 仍然只保留能解释构图、动作或光线的环境信息。见 `references/scene-block.md`。

## 8. Weighting & Negative

NovelAI 数值 emphasis：

1.5::tag::
0.5::tag::
-2::tag::

- >1.0：加强
- 0.0–1.0：削弱
- 负值：针对性抑制 / removal / inversion
- 只给画师混合、关键风格方向、关键角色特征、不想要的风格抑制
- 不给每个 token 都加权
- 随机 artist stack 默认采用“1 名主画师接近 1.0 + 其余 <=0.6”的层级，而不是多名 0.8+ 同时叠加
- 用户已经有固定 Negative 时，不输出 Negative 段

## 8.5 Compact prompt discipline

用户默认偏好精炼提示词。NAI5 不把设计说明塞进 tag：
- 保留 subject / framing / artist / quality / complexity / rendering / scene / action 的控制骨架；
- 删除同义质量词、重复外观词、可由结构推断的枝节；
- 现代 Key Visual 重点保留大形、动势、材质、遮挡、主色块与关键事件；
- 叙事场景中，环境只保留能改变构图、动作、光或故事理解的元素；
- 用户有自己的 Negative 时继续默认不输出。

NAI5 的 compact 目标不是死卡词数，而是让每个 tag 都承担控制职责。

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
- [ ] 随机画师是否控制在 3–4 位（默认 3–4）？
- [ ] 是否只有 1 名主画师约 0.95–1.10？
- [ ] 其他画师是否全部 <=0.6？
- [ ] 是否保留用户原始 artist: namespace？
- [ ] 用户原始 artist tag 的转义/特殊语法是否被保留？
- [ ] subject / framing 是否靠前？
- [ ] 是否遵循 Subject → Year/Era → Artist → Quality → Complexity → Rendering → Control → Scene → Character → Action 的骨架？
- [ ] Quality layer 是否显式存在？
- [ ] 当前输入是否已经通过 Aesthetic/Blueprint Gate？
- [ ] quality / aesthetic / complexity / rendering 是否形成明确的全局层？
- [ ] 是否避免无限堆叠同义质量词？
- [ ] char block 顺序反映了主锚点 / 安静区？
- [ ] 刺点颜色只出现一次？
- [ ] 被删掉的物件没有以 tag 回流？
- [ ] 权重语义是否正确（>1.0 加强，0.0–1.0 削弱）？
- [ ] 权重只用在必要处？
- [ ] 默认没有附带 Negative？
- [ ] 默认没有把方括号分区标题直接输出为 prompt token？
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
