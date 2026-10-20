# DADG Agent Guidelines

These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## Think Before Coding

Do not assume. Do not hide confusion. Surface tradeoffs.

- State assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop, name what is confusing, and ask.

## Simplicity First

Use the minimum code that solves the problem.

- No features beyond what was asked.
- No abstractions for single-use code.
- No speculative flexibility or configurability.
- No error handling for impossible scenarios.
- If a solution is much larger than it needs to be, simplify it.

## Surgical Changes

Touch only what the task requires.

- Do not improve adjacent code, comments, or formatting opportunistically.
- Do not refactor unrelated code.
- Match existing style, even where another style would be preferable.
- Mention unrelated dead code instead of deleting it.
- Remove only imports, variables, functions, or files that your own changes made unused.

Every changed line should trace directly to the user's request.

## Goal-Driven Execution

Turn tasks into verifiable goals.

- Add validation: write tests for invalid inputs, then make them pass.
- Fix a bug: reproduce it with a test or live check, then make it pass.
- Refactor code: verify tests before and after where practical.

For multi-step tasks, state a brief plan with verification points.

## Project-Specific Context

- For codebase orientation (architecture, modules, feature domains, case studies), load the `dadg-project-context` skill.
- For machine and project values (Rider `project_path`, logs, new-game option, evaluation anchor, cheats, installs), load the `bannerlord-agent-settings` skill before any Rider, GABS or playtest work.
- For live Bannerlord debugging, GABS, Rider debugger issues, CLR exceptions, or fix/relaunch/verify loops, use the `bannerlord-debug` skill.
- For conditional breakpoint syntax, JetBrains dialog handling, and decompiled source breakpoints, use `bannerlord-debug/references/jetbrains-debugger-tips.md`.

## DADG Project Overview

This repository is the C# source for DellarteDellaGuerra, a Mount & Blade II: Bannerlord mod set during the English War of the Roses.

### Module Layout

- `src/`: this repository, C# game logic, Harmony patches, dependency injection, and feature code.
- `../DellarteDellaGuerra`: main content module with XML, armour, weapons, animation assets, music, and compiled asset cache.
- `../DellarteDellaGuerraMap`: England campaign map, campaign UI, map XML, sandbox XML, and UI assets.
- `../DellarteDellaGuerraScenes`: custom mission scenes.

Never hand-edit `RuntimeDataCache/`; regenerate it through Bannerlord tooling.

### Architecture

The codebase is migrating toward hexagonal architecture:

- `DellarteDellaGuerra.Domain`: pure business logic, no Bannerlord references.
- `DellarteDellaGuerra.Infrastructure`: Bannerlord adapters, Harmony patches, events.
- `DellarteDellaGuerra`: application and feature logic.
- `DellarteDellaGuerra.Integration`: DI composition root and `SubModule` entry point.

Entry point: `DellarteDellaGuerra.Integration/SubModule.cs`.
DI setup: `DellarteDellaGuerra.Integration/DI/DadgServiceContainer.cs`.

### Build And Test

Run commands from `src/`:

```powershell
dotnet restore DellarteDellaGuerra.sln
dotnet build DellarteDellaGuerra.sln --configuration Release
dotnet test DellarteDellaGuerra.sln
dotnet test --filter "ClassName=GetJoustEquipmentUtilTests"
```

Test coverage is sparse. Scale verification to risk and use live debugging checks when the affected behavior is mostly in Bannerlord runtime state.

### Controlled Dependencies

`Bannerlord.ExpandedTemplate` and `Bannerlord.Cannons` live under `src/submodules/` and are project-referenced by DADG. Edit them in place there, not in legacy standalone module folders. Rebuild DADG to deploy their DLLs into the running game's loaded bin folder.

### Debugging

Prefer the `bannerlord-debug` skill for crashes, CLR exceptions, GABS, Rider debugging, or any fix/relaunch/verify loop. DADG bugs are often data bugs in XML or scene files rather than C# bugs.

## DADG knowledge brains

- DADG brain: `src/submodules/dadg-agent/brain/` (start at `INDEX.md`). This holds mod
  features, map and settlements, incidents, branches and workflow.
- Generic brain: `src/submodules/bannerlord-agent/brain/`. This holds engine, format and tool
  lessons true for any mod.
- Write new lessons to these submodule checkouts, never to `apm_modules/` or `.claude/`.
  A lesson with a generic rule and a DADG incident becomes two linked notes. The Obsidian vault
  is `src/submodules/`, so links between the two brains resolve.
