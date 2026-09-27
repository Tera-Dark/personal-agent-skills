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

1. Confirm no existing Skill already owns the responsibility.
2. Create an isolated directory.
3. Add SKILL.md with clear boundaries.
4. Put detailed knowledge in references/.
5. Register the Skill in docs/skill-registry.md.
6. Update README when architecture changes.

## Design Principle

Prefer adding knowledge over adding duplicate Skills.
