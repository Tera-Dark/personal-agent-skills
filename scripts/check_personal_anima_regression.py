#!/usr/bin/env python3
"""
Deterministic prompt-architecture regression checks.

The visual quality cases remain manual. This checker verifies that the v4
shared prompt architecture still preserves the critical Anima / NAI5 contracts:
shared Visual Prompt Core, shared Danbooru verification, thin renderers,
fail-closed behavior, and the existing P12/P13/P14 regression matrix.
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

    expected_anima = [
        "visual-prompt-core",
        "danbooru-tag-gate",
        "anima-renderer",
    ]
    expected_nai5 = [
        "visual-prompt-core",
        "danbooru-tag-gate",
        "nai5-renderer",
    ]

    require(
        cfg["pipeline"]["pipeline_packs"].get("anima") == expected_anima,
        "Anima pipeline pack changed",
        failures,
    )
    require(
        cfg["pipeline"]["pipeline_packs"].get("nai5") == expected_nai5,
        "NAI5 pipeline pack changed",
        failures,
    )
    require(
        cfg["pipeline"].get("prompt_core") == "visual-prompt-core",
        "shared prompt core is not registered",
        failures,
    )
    require(
        cfg["pipeline"].get("danbooru_tag_gate") == "danbooru-tag-gate",
        "shared Danbooru gate is not registered",
        failures,
    )

    require(
        cfg["always_on"].keys() == {"personal-identity-profile", "creative-skill-router"},
        "always-on scope drifted; only identity + router should be session-wide",
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
        failure["danbooru_tag_index"].get("on_fetch_failure") == "unverified_to_nl",
        "Danbooru failure state is not unverified_to_nl",
        failures,
    )
    require(
        failure["danbooru_tag_index"].get("hard_tags_allowed") is False,
        "Danbooru degradation permits hard_tags",
        failures,
    )
    require(
        failure["danbooru_tag_index"].get("fuzzy_promotion") is False,
        "Danbooru degradation permits fuzzy promotion",
        failures,
    )
    for scope in ("standalone_module", "pipeline_pack", "danbooru_tag_index"):
        require(
            failure[scope].get("memory_substitution") is False,
            f"{scope} allows memory substitution",
            failures,
        )

    sources = {
        "core": read("03_prompt/visual-prompt-core/SKILL.md"),
        "gate": read("03_prompt/danbooru-tag-gate/SKILL.md"),
        "anima": read("03_prompt/anima-renderer/SKILL.md"),
        "nai5": read("03_prompt/nai5-renderer/SKILL.md"),
        "router": read("01_router/creative-skill-router/SKILL.md"),
        "kernel": read("kernel/KERNEL.md"),
    }

    for needle in (
        "Visual Prompt Packet",
        "style:",
        "subject:",
        "composition:",
        "relations:",
        "tag_candidates:",
        "Compression",
        "Design Lock",
        "output_policy:",
    ):
        require(needle.lower() in sources["core"].lower(), f"Prompt Core lost contract token: {needle}", failures)

    for needle in (
        "exact",
        "alias",
        "missing",
        "fuzzy",
        "hard tag",
        "fail-closed",
    ):
        require(needle.lower() in sources["gate"].lower(), f"Danbooru Gate lost contract token: {needle}", failures)

    for needle in (
        "Tag block",
        "Natural Language",
        "37_(reverse:1999)",
        "does not design",
    ):
        require(needle.lower() in sources["anima"].lower(), f"Anima renderer lost contract token: {needle}", failures)
    require("37\\\\(reverse1999\\\\)" in sources["anima"], "Anima renderer lost exact escaped 37 token", failures)

    for needle in (
        "artist:",
        "weight",
        "char1",
        "source#",
        "target#",
        "mutual#",
        "does not design",
    ):
        require(needle.lower() in sources["nai5"].lower(), f"NAI5 renderer lost contract token: {needle}", failures)

    for needle in (
        "visual-prompt-core",
        "danbooru-tag-gate",
        "anima-renderer",
        "nai5-renderer",
    ):
        require(needle.lower() in sources["router"].lower(), f"Router lost shared prompt route: {needle}", failures)

    for needle in (
        "Visual Prompt Packet",
        "renderer",
        "card-only",
        "pipeline-unavailable",
        "tag-index-unavailable",
        "memory",
    ):
        require(needle.lower() in sources["kernel"].lower(), f"Kernel lost architecture/failure guard: {needle}", failures)

    case_ids = re.findall(r"^### (P12-[A-Z]+(?:-[A-Z]+)*-\d{2})\s+—", matrix, re.M)
    expected_prefixes = {
        "TAG": 10, "SYN": 4, "SKL": 2, "CMP": 3, "PRT": 3,
        "FLR": 4, "WEB": 11, "REAL": 6,
    }
    for prefix, expected_count in expected_prefixes.items():
        actual = len([x for x in case_ids if x.startswith(f"P12-{prefix}-")])
        require(
            actual == expected_count,
            f"matrix count for {prefix}: expected {expected_count}, got {actual}",
            failures,
        )
    require(len(set(case_ids)) == len(case_ids), "duplicate P12 case IDs detected", failures)
    require(len(case_ids) == 43, f"expected 43 P12 cases, found {len(case_ids)}", failures)
    version_parts = version.split(".")
    require(
        len(version_parts) == 3 and all(part.isdigit() for part in version_parts),
        f"VERSION must follow semantic x.y.z format, found {version}",
        failures,
    )

    p13 = read("tests/p13-real-task-regression.md")
    p13_cases = re.findall(r"^### (P13-(?:\d{2}|X-\d{2}))\s+—", p13, re.M)
    expected_p13 = [
        "P13-01", "P13-02", "P13-03", "P13-04",
        "P13-05", "P13-06", "P13-07", "P13-08",
        "P13-X-01", "P13-X-02", "P13-X-03", "P13-X-04",
        "P13-X-05", "P13-X-06", "P13-X-07", "P13-X-08",
    ]
    require(p13_cases == expected_p13, "P13 case IDs or order changed", failures)
    for needle in (
        "modern gacha",
        "white-background",
        "high-fashion",
        "punctum",
        "local density",
        "reference-to-original",
        "prompt compression",
        "design survives adapter",
    ):
        require(needle.lower() in p13.lower(), f"P13 matrix lost required regression concept: {needle}", failures)

    # Preserve current owner-specific prompt defaults and artist blacklist.
    director = read("00_core/aesthetic-director-core/SKILL.md")
    require(
        "普通 NAI5 设计请求不重复已经预设的 artist stack 与质量层" in director,
        "ordinary NAI5 prompts may duplicate the owner's fixed artist/quality layer",
        failures,
    )
    identity_pool = read("00_core/personal-identity-profile/references/nai5-artist-pool.md")
    for needle in (
        "Any artist tag ending with a digit is blacklisted by default.",
        "artist:yellowshark601",
        "artist:mihiro_00122",
        "artist:vlfdus_0",
        "artist:zishengtian123",
        "blacklisted artists must never be emitted into new artist stacks",
    ):
        require(needle in identity_pool, f"personal artist blacklist lost required rule/example: {needle}", failures)

    default_stack_heading = "## 1.1 Current standby small-artist stack"
    require(default_stack_heading in identity_pool, "current standby artist stack section is missing", failures)
    if default_stack_heading in identity_pool:
        stack_tail = identity_pool.split(default_stack_heading, 1)[1]
        stack_lines = []
        for line in stack_tail.splitlines():
            if line.startswith("## "):
                break
            if "::artist:" in line:
                stack_lines.append(line)
        default_artists = re.findall(r"artist:([^,]+?)::", "\\n".join(stack_lines))
        require(bool(default_artists), "could not parse the current standby artist stack", failures)
        for artist in default_artists:
            require(
                not artist[-1:].isdigit(),
                f"default standby artist stack contains a digit-suffixed blacklisted artist: {artist}",
                failures,
            )

    painterly_grammar = read("00_core/aesthetic-director-core/references/ruoganzhao-composition-color-grammar.md")
    aesthetic_director = read("00_core/aesthetic-director-core/SKILL.md")
    calibration_library = read("00_core/aesthetic-director-core/references/high-aesthetic-calibration-library.md")
    require(
        "references/ruoganzhao-composition-color-grammar.md" in aesthetic_director,
        "Aesthetic Director does not route to the painterly game-illustration calibration",
        failures,
    )
    require(
        "## 14. Study calibration — painterly light-rich game illustration" in calibration_library,
        "High-Aesthetic Calibration Library lost the painterly game-illustration study",
        failures,
    )
    for needle in (
        "Light as a connector",
        "Effective and ineffective information",
        "color",
        "movement",
        "do not force teal-orange palettes",
    ):
        require(needle.lower() in painterly_grammar.lower(), f"Painterly illustration calibration lost required rule: {needle}", failures)
    pool_check = read("00_core/personal-identity-profile/references/nai5-artist-pool.md")
    require("ruoganzhao-composition-color-grammar.md" in pool_check, "ruoganzhao personal profile is not linked to the new calibration", failures)

    p14 = read("tests/test-suite.md")
    for needle in (
        "P14 — Aesthetic Floor Regression",
        "怪 ≠ 丑",
        "第一眼美感",
        "丑的很有特点",
    ):
        require(needle.lower() in p14.lower(), f"P14 regression contract lost required concept: {needle}", failures)

    if failures:
        print("Prompt architecture regression contract: FAIL")
        for item in failures:
            print(f"  ERROR {item}")
        return 1

    print(f"Prompt architecture regression contract: PASS — {len(case_ids)} P12 cases + 16 P13 cases, version {version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
