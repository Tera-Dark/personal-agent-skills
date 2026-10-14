# Anima × Cinematic v4.7.1 回归清单（2026-10-14）

> **性质**：规范 SPEC + 人工/后续成图对照。这里没有实际 Anima/NAI5 图片实验记录；禁止把“规范通过”描述为“已跑图成功”。最新内容分别以 renderer 和 illustration-direction 来源文件为准，本文件只保存测试场景。

## 一、静态规范测试（SPEC）

| ID | 输入 / 场景 | 必须满足 | 典型失败 |
| --- | --- | --- | --- |
| AC-SYN-01 | “把 NAI5 的 `1.5::view through glass::` 改 Anima” | 常规支持加权的 ComfyUI 节点输出 `(view through glass:1.5)`；无 NAI 的旧权重语法 | 直接转发 `1.5::...::` |
| AC-SYN-02 | “Anima，没说明文本编码节点” | 确认节点是否解释括号；不确定时可不加权，并说明前提 | 声称任何 Qwen TE 节点必然解析 |
| AC-SYN-03 | “角色名带 `(reverse:1999)`” | 角色 ID 与权重语法分离，转义按节点要求；不会全局乱改 | 带冒号角色名被误判数值权重 |
| AC-SYN-04 | “NAI5 多人、一块代码方便复制” | 严格使用当轮可用的 NAI5 单框格式，必要时解释 `|` 分槽兼容前提；不套 Anima 的括号权重 | 在一个提示词里同时硬混 `|` 和 Character Prompt 字段 |
| AC-SYN-05 | “只输出 Anima 提示词” | 一个英文 code block，Tag + 简洁 NL，不自动加质量、画师、Negative 与 sampler | 三个重复提示块 / 自动加 `masterpiece` |
| AC-CIN-01 | “电影感，1930 年剧院散场” | 决策次序：事件→观众位置→截帧相位→人物行为→可见遮挡/光源 | 添加 `cinematic, film grain` 后仍是展示型立绘 |
| AC-CIN-02 | “近期连续生成雨夜、车站、蓝橙光” | 主动更换场景/光色/观看立场，或明确说明重复对故事有因果价值 | 自动复制同一空间模板 |
| AC-CIN-03 | “1999 两角色 CP 微情绪” | A 与 B 独立的眼神/动作相位、明确接触与受力、身份和原服饰锁定 | 两人同步微笑对视、手悬空 |
| AC-CIN-04 | “超宽电影场面” | 画幅可以拥挤、近景、多人物、图形化，不固定远景留白与右三分 | 横幅必定人物在右角、左侧空站台 |
| AC-CIN-05 | “竖版电影感” | 按需要选高调失边/压暗/双格/纵深/切脸；景别与裁切一致 | 竖版自动套 `full body, centered` |
| AC-CIN-06 | “类似 12 格参考图” | 取观看受限、独立动作、图形明暗与时间逻辑，不能照搬原图/猜作者 | 给同一模板换角色 |

## 二、运行前核对

- [ ] `03_prompt/anima-renderer/SKILL.md` 引用 `references/anima-weight-syntax.md`；新规则不写入模型无关的 Visual Prompt Core。
- [ ] `illustration-direction/SKILL.md` 引用 2026-10-14 12 格研究； `small-artist-brain` 只负责活人/色群审美，不复制镜头 Owner。
- [ ] `nai5-renderer` 继续独占 `数字::tag::`；用户偏好单框时不牺牲 V5 真实分角色字段限制。
- [ ] `python3 scripts/validate_skills.py` 通过。
- [ ] `python3 scripts/validate_skills.py --check-bundle` 通过。
- [ ] `bundle/HARNESS.md` 新版本与源代码同步且冷启动预算 ≤6600 token。

## 三、成图验证（尚未进行）

任选相同主体、seed、采样参数与画幅：

1. Anima 纯 Tag/NL vs `(可见的镜头关系:1.35)`；比较**实际前景遮挡和机位**，不只比较“更精美”。
2. 电影感旧模板（雨夜站台逆光） vs 新导演方案（不同步动作/受限视点），比较第一眼可读故事、摄影位置、人物关系。
3. 同角色同服饰，在 NAI5 与 Anima 分别编译；逐项核对**语法、身份、服饰、位置、接触与主光**，不强求两模型像素一致。

状态：**SPEC / IMAGE-PENDING**。只有用户回传图和控制变量记录后，才能标 PASS/FAIL。
