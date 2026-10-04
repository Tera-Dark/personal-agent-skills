# NAI5 Community Prompt Format

## Organization

Use these as internal planning layers only:
- artist stack
- global style
- scene
- char1 / char2
- negative (only when requested)

Do **not** emit bracketed section headers such as:
[Artist Stack]
[Global Style]
[Scene]

into the actual NovelAI prompt by default. In NovelAI, square brackets have weakening semantics, so these headers can affect interpretation rather than behaving like Markdown headings.

## Character Blocks

Keep character identity isolated.

Example:

char1:
girl, character name, hair, eyes, outfit, action

## Weight Syntax

NovelAI numerical emphasis:

1.5::tag::
0.5::tag::
-1::tag::

- 1.0 is the baseline
- >1.0 strengthens
- 0.0–1.0 weakens
- negative values are targeted suppression/removal/inversion

## Artist Syntax

For artist tags, preserve the NovelAI artist: namespace:

1.0::artist:example_artist::
0.55::artist:secondary_artist::

When the user provides a pool of artist tags, do not strip artist: or normalize special syntax unless explicitly asked.

## Negative

Omit Negative by default when the user already has a fixed Undesired Content / Negative setup.

## Philosophy

Prefer dense visual tokens over long descriptive paragraphs, while preserving the blueprint's key composition and causal relationships.
