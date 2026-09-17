# Anima Troubleshooting & Diagnostic Guide

> **Version**: 1.0.0  
> **Last Updated**: 2026-09-17  
> **Scope**: 常见生图异常排查、提示词冲突消解与修复建议

本文档为 `anima-prompt-compiler` 提供异常诊断经验沉淀。当生成的画面出现崩坏、色彩融化、构图混乱或角色串线时，可依据本指南进行针对性修正。

---

## 1. 肢体畸形与手指崩坏 (Anatomy & Hand Artifacts)

### 常见诱因
1. **动作冲突 (Conflicting Poses)**：例如 Prompt 中同时包含了 `running` 和 `hands clasped behind back`，模型在运动动力学与静止姿势间冲突。
2. **多余肢体引导**：过度泛化的词汇（如 `dynamic crazy action pose`）导致四肢数量随机增加。
3. **未说明手部位置**：手部无明确归宿时，AI 容易在衣角或口袋处生成多余的手指。

### 修复建议
- **精准锚定手部行为**：明确指出手部所在位置（如 `hands gently resting on lap`、`one hand in coat pocket`、`holding a teacup with both hands`）。
- **降低肢体复杂度**：由夸张复杂扭转退回为自然的静态或半身景别（Cowboy shot）。

---

## 2. 服装融合与内外层串色 (Garment Merging & Color Bleeding)

### 常见诱因
1. **多重颜色修饰词散落**：例如 `blue eyes, black coat, white shirt, red scarf, brown shoes`，模型容易将红色混入大衣，或把黑色染上衬衫。
2. **缺乏空间装配次序**：未按物理层级从内向外描述。

### 修复建议
- **紧凑短语绑定 (Tight Phrase Binding)**：将颜色与服装紧密锁定在一个从句内：
  ```text
  [优化前] a girl in a coat, shirt, scarf, black, white, red
  [优化后] wearing an open black wool coat over a crisp white cotton shirt, accented by a red knitted scarf
  ```
- **物理层级排序**：严格遵循 `Base Layer (贴身) → Mid Layer (中层) → Outer Shell (外套)` 的顺序编译。

---

## 3. 背景抢主体与视觉过载 (Background Dominance & Visual Overload)

### 常见诱因
1. **背景信息密度远超主体**：大段描述了复杂的赛博朋克街景、几十栋建筑、车流与广告牌，稀释了人物注意力。
2. **缺乏景深衰减指令**。

### 修复建议
- **引入负空间与散景**：在背景描述中加入 `shallow depth of field, background softly blurred, low visual density, simple minimalist backdrop`。
- **调大角色构图占比**：改用 `close-up`, `cowboy shot` 或指定 `character dominating the foreground`。

---

## 4. 多角色属性串线 (Multi-Character Attribute Cross-Contamination)

### 常见诱因
当画面出现 2 个或更多角色时，AI 会把 A 的金色长发画到 B 头上，或把 B 的西装穿到 A 身上。

### 修复建议
- **单人优先原则**：若非绝对必要，立绘与服设尽量坚持单主体（`1girl` 或 `1boy`）。
- **严格分块绑定**：如果必须编译双人插画，使用严格的方位前缀：
  ```text
  2girls,
  the girl on the left has long blonde hair and wears a blue dress,
  the girl on the right has short black hair and wears a white sweater
  ```
- **多尺度展示板替代**：如果是展示同一角色的不同角度或特写，使用 `layered character presentation layout`，并指明为 `same character`。

---

## 5. 纯白背景边缘消融 (White Background Edge Bleaching)

### 常见诱因
当指定 `white background` 且角色穿浅色或反光材质衣物时，受光面容易与背景融为一体失去轮廓。

### 修复建议
- **注入弱阴影锚点**：添加 `subtle soft contact shadow beneath feet, gentle grey gradient backdrop`，既保持了纯净背景，又保证了边缘轮廓完整。
