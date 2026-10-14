"""Regression tests for the on-demand Yu de Kuluopai photography decision lens.

These structural tests verify owner boundaries and reference availability only.
They are not image-generation quality measurements.
"""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PHOTOGRAPHY = ROOT / "02_design" / "yu-de-kuluopai-photography-brain"
SKILL = PHOTOGRAPHY / "SKILL.md"


class PhotographySkillContracts(unittest.TestCase):
    def test_module_exists_and_is_on_demand(self):
        text = SKILL.read_text(encoding="utf-8")
        self.assertIn("name: yu-de-kuluopai-photography-brain", text)
        self.assertIn('layer: "02_design"', text)
        self.assertIn('load: "on-demand"', text)
        self.assertIn("鱼的库洛牌", text)
        self.assertIn("Photography Decision Sheet", text)

    def test_reference_studies_and_attribution(self):
        body = SKILL.read_text(encoding="utf-8")
        study = PHOTOGRAPHY / "references/nine-frame-study-2026-10-14.md"
        transfer = PHOTOGRAPHY / "references/cross-genre-camera-recipes.md"
        self.assertTrue(study.is_file())
        self.assertTrue(transfer.is_file())
        for ref in (study, transfer):
            self.assertIn(ref.name, body)
        notes = study.read_text(encoding="utf-8")
        for num in range(1, 10):
            self.assertIn(f"## {num:02d} ·", notes)
        self.assertIn("未对原创作者身份", notes)

    def test_handoff_and_renderer_boundaries(self):
        lens = SKILL.read_text(encoding="utf-8")
        router = (ROOT / "01_router/creative-skill-router/SKILL.md").read_text(encoding="utf-8")
        director = (ROOT / "02_design/illustration-direction/SKILL.md").read_text(encoding="utf-8")
        for needle in ("viewer_position", "nearest_visible", "contact_points",
                       "background_visible", "light", "do_not_import"):
            self.assertIn(needle, lens)
        self.assertIn("yu-de-kuluopai-photography-brain", router)
        self.assertIn("yu-de-kuluopai-photography-brain", director)
        self.assertIn("visual-prompt-core", lens)
        self.assertIn("nai5-renderer", lens)
        self.assertIn("不擅自生图", lens)


if __name__ == "__main__":
    unittest.main()
