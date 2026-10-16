#!/usr/bin/env python3
"""Evidence-aware A/B records for user-run NAI5/Anima images.

The script validates experiment metadata and deliberately NEVER claims to
inspect, generate or score an image. Real user verdicts are required.
"""
import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CASE_FILE = ROOT / "tests" / "visual-benchmarks" / "cases.json"
SCOPES = {"portrait", "cinematic-duo", "concept-poster"}
STATES = {"IMAGE-PENDING", "USER-RATED", "IMAGE-REVIEWED"}
SETTING_KEYS = ("model", "checkpoint", "seed", "sampler", "steps", "resolution",
                "artist_stack", "quality", "negative", "guidance")


def load_cases(root=ROOT):
    doc = json.loads((root / "tests/visual-benchmarks/cases.json").read_text(encoding="utf-8"))
    if doc.get("schema_version") != 1 or not isinstance(doc.get("cases"), list):
        raise ValueError("invalid visual-benchmark case schema")
    out = {}
    for case in doc["cases"]:
        if case.get("id") in out or case.get("id") not in SCOPES:
            raise ValueError("unknown/duplicate case")
        if not case.get("locked") or not case.get("rubric") or not case.get("axis"):
            raise ValueError("benchmark case lacks lock, rubric or change axis")
        if case.get("status") != "IMAGE-PENDING":
            raise ValueError("template must remain IMAGE-PENDING, not falsely graded")
        out[case["id"]] = case
    if set(out) != SCOPES:
        raise ValueError("three baseline task categories required")
    return out


def validate_record(run, root=ROOT):
    cases = load_cases(root)
    if not isinstance(run, dict) or run.get("case_id") not in cases:
        raise ValueError("unknown benchmark case")
    case = cases[run["case_id"]]
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{2,60}", str(run.get("run_id", ""))):
        raise ValueError("run_id must be a safe short slug")
    a, b = run.get("baseline"), run.get("variant")
    if not isinstance(a, dict) or not isinstance(b, dict):
        raise ValueError("baseline and variant must be objects")
    for field in SETTING_KEYS:
        if field not in a or field not in b or a[field] != b[field]:
            raise ValueError(f"uncontrolled setting differs/missing: {field}")
    if a.get("design_id") == b.get("design_id"):
        raise ValueError("A/B requires different design IDs")
    if run.get("changed_axis") != case["axis"]:
        raise ValueError("changed_axis deviates from the pre-registered benchmark")
    changes = run.get("design_changes", [])
    if changes != [case["axis"]]:
        raise ValueError("change one pre-registered design variable only")
    # Store refs/abstract metadata only; do not put private image files or full prompts in public Git.
    if any(k in run for k in ("image_base64", "image_path", "full_prompt", "image_url")):
        raise ValueError("do not save images, URLs or complete prompts in a public benchmark record")
    result = run.get("result")
    if not isinstance(result, dict) or result.get("status") not in STATES:
        raise ValueError("result must have a valid evidence status")
    if result["status"] == "IMAGE-PENDING":
        if result.get("scores") or result.get("winner"):
            raise ValueError("pending run cannot claim scores or winner")
    else:
        if not str(result.get("reviewer", "")).strip():
            raise ValueError("human reviewer is required for a rated/reviewed result")
        scores = result.get("scores")
        if not isinstance(scores, dict) or set(scores) != {"baseline", "variant"}:
            raise ValueError("both image score matrices required")
        for group in ("baseline", "variant"):
            if set(scores[group]) != set(case["rubric"]):
                raise ValueError("missing/mismatched evaluation axes")
            if any(type(v) is not int or not 1 <= v <= 5 for v in scores[group].values()):
                raise ValueError("scores must be human 1..5 integer ratings")
        if result.get("winner") not in ("baseline", "variant", "tie", "inconclusive"):
            raise ValueError("winner must include explicit uncertainty option")
    return {"run_id": run["run_id"], "case_id": run["case_id"], "status": result["status"]}


def template(case_id, run_id, root=ROOT):
    case = load_cases(root)[case_id]
    settings = {k: "" for k in SETTING_KEYS}
    return {
        "run_id": run_id,
        "case_id": case_id,
        "baseline": {"design_id": "baseline-v1", **settings},
        "variant": {"design_id": "artist-eye-v1", **settings},
        "changed_axis": case["axis"],
        "design_changes": [case["axis"]],
        "result": {"status": "IMAGE-PENDING", "scores": {}, "notes": "Await actual user-run images"},
    }


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", type=Path, default=ROOT)
    sub = p.add_subparsers(dest="command", required=True)
    sub.add_parser("validate")
    t = sub.add_parser("template")
    t.add_argument("--case", required=True, choices=sorted(SCOPES))
    t.add_argument("--run-id", required=True)
    s = sub.add_parser("record")
    s.add_argument("--file", type=Path, required=True)
    a = p.parse_args(argv)
    try:
        if a.command == "validate":
            cases = load_cases(a.root)
            folder = a.root / "data/visual-benchmarks/records"
            for path in folder.glob("*.json") if folder.exists() else []:
                validate_record(json.loads(path.read_text(encoding="utf-8")), a.root)
            print(f"Visual benchmark: {len(cases)} specs validated; image quality remains unverified")
        elif a.command == "template":
            print(json.dumps(template(a.case, a.run_id, a.root), ensure_ascii=False, indent=2))
        else:
            data = json.loads(a.file.read_text(encoding="utf-8"))
            result = validate_record(data, a.root)
            folder = a.root / "data/visual-benchmarks/records"
            folder.mkdir(parents=True, exist_ok=True)
            dest = folder / (result["run_id"] + ".json")
            if dest.exists():
                raise ValueError("run_id already exists; preserve original run")
            dest.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            print(json.dumps(result, ensure_ascii=False))
        return 0
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f"visual benchmark error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
