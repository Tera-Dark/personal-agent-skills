# Personal NAI5 Artist Pool

> Canonical personal artist pool for NovelAI V5 experiments.
>
> Updated: 2026-10-06

## 1. Pool semantics

This file stores artist identity, evidence, manual tiering, and successful combination history, not permanent weights.

Current personal NAI5 experiment rule:
- 3–8 artists per experiment
- every artist weight: 0.3–1.2
- at least one artist must be >1.0
- canonical artist syntax: `1.05::artist:name::`
- preserve the `artist:` namespace and any special spelling exactly

Weights belong to a specific experiment. They are not a permanent artist ranking.

Do not persist a weight beside an artist in this pool. A good artist can be used as primary in one experiment and secondary in another.

## 2. Manual preference tiers

The user will manually classify the artist pool into four levels. Do not infer or auto-promote between these levels.

### 夯
_(manual assignment)_

### 顶级
_(manual assignment)_

### 中等
_(manual assignment)_

### 次等
- `artist:harrymiao` — user says '还可以', classify as second-tier for now.

### 未分级 / experimental
All other artists remain here until manually assigned.

## 3. Confirmed liked / high-value combinations

These artists have been validated through the user's actual NAI5 experiments and should be treated as the strongest current anchors for future exploration.

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

## 4. Newly validated experiment combinations — 2026-10-06

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

User feedback: '这个组合的效果不错'.

Keep this as a high-value combination sample. This approves the combination, not automatic individual tier promotion.

## 5. Existing aesthetic-good candidate pool

These are retained from the personal aesthetic pool. They are eligible experiment candidates, but individual preference tier is intentionally left unassigned until the user performs manual comparison.

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

## 6. Current exploration queue

### Tier A — verified new exploration candidates; ready for NAI5 controlled testing

~~~text
artist:memuro
artist:inoriac
artist:kuuus
artist:youlizi-yuri
~~~

#### memuro
- Exact artist tag: `artist:memuro`
- Observed count: 167–171 posts in recent Danbooru-family results.
- Ecosystem: Chinese-language illustrator; social profile identifies a Chinese-language creator and links Chinese social accounts. Recent work includes cute anime girls, frills, ribbons, simple/white backgrounds and character-centered composition.
- Visual fit: **high** for cute, soft, decorative character tests.
- Status: verified exploration candidate; not user-tiered.

#### inoriac
- Exact artist tag: `artist:inoriac`
- Verified artist profile count: 238 posts.
- Ecosystem: artist profile links Weibo, Bilibili, Lofter and Xiaohongshu; recent posts include character illustration, fashion/costume and anime game work.
- Visual fit: **high** for polished anime character art with stronger color/motif structure.
- Status: verified exploration candidate; not user-tiered.

#### kuuus
- Exact artist tag: `artist:kuuus`
- Verified observed count: 193 posts.
- Ecosystem: recent Danbooru-family post is sourced from Xiaohongshu; external artwork indexing identifies kuuus as a Chinese anime artist.
- Visual fit: **high** for elegant game-character illustration, costume, flowing hair and larger compositional motion.
- Status: verified exploration candidate; not user-tiered.

#### youlizi-yuri
- Exact artist tag: `artist:youlizi-yuri`
- Verified observed count: 134 posts on recent Danbooru-family results.
- Ecosystem: multiple indexed works are directly sourced from Xiaohongshu and Weibo, including original/OC, commission, school-uniform and Chinese-style character illustrations.
- Visual fit: **high** for character-focused commission work, expressive faces, costume and decorative detail.
- Status: verified exploration candidate; not user-tiered.

### Tier B — ecosystem leads; exact artist tag and post count still need verification

~~~text
圈点儿
桑杰尔
律秋 / lvqiu
華野 / Hananohara_Cano
-蒸ZHENG--
极度缺米的小草草 / carol_cao_
~~~

These names remain leads only and must not be emitted as NAI5 artist tokens until their exact Danbooru identifier and >50-post threshold are independently verified.

## 7. Discovery protocol

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
6. promote to §2 only after the user explicitly likes the result

Do not reverse this order by discovering a random Danbooru artist first and retroactively calling them a "小画师".

## 8. Permanent exclusion

~~~text
artist:yellowshark601
~~~

Never use this artist in random selection.

## 9. Maintenance rules

- Do not silently rename, normalize, split, or "fix" artist tags.
- Preserve underscores, periods, parentheses, suffixes, and other syntax exactly.
- `artist:vlfdus_0` remains unresolved/ambiguous; do not invent a different artist identity.
- Keep confirmed favorites separate from experimental candidates.
- Record user-approved combinations separately from individual artist approval.
- When a new artist is promoted, add the evidence source, exact artist tag, verification date, and a short aesthetic role description.
