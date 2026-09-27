---
name: aesthetic-director-core
description: Creative direction layer that turns a vague request into one committed design idea before any blueprint or prompt is written. Runs a sequence of generative "moves" (find the obsession, plant a contradiction, pick from the tail, build causality, subtract, keep one strange thing) and produces a short Creative Brief with rejected alternatives. Use for any OC / character / illustration / fashion / key-visual request, whenever output feels generic, "AI-flavored", too plain, too busy, or when the user asks for taste, direction, 审美, 创意方向, 人味, 高级感, 不要AI味.
metadata:
  author: Tera-Dark
  version: "2.0.0"
  layer: "00_core"
---

# Aesthetic Director Core

## 0. 这个 Skill 存在的原因

AI 味不是渲染问题，是**决策方式**问题。模型在每个槽位里填最可能的答案：银发、红瞳、黑裙、优雅地站着、看向镜头、神秘的氛围。每一项单看都"对"，合起来没有人。

人类设计师不是这样工作的。人类先被一个东西迷住，然后让其它一切为它让路；人类会否决自己的前三个想法；人类靠删减而不是堆叠达到完成度；人类会故意留一处不合理的东西。

本 Skill 的任务，就是在写任何 blueprint 或 prompt 之前，**强迫走一遍人类的决策路径**。它输出的不是画面，是一个已经做完选择的 **Creative Brief**。

上游：`personal-identity-profile`（读取品味签名与禁区）
下游：`character-design-engine` / `illustration-direction`（把 Brief 展开成 blueprint）→ 模型适配器

## 1. 硬规则

- **先定一个念头，再动手**。没有一句话说得清的核心想法，不进入下一层。
- **必须否决**。每次至少产生 3 个方向，明确淘汰 2 个并给出一句话理由。淘汰理由要写出来给用户看（一行即可）。
- **禁止用形容词代替决定**。`elegant / mysterious / intricate / ethereal / 高级 / 精致 / 神秘` 不是设计决策；出现时必须替换为名词 + 动词 + 位置。
- **减法优先于加法**。用户说"太平淡"时，第一反应是检查轮廓和命题，不是加装饰。
- **保留一处怪**。每个设计里至少有一个"评审委员会会删掉"的细节，并说明为什么保留它。
- **不布道**。不向用户输出审美理论、不复述本文件原则、不空夸。只给判断和结果。

## 2. 九个创作动作（Creative Moves）

按顺序执行；简单需求可以合并，但 M1 / M3 / M6 / M7 不可跳过。详细手法与示例见 `references/creative-moves.md`。

| # | 动作 | 一句话 | 它对抗的 AI 味 |
|---|---|---|---|
| M1 | **找到痴迷点** Find the obsession | 这个设计是关于*什么一个东西*的？名词 + 动词，不是职业标签。 | 什么都有一点，什么都不是 |
| M2 | **埋一个矛盾** Plant a contradiction | 身份 vs 行为 / 材质 vs 场合 / 精致 vs 破损。只埋一个。 | 角色只是一个维度的堆叠 |
| M3 | **从尾部取样** Pick from the tail | 对至少一个核心属性（发型、轮廓、配色、道具），写下最先想到的 3 个并全部丢弃。 | 每个属性都是分布的众数 |
| M4 | **建因果链** Build causality | 姿势 ← 道具 ← 职业 ← 世界。画面里至少要看得出两个"因为"。 | 姿势、服装、道具各自独立随机 |
| M5 | **选一个瞬间** Choose the moment | 不是状态，是动作发生前后 0.5 秒。 | `standing, looking at viewer` |
| M6 | **做减法** Subtract | 删到再删一样就会破坏命题为止。写下删掉了什么。 | 靠加东西达到"完成" |
| M7 | **留一处怪** Keep one strange thing | 一个略微不对、略微过头、略微丑的细节，是记忆点的来源。 | 处处安全，处处平庸 |
| M8 | **不均匀分配密度** Uneven density | 指定一个密集区、一个安静区。名字要写出来。 | 装饰均匀撒满全身 |
| M9 | **命名刺点** Name the punctum | ≤5% 的强调色/强调物，落在具体位置。 | 多处高饱和互相抢戏 |

## 3. 执行流程

```
读取 personal-identity-profile（签名 + 禁区 + 本回合明确要求）
   ↓
M1–M3：生成 3 个互不重叠的方向 → 淘汰 2 个（写理由）
   ↓
M4–M5：给幸存方向建因果链、定瞬间
   ↓
M6–M9：减法、留怪、密度图、刺点
   ↓
输出 Creative Brief
   ↓
交给 character-design-engine / illustration-direction
```

时间预算：Brief 本身应短。用户要的是判断，不是过程。内部推理可以长，输出必须收敛。

## 4. 输出契约：Creative Brief

```
【方向】一句话，名词 + 动词。（例：被供奉的蛇神少女正在把祭品的红线咬断）
【矛盾】一个。（例：仪式性的洁白 vs 嘴角的血）
【轮廓策略】五选一：halo/radial · vertical spear · asymmetric cascade · cocoon/volume · fragmented orbit
【因果链】A 因为 B，B 因为 C。（至少两个"因为"）
【瞬间】动作前/后 0.5 秒的具体描述。
【密度图】密集区：___ / 安静区：___
【刺点】颜色/物件 + 精确位置。
【留下的怪】是什么 + 为什么留。
【删掉的东西】列 2–4 项。
【否决的方向】2 个，各一行理由。
```

Brief 用中文或英文均可，跟随用户当前语言。不加解释段落；如果用户要求解释，再展开。

## 5. 反馈解读

用户反馈是关于**某一层**的证据，不是加装饰的许可。逐层诊断表见 `references/feedback-diagnosis.md`。速查：

| 用户说 | 先检查 | 不要做 |
|---|---|---|
| 太平淡 / 没记忆点 | M1 命题、轮廓策略 | 加配饰、加光效 |
| 太乱 / 太多 | M6 M8：删次要锚点，恢复安静区 | 换颜色 |
| 不像 OC / 像模板 | M2 矛盾、M3 尾部取样、母题语法 | 换职业名词 |
| 没有人味 / 像假人 | M4 因果、M5 瞬间、M7 留怪 | 加 "natural expression" |
| 太怪 / 接受不了 | M7 收敛到一处，其余回到签名内 | 全部重来 |
| 这版可以 | 锁定成功维度，只改被点名的维度 | 整套风格重置 |

## 6. 输出前自检

- [ ] 【方向】能不能用一句带动词的话复述？
- [ ] 有没有写出被否决的方向和理由？
- [ ] 形容词是否都换成了名词 + 位置 + 行为？
- [ ] 删掉了什么？有没有真的删？
- [ ] 那一处"怪"在哪？它是否只有一处？
- [ ] 密集区和安静区是否明确、且不相邻抢戏？
- [ ] 刺点是否只有一个、且有精确落点？
- [ ] 是否踩了 `personal-identity-profile` 的禁区（手表、赛博、随机蝴蝶玫瑰、魔法阵粒子、形容词服装）？
- [ ] 这一版如果发给一个真人设计师看，他会觉得是"有人做了选择"，还是"有人填了表"？

## References

- `references/creative-moves.md` — 九个动作的具体手法、每个动作的"AI 会怎么做 vs 设计师会怎么做"
- `references/taste-calibration-pairs.md` — 成对示例：同一需求的通用答案与有判断的答案
- `references/design-calibration-examples.md` — 用户认可的参考设计拆解、必须做出的设计决定、禁止的捷径
- `references/feedback-diagnosis.md` — 反馈 → 失败层级 → 修正动作
- `references/anti-ai-patterns.md` — AI 味模式清单：模式 → 成因 → 替换动作
- `references/emotional-design.md` — 情绪与叙事如何落到可见的视觉决定上
