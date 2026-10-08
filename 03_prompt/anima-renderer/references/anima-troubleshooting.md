# Anima Diagnostic & Troubleshooting System

> **Version**: 1.2.0  
> **Last Updated**: 2026-09-17  
> **Scope**: 异常可见伪影诊断流程、最小扰动修复、不确定性处理与排查标准

本文档为 `anima-prompt-compiler` 提供系统化生图异常诊断体系。当生成的画面出现崩坏、色彩融化、构图混乱或角色串线时，依照结构化诊断流程执行最小必要修正，杜绝盲目堆叠无效负面词。

---

## 1. 标准诊断执行流 (Standard Diagnostic Flow)

遇到异常出图时，按以下四步顺序排查，严禁一次性修改多个变量：

```text
Step 1: 识别可见伪影 (Identify Visible Artifact)
   ↓
Step 2: 定位问题根源 (Root Cause Analysis: 提示词冲突 / 主体计数 / 空间歧义 / 材质融色 / 参数设置)
   ↓
Step 3: 施加最小扰动修复 (Apply Smallest Possible Prompt Modification)
   ↓
Step 4: 单变量回测验证 (Re-test while keeping other variables strictly unchanged)
```

---

## 2. 结构化诊断条目 (Diagnostic Catalog)

### 诊断项 01 · 肢体畸变与手部多指 (Anatomy & Hand Artifacts)

- **症状 (Symptom)**：手部指头粘连、多指、关节反折或胸前莫名伸出多余手臂。
- **可能原因 (Potential Root Causes)**：
  1. 提示词中同时存在互斥的姿态动词（如同时写了奔跑与背手）；
  2. 未给手部指定任何物理锚点，模型在自由发散中产生幻觉；
  3. 含有过度夸张的动作修饰词（如 `extreme crazy pose`）。
- **优先排查项 (First-order Checks)**：检查是否包含 2 个以上的冲突动作词。
- **最小修复措施 (Minimal Remediation)**：明确手部所在物理位置（如 `hands resting naturally on lap`、`one hand in coat pocket`、`holding a book with both hands`）。
- **不要立即做的事情 (What NOT to do)**：❌ 不要盲目在 Negative Prompt 堆叠几十个 `bad hands, extra fingers, missing fingers, malformed limbs`；❌ 不要随意加到 `(detailed fingers:1.5)` 这种过高权重。
- **验证标准 (Verification Criteria)**：手部有明确的着落点，指关节清晰自然。

---

### 诊断项 02 · 服装融合与内外层串色 (Garment Merging & Color Bleeding)

- **症状 (Symptom)**：外套的颜色渗入内搭，围巾的花纹融进衬衫，或下摆与长裤材质混淆。
- **可能原因 (Potential Root Causes)**：
  1. 多种颜色形容词散落排列，模型注意力未能正确对应具体名词；
  2. 缺乏从内到外的物理装配空间顺序。
- **优先排查项 (First-order Checks)**：检查颜色词是否紧贴在对应的服饰名词之前。
- **最小修复措施 (Minimal Remediation)**：采用**紧凑短语绑定 (Tight Phrase Binding)** 与 4 层叠穿语法：
  ```text
  [修复方案]
  wearing an open [Color + Material] coat over a [Color + Material] shirt, paired with [Color] trousers
  ```
- **不要立即做的事情 (What NOT to do)**：❌ 不要单纯提高某个颜色的括号权重；❌ 不要拆分成无上下文的单独逗号 Tag。
- **验证标准 (Verification Criteria)**：内搭与外套领口界限分明，颜色无渗透。

---

### 诊断项 03 · 背景喧宾夺主与视觉过载 (Background Dominance)

- **症状 (Symptom)**：复杂的街道建筑、密集路人或刺眼光污染夺取了角色主体地位，角色被压缩变小。
- **可能原因 (Potential Root Causes)**：
  1. 背景词汇长度与信息密度显著高于角色；
  2. 未指明景深衰减或构图景别；
  3. 缺少负空间休止区。
- **优先排查项 (First-order Checks)**：检查背景描述所占篇幅（*注：将 40% 视为粗略排查参考信号，而非绝对通用硬阈值 / Treat 40% as a rough investigation signal, not a universal threshold*）。
- **最小修复措施 (Minimal Remediation)**：
  1. 将景别收拢至 `cowboy shot` 或 `upper body portrait`；
  2. 在背景描述中加入 `shallow depth of field, background softly blurred, low visual density`。
- **不要立即做的事情 (What NOT to do)**：❌ 不要直接粗暴使用纯白底破坏原有叙事意图。
- **验证标准 (Verification Criteria)**：主体占据画面视觉焦点，背景虚化或留白自然退后。

---

### 诊断项 04 · 多角色属性串线 (Multi-Character Cross-Contamination)

- **症状 (Symptom)**：角色 A 的金发或服装被绘制在角色 B 身上，或者两个角色长相融合成连体婴。
- **可能原因 (Potential Root Causes)**：
  1. 使用了全局泛化描述而未按方位/角色独立分块；
  2. 出现多主体时未明确数量与站位关系。
- **优先排查项 (First-order Checks)**：检查是否使用了单一大段从句混合描述两个角色。
- **最小修复措施 (Minimal Remediation)**：
  按严格分块语法隔离：
  ```text
  2girls,
  [LEFT]: the girl on the left has [Hair/Eyes] and wears [Outfit A],
  [RIGHT]: the girl on the right has [Hair/Eyes] and wears [Outfit B]
  ```
- **不要立即做的事情 (What NOT to do)**：❌ 不要在同一个句式中并列两套服装词。
- **验证标准 (Verification Criteria)**：两人特征清晰独立，发色与衣物无交叉混淆。

---

### 诊断项 05 · 纯白背景边缘消融 (White Background Edge Bleaching)

- **症状 (Symptom)**：角色穿着浅色、白色丝绸或羽绒服时，身体边缘与纯白背景融合成一片。
- **可能原因 (Potential Root Causes)**：
  纯白背景拉高了全局明度，浅色物体受光面失去对比阶调。
- **优先排查项 (First-order Checks)**：检查是否缺少受光与暗部接地面。
- **最小修复措施 (Minimal Remediation)**：添加微弱暗部支点：`soft subtle contact shadow beneath feet, gentle grey gradient backdrop, balanced ambient lighting`。
- **不要立即做的事情 (What NOT to do)**：❌ 不要将角色衣服强制改成深色。
- **验证标准 (Verification Criteria)**：白裙白衣依然成立，但边缘通过微弱阴影获得清晰轮廓。

---

## 3. 归因不确定性处理 (Uncertainty Handling)

当生成画面出现异常且无法一眼断定单一根因时，执行以下不确定性处理规范，防止误诊：

1. **Do not claim a definitive cause (严禁轻率武断断言)**：不得在未隔离变量前将复杂伪影直接宣布为“提示词写错”或“模型缺陷”。
2. **Identify the top two plausible causes (列出前两位可能性)**：例如：① 动作动词冲突；② 采样器步数不足。
3. **Apply the least invasive test first (优先执行侵入性最小的单变量测试)**：优先微调单个词汇（如补充手部着落点），保持 CFG、步数、种子及其他词句完全不变。
4. **Record the result separately (独立记录观察)**：若修复有效，将其归档至 Experiment Log 并注明测试范围；若无效，回滚后再测试第二假设。
