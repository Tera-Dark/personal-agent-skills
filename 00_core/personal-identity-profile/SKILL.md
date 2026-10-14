---
name: personal-identity-profile
description: Persistent identity and taste layer for Tera-Dark's creative work. Holds the aesthetic signature (structured foundation, one strange thing, a hint of danger, modern key-visual impact, fashion-grade garment construction, female-oriented OC/gacha sensibility, Xiao-artist female-oriented 2D taste and NAI5 artist-mixing rules), hard dislikes (watches, cyber/mech, random butterflies-roses-particles, adjective costumes), business goals. Does not generate prompts. Load first for any creative, design, illustration, prompt or aesthetic-judgment task; also when the user says 我的风格, 我喜欢, 按我习惯, 个人偏好.
metadata:
  author: Tera-Dark
  version: "2.5.0"
  layer: "00_core"
  load: "always"
  status: "active"
  triggers: "我的风格, 个人偏好, 按我习惯, any creative task"
---

# Personal Identity Profile

唯一的长期个人审美与画师策略 owner；不生成 Prompt，也不替用户决定当轮指令。

## 常驻与按需

常驻：本契约 + `references/taste-core.md`。避免把历史审美和大数据库全部塞进冷启动。

按需只读相关引用：`references/design-dislikes.md`（明确拒绝）、`references/taste-signature.md`（稳定审美和认可样本）、`references/nai5-artist-pool.md`（画师）、`references/visual-preferences.md`（画幅历史）、`references/business-objectives.md`（商业目标）。
反馈记录专用：`references/feedback-learning-loop.md`（晋升规则）与 `references/feedback-ledger.md`（可追溯候选），**评价时读取，普通创作不加载**。

## 冲突优先级

当轮明确要求 > 已锁定角色/参考事实 > 最新否定反馈 > Tier A 稳定签名 > Tier B 倾向 > 自由设计。一次尝试不自动升级为长期规则。

## 更新准则

用户评价 → `evaluation-loop` 拆分成功/失败维度 → 当轮立即应用 → 按 `references/feedback-learning-loop.md` 形成有证据和作用域的候选。写权限及许可满足时更新 `references/feedback-ledger.md`，否则保存在当轮并可导出；**不能假装新会话能自动持久写 GitHub**。

“以后默认”或 ≥3 次独立同范围证据才晋升；审美归 taste-signature，禁区归 design-dislikes，画师归 artist pool，技术语法归 renderer。变更须可追溯/可撤销、不能擅自扩大全局范围。Kernel 决定实际生图许可与 Prompt-only；Identity 不生成 Prompt。
