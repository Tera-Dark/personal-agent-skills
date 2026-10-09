# NAI5 Multi-Character Interaction Tags

## Core principle

Keep each participant's action in the Character Prompt belonging to that participant. The Base Prompt defines the overall event and composition; each Character Prompt clarifies what its character is doing in that event.

## Relation markers

[Official] NovelAI documents three optional markers for interactions:

- source#action — the active / initiating participant's action
- target#action — the passive / receiving participant's corresponding action
- mutual#action — an action genuinely performed mutually by both participants

These markers can improve relation clarity but are explicitly not always reliable by themselves. Use a known action tag when available, then reinforce unusual or nuanced interactions with concise natural language in the relevant Character Prompt.

Official reference: https://docs.novelai.net/en/image/multiplecharacters/

## Example pattern

Base Prompt:

    1girl, 1boy, couple, walking together, convenience store entrance, both holding takeaway drinks, candid snapshot, medium shot

Character Prompt 1:

    girl, first character identity, leaning toward the boy's cup, source#drinking, sneaking a sip from his drink, pretending nothing happened, mischievous smile

Character Prompt 2:

    boy, second character identity, holding a takeaway drink, target#drinking, noticing her with a helpless amused smile

The example illustrates ownership and direction; choose action tags that match the intended movement. Do not force a marker if the corresponding action tag is not suitable or is unverified.

## Rules

- Keep source / target ownership consistent across the involved character fields.
- Use mutual# only if both characters genuinely perform the same reciprocal action.
- A passive participant does not need an invented matching action if it would distort the scene.
- Use concise natural language to clarify nonstandard interactions, spatial direction, contact, gaze and causal sequence.
- Do not copy a complicated action into both character fields without changing its role; duplicated actions can blur who initiates the movement.
- Do not present source# / target# / mutual# as a guarantee or as a substitute for clear pose and spatial descriptions.
