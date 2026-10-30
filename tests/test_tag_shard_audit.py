"""Audit is read-only and refuses malformed/mislicensed shard snapshots."""
import json
import sys
import tempfile
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from tag_shard_audit import analyze


class ShardAuditTests(unittest.TestCase):
    def fixture(self, root):
        d = root / "bundle/tag-index/artists"
        d.mkdir(parents=True)
        (d / "abc.json").write_text('{"_meta":{"prefix":"abc"},"exact":{}}', encoding="utf-8")
        (d / "abd.json").write_text('{"_meta":{"prefix":"abd"},"exact":{}}', encoding="utf-8")
        base = root / "bundle/tag-index"
        (base / "NOTICE.md").write_text("GPL-3.0", encoding="utf-8")
        manifest = {"schema_version": 1, "source": {"license": "GPL-3.0"},
                    "groups": {"artists": {"shard_count": 2}}}
        (base / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

    def test_small_shards_merge_only_in_projection(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.fixture(root)
            report = analyze(root, max_bucket_bytes=300)
            self.assertEqual(report["current_shards"], 2)
            self.assertEqual(report["estimated_adaptive_shards"], 1)
            self.assertTrue((root / "bundle/tag-index/artists/abc.json").exists())

    def test_large_bucket_kept_separate(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.fixture(root)
            self.assertEqual(analyze(root, max_bucket_bytes=3)["estimated_adaptive_shards"], 2)

    def test_license_metadata_is_not_ignored(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.fixture(root)
            p = root / "bundle/tag-index/manifest.json"
            data = json.loads(p.read_text(encoding="utf-8"))
            data["source"]["license"] = "MIT"
            p.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaises(ValueError):
                analyze(root)


if __name__ == "__main__":
    unittest.main()
