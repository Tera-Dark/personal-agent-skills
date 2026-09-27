---
name: character-design-engine
description: Turns a Creative Brief (from aesthetic-director-core) into a complete, model-agnostic character blueprint — design thesis, silhouette architecture, visual anchors, garment engineering (base / structural / signature extension / accessory system), material contrast, palette hierarchy, behavioral pose + camera, narrative residue, presentation format — then runs a subtraction pass. Use for OC, 人设, 角色设计, 服装设计, 立绘, 高定服设, 二游角色, character sheet, fashion concept. Never writes model-specific prompt syntax.
metadata:
  author: Tera-Dark
  version: "2.0.0"
  layer: "02_creation"
---

# Character Design Engine

## 定位

输入：`aesthetic-director-core` 产出的 **Creative Brief**（方向、矛盾、轮廓策略、因果链、瞬间、密度图、刺点、留下的怪、删掉的东西）。
输出：一份**角色 blueprint**，任何模型适配器都能直接翻译，且不需要再做设计决定。

如果被直接调用而没有 Brief：先用 `aesthetic-director-core` 的 M1 / M3 / M6 / M7 压缩跑一遍（内部完成，不必输出完整 Brief），再进入下面的流程。**不要跳过。** 跳过的结果就是表单填充。

本 Skill 不写 Anima / NAI5 语法。本 Skill 不重新决定品味——品味来自 `personal-identity-profile`。

## 为什么不是一张表

上一版的输出契约是 `Identity: / Background: / Silhouette: / Costume: / ...` 十三个空格。空格会被填满，而且每格填的都是最常见值。
这一版的输出是**一串有先后依赖的决定**：后面的每一项都由前面的项推出。如果某一项推不出来，说明前面的决定没做实。

## 执行流程

详细手法见 `references/oc-design-system.md`（六层结构、轮廓策略、复杂度控制、反平庸检查）。

```
Step 1  命题        从 Brief 的【方向】开始。一句话，含动词。写不出动词 → 退回 director。
Step 2  轮廓策略    五选一：halo/radial · vertical spear · asymmetric cascade · cocoon/volume · fragmented orbit
                    写出空间关系：behind the head / wrapping the torso / descending from one shoulder
Step 3  视觉锚点    1 个主锚点（头/胸/腰/背/手中物 五选一）+ ≤2 个次锚点。主锚点 = Brief 的密集区。
Step 4  服装工程    Base garment → Structural garment → Signature extension → Accessory system
                    每一层写「形状 + 位置 + 功能/运动」，不写形容词。词汇见 references/garment-lexicon.md
Step 5  材质对抗    至少一组：哑光 vs 反光 / 柔软 vs 硬质 / 织物 vs 生物 / 粗糙 vs 光滑。绑定到具体结构。
Step 6  配色层级    基底 60–75% / 结构色 20–30% / 刺点 ≤5%。每个颜色写落点。刺点 = Brief 的刺点。
Step 7  姿势 + 镜头 姿势由 Brief 的【瞬间】和【因果链】给出。镜头由姿势类型决定（展示/操控/回身/仪式/脆弱 → 对应机位）。
Step 8  叙事残留    一件东西的状态说明发生过什么。必须是她行为的结果。
Step 9  展示方式    clean plate / decorated key visual / editorial plate / environmental vignette
Step 10 减法        对 Step 4–9 的每一件东西问"删掉它命题还在吗"。在 → 删。写下删了什么。
Step 11 反平庸检查  references/oc-design-system.md § 4
```

## 输出契约：Character Blueprint

用连贯的短段落写，不用空表格。每段开头是决定，后面是它的依据。适配器需要的所有事实都要在里面，用**名词 + 位置 + 行为**表达。

```
## [角色名或代号]

**命题**：一句话。
**轮廓**：策略 + 空间关系 + 缩略图里能认出的那个形状。
**锚点**：主锚点在___；次锚点在___、___。安静区在___。
**服装**：
  - Base：
  - Structural：
  - Signature extension：
  - Accessory system（同一形态语法）：
**材质对抗**：___ vs ___，落在___。
**配色**：基底___ / 结构___ / 刺点___（位置）。
**外观**：发（形状、长度分布、颜色——不是"银色长直"）、眼、肤、种族特征。
**姿势与镜头**：她正在___（瞬间）。因为___所以___（因果）。机位___，视线___，手___。
**叙事残留**：___
**展示方式**：___
**留下的怪**：___，因为___。
**删掉的**：___、___、___。
**否决的方向**：① ___ ② ___
**锁定事实**（用户明确给定、不可被适配器"优化"的）：___
```

## 多套设计

用户要 N 套时，每套之间至少在 **命题、轮廓策略、主锚点、材质语言、动作逻辑** 五项里有两项明显不同。不要出同一个设计的三个配色。

## 参考图输入

用户给参考图时，先走 `image-reverse-analysis` 提取**结构**（轮廓、密度分布、母题语法、颜色层级、材质、姿势逻辑、留白），再在这里换掉全部具体物件、保留结构。见 `aesthetic-director-core/references/taste-calibration-pairs.md` Pair 5。

## 自检

- [ ] 命题里有动词吗？
- [ ] 只有一个主锚点吗？
- [ ] 服装四层每层都有形状和位置，没有一处是形容词？
- [ ] 删掉颜色，轮廓还认得出？删掉装饰，基础服装还有独立剪裁？
- [ ] 姿势会改变头发 / 衣摆 / 道具 / 光的位置吗？
- [ ] 叙事残留是她造成的吗？
- [ ] 刺点只有一个、有精确位置？
- [ ] 有"删掉的"和"否决的方向"两行吗？
- [ ] 踩了 `personal-identity-profile/references/design-dislikes.md` 吗？
- [ ] 锁定事实完整传下去了吗？

## References

- `references/oc-design-system.md` — 六层结构、五种轮廓策略、姿势-镜头对应、展示方式、复杂度控制、反平庸检查、开放式请求默认行为
- `references/garment-lexicon.md` — 穿搭原型、四层叠穿、不对称手法、材质碰撞矩阵、领/袖/腰/裙词汇（英文短语可直接进 prompt）
