---
name: illustration-direction
description: Turns a Creative Brief into a model-agnostic illustration blueprint — the captured moment, camera and framing, figure-to-frame ratio, negative space, physical light sources, density map, narrative residue in the environment, and one atmosphere preset. Use for 插画, 氛围图, 竖屏, 半留白, 印象风, 故事感, key visual, poster, scene illustration, cinematic composition, or whenever a character needs to be placed into a moment rather than displayed on a plate. Never writes model-specific prompt syntax.
metadata:
  author: Tera-Dark
  version: "2.0.0"
  layer: "02_creation"
  load: "on-demand"
  status: "active"
  triggers: "插画, 氛围图, 竖屏, 半留白, 印象风, 故事感, key visual, poster, scene"
---

# Illustration Direction

## 定位

输入：Creative Brief（来自 `aesthetic-director-core`）+ 可选的角色 blueprint（来自 `character-design-engine`）。
输出：一份**画面 blueprint**。适配器只需翻译，不需要再决定"人放哪、光从哪来、留多少白"。

插画和立绘的区别：立绘展示角色，插画捕捉**一个时刻**。所以本 Skill 的第一个决定不是构图，是**瞬间**。

## 硬规则

- **先有瞬间，再有构图。** 构图是为了让那个瞬间被看见，不是为了"好看"。
- **人物不默认居中、不默认看镜头、不默认占满画面。** 每一项都需要理由。
- **光必须有物理来源。** 一个主光源 + 方向 + 衰减 + 阴影沉降区。禁止无来源 rim light。
- **背景只保留能解释光或动作的那一层。** 窗 + 城市 + 星空 = 三层无关背景 → 留一层。
- **氛围元素（花瓣、粒子、光点、蝴蝶）默认删除。** 空由留白、叙事残留、光的衰减来填。
- **氛围预设一次只开一个。** 见 `references/atmosphere-presets.md`。

## 执行流程

```
Step 1  瞬间        Brief 的【瞬间】：动作前后 0.5 秒。前 1 秒和后 1 秒分别发生了什么？
Step 2  人物占比    人物占画面多少？1/3 / 1/2 / 2/3 / 特写。半留白/印象风默认 ≤1/2。
Step 3  位置与视线  人物在画面哪个区域（三分线）；她在看什么（画内物 / 画外 / 无）；视线方向决定留白方向。
Step 4  机位        由姿势类型决定（展示 / 操控 / 回身 / 仪式 / 脆弱 → 对应机位，见 oc-design-system § Layer 5）。
                    相机高度、方向、裁切、前景遮挡（sub-framing）有无。
Step 5  主光源      一个。位置、方向、色温、衰减。如果有第二光源，它和主光源的**关系**就是主题（Pair 3：窗光胜过灯光）。
Step 6  密度图      密集区 / 安静区 / 连接两者的动线。安静区通常是大块单一材质的墙、天、地、布。
Step 7  叙事残留    环境里一件东西的状态说明发生过什么：烟痕、一地的东西、未收的物、磨损的地面。
Step 8  氛围预设    从 references/atmosphere-presets.md 选一个（或不选）。预设只调光 / 色 / 材质 / 神态，不加物件。
Step 9  减法        删背景层、删氛围物、删第二光源（除非它是主题）。写下删了什么。
```

## 输出契约：Illustration Blueprint

```
## [画面代号]

**瞬间**：她正在___。前一秒___，后一秒___。
**画幅与占比**：竖/横，比例；人物占___，位于___（三分线位置）。
**视线**：看向___；留白在___侧。
**机位**：___高度，从___方向，___裁切；前景遮挡：___/无。
**主光源**：来自___，___色温，衰减到___；阴影沉降在___。第二光源（若有）：___，与主光的关系是___。
**密度图**：密集区___ / 安静区___ / 动线___。
**环境**：只保留___（它解释了光/动作）。
**叙事残留**：___
**氛围预设**：___（或无）
**刺点**：___在___。
**留下的怪**：___
**删掉的**：___
**锁定事实**（角色 blueprint 中不可更改的）：___
```

## 立绘模式（白底 / 展示板）

如果任务其实是立绘而不是插画（白底、设定图、展示板），走 `references/composition-patterns.md`：景别协议、前景立绘 + 背景放大头像的分层展示、设定三视图、表情差分。核心原则：**背景空，构图不空**——空由轮廓、接地影、包边线、一件有叙事的地面物来填。

## 自检

- [ ] 能说出前 1 秒和后 1 秒吗？
- [ ] 人物居中 / 看镜头 / 占满画面——如果是，理由是什么？
- [ ] 光源有位置和衰减吗？画面里有敢于压暗的区域吗？
- [ ] 背景是一层还是三层？
- [ ] 花瓣、粒子、光点删干净了吗？
- [ ] 安静区够大吗？缩略图里能看出重的地方在哪吗？
- [ ] 叙事残留是她造成的吗？
- [ ] 只开了一个氛围预设吗？

## References

- `references/composition-patterns.md` — 景别协议、分层展示板、设定图、三分偏置、sub-framing、极端机位（英文短语可直接进 prompt）
- `references/atmosphere-presets.md` — 去 AI 塑料感六维度 + 五个氛围预设（商业头像 / 清新日系 / 高定极简 / 暗黑叙事 / 电影海报）+ 选择决策流
