# AGENTS.md

This repository is an LLM harness for Tera-Dark's creative work: character / illustration design plus model-agnostic prompt planning and target renderers.

Core product priorities: personal use, web-first, lightweight and easy to use. A new chat should work from a link without installation. Prefer selective loading and fewer user steps; do not add services or infrastructure without demonstrated need. Preserve the owner's creative preferences and current-request precedence.

## When operating under the repository

1. Read \`bundle/HARNESS.md\` and follow it.
2. For normal creative use, do not summarize the repository; explicit requests to inspect or review it take precedence.
3. Use the handshake and routing rules from the harness.

## When editing the repository

- Sources are \`kernel/\`, \`harness.json\`, \`VERSION\`, and the numbered source layers.
- \`bundle/\` and \`docs/skill-registry.md\` are generated; do not edit them by hand.
- After changes, run:
  \`python3 scripts/validate_skills.py && python3 scripts/build.py\`
- v4.0 ownership:
  - \`personal-identity-profile\` owns persistent user taste and NAI5 artist identity.
  - \`aesthetic-director-core\` owns creative decision-making.
  - \`character-design-engine\` / \`illustration-direction\` own blueprints.
  - \`visual-prompt-core\` owns model-agnostic prompt planning.
  - \`danbooru-tag-gate\` owns tag evidence.
  - \`anima-renderer\` / \`nai5-renderer\` own target syntax only.
- Adding a capability follows \`kernel/EXTENSION-PROTOCOL.md\`.
- \`scripts/install.sh [target]\` installs each discovered skill into the runtime skill directory.
