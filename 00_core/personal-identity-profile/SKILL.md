---
name: personal-identity-profile
description: Persistent identity and taste layer for Tera-Dark's creative work. Holds the aesthetic signature (restrained base, one strange thing, a hint of danger, fashion-grade garment construction, female-oriented OC/gacha sensibility), hard dislikes (watches, cyber/mech, random butterflies-roses-particles, adjective costumes), business goals and workflow style. Does not generate prompts. Load first for any creative, design, illustration, prompt or aesthetic-judgment task; also when the user says 我的风格, 我喜欢, 按我习惯, 个人偏好.
metadata:
  author: Tera-Dark
  version: "2.0.0"
  layer: "00_core"
  load: "always"
  status: "active"
  triggers: "我的风格, 个人偏好, 按我习惯, any creative task"
---

# Personal Identity Profile

## 定位

这是整个系统里**唯一**存放用户长期品味的地方。其它任何 Skill（包括模型适配器）不得再维护自己的"个人审美规则"副本——它们只引用这里。

本 Skill 不生成任何 prompt。它回答一个问题：**这是给谁做的。**

## 用法

任何创作类任务开始前：

1. 读 `references/taste-signature.md` —— 品味是什么（不是"避免什么"，是"是什么"）。
2. 读 `references/design-dislikes.md` —— 历史上反复否决的东西。
3. 读 `references/workflow-style.md` —— 怎么和用户说话、怎么交付。
4. 把签名交给 `aesthetic-director-core`，由它做具体决定。

## 优先级（冲突时）

```
1. 本回合用户的明确要求
2. 用户锁定的角色事实 / 参考图事实
3. 最近一次明确的否定反馈
4. taste-signature.md 里的 Tier A 签名
5. taste-signature.md 里的 Tier B 倾向
6. 自由发挥
```

用户一次性的实验不自动变成永久规则；只有明确说"以后都这样"或反复确认三次以上，才升级写入 references。

## 什么时候更新本 Skill

- 用户明确说"我喜欢这个方向 / 以后都这样" → 写入 `taste-signature.md` 对应 Tier
- 用户反复（≥3 次）否决同一类东西 → 写入 `design-dislikes.md`
- 用户认可了一版输出 → 把该版的命题类型、轮廓策略、密度分布、刺点位置记到 `taste-signature.md` § 5「被认可的样本」

更新时保留日期。旧条目不删，标记为"已被 X 取代"。

## References

- `references/taste-signature.md` — 品味签名：核心、Tier A/B/C、被认可的样本
- `references/design-dislikes.md` — 否决清单与否决理由
- `references/visual-preferences.md` — 偏好的类型、构图、参考来源
- `references/business-objectives.md` — 商业目标与评价标准
- `references/workflow-style.md` — 沟通、交付格式、迭代方式
