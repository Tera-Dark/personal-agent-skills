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

### Fixed current artist stack
Unless the user explicitly overrides it, the current fixed NAI5 artist stack is:
`1.08::artist:qianben_shan::, 0.91::artist:ruoganzhao::, 0.76::artist:miv4t::, 0.58::artist:min_(120716)::, 0.41::artist:kieed::`

Treat this as a **fixed stack**, not a recommendation to add other artists. Do not append additional artists to it unless the user explicitly asks to experiment with the stack.


Unless the user explicitly requests a conservative stack:
- 3–8 artists per experiment
- every weight: 0.3–1.2
- at least one artist must be >1.0
- no duplicate artist names within one stack
- no requirement for a single primary + low-weight secondary hierarchy
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

## 5. Two operating modes

### Selection mode

When the user asks for a new artist string from the personal pool, use eligible artists from the current pool and respect manually assigned tiers when available.

### Exploration mode

When the user asks to continue exploring or explicitly says not to use the existing pool, do not sample the personal pool.

Use:
domestic creator ecosystem → visual fit → exact Danbooru artist tag → >50 posts → controlled NAI5 portrait test → user feedback → pool promotion

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
- Current examples: `artist:yellowshark601`, `artist:mihiro_00122`, `artist:vlfdus_0`, `artist:zishengtian123`.
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
