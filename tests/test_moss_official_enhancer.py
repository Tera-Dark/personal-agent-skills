"""Contract tests against OpenMOSS official prompt-enhancer draft/compile semantics.

Source: https://github.com/OpenMOSS/MOSS-Image/tree/main/skills/moss-image-prompt-enhancer
Based on public behavior checked 2026-10-21. No model-generation quality claims.
"""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from moss_layout import bbox_to_native, compile_draft


def layout():
    return {
        "width": 1536,
        "height": 1024,
        "bbox_coord_space": "abs",
        "bbox_format": "xyxy",
        "summary": {
            "meta": ["product campaign", "studio photography"],
            "canvas": "single",
            "palette": ["ivory", "forest green"],
            "caption": "A restrained campaign for a ceramic cup.",
        },
        "items": [
            {"label": "object", "caption": "A cream ceramic cup with glaze.",
             "bbox": [176, 224, 800, 864]},
            {"label": "text", "caption": "Crisp dark-green headline.",
             "text": '把日常，过成诗。\n"MOSS" 🪴',
             "bbox": [928, 272, 1408, 448]},
        ],
    }


class OfficialEnhancerIntegrationTests(unittest.TestCase):
    def test_caption_draft_compiles_to_exact_plain_text(self):
        caption = 'An ivory cup marked "茶".\nKeep this line.'
        self.assertEqual(compile_draft({"caption": caption}), caption)
        for bad in ({"caption": ""}, {"caption": caption, "items": []}):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                compile_draft(bad)

    def test_compiled_layout_exact_native_structure_and_text(self):
        draft = layout()
        before = copy.deepcopy(draft)
        result_str = compile_draft(draft)
        result = json.loads(result_str)
        self.assertEqual(set(result), {
            "summary", "items", "bbox_coord_space", "bbox_format",
        })
        self.assertEqual(result["bbox_format"], "yxyx")
        self.assertEqual(result["bbox_coord_space"], "abs_centralized")
        self.assertEqual(result["items"][0]["bbox"], [-288, -592, 352, 32])
        self.assertEqual(result["items"][1]["bbox"], [-240, 160, -64, 640])
        self.assertEqual(result["items"][1]["text"], '把日常，过成诗。\n"MOSS" 🪴')
        self.assertNotIn("\n", result_str)
        self.assertEqual(draft, before)

    def test_upstream_fractional_edge_rounding(self):
        self.assertEqual(
            bbox_to_native([0, 0, 768, 1344], 768, 1344),
            [-672, -384, 672, 384],
        )
        self.assertEqual(
            bbox_to_native([10.9, 20.1, 100.01, 200.99], 768, 1344),
            [-652, -374, -471, -283],
        )
        self.assertEqual(
            bbox_to_native([1.00000000001, 2, 100, 200], 768, 1344),
            [-670, -383, -472, -284],
        )

    def test_does_not_silently_accept_unexportable_box(self):
        for box in (
            [0, 0, 0.00000000001, 100],
            [True, 0, 100, 100],
            [-1, 0, 100, 100],
            [0, 0, 1537, 100],
            [0, 0, 100, float("inf")],
        ):
            with self.subTest(box=box), self.assertRaises(ValueError):
                bbox_to_native(box, 1536, 1024)

    def test_layout_is_schema_strict_and_accepts_optional_text(self):
        draft = layout()
        draft["items"][0]["text"] = "陶瓷杯"
        self.assertEqual(
            json.loads(compile_draft(draft))["items"][0]["text"], "陶瓷杯",
        )
        for key in ("children", "parent", "id", "font_size"):
            bad = layout()
            bad["items"][0][key] = "unexpected"
            with self.subTest(key=key), self.assertRaises(ValueError):
                compile_draft(bad)
        bad = layout()
        bad["items"][1].pop("text")
        with self.assertRaises(ValueError):
            compile_draft(bad)

    def test_invalid_sizes_and_coord_systems_are_rejected(self):
        for key, value in (
            ("width", True), ("height", 1025), ("width", 1536.0),
            ("bbox_coord_space", "abs_centralized"), ("bbox_format", "yxyx")
        ):
            bad = layout()
            bad[key] = value
            with self.subTest(key=key, value=value), self.assertRaises(ValueError):
                compile_draft(bad)

    def test_cli_never_overwrites_draft_and_preserves_utf8(self):
        script = ROOT / "scripts" / "moss_layout.py"
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "draft.json"
            output = Path(directory) / "prompt.txt"
            source.write_text(json.dumps(layout(), ensure_ascii=False), encoding="utf-8")
            original = source.read_text(encoding="utf-8")
            run = subprocess.run(
                [sys.executable, str(script), str(source), "--output", str(output)],
                capture_output=True, text=True,
            )
            self.assertEqual(run.returncode, 0, run.stderr)
            result = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(result["items"][1]["text"], '把日常，过成诗。\n"MOSS" 🪴')
            self.assertEqual(source.read_text(encoding="utf-8"), original)
            bad = subprocess.run(
                [sys.executable, str(script), str(source), "--output", str(source)],
                capture_output=True, text=True,
            )
            self.assertNotEqual(bad.returncode, 0)
            self.assertEqual(source.read_text(encoding="utf-8"), original)

    def test_integration_docs_are_on_demand_and_keep_tags_separate(self):
        skill = (ROOT / "03_prompt/moss-image-renderer/SKILL.md").read_text(encoding="utf-8")
        doc = ROOT / "03_prompt/moss-image-renderer/references/official-enhancer-workflow.md"
        self.assertTrue(doc.is_file())
        self.assertIn("references/official-enhancer-workflow.md", skill)
        self.assertIn("Caption", skill)
        self.assertIn("Tags", skill)
        self.assertIn("Layout", skill)
        self.assertIn("scripts/moss_layout.py", skill)
        self.assertIn("IMAGE-PENDING", skill)


if __name__ == "__main__":
    unittest.main()
