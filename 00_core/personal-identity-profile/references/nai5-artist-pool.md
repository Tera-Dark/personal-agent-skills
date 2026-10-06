# Personal NAI5 Artist Pool

> Canonical personal artist pool for NovelAI V5 experiments.
>
> Updated: 2026-10-06

## 1. Pool semantics

This file stores **artist identity candidates**, not permanent weights.

Weights belong to an individual NAI5 experiment and must follow the current NAI5 emitter rule:
- one primary artist: approximately `0.95–1.10`
- secondary artists: `<=0.6`
- canonical artist syntax: `1.05::artist:name::`
- preserve the `artist:` namespace and any special spelling exactly

Do not persist a weight beside an artist in this pool. A good artist can be used as primary in one experiment and secondary in another.

## 2. Confirmed liked / high-value combinations

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

## 3. Newly validated experiment combinations — 2026-10-06

**Experiment 17 — liked**

1.05::artist:eteru::, 0.55::artist:banbanimi::, 0.45::artist:pekopeco::

User feedback: "17的那组很好看".

Keep this as a high-value combination sample. Do not infer that every individual artist is independently approved.

**Experiment 19 — liked**

1.04::artist:qing_yan_xia::, 0.56::artist:pekopeco::, 0.48::artist:rei_(sanbonzakura)::

User feedback: "19也不错".

Keep this as a secondary positive combination sample. Do not infer that every individual artist is independently approved.


## 4. Existing aesthetic-good candidate pool

These are retained from the personal aesthetic pool. They are valid candidates for experiments, but unless listed in §2 they should not be described as individually validated favorites.

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

## 5. Current exploration queue

### Tier A — promising ecosystem hits; verify before adding to the experimental pool

~~~text
artist:eteru
artist:harrymiao
~~~

Reason:
- Both are featured creators in the 2026 米画师 × 中信出版《梦绘师 DreamMaker》 OC project.
- `eteru` has an observed Danbooru-family artist count above the current >50-post gate.
- `harrymiao` likewise clears the current >50-post gate in the observed Danbooru-family index.
- They still need personal-aesthetic scoring and controlled NAI5 tests before becoming confirmed favorites.

### Tier B — ecosystem leads; exact artist tag and post count still need verification

~~~text
圈点儿
桑杰尔
~~~

These names are useful discovery leads because they are explicitly featured by 米画师's current OC-focused DreamMaker project, but they must not be converted into NAI5 artist tags until the exact Danbooru artist identifier and >50-post threshold are independently verified.

## 6. Discovery protocol

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

## 7. Permanent exclusion

~~~text
artist:yellowshark601
~~~

Never use this artist in random selection.

## 8. Maintenance rules

- Do not silently rename, normalize, split, or "fix" artist tags.
- Preserve underscores, periods, parentheses, suffixes, and other syntax exactly.
- `artist:vlfdus_0` remains unresolved/ambiguous; do not invent a different artist identity.
- Keep confirmed favorites separate from experimental candidates.
- Record user-approved combinations separately from individual artist approval.
- When a new artist is promoted, add the evidence source, exact artist tag, verification date, and a short aesthetic role description.
