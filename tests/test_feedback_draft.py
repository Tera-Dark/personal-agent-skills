"""Feedback drafting never silently persists policies or fabricates image review."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from feedback_draft import draft
from learn import LearnError


class FeedbackDraftTests(unittest.TestCase):
    def test_positive_draft_uses_existing_normalization(self):
        event = draft("portrait.camera", "mode:portrait", "camera",
                      "Eye height aligns with seated figure", "anon-r01",
                      "support", "USER-IMAGE-REPORT", "User reports better face")
        self.assertEqual(event["polarity"], "support")
        self.assertNotIn("active", event)
        self.assertNotIn("id", event)

    def test_explicit_user_policy_cannot_be_oppose(self):
        with self.assertRaises(LearnError):
            draft("portrait.camera", "mode:portrait", "camera", "Avoid soft blur",
                  "anon-r02", "oppose", "USER-EXPLICIT-POLICY", "")

    def test_invalid_scope_is_rejected(self):
        with self.assertRaises(LearnError):
            draft("portrait.camera", "secret:private", "camera", "Do not copy", "anon-r03",
                  "support", "USER-IMAGE-REPORT", "")


if __name__ == "__main__":
    unittest.main()
