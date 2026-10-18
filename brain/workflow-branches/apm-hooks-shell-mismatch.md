---
name: apm-hooks-shell-mismatch
description: apm emits $env:CLAUDE_PROJECT_DIR in Claude Code hooks but hooks run under bash on Windows - fix the .apm/hooks templates, not the generated settings.json
type: howto
topic: workflow-branches
tags: [apm, claude-code, hooks, windows]
sources: [memory/apm-hooks-shell-mismatch.md]
updated: 2026-10-18
---

# apm hook commands break under bash

APM (Agent Package Manager) generates Claude Code hook commands with PowerShell's `$env:CLAUDE_PROJECT_DIR` syntax, but Claude Code runs hook `command` strings through Git Bash on Windows. Bash expands `$env` to empty and leaves `:CLAUDE_PROJECT_DIR/...` literal, so pwsh errors with "The argument ':CLAUDE_PROJECT_DIR/...' is not recognized as the name of a script file." This is NOT a failed `apm install`; the scripts are on disk and fine.

**Fix (verified 2026-08-13, apm 0.28.0):** edit the source templates `.apm/hooks/*.json`, never generated output. Change `-File "..."` to a single-quoted `-Command`:

```
"command": "pwsh -NoProfile -Command '& \"${PLUGIN_ROOT}/.apm/hooks/scripts/foo.ps1\"'"
```

Single quotes stop bash touching the string, so pwsh itself expands `$env:`. Works under bash or pwsh.

Keep `${PLUGIN_ROOT}`: it is target-aware (for `claude` it expands to `$env:CLAUDE_PROJECT_DIR/.claude/hooks/<pkg>`, for `codex` to a relative `.codex/hooks/<pkg>`).

Gotchas:
- Editing `.claude/settings.json` is wasted work; `apm install --force` regenerates it. Only `.apm/hooks/*.json` is checked in.
- `-Command` swallows `exit 2` (surfaces as exit 1), which PreToolUse treats as a non-blocking error. A PreToolUse hook that must block has to print JSON `hookSpecificOutput.permissionDecision=deny` on stdout with exit 0 (the repo's `jb-pause-guard.ps1` does this deliberately).
- The repo's hook scripts self-locate via `$PSScriptRoot` and never read `CLAUDE_PROJECT_DIR`; only pwsh finding the file was broken.

Same fix applies to any other apm-managed project.

Related: [[debugger-pause-kills-gabp-game]]
