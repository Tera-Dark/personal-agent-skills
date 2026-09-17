# Agent Skill 编写与扩展规范 (Skill Specification)

本项目遵循模块化、自包含、跨平台通用的 Agent Skill 设计规范。所有新增技能均需符合本标准，以确保能够在不同的 AI 客户端（Claude、ChatGPT、Antigravity、Cursor 等）中无缝解析与执行。

---

## 1. 目录结构规范

每个技能必须作为一个独立的自包含目录存放在项目根目录下：

```text
[skill-name]/
├── SKILL.md                  # [必需] 核心技能定义、路由分发与执行契约
├── references/               # [推荐] 深度参考知识库、模式库、语法表
│   ├── [topic-a].md
│   └── [topic-b].md
├── templates/                # [可选] 输出模板或结构骨架
└── examples/                 # [可选] Few-Shot 优质示例或对比用例
```

---

## 2. SKILL.md 编写标准

### 2.1 YAML Frontmatter (元数据头)
每个 `SKILL.md` 顶部必须包含标准的 Frontmatter，便于 Agent 自主发现与检索：

```yaml
---
name: [技能唯一标识，小写中划线，如：video-director-compiler]
description: [50-100字简述，明确说明本技能的使用场景、输入类型与交付成果。Agent 根据此字段决定何时激活本技能]
---
```

### 2.2 正文结构框架
正文应保持**逻辑主干清晰、规则高度凝练**，避免将几十页的词库硬编码在主文档中（应下沉到 `references/`）：

1. **Mission & Architecture (定位与系统架构)**：声明技能职责、上下游输入输出边界。
2. **Core Principles (核心原则与约束)**：声明 MUST 和 MUST NOT 规则底线。
3. **Task Routing (任务路由机制)**：根据用户场景分流到不同子模式。
4. **Execution Workflow (执行流程)**：Step-by-Step 标准操作流程（SOP）。
5. **Output Contract (交付契约)**：明确规定的输出格式（如代码块、Markdown 报告、JSON 等）。
6. **Verification Checklist (自检清单)**：供 Agent 输出前的自检闭环。

---

## 3. 知识下沉原则 (References Separation)

- **为什么需要 References？**
  若将所有微观细节（词表、参数、特定画风实验记录）全部写在 `SKILL.md` 中，会造成 Context 冗长膨胀，且容易导致 Agent 产生“机械式死板套用”。
- **下沉策略**：
  - 将**固定语法、模型参数、实验记录**抽离为独立参考文件。
  - 将**领域词汇库、穿搭模式、构图模板**抽离为独立参考文件。
  - 将**多分支的美学/设计策略**抽离为独立参考文件，由主 Skill 按需索引加载。

---

## 4. 跨平台通用性考量

- **无平台私有依赖**：避免绑定仅某一个客户端特有的专有语法（如某些工具内部的特定私有函数），保持为标准 Markdown + YAML。
- **纯文本/通用格式交互**：支持自然语言输入与标准代码块交付。
