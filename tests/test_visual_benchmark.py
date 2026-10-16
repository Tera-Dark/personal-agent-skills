"""Visual benchmark contracts: genuine runs required; no imaginary art ratings."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import visual_benchmark as vb

ROOT = Path(__file__).resolve().parents[1]


class VisualBenchmarkTests(unittest.TestCase):
    def test_specs_are_pending(self):
        self.assertEqual(set(vb.load_cases(ROOT)), vb.SCOPES)

    def good_run(self):
        r = vb.template("portrait", "oc-portrait-run-01", ROOT)
        for group in ("baseline", "variant"):
            for field in vb.SETTING_KEYS:
                r[group][field] = "same-config"
        return r

    def test_pending_requires_no_fake_scores(self):
        run = self.good_run()
        self.assertEqual(vb.validate_record(run)["status"], "IMAGE-PENDING")
        run["result"]["winner"] = "variant"
        with self.assertRaises(ValueError):
            vb.validate_record(run)

    def test_fixed_settings_required(self):
        run = self.good_run()
        run["variant"]["seed"] = "different"
        with self.assertRaises(ValueError):
            vb.validate_record(run)

    def test_change_axis_locked(self):
        run = self.good_run()
        run["design_changes"] = ["camera_crop", "outfit"]
        with self.assertRaises(ValueError):
            vb.validate_record(run)

    def test_human_required_for_scores(self):
        run = self.good_run()
        run["result"] = {"status": "USER-RATED",
                         "winner": "variant",
                         "scores": {"baseline": {k: 3 for k in vb.load_cases()["portrait"]["rubric"]},
                                    "variant": {k: 4 for k in vb.load_cases()["portrait"]["rubric"]}}}
        with self.assertRaises(ValueError):
            vb.validate_record(run)
        run["result"]["reviewer"] = "user"
        self.assertEqual(vb.validate_record(run)["status"], "USER-RATED")

    def test_public_data_excludes_raw_images(self):
        run = self.good_run()
        run["image_url"] = "https://private.example/image"
        with self.assertRaises(ValueError):
            vb.validate_record(run)


if __name__ == "__main__":
    unittest.main()
