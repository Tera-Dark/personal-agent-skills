---
name: personal-identity-profile
description: Persistent personal taste and artist policy for Tera-Dark's creative work. Holds preferences for structured visual design, Xiao-artist and fashion sensibilities, optional tension or unusual details when appropriate, scoped dislikes, and business goals. Current requests and locked references take priority. Does not generate prompts. Use for creative, illustration, design and aesthetic tasks or 我的风格 / 按我习惯.
metadata:
  author: Tera-Dark
  version: "2.6.0"
  layer: "00_core"
  load: "always"
  status: "active"
  triggers: "我的风格, 个人偏好, 按我习惯, any creative task"
---

# Personal Identity Profile

唯一的长期个人审美与画师策略 owner；不生成 Prompt，也不替用户决定当轮指令。

## 常驻与按需

常驻：本契约 + `references/taste-core.md`。避免把历史审美和大数据库全部塞进冷启动。

按需只读相关引用：`references/design-dislikes.md`（明确拒绝）、`references/taste-signature.md`（稳定审美和认可样本）、`references/nai5-artist-pool.md`（画师）、`references/visual-preferences.md`（画幅历史）、`references/business-objectives.md`（商业目标）、`references/session-feedback-2026-10-14-15.md` 和 `references/session-feedback-2026-10-22-23.md`（限定范围的会话反馈）。
**动态已批准偏好**：开始新的创作主题、用户说“按我的喜好”或跨会话续作时，按需读取 `references/learning-digest.md`（只含已审核规则），优先使用与本次 mode/model/IP 匹配的最窄作用域；没有生效规则就直接使用 Taste Core。
**学习反馈**：评价时按需读取 `references/feedback-learning-loop.md`；`references/feedback-ledger.md` 是旧的人类可读记录，不计入自动证据晋升。结构化证据见 `data/learning/events.jsonl`，来源与执行方式见 `data/learning/README.md`。

## 冲突优先级

当轮明确要求 > 已锁定角色/参考事实 > 最新否定反馈 > Tier A 稳定签名 > Tier B 倾向 > 自由设计。一次尝试不自动升级为长期规则。

## 更新准则

用户评价 → `evaluation-loop` 拆分成功/失败维度 → 当轮立即应用 → 有写权限且获许可时记入结构化 JSONL 证据；否则提供可复制 JSON、当轮继续生效。`scripts/learn.py` 负责去重、评审、晋升、撤销与接力状态，`learning-digest.md` 是从已批准规则生成的摘要。**不承诺跨聊天自动写入或后台运行**。

“以后默认”或 ≥3 次不同作品的独立同范围证据，经过 review + promote 才晋升；审美归 taste-signature，禁区归 design-dislikes，画师归 artist pool，技术语法归 renderer。变更须可追溯/可撤销、不能擅自扩大全局范围。Kernel 决定实际生图许可与 Prompt-only；Identity 不生成 Prompt。

## L1 compact entry

- `references/identity-quickstart.md` — L1 minimal immutable identity/feedback contract; full references remain on demand.
