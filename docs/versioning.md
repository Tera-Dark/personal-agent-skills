# Skill Versioning Guide

## Purpose

Define how this repository evolves while keeping Skill responsibilities stable.

## Where the version lives

`VERSION` (single line) is the harness version. `scripts/build.py` stamps it into `bundle/HARNESS.md`, the handshake line, and `bundle/manifest.json`. Individual skills carry their own `metadata.version`; bump it when that skill's contract changes.

## Version Rules

### Patch (x.y.Z)

- wording fixes, new examples, new reference knowledge, new rows in target-notes
- no contract change; a running session would not notice

### Minor (x.Y.0)

- a new module
- a new section in a module's output contract
- new kernel command
- always-on set changed in `harness.json`

### Major (X.0.0)

- kernel operating loop or non-negotiables changed
- skills moved between layers or renamed (fetch URLs change)
- router behavior changed
- gate contracts changed in a way that can alter module execution
- anything that breaks a custom GPT / Gem that uploaded the previous HARNESS-FULL.md

## New Skill Checklist

See `docs/skill-specification.md` § Checklist. In short: no overlap → isolated directory → `name` == dir → knowledge in `references/` → register in `docs/skill-registry.md` → `scripts/validate_skills.py` passes → README/architecture updated if the architecture changed.

## Taste updates are versioned too

Changes to `personal-identity-profile/references/taste-signature.md` or `design-dislikes.md` are dated entries, never silent edits. Old entries are marked superseded, not deleted — the history of what the owner stopped liking is itself taste data.

## Design Principle

Prefer adding knowledge over adding duplicate Skills.


## Architecture releases

The Aesthetic Gate and Blueprint Gate are architecture-level contracts. Changes to when a creative task is design-ready, which specialist owns a packet, or whether an adapter may execute require a major version bump.
