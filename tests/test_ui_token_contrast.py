"""Contrast checks for the starter control-border and focus tokens."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKENS = ROOT / "02_design/chatgpt-inspired-ui/references/design-tokens.md"


def luminance(hex_color):
    values = [int(hex_color[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in values]
    return sum(a * b for a, b in zip(linear, (0.2126, 0.7152, 0.0722)))


def contrast(a, b):
    low, high = sorted((luminance(a), luminance(b)))
    return (high + 0.05) / (low + 0.05)


class StarterTokenContrastTests(unittest.TestCase):
    def test_control_border_and_focus_against_example_surfaces(self):
        css = TOKENS.read_text(encoding="utf-8")
        light, dark = css.split('[data-theme="dark"]', 1)
        for theme in (light, dark):
            tokens = dict(re.findall(r"(--ui-[\w-]+):\s*(#[0-9a-fA-F]{6})", theme))
            for surface in ("--ui-bg", "--ui-nav", "--ui-surface", "--ui-surface-muted", "--ui-hover"):
                for foreground in ("--ui-control-border", "--ui-focus"):
                    with self.subTest(surface=surface, foreground=foreground, color=tokens[foreground]):
                        self.assertGreaterEqual(contrast(tokens[foreground], tokens[surface]), 3.0)


if __name__ == "__main__":
    unittest.main()
