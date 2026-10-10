---
name: personal-identity-profile
description: Persistent identity and taste layer for Tera-Dark's creative work. Holds the aesthetic signature (structured foundation, one strange thing, a hint of danger, modern key-visual impact, fashion-grade garment construction, female-oriented OC/gacha sensibility, Xiao-artist female-oriented 2D taste and NAI5 artist-mixing rules), hard dislikes (watches, cyber/mech, random butterflies-roses-particles, adjective costumes), business goals. Does not generate prompts. Load first for any creative, design, illustration, prompt or aesthetic-judgment task; also when the user says 我的风格, 我喜欢, 按我习惯, 个人偏好.
metadata:
  author: Tera-Dark
  version: "2.4.0"
  layer: "00_core"
  load: "always"
  status: "active"
  triggers: "我的风格, 个人偏好, 按我习惯, any creative task"
---

# Personal Identity Profile

唯一的长期个人审美与画师策略 owner；不生成 Prompt，也不替用户决定当轮指令。

## 常驻与按需

常驻只嵌入本契约 + `references/taste-core.md`：这是精简审美签名和当前交付习惯。避免把历史案例、完整禁区和画师数据库压进每次冷启动。

任务触发时，**只读取相关单文件**：
- `references/design-dislikes.md` — 用户否定该方向、涉及高频违禁元素或进行深度审美复盘时读取。
- `references/taste-signature.md` — 完整 Tier A/B/C、已认可样本、审美校准记录。
- `references/nai5-artist-pool.md` — 仅画师串、画师测试与选择时读取。
- `references/visual-preferences.md` — 题材/构图历史偏好。
- `references/business-objectives.md` — 明确涉及 OC 商品商业约束时读取。

这些文件的源码位置在 `00_core/personal-identity-profile/` 下；不要为一个参考文件重新加载完整 Identity Bundle。

## 冲突优先级

当轮明确要求 > 已锁定角色/参考事实 > 最新否定反馈 > Tier A 稳定签名 > Tier B 倾向 > 自由设计。一次尝试不自动升级为长期规则。

## 更新准则

明确表示“以后这样”或至少三次一致反馈才推广为默认。新的喜好写入 `taste-signature.md`，明确拒绝写入 `design-dislikes.md`，画师身份/黑名单只写入 `nai5-artist-pool.md`；记录日期，旧记录标注被替代而非默默删除。

当轮 prompt-only / 生图许可由 Kernel 最终确定；其他 Skill 只引用 Identity，不复制个人审美规则。
