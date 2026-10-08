# Usage — 怎么让一个对话模型跑在这个 harness 上

## 1. 一个链接启动

\`\`\`
GitHub repository
   ↓
README bootstrap
   ↓
bundle/HARNESS.md
   ↓
handshake
   ↓
router
\`\`\`

HARNESS.md 只常驻真正的 session-wide policy：Identity + Router。创作、Prompt Core、tag gate、renderer、analysis、evaluation 都按任务加载。

## 2. Target prompt flow

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

## 3. Web-first contract

正常 Web 使用不需要 repository clone、Python、Node、SQLite 或本地服务器。模块与 pipeline pack 从 Bundle 索引中的 raw URL 按需加载。

失败策略：
- standalone module → [card-only]
- pipeline pack → [pipeline-unavailable]
- Danbooru index → [tag-index-unavailable]

## 4. Commands

| 命令 | 作用 |
|---|---|
| /state | 当前状态 |
| /modules | 模块索引与已加载模块 |
| /reload <name> | 强制重新加载 |
| /mode direct\|standard\|deep | 输出模式 |
| /model anima\|nai5\|<other> | 目标模型 |
| /new-module <name> | 扩展协议 |
| /version | 版本与构建日期 |

## 5. 开发

\`\`\`bash
python3 scripts/validate_skills.py
python3 scripts/build.py
python3 scripts/validate_skills.py --check-bundle
\`\`\`

最终 token 数以 bundle/manifest.json 为准；不要在文档里硬编码过时的估算。
