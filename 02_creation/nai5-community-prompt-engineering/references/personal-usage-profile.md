# Personal NAI5 Usage Profile

> Personal override layer for the user's NovelAI V5 workflow.

## 1. Primary use case

The user mainly uses NAI5 as a rapid visual experimentation tool for female-oriented anime, OC, character illustration, portrait, and small-artist style discovery.

Priority:
1. artist-stack exploration and style discovery
2. attractive character / portrait result
3. clothing and character-design readability
4. compact prompt control
5. reproducible copy-paste formatting

Do not drift into long explanatory prompts, generic quality-word soup, or cinematic prose unless explicitly requested.

## 2. Default output mode

When the user asks for an NAI5 prompt or artist string:
- Put the artist stack and the test content in one copyable code block by default.
- Do not split the artist string into a separate block unless requested.
- Keep prose outside the block to one short note at most.
- Do not output a Negative block by default; the user generally maintains their own Undesired Content configuration.
- Do not add workflow parameters such as steps, CFG, sampler, LoRA strength, or ComfyUI syntax unless requested.

## 3. Personal artist-stack experiment mode

### Current proven core + experiment mode

The user's current proven core anchors for the “small-artist / feminine illustration” direction are:
`1.15::artist:starshadowmagician::, 0.92::artist:fengjian_yuzhi::`

This is **not a permanent fixed stack**. Treat the two artists as strong candidate master anchors when building experimental ensembles.

Unless the user explicitly requests a conservative stack:
- total 4–8 artists per experiment
- 1–2 master anchors + 2–6 randomly selected assistants
- every weight: 0.3–1.2
- at least one artist must be >1.0
- no duplicate artist names within one stack
- default to ending the ensemble with `artist collaboration`
- do not mix yellow-pool artists into the main roll
- use weights as experiment variables, not permanent artist rankings
- avoid excessive short-cycle repetition between consecutive experiments

The artist pool stores identity and evidence, not permanent weights.

## 4. Manual artist tiers

The user will manually classify artists into four levels:
- 夯
- 顶级
- 中等
- 次等

Do not infer or auto-promote between these tiers.

Keep the four tiers separate from exploration candidates, liked-combination history, and unverified ecosystem leads.

## 4.5. User-validated artist evidence

The following are explicit user test results and should be treated as evidence records, not automatic permanent weights:

- `artist:yan_zi_yao_yu` — **8.5/10**. Extremely distinctive visual language; use only for special cases where an intentionally dense, highly elaborate overall image treatment is desired. Do **not** treat as a routine mainstream-roll artist.
- `artist:shen_a_fang` — **8/10**. Light, distinctive coloring; especially suitable for conceptual / atmospheric illustration.
- `artist:contactz` — **7/10**. Distinctive high-end small-artist portrait style; good for refined portrait-oriented tests and combinations.

These records preserve the user's qualitative judgments. Do not auto-convert scores into the manual tiers (夯 / 顶级 / 中等 / 次等) unless the user explicitly assigns a tier.

## 4.6. User artist rating tiers

The user's manual rating-to-tier mapping is:
- **夯**: 8.5–10.0
- **顶级**: 7.5–8.4
- **中等**: 6.5–7.4
- **次等 / 不入流**: below 6.5, effectively not worth retaining unless specifically requested

Scored mainstream / non-yellow records currently classified from the user's explicit ratings:
- 夯: `artist:baifeidaiwang` — 9/10; `artist:starshadowmagician` — 8.5/10; `artist:yan_zi_yao_yu` — 8.5/10
- 顶级: `artist:shen_a_fang` — 8/10; `artist:mgong520` — 8/10; `artist:fengjian_yuzhi` — 8/10; `artist:kurikabacha` — 8/10; `artist:zhi_xu_li_ming` — 8/10; `artist:ruoganzhao` — 8/10; `artist:cuso4_suiwabutu` — 8/10; `artist:yalmyu` — 8/10; `artist:ask_(askzy)` — 7.5/10; `artist:youlizi-yuri` — 7.5/10; `artist:zhanzhan_lan` — 7.5/10; `artist:qingming_tiaohetu` — 7.5/10; `artist:guigui_rongrong` — 7.5/10; `artist:kelezi` — 7.5/10; `artist:diurtion` — 7.5/10; `artist:duoqing_tie_ban_shao` — 7.5/10; `artist:jacknife` — 7.5/10; `artist:contactz` — 7/10; `artist:memuro` — 7/10; `artist:kuuus` — 7/10; `artist:qing_yan_xia` — 7/10; `artist:inoriac` — 7/10; `artist:harrymiao` — 7/10
- 中等: `artist:dino_(dinoartforame)` — 6.5/10

Yellow pool remains independent from the mainstream tier roll:
- `artist:qiandaiyiyu` — 7/10 — yellow pool
- `artist:mimonel` — 7/10 — yellow pool

Unscored / only provisionally mentioned artists are not auto-classified. Historical blacklist records remain ineligible regardless of prior score or provenance.

## 5. Two operating modes

### Selection mode

When the user asks for a new artist string from the personal pool, use eligible artists from the current pool and respect manually assigned tiers when available.

### Exploration mode

When the user asks to continue exploring or explicitly says not to use the existing pool, do not sample the personal pool.

Use:
domestic creator ecosystem → **小红书 / 米画师审美匹配** → visual fit → exact Danbooru / NovelAI artist tag → sufficient coverage → controlled NAI5 portrait test → user feedback → pool promotion

Exploration target:
- female-oriented anime illustration
- refined portrait / character illustration
- small-artist / personal style feel
- tasteful character design
- commercial commission / 小画师投稿审美
- Chinese-oriental / fantasy / modern anime directions are all acceptable when visually strong

Hard exclusions:
- do not proactively explore artists whose dominant indexed work is NSFW / erotic / fetish-oriented
- yellow-pool artists are tracked separately and never sampled into the main exploration or roll
- current yellow pool: `artist:qiandaiyiyu` (7/10), `artist:mimonel` (7/10)

Candidates without an exact verified artist tag must not be emitted as NAI5 artist tokens.

### Single-artist test baseline

Every single-artist comparison must include the year tags `year 2025, year 2026` and a compact explicit quality layer. Default quality layer: `masterpiece, best quality, high quality, very aesthetic, high complexity`. Add rendering controls only when the test is intended to compare rendering behavior.

## 6. Default test image

The default comparison test is a refined female character portrait / half-body illustration because it exposes artist differences efficiently.

Test for:
- face design
- hair rendering
- eye treatment
- clothing construction
- accessory density
- line / shading language
- color organization
- female-oriented OC / commission feel

Avoid elaborate backgrounds during basic artist comparison.

## 7. Compactness

Prefer the smallest prompt that controls the image.

Default skeleton:
subject + framing + weighted artist stack + compact quality/complexity + rendering + character appearance + outfit + accessories + expression + pose + minimal background

Do not restate the same information with multiple synonyms.

## 8. Quality and complexity

For normal V5 portrait / character tests:
- high complexity is the default
- ultra complexity is reserved for intentionally dense portrait experiments
- keep quality tags compact
- if NovelAI Quality Tags is already enabled, do not mechanically duplicate the complete automatic quality preamble

A practical explicit quality base is usually: masterpiece, very aesthetic, high complexity.

Add detailed shading, smooth gradients, or anime coloring only when they test a deliberate rendering direction.

## 9. Artist-tag discipline

- Preserve artist: namespace.
- Preserve underscores, parentheses, periods, suffixes, and other exact syntax.
- Never invent a tag from a creator display name.
- Exact tag verification belongs to the exploration stage.
- Any artist tag whose **final character is a digit** is blacklisted by default and must not be tested, recommended, or randomly selected unless the user explicitly overrides it.
- Historical examples: `artist:yellowshark601`, `artist:mihiro_00122`, `artist:vlfdus_0`, `artist:zishengtian123`.
- These historical names may remain for provenance but must never be emitted into new stacks.
- Historical combination records may retain these names for provenance, but they must never be emitted into new prompts.
- Preserve exact artist syntax for eligible artists; do not guess unresolved tags.

## 10. Feedback memory

Record exact artist stack, exact weights, user feedback, date, and whether the feedback approves the combination or an individual artist.

Do not collapse 'this combination looks good' into 'every artist is individually top-tier'.

## 11. Negative / correction strategy

Negative prompting is not part of the default copy block.

Use negative numerical emphasis only for a demonstrated conflict or targeted removal, not as a generic negative list.

## 12. Current normal design mode · 2026-10-07

The artist stack and quality layer are now preset for normal design work.

For ordinary requests such as “设计一个插画 / 做个海报 / 继续设计”, do not repeat the preset artist or quality layer unless the user asks for a full NAI5 prompt.

Spend prompt space on:
- concept and visual metaphor
- macro composition and reading path
- camera / viewpoint / crop / foreground occlusion
- character action and causal storytelling
- environment and object relationships
- typography / graphic layout when relevant
- painterly texture, soft color transitions, and controlled detail density

Current default visual bias:
- domestic female-oriented small-artist commission aesthetics
- softer, atmospheric, painterly rendering rather than hyper-sharp polish
- attractive anime character design without generic moe emphasis
- fashion / costume as part of character identity
- close-up / near-camera compositions when the concept benefits
- photography and film composition translated into illustration
- semi-blank or controlled high-density layouts according to the concept
- poster treated as graphic design first

Single-artist tests remain separate and keep their explicit year and quality tags.
