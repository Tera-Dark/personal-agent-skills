# Skill Versioning Guide

## Purpose

Define how this repository evolves while keeping Skill responsibilities stable.

## Version Rules

### Minor changes

Use when:

- adding references
- improving prompts or examples
- extending supported workflows

No architecture change.

### Major changes

Use when:

- changing Skill responsibilities
- moving modules between layers
- changing Router behavior
- breaking existing workflows

## New Skill Checklist

See `docs/skill-specification.md` § Checklist. In short: no overlap → isolated directory → `name` == dir → knowledge in `references/` → register in `docs/skill-registry.md` → `scripts/validate_skills.py` passes → README/architecture updated if the architecture changed.

## Taste updates are versioned too

Changes to `personal-identity-profile/references/taste-signature.md` or `design-dislikes.md` are dated entries, never silent edits. Old entries are marked superseded, not deleted — the history of what the owner stopped liking is itself taste data.

## Design Principle

Prefer adding knowledge over adding duplicate Skills.
