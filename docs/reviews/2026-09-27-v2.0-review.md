# 审查报告 · personal-agent-skills → v2.0.0

> 审查对象：`main @ c7c1d51`（"docs: sync README with final architecture"）
> 修补分支：`review/v2-restructure`（本工作区内，已提交）
> 日期：2026-09-27

---

## 0. 一句话结论

**"没人味"不是提示词写法的问题，是整个系统里负责品味的那一层根本不存在。** 架构图上写着 `00_core/aesthetic-director-core` 是"创作方向层"，但它没有 `SKILL.md`，只有两个二十行的 reference。Router 说"先跑 aesthetic-director"，AI 找不到东西可跑，就直接落到 `character-design-engine` 那张十三格的空表——然后把每一格填上最常见的值。这就是 AI 味的来源。

结构上，仓库里同时存在三代 Skill（`skills/`、根目录 `anima-prompt-compiler/`、编号层 `0X_`），最成熟的设计知识全在被架构图遗漏的那个根目录 Skill 里，只有用户点名要 Anima 时才会被读到。

v2.0.0 做了两件事：**把品味层真的建出来**，**把三代合成一代**。

---

## 1. 为什么输出没有人味 —— 根因

我把仓库的全部内容读完后，能看出的因果链：

| # | 现象 | 根因 | 后果 |
|---|---|---|---|
| 1 | 输出像模板 | `aesthetic-director-core` 没有 SKILL.md | 架构的核心层是空的；"先理解再生成"没有任何可执行动作 |
| 2 | 每个属性都是最常见值（银发红瞳黑裙） | `character-design-engine` 的输出契约是 13 个空标签 | **表单会被填满，而且每格都填众数**。这是给 LLM 的最差契约形式 |
| 3 | 会避开错误，但不会做出选择 | 全仓库几乎都是禁令（Avoid / Do not / 不要），几乎没有**生成性动作** | 模型知道"不要平庸"之后仍然平庸，因为它没有别的动作可做；禁令越多，它越往安全区退 |
| 4 | 不知道你的品味是什么 | 品味被描述成市场标签（女性向、二游、商业插画） | 市场标签召唤的是该市场的平均值；真正的签名（浅色基底 + 墨色结构 + 一个刺点、有理由的不对称、"漂亮但有点危险"、生物/织物母题）散落在 Anima 的 reference 里，从来没被**命名** |
| 5 | 同一偏好五处副本、互相漂移 | `docs/tera-aesthetic-profile.md`、`personal-identity-profile/references/*`、`anima-user-aesthetic-profile.md`、`anima-human-aesthetic-calibration.md`、`skills/nai5.../SKILL.md § Personal Aesthetic Rules` | 哪份被读到是随机的；NAI5 路径读到的是最粗的那份 |
| 6 | 只有 Anima 出得好 | 六层角色结构、服装词汇、构图协议、反馈诊断全在 `anima-prompt-compiler/references/` | 你最好的设计方法只在一个模型适配器里；NAI5 和其它路径完全拿不到 |
| 7 | 没有"像什么样"的参照 | 全仓库没有一组"通用答案 vs 好答案"的对照 | 对 LLM 来说，**成对示例是传递品味最有效的方式**，规则列表最差 |
| 8 | 修改 = 加东西 | 反馈规则分散、没有"先定位失败层"的强制流程 | "太平淡" → 加肩章加披风加光效 |

结论：**不是缺规则，是缺决策路径、缺命名的品味、缺示例。** 加更多"避免 X"只会更糟。

---

## 2. 结构问题清单

### 2.1 三代并存

| 位置 | 内容 | 状态 |
|---|---|---|
| `skills/creative-prompt-router` | v1 router，路由到 `anima-prompt-compiler` 和 `skills/nai5-prompt-engineering` | 与 `01_router/creative-skill-router` 冲突，两者指向的 Skill 名不同 |
| `skills/nai5-prompt-engineering` | v1 NAI5，8 个 reference，比编号层那份**完整** | 编号层那份是 7 个更薄的 reference |
| `anima-prompt-compiler/`（根目录） | v1.3，最成熟的 Skill，979 行 reference | 不在 README 的树里；`02_creation/anima-prompt-engineering` 是它的 7 行影子 |
| `02_creation/anima-prompt-engineering` | 7 行 | 空壳 |

### 2.2 规范违反（对照 agentskills.io）

| 文件 | 问题 |
|---|---|
| `00_core/aesthetic-director-core/` | **无 SKILL.md** |
| `00_core/personal-identity-profile/SKILL.md` | frontmatter 无 `description`（且 `name` 后有空行，部分解析器会断） |
| `05_evaluation/SKILL.md` | `name: evaluation-loop` 但目录是 `05_evaluation`——spec 要求 name == 目录名 |
| 全部编号层 Skill | `priority:` 是非规范顶层键；`docs/skill-development-guide.md` 还要求 `trigger / input / output / dependencies`，但没有一个 Skill 真的写了 |
| 多数 description | 只写"做什么"，不写"什么时候用"和触发词——这是 Agent 决定是否激活的唯一依据 |

### 2.3 文档漂移

- CHANGELOG 1.3.0 说 SKILL.md 里有 V1/V2 Key Fact Lock，实际 `anima-prompt-compiler/SKILL.md` 里没有 V1/V2 字样（只有 Direct/Standard/Deep）。
- `docs/project-map.md`、`docs/skill-registry.md` 都不提 `anima-prompt-compiler` 和 `skills/`。
- `docs/architecture.md` 与 `docs/creative-system-overview.md` 重复；`docs/skill-specification.md` 与 `docs/skill-development-guide.md` 重复且互相矛盾（一个说 Skill 放根目录，一个说放层目录）。
- 反推流程有三份（`03_analysis/image-reverse-analysis`、`skills/nai5.../reverse-image-analysis.md`、`anima-prompt-compiler § 5`）。

### 2.4 安装问题

编号目录 `00_core/x/SKILL.md` 是两层深，而 Claude Code / Codex 只扫一层（`~/.claude/skills/<name>/SKILL.md`）。根目录的 `anima-prompt-compiler/` 大概率是因为你手动 symlink 了它——这也解释了为什么只有它被用得多、长得好。

### 2.5 占位 Skill

`04_tools/*` 三个 Skill 只有"Does not handle"清单，没有任何操作知识。不删，但应诚实标记为 placeholder，否则 Router 会把技术问题路由到一个空 Skill。

---

## 3. 做了什么

### 3.1 新建品味层（这是修"人味"的核心）

| 文件 | 作用 |
|---|---|
| `00_core/aesthetic-director-core/SKILL.md` | **九个创作动作**（找痴迷点 / 埋矛盾 / 从尾部取样 / 建因果 / 选瞬间 / 减法 / 留一处怪 / 不均匀密度 / 命名刺点）→ 输出 **Creative Brief**。Brief 强制包含【否决的方向】和【删掉的东西】两行——这是"有人做了选择"最直接的证据 |
| `references/creative-moves.md` | 每个动作：解决什么 / AI 默认怎么做 / 设计师怎么做 / 具体手法 / 检验标准。**给替代动作，不只给禁令** |
| `references/taste-calibration-pairs.md` | **六组成对示例**：开放式 OC、"更高级一点"、故事感插画、白底立绘、参考图原创、"太平淡"反馈轮。每组：❌ 一个看起来没问题的典型 AI 答案 → ✅ 走完动作后的版本 → 差别在哪。全部写在你的签名里 |
| `references/feedback-diagnosis.md` | 用户原话 → 失败层 → 修正动作 → 明确不要做。合并了原先散在 Anima 里的三处反馈规则 |
| `references/anti-ai-patterns.md` | 重写为 模式 → 成因 → **替换动作** 三栏；加了"回复语言层面的 AI 味"一节 |
| `references/emotional-design.md` | 扩写：情绪写证据不写形容词（身体 + 物 + 时间痕迹）、表情处理、叙事残留 |
| `references/design-calibration-examples.md` | 从 Anima 迁入：你认可的五个参考设计为什么成立 |

### 3.2 命名品味

| 文件 | 作用 |
|---|---|
| `00_core/personal-identity-profile/references/taste-signature.md` | 一句话签名「**精致的基底上，一处怪，一点危险**」+ 证据表 + Tier A/B/C/D + 边界（签名不是什么）+ 被认可样本日志。合并了五处副本，成为**唯一**的品味来源 |
| `personal-identity-profile/SKILL.md` | 修 frontmatter；声明"其它 Skill 不得再维护品味副本"；写明更新规则 |
| `references/design-dislikes.md` | 补上"手表最高频否决"（原来只在 Anima 里有）；加因果链例外说明 |
| `references/workflow-style.md` | 加「创作类回复的语气」：第一行就是方向、说出否决和删除、不布道、不空夸、结尾给一个分支而不是问"您觉得怎么样" |

### 3.3 设计层：从表单改成方法

| 文件 | 改动 |
|---|---|
| `02_creation/character-design-engine/SKILL.md` | 13 格空表 → **11 步有依赖关系的决定**（命题 → 轮廓策略 → 锚点 → 四层服装 → 材质对抗 → 配色层级 → 姿势+镜头 → 叙事残留 → 展示方式 → 减法 → 反平庸检查）。输出契约要求"删掉的"和"否决的方向" |
| `references/oc-design-system.md` | 从 Anima 迁入（六层结构、五种轮廓策略、姿势-镜头对应） |
| `references/garment-lexicon.md` | 从 Anima 迁入（穿搭原型、四层叠穿、不对称手法、材质碰撞矩阵、领袖腰裙词汇） |
| `02_creation/illustration-direction/SKILL.md` | 重写：先有瞬间再有构图、人物不默认居中/看镜头/占满、光必须有物理来源、背景只留一层、氛围物默认删、预设只开一个 |
| `references/composition-patterns.md` / `atmosphere-presets.md` | 从 Anima 迁入 |

### 3.4 适配器：只翻译，不设计

| 文件 | 改动 |
|---|---|
| `02_creation/anima-prompt-compiler/` | 从根目录迁入；SKILL.md 精简为纯适配器（格式契约、长度预算、V1/V2 模式——CHANGELOG 说有但原文没有的，现在补上了、模型档案、伪影排查）。加**输入检查**：收到的不是 blueprint 就退回 |
| `02_creation/nai5-community-prompt-engineering/` | 合并两份副本，保留更全的 reference；删掉私有的"Personal Aesthetic Rules"；新增 § 9「翻译 blueprint 时的取舍」（密度用 tag 数量表达、刺点颜色只出现一次、被删的物件不许以 tag 回流）；明确 NAI 质量词是合法的模型级例外 |

### 3.5 其它

| 文件 | 改动 |
|---|---|
| `01_router/creative-skill-router/` | 更新管线表、"概念是否已存在"的判断标准、"适配器只收 blueprint"规则、skill-map 与实际一致 |
| `03_analysis/image-reverse-analysis/` | 合并三份反推流程；区分"忠实还原"与"结构提取做原创" |
| `03_analysis/prompt-analysis/` | 先看设计层再看语法层；禁止用"加词"解决设计问题 |
| `05_evaluation/evaluation-loop/` | 移到符合规范的目录；带六维评分表 + Design Read |
| `04_tools/*` | 标 `status: placeholder`，description 补触发词 |
| `scripts/validate_skills.py` | name==目录、description 存在与长度、重名、非规范键、引用的 reference 文件是否存在、registry 与磁盘交叉检查。**这次发现的所有结构问题，这个脚本都能提前抓到** |
| `scripts/install.sh` | 把编号层里的 Skill symlink 到 `~/.claude/skills/`（或任意目标），解决两层深不被发现的问题 |
| `tests/test-suite.md` | 修路径；新增 Design-01…05 设计层回归用例（只测四项：有动词命题 / 有否决 / 有删除 / 有一处怪） |
| `docs/` | 8 → 4 个文件；`architecture.md` 加"人味的可操作定义"表；`skill-specification.md` 对齐 agentskills.io；`skill-registry.md` 加状态列和"已移除"表 |
| `README.md`、`CHANGELOG.md` | 与实际一致；2.0.0 条目含迁移说明 |

### 3.6 数字

- 文件：67 → 60
- SKILL.md：15 → 13（去掉 2 个重复 router/NAI5、1 个 Anima 空壳，新增 1 个 aesthetic-director）
- 品味副本：5 → 1
- 反推流程副本：3 → 1
- 规范违反：4 类 → 0（`validate_skills.py` 通过，0 error 0 warning）

---

## 4. 我没做、需要你决定的

1. **`04_tools/` 三个占位 Skill 要不要留。** 我留了并标 placeholder。如果短期内不会填内容，建议从 registry 里移到"roadmap"段，别让 Router 看到它们。
2. **`taste-signature.md` 的一句话签名是我从证据里归纳的**（"精致的基底上，一处怪，一点危险"）。这是全仓库最需要你亲自改的一行。如果不准，改它，其它文件都引用它。
3. **六组对照示例里的具体设计**（守夜祭司、蚕丝少女、钉掌骑士等）是我写的，用来示范动作序列。如果某组的 ✅ 你看了觉得"不是我要的"，那正好是最有价值的反馈——告诉我哪一步偏了，我改示例，比改规则有效得多。
4. **语言**：新写的核心内容用中文（跟你原来 Anima 部分一致），prompt 片段用英文。如果你要跨模型分发给不太吃中文的 runtime，可以只把 `aesthetic-director-core/SKILL.md` 翻成英文，reference 保持中文。
5. **Anima 的实验日志**（Log-001…003）我没动。它们仍在 `anima-model-profiles.md`。
6. **NAI5 那边我没有添加任何关于 NovelAI V5 模型本身的断言**——只重组了你已有的内容。你对 NAI5 语法的了解比我从仓库里看到的多，`references/` 里的 tag 语法请你再过一遍。

---

## 5. 怎么验证

```bash
# 结构
python3 scripts/validate_skills.py          # 应输出 OK — 0 errors

# 安装（先 dry-run）
scripts/install.sh --dry-run
scripts/install.sh                          # → ~/.claude/skills

# 人味——跑 tests/test-suite.md § 3 的 Design-01
# 给 agent：「设计一个有创意的原创女性角色。」
# 看输出里有没有这四行：带动词的命题 / 否决的方向 / 删掉的东西 / 一处怪
# 缺三项以上 = 品味层没被加载，检查 router 是否先走了 aesthetic-director-core
```

一个更直接的对照测试：用同一句需求，分别在 `main` 和 `review/v2-restructure` 下跑一次。如果 v2 的输出**字数没有变多但决定变多了**——有一句能复述的念头、有被扔掉的东西、有一处你会犹豫要不要留的细节——就对了。

---

## 6. 后续建议（按收益排序）

1. **每次你认可一版输出，往 `taste-signature.md § 5` 追加一行。** 这是最真实的品味数据，三个月后它比任何规则都准。
2. **每次你否决某类东西 ≥3 次，才写进 `design-dislikes.md`。** 一次性否决不升格——否则禁令又会长回来。
3. **对照示例每季度换血。** 示例被模型看多了会变成新的众数。把被认可的真实案例替换进 `taste-calibration-pairs.md`。
4. **把 `validate_skills.py` 挂到 pre-commit 或 GitHub Actions。** 这次的漂移全部是可以机器发现的。
5. **不要再给适配器加设计规则。** 你会想在 NAI5 里加一句"注意轮廓"——忍住，加到 `character-design-engine` 里，两个适配器就都有了。
