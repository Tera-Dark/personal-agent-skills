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

    def test_full_bundle_embeds_references_but_not_tag_index(self):
        _, _, outputs = build.build_outputs(str(ROOT))
        full = outputs["bundle/HARNESS-FULL.md"]
        self.assertIn("External tag verification still requires the separate index", full)
        self.assertIn("reuse its embedded active modules and references", full)
        self.assertIn("composition-quick-card.md", full)
        self.assertIn("tag-index-unavailable", full)
        self.assertNotIn("Nothing else needs to be fetched", full)


if __name__ == "__main__":
    unittest.main()
