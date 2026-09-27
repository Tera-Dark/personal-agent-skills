# Skill Registry

Central index of all skills. The router uses this as its map. `scripts/validate_skills.py` cross-checks this table against the files on disk.

Skills reference each other **by name**, never by relative path — they may be installed to different locations (see `scripts/install.sh`).

| Skill | Layer | Purpose | Trigger examples | Status |
|---|---|---|---|---|
| `personal-identity-profile` | 00_core | Single source of taste: signature, dislikes, workflow voice | 我的风格, 个人偏好, any creative task (loaded first) | active |
| `aesthetic-director-core` | 00_core | Nine creative moves → Creative Brief with rejected alternatives | any OC / illustration / fashion request; 审美, 人味, 太平淡, 不要AI味 | active |
| `creative-skill-router` | 01_router | Intent classification and pipeline assembly | any creative request | active |
| `character-design-engine` | 02_creation | Brief → model-agnostic character blueprint | OC, 人设, 角色设计, 服装设计, 立绘 | active |
| `illustration-direction` | 02_creation | Brief → model-agnostic illustration blueprint | 插画, 氛围图, 竖屏, 半留白, 故事感 | active |
| `anima-prompt-compiler` | 02_creation | Adapter: blueprint → Anima Tag + NL prompt | Anima, Anima 提示词 | active |
| `nai5-community-prompt-engineering` | 02_creation | Adapter: blueprint → NAI5 community format | NAI5, NovelAI, tag prompt | active |
| `image-reverse-analysis` | 03_analysis | Reference image → structural design language | 反推, 分析图片, 参考这张 | active |
| `prompt-analysis` | 03_analysis | Existing prompt → intent / weakest layer / noise / fix | 优化提示词, 这个 prompt 哪里有问题 | active |
| `comfyui-workflow` | 04_tools | ComfyUI operations | ComfyUI, workflow, nodes | placeholder |
| `lora-training` | 04_tools | LoRA training workflows | LoRA, 训练, fine-tune | placeholder |
| `dataset-management` | 04_tools | Dataset preparation | dataset, 打标, captions | placeholder |
| `evaluation-loop` | 05_evaluation | Rubric + design read → which layer to fix | 太平淡, 太乱, 这版可以, 评价一下 | active |

## Routing principle

One skill, one responsibility.

- Taste lives in `personal-identity-profile` only.
- Creative decisions are made in `aesthetic-director-core` and expanded by `character-design-engine` / `illustration-direction`.
- Adapters translate; they never design. If an adapter receives a request instead of a blueprint, it routes back.
- Feedback goes through `evaluation-loop`, which decides which layer owns the fix.

## Removed in v2.0.0

| Removed | Reason | Superseded by |
|---|---|---|
| `skills/creative-prompt-router` | duplicate router pointing at stale skill names | `creative-skill-router` |
| `skills/nai5-prompt-engineering` | duplicate NAI5 adapter | merged into `nai5-community-prompt-engineering` |
| `02_creation/anima-prompt-engineering` | 7-line stub shadowing the real compiler | `anima-prompt-compiler` (moved into 02_creation) |
| `docs/tera-aesthetic-profile.md` | third copy of the taste profile | `personal-identity-profile/references/taste-signature.md` |
