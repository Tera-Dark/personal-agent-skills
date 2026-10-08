## [4.0.0] - 2026-10-08

### Shared visual prompt architecture
- Replaced parallel Anima / NAI5 prompt-planning responsibilities with a shared `visual-prompt-core`.
- Added shared `danbooru-tag-gate` for exact / alias / missing verification.
- Added thin `anima-renderer` and `nai5-renderer` model-specific endpoints.
- Moved design, prompt, analysis, tools, evaluation and extension skills into explicit v4 layers.
- Reduced the always-on runtime to persistent identity + routing policy.
- Removed duplicated workflow voice and duplicated NAI5 personal artist policy from non-owner modules.
- Preserved Anima and NAI5 regression material under the new owners instead of deleting the knowledge.

## [3.11.0] - 2026-10-06

### High-density small-artist aesthetic calibration
- Added the validated “高密度花哨人物肖像” mode based on the user's domestic small-artist commission reference board.
- Clarified that dense ornament belongs around the character: hair, face, shoulders, chest, hands and costume, rather than being interpreted as a complex scenic background.
- Added dense sweet/ornate OC portrait principles: character nearly fills frame, coordinated ornament clusters, layered costume detail, controlled high-saturation color groups, and collectible commission-illustration logic.
- Added artist:xixizi, artist:luckyia, and artist:bochishiraita to the candidate pool after Danbooru >50-post and domestic-platform evidence checks.
- Preserved the user's current 3–8 artist, 0.3–1.2 random-weight experiment rule and excluded artist:yellowshark601.
## [3.10.0] - 2026-10-06

### Small-artist mixer refinement
- Refined discovery to start from mainland-China Xiaohongshu / Mihuashi / Weibo creator ecosystem, then verify Danbooru tags and post counts.
- Made Danbooru >50 posts a hard candidate-screening threshold for newly discovered artists.
- Added the user-validated trio artist:banbanimi + artist:mido_(mido_chen) + artist:pekopeco as a high-value small-artist combination sample.
- Added these three artists to the active small-artist pool.
- Temporarily replaced the 1-main+3-support mixer with 3–8 artists per experiment and random weights from 0.3–1.2.
- Kept artist:yellowshark601 explicitly excluded.

## [3.9.0] - 2026-10-06

### Small-artist aesthetic calibration
- Added a dedicated “小画师审美模式” to the personal taste layer, distinguishing this female-oriented 2D character ecosystem from generic anime illustration and template-heavy commercial game art.
- Added confirmed calibration samples and explicit boundaries between mainstream少女向 and 2D/OC/亚文化向 branches.
- Added the current NAI5 artist pool, 1主+3辅 mixer contract, weighted hierarchy, Danbooru-first screening preference (preferably >50 posts), and the explicit exclusion of artist:yellowshark601.
- Kept the artist pool as a taste/runtime preference source rather than claiming all tags have equal or permanent stability.

## [3.8.0] - 2026-10-05

### Aesthetic floor
- Added an explicit aesthetic floor: distinctiveness must remain subordinate to proportion, silhouette, color hierarchy and garment construction.
- Clarified that the “one strange thing” is a local tension device, not permission to make the whole design awkward or ugly.
- Added P14 regression coverage for aesthetic floor, removal tests, feedback routing, Modern Key Visual impact, compression and long-term taste boundaries.
- Refined the evaluation loop so “ugly” feedback is diagnosed as a design-layer failure instead of defended as intentional.

## [3.7.0] - 2026-10-05

### Real-task regression
- Added P13 real-task regression coverage for modern gacha key visuals, Y2K/daily fashion, maximalist couture, white-background full-body plates, ice couture, compact Anima compilation, authored illustration, and reference-to-original transfer.
- Added cross-task anti-regression checks for one strange point, one punctum, local density, decorative filler, white-background separation, compression order, adapter translation, and generic-market fallback.
- Kept P13 visual judgment manual: the harness tests creative decisions and prompt translation, while CI checks that the regression matrix and its invariants remain present.

## [3.6.0] - 2026-10-05

### Personal Anima regression
- Added a unified P12 regression matrix covering tag identity, IP/artist scope, appearance/clothing/action classification, composite packets, special syntax, relation-oriented skeleton assembly, compression, aesthetic protection, failure degradation, Web-first loading, and recent real tasks.
- Added scripts/check_personal_anima_regression.py for deterministic offline contract checks.
- CI now runs the P12 contract checker alongside skill validation and bundle integrity checks.
- Live Good Anima alias verification and visual/aesthetic judgment remain explicit manual cases; the machine checker never invents tag evidence or claims to judge image quality automatically.

## [3.5.0] - 2026-10-04

### Failure degradation
- Added a single fail-closed degradation contract in the Kernel and `harness.json`.
- Standalone module failures use `[card-only]` without memory substitution.
- Pipeline-pack failures use `[pipeline-unavailable]` and block unsafe adapter jumps.
- Anima tag-index failures use `[tag-index-unavailable]`, preserving design while routing affected tag meanings to Natural Language.
- Validator checks required failure states and forbids hard-tag/fuzzy promotion during Tag Index degradation.
- Added P11 acceptance coverage.

## [3.4.0] - 2026-10-04

### Bundle build integrity
- Pipeline packs are now first-class generated artifacts in `scripts/build.py`.
- `bundle/pipelines/<name>.md` is generated from `harness.json` and automatically checked for stale/orphan files.
- Kernel pipeline-pack entries are generated from configuration instead of hardcoded routes.
- Manifest output exposes pipeline-pack module lists, fetch cost and generated URLs.
- P10 acceptance tests cover source → bundle → manifest → pipeline pack → registry consistency.

## [3.2.0] - 2026-10-04

Web-first runtime and Anima pipeline hardening release.

### Added
- Dedicated Web-first runtime contract in `kernel/KERNEL.md`.
- Declarative `web_first` entries in `harness.json`.
- Anima P2 exact → alias → missing tag gate.
- Anima P3 tag classifier/filter.
- Anima P4 syntax serializer with the explicit Reverse:1999 serialization rule.
- Anima P5 compact Tag/NL prompt skeleton.
- Anima P6 minimum-sufficient prompt compressor.
- Anima P7 aesthetic protection / design-drift boundary.

### Changed
- Web conversation is now the canonical no-local-runtime execution path.
- Anima prompts default to the smallest sufficient control packet instead of filling a word budget.
- Verified tags are not automatically retained; verification, structure, compression and syntax serialization are separate responsibilities.

### Compatibility
The GitHub repository page remains the discovery surface. `bundle/HARNESS.md` is the web runtime artifact; CI regenerates it from source skills after changes.

## [3.1.0] - 2026-10-04

Taste calibration release. The harness now recognizes a separate Modern Character Key Visual mode based on the owner's latest reference-board calibration.

### Added
- Modern Key Visual grammar: strong silhouette, directional motion, graphic composition, local high-density pockets, material contrast, physical attachment logic, decisive shadows, and human-painted irregularity.
- Explicit anti-patterns for beauty-filter faces, soft-light soup, surface-only hair, accessory wallpaper and atmosphere-as-background.
- Compact prompt budgets for Anima / general image prompts and a concise discipline for NAI5.

### Changed
- personal-identity-profile now distinguishes clean plate, modern key visual and Eastern decorative narrative presentation modes.
- aesthetic-director-core routes modern gacha / commercial key visuals through the new grammar without forcing them into a restrained or soft-light aesthetic.
- illustration-direction adds a Modern Key Visual mode.
- Prompt adapters prioritize event, silhouette, action, material and construction facts over explanatory prose.

# Changelog

## [3.0.0] - 2026-10-04

Architecture hardening release. The harness now treats aesthetics and blueprint readiness as explicit gates instead of informal expectations.

### Added
- Mandatory **Aesthetic Gate** with FULL / AUDIT / ESCALATE modes.
- Type-specific **Blueprint Gate** for character and illustration packets.
- Declarative pipeline contract in `harness.json`, exported through the generated manifest.
- Architecture regression cases for routing, gates, adapter boundaries, prompt skeletons, artist mixing and bundle consistency.

### Changed
- Kernel operating loop now explicitly gates specialist and adapter execution.
- Router now distinguishes unfinished creative requests from already-finished designs.
- Aesthetic Director now has an explicit audit mode rather than forcing a redesign when the user has already made the decisions.
- Character and illustration specialists now expose readiness contracts.
- Anima declares a canonical Tag Lock + Natural-language Relations skeleton.
- NAI5 declares a canonical community weighted-tag skeleton with a dedicated quality layer.
- Evaluation checks design-packet integrity before technical prompt issues.
- Validator checks architecture references and gate contracts.
- Build manifest exposes the declarative pipeline contract.
- CI compiles scripts and validates the generated bundle after rebuild.
- Documentation and tests updated for the new architecture.

### Compatibility
This is a major release because routing and adapter-readiness behavior changed. Reload the harness after upgrading.

All notable changes to the `personal-agent-skills` repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.2.0] - 2026-10-01

Illustration-direction visual design upgrade. This release adds an authored-composition layer based on the owner's recent reference calibration: the image must have a visual thesis, a structural motif, environmental agency, scale rhythm, intentional negative space, and narrative residue before it is translated into a model prompt.

### Added
- **`02_creation/illustration-direction/references/visual-grammar.md`** — a model-agnostic visual grammar covering image thesis, captured moment, visual motifs, environment-character relationships, scale contrast, controlled occlusion, density rhythm, color-mass design, physical light, coherent surrealism, reference calibration, and anti-pattern replacements.

### Changed
- **`02_creation/illustration-direction/SKILL.md`** upgraded from a moment-first composition workflow to a thesis-first authored illustration workflow.
- Added mandatory **画面命题 / visual motif / environment-character relationship / scale strategy / occlusion plan / color-mass strategy / unique strange point** fields to the illustration blueprint.
- Added a thumbnail-read test and a final “remove all decoration” test to prevent generic pretty-background outputs.
- Explicitly separated **illustration** from **plate-style character presentation**: narrative illustrations should not default to a centered, fully visible character over a scenic background.
- Added reference-derived strategies for architectural framing, organic enclosure, extreme environmental scale, and environment-as-story-evidence without imitating a specific artist.

---

## [2.1.0] - 2026-09-28

Harness release. Target use changed from "skills discovered by a coding-agent runtime" to "a chat model (ChatGPT / Gemini / Claude) handed one URL". That needs a kernel, a build step, single-file bundles, and CI — added here.

### Added
- **`kernel/KERNEL.md`** — the operating contract: handshake (a one-line version probe instead of a repo summary), READ→ROUTE→LOAD→THINK→EXECUTE→VERIFY→DELIVER loop, non-negotiables, two-tier module loading with graceful degradation to module cards (`[card-only]`), generated module index, voice, Session State block, vision protocol (`seen:` first, observed vs inferred), commands (`/state /modules /reload /mode /model /new-module /version /help`), extension protocol, named failure modes.
- **`kernel/EXTENSION-PROTOCOL.md`** + **`kernel/templates/`** — how a new capability is drafted in chat (overlap check → layer → complete files with paths → commit → CI) with a SKILL and a reference template.
- **`scripts/build.py`** — compiles sources into `bundle/HARNESS.md` (kernel + index + always-on modules, ≈23k tokens), `bundle/HARNESS-FULL.md` (everything, ≈56k), `bundle/modules/<name>.md` (one fetch per module), `bundle/manifest.json`, and a generated `docs/skill-registry.md`. `--check` reports stale outputs.
- **`scripts/skills_lib.py`** — shared frontmatter parser / discovery / token estimate / heading demotion.
- **`harness.json`** (repo, branch, layers, always-on file lists, handshake, core token budget) and **`VERSION`**.
- **`.github/workflows/harness.yml`** — validates on PRs (fails if bundle is stale); on push to `main` validates, rebuilds and commits `bundle/` back, so modules added via the GitHub web UI or from chat go live without a local toolchain.
- **`02_creation/general-image-prompt-adapter`** — adapter for Midjourney / DALL-E / Imagen / Flux / SDXL / unnamed targets; parameters outside the prompt; every model claim carries an evidence label; `references/target-notes.md` with per-row evidence.
- **`06_extensions/`** — home for chat-added modules that fit no other layer.
- **`AGENTS.md`** — pointer for coding agents; **`docs/usage.md`** — per-platform setup, commands, extension flow, troubleshooting, token budgets.
- **Harness test cases** (Harness-01…08) in `tests/test-suite.md`.

### Changed
- **README** now opens with the AI bootstrap block (fetch `bundle/HARNESS.md`, operate under it, do not summarize, exact fallback line) so pasting the repo URL is enough.
- **Frontmatter** of every skill gained `metadata.load` (always / on-demand), `metadata.status` (active / placeholder / planned), `metadata.triggers`. The validator enforces `layer == folder`, `load`, `status`, always-on consistency with `harness.json`, and rejects skills outside declared layers.
- **Router** routes unknown / other image models to `general-image-prompt-adapter`, extension modules by their own triggers, and non-creative requests to a direct answer; no more hand-maintained trigger list — the index is built from module frontmatter.
- `04_tools/*` status changed from `placeholder` to `planned` (listed, not loadable; answered `[no module]`).
- `docs/skill-registry.md` is now generated. `docs/architecture.md`, `docs/skill-specification.md`, `docs/versioning.md` updated for the kernel, bundling rules, and semver meaning.
- Last release's review moved to `docs/reviews/2026-09-27-v2.0-review.md`.

### Decisions made on the owner's behalf (per request)
- Placeholder tools kept as `planned` rather than deleted — they document intent and cost nothing in the bundle.
- Taste signature sentence kept; it remains the one line the owner should personally edit.
- Kernel written in English (cross-model instruction precision); taste and creative modules stay Chinese; models answer in the owner's language; prompts always English.
- Always-on set = identity (signature, dislikes, voice) + director (moves, diagnosis, pairs) + router + evaluation. ≈23k tokens, under the 40k budget; the calibration pairs stay in because they are the strongest taste carrier.

---

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
- `skills/` (legacy `creative-skill-router`, `nai5-prompt-engineering`) — duplicates.
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


All notable changes to the `personal-agent-skills` repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.2.0] - 2026-10-01

Illustration-direction visual design upgrade. This release adds an authored-composition layer based on the owner's recent reference calibration: the image must have a visual thesis, a structural motif, environmental agency, scale rhythm, intentional negative space, and narrative residue before it is translated into a model prompt.

### Added
- **`02_creation/illustration-direction/references/visual-grammar.md`** — a model-agnostic visual grammar covering image thesis, captured moment, visual motifs, environment-character relationships, scale contrast, controlled occlusion, density rhythm, color-mass design, physical light, coherent surrealism, reference calibration, and anti-pattern replacements.

### Changed
- **`02_creation/illustration-direction/SKILL.md`** upgraded from a moment-first composition workflow to a thesis-first authored illustration workflow.
- Added mandatory **画面命题 / visual motif / environment-character relationship / scale strategy / occlusion plan / color-mass strategy / unique strange point** fields to the illustration blueprint.
- Added a thumbnail-read test and a final “remove all decoration” test to prevent generic pretty-background outputs.
- Explicitly separated **illustration** from **plate-style character presentation**: narrative illustrations should not default to a centered, fully visible character over a scenic background.
- Added reference-derived strategies for architectural framing, organic enclosure, extreme environmental scale, and environment-as-story-evidence without imitating a specific artist.

---

## [2.1.0] - 2026-09-28

Harness release. Target use changed from "skills discovered by a coding-agent runtime" to "a chat model (ChatGPT / Gemini / Claude) handed one URL". That needs a kernel, a build step, single-file bundles, and CI — added here.

### Added
- **`kernel/KERNEL.md`** — the operating contract: handshake (a one-line version probe instead of a repo summary), READ→ROUTE→LOAD→THINK→EXECUTE→VERIFY→DELIVER loop, non-negotiables, two-tier module loading with graceful degradation to module cards (`[card-only]`), generated module index, voice, Session State block, vision protocol (`seen:` first, observed vs inferred), commands (`/state /modules /reload /mode /model /new-module /version /help`), extension protocol, named failure modes.
- **`kernel/EXTENSION-PROTOCOL.md`** + **`kernel/templates/`** — how a new capability is drafted in chat (overlap check → layer → complete files with paths → commit → CI) with a SKILL and a reference template.
- **`scripts/build.py`** — compiles sources into `bundle/HARNESS.md` (kernel + index + always-on modules, ≈23k tokens), `bundle/HARNESS-FULL.md` (everything, ≈56k), `bundle/modules/<name>.md` (one fetch per module), `bundle/manifest.json`, and a generated `docs/skill-registry.md`. `--check` reports stale outputs.
- **`scripts/skills_lib.py`** — shared frontmatter parser / discovery / token estimate / heading demotion.
- **`harness.json`** (repo, branch, layers, always-on file lists, handshake, core token budget) and **`VERSION`**.
- **`.github/workflows/harness.yml`** — validates on PRs (fails if bundle is stale); on push to `main` validates, rebuilds and commits `bundle/` back, so modules added via the GitHub web UI or from chat go live without a local toolchain.
- **`02_creation/general-image-prompt-adapter`** — adapter for Midjourney / DALL-E / Imagen / Flux / SDXL / unnamed targets; parameters outside the prompt; every model claim carries an evidence label; `references/target-notes.md` with per-row evidence.
- **`06_extensions/`** — home for chat-added modules that fit no other layer.
- **`AGENTS.md`** — pointer for coding agents; **`docs/usage.md`** — per-platform setup, commands, extension flow, troubleshooting, token budgets.
- **Harness test cases** (Harness-01…08) in `tests/test-suite.md`.

### Changed
- **README** now opens with the AI bootstrap block (fetch `bundle/HARNESS.md`, operate under it, do not summarize, exact fallback line) so pasting the repo URL is enough.
- **Frontmatter** of every skill gained `metadata.load` (always / on-demand), `metadata.status` (active / placeholder / planned), `metadata.triggers`. The validator enforces `layer == folder`, `load`, `status`, always-on consistency with `harness.json`, and rejects skills outside declared layers.
- **Router** routes unknown / other image models to `general-image-prompt-adapter`, extension modules by their own triggers, and non-creative requests to a direct answer; no more hand-maintained trigger list — the index is built from module frontmatter.
- `04_tools/*` status changed from `placeholder` to `planned` (listed, not loadable; answered `[no module]`).
- `docs/skill-registry.md` is now generated. `docs/architecture.md`, `docs/skill-specification.md`, `docs/versioning.md` updated for the kernel, bundling rules, and semver meaning.
- Last release's review moved to `docs/reviews/2026-09-27-v2.0-review.md`.

### Decisions made on the owner's behalf (per request)
- Placeholder tools kept as `planned` rather than deleted — they document intent and cost nothing in the bundle.
- Taste signature sentence kept; it remains the one line the owner should personally edit.
- Kernel written in English (cross-model instruction precision); taste and creative modules stay Chinese; models answer in the owner's language; prompts always English.
- Always-on set = identity (signature, dislikes, voice) + director (moves, diagnosis, pairs) + router + evaluation. ≈23k tokens, under the 40k budget; the calibration pairs stay in because they are the strongest taste carrier.

---

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
- `skills/` (legacy `creative-skill-router`, `nai5-prompt-engineering`) — duplicates.
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
