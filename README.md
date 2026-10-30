# personal-agent-skills

给 Tera-Dark 个人使用的创作 harness：**网页优先、轻量、好用**。在新对话中发仓库链接，AI 按需加载个人偏好、创作方法与目标模型规则，不需要安装。

## ⚡ AI bootstrap

1. For web access, resolve `https://api.github.com/repos/Tera-Dark/personal-agent-skills/commits/main` to a full commit SHA. Fetch `https://raw.githubusercontent.com/Tera-Dark/personal-agent-skills/<SHA>/bundle/HARNESS.md` and use that SHA for subsequent repository files in this session.
2. If SHA resolution or the pinned file fails, fetch `https://raw.githubusercontent.com/Tera-Dark/personal-agent-skills/main/bundle/HARNESS.md`; follow its version checks and disclose that consistency is unverified. Never invent a SHA or claim unread content was loaded.
3. Follow the harness. If the user supplied a task, complete it; otherwise use its handshake. Do not clone or install for normal web use.

If the harness is inaccessible, reply: `我无法访问链接。请把 bundle/HARNESS.md 的内容粘贴给我。`

## 怎么用

在 ChatGPT、Gemini、Claude 等支持读取链接的 AI 新对话中发送本仓库链接，可以直接一起说明需求，例如：

> 读取这个仓库，按我的偏好写一条 NAI5 双人插画提示词：……

只有链接时，AI 会确认加载；同一条消息有任务时直接做任务。链接读取、缓存与多文件访问能力因平台而异，不能保证每次都成功。无法访问时可粘贴 [精简入口](bundle/HARNESS.md)，并在需要时粘贴相应 [模型管线](bundle/pipelines/)；[完整包](bundle/HARNESS-FULL.md) 体积很大，能上传不代表一定能被完整利用。

版本固定保证会话内读取同一提交；如果网页工具缓存了 GitHub API，所选提交仍可能不是最新版本。不能固定时，AI 应检查可用文件的版本并说明一致性尚未验证。

## 默认习惯

- 用中文沟通；图像模型提示词按目标模型输出英文。
- OC、插画和画面设计默认交付文字或提示词；只有明确要求实际生图或编辑图片时才调用生图工具。
- 普通 NAI5 输出一块可复制的英文正向提示词，不重复已在界面固定的画师串、质量词或 Negative；当轮要求优先。
- 只改一个变量时保留其他已确认条件；复杂原创任务才按需深入设计和参考。
- 单会话内的反馈可用于下一稿。跨会话保存需要已授权的写入或手动导出；只发链接不会自动记住聊天。

## 它如何工作

**个人偏好和路由 → 任务卡或设计模块 → 共享视觉事实 → 按需标签核验 → 目标模型输出。**

入口只包含常驻规则和索引；肖像、双人、海报、小改使用紧凑任务卡，复杂任务才加载深入参考。NAI5、Anima、MOSS 和通用模型共享创作决定，各自处理输出语法。软件 UI 任务独立路由，不强制经过绘图管线。

MOSS 默认使用 Caption；需要经验证的标签时使用 [moss-tags 管线](bundle/pipelines/moss-tags.md)。

- [使用与故障处理](docs/usage.md) · [模块总览](docs/main-overview.md) · [架构说明](docs/architecture.md)
- [个人偏好](00_core/personal-identity-profile/SKILL.md) · [反馈整理](docs/feedback-quickstart.md)
- [构图审美与网页实测](docs/composition-taste-review.md)
- [完整模块清单](docs/skill-registry.md) · [版本记录](CHANGELOG.md)

## 维护

源文件在 `kernel/`、`harness.json`、`VERSION` 和编号目录；`bundle/` 与 `docs/skill-registry.md` 是生成产物。标签索引是带独立来源和许可说明的固定快照，按需读取，见 [第三方说明](THIRD_PARTY_NOTICES.md)。

```bash
python3 scripts/validate_skills.py
python3 scripts/build.py
python3 scripts/validate_skills.py --check-bundle
python3 -m unittest discover -s tests -p 'test_*.py'
```

测试与构建验证文件契约，不能替代网页 AI 的真实会话测试或实际出图评价。详细约定见 [Skill 规范](docs/skill-specification.md) 和 [版本管理](docs/versioning.md)。

代码许可：MIT；第三方标签数据许可见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
