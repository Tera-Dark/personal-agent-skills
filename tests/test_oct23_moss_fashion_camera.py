"""Oct 22–23 scoped MOSS/fashion/camera documentation contracts.

These tests check routing and scope, not subjective visual quality or model results.
"""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
REF_FASHION = ROOT / "02_design/character-design-engine/references/commercial-game-fashion-calibration-2026-10.md"
REF_DUO = ROOT / "02_design/illustration-direction/references/duo-fashion-camera-staging-2026-10.md"
REF_MOSS = ROOT / "03_prompt/moss-image-renderer/references/caption-efficiency-2026-10.md"
SESSION = ROOT / "00_core/personal-identity-profile/references/session-feedback-2026-10-22-23.md"


class ScopedOct23DesignRegressions(unittest.TestCase):
    def test_new_references_exist_and_are_linked(self):
        for ref in (REF_FASHION, REF_DUO, REF_MOSS, SESSION):
            self.assertTrue(ref.is_file(), ref)
        linked = {
            "02_design/character-design-engine/SKILL.md": REF_FASHION.name,
            "02_design/illustration-direction/SKILL.md": REF_DUO.name,
            "03_prompt/moss-image-renderer/SKILL.md": REF_MOSS.name,
            "00_core/personal-identity-profile/references/taste-core.md": SESSION.name,
        }
        for source, name in linked.items():
            self.assertIn(name, (ROOT / source).read_text(encoding="utf-8"))

    def test_scope_and_no_false_generation_proof(self):
        text = SESSION.read_text(encoding="utf-8")
        for term in ("TEXT-APPROVED", "IMAGE-PENDING", "candidate", "mode: commercial OC",
                     "ip: Endfield AU", "不等于全局审美禁令"):
            self.assertIn(term, text)
        self.assertIn("用户明确", REF_FASHION.read_text(encoding="utf-8"))
        self.assertIn("IMAGE-PENDING", REF_MOSS.read_text(encoding="utf-8"))

    def test_camera_and_identity_failure_modes(self):
        duo = REF_DUO.read_text(encoding="utf-8")
        for term in ("中近景", "手持物", "裁切", "IP AU", "宫门", "运动风"):
            self.assertIn(term, duo)
        moss = REF_MOSS.read_text(encoding="utf-8")
        for term in ("原版", "AU", "medium-close", "full-body", "避免", "身份锁"):
            self.assertIn(term, moss)

    def test_varied_outfit_construction_not_one_template(self):
        fashion = REF_FASHION.read_text(encoding="utf-8")
        for term in ("裁片", "材质", "露肤", "黑色乳胶模板", "新中式旗袍", "大形"):
            self.assertIn(term, fashion)


if __name__ == "__main__":
    unittest.main()
