"""Google AI Studio adapter bundle contract."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build


class AIStudioAdapterTests(unittest.TestCase):
    def test_adapter_is_generated_and_registered(self):
        _, manifest, outputs = build.build_outputs(str(ROOT))
        adapter = outputs["bundle/AISTUDIO.md"]
        self.assertIn("Google AI Studio", adapter)
        self.assertIn("Harness v" + manifest["version"], adapter)
        self.assertIn("URL Context", adapter)
        self.assertIn("does **not** automatically crawl", adapter)
        self.assertEqual(manifest["aistudio_url"],
                         "https://raw.githubusercontent.com/Tera-Dark/personal-agent-skills/main/bundle/AISTUDIO.md")
        self.assertEqual(manifest["aistudio_tokens"], build.L.estimate_tokens(adapter))
        self.assertLess(manifest["aistudio_tokens"], 8500)

    def test_adapter_indexes_every_module_and_marks_planned_modules(self):
        _, manifest, outputs = build.build_outputs(str(ROOT))
        adapter = outputs["bundle/AISTUDIO.md"]
        for module in manifest["modules"]:
            self.assertIn(module["name"], adapter)
        self.assertIn("on-demand/planned", adapter)
        self.assertIn("placeholders, not implemented capabilities", adapter)

    def test_adapter_exposes_task_and_pipeline_routes(self):
        _, manifest, outputs = build.build_outputs(str(ROOT))
        adapter = outputs["bundle/AISTUDIO.md"]
        for name in manifest["knowledge_tiers"]["task_packs"]:
            self.assertIn(f"task-packs/{name}.md", adapter)
        for name in manifest["pipeline_packs"]:
            self.assertIn(f"pipelines/{name}.md", adapter)
        self.assertIn("Do not preload all modules", adapter)
        self.assertIn("[pipeline-unavailable]", adapter)
        self.assertIn("[tag-index-unavailable]", adapter)


if __name__ == "__main__":
    unittest.main()
