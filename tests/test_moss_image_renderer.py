"""MOSS-Image prompt data contracts. No model invocation or aesthetic score."""
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from moss_layout import compile_draft, bbox_to_native, unique_pairs

SKILL = ROOT / "03_prompt/moss-image-renderer/SKILL.md"


def one_layout():
    return {
        "width": 1024, "height": 1024,
        "bbox_coord_space": "abs", "bbox_format": "xyxy",
        "summary": {"meta": ["album cover"], "canvas": "single",
                    "caption": "An illustrated young woman before a quiet photographic street."},
        "items": [
            {"label": "character", "caption": "A 2D anime schoolgirl on the left.",
             "bbox": [80, 240, 500, 900]},
            {"label": "text", "caption": "A title in the upper-right.",
             "text": "AFTER SCHOOL\n雨上がり", "bbox": [544, 160, 940, 288]},
        ],
    }


class MossLayoutTests(unittest.TestCase):
    def test_caption_compiles_as_plain_text(self):
        self.assertEqual(compile_draft({"caption": "A quiet anime still."}), "A quiet anime still.")
        with self.assertRaises(ValueError):
            compile_draft({"caption": "A girl", "width": 1024})

    def test_layout_native_coordinates(self):
        raw = compile_draft(one_layout())
        native = json.loads(raw)
        self.assertEqual(set(native), {"summary", "items", "bbox_coord_space", "bbox_format"})
        self.assertEqual(native["bbox_coord_space"], "abs_centralized")
        self.assertEqual(native["bbox_format"], "yxyx")
        self.assertEqual(native["items"][0]["bbox"], [-272, -432, 388, -12])
        self.assertEqual(native["items"][1]["bbox"], [-352, 32, -224, 428])
        self.assertEqual(native["items"][1]["text"], "AFTER SCHOOL\n雨上がり")
        self.assertNotIn("width", native)

    def test_out_of_bounds_and_wrong_draft_system(self):
        data = one_layout()
        data["items"][0]["bbox"][0] = -4
        with self.assertRaises(ValueError):
            compile_draft(data)
        data = one_layout()
        data["bbox_format"] = "yxyx"
        with self.assertRaises(ValueError):
            compile_draft(data)

    def test_fractional_coordinates_enclose_edges(self):
        self.assertEqual(bbox_to_native([100.2, 200.7, 400.1, 500.1], 1024, 1024),
                         [-312, -412, -11, -111])

    def test_non_multiple_of_16_is_invalid(self):
        data = one_layout()
        data["height"] = 1025
        with self.assertRaises(ValueError):
            compile_draft(data)
        data = one_layout()
        data["width"] = True
        with self.assertRaises(ValueError):
            compile_draft(data)

    def test_text_fields_not_assumed(self):
        data = one_layout()
        data["items"][1].pop("text")
        with self.assertRaises(ValueError):
            compile_draft(data)
        data = one_layout()
        data["items"][0]["text"] = "hidden"
        with self.assertRaises(ValueError):
            compile_draft(data)

    def test_reject_duplicate_keys(self):
        with self.assertRaises(ValueError):
            json.loads('{"caption":"first","caption":"second"}', object_pairs_hook=unique_pairs)

    def test_skill_is_web_first_and_has_provenance(self):
        s = SKILL.read_text(encoding="utf-8")
        for keyword in ["name: moss-image-renderer", "Visual Prompt Packet", "Caption",
                        "Tags", "Layout", "abs_centralized", "yxyx",
                        "IMAGE-PENDING", "references/official-spec-and-sources.md"]:
            self.assertIn(keyword, s)
        for source in ["official-spec-and-sources.md", "style-control.md",
                       "layout-contract.md", "examples.md"]:
            self.assertTrue((SKILL.parent / "references" / source).is_file())


if __name__ == "__main__":
    unittest.main()
