"""MOSS as a peer renderer: preserved Anima/NAI5, optional tag verification."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class MossModelRouteTests(unittest.TestCase):
    def test_config_has_separate_native_moss_pipelines(self):
        cfg = json.loads((ROOT / "harness.json").read_text(encoding="utf-8"))
        p = cfg["pipeline"]
        self.assertEqual(p["pipeline_packs"]["moss"],
                         ["visual-prompt-core", "moss-image-renderer"])
        self.assertEqual(p["pipeline_packs"]["moss-tags"],
                         ["visual-prompt-core", "danbooru-tag-gate", "moss-image-renderer"])
        self.assertIn("moss-image-renderer", p["adapters"])
        self.assertEqual(p["pipeline_packs"]["nai5"],
                         ["visual-prompt-core", "danbooru-tag-gate", "nai5-renderer"])
        self.assertEqual(p["pipeline_packs"]["anima"],
                         ["visual-prompt-core", "danbooru-tag-gate", "anima-renderer"])

    def test_moss_owns_serialization_but_not_creative_direction(self):
        renderer = (ROOT / "03_prompt/moss-image-renderer/SKILL.md").read_text(encoding="utf-8")
        core = (ROOT / "03_prompt/visual-prompt-core/SKILL.md").read_text(encoding="utf-8")
        router = (ROOT / "01_router/creative-skill-router/SKILL.md").read_text(encoding="utf-8")
        kernel = (ROOT / "kernel/KERNEL.md").read_text(encoding="utf-8")
        for piece in (router, core, kernel):
            self.assertIn("moss", piece.lower())
        for piece in ("Visual Prompt Packet", "Blueprint", "Caption", "Tags",
                      "Layout", "prompt only", "用户没说生成图片"):
            self.assertIn(piece.lower(), renderer.lower())
        self.assertIn("不强制", router)
        self.assertIn("no forced Danbooru fetch", (ROOT / "01_router/creative-skill-router/references/model-selection.md").read_text(encoding="utf-8"))

    def test_style_evidence_is_not_falsely_model_verified(self):
        s = (ROOT / "03_prompt/moss-image-renderer/references/style-control.md").read_text(encoding="utf-8")
        evidence = (ROOT / "03_prompt/moss-image-renderer/references/official-spec-and-sources.md").read_text(encoding="utf-8")
        for term in ("[Candidate]", "hand-drawn 2D anime", "photographic", "IMAGE-PENDING"):
            self.assertIn(term, s)
        for term in ("MOSS-Image-Base", "MOSS-Image-SFT", "USERGUIDE.md",
                     "abs_centralized", "yxyx", "3.0", "50"):
            self.assertIn(term, evidence)

    def test_readme_and_version(self):
        self.assertEqual((ROOT / "VERSION").read_text(encoding="utf-8").strip(), "5.2.0")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("MOSS Renderer", readme)
        self.assertIn("moss-tags", readme)
        self.assertIn("MOSS --> OUTPUT", readme)


if __name__ == "__main__":
    unittest.main()
