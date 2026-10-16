"""Tiered runtime regression: small bootstrap, selective task cards, L3 ownership."""
from pathlib import Path
import json
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build


class TieredLoadingTests(unittest.TestCase):
    def test_l1_always_on_only_compact_projection(self):
        cfg = json.loads((ROOT / "harness.json").read_text(encoding="utf-8"))
        always = cfg["always_on"]
        self.assertEqual(set(always), {"personal-identity-profile", "creative-skill-router"})
        self.assertNotIn("SKILL.md", always["creative-skill-router"])
        self.assertNotIn("SKILL.md", always["personal-identity-profile"])
        self.assertIn("references/taste-core.md", always["personal-identity-profile"])
        self.assertEqual(cfg["knowledge_tiers"]["l1_core_target_tokens"], 5500)

    def test_compilation_enforces_l1_target(self):
        cfg, manifest, outputs = build.build_outputs(str(ROOT))
        self.assertLessEqual(manifest["core_tokens"], cfg["knowledge_tiers"]["l1_core_target_tokens"])
        self.assertEqual(set(manifest["knowledge_tiers"]["task_packs"]),
                         {"portrait", "cinematic-duo", "concept-poster", "fast-variant"})
        for name in manifest["knowledge_tiers"]["task_packs"]:
            path = f"bundle/task-packs/{name}.md"
            self.assertIn(path, outputs)
            self.assertIn("L2 TASK CARD", outputs[path])
            self.assertLess(manifest["knowledge_tiers"]["task_packs"][name]["tokens"], 1100)
        self.assertNotIn("## 3.6 当前模式校准：Modern Poster Design",
                         outputs["bundle/HARNESS.md"])

    def test_adaptive_creativity_preserves_identity_and_simple_life(self):
        path = ROOT / "00_core/aesthetic-director-core/references/adaptive-creative-intensity.md"
        data = path.read_text(encoding="utf-8")
        for mode in ("daily", "portrait", "cinematic", "experimental"):
            self.assertIn(mode, data)
        self.assertIn("Identity Lock", data)
        self.assertIn("不强制", data)
        self.assertIn("真实出图", data)

    def test_existing_renderers_remain_unchanged_owners(self):
        cfg = json.loads((ROOT / "harness.json").read_text(encoding="utf-8"))
        self.assertEqual(cfg["pipeline"]["pipeline_packs"]["nai5"],
                         ["visual-prompt-core", "danbooru-tag-gate", "nai5-renderer"])
        self.assertEqual(cfg["pipeline"]["pipeline_packs"]["anima"],
                         ["visual-prompt-core", "danbooru-tag-gate", "anima-renderer"])


if __name__ == "__main__":
    unittest.main()
