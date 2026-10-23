"""Editorial layout skill contracts: authored composition, not prompt syntax or fake art claims."""
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
MOD = ROOT / "02_design" / "editorial-layout-design"


class EditorialLayoutContractTests(unittest.TestCase):
    def test_standalone_skill_is_on_demand_and_referenced(self):
        s = (MOD / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("name: editorial-layout-design", s)
        self.assertIn('layer: "02_design"', s)
        self.assertIn('load: "on-demand"', s)
        for ref in (
            "references/editorial-breakout-reference-2026-10-23.md",
            "references/editorial-pattern-library.md",
            "references/production-delivery.md",
        ):
            self.assertIn(ref, s)
            self.assertTrue((MOD / ref).is_file())

    def test_respects_existing_design_owner_boundaries(self):
        s = (MOD / "SKILL.md").read_text(encoding="utf-8")
        for existing in ("aesthetic-director-core", "illustration-direction",
                         "visual-prompt-core", "moss", "Output"):
            self.assertIn(existing.lower(), s.lower())
        self.assertIn("不接管人物身份", s)
        self.assertIn("Typography Fidelity", s)
        self.assertIn("Editorial Layout Blueprint", s)
        self.assertIn("不要", s)

    def test_router_and_concept_task_card_discover_module(self):
        router = (ROOT / "01_router/creative-skill-router/SKILL.md").read_text(encoding="utf-8")
        card = (ROOT / "kernel/task-packs/concept-poster.md").read_text(encoding="utf-8")
        illust = (ROOT / "02_design/illustration-direction/SKILL.md").read_text(encoding="utf-8")
        for body in (router, card, illust):
            self.assertIn("editorial-layout-design", body)
        self.assertIn("不默认", router)
        self.assertIn("纯插画", illust)

    def test_no_auto_always_on_token_burden(self):
        cfg = json.loads((ROOT / "harness.json").read_text(encoding="utf-8"))
        self.assertNotIn("editorial-layout-design", cfg["always_on"])
        self.assertEqual(set(cfg["knowledge_tiers"]["task_packs"]),
                         {"portrait", "cinematic-duo", "concept-poster", "fast-variant"})

    def test_reference_observation_not_claiming_exact_font(self):
        s = (MOD / "references/editorial-breakout-reference-2026-10-23.md").read_text(encoding="utf-8")
        for label in ("OBSERVED", "INFERRED", "UNKNOWN", "图像窗", "破框",
                      "反事实删除测试", "不复制参考图"):
            self.assertIn(label, s)
        self.assertIn("近似", s)

    def test_multiple_substantively_different_patterns(self):
        s = (MOD / "references/editorial-pattern-library.md").read_text(encoding="utf-8")
        for pat in ("E1", "E2", "E3", "破框", "侧边栏", "切割"):
            self.assertIn(pat, s)
        self.assertIn("失效", s)
        self.assertIn("不用编辑模块", s)

    def test_text_accuracy_and_no_fake_metadata_rules(self):
        s = (MOD / "references/production-delivery.md").read_text(encoding="utf-8")
        for term in ("精确中文", "不虚构", "abs_centralized", "yxyx",
                     "moss_layout.py", "图窗", "最终画布"):
            self.assertIn(term, s)
        core = (MOD / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("不能", core)
        self.assertIn("图文", core)


if __name__ == "__main__":
    unittest.main()
