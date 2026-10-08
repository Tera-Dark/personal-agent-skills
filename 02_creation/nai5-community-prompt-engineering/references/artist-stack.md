# NAI5 Artist Stack Engineering

## Purpose

Guide weighted artist mixing for NovelAI V5 community prompts.

Default syntax:

1.0::artist:name::

## NAI5 weight semantics

NovelAI's numerical emphasis uses 1.0 as the baseline:
- >1.0 strengthens
- 0.0–1.0 weakens
- negative values are reserved for targeted suppression/removal/inversion

So 0.8 is **not** a high-strength artist weight; it is a weakened emphasis. For a strong primary artist, start around 1.0 and only move above 1.0 when stronger influence is actually needed.

## Principles

For this personal workflow, the current random experiment mode is authoritative: 4–8 artists total, 1–2 master anchors + 2–6 randomly selected assistants, each 0.3–1.2, with at least one artist >1.0. The conservative single-primary recipe remains only a generic fallback when no personal experiment rule is specified.

Artist tags are not decoration. They influence the visual prior of the generation:
- line quality
- color language
- composition
- character design feeling

Avoid blindly stacking artists.

### Default random-mix habit

Current personal experiment mode:

- Roll a total of **4–8 artists**.
- Lock **1–2 master anchors** first.
- Randomly fill **2–6 assistants** from the eligible exploration / personal pool.
- Every artist weight must be **0.3–1.2**.
- At least **one master or other artist must be >1.0**.
- Keep masters visibly stronger than the low-end assistants unless a specific test is intended to break that hierarchy.
- Append **artist collaboration** by default for this multi-artist experiment mode.
- Exclude yellow-pool artists from the main roll.
- Avoid duplicate artists within one stack.
- Across sequential experiments, minimize short-cycle repeats while preserving high-value combinations for re-tests.
- When visual languages strongly conflict, reduce artist count rather than adding more weights.
- If the result becomes noisy, dirty, or stylistically torn, inspect artist count and weight conflict before adding prompt content.

### Preserve user syntax

**Keep the artist: namespace. Do not strip it.**

If the user's pool contains escaped tags, wildcards, parentheses, suffixes, or unusual syntax, preserve them exactly unless the user explicitly asks for normalization. Do not silently rewrite a tag into a different artist identifier.

Examples that should remain untouched:

artist:rei(sanbonzakura)
artist:sencha_(senchat)
artist:mr.owlish

If an entry contains an obvious malformed or ambiguous trailing weight/value, do not guess its intended meaning and push it into a high-weight stack. Prefer skipping it or using it only after the user clarifies.

The special entry vlfdus 0 is treated as ambiguous unless the user confirms it; do not silently convert it into a guessed artist name.

### Personal blacklist gate

Before emitting any new artist stack, exclude every artist token whose **final character is a digit**. This rule overrides random selection and combination design unless the user explicitly overrides it. Historical-only records containing such artists must never be emitted into new prompts.

### Yellow pool gate

The main artist roll must exclude all artists currently classified by the user as yellow-pool. Current yellow-pool records:
- artist:qiandaiyiyu — 7/10
- artist:mimonel — 7/10

Do not recommend, explore, or randomly select these for the mainstream pool unless the user explicitly requests the yellow pool.

A good stack balances the blueprint's needs across:
- character design
- rendering
- lighting
- illustration composition

The stack supports the blueprint; it does not replace character or composition design.

For the current mainstream 4–8 artist experiment mode, artist collaboration is enabled by default.

Treat it as a community experimental control tag, not an official guaranteed fusion mechanism. When debugging, A/B test the same seed and prompt with and without it rather than assuming it must help.

Optional suppression when a clean separation is desired:
-1::artist collaboration::

## Practical templates

### Strong primary + light blend

1.05::artist:primary::
0.55::artist:secondary::
0.5::artist:third::
0.4::artist:fourth::

### Conservative portrait

1.0::artist:primary::
0.55::artist:secondary::
0.45::artist:third::

The exact values are starting points, not guarantees. Tune one variable at a time.


## Cold-dark pseudo-painterly specialist

When the prompt needs a gray, cold, bleak, rough-painterly or post-apocalyptic visual language, `artist:huke` is a valid external experimental candidate. Its current indexed artist tag is verified and has substantial coverage; use it as a contrast/rendering component rather than assuming it is a permanent personal favorite. citeturn659470search0turn659470search1
