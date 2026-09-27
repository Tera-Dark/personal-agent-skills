# Skill Registry

## Purpose

Central index of all skills in Personal Agent Skills Hub.
The router should use this document as a high-level map before selecting execution modules.

---

| Skill | Location | Purpose | Trigger Examples |
|---|---|---|---|
| personal-identity-profile | 00_core | User preferences and workflow context | personal style, preferences |
| aesthetic-director-core | 00_core | Creative judgment and anti-pattern control | design quality, taste |
| creative-skill-router | 01_router | Task routing and execution planning | any complex request |
| character-design-engine | 02_creation | Character concept creation | OC, character, setting |
| illustration-direction | 02_creation | Scene and composition design | illustration, artwork |
| nai5-community-prompt-engineering | 02_creation | NovelAI v5 prompt conversion | NAI5, NovelAI |
| anima-prompt-engineering | 02_creation | Anima prompt conversion | Anima workflows |
| image-reverse-analysis | 03_analysis | Image decomposition | reverse prompt, analyze image |
| prompt-analysis | 03_analysis | Prompt structure analysis | optimize prompt |
| comfyui-workflow | 04_tools | ComfyUI operations | workflow, nodes |
| lora-training | 04_tools | LoRA training workflows | training, fine-tune |
| dataset-management | 04_tools | Dataset preparation | dataset, captions |
| evaluation-loop | 05_evaluation | Output evaluation and iteration | improve result |

---

## Routing Principle

Skills should solve one responsibility only.

Creative planning belongs to creation skills.
Model syntax belongs to adapters.
Technical execution belongs to tools.
