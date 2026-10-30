"""Verify routing and preservation contracts; does not judge visual quality."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build


class CompositionTasteHandoffTests(unittest.TestCase):
    def test_named_aesthetic_is_not_skipped_by_l2(self):
        _, _, outputs = build.build_outputs(str(ROOT))
        core = outputs["bundle/HARNESS.md"]
        self.assertIn("composition-quick-card.md", core)
        self.assertIn("asks to read the full module", core)
        self.assertIn("Other explicitly requested aesthetics load their named module", core)
        self.assertIn("Never claim a file or image was read if it was not", core)
        self.assertIn("FAST VARIANT changes only the named dimension", core)
        named = outputs["bundle/modules/small-artist-brain.md"]
        self.assertIn("zheng-transferable-grammar.md", named)
        self.assertIn("bundle/references/small-artist-brain/references/zheng-transferable-grammar.md", named)
        card_path = "bundle/references/small-artist-brain/references/composition-quick-card.md"
        self.assertIn(card_path, outputs)
        self.assertIn("不得声称已读完整模块", outputs[card_path])

    def test_composition_survives_prompt_compilation_without_forced_props(self):
        core = (ROOT / "03_prompt/visual-prompt-core/SKILL.md").read_text(encoding="utf-8")
        director = (ROOT / "02_design/illustration-direction/SKILL.md").read_text(encoding="utf-8")
        card = (ROOT / "kernel/task-packs/portrait.md").read_text(encoding="utf-8")
        self.assertIn("审美转译不可丢", core)
        self.assertIn("N/A", director)
        self.assertIn("never add props", card)
        self.assertIn("Centered or quiet portraits", card)

    def test_manual_cases_and_real_image_evidence_remain_distinct(self):
        doc = (ROOT / "docs/composition-taste-review.md").read_text(encoding="utf-8")
        for case in ("小画师脑", "对称而克制", "只改表情", "构图很 AI", "IMAGE-PENDING"):
            self.assertIn(case, doc)

    def test_calm_design_and_user_first_diagnosis_are_permitted(self):
        char = (ROOT / "02_design/character-design-engine/SKILL.md").read_text(encoding="utf-8")
        review = (ROOT / "06_evaluation/evaluation-loop/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("不要求固定比例、怪点、动作或叙事", char)
        self.assertIn("用户问题优先的诊断", review)
        self.assertIn("方案可行但图没遵循", review)
        self.assertIn("无怪点、无剧情、正面或对称不构成失败", review)
        self.assertIn("跨会话持久化需用户授权", review)


if __name__ == "__main__":
    unittest.main()
