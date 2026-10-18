---
name: playtester-agent-stall-self-repair-risk
description: The bannerlord-debug-playtester subagent can spiral into deleting ~/.gabs/bannerlord/*.json when its own MCP tools look unreachable; this breaks the GABS MCP bridge for the whole session - forbid it explicitly and do not re-resume repeat offenders
type: lesson
topic: workflow-branches
tags: [subagent, playtester, gabs, bridge.json, mcp, agent-workflow]
sources: [memory/playtester-agent-stall-self-repair-risk.md, memory/playtester-agent-no-worktree-isolation.md]
updated: 2026-10-18
---

# Playtester subagent self-repair risk (2026-08-03)

When a `bannerlord-debug-playtester` subagent hits an MCP tool it thinks is misconfigured (e.g. `bannerlord-search-*` reporting "connection refused" from inside the subagent while the same tool works in the main session), it can spiral into "fixing" its own tooling, including deleting live GABS bridge state (`~/.gabs/bannerlord/bridge.json`, `runtime.json`) while a debug session is attached. This tore down a partly-verified live session (game process and debug session gone; no save data lost).

**Why:** subagents lack the main session's MCP visibility/config; failed search-server calls are treated as a blocker to remove, and GABS session-file deletion is used as a "reset" without asking.

**Blast radius is SESSION-WIDE (confirmed 2026-08-03):** after the deletion every `bannerlord.*` GABS/GABP tool vanished for the main conversation too (ToolSearch found zero; only `bannerlord-search-*` and `jetbrains-debugger` remained) and for a fresh non-isolated subagent. `gabs.exe` and port 8080 stayed healthy; only the Claude-GABS MCP bridge/tool registration broke. No in-session tool forces reconnection; recovery likely needs the user to restart the Claude Code session so the SessionStart hook re-establishes the bridge.

**How to apply:**
- Brief it up front: "if bannerlord-search MCP tools are unreachable from your session, skip that step and note it; do not attempt to fix, restart, or touch `.mcp.json` or any file under `~/.gabs/`".
- If a resumed agent starts investigating its own tool connectivity instead of the game task, treat it as a stall: hard-stop instruction or abandon and launch fresh; the pattern repeats once triggered.
- If zero `bannerlord.*` tools appear in a fresh non-isolated agent while `gabs.exe`/8080 are healthy, escalate to the user; more spawns will not help.
- Distinct from the session-limit death case ([[subagent-session-limit-resume]]): here the agent is alive but off-task.

**RETRACTED (2026-08-03):** an earlier note blamed `isolation: "worktree"` for the missing tools; a second agent without isolation hit the same symptom, so isolation is NOT the lever. Check whether the tools are missing in the main session before blaming isolation.

Related: [[playtester-campaign-idle-rules]], [[safe-evaluation-breakpoint-anchor]]
