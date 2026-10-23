# Quantified Aesthetic Review v1 · 审美量化评审

归属：evaluation-loop。用于“自己打分、多少分、评审、复盘、比较版本”。这是一套**主观但可复核的量表**，不是可证明的机器审美真值；不替代原六维硬约束 Gate 或 Aesthetic Director 的决策权。

## Evidence Gate

- **SPEC**：只看设计说明和 Prompt，评分为**文本预评估**。只能评价是否具有可执行的镜头、剪裁、互动、疏密设计和创意，不能证明生成效果。
- **IMAGE-REVIEWED**：评审者实际看过用户提供的成图，并用**画面可见证据**评分。不等于用户已经认可。
- **USER-IMAGE-REPORT**：用户描述了实际跑图效果，未提供可见图像时只记文字反馈，不编造完整成图评分。
- SPEC 与 IMAGE-REVIEWED 的分数不可直接相减，不能说“出图因此提高2分”。不同题材 Profile 和不同评审者也不做无条件可比。
- 用户认可一段文字为 TEXT-APPROVED，不代表 IMAGE-VERIFIED。所有自评保持 confidence 标记（low/medium/high）；未出图自评不可为 high。

## 8 个轴 · 每轴 0–10 分、步长 0.5

1. **camera**：机位、画幅、透视、裁切、观看立场与视觉引导；海报类评价主图形阅读视角。
2. **fashion**：服装裁片、固定点、材质分区、潮流辨识度和造型吸引力；无服装任务时权重为零。
3. **interaction**：人物行为与性格、动作因果、自然手势和关系。非叙事图允许权重为零。
4. **identity**：IP、原设、用户锁定事实，或是否符合约定改装范围。
5. **hierarchy**：焦点、人物占比、留白、层次、信息密度、缩略图可读性。
6. **light_color**：光源、环境反光、接触阴影、色彩秩序。
7. **originality**：具体可指认的创作记忆点、角色必要性、商业视觉冲击，不以形容词数量为证据。
8. **technical**：SPEC 为提示词可执行性、矛盾与冗余；IMAGE-REVIEWED 为实际解剖、边缘和画质完成度。

每个有效轴要求 **score + evidence**（一条具体可见事实或 Prompt 依据），可附 issue。评分锚点：0–2 失效；3–4 严重不足；5–6 可用但平庸；7–8 良好到优秀；8.5–9 出色且独特；9.5–10 极罕见、需充分证据，不能承诺“满分”。

## Profile 权重（各列合计100）

| 轴 | duo_fashion | portrait | cinematic | concept_poster | general |
|---|---:|---:|---:|---:|---:|
| camera | 20 | 18 | 24 | 16 | 20 |
| fashion | 20 | 16 | 8 | 0 | 0 |
| interaction | 18 | 8 | 18 | 0 | 0 |
| identity | 10 | 16 | 10 | 8 | 0 |
| hierarchy | 12 | 14 | 14 | 24 | 25 |
| light_color | 8 | 12 | 12 | 18 | 20 |
| originality | 7 | 10 | 10 | 28 | 27 |
| technical | 5 | 6 | 4 | 6 | 8 |

仅正权重轴参与评分。**同一作品各版本必须使用同一 Profile，不能为提高分数临时调整权重。**

## Hard Gate

先跑 Identity/Blueprint/技术 Gate。硬伤可让加权总分被截断：wrong_identity≤5.0、brief_violation≤5.5、unreadable_subject≤5.5、crop_conflict≤6.5。报告原始加权分、截断后的总分及原因。高光色分数不能掩盖 IP 错误或人物构图失效。

## 评分、反馈与学习闭环

1. 当用户要求“给这稿打分”，提供 `[SPEC | profile | self-rated | confidence]`、一位小数的总分、八轴分项与每轴可观察证据、最重要的一个弱点。
2. 有生成图时重新以 IMAGE-REVIEWED 评价**实际可见**的成图，不能引用 SPEC 对未出现细节的赞美。
3. **锁定已认可维度**，以最低的高权重轴确定一个优先修复变量，并路由回 aesthetic-director-core / character-design-engine / illustration-direction / renderer，禁止 Evaluation Loop 亲自重写方案。
4. `compare` 只比较相同 work_id/stage/profile/rater 的两稿；逐轴显示变化与加权贡献。这是描述性变化，不等于严格因果 A/B。
5. `calibrate` 对同稿、同阶段、同 profile 的助手与用户评分计算偏差。至少三个独立作品的配对才作趋势判断；不能自动修改权重、晋升个人偏好。
6. 用户只给整体评分时直接记录文字反馈，不伪造八轴分项。脚本对结构化用户分项要求相同证据标准。
7. 不自动持久化到公开仓库；只在用户授权记录时保存**短证据**与评分，不上传原图、私密链接或整篇 Prompt。偏好晋升仍归 feedback-learning-loop。

## CLI

```bash
python3 scripts/aesthetic_score.py template --profile duo_fashion --stage SPEC --work-id endfield-sport --version v1 > review.json
# 由评审者填写各轴的 score 和 evidence
python3 scripts/aesthetic_score.py score --file review.json
python3 scripts/aesthetic_score.py compare --before v1.json --after v2.json
python3 scripts/aesthetic_score.py calibrate --assistant ai.json --user user.json
python3 scripts/aesthetic_score.py record --file review.json
python3 scripts/aesthetic_score.py validate
```

脚本做数学与契约验证，**不自动看图、不产生未经人审的审美分数**。对不能访问的图片只说明证据不足。
