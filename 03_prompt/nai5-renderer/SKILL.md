---
name: nai5-renderer
description: Thin NovelAI V5 community renderer that converts a Visual Prompt Packet plus verified Danbooru tags into the user's compact NAI5 prompt format. Handles artist namespace, weighting syntax, scene and character blocks, interaction tags, ordering, and optional targeted negatives. Does not design.
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
输出：可直接复制的 NovelAI V5 community-style prompt。

上游：visual-prompt-core → danbooru-tag-gate
下游：user-facing NAI5 prompt
不做：不重新设计、不维护长期 artist pool、不发现未经验证的 artist tag、不负责通用审美。

## 硬规则

- Preserve canonical verified Danbooru identity.
- Preserve the user artist namespace: artist:name.
- Artist membership and permanent blacklist belong to personal-identity-profile; renderer only composes the selected stack.
- Current compact default: use the owner's active artist policy rather than hard-coding a second personal policy here.
- Weight syntax is target syntax, not design logic: primary / support differences are serialized with NAI5 weight::tag:: form.
- Put high-priority subject and composition anchors early.
- Use char1 / char2 and source# / target# / mutual# only when multi-character structure requires them.
- Keep scene information only when it affects composition, action, light, scale, or narrative reading.
- Negative is omitted by default unless requested or necessary for a specific targeted correction.
- Do not solve design-layer problems by adding more tags.
- Model-behavior claims use Kernel evidence labels.

## Rendering flow

1. Read style intent from the Packet and obtain the selected artist pool from Identity when artist output is required.
2. Keep only verified high-value tags; omit generic support tags that are redundant with stronger structure.
3. Serialize the shared style / quality / rendering intent using NAI5 community syntax.
4. Order the result as:
   subject / framing anchor → year or era when relevant → artist layer → quality / rendering when requested → scene → character detail → action / interaction → optional tail.
5. For one character, use a compact char1 block only when it improves isolation or interaction readability.
6. Preserve causal relations with concise compound tags or ordering; do not turn the prompt into prose.
7. Apply compression and the Packet's output policy.
8. Run Design Lock before emission.

## Artist handling

The renderer receives eligible artists from the user's pool. It does not invent or permanently rank them.

Default personal policy is defined by the current Identity source. Historical conflicting mixer policies must not be recreated here.

When the user says artist names only / artist exploration, bypass normal content compilation and emit the requested artist stack under the current NAI5 artist-pool rules.

## Output contract

Normal output is one copyable NAI5 prompt in a single code block.

Do not emit bracketed Markdown section headings into the actual prompt.

Do not emit Negative by default.

## Acceptance

- [ ] artist namespace preserved
- [ ] only verified hard tags used
- [ ] subject / framing are near the front
- [ ] no duplicate quality / artist layer
- [ ] no design invention
- [ ] compact output
- [ ] user fixed Negative remains external unless requested
