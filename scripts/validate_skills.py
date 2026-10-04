#!/usr/bin/env python3
"""
validate_skills.py — structural checks for the skill hub.

Checks every SKILL.md against the Agent Skills spec (agentskills.io/specification)
plus repo-local rules:

  spec
  - frontmatter present; `name` and `description` non-empty
  - `name` == parent directory; [a-z0-9] + single hyphens; <= 64 chars
  - `description` <= 1024 chars, no '<' or '>'
  - warns on non-spec top-level keys (priority, trigger, ...)

  repo
  - architecture pipeline references are valid
  - creative director, specialists, adapters and evaluation loop expose gate contracts
  - no duplicate skill names
  - metadata.layer == actual layer folder; metadata.load in {always, on-demand}; metadata.status in {active, placeholder, planned}
  - every `references/*.md` mentioned in SKILL.md exists; every references/*.md on disk is mentioned (warn)
  - always-on entries in harness.json point at existing skills/files
  - skills live only under the layer folders listed in harness.json
  - warns when SKILL.md body is large (> ~5000 tokens)

  --check-bundle
  - rebuilds the bundle in memory and fails if bundle/ or docs/skill-registry.md on disk are stale

Usage:  python3 scripts/validate_skills.py [--check-bundle] [repo_root]
Exit 1 on any error; warnings never fail.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import skills_lib as L  # noqa: E402


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    check_bundle = "--check-bundle" in sys.argv
    root = L.repo_root(args[0] if args else None)
    cfg = L.load_config(root)
    layers = cfg["layers"]
    errors, warnings = [], []

    # skills outside declared layers (e.g. a stray root-level skill) are an error
    all_paths = set(L.find_skill_files(root))
    layer_paths = set(L.find_skill_files(root, layers))
    for p in sorted(all_paths - layer_paths):
        errors.append(f"{os.path.relpath(p, root)}: SKILL.md outside declared layers {layers}")

    skills = {}
    for path in sorted(layer_paths):
        s = L.load_skill(path, root)
        rel = s["rel"]
        for e in s["errors"]:
            errors.append(f"{rel}: {e}")
        if s["errors"]:
            continue
        name, desc, md = s["name"], s["description"], s["metadata"]

        if not name:
            errors.append(f"{rel}: missing `name`")
        else:
            if name != s["parent"]:
                errors.append(f"{rel}: name `{name}` != directory `{s['parent']}`")
            if not L.NAME_RE.match(name) or len(name) > 64:
                errors.append(f"{rel}: name `{name}` violates [a-z0-9-]/64-char rule")
            if name in skills:
                errors.append(f"{rel}: duplicate skill name `{name}` (also {skills[name]['rel']})")
            skills.setdefault(name, s)

        if not desc:
            errors.append(f"{rel}: missing `description`")
        else:
            if len(desc) > 1024:
                errors.append(f"{rel}: description {len(desc)} chars (> 1024)")
            if "<" in desc or ">" in desc:
                errors.append(f"{rel}: description contains angle brackets")
            if len(desc) < 60:
                warnings.append(f"{rel}: description short ({len(desc)} chars) — say what + when + triggers")

        for k in s["top_keys"]:
            if k not in L.SPEC_KEYS:
                warnings.append(f"{rel}: non-spec top-level key `{k}` (move under metadata:)")

        if md.get("layer") != s["layer"]:
            errors.append(f"{rel}: metadata.layer `{md.get('layer')}` != folder `{s['layer']}`")
        if md.get("load") not in L.LOAD_VALUES:
            errors.append(f"{rel}: metadata.load must be one of {sorted(L.LOAD_VALUES)}")
        if md.get("status") not in L.STATUS_VALUES:
            errors.append(f"{rel}: metadata.status must be one of {sorted(L.STATUS_VALUES)}")
        if not md.get("triggers"):
            warnings.append(f"{rel}: metadata.triggers empty — router index will rely on description only")

        for ref in s["references"]:
            if not os.path.exists(os.path.join(s["dir"], ref)):
                errors.append(f"{rel}: mentions missing file {ref}")
        mentioned = set(m for m in s["references"] if f"`{m}`" in s["body"])
        for ref in s["references"]:
            if ref not in mentioned:
                warnings.append(f"{rel}: {ref} exists but is not listed in SKILL.md (bundled anyway, alphabetically)")

        toks = L.estimate_tokens(s["body"])
        if toks > 5000:
            warnings.append(f"{rel}: body ≈{toks} tokens (> 5000) — move detail into references/")

    # always-on config sanity
    for name, files in cfg.get("always_on", {}).items():
        if name not in skills:
            errors.append(f"harness.json always_on: unknown skill `{name}`")
            continue
        for f in files:
            if not os.path.exists(os.path.join(skills[name]["dir"], f)):
                errors.append(f"harness.json always_on: `{name}` has no file {f}")
        if skills[name]["metadata"].get("load") != "always":
            errors.append(f"harness.json always_on: `{name}` must declare metadata.load: always")
    for name, s in skills.items():
        if s["metadata"].get("load") == "always" and name not in cfg.get("always_on", {}):
            errors.append(f"{s['rel']}: metadata.load is `always` but harness.json always_on does not list it")


    # architecture contract sanity
    pipeline = cfg.get('pipeline', {})
    required_pipeline = {'aesthetic_gate', 'blueprint_gate', 'evaluation_gate', 'adapters'}
    missing = required_pipeline - set(pipeline)
    if missing:
        errors.append(f'harness.json pipeline missing keys: {sorted(missing)}')
    for key in ('aesthetic_gate', 'evaluation_gate'):
        name = pipeline.get(key)
        if name and name not in skills:
            errors.append(f'harness.json pipeline.{key}: unknown skill `{name}`')
    for kind, name in (pipeline.get('blueprint_gate') or {}).items():
        if name not in skills:
            errors.append(f'harness.json pipeline.blueprint_gate.{kind}: unknown skill `{name}`')
    for name in pipeline.get('adapters', []):
        if name not in skills:
            errors.append(f'harness.json pipeline.adapters: unknown skill `{name}`')

    director = skills.get('aesthetic-director-core')
    if director:
        body = director['body']
        if not all(token in body for token in ('FULL', 'AUDIT', 'ESCALATE')):
            errors.append('aesthetic-director-core: missing FULL/AUDIT/ESCALATE gate contract')
    for name in ('character-design-engine', 'illustration-direction'):
        skill = skills.get(name)
        if skill and 'Blueprint Gate Contract' not in skill['body']:
            errors.append(f'{name}: missing Blueprint Gate Contract')
    for name in ('anima-prompt-compiler', 'nai5-community-prompt-engineering', 'general-image-prompt-adapter'):
        skill = skills.get(name)
        if skill:
            body = skill['body'].lower()
            if 'blueprint' not in body or 'adapter' not in body:
                errors.append(f'{name}: missing adapter blueprint boundary')

    if not os.path.exists(os.path.join(root, cfg["kernel"])):
        errors.append(f"kernel file {cfg['kernel']} missing")

    if check_bundle and not errors:
        import build  # noqa: E402  (same directory)
        stale = build.stale_outputs(root)
        for rel in stale:
            errors.append(f"stale generated file: {rel} — run `python3 scripts/build.py`")

    print(f"checked {len(skills)} skills under {root}")
    for w in warnings:
        print("  WARN ", w)
    for e in errors:
        print("  ERROR", e)
    if errors:
        print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
        sys.exit(1)
    print(f"\nOK — 0 errors, {len(warnings)} warning(s)")


if __name__ == "__main__":
    main()
