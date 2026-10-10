# P15 — Creative Harness Behavioral Acceptance Matrix

These prompts require a **live model-in-the-loop** review. CI can enforce static
ownership/output rules and build consistency; it cannot prove visual taste.

| ID | Input | Expected | Failure |
|---|---|---|---|
| P15-01 | 设计个精美 OC 头像 | Prompt text only | Image tool called |
| P15-02 | 请给我生成一张图片 | Generation allowed when a tool is available | Treated as forbidden |
| P15-03 | 按 NAI5 格式只输出提示词 | Copyable positive prompt; no preset stack/quality/Negative/Brief | Extra workflow chatter or preset terms |
| P15-04 | 上一版只改裙子颜色 | FAST VARIANT keeps identity/composition | Full redesign |
| P15-05 | 重新设计插画的镜头和动作 | FULL creative + illustration blueprint | Template scene + prop pile |
| P15-06 | NovelAI artist tag without shard evidence | No claim of exact tag | Guessed canonical identity |
| P15-07 | 白底半身精品 OC | Portrait/character refs only | Downloads all poster grammar |
| P15-08 | 高完成度小画师插画 | Focus, authored crop, meaningful pose, density map, causal environment | Floating decorations/generic background |
| P15-09 | Existing locked design → Anima | Same locked facts in Tag + NL | New design injected by renderer |
| P15-10 | 仅测试画师组合 | Artist policy/verified syntax; no character storyboard | Unrelated brief |
| P15-11 | Upstream tags change without explicit sync | PR works from committed index | Freshness/network failure |
| P15-12 | GitHub unavailable for one module | Honest scoped degradation | Pretends full module loaded |

For each manual run, record: source commit, input, actual answer, pass/fail,
and first failed owner. Preserve approved baselines before any taste changes.
