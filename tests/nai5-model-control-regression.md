# NAI5 V5 控制与画面关系回归（2026-10-14）

> 这是**规范检查/人工试跑用例**，不是当前已运行的 V5 图像测试记录。标识：SPEC（文本符合契约）、IMAGE-PENDING（等待成图 A/B）。来源案例来自用户提供的《小克 V5》样本结果，非本仓库独立复现。

## 静态路径与所有权（SPEC）

| ID | 输入 | 期望 owner / 输出 |
|---|---|---|
| N5-OWN-01 | “漂亮神性少女，张力更足” | illustration-direction 先定观察者、决定性时刻和可见空间结果；Renderer 不创造新背景 |
| N5-OWN-02 | “低角度，全身，衣服原版” | Prompt Core 锁全身和原服饰；NAI5 `from below` + 具体前景近大远小 |
| N5-OWN-03 | “only prompt，无画师无质量” | NAI5 不注入 artist、masterpiece、year、complexity、Negative 或多余讲解 |
| N5-OWN-04 | “双人公主抱逆常识方向” | Character Prompt 由各自所有者描述 source/target，Base 不混身份 |
| N5-OWN-05 | “冷门角色” | Gate 只验 canonical；NAI5 输出外貌锚点，不能声称标签已被模型学会 |
| N5-OWN-06 | “假签名问题” | 正向负权重仅针对复现故障；不升级为全局默认 |
| N5-OWN-07 | “Anima Prompt” | 不把 NAI5 `source#` / `-1::...` 硬编码到共用 Packet 或 Anima Renderer |
| N5-OWN-08 | “高定服装视觉还原” | 可见衣件逐项绑定；时装舞台词不能擅自换成其它服装 |
| N5-OWN-09 | “完整全身 + 大脸特写” | 相互冲突必须回 Blueprint 决策，不靠形容词糊弄 |

## NAI5 试跑用例（IMAGE-PENDING；seed/画师/尺寸一致）

| ID | A/B 对照 | 重点检查 |
|---|---|---|
| N5-IMG-01 | `floating in sky` vs `2::floating in sky::, -1::standing::` | 站立感是否消失，悬浮腿姿更自然 |
| N5-IMG-02 | `from below, low angle` vs 可见的鞋/腰/下巴/天花板关系 | 腰部近大远小，不出现摄影机实体 |
| N5-IMG-03 | `high kick, kicking at viewer` vs 增加脚最大前景的句子 | 脚向观众、不挡面部 |
| N5-IMG-04 | `backlighting, silhouette` vs 说明正面柔和补光 | 露脸和逆光能否兼容 |
| N5-IMG-05 | 仅 `red theme` vs 逐服装件绑定红色 | 衣件颜色是否遵守设计锁 |
| N5-IMG-06 | 默认 vs `medium complexity` | 亮度/细节变化，并用相同画师样本 |
| N5-IMG-07 | 短人物名 vs verified full canonical + 衣服锚点 | 辨识度及服装一致性 |
| N5-IMG-08 | 全局“公主抱” vs 独立 source#/target# 角色槽位 | 主动/被动方是否正确，关节是否可信 |

## 执行记录模板

```text
case: N5-IMG-XX
state: IMAGE-PENDING | PASS | FAIL | INCONCLUSIVE
source: Community/source report | Owner A/B
model / date:
artist string:
prompt A / B:
seed / dimensions / steps / CFG:
visible result:
single changed variable:
decision: keep / revert / retest
```

**验收底线**：没有截图和固定条件不写 PASS；强画师/任务换了须重新 A/B。特殊透视和异种/多维概念若破坏美型与角色身份，先回设计层重做，而非无限加权。
