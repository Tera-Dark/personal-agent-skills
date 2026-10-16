#!/usr/bin/env python3
"""Compile an editable top-left pixel draft into MOSS-Image's native prompt.

MOSS-Image accepted Layout: summary/items + centered yxyx coordinates.
This standalone standard-library helper never generates images.
Spec: https://github.com/OpenMOSS/MOSS-Image/blob/main/skills/moss-image-prompt-enhancer/references/layout.md
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import sys


def require(ok, why):
    if not ok:
        raise ValueError(why)


def keys(obj, allowed, required, label):
    require(isinstance(obj, dict), f"{label} must be a JSON object")
    unknown = set(obj) - set(allowed)
    missing = set(required) - set(obj)
    require(not unknown and not missing,
            f"{label} has unknown {sorted(unknown)} or missing {sorted(missing)} fields")


def nonempty(s, label):
    require(isinstance(s, str) and bool(s.strip()), f"{label} must be nonempty text")


def string_list(value, label):
    require(isinstance(value, list) and all(isinstance(x, str) and x.strip() for x in value),
            f"{label} must be a list of nonempty strings")


def bbox_to_native(bbox, width, height):
    require(isinstance(bbox, list) and len(bbox) == 4, "bbox must contain x1,y1,x2,y2")
    require(all(type(v) in (int, float) and math.isfinite(v) for v in bbox),
            "bbox values must be finite numbers")
    x1, y1, x2, y2 = bbox
    require(0 <= x1 < x2 <= width and 0 <= y1 < y2 <= height,
            "bbox must have positive area inside the canvas")
    # Contain fractional bbox within whole pixels before converting; never clip.
    y_min = math.floor(y1) - height // 2
    x_min = math.floor(x1) - width // 2
    y_max = math.ceil(y2) - height // 2
    x_max = math.ceil(x2) - width // 2
    return [y_min, x_min, y_max, x_max]


def compile_draft(draft):
    require(isinstance(draft, dict), "input must be JSON object")
    if "caption" in draft:
        keys(draft, {"caption"}, {"caption"}, "caption draft")
        nonempty(draft["caption"], "caption")
        return draft["caption"]

    root = {"width", "height", "bbox_coord_space", "bbox_format", "summary", "items"}
    keys(draft, root, root, "layout draft")
    w, h = draft["width"], draft["height"]
    for name, n in (("width", w), ("height", h)):
        require(type(n) is int and n > 0 and n % 16 == 0,
                f"{name} must be a positive multiple of 16")
    require(draft["bbox_coord_space"] == "abs" and draft["bbox_format"] == "xyxy",
            "editable draft must use abs/xyxy; native model already uses abs_centralized/yxyx")
    sm = draft["summary"]
    keys(sm, {"caption", "meta", "canvas", "palette"}, {"caption"}, "summary")
    nonempty(sm["caption"], "summary.caption")
    if "canvas" in sm:
        require(sm["canvas"] in {"single", "multi_panel", "collage"},
                "canvas must be single/multi_panel/collage")
    for k in ("meta", "palette"):
        if k in sm:
            string_list(sm[k], f"summary.{k}")

    items = draft["items"]
    require(isinstance(items, list) and len(items) > 0, "items must be nonempty flat array")
    formatted = []
    for i, item in enumerate(items):
        label = f"items[{i}]"
        keys(item, {"label", "caption", "bbox", "text", "tags", "palette"},
             {"label", "caption", "bbox"}, label)
        require(item["label"] in {"character", "object", "text"},
                f"{label}.label must be character/object/text")
        nonempty(item["caption"], f"{label}.caption")
        if item["label"] == "text":
            require("text" in item, f"{label} text item missing text")
        elif "text" in item:
            raise ValueError(f"{label} text field only allowed for text items")
        if "text" in item:
            nonempty(item["text"], f"{label}.text")
        for k in ("tags", "palette"):
            if k in item:
                string_list(item[k], f"{label}.{k}")
        formatted.append({
            **{k: v for k, v in item.items() if k != "bbox"},
            "bbox": bbox_to_native(item["bbox"], w, h),
        })
    native = {"summary": sm, "items": formatted,
              "bbox_coord_space": "abs_centralized", "bbox_format": "yxyx"}
    return json.dumps(native, ensure_ascii=False, separators=(",", ":"), allow_nan=False)


def unique_pairs(pairs):
    result = {}
    for k, v in pairs:
        require(k not in result, f"duplicate JSON key: {k}")
        result[k] = v
    return result


def reject_nonfinite(value):
    raise ValueError(f"invalid JSON numeric constant: {value}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("draft", type=Path, help="UTF-8 caption or layout draft JSON")
    parser.add_argument("--output", type=Path, help="separate output prompt file")
    args = parser.parse_args(argv)
    try:
        if args.output:
            require(args.draft.resolve() != args.output.resolve(), "never overwrite the editable draft")
        draft = json.loads(args.draft.read_text(encoding="utf-8"),
                           object_pairs_hook=unique_pairs, parse_constant=reject_nonfinite)
        prompt = compile_draft(draft)
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(prompt + "\n", encoding="utf-8")
            print(f"Compiled prompt saved: {args.output}", file=sys.stderr)
        else:
            print(prompt)
        return 0
    except (OSError, ValueError) as exc:
        print(f"moss layout error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
