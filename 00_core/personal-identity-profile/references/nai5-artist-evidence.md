# NAI5 Artist Evidence Archive

> Historical working archive moved out of the always-on identity runtime during the v4.0 prompt architecture refactor.
> Source snapshot: 2026-10-08 before runtime-card compaction.

# Personal NAI5 Artist Pool

> Canonical personal artist pool for NovelAI V5 experiments.
>
> Updated: 2026-10-07

## 1. Pool semantics

This file stores artist identity, evidence, manual tiering, style-role tags, and successful combination history.

Current personal NAI5 experiment rule:
- 3–8 artists per experiment
- every artist weight: 0.3–1.2
- at least one artist must be >1.0
- canonical artist syntax: `1.05::artist:name::`
- preserve the `artist:` namespace and any special spelling exactly

Weights belong to a specific experiment. They are not a permanent artist ranking.

Do not persist a weight beside an artist in this pool. A good artist can be used as primary in one experiment and secondary in another.

## 1.1 Current standby small-artist stack

User-confirmed on 2026-10-07 as the current **常备串** for normal NAI5 design work:

1.08::artist:qianben_shan::, 0.91::artist:ruoganzhao::, 0.76::artist:miv4t::, 0.58::artist:min_(120716)::, 0.41::artist:kieed::

Do not treat these weights as permanent artist rankings. This is a confirmed working combination. Individual artists remain separately tiered or experimental unless the user explicitly scores them.

## 2. Manual preference tiers

These four levels represent the user's long-term preference classification. A recent test score is evidence, but historical explicit manual assignments remain authoritative unless the user changes them.

### 夯
_(manual assignment)_

### 顶级
- `artist:starshadowmagician` — user explicitly placed in 顶级; latest single-artist score: **8.5/10**; user says they especially like the soft, feminine line quality and coloring.
- `artist:ask_(askzy)` — user explicitly placed in 顶级; latest single-artist score: **7.5/10**; user says it is not their personal taste, but the style is highly distinctive and strongly summarized. Keep as a **specialized high-value style reference**, not a default personal-style anchor.

### 中等
- `artist:yalmyu` — latest single-artist score: **8.0/10**; particularly strong in the user's **萌系** branch.
- `artist:youlizi-yuri` — latest single-artist score: **7.5/10**; reads as **精美插画 / 华丽角色插画** rather than pure cute-style work.
- `artist:inoriac` — latest single-artist score: **7.0/10**; user found the character output somewhat ordinary, with a possible **场景 / 概念插画** strength that remains to be verified.
- `artist:memuro` — latest single-artist score: **7.0/10**; useful **萌系** reference.
- `artist:kuuus` — latest single-artist score: **7.0/10**; useful **经典王道二次元** reference.

### 次等
- `artist:dino_(dinoartforame)` — latest single-artist score: **6.5/10**; user dislikes the face, although they recognize the overall illustration style as strong.
- `artist:harrymiao` — user says '还可以', classified as second-tier before the current single-artist testing phase.

> Tier note: the latest score is a preference signal, not a mathematical conversion rule. The user may reassign any artist later.

## 3. Style-role taxonomy

Use these tags to choose artists by **function**, not only by overall score.

### Soft / feminine / polished
- `starshadowmagician`
  - style tags: **柔美 / 软线条 / 柔和上色 / 高完成度 / 少女向 / 精美角色插画**
  - strongest use: elegant female portraits, delicate fashion, soft facial appeal, romantic or gentle lighting
  - useful elements: ribbons, lace, flowing hair, jewelry, refined sleeves/collars, pastel or restrained color palettes

### Cute / moe
- `yalmyu`
  - style tags: **萌系 / 甜妹 / 软糯 / 可爱脸 / 轻量装饰**
  - strongest use: cute OC, mascot-like girls, sweet commissions, playful poses
  - useful elements: bows, hair clips, rounded silhouettes, small props, frills, candy/flower motifs
- `memuro`
  - style tags: **萌系 / 童话感 / 小装饰密度 / 可爱角色**
  - strongest use: cute character commissions, animal motifs, maid/frill details, playful accessories
  - useful elements: rabbit/animal motifs, maid elements, frills, ribbons, tiny ornaments

### Elegant / refined illustration
- `youlizi-yuri`
  - style tags: **精美插画 / 华丽角色 / 细节装饰 / 花卉 / 约稿感**
  - strongest use: decorative portraits, refined outfits, floral or romantic themes
  - useful elements: flowers, lace, ornate collars, layered skirts, jewelry, elegant framing

### Classic anime / stable base
- `kuuus`
  - style tags: **经典二次元 / 王道日系 / 清爽角色表现 / 立绘友好**
  - strongest use: stable anime character design, conventional gacha-style girls, clean OC bases
  - useful elements: simple accessories, readable costume blocks, bows, long hair, clean backgrounds

### Strong summarization / design-forward
- `ask_(askzy)`
  - style tags: **强概括 / 高辨识度 / 设计感 / 平面化倾向 / 独特造型语言**
  - strongest use: style contrast, graphic character design, distinctive silhouettes
  - useful elements: bold shape language, simplified accessories, strong costume silhouette, graphic color blocks
  - personal-fit note: aesthetically interesting but not a default personal-style choice.

### Polished commercial illustration / face-sensitive
- `dino_(dinoartforame)`
  - style tags: **商业插画 / 高完成度 / 精致刻画 / 人物脸型辨识强**
  - strongest use: polished character illustration where face design is deliberately chosen
  - useful elements: fashionable costumes, decorative hair, controlled lighting, presentation-focused framing
  - personal-fit note: overall style is respected, but the user does not currently prefer the face.


### Cold dark / rough painterly
- `huke`
  - verification: exact Safebooru/Danbooru artist tag confirmed; indexed artist count observed at **2790** on 2026-10-06. citeturn659470search0turn659470search1
  - style tags: **冷灰 / 阴郁 / 粗粝线条 / 概括感 / 半厚涂倾向 / 工业感**
  - strongest use: bleak sci-fi posters, weathered character key visuals, industrial or post-apocalyptic scenes
  - best-fit elements: blue-gray palettes, black technical clothing, rain, ruins, hard rim light, rough material surfaces, sparse environments
  - status: newly added external experimental artist; not user-tiered.

### Scene / concept candidate
- `inoriac`
  - style tags: **清爽二次元 / 场景潜力 / 概念插画候选**
  - strongest use: scene-led illustrations, worldbuilding, character-in-environment tests
  - useful elements to test next: environmental lighting, props, architecture, atmospheric perspective
  - status: **scene/concept hypothesis only**, not yet confirmed.

## 4. Single-artist test records — 2026-10-06

These are user-scored individual tests. **Scores do not automatically change the four manual preference tiers.** Artists remain manually tiered unless the user explicitly reassigns them.

### `artist:zhi_xu_li_ming`
- Score: **8.0/10**
- User feedback: "还可以".
- Style tags: **精致柔和 / 细腻笔触 / 精致风肖像**
- Best-fit elements: delicate facial details, refined hair, elegant costume details, restrained lighting, portrait framing.
- Status: individually positive, tier remains manually unassigned.

### `artist:kurikabacha`
- Score: **8.0/10**
- User feedback: "还可以".
- Style tags: **精致柔和 / 细腻笔触 / 精致风肖像**
- Best-fit elements: delicate portrait, soft rendering, refined clothing details, gentle light, decorative close-up composition.
- Status: individually positive, tier remains manually unassigned.

### `artist:zhanzhan_lan`
- Score: **7.5/10**
- User feedback: suitable for "精致肖像"; brushwork is slightly light and blurry.
- Style tags: **精致肖像 / 淡雅 / 轻柔笔触 / 低对比 / 轻微朦胧**
- Best-fit elements: pale palettes, soft portraits, elegant clothing, diffuse light, airy backgrounds.
- Caution: can become too soft or lose edge clarity.

### `artist:shu_bing`
- Score: **7.0/10**
- User feedback: "效果一般，适合插画类".
- Style tags: **插画型 / 场景插画 / 非纯人物向**
- Best-fit elements: narrative illustration, environmental composition, decorative props, scene-led character pieces.
- Status: stronger as illustration than pure portrait.

### `artist:sanfu_qwq`
- Score: **7.0/10**
- User feedback: somewhat like **古风精美场景立绘型**.
- Style tags: **古风 / 精美场景 / 角色立绘 / 装饰型**
- Best-fit elements: Chinese costume, architectural scenery, flowers, lanterns, traditional props, elegant standing poses.

### `artist:ruoganzhao`
- Score: **8.0/10**
- User feedback: **精致柔细感 + 场景画风**, but the palette tends yellow and images easily become blurry.
- Style tags: **精致柔细 / 场景型 / 氛围插画 / 暖黄调 / 易糊**
- Best-fit elements: warm environmental light, atmospheric scenes, soft costume details, flowers, architecture, narrative backgrounds.
- Caution: watch yellow cast and loss of detail.

### `artist:qingming_tiaohetu`
- Score: **7.5/10**
- User feedback: distinctive "宝石感", similar to **turino**; considered very good.
- Style tags: **宝石感 / 晶莹质感 / 独特平涂 / 高辨识**
- Best-fit elements: jewel-like eyes, glossy accessories, gemstones, crisp color blocks, decorative fantasy costumes.
- Status: high-value style reference despite mid-range numerical score.

### `artist:qing_yan_xia`
- Score: **7.0/10**
- User feedback: **克制、淡雅、人物设计向的平涂**.
- Style tags: **克制 / 淡雅 / 平涂 / 人物设计 / 简洁色块**
- Best-fit elements: clean costume design, controlled color palettes, graphic silhouettes, subtle accessories, white/empty backgrounds.

### `artist:guigui_rongrong`
- Score: **7.5/10**
- User feedback: **复古亚比感 / 人物动态展示型**.
- Style tags: **复古 / 亚比感 / 动态展示 / 角色表现**
- Best-fit elements: dynamic poses, character showcases, fashion-forward silhouettes, retro styling, presentation-oriented framing.

### `artist:mr._owlish`
- Score: **N/A — no visible effect / excluded from current style-mixing consideration**
- User feedback: "没效果".
- Status: negative/low-signal evidence; do not prioritize in future experiments unless specifically revisiting.

## 5. Single-artist test records — 2026-10-06 (continued)

### `artist:kelezi`
- Score: **7.5/10**
- User feedback:画风比较精致，适合精细人设造型类.
- Style tags: **精致 / 人设造型 / 细节型 / 角色设计**
- Best-fit elements: detailed costume construction, character sheets, accessories, hairstyle design, refined silhouette.

### `artist:diurtion`
- Score: **7.5/10**
- User feedback:画风质感适合情绪流，笔触偏概括，适合简单情绪画面.
- Style tags: **情绪流 / 概括笔触 / 质感 / 简洁叙事**
- Best-fit elements: restrained composition, emotional expression, simple props, atmospheric lighting, minimal scenes.

### `artist:fengjian_yuzhi`
- Score: **8.0/10**
- User feedback:画面清丽甜美，适合精致人物肖像.
- Style tags: **清丽 / 甜美 / 精致肖像 / 少女向**
- Best-fit elements: soft colors, clean portraits, delicate hair, elegant clothing, gentle expressions, pale backgrounds.

### `artist:duoqing_tie_ban_shao`
- Score: **7.5/10**
- User feedback:画面张力十足、色调华丽，人物姿势又有一些克制；适合御姐、张力感插画.
- Style tags: **华丽 / 张力 / 克制姿势 / 御姐 / 高戏剧性**
- Best-fit elements: mature female characters, dramatic poses, rich color palettes, fashion details, dynamic framing.

### `artist:baifeidaiwang`
- Score: **9.0/10**
- User feedback:非常特殊；属于精美人像插画类，画风独特，有点伪厚涂；个人给到9分，但仅适配肖像类.
- Style tags: **精美人像 / 独特画风 / 伪厚涂 / 高级感 / 肖像专用**
- Best-fit elements: close portraits, bust shots, facial rendering, elegant hair, premium costume details, controlled backgrounds.
- Constraint: **portrait-only specialist**; do not treat as a general scene/pose artist.

### `artist:cuso4_suiwabutu`
- Score: **8.0/10**
- User feedback:精美概念人像设计类.
- Style tags: **精美 / 概念人像 / 人物设计 / 高完成度**
- Best-fit elements: conceptual costumes, distinctive character motifs, ornate accessories, designed portraits, fantasy elements.

### `artist:baicumikuo`
- Score: **6.0/10**
- User feedback:本身属于高级精品人物场景插画类，但可能因训练集太少，当前肖像测试效果只有6分.
- Style tags: **高级精品 / 人物场景 / 场景插画 / 训练集敏感**
- Best-fit elements: full scene illustration, environmental storytelling, character-in-world compositions, architecture and props.
- Constraint: **low confidence for portrait testing due to possible training-data limitation**; do not equate the 6/10 portrait score with overall style quality.

### `artist:vlfdus_0`
- Score: **7.0/10**
- User feedback:画风偏西方半写实风.
- Style tags: **西方半写实 / 半写实 / 成熟质感 / 非典型二次元**
- Best-fit elements: mature characters, restrained anime features, realistic costume rendering, dramatic lighting.
- Note: artist identity remains unresolved/ambiguous; preserve exact token and do not infer a different canonical identity.

### `artist:aniao_ya`
- Score: **7.5/10**
- User feedback:偏二游商业海报风格，比较精美.
- Style tags: **二游商业海报 / 商业插画 / 精美 / 宣传视觉**
- Best-fit elements: game-promo composition, character key visuals, strong focal framing, readable costume design, polished lighting.

### `artist:mihiro_00122`
- Status: **permanently blacklisted by user**
- User feedback:使用时出现与 `yellowshark601` 类似的糊图问题.
- Blacklist rule: user explicitly requests that **artists whose canonical artist tag contains digits be blacklisted and not considered for future use**.
- Do not include in random artist selection, single-artist testing, or recommended stacks.

### `artist:tidsean`
- Score: **8.5/10**
- User feedback: "蛮清透".
- Test subject: clear-aesthetic ancient Chinese portrait.
- Style tags: **清透 / 清美古风 / 艺术肖像 / 柔和光感 / 东方人物**
- Best-fit elements: pale hanfu, flowing sleeves, refined hair ornaments, mist, water, willow/plum motifs, restrained cool palettes, airy negative space.
- Status: individually liked; **tier remains manually unassigned**.

### `artist:sainker`
- Score: **8.0/10**
- User feedback: **风格极为独特的艺术插画古典风**.
- Test direction: ornate classical oriental illustration with integrated page / poster layout.
- Style tags: **古典艺术插画 / 极繁 / 独特画风 / 版式设计 / 精品画板 / 装饰构成**
- Best-fit elements: ornamental frames, classical architecture, botanical motifs, antique gold, patterned borders, embedded vignettes, title panels, exhibition / book-plate layouts.
- Best use: **art-board / poster / decorative illustration / premium classical composition**, rather than ordinary clean character portrait.
- Status: individually liked; **tier remains manually unassigned**.

## 6. Confirmed liked / high-value combinations

These artists have been validated through the user's actual NAI5 experiments and should be treated as strong anchors for future exploration.

~~~text
artist:banbanimi
artist:mido_(mido_chen)
artist:pekopeco
~~~

### Validated combination

`artist:banbanimi + artist:mido_(mido_chen) + artist:pekopeco`

User feedback: this combination produced the intended "真正想要的组合搭配效果".

Use it as a **structural reference**, not as a permanent three-artist recipe:
- banbanimi — fashion少女 / OC / 小红书传播感
- mido_(mido_chen) — 二次元角色原画 / 可爱角色 / 二游完成度
- pekopeco — 古风 / 服装 / 柔和留白

## 7. Newly validated experiment combinations — 2026-10-06

**Experiment 17 — liked**

1.05::artist:eteru::, 0.55::artist:banbanimi::, 0.45::artist:pekopeco::

User feedback: "17的那组很好看".

Keep this as a high-value combination sample. Do not infer that every individual artist is independently approved.

**Experiment 19 — liked**

1.04::artist:qing_yan_xia::, 0.56::artist:pekopeco::, 0.48::artist:rei_(sanbonzakura)::

User feedback: "19也不错".

Keep this as a secondary positive combination sample. Do not infer that every individual artist is independently approved.

**Experiment 30 — liked**

1.15::artist:tatatsu::, 0.86::artist:mr._owlish::, 0.69::artist:mafuin_da::, 0.57::artist:zishengtian123::, 0.48::artist:wolrero::, 0.39::artist:bochishiraita::, 0.31::artist:vlfdus_0::

User feedback: "这个组合的效果不错".

Keep this as a high-value combination sample. This approves the combination, not automatic individual tier promotion.

## 8. Existing aesthetic-good candidate pool

These are retained from the personal aesthetic pool. Artists tested individually are still useful pool members; their current classification and role tags are recorded above.

~~~text
artist:zhi_xu_li_ming
artist:zhanzhan_lan
artist:kurikabacha
artist:shu_bing
artist:sanfu_qwq
artist:ruoganzhao
artist:qingming_tiaohetu
artist:qing_yan_xia
artist:mr._owlish
artist:guigui_rongrong
artist:kelezi
artist:diurtion
artist:fengjian_yuzhi
artist:duoqing_tie_ban_shao
artist:baifeidaiwang
artist:cuso4_suiwabutu
artist:baicumikuo
artist:aniao_ya
artist:liduke
artist:jadetilaurant
artist:wolrero
artist:tatatsu
artist:sencha_(senchat)
artist:seapall
artist:rella
artist:rei_(sanbonzakura)
artist:mafuin_da
artist:infukun
artist:pengren_siya
artist:messikid
artist:ergouzi_echo
artist:kikihuihui
artist:tracyton
artist:saku_nosuke
artist:taiki_(luster)
artist:natsuiro_xx
artist:repi
artist:xixizi
artist:luckyia
artist:bochishiraita
~~~

## 9. Current exploration queue

### Tier A — verified Red-direction exploration candidates

~~~text
artist:yalmyu
artist:starshadowmagician
artist:ask_(askzy)
artist:krab_(fumekrab)
~~~

The three already tested above should now be treated as **measured controls**, not pending candidates. `krab_(fumekrab)` remains pending for a future Red-direction single-artist test.

### Positive experiment history — 2026-10-06

**Experiment 35 — liked**
- User feedback: "蛮可爱".
- Keep the exact combination as a positive cute-small-artist reference.

**Experiment 36 — liked**
- User feedback: "蛮可爱".
- Keep the exact combination as a positive cute-small-artist reference.

**Experiment 39 — liked**
- User feedback: "蛮可爱".
- Keep the exact combination as a positive cute-small-artist reference.

## 10. Discovery protocol

When expanding the pool, use this order:

1. domestic creator ecosystem first: 小红书 / 米画师 / 微博 / OC-focused Chinese communities
2. inspect the creator's actual body of work for the user's target zone:
   - female-oriented anime character work
   - OC / 二游 / character illustration
   - attractive first impression
   - clothing and character identity strongly linked
   - collectible / commission appeal
   - clean or intentionally localized high density
3. verify the **exact Danbooru artist tag**
4. require **>50 posts** before entering the experimental pool
5. run a controlled NAI5 portrait test
6. classify by user feedback, with style-role tags recorded alongside the score
7. only treat a style-role hypothesis as confirmed when the user's actual NAI5 output supports it

Do not reverse this order by discovering a random Danbooru artist first and retroactively calling them a "小画师".

## 11. Permanent exclusion

~~~text
artist:yellowshark601
artist:mihiro_00122
~~~

Never use these artists in random selection.

### Global user blacklist rule

- **Any artist tag ending with a digit is blacklisted by default.**
- Do not test, recommend, or randomly select artist tags whose final character is a digit unless the user explicitly overrides this rule.
- Current confirmed examples: `artist:yellowshark601`, `artist:mihiro_00122`, `artist:vlfdus_0`, and `artist:zishengtian123`.
- This is a user-level practical exclusion rule based on repeated observed workflow problems, not a claim about the technical cause of blurry output.
- Historical combinations may retain blacklisted artists as records, but blacklisted artists must never be emitted into new artist stacks.

## 12. Maintenance rules

- Do not silently rename, normalize, split, or "fix" artist tags.
- Preserve underscores, periods, parentheses, suffixes, and other syntax exactly.
- `artist:vlfdus_0` remains unresolved/ambiguous; do not invent a different artist identity.
- Keep confirmed favorites separate from experimental candidates.
- Record user-approved combinations separately from individual artist approval.
- For each single-artist test, record: artist, weight, benchmark, test date, user score, concise feedback, style-role tags, and any confirmed/uncertain suitability.
- When a new artist is promoted, add the evidence source, exact artist tag, verification date, and a short aesthetic role description.

