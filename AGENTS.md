# AGENTS.md

This repository is an LLM **harness**: a kernel plus modular skills for Tera-Dark's creative work (OC design, illustration direction, image-prompt compilation for Anima / NovelAI / other models).

**If you are an AI agent asked to operate under this repo** (Codex, Cursor, Claude Code, any coding agent):

1. Read `bundle/HARNESS.md` and follow it. It contains the kernel (operating contract), the module index, and the always-on modules. On-demand modules are single files in `bundle/modules/`.
2. Do not summarize the repository. Handshake as KERNEL §1 says, then work.

**If you are editing this repo:**

- Sources are `kernel/`, `harness.json`, `VERSION`, and `<layer>/<skill>/SKILL.md` (+ `references/`). `bundle/` and `docs/skill-registry.md` are generated — never edit them by hand.
- After any change: `python3 scripts/validate_skills.py && python3 scripts/build.py`. CI does the same and commits the bundle on `main`.
- Adding a capability: follow `kernel/EXTENSION-PROTOCOL.md`; template in `kernel/templates/`.
- To install skills into a runtime that discovers `~/.claude/skills/<name>/SKILL.md` (or similar): `scripts/install.sh [target]`.
