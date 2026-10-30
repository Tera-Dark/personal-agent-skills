# Usage — 怎么让一个对话模型跑在这个 harness 上

## 1. 一个链接启动

\`\`\`
GitHub repository
   ↓
README bootstrap
   ↓
bundle/HARNESS.md
   ↓
commit SHA + pinned HARNESS (if accessible)
   ↓
handshake (only when no task was supplied)
   ↓
router
\`\`\`

HARNESS.md 只常驻真正的 session-wide policy：Identity + Router。创作、Prompt Core、tag gate、renderer、analysis、evaluation 都按任务加载。

## 2. Owner output defaults

设计 OC / 插画或提出 NAI5 / Anima 创作任务时，默认**只交付提示词文本**；只有明确的图片生成或编辑请求才使用生图工具。用户要求“只输出提示词”时，内部设计分析不打印 Creative Brief。普通 NAI5 提示词不重复常备画师串、质量词和 Negative。

局部改色/修改细节用 FAST VARIANT；新角色或插画使用与复杂度匹配的 FULL；已有成品设计转提示词用 AUDIT。执行深度和输出长度独立控制。

## 3. Target prompt flow

### Anima

\`\`\`
design / finished packet
 → Aesthetic / Blueprint Gate
 → Visual Prompt Core
 → Danbooru Tag Gate
 → Anima Renderer
 → Tag + Natural Language
\`\`\`

### NAI5

\`\`\`
design / finished packet
 → Aesthetic / Blueprint Gate
 → Visual Prompt Core
 → Danbooru Tag Gate
 → NAI5 Renderer
 → community tag prompt
\`\`\`

两条路共享同一个 Prompt Packet；不会重新设计一遍角色或画面。

## 4. Web-first contract

正常 Web 使用不需要 repository clone、Python、Node、SQLite 或本地服务器。AI 解析主分支提交 SHA 后，用该 SHA 读取入口和按需模块；API 或固定链接不可用时可退回 main，检查版本并说明一致性未验证。缓存的 API 结果仍可能是旧提交，因此版本固定保障同一会话一致性，不保证最新。

最省事的用法：新对话粘贴仓库链接和需求，例如“读取此仓库，然后按我的偏好写一条 NAI5 双人插画提示词：……”。遇到无法访问链接时，将 `bundle/HARNESS.md` 内容粘贴给 AI；如还需要模型管线，再粘贴对应 `bundle/pipelines/` 文件。完整版很大，只适合作为可容纳它的环境中的备选，不能保证被完整使用。

失败策略：
- standalone module → [card-only]
- pipeline pack → [pipeline-unavailable]
- Danbooru index → [tag-index-unavailable]

## 5. Commands

| 命令 | 作用 |
|---|---|
| /state | 当前状态 |
| /modules | 模块索引与已加载模块 |
| /reload <name> | 强制重新加载 |
| /mode direct\|standard\|deep | 输出模式 |
| /model anima\|nai5\|moss\|other | 目标模型 |
| /new-module <name> | 扩展协议 |
| /version | 版本与构建日期 |

## 6. 开发

\`\`\`bash
python3 scripts/validate_skills.py
python3 scripts/build.py
python3 scripts/validate_skills.py --check-bundle
\`\`\`

`bundle/manifest.json` 中的 token 数是粗略估算，实际取决于模型与平台。

## 7. CI / tag-index maintenance

日常 PR 使用仓库已提交的标签索引快照，离线检验结构，然后在 Runner 中生成并检查 Bundle；不要求 PR 作者手工提交生成产物。合入 main 后，CI 自动提交更新的 Bundle。

确实需要更新第三方 Danbooru 数据时，在 GitHub Actions 选择 **main** 手动运行 `harness`，开启 `sync_tag_index`。验证任务将已检查的快照传给提交任务；其他分支上的手动运行只验证，不写入 main。不把第三方 main 的最新内容强行绑定到每次代码修改。
