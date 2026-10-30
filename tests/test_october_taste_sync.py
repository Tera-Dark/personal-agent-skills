"""October 14–15 user taste/NAI5 defaults sync smoke tests.

These test documentation contracts, not the quality of images or NAI5 generation.
"""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
IDENTITY = ROOT / "00_core/personal-identity-profile/references"
DIRECTOR = ROOT / "02_design/illustration-direction/SKILL.md"
SMALL_ARTIST = ROOT / "02_design/small-artist-brain/SKILL.md"
RENDERER = ROOT / "03_prompt/nai5-renderer/SKILL.md"


class OctoberTasteSync(unittest.TestCase):
    def test_current_output_policy_is_explicit(self):
        core = (IDENTITY / "taste-core.md").read_text(encoding="utf-8")
        renderer = RENDERER.read_text(encoding="utf-8")
        self.assertIn("2026-10-15", core)
        self.assertIn("默认只交付提示词", core)
        self.assertIn("画师串和质量词已在界面固定", core)
        self.assertIn("externally", renderer)
        self.assertIn("year", renderer)
        self.assertIn("one copyable code block", renderer)
        self.assertIn("unless expressly requested", renderer)

    def test_evidence_not_overpromoted(self):
        ledger = (IDENTITY / "feedback-ledger.md").read_text(encoding="utf-8")
        summary = (IDENTITY / "session-feedback-2026-10-14-15.md").read_text(encoding="utf-8")
        signature = (IDENTITY / "taste-signature.md").read_text(encoding="utf-8")
        for k in ("FB-20261015-01", "FB-20261015-02", "FB-20261015-07"):
            self.assertIn(k, ledger)
        self.assertIn("不是模型自动学习结果", summary)
        self.assertIn("没有明确图生成功效记录", summary)
        self.assertIn("不把评分等同", ledger)
        self.assertIn("session-feedback-2026-10-14-15.md", signature)

    def test_design_boundaries_and_subject_safety(self):
        director = DIRECTOR.read_text(encoding="utf-8")
        small = SMALL_ARTIST.read_text(encoding="utf-8")
        for term in ("双格人物面部", "矿物/水墨淡入", "人物传", "同人"):
            self.assertIn(term, director)
        self.assertIn("铃兰", small)
        self.assertIn("不授权通用模式每张图加樱花", small)
        self.assertIn("活人互动", small)

    def test_current_version(self):
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        self.assertRegex(version, r"^\d+\.\d+\.\d+$")
        self.assertIn(f"## [{version}]", (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
