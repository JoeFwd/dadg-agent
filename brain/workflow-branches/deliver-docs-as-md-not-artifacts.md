---
name: deliver-docs-as-md-not-artifacts
description: Agent-workflow preference - design docs, plans and reports go to doc/<kebab-name>.md in the repo; never publish artifacts
type: decision
topic: workflow-branches
tags: [workflow, docs, preference, artifacts]
sources: [memory/deliver-docs-as-md-not-artifacts.md]
updated: 2026-10-18
---

# Deliver written work as repo markdown, not artifacts

Stated by the user on 2026-09-05; applies to every written deliverable (design docs, implementation plans, analyses, reports).

**Why:** DADG documents live in `doc/` under version control beside the code they describe. An artifact is a second copy that drifts, cannot be diffed, reviewed or branched with the change.

**How to apply:** write `doc/<kebab-case-name>.md` in the worktree and report the path. Do not call the Artifact tool or offer to publish one. If a published artifact genuinely needs updating, ask first.

Related: [[user-azerty-keyboard]], [[sendinput-foreground-guard]]
