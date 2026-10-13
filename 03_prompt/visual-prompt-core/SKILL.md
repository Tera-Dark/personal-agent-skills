---
name: visual-prompt-core
description: Model-agnostic prompt planning layer that converts a validated character or illustration blueprint into one compact Visual Prompt Packet shared by Anima, NAI5, and future image-model renderers. Use after design is complete and before any model-specific prompt syntax. Does not redesign the concept or emit target-model syntax.
metadata:
  author: Tera-Dark
  version: "0.1.0"
  layer: "03_prompt"
  load: "on-demand"
  status: "active"
  triggers: "prompt packet, visual prompt, prompt core, 提示词编译, 提示词规划, NAI5, Anima"
---

# Visual Prompt Core

## 定位

输入：通过 Aesthetic / Blueprint Gate 的 character blueprint、illustration blueprint，或经过 AUDIT 的 finished-design packet。
输出：一个模型无关的 Visual Prompt Packet，供 anima-renderer、nai5-renderer 或未来 renderer 使用。

上游：character-design-engine / illustration-direction，必要时 aesthetic-director-core
下游：model renderer
不做：不重新设计、不选择具体模型语法、不替用户发明缺失设计。

## 硬规则

- 设计与编码分离：先结构化设计事实，再翻译成模型语法。
- 共享优先：任何 Anima / NAI5 都需要的规则只在这里拥有一份。
- 模型无关：不要写 Anima 转义、NAI5 namespace、权重或 char1 语法；这些属于 renderer。
- 设计锁定：保留用户锁定事实、核心命题、宏观轮廓、构图、动作、签名结构、唯一刺点和必要环境关系。
- **镜头保真是设计锁的一部分**：只编译 illustration blueprint 已决定的观看立场、机位侧向/高度/距离、前中后遮挡、裁切和关键清晰度；没有 camera intent 时退回 illustration-direction，renderer 不得用 `cinematic`、`35mm` 等空泛标签补设计。
- 最小充分：不因为“完整”而重复同义词。
- Tag 表达稳定视觉事实；Relation 表达位置、因果、遮挡、承重、动势和材质关系。
- 外部模型行为断言遵守 Kernel 的证据规则。

## 执行流程

1. 输入检查：确认已过 Aesthetic / Blueprint Gate；缺失核心设计则退回上游。
2. Style Layer：整理 artist intent、quality intent、rendering、complexity，不输出模型专属语法。
3. Visual Facts：提取 subject、identity、appearance、clothing、props。
4. Camera-first Composition：先读取上游已批准的 camera intent、captured moment、camera side/height/distance、foreground/midground overlaps 和 deliberate crop，再提取 framing、silhouette、motion axis、density、negative space；不允许按 Prompt 惯用模板擅自恢复正面全身镜头。
5. Scene & Action：组织 environment、pose、gesture、event 和物理光/空间关系。
6. Relations：保留因果、遮挡、层级、材质和视觉动线，不重复成 tag。
7. Signature：保留 punctum、strange detail 和唯一关键记忆点。
8. Tag candidates：标记值得进入 Danbooru Gate 的高价值视觉事实；不在此处证明 tag 存在。
9. Compression：删除同义重复、装饰性解释和可由更高层事实推出的枝节。
10. Design Lock：对照 blueprint，确认没有改设计、添设计或丢关键事实。
11. Output Policy：应用用户的默认隐藏/展开策略。
12. Packet emission：输出紧凑 Visual Prompt Packet。

## Visual Prompt Packet

使用以下稳定字段；空字段省略，不为了填表而填。

yaml shape:

style:
  artists:
  quality:
  rendering:
  complexity:

subject:
  count:
  identity:
  appearance:

character:
  hair:
  face:
  outfit:
  accessories:
  props:

composition:
  framing:
  camera:
  camera_intent:
  camera_position:
  depth_and_occlusion:
  deliberate_crop:
  focal_hierarchy:
  silhouette:
  motion_axis:
  visual_mass:
  density:
  negative_space:

scene:
  environment:
  background:
  objects:

action:
  pose:
  gesture:
  event:

relations:
  character_environment:
  pose_clothing:
  character_prop:
  visual_flow:
  material_interaction:

signature:
  punctum:
  strange_detail:

locked_facts:
rejected:
tag_candidates:

compression_policy:
output_policy:

## Shared layer rules

### Style

保存“想要什么视觉语言”，而不是具体字符串。Artist 是 identity/style intent；质量是 quality intent；renderer 决定是否实际展开。

### Tags

只把稳定、可验证、对画面有高控制价值的视觉事实标为 candidate。不要把每个 noun 都变成 tag。

### Relations

摄影设计中的前景遮挡、中景人物、近大远小、重心支撑与裁切边界首先是**关系**，不应被压成 `cinematic, dynamic pose, dramatic angle` 的空泛词列。NAI5/Anima 编译需优先保留能被模型描绘的具体可见关系；焦段数字和镜头术语没有明确视觉后果时删除。

以下信息优先保持为关系：
- 左右 / 前后 / 内外层级；
- 角色与环境的接触、遮挡、反射、承重；
- 动作导致的头发、衣摆、饰品响应；
- 视觉动线和密度转换；
- 材质之间的对抗。

### Compression

删除顺序：
1. 同义重复；
2. 可由锁定事实推出的描述；
3. 无构图、身份或行动作用的装饰；
4. 解释“为什么好看”的废话。

不得删除：
- identity；
- framing / macro silhouette；
- essential pose / action；
- signature garment construction；
- punctum；
- locked facts；
- 会改变第一眼结构的关系。

### Design Lock

最终必须保持：
same subject
same locked facts
same thesis
same macro silhouette
same framing
same camera intent / position / occlusion / crop / focal hierarchy
same essential pose
same signature construction
same palette hierarchy
same punctum
same environment relationship

任何一项失败，都属于上游设计漂移，不得由 renderer 临时补救。

## 输出契约

内部只输出一个紧凑 Packet。需要给用户看的最终文本由 renderer 决定。

## 自检

- [ ] 输入已经通过 Aesthetic / Blueprint Gate。
- [ ] 没有重新设计。
- [ ] Shared 内容没有写入 Anima / NAI5 专属语法。
- [ ] tag candidate 只代表高价值视觉事实。
- [ ] 关系没有被压成无意义 tag 堆。
- [ ] Compression 没有删除核心结构和会改变观看关系的机位、遮挡、裁切信息。
- [ ] 同一 Prompt 中的景别、机位、裁切互相兼容（不能又大特写又全身完整展示）。
- [ ] locked facts / rejected items 没有丢失。
- [ ] Packet 足以支持 renderer 在不重新设计的情况下完成输出。
