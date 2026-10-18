---
name: subagent-session-limit-resume
description: Background subagents that die on "session limit" can auto-resume after the reset and still complete; do not relaunch duplicates, and do not trust a 0-byte transcript or unchanged worktree as proof of death
type: lesson
topic: workflow-branches
tags: [subagent, session-limit, resume, agent-workflow]
sources: [memory/subagent-session-limit-resume.md]
updated: 2026-10-18
---

# Session-limit subagent deaths can resume

Observed 2026-07-18: a background implementer returned a completion notification containing only "You've hit your session limit, resets HH:MM"; after the reset a *second* completion arrived from the same agent id with the full result. Meanwhile its transcript read 0 bytes and the worktree showed no changes, so the work looked lost.

**Why:** the limit notification is not terminal; the harness can resume the agent with context intact. A duplicate risks two agents editing the same files and burns tokens the user is trying to save (they asked to preserve prior subagent progress).

**How to apply:** wait for the reset rather than relaunching. If a duplicate was launched, TaskStop it as soon as the original shows life.

Related: [[worktree-build-quirks]], [[playtester-agent-stall-self-repair-risk]]
