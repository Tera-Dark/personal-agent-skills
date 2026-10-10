#!/usr/bin/env python3
"""Deterministic behavioral contract regressions; visual aesthetics need manual review."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return (ROOT / path).read_text(encoding="utf-8")

def require(ok, reason):
    if not ok:
        raise AssertionError(reason)

def main():
    kernel = read("kernel/KERNEL.md")
    router = read("01_router/creative-skill-router/SKILL.md")
    taste = read("00_core/personal-identity-profile/references/taste-core.md")
    director = read("00_core/aesthetic-director-core/SKILL.md")
    character = read("02_design/character-design-engine/SKILL.md")
    illustration = read("02_design/illustration-direction/SKILL.md")
    generic = read("03_prompt/general-image-prompt-adapter/SKILL.md")
    nai5 = read("03_prompt/nai5-renderer/SKILL.md")
    anima = read("03_prompt/anima-renderer/SKILL.md")
    harness = read("bundle/HARNESS.md")
    manifest = json.loads(read("bundle/manifest.json"))
    config = json.loads(read("harness.json"))

    for token in (
        "Image-generation permission", "do not authorize image generation",
        "PROMPT ONLY", "FAST VARIANT", "FULL CREATIVE", "Visual Prompt Packet",
        "danbooru-tag-gate", "No unsolicited image generation",
    ):
        require(token.lower() in kernel.lower(), f"Kernel lacks: {token}")
    for token in ("Image-generation permission", "PROMPT ONLY", "请给我生成一张图片"):
        require(token in harness, f"Runtime lacks: {token}")
    require("默认只交付提示词文本" in taste, "owner prompt-first rule disappeared")
    require("省略常备 artist stack" in taste, "fixed NAI5 stack no longer external")
    require("不展示内部候选" in director, "Director leaks rejected candidates")
    require("仅交付可复制 Prompt" in router, "Router leaks Creative Brief")
    require(router.count("## References") == 1, "Router has duplicate reference headings")
    require(illustration.count("## References") == 1, "Illustration has duplicate references")
    require("illustration-direction" in character, "character/illustration ownership bridge lost")
    require("Visual Prompt Packet" in generic, "generic renderer bypasses shared core")
    require("Negative is omitted by default" in nai5, "NAI5 negative default lost")
    require("only verified" in anima.lower(), "Anima verified tag contract lost")

    require(manifest["version"] == read("VERSION").strip(), "manifest version mismatch")
    require(manifest["core_tokens"] <= config["core_budget_tokens"], "core budget exceeded")
    require(manifest["core_tokens"] < 10279, "cold start not lighter than v4.5 baseline")
    for name, adapter in (("nai5", "nai5-renderer"), ("anima", "anima-renderer")):
        require(
            config["pipeline"]["pipeline_packs"][name]
            == ["visual-prompt-core", "danbooru-tag-gate", adapter],
            f"{name} shared pipeline changed",
        )
    print(
        f"Output contract regression: PASS; core {manifest['core_tokens']} / "
        f"{config['core_budget_tokens']} tokens"
    )

if __name__ == "__main__":
    main()
