# 安装与宿主

两个 Skill 可单独安装，也可一起使用。选择当前 Agent 对应的入口，安装后新开会话并确认能读取完整技能。这里区分目录安装、产品内导入和单文件使用；文件复制成功不代表该宿主已通过设计或交互任务验证。

## 目录型 Agent

快捷安装使用 [Skills CLI](https://github.com/vercel-labs/skills)。本文命令固定为 **1.7.4**，要求 **Node.js ≥22.20.0**；首次运行需要联网获取安装器。技能源为公开仓库 [viowai/7viow-ux-skills](https://github.com/viowai/7viow-ux-skills)。

先进入目标项目目录，以 Codex 为例：

```bash
npx -y skills@1.7.4 add viowai/7viow-ux-skills --skill 7viow-ux-review --skill 7viow-ux-ui-design --agent codex --copy -y
```

`--agent` 明确安装对象，`--skill` 只选择需要的技能，`--copy` 复制完整资源。命令默认仅用于当前项目；需要个人所有项目共用时才加 `-g`。不使用 `--all`，它会扩大安装范围。

将 `codex` 换成下表标识。路径是 **Skills CLI 1.7.4 的项目级输出位置**；共享 `.agents/skills/` 的客户端可能同时发现该目录中的技能。

| 入口 | `--agent` 标识 | 项目级目录 |
| --- | --- | --- |
| Codex 本地应用、CLI、IDE | `codex` | `.agents/skills/` |
| Claude Code | `claude-code` | `.claude/skills/` |
| Cursor | `cursor` | `.agents/skills/` |
| GitHub Copilot | `github-copilot` | `.agents/skills/` |
| OpenCode | `opencode` | `.agents/skills/` |
| Antigravity | `antigravity` | `.agents/skills/` |
| Antigravity CLI | `antigravity-cli` | `.agents/skills/` |
| Gemini CLI | `gemini-cli` | `.agents/skills/` |
| Grok Build | `grok` | `.grok/skills/` |
| CodeBuddy | `codebuddy` | `.codebuddy/skills/` |
| Qoder | `qoder` | `.qoder/skills/` |
| TRAE | `trae` | `.trae/skills/` |
| TRAE CN | `trae-cn` | `.trae/skills/` |
| ZCode | `zcode` | `.zcode/skills/` |

这些目标已验证安装器对本包的发现与完整目录复制；实际客户端的自动发现、调用和任务表现需在使用的版本中确认。路径依据：[Skills CLI Agent 表](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)。ZCode 安装后在 Settings → Skills 刷新；也可通过该页导入现有 Agent 的技能，见 [ZCode 官方说明](https://zcode.z.ai/en/docs/skill)。

**Qoder CN 单独处理：**其[官方文档](https://docs.qoder.cn/user-guide/skills)要求项目 `.lingma/skills/`；Skills CLI 1.7.4 的 `qoder-cn` 目标写入 `.qoder/skills/`，两者不一致。因此本版使用下述完整目录复制法，目标改为 `.lingma/skills/`，随后按官方要求重启 IDE 并查看技能列表。

## 本地目录与下载包

从 [v0.3.2 下载页](https://github.com/viowai/7viow-ux-skills/releases/tag/v0.3.2)选择完整仓库 ZIP、单技能 ZIP 或单文件 MD；[README 下载表](../README.md#直接下载)提供直接链接。

有完整仓库目录时，在目标项目运行下列命令。将示例路径换成实际目录，**不要指向 ZIP 文件**；`--agent` 按上表替换。

```bash
npx -y skills@1.7.4 add /path/to/7viow-ux-skills --skill 7viow-ux-review --skill 7viow-ux-ui-design --agent codex --copy -y
```

不使用 Node.js 时，解压包并复制所需 Skill 的**整个目录**到宿主的技能目录。例如 Codex 的最终结构：

```text
你的项目/
└── .agents/skills/
    ├── 7viow-ux-review/
    │   ├── SKILL.md
    │   ├── references/、assets/、agents/
    │   └── LICENSE、VERSION
    └── 7viow-ux-ui-design/
        ├── SKILL.md
        ├── references/、assets/、agents/、scripts/
        └── LICENSE、VERSION
```

只安装一个时保留对应目录即可。只复制 `SKILL.md` 会丢失按需参考、模板和辅助脚本；单文件版是单独提供的展开文件，不等于从目录中抽出入口。

## 确认安装与开始使用

可在目标项目查看安装器记录：

```bash
npx -y skills@1.7.4 list --agent codex
```

然后新开宿主会话，在技能列表中找到 `7viow-ux-review` 或 `7viow-ux-ui-design`，并检查它能读取参考资源。Codex 可输入 `$7viow-ux-review`；Claude Code 可输入 `/7viow-ux-review`；其他产品按各自技能选择器操作，也可直接说出完整名称。

> 使用 7viow UX Review，检查所附界面的报名流程。只评审，说明问题、影响、证据和复验方式。

> 使用 7viow UX/UI Design，按所附需求设计报名页，沿用项目 Design System，交付所需页面与交互状态。

如果能列出文件却无法调用，先确认安装范围、宿主当前项目、技能是否启用及会话是否刷新。遇到缺参考文件，重新复制完整目录。同一环境避免保留同职责旧名与新名两个活动版本。

## 通过界面导入的产品

这类产品使用各自的技能管理功能，不能仅凭同厂商的编程 Agent 路径判断。导入完整单技能包；只有客户端明确支持多技能仓库时，才导入整个仓库包。

| 产品 | 使用入口 | 当前边界 |
| --- | --- | --- |
| Claude / 原 Cowork | [Customize → Skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude)，导入单技能 ZIP | 需在当前账户开启所需能力 |
| WorkBuddy | [技能页本地导入](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market) | 以导入器接受的目录/文件格式为准 |
| DuMate | 技能安装页；[官方技能说明入口](https://cloud.baidu.com/discover/skill-dev-topic.html) | ZIP/MD 以当前客户端支持为准 |
| 豆包工作 | [技能・连接器・伙伴](https://www.feishu.cn/content/article/7677519271848610746) | 按当前本地导入入口操作 |
| 千问办公 | [技能管理](https://www.alibabacloud.com/help/tc/qwenwork/skills)，完整目录或本地导入 | 用户目录入口为 `~/.qwenwork/skills/`，与 Qoder 分开配置 |
| ChatGPT Chat / Work | [官方技能与插件入口](https://learn.chatgpt.com/docs/build-skills) | 本项目提供独立 Skill 目录，尚无原生插件安装包；Codex 本地安装不等于云端安装。使用当前账户可用的创建/导入功能，或采用下述单文件方式 |

这里提供格式与入口指引，尚未逐一完成这些产品的真实导入和任务验证。缺少自定义导入能力时，使用单文件方式。

## 单文件方式

适用于具有完整文件读取能力、但尚未确认自定义技能导入入口的产品，例如 M365 Copilot/Cowork、Gemini Enterprise、Grok Bot、库库 AI、Comate；也可供其他宿主临时使用。

将所需的 `7viow-ux-review-<版本>-standalone.md` 或 `7viow-ux-ui-design-<版本>-standalone.md` 与工作材料一起提供，并说明：

> 请把这份 7viow 技能文件作为本次工作方法，使用所附材料完成任务；先确认完整读取方法与相关参考，再按设计产出或只读评审的职责执行。

展开文件已包含方法、参考、模板和脚本说明。它是本次任务的显式输入，不是永久安装，也不保证自动触发。缺少浏览器、文件写入或设计工具时，只能完成宿主能力覆盖的部分；截图和规格评审不能证明交互已经运行。

## 固定版本

需要固定在 v0.3.2 时，用 tag 地址替代默认分支地址。例如只安装 Review 到 Codex 当前项目：

```bash
npx -y skills@1.7.4 add https://github.com/viowai/7viow-ux-skills/tree/v0.3.2 --skill 7viow-ux-review --agent codex --copy -y
```

只安装 Design 时将技能名换为 `7viow-ux-ui-design`；也可以同时给出两组 `--skill`。固定版本更新时，明确换成所需的新 tag，或恢复使用默认分支地址。

## 更新与移除

更新时在原安装项目执行同一条 `add` 命令，保留相同 Agent、范围和 `--copy`。它只重新安装明确选择的两个技能，不改其他技能。手动安装者替换完整目录；修改过技能内容时先保存自己的改动。

移除当前项目中的两个技能（包括该项目其他 Agent 的同名副本）：

```bash
npx -y skills@1.7.4 remove 7viow-ux-review 7viow-ux-ui-design -y
```

此命令只移除明确指定的两个名称，保留其他技能。原来加 `-g` 安装的，移除时也加 `-g`。多个宿主共享同一 `.agents/skills/` 目录，无法只为其中一个宿主删除共享文件；只想在单个产品停用时，使用该产品的启用开关。共享目录存在其他读取者时，安装器的 `remove --agent codex` 可能显示成功却保留文件，因此完整移除采用上述按名称限定的命令。图形导入通过原产品管理入口移除，完成后刷新会话。

两个技能的独立能力和可选协作见[独立使用与协作](using-together.md)。反馈请附宿主与版本、安装方式、任务材料、实际结果和期望变化。
