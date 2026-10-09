# NAI5 Multi-Character Prompt Fields

## Overview

[Official] NovelAI V5's recommended multi-character workflow uses one Base Prompt and one separate Character Prompt field per character. This isolation helps reduce feature leakage.

The headings below are for the human-readable answer only. Do not paste labels such as “Base Prompt” or “Character Prompt 1” into the prompt contents.

## Base Prompt

The Base Prompt defines what the image shares across characters:

- count tags, e.g. 2girls or 1girl, 1boy
- shared location, environment, time and lighting
- camera, framing, placement cues and composition
- global style / rendering cues
- common action and shared atmosphere
- the narrative event in concise terms

Example:

    1girl, 1boy, outdoors, city sidewalk, walking together, candid photography, slightly tilted camera angle, medium shot, natural daylight, muted cool colors, convenience store entrance

## Character Prompt structure

Use one Character Prompt field for each character, in the intended visual order.

Example:

    girl, character identity, signature hair and face, distinctive outfit, personal props, expression, pose, own action

    boy, character identity, signature appearance, outfit, personal props, expression, pose, own action

Recommended order:
1. singular subject type: girl / boy / other
2. canonical character identity
3. signature facial and hair features
4. outfit and distinctive accessories
5. personal props
6. expression
7. pose / gesture / action
8. short natural-language clarification when needed

## Rules

- Put subject-count tags only in the Base Prompt. Character fields use singular subject-type tags without counts.
- Keep each character's identity tokens near the beginning of its own field.
- Describe signature features before secondary decoration.
- Keep each character's outfit, props, expression and local action in that character's field.
- Avoid mixing two characters in one Character Prompt; shared scene and composition belong in Base.
- Character field order usually influences placement (commonly top-to-bottom / left-to-right). Keep it aligned with the intended composition; use Custom Character Positions for precise placement.
- Tags and natural language can coexist. Keep tag-like facts compact and use a short sentence to disambiguate a complex gesture.
- Do not write literal char1: / char2: labels in prompt contents. Those labels may be used internally only when discussing the structure.

Official reference: https://docs.novelai.net/en/image/multiplecharacters/
