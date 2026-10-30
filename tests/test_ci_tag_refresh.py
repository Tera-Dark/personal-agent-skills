"""A manual tag refresh must carry the validated snapshot into the writer job."""
from pathlib import Path
import unittest


class TagRefreshWorkflowTests(unittest.TestCase):
    def test_validated_snapshot_reaches_main_writer(self):
        workflow = (Path(__file__).resolve().parents[1] / ".github/workflows/harness.yml").read_text(encoding="utf-8")
        validation, writer = workflow.split("  persist-generated:", 1)
        self.assertIn("inputs.sync_tag_index", validation)
        self.assertIn("python3 scripts/build_tag_index.py\n          python3 scripts/check_tag_index_snapshot.py", validation)
        self.assertIn("actions/upload-artifact@v4", validation)
        self.assertIn("name: validated-tag-index", validation)
        self.assertIn("actions/download-artifact@v4", writer)
        self.assertIn("name: validated-tag-index", writer)
        self.assertLess(writer.index("tar -xzf"), writer.index("python3 scripts/build.py"))
        self.assertIn("python3 scripts/check_tag_index_snapshot.py", writer)
        self.assertIn("github.ref == 'refs/heads/main'", writer)


if __name__ == "__main__":
    unittest.main()
