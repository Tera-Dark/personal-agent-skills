# Architecture

## Principle

The harness separates five responsibilities and keeps output authorization separate from design:

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
MOSS pack  = Visual Prompt Core + MOSS Renderer (tag mode adds Danbooru Gate)
\`\`\`

This keeps the shared logic identical across targets without requiring seven independent Anima fetches.

Web sessions resolve a commit SHA and use it for the core and all on-demand raw URLs. If a pinned fetch is unavailable, the runtime falls back to main with version checks and an explicit consistency caveat. This reduces mixed-revision loads but cannot guarantee the SHA is the latest when a web tool caches the API response. Offline pasted content does not require this lookup.

## Generated distribution

\`bundle/\` and \`docs/skill-registry.md\` are generated from source. \`harness.json\` is the runtime configuration; the Kernel defines the operating contract.

## v4.6 runtime behavior

- `PROMPT ONLY` is an output overlay, not a shortcut around necessary design validation.
- Generating/editing an actual image is separate from designing an image prompt and needs an explicit request.
- FULL scales its design effort to the task; FAST VARIANT preserves approved facts.
- Kernel embeds a compact module-card index, not a duplicated index plus repeated descriptive cards.
- Offline CI checks the **pinned** tag snapshot. Third-party tag synchronization is manual through `workflow_dispatch` with `sync_tag_index` enabled.
- PRs rebuild and validate generated assets in CI; main branch CI commits refreshed bundle artifacts after a successful build.

### Lean identity residency

The startup bundle contains Identity's small policy contract and `taste-core.md`; the full `design-dislikes.md` and history remain retrievable only when required. This keeps the critical no-clock/no-accessory/anti-plastic-skin defaults in the compact baseline without repeatedly loading the full archive.

## v4.7 — evidence-driven NAI5 adapter, without second design pipeline

The core ownership model is unchanged. The new fast-path is **not** a new Skill:

```
Illustration camera intent + visible spatial facts
                    ↓
Visual Prompt Packet (visible_geometry; no model-specific tags)
                    ↓
Danbooru Gate (identity exact/alias/missing; NOT trained-model recognition)
                    ↓
NAI5 Renderer
  ├─ references/nai5-control-matrix.md (quick execution routing)
  └─ references/nai-v5-usage-guide.md (full reported experiments, on demand)
                    ↓
A/B evidence + evaluation-loop (no unverified PASS)
```

Key split:
- **Design decision**: visual thesis, decisive moment, viewer relation, which near/far object matters.
- **Shared compilation**: preserve near/relative scale/occlusion/face-readability, reduce redundant words.
- **V5 serialization**: map intended viewpoint to stable framing tags + one visible-geometry sentence; optional local positive negative weight only for a specific conflict.
- **Tag evidence**: canonical identity validation never implies the model recognizes a character; source-reported dataset timing/post-count are not hard rejection rules.
- **Testing**: `tests/nai5-model-control-regression.md` contains text-contract cases and *pending* paired-image studies; the specification is not proof of model output.
