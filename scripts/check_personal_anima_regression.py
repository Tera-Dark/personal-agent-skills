#!/usr/bin/env python3
"""
Deterministic P12 contract checks.

This checker is deliberately offline. It never fetches the Good Anima corpus and
never pretends to judge visual quality. Live-index and image-output cases remain
manual in tests/personal-anima-regression.md.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def main() -> int:
    failures: list[str] = []
    cfg = json.loads(read("harness.json"))
    version = read("VERSION").strip()
    matrix = read("tests/personal-anima-regression.md")

    expected_pack = [
        "anima-tag-gate",
        "anima-tag-classifier",
        "anima-prompt-skeleton",
        "anima-aesthetic-protection",
        "anima-prompt-compressor",
        "anima-tag-serializer",
        "anima-prompt-compiler",
    ]
    require(
        cfg["pipeline"]["pipeline_packs"].get("anima") == expected_pack,
        "Anima pipeline order changed",
        failures,
    )

    failure = cfg["failure_policy"]
    require(failure.get("default_mode") == "fail_closed", "failure policy is not fail_closed", failures)
    require(
        failure["standalone_module"].get("on_fetch_failure") == "card_only",
        "standalone failure state is not card_only",
        failures,
    )
    require(
        failure["pipeline_pack"].get("on_fetch_failure") == "pipeline_unavailable",
        "pipeline failure state is not pipeline_unavailable",
        failures,
    )
    require(
        failure["anima_tag_index"].get("on_fetch_failure") == "unverified_to_nl",
        "tag-index failure state is not unverified_to_nl",
        failures,
    )
    require(
        failure["anima_tag_index"].get("hard_tags_allowed") is False,
        "tag-index degradation permits hard_tags",
        failures,
    )
    require(
        failure["anima_tag_index"].get("fuzzy_promotion") is False,
        "tag-index degradation permits fuzzy promotion",
        failures,
    )
    for scope in ("standalone_module", "pipeline_pack", "anima_tag_index"):
        require(
            failure[scope].get("memory_substitution") is False,
            f"{scope} allows memory substitution",
            failures,
        )

    sources = {
        "gate": read("02_creation/anima-tag-gate/SKILL.md"),
        "classifier": read("02_creation/anima-tag-classifier/SKILL.md"),
        "skeleton": read("02_creation/anima-prompt-skeleton/SKILL.md"),
        "compressor": read("02_creation/anima-prompt-compressor/SKILL.md"),
        "serializer": read("02_creation/anima-tag-serializer/SKILL.md"),
        "protection": read("02_creation/anima-aesthetic-protection/SKILL.md"),
        "compiler": read("02_creation/anima-prompt-compiler/SKILL.md"),
        "router": read("01_router/creative-skill-router/SKILL.md"),
        "kernel": read("kernel/KERNEL.md"),
    }

    for needle in ("exact", "alias", "missing", "fuzzy", "hard_tags", "tag-index-unavailable", "37_(reverse:1999)"):
        require(needle in sources["gate"], f"Tag Gate lost contract token: {needle}", failures)

    for needle in ("identity_scope", "artist", "character", "series", "appearance", "clothing", "action", "prompt_role"):
        require(needle in sources["classifier"], f"Classifier lost contract token: {needle}", failures)

    for needle in ("hard_tags → Tag block", "nltags_block → Natural-language block", "garment hierarchy and overlap", "pose causality", "asymmetry distribution"):
        require(needle in sources["skeleton"], f"Skeleton lost relation contract: {needle}", failures)

    for needle in ("Tier A", "Tier B", "Tier C", "smallest prompt", "identity", "punctum"):
        require(needle.lower() in sources["compressor"].lower(), f"Compressor lost contract token: {needle}", failures)

    for needle in ("canonical_tag", "serialized_tag", "37\\(reverse1999\\)", "idempot"):
        require(needle in sources["serializer"], f"Serializer lost contract token: {needle}", failures)

    for needle in ("not an aesthetic generator", "design-drift", "asymmetry", "quiet field", "punctum"):
        require(needle.lower() in sources["protection"].lower(), f"Protection lost contract token: {needle}", failures)

    for needle in ("Blueprint Gate", "Failure boundary", "37\\(reverse1999\\)"):
        require(needle.lower() in sources["compiler"].lower(), f"Compiler lost boundary token: {needle}", failures)

    require(
        "pipeline pack" in sources["router"].lower() or "pipeline_packs.anima" in sources["router"],
        "Router no longer names the Anima pipeline pack",
        failures,
    )
    for needle in ("card-only", "pipeline-unavailable", "tag-index-unavailable", "memory", "silent"):
        require(needle.lower() in sources["kernel"].lower(), f"Kernel lost failure guard: {needle}", failures)

    case_ids = re.findall(r"^### (P12-[A-Z]+-\d{2})\s+—", matrix, re.M)
    expected_prefixes = {
        "TAG": 10, "SYN": 4, "SKL": 2, "CMP": 3, "PRT": 3,
        "FLR": 4, "WEB": 4, "REAL": 6,
    }
    for prefix, expected_count in expected_prefixes.items():
        actual = len([x for x in case_ids if x.startswith(f"P12-{prefix}-")])
        require(
            actual == expected_count,
            f"matrix count for {prefix}: expected {expected_count}, got {actual}",
            failures,
        )
    require(len(case_ids) == 36, f"expected 36 P12 cases, found {len(case_ids)}", failures)
    require(version == "3.6.0", f"VERSION must be 3.6.0, found {version}", failures)

    if failures:
        print("P12 regression contract: FAIL")
        for item in failures:
            print(f"  ERROR {item}")
        return 1

    print(f"P12 regression contract: PASS — {len(case_ids)} matrix cases, version {version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
