# Extension Protocol — 通过聊天给 harness 加能力

> 这份文件在 `/new-module` 时加载。它定义：当 owner 在对话里说"加一个 X 的功能"时，模型要产出什么、放哪里、怎么上线。
> 目标：owner 不需要理解仓库结构，只需要把模型给的文件提交到 GitHub；CI 会验证并重建 bundle。

---

## 1. 先判断：是新模块，还是改旧模块

对照 harness 索引（KERNEL §5）：

| 情况 | 做法 |
|---|---|
| 已有模块负责这个职责 | **不建新模块**。指出要改的文件（`<layer>/<name>/SKILL.md` 或某个 reference），给出完整替换后的文件或明确的插入段落 |
| 已有模块负责 80%，缺一块知识 | 给该模块加一个 `references/<topic>.md`，并在 SKILL.md 的 References 段加一行 |
| 真的没有人负责 | 新建模块，按下面走 |

一个模块一个职责。"图片生成全能助手"不是模块；"给 Midjourney 写提示词"、"整理 LoRA 训练集的打标"是。

## 2. 选层

```
00_core         品味、创作方向（很少新增；改动要极谨慎）
01_router       路由（几乎不新增；新模块只需在自己的 description 里写好触发词，router 会读索引）
02_creation     设计 Skill（模型无关）或模型适配器（只翻译）
03_analysis     分析：图 → 结构；prompt → 问题
04_tools        技术执行：ComfyUI、LoRA、数据集
05_evaluation   评价与迭代
06_extensions   以上都不合适的：owner 的"杂七杂八"（例如：给推文配文案、整理灵感库、翻译设定集、生成角色问卷）
```

不确定就放 `06_extensions`。之后可以移。

## 3. 命名

- 目录名 = `name` = 小写字母、数字、单个连字符。≤ 64 字符。
- 名字说职责，不说技术："`midjourney-prompt-adapter`" 而不是 "`mj-helper`"；"`tweet-caption-writer`" 而不是 "`social`"。
- 适配器以 `-adapter` 或 `-prompt-*` 结尾；分析类以 `-analysis` 结尾；这只是惯例，不是校验项。

## 4. 文件结构

```
<layer>/<name>/
├── SKILL.md              必需：过程
└── references/           可选：知识（词表、模式、参数、示例、实验记录）
    └── <topic>.md
```

**SKILL.md 写过程，references 写知识。** SKILL.md 控制在 ~5000 tokens 以内。

## 5. SKILL.md 模板

完整模板在 `kernel/templates/SKILL.template.md`。骨架：

```markdown
---
name: <directory-name>
description: <一句话做什么>. <一句话什么时候用，含中英文触发词>. <一句话不做什么（如果是适配器：Does not design）>.
metadata:
  author: Tera-Dark
  version: "0.1.0"
  layer: "<layer>"
  load: "on-demand"
  status: "active"
  triggers: "<逗号分隔的触发词，中英混排>"
---

# <Title>

## 定位
输入是什么、输出是什么、上游下游是谁、明确不做什么。

## 硬规则
MUST / MUST NOT，3–7 条。

## 执行流程
有先后依赖的步骤。后一步由前一步推出。

## 输出契约
精确的输出形状。创作类必须含「删掉的」「否决的方向」。

## 自检
输出前逐项打勾的清单。

## References
- `references/<topic>.md` — 一行说明
```

### frontmatter 字段

| 字段 | 必需 | 规则 |
|---|---|---|
| `name` | 是 | == 目录名 |
| `description` | 是 | ≤ 1024 字符；**做什么 + 什么时候用 + 触发词**；不含 `<` `>` |
| `metadata.author` | 否 | 字符串 |
| `metadata.version` | 否 | 字符串，引号包住 |
| `metadata.layer` | 是（本仓库） | 所在层目录名 |
| `metadata.load` | 是（本仓库） | `always` 或 `on-demand`。新模块一律 `on-demand`；`always` 需要 owner 改 `harness.json` |
| `metadata.status` | 是（本仓库） | `active` / `placeholder` / `planned` |
| `metadata.triggers` | 推荐 | 逗号分隔字符串，进索引表 |

不要用 `priority` / `trigger` / `input` / `output` 等非规范顶层键。

## 6. 适配器的额外要求

如果新模块是某个图像模型的适配器：

- 定位段必须写：**只翻译，不设计**；收到的不是 blueprint 就退回 director。
- 不得有"个人审美规则"段。品味在 `personal-identity-profile`。
- 任何关于该模型行为的断言必须带证据标签 `[Official]` `[Community]` `[Personal experiment]` `[Unverified]`。**宁可写 `[Unverified]`，不要编参数。**
- 有一个「翻译 blueprint 时的取舍」段：这个模型的格式会丢失什么关系（因果 / 密度 / 刺点位置），怎么补救。

## 7. 非创作类模块（"杂七杂八"）

同样的结构。区别只在内容：

- 定位段说清输入输出。
- 输出契约仍然要精确（表格 / 列表 / 固定字段），不要"生成一段合适的文字"。
- 自检清单仍然要有。
- 如果它和 owner 的品味有关（例如写文案），在硬规则里引用 `personal-identity-profile/references/workflow-style.md` 的语气规则，不要另写一套。

## 8. 输出格式（给 owner 的回复）

```
新模块：<name>（层：<layer>）
理由：<一行：为什么现有模块不覆盖>

<path>/SKILL.md
```markdown
...完整文件...
```

<path>/references/<topic>.md   （如有）
```markdown
...完整文件...
```

上线步骤：
1. 把上面的文件按路径提交到 main（GitHub 网页 "Add file" 即可）。
2. CI 会自动校验并重建 bundle/；几分钟后新会话里就能用。
3. 本次会话我已按这个模块工作。
```

**不要**输出片段、"…此处省略…"、或让 owner 自己补全的占位符。

## 9. 自检（模型在输出新模块前）

- [ ] 索引里没有已经负责这个职责的模块？
- [ ] `name` == 目录名，只含 `[a-z0-9-]`？
- [ ] description 有做什么 + 什么时候用 + 触发词？
- [ ] `metadata.layer` / `load` / `status` 都有？
- [ ] SKILL.md 六段齐全？知识在 references 而不是 SKILL.md？
- [ ] 如果是适配器：有"只翻译不设计"、有证据标签规则、没有品味段？
- [ ] 文件完整、路径精确、可直接提交？
- [ ] 告诉 owner 了上线两步？
