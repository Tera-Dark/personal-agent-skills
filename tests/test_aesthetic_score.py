"""Quantified aesthetic scorebook: deterministic math and evidence boundaries only."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import aesthetic_score as a


def draft(profile="duo_fashion", stage="SPEC", version="v1",
          rater="assistant", work_id="endfield-sport"):
    entry = a.template(profile, stage, work_id, version)
    entry["rater"] = rater
    entry["assessment_id"] = f"{work_id}-{version}-{rater}-{stage.lower()}"
    for key in entry["axes"]:
        entry["axes"][key] = {"score": 8.0,
                              "evidence": f"{key}: the prompt specifies a concrete compositional fact"}
    if stage == "IMAGE-REVIEWED":
        entry["image_seen"] = True
        entry["image_ref"] = f"{work_id}-asset"
    return entry


class QuantifiedAestheticReviewTests(unittest.TestCase):
    def test_profiles_have_fixed_weights(self):
        self.assertEqual(set(a.WEIGHTS), {
            "duo_fashion", "portrait", "cinematic", "concept_poster", "general"})
        for weights in a.WEIGHTS.values():
            self.assertEqual(sum(weights), 100)

    def test_weighted_score_and_one_decimal(self):
        entry = draft()
        entry["axes"]["fashion"]["score"] = 5
        entry["axes"]["camera"]["score"] = 9
        result = a.score(entry)
        self.assertEqual(result["total"], 7.6)  # 8 + 0.2 - 0.6
        self.assertFalse(result["score_capped"])

    def test_hard_failures_cap_even_beautiful_prompt(self):
        entry = draft()
        for value in entry["axes"].values():
            value["score"] = 10.0
        entry["hard_failures"] = ["wrong_identity", "crop_conflict"]
        result = a.score(entry)
        self.assertEqual(result["weighted_raw"], 10)
        self.assertEqual(result["total"], 5.0)
        self.assertTrue(result["score_capped"])

    def test_spec_never_claims_image_review_or_high_confidence(self):
        entry = draft()
        entry["confidence"] = "high"
        with self.assertRaises(ValueError):
            a.score(entry)
        entry["confidence"] = "medium"
        entry["image_seen"] = True
        with self.assertRaises(ValueError):
            a.score(entry)

    def test_unviewed_image_cannot_be_rated(self):
        entry = a.template("duo_fashion", "IMAGE-REVIEWED",
                           "endfield-sport", "v2")
        for axis in entry["axes"]:
            entry["axes"][axis] = {"score": 9, "evidence": "A genuine visible fact on the image"}
        with self.assertRaises(ValueError):
            a.score(entry)
        entry["image_seen"] = True
        entry["image_ref"] = "https://private.example/asset.png"
        with self.assertRaises(ValueError):
            a.score(entry)

    def test_missing_evidence_and_fake_precision_rejected(self):
        entry = draft()
        entry["axes"]["camera"]["evidence"] = "good"
        with self.assertRaises(ValueError):
            a.score(entry)
        entry = draft()
        entry["axes"]["camera"]["score"] = 8.3
        with self.assertRaises(ValueError):
            a.score(entry)

    def test_scopes_with_no_fashion_dont_require_it(self):
        entry = draft(profile="concept_poster")
        self.assertNotIn("fashion", entry["axes"])
        self.assertNotIn("interaction", entry["axes"])
        self.assertEqual(a.score(entry)["total"], 8)

    def test_comparison_requires_same_work_stage_profile_rater(self):
        v1 = draft()
        v2 = draft(version="v2")
        v2["axes"]["camera"]["score"] = 10
        result = a.compare(v1, v2)
        self.assertEqual(result["delta"], 0.4)
        self.assertEqual(result["changes"]["camera"]["weighted_contribution"], 0.4)
        with self.assertRaises(ValueError):
            a.compare(v1, draft(stage="IMAGE-REVIEWED", version="v2"))
        with self.assertRaises(ValueError):
            a.compare(v1, draft(profile="portrait", version="v2"))

    def test_calibration_preserves_rater_difference(self):
        ai, user = draft(), draft(rater="user")
        user["axes"]["fashion"]["score"] = 6.0
        result = a.calibrate(ai, user)
        self.assertEqual(result["assistant_minus_user"], 0.4)
        with self.assertRaises(ValueError):
            a.calibrate(user, ai)

    def test_owner_doc_is_linked(self):
        ref = ROOT / "06_evaluation/evaluation-loop/references/quantified-aesthetic-review.md"
        skill = ROOT / "06_evaluation/evaluation-loop/SKILL.md"
        self.assertTrue(ref.is_file())
        self.assertIn("quantified-aesthetic-review.md", skill.read_text(encoding="utf-8"))
        doc = ref.read_text(encoding="utf-8")
        for keyword in ("SPEC", "IMAGE-REVIEWED", "0.5", "duo_fashion", "User", "wrong_identity"):
            self.assertIn(keyword.lower(), doc.lower())


if __name__ == "__main__":
    unittest.main()
