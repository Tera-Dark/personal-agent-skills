# P9 Anima Pipeline Integration — Acceptance Suite

## P9-01 — machine-readable chain

`harness.json` declares `pipeline.pipeline_packs.anima` with exactly this order:

`anima-tag-gate` → `anima-tag-classifier` → `anima-prompt-skeleton` → `anima-aesthetic-protection` → `anima-prompt-compressor` → `anima-tag-serializer` → `anima-prompt-compiler`.

## P9-02 — one-fetch Web-first execution

The generated `bundle/pipelines/anima.md` contains the seven declared stages and is exposed as one runtime fetch.

## P9-03 — no stage skipping

The router must not route directly from Blueprint Gate to Compiler for Anima.

## P9-04 — Gate precedes classification

Unverified or missing tags cannot reach Classifier as verified hard tags.

## P9-05 — Skeleton precedes protection

Protection audits the structured prompt packet produced by the Skeleton; it does not replace Skeleton responsibilities.

## P9-06 — Protection precedes compression

Compression may shorten only after protected design decisions are locked.

## P9-07 — Compression precedes serialization

Serializer sees the final surviving canonical tags, not an earlier uncompressed packet.

## P9-08 — Serialization precedes adapter emission

Compiler receives serialized tag syntax and cannot invent escaping rules.

## P9-09 — fail closed

Missing/unverified tags, missing upstream stage state, design drift, or unavailable pack content must not silently fall back to model memory.

## P9-10 — no redundant fetches

After `pipeline_packs.anima` is loaded, its constituent modules are treated as loaded; individual module refetch is reserved for explicit `/reload`.

## P9-11 — validator coverage

`validate_skills.py` rejects unknown, duplicate, planned, or always-on skills inside a pipeline pack.

## P9 Exit Criteria

- [ ] Anima has one declared, ordered machine-readable pipeline.
- [ ] Web-first Anima fits the per-turn fetch budget.
- [ ] Generated pipeline pack is part of the normal build/check path.
- [ ] Router and Kernel agree on the same execution contract.
- [ ] Validator fails closed on malformed pack definitions.
- [ ] No module stage can be silently skipped.