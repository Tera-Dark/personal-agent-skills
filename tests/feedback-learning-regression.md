# Feedback Learning & QoL Regression — 2026-10-14

> 静态规范与人工会话用例。需要已授权 GitHub connector 才能演示真正跨会话写回；**普通的“加载仓库链接”不等于后台记忆或 GitHub 写权限**。

| ID | 用户输入/条件 | 必须出现的行为 | 不可出现 |
| --- | --- | --- | --- |
| FL-01 | “这个不错，再来一版” | 锁已认可轴，另外换一个真正不同的构图/事件；反馈标 TEXT-APPROVED | 假称已跑图成功；继续复用固定车站 |
| FL-02 | “构图很好，但脸丑” | 两条相反 polarity 的同源反馈，保持构图、只修脸 | 单条整体负反馈；推翻构图 |
| FL-03 | 同一张失败图连续抱怨三次 | 算 1 个独立来源；影响当前稿 | 升级全局永久禁令 |
| FL-04 | 三张不同作品独立一致评价“这个镜头太平” | 限 scope 累积证据；由身份模块考虑推广 | 一律把电影感禁掉 |
| FL-05 | “以后所有 NAI5 都一块复制” | USER-EXPLICIT-POLICY → output 偏好可直接晋升；必要时提示多角色 V5 的格式边界 | 为了合框输出模型不支持的随机分隔符 |
| FL-06 | “我在 Anima 里试出来括号能生效” | USER-IMAGE-REPORT + 模型和节点范围；Renderer 格式记录 | 当成所有 ComfyUI 编码器官方事实 |
| FL-07 | “这画师 8 分，适合白底半身，不适合剧情” | 仅往 artist pool 发范围与评分候选 | 变成全局人物美学禁令 |
| FL-08 | “撤销上次记录” | 关联 FB ID，标 superseded，并更新已晋升目标 | 直接删除旧记录不留踪迹 |
| FL-09 | GitHub 不可写/未安装 Connector；用户说“记住” | 当轮候选 + /learn export；明确未持久写回 | 假称“已保存到仓库” |
| FL-10 | 已授权 GitHub 连接且明确同意持续记录 | 去重追加 ledger，source SHA/冲突检查，晋升满足门槛才改 stable taste | 每句感叹都改 taste-core 产生 commit 洪水 |
| FL-11 | 评分 9/10 但无成图截图 | TEXT-APPROVED/USER-IMAGE-REPORT 视用户是否明确说已跑图 | 自动标 IMAGE-VERIFIED |
| FL-12 | “只改光影，其他照旧” | FAST VARIANT 保留身份、服装、构图与动作 | 重新设计全张插画 |
| FL-13 | 新聊天只发 GitHub 仓库链接 | 从最新版 Harness 加载稳定偏好与按需路由 | 假装拥有旧会话的未同步候选 |
| FL-14 | 明确角色是反派且需赛博风 | 当前锁定事实覆盖过往“不要无故赛博”倾向 | 把历史偏好变成无条件禁止 |
| FL-15 | 公共仓库偏好记录 | 仅抽象设计偏好 + 最少短文本证据 | 上传用户图片或私人内容 |

## 自动验收（SPEC）

```bash
python3 scripts/validate_skills.py
python3 scripts/build.py
python3 scripts/validate_skills.py --check-bundle
python3 scripts/check_output_contract.py
```

`validate_skills.py` 检查学习协议、Ledger、Router、Evaluation 的硬链接，并拒绝重复的反馈 ID 或缺失状态。真实会话的口语化解析、实际 GitHub 写回与成图审美效果仍需人工实测，静态校验不等于这些结果通过。

## 证据审计模板

```text
source_commit:
scenario:
feedback_id:
scope / polarity / axis:
source_type: TEXT-APPROVED | USER-IMAGE-REPORT | USER-EXPLICIT-POLICY | TECHNICAL-CORRECTION
same-image duplicate?:
session result:
GitHub write available / authorized?:
ledger updated / exported:
promoted / not promoted:
actual result: PASS | FAIL | INCONCLUSIVE
```
