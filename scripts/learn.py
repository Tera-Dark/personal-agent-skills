#!/usr/bin/env python3
"""Deterministic, offline personal-taste learning. Python standard library only."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
EVENTS = Path("data/learning/events.jsonl")
ACTIONS = Path("data/learning/actions.jsonl")
POLICIES = Path("data/learning/policies.json")
SESSIONS = Path("data/learning/sessions")
DIGEST = Path("00_core/personal-identity-profile/references/learning-digest.md")
REQUIRED = ("rule_id", "scope", "axis", "rule", "polarity", "evidence_type", "artifact_id")
KINDS = {"TEXT-APPROVED", "TEXT-REJECTED", "USER-IMAGE-REPORT",
         "IMAGE-VERIFIED", "USER-EXPLICIT-POLICY", "TECHNICAL-CORRECTION"}
RULE_RE = re.compile(r"^[a-z0-9][a-z0-9_.-]{1,79}$")
SESSION_RE = re.compile(r"^[a-z0-9][a-z0-9_-]{0,63}$")
PREFIXES = ("mode:", "model:", "ip:", "project:", "artist:")


class LearnError(ValueError):
    pass


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def jsonl(root, rel):
    p = root / rel
    if not p.exists():
        return []
    result = []
    for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        if line.strip():
            try:
                item = json.loads(line)
                if not isinstance(item, dict):
                    raise ValueError("expected JSON object")
                result.append(item)
            except ValueError as exc:
                raise LearnError(f"{rel}:{n}: {exc}") from exc
    return result


def append(root, rel, obj):
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(obj, ensure_ascii=False, sort_keys=True) + "\n")


def read_policies(root):
    p = root / POLICIES
    if not p.exists():
        return {}
    data = json.loads(p.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise LearnError("policies must be a JSON object")
    return data


def write_json(p, obj):
    p.parent.mkdir(parents=True, exist_ok=True)
    temp = p.with_name(p.name + ".tmp")
    temp.write_text(json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    temp.replace(p)


def normalize(event):
    if not isinstance(event, dict):
        raise LearnError("expected JSON object")
    for k in REQUIRED:
        if not isinstance(event.get(k), str) or not event[k].strip():
            raise LearnError(f"missing or blank field: {k}")
    e = {k: event[k].strip() for k in REQUIRED}
    if not RULE_RE.fullmatch(e["rule_id"]):
        raise LearnError("rule_id must be lowercase slug of length 2-80")
    if e["scope"] != "global" and not any(
        e["scope"].startswith(p) and len(e["scope"]) > len(p) for p in PREFIXES
    ):
        raise LearnError("invalid scope; use global, mode:, model:, ip:, project:, artist:")
    if e["polarity"] not in ("support", "oppose"):
        raise LearnError("polarity must be support or oppose")
    if e["evidence_type"] not in KINDS:
        raise LearnError("invalid evidence_type")
    if e["evidence_type"] == "USER-EXPLICIT-POLICY" and e["polarity"] != "support":
        raise LearnError("explicit policy must support its specified rule")
    if any(len(e[k]) > 400 for k in ("rule", "axis", "artifact_id")):
        raise LearnError("field too long for public abstract ledger")
    e["note"] = str(event.get("note", "")).strip()[:400]
    e["date"] = str(event.get("date", now()[:10]))
    try:
        datetime.strptime(e["date"], "%Y-%m-%d")
    except ValueError as exc:
        raise LearnError("date must be a real YYYY-MM-DD") from exc
    return e


def same_definition(a, b):
    return all(a.get(k) == b.get(k) for k in ("rule_id", "scope", "axis", "rule"))


def record(root, raw):
    e = normalize(raw)
    existing = jsonl(root, EVENTS)
    for old in existing:
        if old["rule_id"] == e["rule_id"] and not same_definition(old, e):
            raise LearnError("rule_id already assigned to a different rule or scope")
        if (old["rule_id"], old["artifact_id"], old["polarity"]) == (
            e["rule_id"], e["artifact_id"], e["polarity"]
        ):
            return {"status": "duplicate", "id": old["id"]}
    seq = 1 + sum(old["date"] == e["date"] for old in existing)
    e["id"] = f"FB-{e['date'].replace('-', '')}-{seq:03d}"
    e["created_at"] = now()
    append(root, EVENTS, e)
    return {"status": "recorded", "id": e["id"]}


def review(root):
    grouped = {}
    for e in jsonl(root, EVENTS):
        grouped.setdefault(e["rule_id"], []).append(e)
    policies = read_policies(root)
    result = []
    for key, rows in sorted(grouped.items()):
        support = {e["artifact_id"] for e in rows if e["polarity"] == "support"}
        oppose = {e["artifact_id"] for e in rows if e["polarity"] == "oppose"}
        explicit = any(e["polarity"] == "support" and e["evidence_type"] ==
                       "USER-EXPLICIT-POLICY" for e in rows)
        eligible = bool(support) and not oppose and (explicit or len(support) >= 3)
        result.append({"rule_id": key, "scope": rows[0]["scope"], "axis": rows[0]["axis"],
                       "rule": rows[0]["rule"], "support": len(support), "oppose": len(oppose),
                       "explicit": explicit, "eligible": eligible,
                       "active": policies.get(key, {}).get("active", False),
                       "needs_review": bool(oppose and policies.get(key, {}).get("active", False)),
                       "effective_active": bool(policies.get(key, {}).get("active", False)
                                                and not oppose)})
    return result


def promote(root, key):
    candidates = {v["rule_id"]: v for v in review(root)}
    if key not in candidates or not candidates[key]["eligible"]:
        raise LearnError("promotion blocked: needs explicit request or >=3 independent examples and no opposition")
    policies = read_policies(root)
    if policies.get(key, {}).get("active"):
        return {"status": "already-active", "rule_id": key}
    row = candidates[key]
    policy = {k: row[k] for k in ("rule", "scope", "axis", "support", "oppose")}
    policy.update({"active": True, "approved_at": now()})
    policies[key] = policy
    write_json(root / POLICIES, policies)
    append(root, ACTIONS, {"action": "promote", "rule_id": key, "at": policy["approved_at"]})
    return {"status": "promoted", "rule_id": key}


def undo(root, key):
    policies = read_policies(root)
    if key not in policies or not policies[key].get("active"):
        raise LearnError("rule is not active")
    policies[key]["active"] = False
    policies[key]["revoked_at"] = now()
    write_json(root / POLICIES, policies)
    append(root, ACTIONS, {"action": "undo", "rule_id": key, "at": now()})
    return {"status": "undone", "rule_id": key}


def digest_content(root):
    status = {r["rule_id"]: r for r in review(root)}
    active = [(k, v) for k, v in sorted(read_policies(root).items())
              if v.get("active") and status.get(k, {}).get("effective_active")]
    lines = [
        "# Learned Taste Digest — approved scoped rules",
        "",
        "> Generated by scripts/learn.py digest. Never treat candidate events as global defaults.",
        "> Explicit current-turn requests and locked identities override these rules.",
        "",
    ]
    if not active:
        lines.append("No approved learned rules yet. Use the existing Taste Core.")
    for key, v in active:
        lines.append(f"- **{v['scope']} / {v['axis']}**: {v['rule']} (ID: {key})")
    lines += ["", "Provenance: data/learning/events.jsonl and data/learning/actions.jsonl.", ""]
    return "\n".join(lines)


def digest(root):
    p = root / DIGEST
    p.parent.mkdir(parents=True, exist_ok=True)
    content = digest_content(root)
    if not p.exists() or p.read_text(encoding="utf-8") != content:
        p.write_text(content, encoding="utf-8")
    return {"status": "ok", "effective_active_rules": sum(
        r["effective_active"] for r in review(root))}


def validate(root):
    ids, definitions, semantics = set(), {}, set()
    events = jsonl(root, EVENTS)
    for e in events:
        normalize(e)
        if not e.get("id") or e["id"] in ids:
            raise LearnError("duplicate/missing event ID")
        ids.add(e["id"])
        k = e["rule_id"]
        if k in definitions and not same_definition(definitions[k], e):
            raise LearnError("inconsistent rule definition")
        definitions[k] = e
        sig = (k, e["artifact_id"], e["polarity"])
        if sig in semantics:
            raise LearnError("duplicate semantic event")
        semantics.add(sig)
    for key, p in read_policies(root).items():
        if key not in definitions or (p.get("active") and not p.get("approved_at")):
            raise LearnError("orphan/invalid active policy")
    jsonl(root, ACTIONS)
    p = root / DIGEST
    if p.exists() and p.read_text(encoding="utf-8") != digest_content(root):
        raise LearnError("stale learning digest; run scripts/learn.py digest")
    return {"status": "pass", "events": len(events), "policies": len(read_policies(root))}


def session_save(root, name, packet):
    if not SESSION_RE.fullmatch(name) or not isinstance(packet, dict):
        raise LearnError("invalid session name or packet")
    keys = ("target", "mode", "project", "prompt_version", "locked",
            "approved", "rejected", "next_action")
    safe = {k: packet[k] for k in keys if k in packet}
    if any(not isinstance(v, (str, list, dict, int, float, type(None)))
           for v in safe.values()):
        raise LearnError("unsupported session field value")
    safe["updated_at"] = now()
    p = root / SESSIONS / (name + ".json")
    write_json(p, safe)
    return {"status": "saved", "path": str(p.relative_to(root))}


def session_load(root, name):
    if not SESSION_RE.fullmatch(name):
        raise LearnError("invalid session name")
    p = root / SESSIONS / (name + ".json")
    if not p.exists():
        raise LearnError("session not found")
    return json.loads(p.read_text(encoding="utf-8"))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    subs = parser.add_subparsers(dest="command", required=True)
    subs.add_parser("record").add_argument("--file")
    subs.add_parser("review")
    subs.add_parser("promote").add_argument("rule_id")
    subs.add_parser("undo").add_argument("rule_id")
    subs.add_parser("digest")
    subs.add_parser("validate")
    p = subs.add_parser("session-save")
    p.add_argument("name")
    p.add_argument("--file")
    subs.add_parser("session-load").add_argument("name")
    a = parser.parse_args(argv)
    root = a.root.resolve()
    try:
        if a.command in ("record", "session-save"):
            raw = Path(a.file).read_text(encoding="utf-8") if a.file else sys.stdin.read()
            packet = json.loads(raw)
            result = record(root, packet) if a.command == "record" else session_save(root, a.name, packet)
        elif a.command == "review":
            result = review(root)
        elif a.command == "promote":
            result = promote(root, a.rule_id)
        elif a.command == "undo":
            result = undo(root, a.rule_id)
        elif a.command == "digest":
            result = digest(root)
        elif a.command == "validate":
            result = validate(root)
        else:
            result = session_load(root, a.name)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (LearnError, ValueError, OSError) as exc:
        print(f"learning error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
