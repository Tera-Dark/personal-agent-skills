# P6 Anima Prompt Compressor — Acceptance Suite

## P6-01 — deletion test

Any retained element must answer yes to:

> If deleted, would the intended image materially change?

Otherwise remove it.

## P6-02 — hard budget

Default targets:

- avatar / half-body: 18–32 words
- full-body / character / outfit: 28–50 words
- simple illustration scene: 35–60 words
- complex narrative / multi-subject: 50–75 words

These are upper targets, not fill quotas.

## P6-03 — one-sentence NL

Simple character, outfit and scene prompts use one compact NL sentence by default. Complex interaction may use two.

## P6-04 — verified does not mean retained

A verified support tag that does not materially change the blueprint is omitted.

## P6-05 — identity protection

Character/series identity, subject count and locked appearance cannot be deleted to satisfy the budget.

## P6-06 — silhouette protection

A garment relation that defines the silhouette survives compression even when secondary clothing details are deleted.

## P6-07 — asymmetry protection

If left/right asymmetry is a locked design fact, it survives. Generic wording cannot replace the explicit relation.

## P6-08 — punctum protection

One deliberate visual punctum survives. Secondary puncta may be removed.

## P6-09 — redundancy

Repeated Tag + NL statements of the same concept collapse to one representation.

## P6-10 — low-impact cleanup

Generic mood adjectives, decorative background nouns, repeated materials, extra lighting adjectives and explanatory prose are removed.

## P6-11 — negative restraint

Generic negative padding is removed unless tied to a known failure, user exclusion, or risky composition.

## P6-12 — no redesign

Compression cannot alter the creative blueprint or invent substitutes for deleted details.

## P6-13 — stop early

If a prompt already expresses the locked blueprint below the target, do not add words merely to approach the budget.

## P6-14 — pipeline boundary

Accepted order:

Gate → Classifier → Skeleton → Compressor → Serializer → Compiler

The compressor cannot verify tags, escape syntax, or redesign the concept.

## P6 Exit Criteria

- [ ] Minimal-sufficient principle is enforced.
- [ ] Default targets are substantially shorter than the old 50–120 word ranges.
- [ ] The prompt does not grow to fill a quota.
- [ ] High-value facts survive.
- [ ] Low-impact prose is consistently removed.
- [ ] One-sentence NL is the default.
- [ ] No aesthetic/design drift.