# 7viow UX Skills

让 AI 设计的界面更易理解、更顺手，让体验评审落到具体问题与可验证的改进。

面向**对设计质量有要求的 AI 使用者**：需要把想法变成可用体验、判断和改善现有产品，或让个人与团队保持协作质量。产品经理、设计师、开发者、创业者都可以按自己的任务使用。

## 从你的任务开始

| 你想完成什么 | 使用哪个 Skill | 你会得到什么 |
| --- | --- | --- |
| 检查现有页面、流程、原型或产品体验 | [7viow UX Review](skills/7viow-ux-review/SKILL.md) | 有证据的问题、影响判断、修正建议和复验条件 |
| 从需求形成设计，或修改已有界面 | [7viow UX/UI Design](skills/7viow-ux-ui-design/SKILL.md) | 信息结构、设计方向、交互状态、界面文案与所需设计产物 |

两个 Skill 可以单独使用，也可以一起完成设计、评审和修正。它们各自携带所需方法、参考和模板，没有必须安装的兄弟 Skill。

## 快速开始

在线安装获取仓库已发布的版本。可从 GitHub 安装，也可下载完整目录后使用[本地安装](docs/hosts.md#本地目录与下载包)。

**让 Agent 帮你安装：**把下面一句话发给具备终端与文件权限的 Agent。

> 请从 https://github.com/viowai/7viow-ux-skills 安装 7viow-ux-review 和 7viow-ux-ui-design，按仓库 docs/hosts.md 选择当前 Agent 的安装方式，优先仅用于当前项目，并确认两个 Skill 的入口和全部参考资源可读取。

**在终端安装：**先进入要使用 Skill 的项目目录。以 Codex 为例，需要 Node.js **22.20.0 或更高版本**：

```bash
npx -y skills@1.7.4 add viowai/7viow-ux-skills --skill 7viow-ux-review --skill 7viow-ux-ui-design --agent codex --copy -y
```

使用 Claude Code，将 `codex` 换成 `claude-code`；Cursor 换成 `cursor`。其他入口见[宿主选择表](docs/hosts.md#目录型-agent)。这条命令安装到当前项目；只需要一个 Skill 时，删去另一个 `--skill` 参数及名称。

完成后新开会话，在宿主技能列表中确认所选 Skill，再给出任务。Claude 等需通过界面导入的产品见[导入方式](docs/hosts.md#通过界面导入的产品)；它们不共用上面的终端命令。

## 直接下载

在 [GitHub Releases](https://github.com/viowai/7viow-ux-skills/releases) 选择已发布版本及附件：

| 需要的内容 | 附件名称 |
| --- | --- |
| 两个 Skill 和使用说明 | `7viow-ux-skills-<版本>.zip` |
| 只安装 UX Review | `7viow-ux-review-<版本>.zip` |
| 只安装 UX/UI Design | `7viow-ux-ui-design-<版本>.zip` |
| 在对话中临时使用完整方法 | `7viow-ux-review-<版本>-standalone.md` 或 `7viow-ux-ui-design-<版本>-standalone.md` |

单文件方式需要宿主能完整读取文件；它不会永久安装或自动增加工具权限。需要固定版本安装时，见[安装与宿主](docs/hosts.md#固定版本)。

## 第一次使用

**评审现有体验：**

> 使用 7viow UX Review，检查这份原型中“找到活动→报名→修改报名”的流程。只评审，按影响排序，说明证据和复验方式。

**从需求做设计：**

> 使用 7viow UX/UI Design，为所附需求设计活动报名页。沿用项目 Design System；先给可比较的方向，再按选定方向完成交互原型。

**修改已选定设计：**

> 使用 7viow UX/UI Design，按这份评审修复比较入口。保留已选布局和原数据，修改维护源，重新生成并验证返回路径。

只需要一项小修正时，直接说明改动范围。已有方向和事实会继续沿用。

## 使用时会发生什么

- 区分创作方法、项目 Design System 和业务事实；发现缺口时，解决真正影响结果的问题。
- 新的核心设计先比较有实质差异的方向；已有设计的局部修正保留既定决定。
- 评审区分实际运行、截图和规格所能提供的证据；报告具体问题和可观察的修复结果。
- 数据驱动或生成的界面回到维护源修改，再检查重建后的结果。
- 界面文案保留必要条件，并用明确长度预算或逐项改写约束检查。

Skill 提供工作方法；文件访问、浏览器和原生设计工具由所用 AI 工具提供。截图评审不能证明交互已运行，设计自检也不能替代独立评审。交付会说明实际完成与未验证的范围。

技能本体无需第三方 Skill、账号或 API key。快捷安装使用独立的 Skills CLI；Design 附带的文案计数脚本使用 Python 3 标准库，也可由宿主按同一规则计算。需要浏览器或设计工具的任务，仍需宿主提供相应能力。

## 一起使用

从 [独立使用与协作](docs/using-together.md) 了解 Design 与 Review 如何交接、如何用 [Talis](https://github.com/viowai/7viow-talis) 保存后续修改与复验请求，以及什么时候适合加入 7viow 写作技能。局部任务只调用需要的能力，保留一份当前产物和一份问题清单。

## 作者与许可

作者与维护者：**Viow** · 系列：**7viow** · 文件版本：**0.4.0**

原创版权：**Copyright (c) 2026 Wenbin Li**。采用 [MIT License](LICENSE)。

使用反馈请说明任务、实际材料、观察到的结果和期望变化；需要贡献时见[贡献说明](CONTRIBUTING.md)。
