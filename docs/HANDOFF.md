# 交接状态 · HANDOFF（browser-harness-pa）

> 任何 agent 开始工作前**必读**，结束工作前**必更新**。
> 本文件是当前任务状态的唯一权威来源；历史决策看 docs/adr/，历史变更看 git log。

## 项目速览

- 路径：`~/_projects_by_logic/03-ai-agent-infra/browser-harness-pa`
- 技术栈：Python
- 远程：https://github.com/iPythoning/browser-harness-pa.git
- 当前分支：`main`
- 最后活动：2026-07-31

## 仓库速览（自动提取，供冷启动）






> 以下内容由 `agents-enrich-handoff.py` 从**本仓库文件**自动提取，只含事实，不含推测。
> 「当前目标 / 下一步」仍需人工填写——脚本无法知道你这轮要做什么。

### 这是什么

Connect an LLM directly to your real browser with a thin, editable CDP harness. For browser tasks where you need **complete freedom**. One websocket to Chrome, nothing between. The agent writes what's missing during execution. The harness improves itself every run.

（package.json 描述：The simplest, thinnest, and most powerful harness to control your real browser with your agent.）

### 需要配置的环境变量（键名，取自 `.env.example`；**值不在仓库里**）

`BROWSER_USE_API_KEY`

### 目录与文件构成

顶层：`AGENTS.md`、`CHANGELOG.md`、`CLAUDE.md`、`GEMINI.md`、`LICENSE`、`README.md`、`SKILL.md`、`agent-workspace/`、`cliff.toml`、`docs/`、`domain-skills/`、`install.md`、`interaction-skills/`、`pyproject.toml`、`src/`、`tests/`

主要文件类型：`.md` × 132、`.py` × 19、`.yml` × 3、`.toml` × 2、`.png` × 2、`.example` × 1

## 如何验证（基线，动手前先跑一次）

- 测试：`pytest -q`

## 当前目标

> ⚠️ **待人工确认**：下次接手的 agent 请与用户确认本轮目标与验收标准后填写，不要凭猜测动手。

## 已完成（最近 10 次提交 · 自动生成于 2026-08-01）

- `d0a33aa` chore: add git-cliff changelog generation（2026-07-31）
- `32d8d51` Merge pull request #318 from browser-use/feat/runtime-dir-split（2026-05-06）
- `6e86f7c` feat(ipc): split BH_RUNTIME_DIR (sock) from BH_TMP_DIR (logs/screenshots)（2026-05-06）
- `5acfe37` Merge pull request #305 from hunnyboy1217/fix/current-tab-missing-target-id（2026-05-06）
- `bc186db` Merge pull request #310 from browser-use/Alezander9-patch-2（2026-05-06）
- `8ee028d` Update VOUCHED.td（2026-05-06）
- `e8a1187` Merge pull request #309 from browser-use/fix/ipc-socket-umask（2026-05-06）
- `8dc7285` fix(ipc): set umask 0077 around AF_UNIX bind to avoid chmod TOCTOU（2026-05-05）
- `455fc04` Merge pull request #308 from browser-use/Alezander9-patch-1（2026-05-05）
- `a248e21` Update VOUCHED.td（2026-05-05）

## 进行中 / 未提交改动（自动生成于 2026-08-01）

- 无未提交改动（工作区干净）

## 已知坑 / 注意事项

（待补充：踩过的坑写这里，比写在对话里有用一万倍）

## 下一步

（待补充）

## 最近交接记录

| 日期 | 操作者 | 摘要 |
|---|---|---|
| 2026-08-01 | agents-handoff.sh | 初始化交接状态（含真实 git 基线）|
