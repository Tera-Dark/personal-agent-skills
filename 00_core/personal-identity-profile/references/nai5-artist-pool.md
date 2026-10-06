# Personal NAI5 Artist Pool

> Canonical personal artist pool for NovelAI V5 experiments.
>
> Updated: 2026-10-06

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

### Scene / concept candidate
- `inoriac`
  - style tags: **清爽二次元 / 场景潜力 / 概念插画候选**
  - strongest use: scene-led illustrations, worldbuilding, character-in-environment tests
  - useful elements to test next: environmental lighting, props, architecture, atmospheric perspective
  - status: **scene/concept hypothesis only**, not yet confirmed.

## 4. Confirmed liked / high-value combinations

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

## 5. Newly validated experiment combinations — 2026-10-06

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

## 6. Existing aesthetic-good candidate pool

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
artist:mihiro_00122
artist:kelezi
artist:diurtion
artist:fengjian_yuzhi
artist:duoqing_tie_ban_shao
artist:baifeidaiwang
artist:cuso4_suiwabutu
artist:baicumikuo
artist:vlfdus_0
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
artist:zishengtian123
artist:xixizi
artist:luckyia
artist:bochishiraita
~~~

## 7. Current exploration queue

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

## 8. Discovery protocol

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

## 9. Permanent exclusion

~~~text
artist:yellowshark601
~~~

Never use this artist in random selection.

## 10. Maintenance rules

- Do not silently rename, normalize, split, or "fix" artist tags.
- Preserve underscores, periods, parentheses, suffixes, and other syntax exactly.
- `artist:vlfdus_0` remains unresolved/ambiguous; do not invent a different artist identity.
- Keep confirmed favorites separate from experimental candidates.
- Record user-approved combinations separately from individual artist approval.
- For each single-artist test, record: artist, weight, benchmark, test date, user score, concise feedback, style-role tags, and any confirmed/uncertain suitability.
- When a new artist is promoted, add the evidence source, exact artist tag, verification date, and a short aesthetic role description.
