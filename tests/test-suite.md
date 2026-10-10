# 核心验证测试集 (Test Suite)

> Architecture baseline: v4.0.0

> **Version**: 4.0.0  
> **Last Updated**: 2026-10-05  
> **Scope**: 验证创作决策、模型适配、Web-first harness、shared Prompt Core + Anima / NAI5 rendering以及审美回归。

---

## 1. 统一人工评分标准体系 (Evaluation Rubric)

在执行基准回归测试时，依照以下 6 个核心维度对编译输出进行 Pass / Fail 评估：

| 评估维度 (Dimension) | 合格判定标准 (Pass Criteria) | 不合格判定 (Fail Signs) |
| :--- | :--- | :--- |
| **Identity Preservation** | 发色、瞳色、种族与显式外观特征 100% 保持一致。 | 擅自改变发色、瞳色或丢失关键特征。 |
| **Outfit Attribute Binding** | 服装内外层材质与颜色紧密物理绑定，无穿插融色。 | 外套颜色渗入内搭，领口材质混淆。 |
| **Spatial & Layout Clarity** | 景别、构图、背景散景或展示板多图层隔离分明。 | 多图展示板生成双胞胎，或背景喧宾夺主。 |
| **Unrequested Additions** | 未主动脑补未授权的世界观、机械配件或异质设定。 | 擅自增加用户未要求的赛博朋克配件或复杂翅膀。 |
| **V1/V2 Fact Consistency** | V2 美学增强版未篡改 V1 锁定的核心事实（除非标注为可选变体）。 | V2 将 V1 的白发改为金发，或将短裙改为长裤。 |
| **Output Contract** | 遵循当前模式契约，无独立负向词，无禁止质量词，格式正确。 | 出现 `masterpiece` 废词，或夹带独立 Negative 代码块。 |

---

## 2. 基准测试用例集 (Benchmark Test Cases)

### Test-01: 角色属性锁定与未确定信息开放
- **用户输入**：
  > “帮我生成一个银发红瞳的吸血鬼少女，穿黑色维多利亚长裙，神情安静，站在古堡月光下。”
- **预期模式**：Standard Mode
- **评分记录表 (Evaluation Record)**：
  ```markdown
  - [ ] Identity Preservation: Pass / Fail
  - [ ] Outfit Attribute Binding: Pass / Fail
  - [ ] Spatial Clarity: Pass / Fail
  - [ ] Unrequested Additions: Pass / Fail
  - [ ] V1/V2 Fact Consistency: Pass / Fail
  - [ ] Output Contract: Pass / Fail
  - Notes:
  ```

---

### Test-02: 4 层复杂服装叠穿与高级材质碰撞
- **用户输入**：
  > “设计一套冬日高级感穿搭：内搭米色针织高领毛衣，外面套深灰开衫西装，再披一件重磅黑色粗呢大衣，围着燕麦色围巾，下身直筒西装裤。”
- **预期模式**：Standard Mode | Aesthetic: Preset C (High Fashion, see 02_design/illustration-direction/references/atmosphere-presets.md)
- **评分记录表 (Evaluation Record)**：
  ```markdown
  - [ ] Identity Preservation: Pass / Fail
  - [ ] Outfit Attribute Binding: Pass / Fail
  - [ ] Spatial Clarity: Pass / Fail
  - [ ] Unrequested Additions: Pass / Fail
  - [ ] V1/V2 Fact Consistency: Pass / Fail
  - [ ] Output Contract: Pass / Fail
  - Notes:
  ```

---

### Test-03: 前景立绘 + 背景放大头像多尺度展示板
- **用户输入**：
  > “帮我做一张角色设计展示图：前面是这个角色的完整全身立绘，背景放一个她的大尺寸半透明虚化头像，突出眼神和耳坠。”
- **预期模式**：Standard Mode | Mode: Layered Character Showcase
- **评分记录表 (Evaluation Record)**：
  ```markdown
  - [ ] Identity Preservation: Pass / Fail
  - [ ] Outfit Attribute Binding: Pass / Fail
  - [ ] Spatial Clarity: Pass / Fail
  - [ ] Unrequested Additions: Pass / Fail
  - [ ] V1/V2 Fact Consistency: Pass / Fail
  - [ ] Output Contract: Pass / Fail
  - Notes:
  ```

---

### Test-04: 浅色服饰与纯白背景防边缘融色
- **用户输入**：
  > “纯白背景，一个穿白色真丝吊带裙的女孩，全身照，不要多余杂物。”
- **预期模式**：Direct Mode 或 Standard Mode
- **评分记录表 (Evaluation Record)**：
  ```markdown
  - [ ] Identity Preservation: Pass / Fail
  - [ ] Outfit Attribute Binding: Pass / Fail
  - [ ] Spatial Clarity: Pass / Fail
  - [ ] Unrequested Additions: Pass / Fail
  - [ ] V1/V2 Fact Consistency: Pass / Fail
  - [ ] Output Contract: Pass / Fail
  - Notes:
  ```

---

### Test-05: 双角色站位与色彩属性隔离
- **用户输入**：
  > “两个少女并排坐着：左边的金发双马尾穿浅蓝水手服，右边的黑长直穿红白巫女服，彼此微笑着。”
- **预期模式**：Standard Mode
- **评分记录表 (Evaluation Record)**：
  ```markdown
  - [ ] Identity Preservation: Pass / Fail
  - [ ] Outfit Attribute Binding: Pass / Fail
  - [ ] Spatial Clarity: Pass / Fail
  - [ ] Unrequested Additions: Pass / Fail
  - [ ] V1/V2 Fact Consistency: Pass / Fail
  - [ ] Output Contract: Pass / Fail
  - Notes:
  ```

---

### Test-06: 极简社交头像与弹性词数规划
- **用户输入**：
  > “简单画个推特头像，粉色短发微卷的元气少女，眨眼浅笑，背景简单点。”
- **预期模式**：Direct Mode | Aesthetic: Preset B (Sweet Vibrant)
- **评分记录表 (Evaluation Record)**：
  ```markdown
  - [ ] Identity Preservation: Pass / Fail
  - [ ] Outfit Attribute Binding: Pass / Fail
  - [ ] Spatial Clarity: Pass / Fail
  - [ ] Unrequested Additions: Pass / Fail
  - [ ] V1/V2 Fact Consistency: Pass / Fail
  - [ ] Output Contract: Pass / Fail
  - Notes:
  ```

---

### Test-07: 电影海报叙事与胶片质感路由
- **用户输入**：
  > “想要一张王家卫风格的雨夜剧照，短发女人坐在老旧咖啡馆窗边，隔着带雨滴的玻璃看外面，很有故事感。”
- **预期模式**：Standard Mode | Aesthetic: Preset E (Cinematic Auteur)
- **评分记录表 (Evaluation Record)**：
  ```markdown
  - [ ] Identity Preservation: Pass / Fail
  - [ ] Outfit Attribute Binding: Pass / Fail
  - [ ] Spatial Clarity: Pass / Fail
  - [ ] Unrequested Additions: Pass / Fail
  - [ ] V1/V2 Fact Consistency: Pass / Fail
  - [ ] Output Contract: Pass / Fail
  - Notes:
  ```

---

### Test-08: 排除意图转换为正向场景约束
- **用户输入**：
  > “画一个女剑士，不要现代背景，不要复杂的光污染，不要有多余的路人，不要露骨擦边。”
- **预期模式**：Standard Mode
- **评分记录表 (Evaluation Record)**：
  ```markdown
  - [ ] Identity Preservation: Pass / Fail
  - [ ] Outfit Attribute Binding: Pass / Fail
  - [ ] Spatial Clarity: Pass / Fail
  - [ ] Unrequested Additions: Pass / Fail
  - [ ] V1/V2 Fact Consistency: Pass / Fail
  - [ ] Output Contract: Pass / Fail
  - Notes:
  ```

---

## 3. 设计层回归用例 (Design-Layer Cases, v2.0.0)

以下用例不测 Anima 语法，测 `aesthetic-director-core` → `character-design-engine` 这条链有没有真的做决定。任何模型适配器都适用。
评分只看四项，缺三项以上判 Fail：**有带动词的命题 / 有被否决的方向 / 有删掉的东西 / 有一处怪**。

### Design-01: 开放式 OC
- **用户输入**：「设计一个有创意的原创女性角色。」
- **Fail 信号**：输出以职业/种族标签开头（"月光祭司"、"精灵弓箭手"）；发色瞳色服装全是众数；没有【否决的方向】；出现手表 / 蝴蝶 / 玫瑰 / 粒子 / 魔法阵。
- **Pass 参照**：`aesthetic-director-core/references/taste-calibration-pairs.md` Pair 1。
- **记录**：
  ```markdown
  - [ ] 命题含动词: Pass / Fail
  - [ ] 否决的方向 ≥2: Pass / Fail
  - [ ] 删掉的东西 ≥2: Pass / Fail
  - [ ] 一处怪（且只有一处）: Pass / Fail
  - Notes:
  ```

### Design-02: "更高级一点"
- **用户输入**：「白衬衫 + 黑长裙，帮我做得更高级一点。」
- **Fail 信号**：高级 = 加蕾丝 / 珍珠 / 刺绣 / 缎面 / 项链 / 手链；没有任何结构或比例决定。
- **Pass 参照**：Pair 2。至少一个大结构决定 + 一个比例决定 + 一个材质决定，且有删除清单。

### Design-03: "太平淡"反馈轮
- **上下文**：上一版是「墨绿军装长外套女骑士，短发，持剑，白底」。
- **用户输入**：「太平淡了。」
- **Fail 信号**：加肩章 / 勋章 / 披风 / 军帽 / 枫叶 / 光效；回复没有"诊断：失败在 X 层"这一行。
- **Pass 参照**：Pair 6。只动命题层与由它引起的轮廓；装饰不增加。

### Design-04: 参考图原创
- **用户输入**：一张参考图 + 「参考这张的感觉，但要原创。」
- **Fail 信号**：换名词当原创（蛇 → 龙）；输出 `white background, anime, intricate` 类无结构词。
- **Pass 参照**：Pair 5。先列出 3–5 条"真正在起作用的结构"，再换掉全部具体物件。

### Design-05: 适配器拒收需求
- **用户输入**：「帮我写个 NAI5 提示词，一个赛博巫女。」
- **Fail 信号**：适配器直接产出 prompt。
- **Pass**：适配器识别出这不是 blueprint，走 identity → director → character-design-engine 后再编译；赛博元素以签名方式处理（有理由的结构、一处怪、一个刺点），而不是拒绝用户要求。

---

## 4. Harness 层用例 (Harness Cases, v3.1.0)

测的是 kernel 行为，不是任何模块。在 ChatGPT / Gemini 新会话里跑。

### Harness-01: 一个链接冷启动
- **输入**：第一条消息只有 `https://github.com/Tera-Dark/personal-agent-skills`
- **Pass**：回复**只有**一行握手，版本与模块数来自当前 `bundle/manifest.json`；不得使用旧的硬编码版本/模块数。
- **Fail**：介绍仓库、列功能、描述架构、问"需要我做什么"之外的任何多余内容

### Harness-02: 抓取失败降级
- **输入**：在不能联网的会话里发链接
- **Pass**：回复精确为 `我无法访问链接。请把 bundle/HARNESS.md 的内容粘贴给我。`
- **Fail**：假装读到了；或凭训练记忆编一个"harness"

### Harness-03: 按需加载与卡片降级
- **输入**：握手后发「设计一个 OC，出 Anima 提示词」
- **Pass**：模型选择 Anima pipeline pack `anima`；standalone module 抓取失败使用 `[card-only]`；pack 抓取失败使用 `[pipeline-unavailable]`，不得绕过缺失阶段
- **Fail**：不加载直接写；或声称加载了但输出里没有该模块的输出契约结构

### Harness-04: 视觉协议
- **输入**：发一张参考图 + 「参考这张的感觉」
- **Pass**：第一段是 `seen:` + ≤3 行可见内容，推断项带 `?`；随后进入 image-reverse-analysis 的结构拆解
- **Fail**：描述了看不见的细节（织物经纬、精确色值）；或跳过 `seen:` 直接输出 prompt

### Harness-05: 会话状态
- **输入**：锁定「银发、金瞳」后迭代三轮，第四轮发 `/state`
- **Pass**：state 块 ≤12 行，locked 含银发金瞳，prompt 版本号递增，rejected 项在后续输出里没有以 tag 回流
- **Fail**：某一轮把银发改成了别的；或 state 块缺字段

### Harness-06: 证据标签
- **输入**：「Midjourney 上怎么写才能让它更听话？」
- **Pass**：每条模型行为断言带 `[Official]` / `[Community]` / `[Unverified]`；官方参数与社区经验分开
- **Fail**：任何无标签的"MJ 对 X 更敏感"式断言；编造参数

### Harness-07: 扩展协议
- **输入**：`/new-module tweet-caption-writer`
- **Pass**：先查索引说明无重叠；输出 `07_extensions/tweet-caption-writer/SKILL.md` 完整文件（frontmatter 含 name==目录、description 有触发词、metadata.layer/load/status）；六段齐全；末尾给出"提交到 main → CI 重建 → 下会话生效"两步；本会话按草稿工作
- **Fail**：片段、省略号、占位符；缺 frontmatter 字段；写成散文

### Harness-08: 不总结、不布道
- **输入**：握手后发「你能干什么？」
- **Pass**：`/help` 表或一两行指向索引；不复述 kernel，不输出审美理论
- **Fail**：长篇介绍


## 6. Taste Calibration Regression Cases

### Taste-10: Modern Key Visual mode
- Modern gacha / commercial character refs produce strong silhouette + motion axis + color masses + material contrast, not soft atmospheric filler.

### Taste-11: Local density
- Design has 1–2 high-density focal pockets and a quiet field; complexity is not uniform.

### Taste-12: Physical attachment
- Hanging accessories identify a fastening / support relationship.

### Taste-13: Human irregularity
- Eyes are not forced into mirror symmetry; iris highlights and skin rendering remain restrained and tactile.

### Taste-14: Hair mass
- Hairstyle is described as readable masses / roots / wrapping before flyaway strands.

### Taste-15: Compact prompt
- Direct / Standard image prompts stay within the adapter's compact budget unless the owner explicitly requests detail.

## 5. Architecture Gate Regression Cases

### Arch-01: Every creative request passes Aesthetic Gate
- Input: “设计一个高级二游女角色，直接给 NAI5”
- Pass: Aesthetic Gate FULL runs before specialist/adapter; adapter receives only a verified packet.
- Fail: NAI5 adapter invents the character concept.

### Arch-02: Finished design uses AUDIT
- Input: user provides fixed hair, eyes, clothing, pose and palette, asks only for prompt compilation.
- Pass: Aesthetic Gate AUDIT checks readiness, changes no locked fact, then adapter compiles.
- Fail: director silently redesigns a locked garment or silhouette.

### Arch-03: AUDIT escalates instead of inventing
- Input: “银发、红瞳、黑裙，帮我出 NAI5”
- Pass: missing structure is detected and escalated to FULL.
- Fail: adapter invents a whole design and calls it faithful.

### Arch-04: Type-specific Blueprint Gate
- Character packet missing silhouette / garment structure → reject to character-design-engine.
- Illustration packet missing camera / environment relationship → reject to illustration-direction.
- Pass: adapters never fill those gaps.

### Arch-05: Anima skeleton
- Pass: Tag Lock → Natural-language Relations → optional Negative.
- Pass: generic quality-word dump is not reintroduced; model parameters stay outside prompt.
- Fail: adapter becomes a designer or collapses everything into tags.

### Arch-06: NAI5 skeleton
- Pass: Subject → Year/Era → Artist → Quality → Complexity → Rendering → Style Control → Scene → Character → Action.
- Pass: Quality layer remains present and artist: namespace is preserved.
- Fail: quality tags are removed as “fluff” or artist namespace is stripped.

### Arch-07: Artist-mix guard
- Pass: random pool defaults to at most four artists unless explicitly overridden; one primary artist may sit near 1.0 while secondary artists stay lighter.
- Fail: automatic 8–12 artist high-weight stacks.

### Arch-08: Feedback routes to the owning layer
- Input: “这版太平庸”
- Pass: evaluation-loop identifies the highest failed design layer, re-enters Aesthetic Gate / specialist, and preserves approved dimensions.
- Fail: blindly adds decorations or keywords.

### Arch-09: Generated bundle consistency
- Pass: source changes make scripts/validate_skills.py --check-bundle fail until build.py regenerates bundle/; CI rebuilds on push.
- Fail: bundle files are hand-edited or silently drift from source.

## P14 — Aesthetic Floor Regression

> 这组回归由 2026-10-05 的真实测试反馈触发。目标不是让角色“更普通”，而是阻止系统把“辨识度”误解成“故意丑”。

### P14-01: 怪点从属于整体美感
- **输入**：设计一个女性向现代二游女角色，要求一处有点怪、白底全身、非对称、有明显轮廓。
- **Pass**：第一眼美感先成立；比例、姿态、色块和服装结构整体顺眼；怪点只制造局部张力。
- **Fail**：比例被故意做歪、轮廓失衡、配色冲突或服装结构被怪点破坏，却把“不协调”当成辨识度。

### P14-02: 删除怪点后仍然好看
- **输入**：对已经完成的角色设计删除唯一怪点，再比较整体结构。
- **Pass**：核心轮廓、服装工程、色块和商业可读性仍成立，只是少了一层记忆点。
- **Fail**：删除怪点后整套设计立刻变空，说明怪点正在替代命题或大结构。

### P14-03: “丑的很有特点”反馈路由
- **反馈**：丑的很有特点，继续。
- **Pass**：先诊断比例 / 形状节奏 / 配色层级 / 剪裁，再决定是否撤回或替换怪点；不得用“这是刻意的”拒绝修正。
- **Fail**：继续加装饰、加复杂度，或把“丑”包装成用户应该接受的风格。

### P14-04: Modern Key Visual 不以怪换冲击
- **输入**：现代二游商业主视觉，要求强轮廓、强动势、局部极密。
- **Pass**：冲击来自大形、运动轴、大色块、材质和阴影；怪点不是主轮廓。
- **Fail**：靠扭曲比例、随机失衡或大量异质元素制造“独特”。

### P14-05: Token 压缩不保留错误的怪
- **输入**：复杂角色进入 Anima 压缩阶段。
- **Pass**：删掉装饰和解释性文字后，保留健康比例、轮廓、服装层级、动作和唯一刺点；怪点仍是可控局部偏差。
- **Fail**：为了保留“独特”而优先牺牲结构美感，或留下多个奇异元素。

### P14-06: 反馈与长期品味边界
- **输入**：单次出现“丑”的反馈。
- **Pass**：修正本次结果，但不把某个具体元素直接写成永久禁区；系统规则只升级为“怪 ≠ 丑”的通用约束。
- **Fail**：把一次反馈直接永久化成“永远不要某种造型”。
\n\n## P12 Prompt Architecture Regression\n\nThe detailed P12 regression matrix is in `tests/personal-anima-regression.md`.\n\nP12 adds 36 cases across exact/alias/missing/fuzzy tags, character/IP/artist isolation, appearance/clothing/action classification, composite packets, exact Anima syntax and idempotence, Tag/NL skeleton boundaries, compression priorities, aesthetic protection, all P11 failure scopes, Web-first pipeline loading, and the owner's recent gacha/full-body/high-fashion/illustration/reference/token-pressure tasks.\n\nThe deterministic CI gate is `scripts/check_personal_anima_regression.py`; live-index and visual/aesthetic judgments remain manual.\n

## P13 Real-Task Regression

The task-driven acceptance suite is maintained in tests/p13-real-task-regression.md.

It covers 8 real-task scenarios plus 8 cross-task anti-regression checks, emphasizing modern gacha key visuals, layered fashion, white-background full-body work, authored illustration, reference-to-original transfer, compact Anima translation, and protection from generic market-average design.


---

## Web-first Runtime Efficiency Regression

### WEB-EFF-01 — compact always-on identity
- Expect: the always-on identity has `taste-core.md` plus the dislike rules, while the full taste archive and NAI5 artist pool are on-demand only.
- Fail: NAI5 artist records are loaded for unrelated Anima or illustration tasks.

### WEB-EFF-02 — enforced core budget
- Expect: `scripts/build.py` exits with an error if generated `HARNESS.md` exceeds `harness.json:core_budget_tokens`.
- Fail: an over-budget bundle is generated with only a warning.

### WEB-EFF-03 — PROMPT ONLY
- Input: “按这个已完成的人设，只给我 NAI5 提示词。”
- Expect: mandatory Audit, Prompt Core, Tag Gate where applicable, renderer and Design Lock remain; no visible Creative Brief or routing narration.
- Fail: validation is skipped or the user receives a long design explanation.

### WEB-EFF-04 — FAST VARIANT
- Input: “保持原设计和构图，只把主色改成酒红色。”
- Expect: preserve every unaffected locked fact and change only the requested palette variable.
- Fail: silhouette, face, outfit construction or pose is redesigned without request.

### WEB-EFF-05 — full-mode escalation
- Input: “保留原角色，但重新设计整体轮廓和核心命题。”
- Expect: escalate to FULL CREATIVE rather than treating the request as a minor variant.
- Fail: a material design change is forced through FAST VARIANT.

### WEB-EFF-06 — selective reference loading
- Input: create a white-background standing character after loading the module contract.
- Expect: fetch only the required white-background/character-design references; do not fetch all poster and illustration reference documents.
- Fail: all references are bundled into or required by every on-demand module fetch.
