#!/usr/bin/env python3
"""
validate_skills.py — sanity checks for this skill hub.

Checks every SKILL.md against the Agent Skills spec (agentskills.io/specification)
plus a few repo-local rules that would have caught the drift fixed in v2.0.0:

  - frontmatter exists and has non-empty `name` and `description`
  - `name` matches the parent directory name; lowercase / digits / single hyphens only; <= 64 chars
  - `description` <= 1024 chars, contains no '<' or '>'
  - no two skills share a name (duplicate copies were the #1 structural problem)
  - warns on non-spec top-level frontmatter keys (e.g. `priority`) — most runtimes ignore them, but they are not portable
  - warns when the SKILL.md body is large (> ~5000 tokens ≈ 20k chars) — spec recommends keeping instructions small and pushing detail into references/
  - every skill referenced in docs/skill-registry.md exists, and every skill on disk is in the registry
  - every `references/*.md` path mentioned in a SKILL.md exists

Usage:  python3 scripts/validate_skills.py [repo_root]
Exit code 1 on any error (warnings do not fail).
No third-party dependencies.
"""
import os
import re
import sys

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), ".."))
SPEC_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
errors, warnings = [], []


def parse_frontmatter(text):
    """Minimal YAML-ish frontmatter parser: top-level `key: value` lines only."""
    if not text.startswith("---"):
        return None, "no frontmatter"
    parts = text.split("\n---", 1)
    if len(parts) < 2:
        return None, "unterminated frontmatter"
    block = parts[0][3:]
    data, top_keys = {}, []
    for line in block.splitlines():
        if not line.strip() or line.startswith(" ") or line.startswith("\t"):
            continue
        if ":" not in line:
            return None, f"bad frontmatter line: {line!r}"
        k, v = line.split(":", 1)
        data[k.strip()] = v.strip()
        top_keys.append(k.strip())
    return (data, top_keys), None


def find_skills():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if not d.startswith(".") and d not in ("node_modules",)]
        if "SKILL.md" in filenames:
            yield os.path.join(dirpath, "SKILL.md")


skills = {}
for path in sorted(find_skills()):
    rel = os.path.relpath(path, ROOT)
    text = open(path, encoding="utf-8").read()
    parsed, err = parse_frontmatter(text)
    if err:
        errors.append(f"{rel}: {err}")
        continue
    data, top_keys = parsed
    name = data.get("name", "")
    desc = data.get("description", "")
    parent = os.path.basename(os.path.dirname(path))

    if not name:
        errors.append(f"{rel}: missing `name`")
    else:
        if name != parent:
            errors.append(f"{rel}: name `{name}` != directory `{parent}`")
        if not NAME_RE.match(name) or len(name) > 64:
            errors.append(f"{rel}: name `{name}` violates [a-z0-9-] / 64-char rule")
        if name in skills:
            errors.append(f"{rel}: duplicate skill name `{name}` (also at {skills[name]})")
        skills.setdefault(name, rel)
    if not desc:
        errors.append(f"{rel}: missing `description`")
    else:
        if len(desc) > 1024:
            errors.append(f"{rel}: description is {len(desc)} chars (> 1024)")
        if "<" in desc or ">" in desc:
            errors.append(f"{rel}: description contains angle brackets")
        if len(desc) < 60:
            warnings.append(f"{rel}: description is short ({len(desc)} chars) — add what it does AND when to use it")
    for k in top_keys:
        if k not in SPEC_KEYS:
            warnings.append(f"{rel}: non-spec frontmatter key `{k}` (move under `metadata:`)")

    body = text.split("\n---", 1)[1] if "\n---" in text else ""
    if len(body) > 20000:
        warnings.append(f"{rel}: body is {len(body)} chars (~{len(body)//4} tokens) — consider moving detail into references/")

    skill_dir = os.path.dirname(path)
    for ref in set(re.findall(r"`(references/[^`]+\.md)`", text)):
        if not os.path.exists(os.path.join(skill_dir, ref)):
            errors.append(f"{rel}: references missing file {ref}")

# registry cross-check
reg_path = os.path.join(ROOT, "docs", "skill-registry.md")
if os.path.exists(reg_path):
    reg = open(reg_path, encoding="utf-8").read()
    reg_names = set(re.findall(r"^\|\s*`([a-z0-9-]+)`\s*\|", reg, flags=re.M))
    for n in sorted(reg_names - set(skills)):
        errors.append(f"docs/skill-registry.md lists `{n}` but no such skill exists")
    for n in sorted(set(skills) - reg_names):
        warnings.append(f"skill `{n}` is not listed in docs/skill-registry.md")
else:
    warnings.append("docs/skill-registry.md not found")

print(f"checked {len(skills)} skills under {ROOT}")
for w in warnings:
    print("  WARN ", w)
for e in errors:
    print("  ERROR", e)
if errors:
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
    sys.exit(1)
print(f"\nOK — 0 errors, {len(warnings)} warning(s)")
