---
name: nai5-renderer
description: Thin NovelAI V5 renderer that converts a Visual Prompt Packet plus verified Danbooru tags into the user's compact NAI5 prompt format. Handles artist namespace, weighting syntax, base/character prompt fields, interaction tags, ordering, and optional targeted negatives. Does not design.
metadata:
  author: Tera-Dark
  version: "0.1.0"
  layer: "03_prompt"
  load: "on-demand"
  status: "active"
  triggers: "NAI5, NovelAI, NAI提示词, tag prompt, Danbooru prompt, artist stack"
---

# NAI5 Renderer

## 定位

输入：Visual Prompt Packet + verified Danbooru tags + user NAI5 artist-pool data when relevant。
输出：符合 NovelAI V5 实际输入结构、可直接使用的紧凑提示词。

上游：visual-prompt-core → danbooru-tag-gate
下游：user-facing NAI5 prompt
不做：不重新设计、不维护长期 artist pool、不发现未经验证的 artist tag、不负责通用审美。

## Blueprint boundary

This module is a target-model adapter. It accepts only a validated blueprint or Visual Prompt Packet and **does not design**. Missing design decisions must route upstream.

## 硬规则

- Preserve canonical verified Danbooru identity; never promote uncertain spellings into verified tags.
- Preserve the user artist namespace: artist:name.
- Artist membership and permanent blacklist belong to personal-identity-profile; renderer only composes the eligible selected stack.
- Weight syntax is target syntax, not design logic: primary / support differences are serialized with NAI5 weight::tag:: form.
- Put high-priority subject and composition anchors early.
- For multi-character V5, prefer NovelAI's official Base Prompt + separate Character Prompt fields. Base controls shared scene, style, framing, and subject counts; each Character Prompt owns one character's identity, appearance, outfit, props, expression, and character-specific action.
- Put count tags such as 2girls or 1girl, 1boy in the Base Prompt only. In each Character Prompt use the singular type tag such as girl, boy, or other, without a count.
- Keep one character's identity and features out of another character's prompt. Do not place literal labels such as char1: or char2: inside the actual prompt; those are internal planning labels only.
- For interactions, keep each participant's action in that participant's Character Prompt. Use source#action, target#action, or mutual#action where useful, then reinforce the relationship with short natural-language wording. Official guidance warns these markers are not always reliable by themselves.
- Character Prompt order usually influences character placement. Align field order with the intended left-to-right order; use Custom Character Positions when placement is critical.
- Use single-field pipe serialization (Base Prompt | Character 1 | Character 2) only when the user explicitly wants a one-block copyable prompt or cannot use separate fields. Official documentation describes this syntax, but recent community reports disagree about its current reliability on V5. Do not imply it is guaranteed; separate fields remain the default.
- Never mix pipe syntax with separate Character Prompt boxes. They are alternative input methods, not additive layers.
- Keep scene information only when it affects composition, action, light, scale, or narrative reading.
- Negative is omitted by default unless requested or necessary for a specific targeted correction.
- Do not solve design-layer problems by adding more tags.
- Model-behavior claims use Kernel evidence labels: [Official], [Community], [Personal experiment], or [Unverified].

## Rendering flow

1. Read style intent from the Packet and obtain the selected artist pool from Identity when artist output is required.
2. Keep only verified high-value tags; omit generic support tags that are redundant with stronger structure.
3. Serialize shared style / quality / rendering intent using NAI5 syntax, respecting the owner's fixed output preferences.
4. For one character, emit one compact prompt block.
5. For two or more characters, emit a Base Prompt and a separate Character Prompt for each person by default. Keep global scene/style/count in Base; bind identity, visual traits, props, expression, and local action to each character.
6. When the user explicitly asks for a single copyable block, serialize the same structure with single pipe separators: base | char1 prompt | char2 prompt. Do not add literal labels or Markdown headings inside the prompt string. Add a brief V5 compatibility caveat only when it is useful to the user's workflow.
7. Preserve causal relations with concise compound tags or natural-language reinforcement; do not turn the prompt into a long paragraph.
8. Apply compression and the Packet's output policy.
9. Run Design Lock before emission.

## Artist handling

The renderer receives eligible artists from the user's pool. It does not invent or permanently rank them.

Default personal policy is defined by the current Identity source. Historical conflicting mixer policies must not be recreated here.

When the user says artist names only / artist exploration, bypass normal content compilation and emit the requested artist stack under the current NAI5 artist-pool rules.

## Output contract

- One character: one copyable NAI5 prompt in one code block.
- Multiple characters: by default, show Base Prompt and one Character Prompt per character in separate, compact code blocks, with labels outside the prompt text.
- If the user explicitly asks for a single-string / one-box version, provide the pipe-separated alternative and do not combine it with instructions to fill separate Character Prompt boxes.
- Do not emit bracketed Markdown section headings or internal labels into the actual prompt.
- Do not emit Negative by default.

## Acceptance

- [ ] artist namespace preserved
- [ ] only verified hard tags used
- [ ] subject count and shared scene belong to Base Prompt in multi-character mode
- [ ] each Character Prompt contains only its character's identity, features, props, and local actions
- [ ] interactions are clear from both action ownership and concise relation wording
- [ ] no mixing of pipe syntax and separate character fields
- [ ] no duplicate quality / artist layer
- [ ] no design invention
- [ ] compact output
- [ ] user fixed Negative remains external unless requested

## References
- references/community-format.md — NAI5 prompt fields, syntax and output conventions.
- references/character-block.md — per-character prompt structure and field ownership.
- references/interaction-tags.md — multi-character interaction syntax and reliability limits.
- references/artist-stack.md — renderer-side artist namespace and weighting syntax.
- references/style-layer.md — NAI5 quality, complexity and rendering layer.
- references/scene-block.md — scene ordering and environment handling.
- references/tag-taxonomy.md — compact tag ordering and semantic grouping.
- references/weighting.md — NAI5 weight syntax details.
- references/negative-strategy.md — targeted negative control.
- references/single-artist-test-protocol.md — controlled single-artist test procedure.
