#!/usr/bin/env python3
"""Create a reviewable feedback event without auto-saving/promoting user preferences."""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from learn import LearnError, normalize


def draft(rule_id, scope, axis, rule, artifact_id, polarity, evidence_type, note):
    return normalize({
        "rule_id": rule_id, "scope": scope, "axis": axis, "rule": rule,
        "artifact_id": artifact_id, "polarity": polarity,
        "evidence_type": evidence_type, "note": note
    })


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--rule-id", required=True)
    p.add_argument("--scope", required=True, help="mode:portrait, model:NAI5, project:..., or global")
    p.add_argument("--axis", required=True, help="camera / outfit / expression / color etc.")
    p.add_argument("--rule", required=True, help="Short abstract reusable observation, not full chat")
    p.add_argument("--artifact-id", required=True, help="Public-safe anonymous comparison ID")
    p.add_argument("--polarity", choices=("support", "oppose"), default="support")
    p.add_argument("--evidence-type", choices=("USER-IMAGE-REPORT", "TEXT-APPROVED", "TEXT-REJECTED", "USER-EXPLICIT-POLICY"),
                   default="USER-IMAGE-REPORT")
    p.add_argument("--note", default="")
    p.add_argument("--out", type=Path, help="Optional draft filename; no GitHub synchronization")
    args = p.parse_args(argv)
    try:
        event = draft(args.rule_id, args.scope, args.axis, args.rule, args.artifact_id,
                      args.polarity, args.evidence_type, args.note)
        text = json.dumps(event, ensure_ascii=False, indent=2) + "\n"
        if args.out:
            if args.out.exists():
                raise LearnError("refusing to overwrite an existing feedback draft")
            args.out.write_text(text, encoding="utf-8")
            print(f"Draft saved (NOT recorded or promoted): {args.out}")
        else:
            print(text, end="")
        return 0
    except (LearnError, OSError, ValueError) as exc:
        print(f"feedback draft error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
