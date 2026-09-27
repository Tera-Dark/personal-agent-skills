# Personal Agent Skills Hub

> Personal AI Creative Operating System
>
> 面向长期创作工作流的模块化 Agent Skill 仓库。
> 目标：让 AI 先理解创作意图，再完成设计、分析、模型适配与迭代。

---

## Architecture

```text
User Intent
    |
    v
00_core
Identity + Aesthetic Direction
    |
    v
01_router
Task Classification + Skill Routing
    |
    v
02_creation
Creative Production + Model Adapters
    |
    v
03_analysis
Reverse Engineering
    |
    v
04_tools
Workflow Implementation
    |
    v
05_evaluation
Quality Review + Iteration Loop
```

核心原则：

- 设计决策与模型语法分离
- 用户审美优先于通用模板
- Skill 负责流程，references 负责知识
- 不让单个 Skill 承担跨层职责

---

## Repository Structure

```text
.
├── 00_core/
├── 01_router/
├── 02_creation/
├── 03_analysis/
├── 04_tools/
├── 05_evaluation/
└── docs/
```

详细地图：

- `docs/project-map.md`
- `docs/skill-registry.md`

---

## Skill Flow

```text
需求
 ↓
理解
 ↓
身份与审美约束
 ↓
设计规划
 ↓
模型适配
 ↓
生成
 ↓
评价优化
```

Prompt 不是设计本身，而是设计思想与模型之间的沟通语言。

---

## Documentation

- `docs/architecture.md` - 系统架构
- `docs/project-map.md` - 项目地图
- `docs/skill-registry.md` - Skill索引
- `docs/skill-development-guide.md` - Skill开发规范
- `docs/versioning.md` - 版本维护规范

---

## License

MIT License
