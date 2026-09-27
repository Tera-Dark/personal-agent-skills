# NAI5 Weighting System

## Purpose

NovelAI V5 community prompts frequently use weighted syntax to control emphasis.

## Common Syntax

```text
1.5::tag::
0.5::tag::
-2::tag::
```

Positive values strengthen visual influence. Negative values suppress unwanted features.

## Weight Guidelines

- 0.25-0.75: subtle influence
- 0.8-1.5: strong influence
- 2+: aggressive emphasis, use carefully
- negative weights: style removal or correction

## Usage Principles

Do not weight every token. Reserve weights for:

- artist blending
- important style direction
- critical character traits
- unwanted style suppression

Avoid turning prompts into random weighted token piles.
