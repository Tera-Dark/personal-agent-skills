# P13 Real-Task Regression Suite

> P13 is the reality check after P2–P12.
> It does not ask whether a rule exists; it asks whether the whole harness still makes the kinds of
> decisions the owner actually wants on recent creative tasks.
>
> This suite is intentionally model-agnostic. The same task should be run in a fresh Web-first chat
> against the current bundle, then optionally compiled to Anima for prompt-level verification.

## 0. Regression protocol

Each case is run twice when practical:

1. Design pass — let the harness produce the design / blueprint.
2. Anima pass — compile that finished packet through the Anima pipeline.

Record:

~~~text
case: <P13-...>
target: design | anima
result: PASS | FAIL | BLOCKED
prompt: <final prompt when applicable>
visual_notes: <what the generated image actually did>
failed_layer: <if FAIL>
regression_owner: <skill>
~~~

### P13 scoring

Every case is judged on five primary axes:

| Axis | PASS | FAIL |
|---|---|---|
| Direction | one clear visual thesis with an actual action / event | generic role + adjective stack |
| Structure | readable silhouette + dependent garment / composition decisions | slot filling or decoration-first design |
| Distinctiveness | one memorable punctum + one deliberate strange point | many interchangeable motifs or no memorable point |
| Density | intentional dense pocket + quiet field | uniform detail wallpaper or empty filler |
| Translation | Anima keeps core facts, relationships and compact structure | tag pile, prompt bloat, syntax invention or design drift |

Do not score “more details” as better. More detail without stronger decisions is a regression.

---

## 1. Modern gacha / commercial character key visual

### P13-01 — Modern gacha OC, white field

Task:
> 设计一个女性向现代二游女角色，白色背景，全身站立，有明显动作，不要老套的魔法少女、机甲或赛博装饰。

Target: modern key visual + clean plate

PASS:
- silhouette reads before micro-detail;
- one strong motion axis affects body + garment extension;
- asymmetry is structural, not a random earring;
- one local high-density pocket, one quiet field;
- no floating particles / butterflies / roses / magic circles;
- character still feels collectible when reduced to a thumbnail.

FAIL:
- “漂亮长发 + 华丽裙子 + 宝石 + 光效” slot filling;
- centered mannequin pose;
- uniform decoration;
- techwear / mecha inserted without request;
- visual impact depends on bloom instead of silhouette / color masses / construction.

Regression owner: aesthetic-director-core → character-design-engine → Anima pipeline

---

### P13-02 — Miku-like daily fashion without techwear drift

Task:
> 初音未来方向的日常时装，但不要科技服。做年轻女性向、Y2K / acubi / prep 混合，叠穿明显，不对称，有一点怪。

PASS:
- daily-fashion language, not sci-fi costume language;
- layering is created by actual garment hierarchy and overlap;
- one side carries the irregularity;
- hair / accessory silhouette supports the clothing motion;
- no generic cyber interface, armor plating or glowing circuitry;
- “一点怪” is one precise decision, not five eccentric accessories.

FAIL:
- translating “Miku + Y2K” into cyberpunk;
- piling chains, buckles, neon and techwear;
- symmetrical school-uniform cosplay;
- adding unrelated luxury accessories.

Regression owner: director + character-design-engine

---

### P13-03 — High-fashion / maximalist couture

Task:
> 做一套极繁但不俗的女性向高定服装，要求繁杂、有设计感，但不能靠珍珠、蝴蝶、玫瑰、金边堆高级感。

PASS:
- complexity is macro → meso → micro;
- garment architecture has at least one dependency chain;
- hanging pieces have a credible fastening / load / drop direction;
- materials create contrast;
- density is concentrated rather than evenly wallpapered;
- decorations are consequences of the construction, not replacements for it.

FAIL:
- “蕾丝 + 珍珠 + 水晶 + 刺绣 + 宝石” decoration wallpaper;
- no structural reason for the layers;
- every area equally dense;
- generic “luxury / elegant / intricate” as the main design argument.

Regression owner: character-design-engine + aesthetic protection

---

### P13-04 — White-background commercial full-body plate

Task:
> 纯白背景，全身角色立绘，画面要干净、适合商品展示，但不要像站桩模特，也不要往背景里塞装饰。

PASS:
- pose creates readable weight shift;
- silhouette + clothing remain readable against white;
- contact shadow / edge separation does the work;
- one useful floor object is allowed only when it belongs to the design story;
- empty field remains genuinely empty.

FAIL:
- floating flowers / particles / symbols used to fill space;
- arbitrary gradient backdrop;
- stiff front-facing stance;
- light clothing merges into white and the response solves it by adding scenery.

Regression owner: character-design-engine + illustration-direction + aesthetic protection

---

## 2. Couture / material / silhouette transfer

### P13-05 — Ice couture / non-human elegance

Task:
> 做一位冰雪系女性角色的高定时装，核心是寒冷、透明、锋利和贵气；不要普通冰法师模板，不要机械化。

PASS:
- “ice” is translated into silhouette, translucency, edge behavior and material hierarchy;
- one strange detail creates slight danger;
- cold visual mass is balanced by one controlled accent;
- non-human motif is integrated with clothing construction;
- no armor-tech fallback.

FAIL:
- ice crystals pasted on a normal dress;
- blue glow everywhere;
- staff / magic circle / generic wizard accessories;
- danger expressed only through weapons.

Regression owner: director + character-design-engine

---

### P13-06 — Dense outfit still compiles compactly

Task:
> 取一套复杂高定角色设计，要求出 Anima 提示词；token 紧张，尽量短，但不能牺牲核心轮廓和服装关系。

PASS:
- core identity / framing / silhouette / signature garment survive;
- relational NL survives where a tag pile would flatten the structure;
- redundant accessories disappear before structural facts;
- final prompt stays within the compiler's task-appropriate compact budget;
- no quality-word padding.

FAIL:
- truncating the silhouette while keeping decorative adjectives;
- retaining every confirmed tag;
- repeating the same fact in Tag and NL;
- forcing the prompt to hit a numeric target.

Regression owner: skeleton → compressor → compiler

---

## 3. Illustration / authored composition

### P13-07 — Character + environment as authored illustration

Task:
> 给一个女性角色设计一张有故事的竖屏插画。环境必须参与叙事，不要变成“角色站在漂亮背景前”的壁纸。

PASS:
- one visual thesis;
- one captured moment with visible before/after implication;
- environment has agency or evidence of the character's action;
- scale / placement creates intentional hierarchy;
- negative space is designed, not leftover;
- lighting has physical source and useful falloff;
- deleting decorative atmosphere still leaves the composition intact.

FAIL:
- character centered at full height because “主角要突出”;
- city / stars / flowers / particles added as generic atmosphere;
- background is three unrelated scenic layers;
- story is expressed only with facial expression.

Regression owner: illustration-direction + director + Anima pipeline

---

### P13-08 — Reference-to-original transfer

Task:
> 给一张优秀二游角色插画参考图，要求“学习画面的高级感和构图，但重新原创一个角色和视觉逻辑”。

PASS:
- extracts transferable structure first: massing, hierarchy, motif, density, framing, material logic;
- replaces concrete objects with a new causal system;
- original design remains recognizable as a new concept;
- prompt does not become a tag dump or “same thing with one noun changed”.

FAIL:
- snake → dragon / rose → butterfly style noun substitution;
- copying the same silhouette, prop arrangement and motif set;
- generic anime / intricate / cinematic replacing structural analysis.

Regression owner: image-reverse-analysis + director

---

## 4. Cross-task anti-regression checks

### P13-X-01 — one strange thing, not a bag of weirdness
Across P13-01…08:
- each result has at most one deliberate strange point;
- the strange point has a visible location and a reason;
- the rest of the design remains coherent and refined.

### P13-X-02 — one punctum, not decoration inflation
Across P13-01…08:
- one dominant visual punctum exists;
- its color / contrast / placement is intentional;
- additional “attention grabbers” are cut unless the composition explicitly requires them.

### P13-X-03 — local density
At least one dense pocket and one quiet field are identifiable.
Uniform complexity fails even when the design looks “rich”.

### P13-X-04 — no forbidden filler by habit
The harness must not add flowers, butterflies, roses, floating particles, magic circles, random chains, watches, or scenic glow merely because the task is an OC / fantasy / high-fashion request.

These items are not universally forbidden. They are regression alarms when they appear without a structural reason or user request.

### P13-X-05 — white-background discipline
For white-background cases, separation comes first from silhouette, contact shadow, edge treatment, overlap and value structure.
Do not solve every white-background problem with more background.

### P13-X-06 — prompt compression order
When Anima prompt length is under pressure, delete in this order:
decorative prose → redundant adjectives → secondary accessories → repeated materials/colors → non-critical camera wording.
Never delete first:
identity → framing → silhouette → signature garment structure → pose/action → critical relationship → punctum.

### P13-X-07 — design survives adapter translation
For every Anima case, compare the blueprint with final prompt:
- locked facts unchanged;
- one strange point unchanged;
- punctum location unchanged;
- asymmetry unchanged;
- garment hierarchy still legible;
- no rejected element returns as a tag.

### P13-X-08 — output stays personal, not generic-market average
A result can be technically correct and still fail P13 when it falls back to market-average female gacha design.
The acceptance question is:
“如果把角色名遮住，只看轮廓、构造和一个刺点，还像这个 harness 的设计判断吗？”

---

## 5. P13 result sheet

Run this table after each regression cycle:

| Case | Direction | Structure | Distinctiveness | Density | Translation | Result | Failed layer |
|---|---|---|---|---|---|---|---|
| P13-01 |  |  |  |  |  |  |  |
| P13-02 |  |  |  |  |  |  |  |
| P13-03 |  |  |  |  |  |  |  |
| P13-04 |  |  |  |  |  |  |  |
| P13-05 |  |  |  |  |  |  |  |
| P13-06 |  |  |  |  |  |  |  |
| P13-07 |  |  |  |  |  |  |  |
| P13-08 |  |  |  |  |  |  |  |

### Cycle acceptance

A cycle is accepted when:
- no P13 case fails Direction or Structure;
- no Anima case loses a locked fact during translation;
- no case relies on generic decoration as the primary source of sophistication;
- no case exceeds its model adapter budget by padding;
- any failure is routed to its owning layer instead of patched by adding keywords.
