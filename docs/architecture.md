# Architecture

> Merged from the previous `architecture.md` + `creative-system-overview.md` (v2.0.0).

## Philosophy

A prompt is not the design. A prompt is the language used to communicate a **decision** to a model.

Generic ("AI-flavored") output is not a rendering problem; it is a **decision-making** problem: the model fills every slot with the most probable value. So the system's job is to force a human decision path *before* any prompt exists — pick one obsession, reject alternatives, build causality, subtract, keep one strange thing — and only then translate.

## Layers

```
User Request
    │
    ▼
01_router · creative-skill-router          classify intent, assemble pipeline
    │
    ▼
00_core · personal-identity-profile        WHO is this for  → taste signature, dislikes, voice
    │
    ▼
00_core · aesthetic-director-core          WHY / WHAT ONE IDEA → Creative Brief (thesis, contradiction,
    │                                        silhouette strategy, causality, moment, density map,
    │                                        punctum, one strange thing, what was cut, what was rejected)
    ▼
02_creation · character-design-engine      WHAT exactly → model-agnostic blueprint
              illustration-direction
    │
    ▼
02_creation · anima-prompt-compiler        HOW this model hears it → translate only
              nai5-community-prompt-engineering
    │
    ▼
05_evaluation · evaluation-loop            WHICH LAYER failed → single-variable fix, back to that layer
```

Side entrances:
- `03_analysis/image-reverse-analysis` — reference image → structure → director (original) or adapter (faithful)
- `03_analysis/prompt-analysis` — existing prompt → weakest layer → fix or route back
- `04_tools/*` — technical execution (placeholders for now)

## Priority when things conflict

```
explicit current-turn request
  > locked character / reference facts
  > latest explicit negative feedback
  > taste signature (Tier A)
  > taste tendencies (Tier B)
  > model syntax habits
  > raw keywords
```

A technically correct prompt that violates the Brief is wrong.

## Invariants

1. **Taste has one home.** Only `personal-identity-profile` stores user preferences. Adapters do not keep "personal aesthetic rules" sections.
2. **Adapters never design.** They check whether the input is a blueprint (has a thesis with a verb, a silhouette, four garment layers, one punctum, locked facts). If not, they route back.
3. **Design knowledge is model-agnostic and lives in 00_core / 02_creation design skills.** In v1 the Anima adapter held the OC design system, garment lexicon, composition protocols and the feedback rules; those were only reachable when the user asked for Anima. They now serve every adapter.
4. **Feedback is evidence about a layer, not permission to add.** `evaluation-loop` + `feedback-diagnosis.md` decide which layer owns the fix.
5. **Skills reference each other by name.** Never by relative path — they may be installed separately.

## Why the numbered folders

`00_core/ … 05_evaluation/` make the dependency direction visible in the file tree. Agent runtimes usually discover skills one directory deep, so `scripts/install.sh` flattens the layout with symlinks into `~/.claude/skills/` (or any target). `name` in every SKILL.md equals its immediate directory name, as the spec requires.

## What "human" means operationally

The system does not try to make output "feel human" with adjectives. It enforces the observable traits of human design decisions:

| Trait | Enforced by |
|---|---|
| one center, unequal attention | M1 obsession, M8 density map |
| choices from the tail, not the mode | M3 |
| things cause other things | M4 causality |
| a moment, not a state | M5 |
| completeness by subtraction | M6, "what was cut" line |
| one deliberate imperfection | M7 |
| visible rejection of alternatives | "rejected directions" line in every Brief |
| a named taste, not a market segment | `taste-signature.md` |
| examples, not just rules | `taste-calibration-pairs.md` |
