---
name: personal-identity-profile
description: Persistent identity and taste layer for Tera-Dark's creative work. Holds the owner's stable aesthetic signature, hard dislikes, business objectives, and compact NAI5 artist-pool card. Does not generate prompts. Load first for creative, design, illustration, prompt, or aesthetic-judgment tasks; also when the user says 我的风格, 我喜欢, 按我习惯, 个人偏好.
metadata:
  author: Tera-Dark
  version: "2.5.0"
  layer: "00_core"
  load: "always"
  status: "active"
  triggers: "我的风格, 个人偏好, 按我习惯, any creative task"
---

# Personal Identity Profile

## 定位

这是系统里唯一存放用户长期品味、长期禁区和个人 NAI5 artist identity 的地方。其它 Skill 不得复制这些长期偏好。

本 Skill 不生成 prompt。它回答：这是给谁做的。

## 用法

任何创作类任务开始前：

1. 读 references/taste-signature.md —— 稳定品味签名。
2. 读 references/design-dislikes.md —— 高频否决与永久禁区。
3. 读 references/nai5-artist-pool.md —— 当前 NAI5 artist 运行卡片。
4. 沟通与交付协议由 Kernel 统一管理。
5. 详细历史证据仅在需要追溯 artist 实验时读取 references/nai5-artist-evidence.md。

## 优先级

1. 本回合用户明确要求
2. 用户锁定事实 / 参考图事实
3. 最近一次明确否定反馈
4. taste-signature Tier A
5. taste-signature Tier B
6. 自由发挥

一次性实验不自动升级为永久规则；只有用户明确说以后都这样或反复确认才写入长期 profile。

## 更新边界

- 用户偏好 / 禁区 → 更新 taste-signature 或 design-dislikes。
- NAI5 artist 身份、池状态、永久排除、当前组合 → 更新 nai5-artist-pool。
- 历史评分、单人测试、组合实验、来源证据 → 更新 nai5-artist-evidence。
- 模型语法和 renderer 规则不进入 Identity。

## References

- `references/taste-signature.md` — 稳定审美与当前方向。
- `references/design-dislikes.md` — 历史否决与禁区。
- `references/nai5-artist-pool.md` — NAI5 当前运行卡片。
- `references/nai5-artist-evidence.md` — 历史 artist 测试与组合证据。
- `references/visual-preferences.md` — 偏好的类型与参考来源。
- `references/business-objectives.md` — 商业目标与评价标准。
