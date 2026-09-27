# Changelog

All notable changes to the `personal-agent-skills` repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-09-27

Architecture release. Fixes the two problems found in review: (1) the taste layer the whole architecture depended on was empty, so outputs fell through to slot-filling; (2) three generations of skills coexisted (`skills/`, root `anima-prompt-compiler/`, numbered `0X_` layers) with drifting duplicates.

### Added
- **`aesthetic-director-core/SKILL.md`** — the creative direction layer now exists. Nine creative moves (find the obsession, plant a contradiction, pick from the tail, build causality, choose the moment, subtract, keep one strange thing, uneven density, name the punctum) producing a Creative Brief that must include rejected directions and what was cut.
- **`aesthetic-director-core/references/creative-moves.md`** — per-move: what it solves, what the AI does by default, what a designer does, concrete technique, test.
- **`aesthetic-director-core/references/taste-calibration-pairs.md`** — six paired examples (generic answer vs directed answer + what changed) covering open OC, "make it higher-end", story illustration, white-plate, reference-to-original, and a "too plain" feedback round. Written inside the owner's signature.
- **`aesthetic-director-core/references/feedback-diagnosis.md`** — one system-wide table: user phrase → failing layer → fix → what not to do. Replaces three partial copies that lived in the Anima adapter.
- **`personal-identity-profile/references/taste-signature.md`** — names the taste ("精致的基底上，一处怪，一点危险") with evidence, Tier A/B/C/D, boundaries, and an approved-samples log. Single source of truth for preferences.
- **`scripts/validate_skills.py`** — checks name==directory, description present/length, duplicate names, non-spec frontmatter keys, missing reference files, registry drift.
- **`scripts/install.sh`** — symlinks every skill into `~/.claude/skills` (or any target) so the numbered layout stays discoverable.
- **Design-layer regression cases** (Design-01…05) in `tests/test-suite.md`.
- **Adapter input check**: both adapters now verify they received a blueprint (thesis with verb, silhouette, four garment layers, one punctum, locked facts) and route back otherwise.

### Changed
- **`character-design-engine`** rewritten from a 13-slot form into an 11-step method with dependent decisions, a subtraction pass, and mandatory "what was cut" / "rejected directions" lines.
- **`illustration-direction`** rewritten: moment first, physical light sources, one background layer, atmosphere preset at most one, plate-mode rules.
- **`anima-prompt-compiler`** moved into `02_creation/` and trimmed to a pure adapter (format contract, length budgets, V1/V2 modes, model profiles, troubleshooting). Its model-agnostic knowledge was re-homed:
  - `anima-oc-design-system.md` → `character-design-engine/references/oc-design-system.md`
  - `anima-fashion-patterns.md` → `character-design-engine/references/garment-lexicon.md`
  - `anima-composition-patterns.md` → `illustration-direction/references/composition-patterns.md`
  - `anima-aesthetic-deai.md` → `illustration-direction/references/atmosphere-presets.md`
  - `anima-human-aesthetic-calibration.md` → `aesthetic-director-core/references/design-calibration-examples.md`
  - `anima-user-aesthetic-profile.md` → merged into `personal-identity-profile/references/taste-signature.md`
- **`nai5-community-prompt-engineering`** merged from the two duplicate copies; kept the fuller references; removed its private "Personal Aesthetic Rules" section; added a blueprint→tag translation section (density as tag count, punctum color appears once, cut items must not return as tags) and an explicit note that NAI quality tags are a legitimate model-level exception.
- **`image-reverse-analysis`** consolidated from three duplicate reverse-analysis flows; now distinguishes faithful reproduction vs structural extraction for original work.
- **`evaluation-loop`** moved to `05_evaluation/evaluation-loop/` (name must match directory); now carries the six-dimension rubric plus a design-layer read.
- **`creative-skill-router`** updated: pipeline table, "is the concept already designed?" test, the rule that adapters only receive blueprints.
- **`anti-ai-patterns.md`** reformatted to pattern → cause → replacement move (prohibitions alone leave the model with no alternative action).
- **`emotional-design.md`** expanded: emotion as evidence (body + object + trace of time), expression handling, narrative residue.
- **`workflow-style.md`** gained a "Creative Presentation Voice" section (lead with the direction, state rejections and cuts, no theory, no empty praise, end with one concrete branch).
- **Frontmatter** normalized across all skills to the Agent Skills spec: `name` == directory, real `description` with what/when/triggers, `priority` moved under `metadata`.
- **Docs** consolidated: `architecture.md` absorbs `creative-system-overview.md`; `skill-specification.md` absorbs `skill-development-guide.md`; `skill-registry.md` rewritten with status column and a removed-items table; `README.md` rewritten to match the tree.
- `04_tools/*` marked `status: placeholder` in metadata and body.

### Removed
- `skills/` (legacy `creative-prompt-router`, `nai5-prompt-engineering`) — duplicates.
- `02_creation/anima-prompt-engineering/` — 7-line stub shadowing the real compiler.
- `docs/tera-aesthetic-profile.md`, `docs/project-map.md`, `docs/creative-system-overview.md`, `docs/skill-development-guide.md` — merged elsewhere.
- `04_tools/tool-system-map.md`, thin `character-framework.md`, `costume-design.md`, `composition.md` — superseded by re-homed references.

### Migration
- If you symlinked `anima-prompt-compiler` from the repo root, re-point it to `02_creation/anima-prompt-compiler` (or run `scripts/install.sh`).
- If any external prompt or note referenced `nai5-prompt-engineering` or `creative-prompt-router`, use `nai5-community-prompt-engineering` / `creative-skill-router`.

---

## [1.3.0] - 2026-09-17

### Added
- **Dedicated Provenance Separation**: Disentangled official facts from engineering guidance in `anima-model-profiles.md`. Added explicit Hugging Face model card URL for `Source-01`, introduced `Source-02 (Compatibility Guidance)`, and labeled Clip Skip as `[Compatibility Guidance]`.
- **Key Fact Lock Constraint for V2**: Explicitly mandated in `SKILL.md` that V2 Enhanced Prompt MUST NOT modify core facts established in V1 (hair, eyes, core clothing style, specified pose) unless explicitly designated as optional creative variants.
- **Uncertainty Handling Protocol**: Added a 4-step diagnostic protocol in `anima-troubleshooting.md` for ambiguous artifacts (avoid hasty claims, identify top 2 causes, apply least invasive test, record separately).
- **Manual Evaluation Rubric in Test Suite**: Enhanced `tests/test-suite.md` with a standardized 6-dimension evaluation rubric (Identity Preservation, Outfit Binding, Spatial Clarity, Unrequested Additions, V1/V2 Fact Consistency, Output Contract) and per-case evaluation record templates.

### Changed
- **Softened Empirical Diagnostics**: Reframed background length ratio (40%) in troubleshooting as a rough investigation signal rather than a rigid universal threshold.
- **Prompt Length Guideline Clarification**: Clarified in `SKILL.md` that length budget ranges serve solely to help AI structure information density, not as rigid pass/fail criteria.

---

## [1.2.0] - 2026-09-17

### Added
- **Provenance & Sources Tracking**: Added a dedicated Source tracking section in `anima-model-profiles.md` with explicit URL/Context, verified dates, and scope to eliminate unverified "Official" assertions.
- **Systematic Diagnostic Flow**: Upgraded `anima-troubleshooting.md` into a 4-step diagnostic flow with structured catalog entries (Symptom, Root Cause, First-order Check, Minimal Remediation, Anti-patterns, Verification Criteria).
- **Core Test Suite**: Created `tests/test-suite.md` featuring 8 comprehensive benchmark cases covering identity lock, 4-tier layering, multi-scale presentation layouts, white backdrop edge retention, multi-character isolation, and word count flexibility.

### Changed
- **De-dogmatized Phrasing Standards**: Enforced 3-tier calibrated phrasing ("Officially documented", "Commonly observed across community workflows", "Observed under tested conditions") to eliminate exaggerated claims.
- **Redefined V1 Faithful Contract**: Revised V1 definition from rigid "strict 1:1" to faithful preservation of explicit intent while allowing necessary language conversion, disambiguation, and structured layout without unsolicited aesthetic upgrades.
- **Flexible Planning Targets for Prompt Length**: Replaced rigid word count limits with dynamic planning budgets prioritizing information density and spatial clarity over arbitrary metrics.
- **Experiment Log Metadata**: Enhanced test logs with `Replication Count` and `Generalizability` boundaries.

---

## [1.1.0] - 2026-09-17

### Added
- **Evidence Levels System**: Introduced 3-tier evidence classification (`Official`, `Community Practice`, `Personal Experiment`) across model profiles to prevent confusing empirical observations with universal laws.
- **Anima Troubleshooting Guide**: Created `references/anima-troubleshooting.md` covering anatomy breakdown, garment color bleeding, background dominance, and multi-character attribute cross-contamination.
- **Output Modes (V1/V2 Contract)**: Formally added `Direct Mode`, `Standard Mode` (V1 Faithful + V2 Enhanced + Enhancement Notes), and `Deep Mode` in `anima-prompt-compiler/SKILL.md`.
- **Prompt Length Strategy**: Defined word budgets for Avatar (30-50), Character/Fashion (50-80), Multi-layer layout (70-100), and Narrative scene (80-120).
- **Multi-Subject Isolation & Ambiguity Handling**: Explicit rules for isolating multiple characters and preserving open possibilities for unconfirmed details.

### Changed
- **Parameter Corrections in Model Profiles**:
  - Adjusted default CFG recommendation for Anima Base/Aesthetic from 5.0-7.0 to 4.0-5.0 to align with official recommendations.
  - Clarified that Turbo steps (4-8) apply to specific distilled models rather than all Turbo/Lightning variants.
  - Replaced hardcoded "Clip Skip 2" with standard `Text Encoder and Frontend Compatibility` guidelines, accommodating Qwen and modern dual-encoder setups.
  - Rewrote personal experiment logs to follow strict structured metadata format.
- **Refined Positive-Only Rule**: Transitioned from strict negative banning to pragmatic `Positive-First Output`, allowing graceful affirmative constraint translation and explaining tradeoffs.
- **README Platform Compatibility**: Tempered claims of universal automatic platform compatibility to acknowledge variations across AI client discovery mechanisms.
- **Illustrative Notes**: Added non-prescriptive disclaimers to prompt examples in `README.md`.

---

## [1.0.0] - 2026-09-17

### Added
- Initial release of the `personal-agent-skills` repository.
- Core `anima-prompt-compiler` skill with modular reference files:
  - `anima-model-profiles.md`
  - `anima-fashion-patterns.md`
  - `anima-composition-patterns.md`
  - `anima-aesthetic-deai.md`
- Multi-AI platform setup instructions and skill specification document.
