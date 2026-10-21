# Third-party datasets and license boundaries

The project root uses the MIT license for original Harness source code. The checked-in generated tag index under bundle/tag-index/ is derived from data in the third-party Good Anima project, identified as GPL-3.0.

- Source project: https://github.com/ShiroEirin/comfyui-good-anima
- Source data: https://github.com/ShiroEirin/comfyui-good-anima/blob/main/danbooru-tags/tags_index.json
- Source license: https://github.com/ShiroEirin/comfyui-good-anima/blob/main/LICENSE
- Snapshot provenance and SHA-256: bundle/tag-index/manifest.json and bundle/tag-index/NOTICE.md
- Intended use: exact/alias tag lookup, not an art-style prompt dataset or training set.
- This MIT repository **does not** assert that its root license relicenses the third-party data.

## MOSS-Image official prompt-enhancer compatibility reference

The MOSS renderer and `scripts/moss_layout.py` are locally maintained code and documentation. The 2026-10-21 behavior-alignment update refers to OpenMOSS's public prompt-enhancer `SKILL.md`, `references/layout.md` and `scripts/compile_prompt.py` for schema, nine-decimal pixel-edge conversion, failure handling, and test examples. The upstream project is Apache-2.0 licensed; the official source was **not vendored verbatim** into this repository.

- Source: https://github.com/OpenMOSS/MOSS-Image/tree/main/skills/moss-image-prompt-enhancer
- Upstream license: https://github.com/OpenMOSS/MOSS-Image/blob/main/LICENSE
- Locally maintained integration guide: `03_prompt/moss-image-renderer/references/official-enhancer-workflow.md`
- Local compatibility tests: `tests/test_moss_official_enhancer.py`

These notices are for attribution/transparency, not a legal opinion that all downstream redistribution conditions are satisfied. Before redistributing bundled third-party data elsewhere, review the applicable upstream license and distribution obligations. As a lower-risk alternative, build shards from upstream directly for an authorized installation rather than republishing them.
