# Usage — 怎么让一个对话模型跑在这个 harness 上

> 面向 owner。模型看的是 `bundle/HARNESS.md`；这份文件解释背后发生了什么、每个平台怎么接、坏了怎么查。

---

## 1. 它是怎么"一个链接就能用"的

```
你发：https://github.com/Tera-Dark/personal-agent-skills
   │
   ▼  模型抓取仓库首页 → 看到 README 最上面的 AI 引导块
   │
   ▼  引导块让它抓 raw 的 bundle/HARNESS.md（一个文件，≈23k tokens）
   │
   ▼  HARNESS.md = kernel（运行契约）+ 模块索引（每个模块的触发词、URL、卡片）+ always-on 模块全文
   │
   ▼  模型回一行握手：Harness v3.4.0 loaded · current modules · 说需求，或发参考图。
   │
   ▼  你提需求 → router 选单模块或 pipeline pack → 按索引里的 raw URL 抓取；多阶段 Web-first 管线优先一次抓 pack
```

关键设计：

- **一次抓取拿到全部"必须有"的东西**：kernel、身份档案、审美导演（含九个动作、反馈诊断、六组对照示例）、router、评价环。这些是"人味"的来源，所以永远在。
- **设计与适配器按需抓**：character-design-engine、illustration-direction、三个适配器、两个分析模块。每个是一个自包含文件（SKILL.md + 全部 references）。
- **抓不到也能降级**：索引里每个模块带一张"卡片"（它的契约）。抓取失败时模型按卡片工作并标 `[card-only]`，同时把 raw URL 给你粘贴。
- **握手行 = 版本探针**。看到 `v2.1.0 · 14 modules` 就知道它加载的是哪个版本、索引里有几个模块。数字不对说明抓到了旧缓存或截断。

## 2. Web-first contract

The supported zero-local-runtime path is:

Paste GitHub repo URL → read README bootstrap → fetch raw bundle/HARNESS.md → handshake → route → fetch selected module → deliver.

Normal web use does not require a repository clone, Python, Node, SQLite, an executable, or a local HTTP server. The GitHub page is the discovery/bootstrap surface; the raw Bundle is the runtime source of truth.

Fresh-session rule: prefer current `main` raw Bundle. The handshake version and module count are a freshness probe. On-demand modules and pipeline packs use generated raw URLs from the Bundle index. A pipeline pack counts as one fetch and loads all declared internal stages together. If raw loading fails, use only the affected module cards and mark `[card-only]`; never silently substitute remembered content.

## 3. 各平台

### ChatGPT（有联网）

1. 新对话，第一条消息只发仓库链接（或直接发 `https://raw.githubusercontent.com/Tera-Dark/personal-agent-skills/main/bundle/HARNESS.md`）。
2. 看到握手行。没看到、或它开始"介绍这个仓库" → 回它：`不要总结。按 README 顶部的指令：抓 bundle/HARNESS.md，按它工作，只回握手行。`
3. 发需求或参考图。

已知行为：ChatGPT 一轮里抓取次数有限。Kernel 每轮最多执行 3 个 on-demand fetch；多阶段 Anima 使用一个 `pipeline pack`，因此不会因 7 个内部模块而跨回合。

### Gemini（有 URL 读取）

同上。Gemini 上下文大，也可以直接发 `bundle/HARNESS-FULL.md` 的 raw 链接（≈56k tokens，包含所有模块，之后不需要再抓）。

### 没有联网 / 不能抓 raw

把 `bundle/HARNESS.md` 全文复制粘贴为第一条消息。需要某个模块时模型会说"请粘贴 bundle/modules/<name>.md"，你去仓库复制那个文件贴进去。

### 自定义 GPT / Gemini Gem / Claude Project

- Instructions（系统指令）写：
  ```
  Read the attached HARNESS-FULL.md and operate under it for every conversation.
  Do not summarize it. Handshake per KERNEL §1, then wait for the task.
  ```
- 上传 `bundle/HARNESS-FULL.md` 作为知识文件。
- 仓库更新后重新上传（文件名不变）。

### Claude Code / Codex / Cursor 等会自动发现 skill 的运行时

```bash
scripts/install.sh                    # → ~/.claude/skills
scripts/install.sh ~/.agents/skills   # → Codex
scripts/install.sh ./.claude/skills   # → 项目内
```

它把每个 `<layer>/<name>/` 软链成 `<target>/<name>/`，运行时按 `SKILL.md` 的 description 自动激活。`AGENTS.md` 也会告诉编码型 agent 去读 `bundle/HARNESS.md`。

## 4. 会话里的命令

| 命令 | 作用 |
|---|---|
| `/state` | 看当前锁定事实 / 已认可维度 / 已否决项 / 目标模型 / 模式 / 已加载模块 |
| `/modules` | 看索引和已加载的模块 |
| `/reload <name>` | 强制重新抓某个模块（你刚改了仓库时用） |
| `/mode direct\|standard\|deep` | 适配器输出模式 |
| `/model anima\|nai5\|<其它>` | 目标模型 |
| `/new-module <name>` | 进入扩展协议，让模型产出一个新模块的完整文件 |
| `/version` | 版本与构建日期 |

## 5. 加功能的完整流程

1. 对话里说：`/new-module tweet-caption-writer` 或 "加一个给推文配文案的功能"。
2. 模型先查索引有没有已经负责的模块；没有就按 `kernel/EXTENSION-PROTOCOL.md` 产出完整的 `06_extensions/<name>/SKILL.md`（和可选的 references），每个文件前面是精确路径。
3. 你在 GitHub 网页 → Add file → Create new file，把路径和内容贴进去，提交到 `main`。
4. GitHub Actions 跑 `validate_skills.py`（不合规会红）→ `build.py` → 把重建的 `bundle/` 自动提交回来。
5. 下一个新会话握手行里的模块数 +1。当前会话里模型已经按草稿工作了。

要修改已有模块：同样的流程，改的是 `<layer>/<name>/SKILL.md` 或它的 reference。

## 6. 常见故障

| 现象 | 原因 | 处理 |
|---|---|---|
| 模型开始介绍仓库、列功能 | 没读到 README 顶部引导块，或读了但忽略 | 回它"不要总结，按 README 顶部指令抓 HARNESS.md" ；或直接发 HARNESS.md 的 raw 链接 |
| 握手行版本 / 模块数不对 | 抓到旧缓存；或 CI 还没跑完 | 等 CI 绿 → `/reload`；或新开会话 |
| 说"无法访问链接" | 平台没联网 / raw 域被拦 | 粘贴 HARNESS.md 全文 |
| 输出里没有「否决的方向」「删掉的东西」 | 审美导演没跑（直接跳到了适配器） | 说"走 director"；或检查它是不是把你的需求当成了已完成的 blueprint |
| 适配器编了模型参数 | 违反 kernel §3 证据标签规则 | 回它"给证据标签"；它应改为 `[Unverified]` 或删除 |
| 反馈"太平淡"后它加了一堆东西 | 没走 feedback-diagnosis | 回它"先诊断失败层，不要加" |
| 描述了图里没有的细节 | 违反视觉协议 | 回它"只写 seen: 里真的看到的" |
| CI 红了 | 新模块 frontmatter 不合规（name≠目录、缺 load/status、description 太短） | 看 Actions 日志里的 `ERROR` 行，按提示改 |
| 本地改了 SKILL 但 bundle 没变 | 忘了 build | `python3 scripts/build.py`；推到 main 的话 CI 会自动做 |


**为什么发仓库首页链接也能工作、以及怎么别把它弄坏**：模型抓取 `github.com/...` 拿到的是整页文本——先是文件列表（每一行都带着该文件最近一次提交的**完整**提交信息），然后才是 README。所以：

- 提交信息保持**一行**。多段的提交正文会在文件列表里重复几十次，把 README 顶部的引导块挤到几千字之后。
- 仓库 About（描述）里保留那句给 AI 的引导，它出现在页面标题里，是任何抓取器读到的第一句话。
- 最稳的入口始终是 raw 链接：`https://raw.githubusercontent.com/Tera-Dark/personal-agent-skills/main/bundle/HARNESS.md`，没有任何页面噪音。

## 7. Token 预算

| 文件 | ≈tokens | 用途 |
|---|---|---|
| `bundle/HARNESS.md` | 23k | 默认入口；ChatGPT / Gemini / 粘贴 |
| `bundle/HARNESS-FULL.md` | 56k | 知识文件上传；1M 上下文模型直接发 |
| `bundle/modules/aesthetic-director-core.md` | 15k | 已含在 HARNESS.md 里，单独抓仅用于 `/reload` |
| `bundle/pipelines/anima.md` | 按实际模块合计 | Web-first Anima 单次 fetch，包含 7 个阶段 |
| 其它 on-demand 模块 | 0.7k–7k | 按需 |

`harness.json` 的 `always_on` 决定 HARNESS.md 里嵌哪些文件；`core_budget_tokens`（默认 40000）超了 build 会警告。
