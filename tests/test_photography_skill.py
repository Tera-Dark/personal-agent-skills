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

    def test_second_wave_and_decision_matrix(self):
        lens = SKILL.read_text(encoding="utf-8")
        study = PHOTOGRAPHY / "references/thirteen-frame-study-2026-10-15.md"
        matrix = PHOTOGRAPHY / "references/camera-decision-matrix.md"
        self.assertTrue(study.is_file())
        self.assertTrue(matrix.is_file())
        for ref in (study, matrix):
            self.assertIn(ref.name, lens)
        notes = study.read_text(encoding="utf-8")
        for n in range(1, 14):
            self.assertIn(f"## {n:02d} ·", notes)
        self.assertIn("02 与 09", notes)  # repeats cannot count as independent evidence
        self.assertIn("没有对每一幅具体图的作者做独立验证", notes)
        methods = matrix.read_text(encoding="utf-8")
        for k in ("Contact", "Following", "Observing", "Threshold",
                  "Opposed attention", "NAI5", "参考渗漏", "叙事距离"):
            self.assertIn(k, methods)
        for k in ("relationship_axis", "narrative_distance", "sequence_mode",
                  "shot_scale_tradeoff", "fish's kuro card style"):
            self.assertIn(k, lens)

    def test_no_photography_shortcuts_in_renderer(self):
        # This module only suggests geometry and must not rewrite an IP or
        # claim its photographer's name is an officially supported style tag.
        lens = SKILL.read_text(encoding="utf-8")
        matrix = (PHOTOGRAPHY / "references/camera-decision-matrix.md").read_text(encoding="utf-8")
        self.assertIn("renderer", lens)
        self.assertIn("不能误当", lens)
        self.assertIn("canon identity/outfit", matrix)
        self.assertIn("不把摄影博主名字", matrix)


if __name__ == "__main__":
    unittest.main()
