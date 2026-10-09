# NAI5 Prompt Format and Output Conventions

## Evidence and scope

- [Official] NovelAI's Multi-Character Prompting documentation recommends one Base Prompt plus separate Character Prompt fields. The Base Prompt controls shared scene and style; each Character Prompt describes one character while minimizing feature leakage.
- [Official] The same documentation describes single-field pipe syntax as an alternative: Base Prompt | Character Prompt 1 | Character Prompt 2. Do not use pipe syntax when Character Prompt fields are already present.
- [Community] Reports dated 2026 describe inconsistent results from pipe syntax with V5. Treat it as a compatibility option, not the default for reliable V5 work.

Official reference: https://docs.novelai.net/en/image/multiplecharacters/
Community report: https://www.reddit.com/r/NovelAi/comments/1vwhgug/v5s_claimed_22_character_support_only_getting_45/

## Default organization

Use the following as output-field labels, not as literal text inside the prompt:

- Base Prompt
- Character Prompt 1
- Character Prompt 2
- Additional Character Prompt fields as needed

The Base Prompt owns:
- subject-count tags (such as 2girls or 1girl, 1boy)
- shared setting, time, atmosphere, lighting and background
- framing, camera and overall composition
- global style and shared props
- relationships that need to read across the whole scene

Each Character Prompt owns:
- one singular subject-type tag (girl, boy, or other; no number)
- identity and signature appearance
- hair, face, eyes, expression and outfit
- character-specific accessories and props
- the character's own pose, gesture and action
- that character's side of an interaction

Do not repeat the subject-count tags inside individual Character Prompts. Do not mix both characters' identity / outfit / action into the same Character Prompt.

## Single-field alternative

Only when the user explicitly needs one copyable field, or cannot access the Character Prompt UI, serialize the same structure as:

    2girls, outdoors, walking together, candid snapshot, global style and framing | girl, first character identity, distinctive appearance, outfit, own pose, source#interaction_action | girl, second character identity, distinctive appearance, outfit, own pose, target#interaction_action

This is an alternative syntax, not an extra layer. Never add pipe separators while also telling the user to fill separate Character Prompt boxes. The official documentation describes this syntax, but current V5 community compatibility reports conflict; prefer separate fields for V5 reliability unless the user's own testing confirms pipe behavior in their workflow.

## Weight syntax

NovelAI numerical emphasis:

    1.5::tag::
    0.5::tag::
    -1::tag::

- 1.0 is the baseline.
- Values above 1.0 strengthen.
- Values between 0.0 and 1.0 weaken.
- Negative values can suppress or invert a feature; use only for targeted correction.

## Artist syntax

Preserve the NovelAI artist namespace:

    1.0::artist:example_artist::
    0.55::artist:secondary_artist::

Do not strip artist: or normalize special syntax unless explicitly asked.

## Avoid

- Do not emit explanatory headings such as Base Prompt or Character Prompt inside the actual prompt.
- Do not use square-bracketed Markdown headings inside prompts; brackets may have model semantics.
- Do not overload the Base Prompt with long descriptions of both characters.
- Do not use relation markers as the only explanation of a complex interaction.
- Do not emit Negative by default when the owner has a fixed Undesired Content setup.

## Philosophy

Prefer dense visual tokens over long descriptive paragraphs, but preserve the image's composition and causal relationships.
