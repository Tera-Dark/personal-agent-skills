# Extension Protocol — 通过聊天给 harness 加能力

## 1. 先判断职责是否已有 owner

| 需求 | 归属 |
|---|---|
| 用户长期偏好 / artist pool | \`00_core/personal-identity-profile\` |
| 创作决策 / 审美 Gate | \`00_core/aesthetic-director-core\` |
| 路由 | \`01_router/creative-skill-router\` |
| 角色 / 画面设计 | \`02_design/*\` |
| 模型无关提示词规划 | \`03_prompt/visual-prompt-core\` |
| Danbooru 证据 | \`03_prompt/danbooru-tag-gate\` |
| 模型语法 | \`03_prompt/<model>-renderer\` |
| 参考图 / Prompt 分析 | \`04_analysis/*\` |
| ComfyUI / Dataset / LoRA | \`05_tools/*\` |
| 评价 / 迭代 | \`06_evaluation/*\` |
| 不属于以上 | \`07_extensions/*\` |

已有模块负责 80% 以上时，扩展现有 owner，不新建第二套职责。

## 2. 一个模块一个职责

新模块必须明确：
- 输入
- 输出
- 上游
- 下游
- 不做什么

禁止创建“全能 prompt 助手”式重叠模块。

## 3. SKILL.md 与 references

\`\`\`
<layer>/<name>/
├── SKILL.md
└── references/
\`\`\`

SKILL.md 写过程；references 写知识、实验记录、词表、参数和示例。

## 4. 适配器边界

模型 renderer：
- 只翻译 Visual Prompt Packet；
- 不维护用户审美副本；
- 不发明 tag；
- 不重新设计 Blueprint；
- 所有模型行为断言带 [Official] / [Community] / [Personal experiment] / [Unverified]。

## 5. 新模块流程

1. 检查现有 owner 与索引。
2. 选择最窄职责层。
3. 用 \`kernel/templates/SKILL.template.md\` 创建模块。
4. 写完整 SKILL.md 与必要 references。
5. 提交前运行 validate + build。
6. 提交到 main 后由 CI 重建 bundle。

## 6. 自检

- [ ] 没有重复 owner。
- [ ] name == directory。
- [ ] metadata.layer == 所在层。
- [ ] model renderer 没有个人审美副本。
- [ ] Prompt Core 与 renderer 的职责没有重叠。
- [ ] 参考资料已被 SKILL.md 的 References 段声明。
