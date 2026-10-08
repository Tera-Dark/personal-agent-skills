# Architecture

## v4.0 principle

The harness separates five responsibilities:

\`\`\`
Policy → Routing → Design → Prompt Planning → Rendering
\`\`\`

The most important change from v3.x is that Anima and NAI5 no longer own separate prompt-planning systems.

## Runtime

\`\`\`
User request
   ↓
Identity
   ↓
Router
   ├─ design
   │   ├─ character-design-engine
   │   └─ illustration-direction
   │
   ├─ analysis
   │   ├─ image-reverse-analysis
   │   └─ prompt-analysis
   │
   └─ prompt
       ↓
   Visual Prompt Core
       ↓
   Danbooru Tag Gate
       ├─ anima-renderer
       ├─ nai5-renderer
       └─ general-image-prompt-adapter
\`\`\`

Feedback enters through \`evaluation-loop\` and returns to the owner of the first failed layer.

## Module ownership

| Owner | Question |
|---|---|
| personal-identity-profile | What does the owner prefer? |
| creative-skill-router | Where should the task go? |
| aesthetic-director-core | Why should the design look this way? |
| character-design-engine | How is the character engineered? |
| illustration-direction | How is the image composed? |
| visual-prompt-core | How do we represent the design before model syntax? |
| danbooru-tag-gate | Is this hard tag proven? |
| anima-renderer | How is the packet expressed in Anima syntax? |
| nai5-renderer | How is the packet expressed in NAI5 syntax? |
| general-image-prompt-adapter | How is the packet expressed in natural-language models? |
| evaluation-loop | Which layer failed? |

## Visual Prompt Packet

The shared Packet is an internal intermediate representation, not a user-facing output:

\`\`\`
style
subject
character
composition
scene
action
relations
signature
locked_facts
rejected
tag_candidates
compression_policy
output_policy
\`\`\`

This is the stable boundary between design and model syntax.

## Shared vs target-specific

Shared in Prompt Core:
- style intent
- quality intent
- visual facts
- composition
- scene
- pose / action
- relations
- punctum
- compression
- design lock
- output policy

Target-specific in renderers:
- Anima Tag + NL structure and syntax serialization
- NAI5 artist namespace, weights, character/interaction tags and ordering
- Generic natural-language formatting and target notes

## Danbooru boundary

\`danbooru-tag-gate\` owns only tag evidence:

\`\`\`
exact | alias | missing
\`\`\`

It does not own:
- Anima escaping
- NAI5 weighting
- renderer ranking
- creative selection

This prevents a model-specific tag gate from becoming a second prompt-planning engine.

## Loading

Only session-wide policy and routing are always-on. Creative design, Prompt Core, tag validation, renderers, analysis and evaluation are on-demand or pipeline-packed.

The Web-first runtime may load a target prompt pack in one fetch:

\`\`\`
Anima pack = Visual Prompt Core + Danbooru Gate + Anima Renderer
NAI5 pack  = Visual Prompt Core + Danbooru Gate + NAI5 Renderer
\`\`\`

This keeps the shared logic identical across targets without requiring seven independent Anima fetches.

## Generated distribution

\`bundle/\` and \`docs/skill-registry.md\` are generated from source. \`harness.json\` is the runtime configuration; the Kernel defines the operating contract.
