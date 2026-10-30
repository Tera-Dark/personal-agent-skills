"""Critical web-session and portable tag routing contracts."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build
import build_tag_index


class WebSessionTests(unittest.TestCase):
    def test_session_revision_and_first_message(self):
        _, manifest, outputs = build.build_outputs(str(ROOT))
        core = outputs["bundle/HARNESS.md"]
        self.assertIn("commits/main", core)
        self.assertIn("same SHA instead of `main`", core)
        self.assertIn("disclose unverified consistency", core)
        self.assertIn("otherwise complete the task", core)
        self.assertIn("If the user's first message includes a task, skip the handshake", core)
        for path, content in outputs.items():
            if path.startswith("bundle/references/"):
                self.assertIn("harness v" + manifest["version"], content.splitlines()[1])

    def test_reserved_prefix_preserves_identity_and_portable_path(self):
        outputs = build_tag_index.generate_outputs(
            {"artists": [["@con_artist", 5, "@con_alias"], ["@nul_artist", 3, ""]]}, "sha")
        for prefix in ("con", "nul"):
            shard = json.loads(outputs[f"bundle/tag-index/artists/{prefix}-shard.json"])
            self.assertEqual(shard["_meta"]["prefix"], prefix)
            self.assertIn(f"@{prefix}_artist", shard["exact"])
        manifest = json.loads(outputs["bundle/tag-index/manifest.json"])
        self.assertIn("<prefix>-shard.json", manifest["lookup"]["shard_filename_rule"])


if __name__ == "__main__":
    unittest.main()
