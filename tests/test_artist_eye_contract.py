"""Static cross-media Artist Eye wiring checks. Not an image-quality benchmark."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DIRECTOR = ROOT / "00_core/aesthetic-director-core"
ANALYSIS = ROOT / "04_analysis/image-reverse-analysis"
LAYOUT = ROOT / "02_design/illustration-direction"
EVALUATION = ROOT / "06_evaluation/evaluation-loop"


class ArtistEyeContractTest(unittest.TestCase):
    def test_references_are_present_and_linked(self):
        matrix = {
            DIRECTOR: "references/artist-eye-creative-lab.md",
            ANALYSIS: "references/artist-eye-crossmedia-evidence.md",
            EVALUATION: "references/artist-eye-review-protocol.md",
        }
        for owner, ref in matrix.items():
            with self.subTest(owner=owner.name):
                self.assertTrue((owner / ref).is_file())
                self.assertIn(ref, (owner / "SKILL.md").read_text(encoding="utf-8"))

    def test_existing_owner_boundaries_remain(self):
        artist_eye = (DIRECTOR / "references/artist-eye-creative-lab.md").read_text(encoding="utf-8")
        layout = (LAYOUT / "SKILL.md").read_text(encoding="utf-8")
        eval_skill = (EVALUATION / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("唯一创意 owner", artist_eye)
        self.assertIn("只接收幸存方向", layout)
        self.assertIn("只动一个变量", eval_skill)
        self.assertIn("NAI5/Anima", artist_eye)

    def test_counterfactual_and_originality_are_required(self):
        lab = (DIRECTOR / "references/artist-eye-creative-lab.md").read_text(encoding="utf-8")
        self.assertIn("视觉反事实", lab)
        self.assertIn("三向竞争", lab)
        self.assertIn("淘汰两个", lab)
        self.assertIn("参考", lab)

    def test_evidence_is_not_claimed_as_verified_image_generation(self):
        atlas = (ANALYSIS / "references/artist-eye-crossmedia-evidence.md").read_text(encoding="utf-8")
        review = (EVALUATION / "references/artist-eye-review-protocol.md").read_text(encoding="utf-8")
        self.assertIn("HYPOTHESIS", atlas)
        self.assertIn("IMAGE-PENDING", atlas)
        self.assertIn("USER-APPROVED", review)
        self.assertIn("自动美感分数", review)

    def test_required_manual_cases_exist(self):
        cases = (ROOT / "tests/artist-eye-regression.md").read_text(encoding="utf-8")
        for case_id in range(1, 9):
            with self.subTest(case_id=case_id):
                self.assertIn(f"## T{case_id} ·", cases)
        self.assertIn("没有说生图", cases)
        self.assertIn("character 1:", cases)


if __name__ == "__main__":
    unittest.main()
