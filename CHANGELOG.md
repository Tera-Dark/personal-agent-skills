# Changelog

All notable changes to the `personal-agent-skills` repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
