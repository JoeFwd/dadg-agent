---
name: dependency-submodules-workflow
description: Controlled dependencies live under src/submodules and are edited in place; rebuild DADG to deploy their DLLs.
type: howto
topic: workflow-branches
tags: [submodules, workflow]
sources: [doc/dependency-submodules.md]
updated: 2026-10-18
---

# Dependency submodules workflow

`Bannerlord.ExpandedTemplate`, `Bannerlord.Cannons` and the PrivateWars submodule live under `src/submodules/` and are project-referenced by DADG. Edit them there, never in legacy standalone module folders, and rebuild DADG so their DLLs reach the loaded bin folder. Worktree builds need submodule init and a short path ([[worktree-build-quirks]]).

Source docs: doc/dependency-submodules.md.

Related: [[worktree-build-quirks]]
