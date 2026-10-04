# Architecture

> v3.0.0 hardens the creative pipeline with explicit Aesthetic and Blueprint Gates.

> v2.1.0: a kernel and a build step were added on top of the v2.0 layered skills, turning the repository into a harness that a chat model can load from one URL.

## Two views of the same repository

```
SOURCE (what you edit)                        DISTRIBUTION (what a model loads)
─────────────────────────                     ────────────────────────────────────
harness.json  VERSION                         bundle/HARNESS.md
kernel/KERNEL.md                 build.py       = kernel (placeholders filled)
00_core/<skill>/SKILL.md      ───────────►      + module index (from frontmatter)
   references/*.md                              + always-on modules, full text
01_router/ … 06_extensions/                   bundle/modules/<name>.md   (one file per module: SKILL.md + references)
                                              bundle/HARNESS-FULL.md     (everything)
                                              bundle/manifest.json       (machine-readable)
                                              docs/skill-registry.md     (human-readable, generated)
```

Chat models (ChatGPT, Gemini, Claude) have no skill-discovery mechanism; a URL fetch returns one document. So the unit of distribution is a **single compiled file**, and the kernel inside it tells the model how to pull more single files on demand. Skill-discovering runtimes (Claude Code, Codex) can still use the sources directly via `scripts/install.sh`.

## Kernel

`kernel/KERNEL.md` is not a skill; it is the operating contract every session runs under:

| Section | What it fixes |
|---|---|
| Handshake | The model's first reply is a one-line version probe, not a summary of the repo |
| Operating loop | READ → ROUTE → LOAD → THINK → EXECUTE → VERIFY → DELIVER, every turn |
| Non-negotiables | adapters never design · taste has one home · no fabricated model facts · feedback is evidence · prompts in English · never echo harness text · never pretend |
| Loading protocol | two tiers (always-on embedded / on-demand fetched), ≤3 loads per turn, cache, graceful degradation to module cards with `[card-only]` |
| Module index | generated from every SKILL.md's frontmatter: triggers, status, token cost, fetch URL, card |
| Voice | the owner's presentation rules, binding |
| Session State | a ≤12-line block tracking target, mode, locked facts, approved dimensions, rejected items, prompt version, loaded modules |
| Vision protocol | `seen:` before anything else; observed vs inferred; route reference vs result vs screenshot |
| Commands | `/state /modules /reload /mode /model /new-module /version /help` |
| Extension protocol | how a new module is drafted in chat and goes live through CI |
| Failure modes | the specific ways this model tends to drift, named |

## Philosophy

A prompt is not the design. A prompt is the language used to communicate a **decision** to a model.

Generic ("AI-flavored") output is not a rendering problem; it is a **decision-making** problem: the model fills every slot with the most probable value. So the system's job is to force a human decision path *before* any prompt exists — pick one obsession, reject alternatives, build causality, subtract, keep one strange thing — and only then translate.

## Layers

```
User Request
    │
    ▼
01_router · creative-skill-router          classify + choose pipeline
    │
    ▼
00_core · personal-identity-profile        WHO is this for
    │
    ▼
00_core · aesthetic-director-core          AESTHETIC GATE (FULL / AUDIT / ESCALATE)
    │
    ▼
02_creation · character-design-engine      CHARACTER BLUEPRINT
              illustration-direction       ILLUSTRATION BLUEPRINT
    │
    ▼
              BLUEPRINT GATE
    │
    ├───────────────┬──────────────────┐
    ▼               ▼                  ▼
 Anima           NAI5              Generic
 Tag + NL       Community Tags       Natural NL
    │               │                  │
    └───────────────┴──────────────────┘
                    ▼
05_evaluation · evaluation-loop            diagnose layer → fix one variable → Blueprint Gate
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


## Gate contracts

**Aesthetic Gate:** every creative task passes FULL or AUDIT. FULL makes design decisions; AUDIT validates supplied decisions without rewriting locked facts; missing core decisions escalate to FULL.

**Blueprint Gate:** adapters run only after a type-appropriate blueprint or verified finished-design packet passes. Character and illustration packets have different required fields.

**Adapter boundary:** Anima and NAI5 have model-specific prompt skeletons, but no authority to change the concept.

**Generated distribution:** bundle/ and docs/skill-registry.md are generated from source. VERSION is the harness version; module versions are independent contract versions.
