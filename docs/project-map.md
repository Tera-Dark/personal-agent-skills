# Personal Agent Skills Project Map

## Architecture

```
User Request
    |
Router
    |
Core Identity + Aesthetic Direction
    |
Creation Skills
    |
Model Adapters
    |
Tools
```

## Modules

### 00_core
- personal-identity-profile: stores creator preferences, constraints and workflow style.
- aesthetic-director-core: converts requests into creative decisions.

### 01_router
- creative-skill-router: selects the correct workflow and prevents skill overlap.

### 02_creation
- character-design-engine: character identity, costume and personality.
- illustration-direction: composition, story and atmosphere.
- nai5-community-prompt-engineering: NovelAI v5 prompt translation.
- anima-prompt-engineering: Anima natural language prompt translation.

### 03_analysis
- image-reverse-analysis: extracts visual language from references.
- prompt-analysis: analyzes and improves prompts.

### 04_tools
- comfyui-workflow: generation workflow management.
- lora-training: training workflow knowledge.
- dataset-management: dataset preparation.
