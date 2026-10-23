# Aesthetic Scorebook · 设计稿/成图量化元数据

由 `06_evaluation/evaluation-loop` 管理，脚本：`scripts/aesthetic_score.py`。这是评分与反馈辅助材料，**不是自动视觉审美算法**。

### 输入与记录

- 每个独立作品使用稳定 `work_id`，不同 Prompt 用 `version`，每张实际图片给出不包含私人路径的 `image_ref`。
- 仅有 Prompt 时用 `SPEC`；评审者实际查看过成图才允许使用 `IMAGE-REVIEWED`。单纯根据用户口头描述不允许伪造视觉评分。
- 评分者标明 `rater: assistant|user`，`confidence: low|medium|high`；每个正权重轴附带分数和一条具体依据。
- 同一作品跨版本比较必须同题材 profile、同阶段、同评分者；助手和用户评分比较仅用于校准偏差。
- `records/` 为可选的**公开 GitHub 数据**。默认不自动写入。必须得到用户明确允许后才运行 `record`。
- 不存原图、完整 Prompt、未公开委托稿、私密链接、隐私信息；短证据亦需在写入公开库前检查。
- 数据只保存每稿的结构化审核记录，不自动成为长期偏好或新的“美商规则”；晋升交给 `personal-identity-profile`。

```bash
python3 scripts/aesthetic_score.py template --profile duo_fashion --stage SPEC --work-id sample-art --version v1 > score.json
python3 scripts/aesthetic_score.py score --file score.json
python3 scripts/aesthetic_score.py compare --before old.json --after new.json
python3 scripts/aesthetic_score.py calibrate --assistant ai.json --user human.json
python3 scripts/aesthetic_score.py validate
```

所有示例评分均须由评审者真实填写，工具不内置假冒“10分作品”的样例或人工评分。
