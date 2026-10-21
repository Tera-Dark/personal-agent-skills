"""Evidence-based visual taste wiring and failure-case regression.

Static spec checks only; cannot measure whether final generated art is beautiful.
"""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DIRECTOR = ROOT / "00_core/aesthetic-director-core"
ILLUSTRATION = ROOT / "02_design/illustration-direction"
ROUTER = ROOT / "01_router/creative-skill-router"
EVALUATION = ROOT / "06_evaluation/evaluation-loop"


def read(path):
    return path.read_text(encoding="utf-8")


class EvidenceBasedTasteTests(unittest.TestCase):
    def test_stable_owner_and_on_demand_reference(self):
        director = read(DIRECTOR / "SKILL.md")
        eval_skill = read(EVALUATION / "SKILL.md")
        self.assertIn("references/visual-taste-evidence-protocol.md", director)
        self.assertIn("references/evidence-based-art-critique.md", eval_skill)
        self.assertTrue((DIRECTOR / "references/visual-taste-evidence-protocol.md").is_file())
        self.assertTrue((EVALUATION / "references/evidence-based-art-critique.md").is_file())
        self.assertIn('load: "on-demand"', director)
        self.assertIn("仍由本导演唯一拥有创意决定", director)
        self.assertIn("本 Skill 不修 prompt", eval_skill)

    def test_router_l1_escalates_feedback(self):
        router = read(ROUTER / "SKILL.md")
        compact = read(ROUTER / "references/router-quickstart.md")
        kernel = read(ROOT / "kernel/KERNEL.md")
        for phrase in ("visual-taste-evidence-protocol.md", "evaluation-loop"):
            self.assertIn(phrase, router)
            self.assertIn(phrase, compact)
        self.assertIn("evidence-based visual-taste protocol", kernel)

    def test_evidence_is_separate_from_unsupported_psychology(self):
        spec = read(DIRECTOR / "references/visual-taste-evidence-protocol.md")
        for marker in ("SEE / READ / UNKNOWN", "FORM–MEANING FIT",
                       "三种", "人物", "正典", "SPEC", "IMAGE-PENDING", "用户真实"):
            self.assertIn(marker, spec)
        self.assertIn("没有象征和反转仍可优秀", spec)
        self.assertIn("第一眼美感", spec)

    def test_composition_role_consumes_but_does_not_serialize_taste(self):
        illustration = read(ILLUSTRATION / "SKILL.md")
        self.assertIn("visual_evidence", illustration)
        self.assertIn("interpretation_status", illustration)
        self.assertIn("不能", illustration)
        anima = read(ROOT / "03_prompt/anima-renderer/SKILL.md")
        self.assertIn("Tag block + Natural Language block", anima)
        self.assertIn("does not design", anima)
        self.assertNotIn("visual-taste-evidence-protocol.md", anima)

    def test_rin_and_previous_painting_repeated_failure_cases_are_documented(self):
        spec = read(DIRECTOR / "references/visual-taste-evidence-protocol.md")
        critique = read(EVALUATION / "references/evidence-based-art-critique.md")
        for marker in ("远坂凛", "圣杯", "天使", "构图"):
            self.assertIn(marker, spec)
            self.assertIn(marker, critique)
        self.assertIn("黑色污液", spec)
        self.assertIn("黑污液", critique)
        for marker in ("失败①", "失败②", "失败③"):
            self.assertIn(marker, critique)
        self.assertIn("用故事补图", critique)

    def test_no_false_claim_of_image_benchmark(self):
        spec = read(DIRECTOR / "references/visual-taste-evidence-protocol.md")
        critique = read(EVALUATION / "references/evidence-based-art-critique.md")
        self.assertIn("未看到", spec)
        self.assertIn("不能", critique)
        self.assertIn("IMAGE-REVIEWED", critique)
        self.assertIn("USER-APPROVED", spec)
        self.assertIn("SEE", spec)
        self.assertIn("Getty", spec)
        self.assertIn("MoMA", spec)
        self.assertIn("Harvard", spec)
        self.assertIn("RISD", spec)


if __name__ == "__main__":
    unittest.main()
