"""Regression suite: executable semantics for the personal learning system."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import learn


def feedback(artifact="picture-1", polarity="support", rule_id="cinematic.scene", **kw):
    data = {
        "rule_id": rule_id,
        "scope": "mode:cinematic",
        "axis": "camera",
        "rule": "Choose meaningful viewpoint before lighting presets",
        "polarity": polarity,
        "evidence_type": "USER-IMAGE-REPORT",
        "artifact_id": artifact,
        "date": "2026-10-14",
    }
    data.update(kw)
    return data


class LearningTests(unittest.TestCase):
    def setUp(self):
        self.t = tempfile.TemporaryDirectory()
        self.root = Path(self.t.name)

    def tearDown(self):
        self.t.cleanup()

    def test_empty_repo_and_digest(self):
        self.assertEqual(learn.validate(self.root)["events"], 0)
        learn.digest(self.root)
        self.assertEqual(learn.validate(self.root)["status"], "pass")
        self.assertIn("No approved learned rules", (self.root / learn.DIGEST).read_text())

    def test_dedup_same_artifact(self):
        a = learn.record(self.root, feedback())
        b = learn.record(self.root, feedback(note="the same image, different message"))
        self.assertEqual(a["id"], b["id"])
        self.assertEqual(len(learn.jsonl(self.root, learn.EVENTS)), 1)
        self.assertEqual(learn.review(self.root)[0]["support"], 1)

    def test_needs_independent_artifacts(self):
        learn.record(self.root, feedback())
        learn.record(self.root, feedback("picture-1", polarity="oppose"))
        self.assertEqual(learn.review(self.root)[0]["support"], 1)
        self.assertEqual(learn.review(self.root)[0]["oppose"], 1)
        with self.assertRaises(learn.LearnError):
            learn.promote(self.root, "cinematic.scene")

    def test_three_distinct_allow_reviewed_promotion(self):
        for i in range(3):
            learn.record(self.root, feedback("picture-" + str(i)))
        row = learn.review(self.root)[0]
        self.assertTrue(row["eligible"])
        self.assertFalse(row["active"])
        self.assertEqual(learn.promote(self.root, "cinematic.scene")["status"], "promoted")
        learn.digest(self.root)
        text = (self.root / learn.DIGEST).read_text()
        self.assertIn("Choose meaningful viewpoint", text)
        self.assertEqual(learn.validate(self.root)["status"], "pass")

    def test_explicit_user_policy_bypasses_three_but_not_manual_review(self):
        learn.record(self.root, feedback(
            evidence_type="USER-EXPLICIT-POLICY", artifact_id="owner-stated-policy"
        ))
        self.assertTrue(learn.review(self.root)[0]["eligible"])
        self.assertFalse(learn.review(self.root)[0]["active"])
        learn.promote(self.root, "cinematic.scene")
        self.assertTrue(learn.review(self.root)[0]["active"])

    def test_opposition_blocks_promotion(self):
        for i in range(3):
            learn.record(self.root, feedback("picture-" + str(i)))
        learn.record(self.root, feedback("picture-x", polarity="oppose",
                                         evidence_type="TEXT-REJECTED"))
        self.assertFalse(learn.review(self.root)[0]["eligible"])
        with self.assertRaises(learn.LearnError):
            learn.promote(self.root, "cinematic.scene")

    def test_opposition_suspends_a_previously_active_rule(self):
        learn.record(self.root, feedback(evidence_type="USER-EXPLICIT-POLICY"))
        learn.promote(self.root, "cinematic.scene")
        learn.record(self.root, feedback("later-disliked-image",
                                         polarity="oppose",
                                         evidence_type="USER-IMAGE-REPORT"))
        row = learn.review(self.root)[0]
        self.assertTrue(row["active"])
        self.assertTrue(row["needs_review"])
        self.assertFalse(row["effective_active"])
        learn.digest(self.root)
        text = (self.root / learn.DIGEST).read_text()
        self.assertNotIn("Choose meaningful viewpoint", text)

    def test_invalid_date_rejected(self):
        with self.assertRaises(learn.LearnError):
            learn.record(self.root, feedback(date="2026-14-99"))

    def test_undo_preserves_audit_history(self):
        learn.record(self.root, feedback(
            evidence_type="USER-EXPLICIT-POLICY"
        ))
        learn.promote(self.root, "cinematic.scene")
        learn.undo(self.root, "cinematic.scene")
        self.assertFalse(learn.review(self.root)[0]["active"])
        actions = learn.jsonl(self.root, learn.ACTIONS)
        self.assertEqual([a["action"] for a in actions], ["promote", "undo"])
        learn.digest(self.root)
        self.assertNotIn("Choose meaningful viewpoint", (self.root / learn.DIGEST).read_text())

    def test_rule_id_collision_is_rejected(self):
        learn.record(self.root, feedback())
        with self.assertRaises(learn.LearnError):
            learn.record(self.root, feedback("picture-2", rule="A different idea"))

    def test_scope_is_not_widened(self):
        with self.assertRaises(learn.LearnError):
            learn.record(self.root, feedback(scope="other:unknown"))
        learn.record(self.root, feedback(scope="mode:cinematic"))
        self.assertEqual(learn.review(self.root)[0]["scope"], "mode:cinematic")

    def test_public_session_whitelist_and_load(self):
        packet = {"target": "nai5", "locked": ["original outfit"],
                  "approved": ["eye contact"], "next_action": "change camera",
                  "private_chat": "must never get persisted", "api_key": "SECRET"}
        learn.session_save(self.root, "vertin-01", packet)
        restored = learn.session_load(self.root, "vertin-01")
        self.assertNotIn("api_key", restored)
        self.assertNotIn("private_chat", restored)
        self.assertEqual(restored["locked"], ["original outfit"])
        with self.assertRaises(learn.LearnError):
            learn.session_save(self.root, "../secrets", packet)

    def test_session_diff_protects_approved_and_locked_facts(self):
        learn.session_save(self.root, "v1", {
            "target": "nai5", "locked": ["original outfit", "silver hair"],
            "approved": ["camera through glass"], "rejected": ["floating petals"],
        })
        learn.session_save(self.root, "v2", {
            "target": "nai5", "locked": ["silver hair"],
            "approved": ["floating petals"], "rejected": ["floating petals"],
        })
        result = learn.session_diff(self.root, "v1", "v2")
        self.assertEqual(result["status"], "fail")
        self.assertIn("original outfit", result["missing_locked"])
        self.assertIn("camera through glass", result["missing_approved"])
        self.assertIn("floating petals", result["resurfaced_rejected"])
        self.assertEqual(learn.session_list(self.root), ["v1", "v2"])

    def test_session_diff_identical_locks_is_safe(self):
        for name in ("v1", "v2"):
            learn.session_save(self.root, name, {
                "target": "anima", "locked": ["green eyes"],
                "approved": ["active camera"], "rejected": ["random petals"],
            })
        self.assertEqual(learn.session_diff(self.root, "v1", "v2")["status"], "pass")

    def test_corrupt_event_is_rejected(self):
        (self.root / learn.EVENTS).parent.mkdir(parents=True)
        (self.root / learn.EVENTS).write_text("{broken json}\n", encoding="utf-8")
        with self.assertRaises(learn.LearnError):
            learn.validate(self.root)

    def test_stale_digest_is_rejected(self):
        learn.record(self.root, feedback(evidence_type="USER-EXPLICIT-POLICY"))
        learn.digest(self.root)
        learn.promote(self.root, "cinematic.scene")
        with self.assertRaises(learn.LearnError):
            learn.validate(self.root)
        learn.digest(self.root)
        self.assertEqual(learn.validate(self.root)["status"], "pass")

    def test_cli_end_to_end(self):
        script = Path(__file__).resolve().parents[1] / "scripts" / "learn.py"
        payload = self.root / "feedback.json"
        payload.write_text(json.dumps(feedback(), ensure_ascii=False), encoding="utf-8")
        result = subprocess.run(
            [sys.executable, str(script), "--root", str(self.root), "record",
             "--file", str(payload)],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["status"], "recorded")


if __name__ == "__main__":
    unittest.main()
