# P9 Shared Prompt Pipeline Integration — Acceptance Suite

## P9-01 — machine-readable chain

`harness.json` declares the shared target prompt packs:

`visual-prompt-core` → `danbooru-tag-gate` → `anima-renderer`

and

`visual-prompt-core` → `danbooru-tag-gate` → `nai5-renderer`.

## P9-02 — one-fetch Web-first execution

Generated target pipeline packs contain the three declared stages and are exposed as one runtime fetch each.

## P9-03 — no stage skipping

The router must not route directly from Blueprint Gate to a model renderer without the shared Prompt Core and Danbooru Gate.

## P9-04 — Prompt Core precedes tag verification

Unverified or missing tags cannot reach Classifier as verified hard tags.

## P9-05 — Shared packet formation precedes target serialization

Protection audits the structured prompt packet produced by the Skeleton; it does not replace Skeleton responsibilities.

## P9-06 — Design Lock and compression remain shared responsibilities before renderer emission

Compression may shorten only after protected design decisions are locked.

## P9-07 — Compression precedes target serialization

Serializer sees the final surviving canonical tags, not an earlier uncompressed packet.

## P9-08 — Renderer-specific serialization is the final target boundary

Compiler receives serialized tag syntax and cannot invent escaping rules.

## P9-09 — fail closed

Missing/unverified tags, missing upstream stage state, design drift, or unavailable pack content must not silently fall back to model memory.

## P9-10 — no redundant fetches

After a target pipeline pack is loaded, its constituent modules are treated as loaded; individual module refetch is reserved for explicit `/reload`.

## P9-11 — validator coverage

`validate_skills.py` rejects unknown, duplicate, planned, or always-on skills inside a pipeline pack.

## P9 Exit Criteria

- [ ] Anima and NAI5 have shared, ordered machine-readable prompt pipelines.
- [ ] Web-first Anima fits the per-turn fetch budget.
- [ ] Generated pipeline pack is part of the normal build/check path.
- [ ] Router and Kernel agree on the same execution contract.
- [ ] Validator fails closed on malformed pack definitions.
- [ ] No module stage can be silently skipped.