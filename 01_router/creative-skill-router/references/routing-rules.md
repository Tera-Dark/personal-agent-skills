# Routing Rules

## Priority

1. Explicit user request
2. Personal identity profile
3. Aesthetic direction
4. Specialist skill
5. Model syntax

## Creative Requests

Always consider:

- personal-identity-profile
- aesthetic-director-core

before execution skills.

## Mixed Requests

Split different responsibilities.

Example:

OC design + LoRA training

should become:

Character Design
+
Dataset / Training

Do not merge unrelated skills.

## Conflict Resolution

User preferences override generic best practices.

## The One Rule That Prevents "AI 味"

模型适配器只接收**已经做完决定**的输入。判断依据：输入里有没有
- 一句带动词的命题
- 被否决的方向
- 删掉的东西
- 一处怪

四项里缺三项以上 → 不是 blueprint，是需求。退回 `aesthetic-director-core`。
