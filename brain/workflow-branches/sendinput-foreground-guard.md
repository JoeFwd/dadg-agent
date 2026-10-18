---
name: sendinput-foreground-guard
description: Agent-workflow rule - never SendInput to Bannerlord without a foreground-PID abort guard; Windows blocks focus stealing and keys land in the user's own app
type: lesson
topic: workflow-branches
tags: [sendinput, foreground, keyboard, agent-workflow, safety]
sources: [memory/sendinput-foreground-guard.md]
updated: 2026-10-18
---

# SendInput needs a foreground guard

On 2026-10-03 an unguarded SendInput "W" meant for Bannerlord landed in a different game the user was playing: `SetForegroundWindow` silently failed because the Windows foreground lock stops a background process stealing focus.

**Why:** the user uses the PC while agents playtest, and raw keys go to whatever window has focus, hijacking their session.

**How to apply:** always use a sender that aborts when the foreground PID is not Bannerlord (the scratchpad `sendkey.ps1` pattern). If it aborts, ask the user to focus the game or press the key themselves. Never retry by force-focusing. GABS has no key-input tool.

Related: [[user-azerty-keyboard]], [[deliver-docs-as-md-not-artifacts]]
