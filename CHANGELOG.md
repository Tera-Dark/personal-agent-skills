# Changelog

All notable changes to the `personal-agent-skills` repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
