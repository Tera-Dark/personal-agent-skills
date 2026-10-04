# P11 Failure Degradation — Acceptance Suite

## P11-01 — global fail-closed default

`harness.json.failure_policy.default_mode` is `fail_closed`.

## P11-02 — standalone module failure

When a standalone module cannot be fetched, enter `card-only`, never reconstruct its content from model memory, and allow unrelated already-loaded modules to continue.

## P11-03 — pipeline-pack failure

When a selected pipeline pack cannot be fetched, enter `pipeline-unavailable`. Do not claim internal stages are loaded and do not jump directly to a model adapter that depends on those stages.

## P11-04 — Anima Tag Index failure

When the Anima 1.0 tag index is unavailable, enter `tag-index-unavailable`; affected anchors remain `unverified`, are excluded from `hard_tags`, and their meaning is routed to Natural Language.

## P11-05 — no fuzzy rescue

Under Tag Index degradation, fuzzy matching, semantic similarity, search-engine suggestions, candidate ranking, and remembered tags remain forbidden as verification sources.

## P11-06 — scoped degradation

Tag Index failure must not erase or redesign the creative blueprint. Pipeline-pack failure blocks model-specific compilation but does not invalidate already-established design decisions.

## P11-07 — truthful loaded state

A failed source is never represented as loaded. A degraded card must be visibly distinguishable from full module content.

## P11-08 — no silent stage skipping

Missing upstream Anima stages cannot be replaced by a direct `anima-prompt-compiler` call.

## P11-09 — generated policy

The generated `bundle/HARNESS.md` exposes the same failure states and labels declared in `harness.json`.

## P11-10 — validator enforcement

`validate_skills.py` rejects a malformed or unsafe failure policy, including a non-fail-closed default or Tag Index degradation that permits hard tags/fuzzy promotion.

## P11 Exit Criteria

- [ ] All three failure scopes have explicit states.
- [ ] No failure path authorizes memory substitution.
- [ ] Tag Index failure degrades only affected tags.
- [ ] Pipeline failure cannot bypass missing stages.
- [ ] Generated runtime exposes the configured policy.
- [ ] Validator enforces the safety invariants.