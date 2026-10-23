#!/usr/bin/env python3
"""Evidence-gated aesthetic scorebook. Computes numbers; never judges unseen art."""
import argparse
from decimal import Decimal, ROUND_HALF_UP
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
RECORDS = ROOT / "data/aesthetic-scores/records"
AXES = ("camera", "fashion", "interaction", "identity", "hierarchy",
        "light_color", "originality", "technical")
WEIGHTS = {
    "duo_fashion": (20, 20, 18, 10, 12, 8, 7, 5),
    "portrait": (18, 16, 8, 16, 14, 12, 10, 6),
    "cinematic": (24, 8, 18, 10, 14, 12, 10, 4),
    "concept_poster": (16, 0, 0, 8, 24, 18, 28, 6),
    "general": (20, 0, 0, 0, 25, 20, 27, 8),
}
CAPS = {"wrong_identity": 5.0, "brief_violation": 5.5,
        "unreadable_subject": 5.5, "crop_conflict": 6.5}
STAGES = ("SPEC", "IMAGE-REVIEWED")
ID_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{2,79}$")
FIELDS = {"assessment_id", "work_id", "version", "stage", "profile", "rater",
          "confidence", "axes", "hard_failures", "summary",
          "image_seen", "image_ref"}


def one_decimal(value):
    return float(Decimal(str(value)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))


def read_file(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def validate_entry(entry):
    if not isinstance(entry, dict) or set(entry) - FIELDS:
        raise ValueError("record must be an object with only supported fields")
    for key in ("assessment_id", "work_id", "version"):
        if not ID_PATTERN.fullmatch(str(entry.get(key, ""))):
            raise ValueError(f"{key}: use a stable public-safe ID (3-80 chars)")
    stage, profile = entry.get("stage"), entry.get("profile")
    if stage not in STAGES or profile not in WEIGHTS:
        raise ValueError("unsupported stage or profile")
    if entry.get("rater") not in ("assistant", "user"):
        raise ValueError("rater must be assistant or user")
    if entry.get("confidence") not in ("low", "medium", "high"):
        raise ValueError("confidence must be low, medium or high")
    if stage == "SPEC":
        if entry["confidence"] == "high" or entry.get("image_seen") is True or entry.get("image_ref"):
            raise ValueError("SPEC cannot claim an image or high evidence confidence")
    else:
        if entry.get("image_seen") is not True:
            raise ValueError("IMAGE-REVIEWED requires explicit image_seen=true")
        if not ID_PATTERN.fullmatch(str(entry.get("image_ref", ""))):
            raise ValueError("IMAGE-REVIEWED requires an opaque non-URL image_ref")
    if entry.get("summary") is not None and (not isinstance(entry["summary"], str)
                                              or len(entry["summary"]) > 400):
        raise ValueError("summary must be <=400 characters")
    failures = entry.get("hard_failures", [])
    if not isinstance(failures, list) or len(set(map(str, failures))) != len(failures):
        raise ValueError("hard_failures must be unique")
    if any(f not in CAPS for f in failures):
        raise ValueError("unknown hard failure")
    axes = entry.get("axes")
    required = {axis for axis, weight in zip(AXES, WEIGHTS[profile]) if weight}
    if not isinstance(axes, dict) or set(axes) != required:
        raise ValueError(f"axes must exactly match positive-weight keys: {sorted(required)}")
    for axis, rating in axes.items():
        if not isinstance(rating, dict) or set(rating) - {"score", "evidence", "issue"}:
            raise ValueError(f"{axis}: invalid axis structure")
        number = rating.get("score")
        if (type(number) not in (int, float) or not 0 <= number <= 10
                or float(number * 2).is_integer() is False):
            raise ValueError(f"{axis}: score must be 0..10 in 0.5 increments")
        evidence = rating.get("evidence")
        if not isinstance(evidence, str) or not 12 <= len(evidence.strip()) <= 400:
            raise ValueError(f"{axis}: provide 12..400 chars of concrete evidence")
        if "issue" in rating and (not isinstance(rating["issue"], str)
                                   or len(rating["issue"]) > 400):
            raise ValueError(f"{axis}: issue must be short")
    return entry


def score(entry):
    validate_entry(entry)
    raw = sum(Decimal(str(entry["axes"][axis]["score"])) * weight
              for axis, weight in zip(AXES, WEIGHTS[entry["profile"]])) / 100
    hard = entry.get("hard_failures", [])
    cap = min((Decimal(str(CAPS[f])) for f in hard), default=Decimal("10"))
    final = one_decimal(min(raw, cap))
    return {"assessment_id": entry["assessment_id"], "work_id": entry["work_id"],
            "version": entry["version"], "stage": entry["stage"],
            "profile": entry["profile"], "rater": entry["rater"],
            "confidence": entry["confidence"], "weighted_raw": one_decimal(raw),
            "total": final, "score_capped": raw > cap,
            "hard_failures": hard,
            "axis_scores": {a: entry["axes"][a]["score"] for a in entry["axes"]}}


def compare(before, after):
    a, b = score(before), score(after)
    for k in ("work_id", "stage", "profile", "rater"):
        if a[k] != b[k]:
            raise ValueError(f"incomparable reviews: {k} differs")
    if a["version"] == b["version"]:
        raise ValueError("comparison requires different versions")
    weights = dict(zip(AXES, WEIGHTS[a["profile"]]))
    changes = {}
    for axis in a["axis_scores"]:
        delta = b["axis_scores"][axis] - a["axis_scores"][axis]
        changes[axis] = {"delta": one_decimal(delta),
                         "weighted_contribution": one_decimal(delta * weights[axis] / 100)}
    return {"from_version": a["version"], "to_version": b["version"],
            "stage": a["stage"], "profile": a["profile"],
            "before": a["total"], "after": b["total"],
            "delta": one_decimal(b["total"] - a["total"]),
            "changes": changes,
            "note": "Descriptive difference, not controlled causal improvement."}


def calibrate(assistant, user):
    a, u = score(assistant), score(user)
    if (a["rater"], u["rater"]) != ("assistant", "user"):
        raise ValueError("calibration needs assistant vs user")
    for key in ("work_id", "version", "stage", "profile"):
        if a[key] != u[key]:
            raise ValueError(f"mismatched calibration pair: {key}")
    return {"work_id": a["work_id"], "version": a["version"],
            "stage": a["stage"], "profile": a["profile"],
            "assistant_total": a["total"], "user_total": u["total"],
            "assistant_minus_user": one_decimal(a["total"] - u["total"]),
            "note": "One pair only; review >=3 independent pairs before judging rating bias."}


def template(profile, stage, work_id, version):
    if not ID_PATTERN.fullmatch(work_id) or not ID_PATTERN.fullmatch(version):
        raise ValueError("invalid work-id or version")
    result = {"assessment_id": f"{work_id}-{version}-assistant-{stage.lower()}",
              "work_id": work_id, "version": version, "stage": stage,
              "profile": profile, "rater": "assistant", "confidence": "medium",
              "axes": {a: {"score": None, "evidence": ""}
                       for a, w in zip(AXES, WEIGHTS[profile]) if w},
              "hard_failures": [], "summary": ""}
    if stage == "IMAGE-REVIEWED":
        result["confidence"] = "low"
        result["image_seen"] = False
        result["image_ref"] = ""
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    t = sub.add_parser("template")
    t.add_argument("--profile", choices=WEIGHTS.keys(), required=True)
    t.add_argument("--stage", choices=STAGES, required=True)
    t.add_argument("--work-id", required=True)
    t.add_argument("--version", required=True)
    for action in ("score", "record"):
        c = sub.add_parser(action)
        c.add_argument("--file", type=Path, required=True)
    cmp_ = sub.add_parser("compare")
    cmp_.add_argument("--before", type=Path, required=True)
    cmp_.add_argument("--after", type=Path, required=True)
    cal = sub.add_parser("calibrate")
    cal.add_argument("--assistant", type=Path, required=True)
    cal.add_argument("--user", type=Path, required=True)
    sub.add_parser("validate")
    args = parser.parse_args(argv)
    try:
        if args.action == "template":
            result = template(args.profile, args.stage, args.work_id, args.version)
        elif args.action == "score":
            result = score(read_file(args.file))
        elif args.action == "compare":
            result = compare(read_file(args.before), read_file(args.after))
        elif args.action == "calibrate":
            result = calibrate(read_file(args.assistant), read_file(args.user))
        elif args.action == "record":
            data = read_file(args.file)
            result = score(data)
            RECORDS.mkdir(parents=True, exist_ok=True)
            dest = RECORDS / (data["assessment_id"] + ".json")
            if dest.exists():
                raise ValueError("assessment_id already exists; never overwrite a rating")
            dest.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n",
                            encoding="utf-8")
            result["saved_as"] = str(dest.relative_to(ROOT))
        else:
            names = set()
            for p in sorted(RECORDS.glob("*.json")) if RECORDS.exists() else []:
                data = read_file(p)
                score(data)
                if data["assessment_id"] in names:
                    raise ValueError("duplicate assessment_id in records")
                names.add(data["assessment_id"])
            result = {"validated_records": len(names),
                      "note": "No image quality was automatically assessed."}
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ValueError, TypeError, OSError, KeyError, json.JSONDecodeError) as exc:
        print(f"aesthetic score error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
