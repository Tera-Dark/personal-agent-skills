# Skill Specification

> Merged from the previous `skill-specification.md` + `skill-development-guide.md` and aligned with the open Agent Skills spec (agentskills.io/specification), v2.0.0.

## Directory

```
<skill-name>/
├── SKILL.md            required
├── references/         optional — knowledge loaded on demand
├── scripts/            optional
└── assets/             optional
```

Skills live under a numbered layer folder (`00_core/` … `06_extensions/`, listed in `harness.json → layers`). The layer folder is organizational only; the skill's identity is its own directory name. A `SKILL.md` outside the declared layers is a validation error.

## Frontmatter

```yaml
---
name: skill-name                 # required. MUST equal the directory name. [a-z0-9] and single hyphens, ≤ 64 chars.
description: What it does. Use when …   # required. ≤ 1024 chars. What + when + trigger keywords (Chinese triggers welcome). No < >.
license: MIT                     # optional
metadata:                        # string → string only
  author: Tera-Dark
  version: "0.1.0"
  layer: "02_creation"           # required here: must equal the layer folder
  load: "on-demand"              # required here: always | on-demand  (always also needs an entry in harness.json)
  status: "active"               # required here: active | placeholder | planned
  triggers: "关键词, keyword"     # recommended: comma-separated, goes into the module index
---
```

Do **not** use non-spec top-level keys (`priority`, `trigger`, `input`, `output`, `dependencies`). Runtimes ignore them at best; put such information under `metadata:` or in the body.

`scripts/validate_skills.py` enforces all of the above; `--check-bundle` additionally fails if `bundle/` is stale. CI runs both.

## How a skill becomes loadable

`scripts/build.py` turns each skill into one file, `bundle/modules/<name>.md` = SKILL.md body + every reference (in the order the SKILL.md's References section lists them; unlisted `references/*.md` are appended alphabetically). Skills with `load: always` are additionally embedded in `bundle/HARNESS.md` — but only the files listed for them in `harness.json → always_on`, so keep those lists tight (`core_budget_tokens`).

Consequences for authors:

- A reference that is not mentioned in SKILL.md still ships, but say what it is for in the References section anyway — the model reads that section to decide whether to scroll.
- Headings inside SKILL.md and references are demoted one/two levels when bundled; start your file at `#` and don't rely on absolute heading depth.
- Frontmatter is stripped in the bundle and replaced by a generated header (layer · load · status · version · source URL · description).
- `status: planned` skills are listed in the index but not embedded in HARNESS-FULL and have no fetch URL.

Template: `kernel/templates/SKILL.template.md` and `kernel/templates/reference.template.md`. Chat-driven additions follow `kernel/EXTENSION-PROTOCOL.md`.

## Body

Keep SKILL.md under ~5000 tokens. It should contain **process**, not **knowledge**:

1. 定位 — what it is, what it receives, what it emits, what it explicitly does not do
2. 硬规则 — MUST / MUST NOT
3. 执行流程 — ordered steps with dependencies between them
4. 输出契约 — exact output shape
5. 自检 — checklist before returning
6. References — one line per file, what it's for

Knowledge (vocabulary, patterns, model parameters, experiment logs, examples) goes in `references/`.

## Design-layer rules specific to this hub

- **Taste lives only in `personal-identity-profile`.** New skills must not add "personal aesthetic" sections. Reference the profile by name.
- **Adapters translate, they do not design.** An adapter's SKILL.md must include the input check ("is this a blueprint?") and the route-back rule.
- **Prefer methods over forms.** An output contract that is a list of empty labels (`Identity: / Costume: / Mood:`) invites slot-filling. Write the contract as dependent decisions, and require the "what was cut" and "rejected directions" lines for anything creative.
- **Prefer replacement moves over prohibitions.** "Avoid X" must be paired with "do Y instead". See `aesthetic-director-core/references/anti-ai-patterns.md` for the format.
- **Skills reference each other by name**, never by relative path.
- **Examples beat rules.** When adding taste knowledge, add a pair to `taste-calibration-pairs.md` (generic answer vs directed answer + what changed) rather than another bullet list.

## Language

Chinese for reasoning and rules (this is how the owner thinks about taste); English for anything that may end up inside a prompt. Frontmatter `description` in English with Chinese trigger words appended.

## Checklist for a new skill

1. Does an existing skill already own this responsibility? (`docs/skill-registry.md`)
2. Which layer? Does it only depend downward?
3. `name` == directory name; description says what + when.
4. Body is process; knowledge is in `references/`.
5. If it's an adapter: input check + route-back rule present; no taste section.
6. Register it in `docs/skill-registry.md`.
7. `python3 scripts/validate_skills.py` passes; `python3 scripts/build.py` run and `bundle/` committed (or let CI do it on `main`).
8. If it changes the architecture, update `README.md` and `docs/architecture.md`, bump `VERSION`, add a `CHANGELOG.md` entry.
