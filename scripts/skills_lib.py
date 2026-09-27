"""
skills_lib.py — shared helpers for validate_skills.py and build.py.

No third-party dependencies. Python 3.8+.
"""
import json
import os
import re
from datetime import date

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SPEC_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
LOAD_VALUES = {"always", "on-demand"}
STATUS_VALUES = {"active", "placeholder", "planned"}
SKIP_DIRS = {".git", "node_modules", "__pycache__"}


def repo_root(start=None):
    p = os.path.abspath(start or os.path.join(os.path.dirname(__file__), ".."))
    return p


def load_config(root):
    with open(os.path.join(root, "harness.json"), encoding="utf-8") as f:
        return json.load(f)


def read_version(root):
    p = os.path.join(root, "VERSION")
    if os.path.exists(p):
        return open(p, encoding="utf-8").read().strip()
    return "0.0.0"


def today():
    return date.today().isoformat()


# ---------- frontmatter ----------

def split_frontmatter(text):
    """Return (frontmatter_text, body_text, error). Frontmatter excludes the --- fences."""
    if not text.startswith("---"):
        return None, text, "no frontmatter"
    end = text.find("\n---", 3)
    if end == -1:
        return None, text, "unterminated frontmatter"
    fm = text[3:end].strip("\n")
    body = text[end + 4:]
    if body.startswith("\n"):
        body = body[1:]
    return fm, body, None


def parse_frontmatter(fm_text):
    """
    Minimal YAML subset: top-level `key: value` and one nested mapping level under `metadata:`.
    Returns (data: dict, top_keys: list, error).
    """
    data, top_keys = {}, []
    current_map = None
    for raw in fm_text.splitlines():
        if not raw.strip():
            continue
        if raw.startswith("  ") and current_map is not None:
            line = raw.strip()
            if ":" not in line:
                return None, top_keys, f"bad nested line: {raw!r}"
            k, v = line.split(":", 1)
            current_map[k.strip()] = _unquote(v.strip())
            continue
        if raw.startswith(" ") or raw.startswith("\t"):
            return None, top_keys, f"unexpected indentation: {raw!r}"
        if ":" not in raw:
            return None, top_keys, f"bad frontmatter line: {raw!r}"
        k, v = raw.split(":", 1)
        k, v = k.strip(), v.strip()
        top_keys.append(k)
        if v == "":
            data[k] = {}
            current_map = data[k]
        else:
            data[k] = _unquote(v)
            current_map = None
    return data, top_keys, None


def _unquote(v):
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    return v


# ---------- discovery ----------

def find_skill_files(root, layers=None):
    """Yield absolute paths of every SKILL.md under the layer folders (or the whole repo if layers is None)."""
    bases = [os.path.join(root, l) for l in layers] if layers else [root]
    for base in bases:
        if not os.path.isdir(base):
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".")]
            if "SKILL.md" in filenames:
                yield os.path.join(dirpath, "SKILL.md")


def load_skill(path, root):
    """Parse one SKILL.md into a dict. Never raises; errors go into skill['errors']."""
    text = open(path, encoding="utf-8").read()
    fm_text, body, err = split_frontmatter(text)
    skill = {
        "path": path,
        "rel": os.path.relpath(path, root).replace(os.sep, "/"),
        "dir": os.path.dirname(path),
        "rel_dir": os.path.relpath(os.path.dirname(path), root).replace(os.sep, "/"),
        "parent": os.path.basename(os.path.dirname(path)),
        "layer": os.path.relpath(os.path.dirname(path), root).replace(os.sep, "/").split("/")[0],
        "text": text,
        "body": body,
        "frontmatter": {},
        "top_keys": [],
        "errors": [],
        "warnings": [],
        "references": [],
    }
    if err:
        skill["errors"].append(err)
        return skill
    data, top_keys, perr = parse_frontmatter(fm_text)
    if perr:
        skill["errors"].append(perr)
        return skill
    skill["frontmatter"] = data
    skill["top_keys"] = top_keys
    skill["name"] = data.get("name", "")
    skill["description"] = data.get("description", "")
    md = data.get("metadata", {}) if isinstance(data.get("metadata"), dict) else {}
    skill["metadata"] = md
    skill["references"] = referenced_files(body, skill["dir"])
    return skill


def referenced_files(body, skill_dir):
    """
    Reference files in the order the SKILL.md mentions them (first mention wins),
    then any references/*.md on disk that were not mentioned, alphabetically.
    """
    seen, ordered = set(), []
    for m in re.finditer(r"`(references/[^`<>\s]+\.md)`", body):
        rel = m.group(1)
        if rel not in seen:
            seen.add(rel)
            ordered.append(rel)
    ref_dir = os.path.join(skill_dir, "references")
    if os.path.isdir(ref_dir):
        for fn in sorted(os.listdir(ref_dir)):
            rel = f"references/{fn}"
            if fn.endswith(".md") and rel not in seen:
                seen.add(rel)
                ordered.append(rel)
    return ordered


# ---------- text utilities ----------

def estimate_tokens(text):
    """Rough, tokenizer-agnostic estimate: CJK ≈ 1 token/char, everything else ≈ 4 chars/token."""
    cjk = 0
    for ch in text:
        o = ord(ch)
        if 0x3000 <= o <= 0x30FF or 0x4E00 <= o <= 0x9FFF or 0xFF00 <= o <= 0xFFEF or 0x3400 <= o <= 0x4DBF:
            cjk += 1
    other = len(text) - cjk
    return int(cjk * 1.0 + other / 4)


def demote_headings(text, levels=1):
    """Add `levels` '#' to every markdown heading outside fenced code blocks."""
    out, in_fence = [], False
    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            out.append(line)
            continue
        if not in_fence and re.match(r"^#{1,6}\s", line):
            out.append("#" * levels + line)
        else:
            out.append(line)
    return "\n".join(out) + ("\n" if text.endswith("\n") else "")


def strip_frontmatter(text):
    _, body, _ = split_frontmatter(text)
    return body
