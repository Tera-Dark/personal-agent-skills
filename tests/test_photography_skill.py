"""Structural checks for the generic Japanese cinematic composition lens.

These verify module ownership, evidence provenance, and routing. They do not
measure image-generation quality or endorse copying any photographer.
"""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
CINEMATIC = ROOT / "02_design" / "japanese-cinematic-composition"
SKILL = CINEMATIC / "SKILL.md"


class CinematicCompositionContracts(unittest.TestCase):
    def test_module_exists_and_is_on_demand(self):
        body = SKILL.read_text(encoding="utf-8")
        self.assertIn("name: japanese-cinematic-composition", body)
        self.assertIn('layer: "02_design"', body)
        self.assertIn('load: "on-demand"', body)
        self.assertIn("日系电影感构图", body)
        self.assertIn("Photography Decision Sheet", body)

    def test_reference_studies_and_provenance(self):
        body = SKILL.read_text(encoding="utf-8")
        nine = CINEMATIC / "references/nine-frame-study-2026-10-14.md"
        thirteen = CINEMATIC / "references/thirteen-frame-study-2026-10-15.md"
        transfer = CINEMATIC / "references/cross-genre-camera-recipes.md"
        for file in (nine, thirteen, transfer):
            self.assertTrue(file.is_file(), file)
            self.assertIn(file.name, body)
        for n in range(1, 10):
            self.assertIn(f"## {n:02d} ·", nine.read_text(encoding="utf-8"))
        for n in range(1, 14):
            self.assertIn(f"## {n:02d} ·", thirteen.read_text(encoding="utf-8"))
        self.assertIn("未对原创作者身份", nine.read_text(encoding="utf-8"))
        self.assertIn("02 与 09", thirteen.read_text(encoding="utf-8"))
        self.assertIn("没有对每一幅具体图的作者做独立验证", thirteen.read_text(encoding="utf-8"))

    def test_handoff_and_renderer_boundaries(self):
        body = SKILL.read_text(encoding="utf-8")
        router = (ROOT / "01_router/creative-skill-router/SKILL.md").read_text(encoding="utf-8")
        director = (ROOT / "02_design/illustration-direction/SKILL.md").read_text(encoding="utf-8")
        for key in ("viewer_position", "nearest_visible", "contact_points",
                    "background_visible", "light", "do_not_import"):
            self.assertIn(key, body)
        for contract in (router, director):
            self.assertIn("japanese-cinematic-composition", contract)
        for key in ("visual-prompt-core", "nai5-renderer", "不擅自生图"):
            self.assertIn(key, body)

    def test_decision_matrix_and_no_personal_style_tags(self):
        body = SKILL.read_text(encoding="utf-8")
        matrix = (CINEMATIC / "references/camera-decision-matrix.md").read_text(encoding="utf-8")
        for key in ("Contact", "Following", "Observing", "Threshold",
                    "Opposed attention", "NAI5", "参考渗漏", "叙事距离"):
            self.assertIn(key, matrix)
        for key in ("relationship_axis", "narrative_distance",
                    "sequence_mode", "shot_scale_tradeoff"):
            self.assertIn(key, body)
        self.assertIn("不按个人摄影师或账号命名风格", body)
        self.assertIn("不能误当", body)
        self.assertIn("canon identity/outfit", matrix)

    def test_old_named_reference_is_absent_from_all_source_docs(self):
        old_chinese_name = "鱼的" + "库洛牌"
        old_slug = "yu-de-" + "kuluopai"
        tracked = [
            ROOT / "README.md",
            ROOT / "01_router/creative-skill-router/SKILL.md",
            ROOT / "02_design/illustration-direction/SKILL.md",
            ROOT / "00_core/personal-identity-profile/references/session-feedback-2026-10-14-15.md",
            ROOT / "00_core/personal-identity-profile/references/feedback-ledger.md",
            *CINEMATIC.rglob("*.md"),
        ]
        for path in tracked:
            with self.subTest(path=str(path.relative_to(ROOT))):
                text = path.read_text(encoding="utf-8")
                self.assertNotIn(old_chinese_name, text)
                self.assertNotIn(old_slug, text)
        self.assertFalse((ROOT / "02_design" / (old_slug + "-photography-brain")).exists())


if __name__ == "__main__":
    unittest.main()
