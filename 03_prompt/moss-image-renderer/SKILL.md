---
name: moss-image-renderer
description: Thin OpenMOSS MOSS-Image renderer for turning approved Visual Prompt Packets into English Caption, optional Danbooru Tag, or native JSON Layout prompts. Uses verified tags only when needed; preserves visual design; never generates images.
metadata:
  author: Tera-Dark
  version: "1.1.0"
  layer: "03_prompt"
  load: "on-demand"
  status: "active"
  triggers: "MOSS-Image, MOSS Image, OpenMOSS, MOSS生图, moss prompt, moss tags, MOSS Layout, MOSS风格触发词"
---

# MOSS-Image Renderer

## 职责与共享边界

输入：**已经通过 Aesthetic Gate / Blueprint Gate 的 Visual Prompt Packet**，加上明确的目标 MOSS-Image-Base 或 MOSS-Image-SFT（未指定则不替用户宣称用的是哪个 checkpoint）。

输出：一个可以复制进 MOSS-Image Positive Prompt 的英文字符串：**Caption / Tags / Layout** 三选一。不能重新设计角色、镜头、背景、动作、色彩或作者姓名。用户没说生成图片，只输出文字提示词。

上游：character-design-engine / illustration-direction → visual-prompt-core；只有 Tags 模式或明确需要 canonical 身份时才请求 danbooru-tag-gate。下游：MOSS-Image positive prompt。若需要明确的 negative 或采样参数，分别给到相应输入字段，不能混入 Positive 造成污染。

### 模式选择（优先遵守用户指定）

1. **Caption（默认）**：普通二次元/写实/摄影/混合背景、电影情绪、lo-fi、带关系的双人画。采用连贯英文自然语言；内容顺序以可见关系为先：主体验证 → 决定性动作/构图 → *分对象*媒介处理 → 环境材质 → 光影、色彩、情绪。画面简单时保持简洁，不规定武断字数，也不灌空泛质量词。只输出 caption 正文；`{"caption":"..."}` 是官方 enhancer 的**草稿**，不是默认供模型粘贴的正文。
2. **Tags**：明确要纯标签、追求已验证角色/系列标签时使用。官方推荐顺序：Quality → Score → Meta → Year → Character → Series → Artist → General；各项**可为空**，个人默认不加画师、年份、质量串。MOSS 官方示例用 `@foo bar` 示意 artist 字段，**不是** NAI5 的 `artist:name`；用户明确不要画师，则不输出任何画师。仅把 Danbooru Gate **exact/alias** 的身份/关键事实当作 verified tag；普通自然语言风格短语是描述，不冒称 canonical tag。不要沿用 NAI5 的 `1.2::tag::` 或 Anima 的权重转义作为 MOSS 官方语法。
3. **Layout**：仅当明确要求结构化坐标、排版文字、复杂多面板，且空间规则对结果有实质价值时使用。实际输入必须是**官方模型面向的 JSON**：`summary` + 平铺 `items`，`bbox_format:"yxyx"`、`bbox_coord_space:"abs_centralized"`、`bbox:[y_min,x_min,y_max,x_max]`。不要把编辑草稿的左上原点 `xyxy` 直接交给模型。可以先用 `scripts/moss_layout.py` 或官方 enhancer 从 `width,height,abs,xyxy` 草稿编译；无法确认坐标时优先 Caption，不杜撰“已经过校验”。详细规则见 `references/layout-contract.md`。

## 官方 Prompt Enhancer 融合流程（2026-10-21）

与 OpenMOSS 官方 [moss-image-prompt-enhancer](https://github.com/OpenMOSS/MOSS-Image/tree/main/skills/moss-image-prompt-enhancer) 对齐，但**不照搬上游的创意决策职责**：美术方案和锁定事实仍由本 Harness 上游负责，Renderer 只在不改变方案的前提下做可见信息具体化、模式选择和格式编译。

1. **Brief / Design Lock**：保留人物/物体数目、关系、参考图锁定事实、机位、媒介边界、明确排除项和目标可见文字。引号里的引用内容不自动等于要印在图上的文字；先分清「画面字」与「指令/参考」。不臆造日期、品牌、地名或文案。
2. **Caption First**：用户未指定且布局没有精确控位需求时，输出连贯英文 caption。把可见的主体动作、材质、环境、机位、照明、色彩具体化；简单需求保持极简，丰富需求保持充实，不强制转成海报或模板、不堆空泛画质词。不因细节多就自动切 Layout。
3. **Typography / Spatial Planning**：只有独立定位文字、多面板、明确对象空间关系确实需要 boxes 时用 Layout。根据画布上的实际像素安排阅读顺序、字号与留白；**文字逐字、大小写、标点、换行保持原样**，不可用 `headline here` 等占位文案。允许自然遮挡/重叠，bbox 只代表位置而非让模型画出边框。
4. **Draft → Compile → Prompt**：Caption 编辑草稿是仅有 `{"caption":"..."}` 的 UTF-8 JSON，编译结果是**纯 caption 文本**；Layout 编辑草稿是带 width/height、`abs/xyxy` 的 JSON，编译后是**单行紧凑** `abs_centralized/yxyx` JSON。Tags 模式原样按既有 Tag Gate 规则导出，不强行套进官方仅支持 Caption/Layout 的编译器。
5. **机器校验**：在有本地 Shell / 文件能力时运行 `python3 scripts/moss_layout.py draft.json --output prompt.txt`，草稿与结果必须分文件，检查文字、坐标、画布一致再交付。输出的 width×height 是**生成设置**，不出现在最终 Layout prompt 中。无法运行脚本时不得宣称 Layout 已编译校验；按请求提供清楚标识的草稿或退回 Caption。
6. **尺寸和修订**：Layout 缺少画幅时默认 1024×1024，除非媒介本身有明确形状倾向；仅给比例时选匹配 16 的倍数。用户显式指定不兼容尺寸时报告冲突，不偷偷改。FAST VARIANT 只修改用户指明的文字/对象/框，其他全部原样保留，重新编译。

详细工作流、schema 和示例见 `references/official-enhancer-workflow.md`；与原有 `references/layout-contract.md` 同时适用。官方原始材料是上游规则证据，未出图的审美候选继续标记 [Candidate] / IMAGE-PENDING。

## MOSS 风格域与“触发词”边界

MOSS 官方确认三种输入**格式**、Tag 字段顺序和示例；未发布逐个被实验验证的“lofi/动漫截图/摄影混合风格触发词词典”。因此：

- `anime screenshot`、`hand-drawn 2D anime character`、`photorealistic environment`、`lo-fi album cover`、`matte cel shading` 等仅为**候选风格描述**，不是官方保证有效的特殊 token。
- 用**材质/空间的角色职责**消除串味：例如 *the girl is hand-drawn in clean 2D anime linework; the residential street behind her is photographic, with natural textures; both share the same overcast light and muted color grade*。
- 允许单独测试单词与自然语言的表现，但测试前不宣称哪组词强或有“模型风格解锁”效果。
- 不用指名非画师作者、电影导演或具体账号模仿；请求**不靠画师串**时，NAI5/Anima 的用户 artist pool 也不得偷渡进来。
- 风格组合只用 1–2 个核心媒介机制 + 具体可见约束，避免大量同义词造成背景/人物趋同。案例见 `references/style-control.md` 和 `references/examples.md`。

## 输出 / Design Lock

- Caption：**一整块可复制英文自然语言**，不加 `prompt:` 标签与技术旁白。
- Tags：只输出可复制逗号标签（必要可加一短句关系描述，但不称它为官方独立语法）；不带 `character 1:` / `|` 等 NAI5 特有角色框格式。
- Layout：一份严格 JSON，内含画面元素与坐标，不在 JSON 同一个代码块内混杂 Markdown。**width/height 是生成设置**；编辑草稿可有这两个字段，模型输入的最终 JSON 不应带它们。明确提醒所需画幅，如 1024×1536。
- Negative：Python 默认空，官方指南给出可选负面 `nsfw, worst quality, bad anatomy, watermark, jpeg artifact`；仅在用户提出或具体故障需要时单独给，不默认污染 Positive。
- 只在用户问工作流/参数时给设置建议，不将 CFG / steps / shift 写进 prompt。官方推理设置见 `references/official-spec-and-sources.md`。
- 保持模型无关 Packet 中 locked_facts、人物性别/数目、原服装、具体机位、动作关系、画幅与色彩职责；不额外添加樱花、路灯、雨夜、光斑或风格画师。
- 官方 [Official] 与候选 [Hypothesis]、用户真实跑图 [User-tested] 证据状态必须明确区分。未曾在 MOSS 实际跑图的候选默认标记 `IMAGE-PENDING`，不推断真实触发强度。
- **失败退化**：Caption 不因标签索引不可用而中止；确需核实的 Tag 若 Gate 不可用则降为描述；Layout 编译失败必须报告，不得假装合法。
- 用户仅说“输出提示词”，按 PROMPT ONLY 一整块交付，不生成图片。

- `references/visual-layout-workflow.md` — 2026-10-26 可视化拖框、第三方编辑器、坐标转换、海报范例、ComfyUI/Gradio 与误区排查。

## 验收

- [ ] 设计上游已完成，Renderer 无再创作。
- [ ] Caption / Tags / Layout 模式选对，风格词没有伪装为官方保证。
- [ ] 用户不要画师时未出现画师字段、权重或特定作者模仿。
- [ ] 二次元人物、写实背景、共同光色分别落实到了明确可见对象。
- [ ] Layout 坐标按 yxyx + abs_centralized、画布尺寸匹配且文本准确。
- [ ] 不携带其他模型独占串法；不加非请求 Negative/参数。
- [ ] 出图性能结论未高于证据强度。

## References

- `references/official-enhancer-workflow.md` — 2026-10-21 官方 enhancer 融合后的 Brief、文字、草稿与编译约束。
- `references/official-spec-and-sources.md` — 官网页、HF 模型卡、推理参数、格式边界（官方证据）。
- `references/style-control.md` — 候选风格描述库、跨媒介锚定方法、单变量测试协议。
- `references/layout-contract.md` — 官方 Layout 输入、草稿转换、坐标、文字与多面板。
- `references/examples.md` — Caption / Tags / Layout 可复制用例，均未声称出图验证。

- Visual JSON Layout practical guide: https://raw.githubusercontent.com/Tera-Dark/personal-agent-skills/main/03_prompt/moss-image-renderer/references/visual-layout-workflow.md
