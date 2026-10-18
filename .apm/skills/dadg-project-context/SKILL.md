---
name: dadg-project-context
description: >
  Project context for DellarteDellaGuerra / Bannerlord development: repository
  architecture, module layout, controlled submodules, build/test commands,
  content-module folders, and feature-domain map. Use when a task requires
  understanding the codebase, tracing feature ownership, editing XML/assets/scenes,
  or orienting implementation work before making changes.
---

# DADG Project Context

Use this skill to orient code, data, and asset work in the DellarteDellaGuerra
Bannerlord mod before making implementation decisions.

Read these references as needed:

- `references/dadg-project-overview.md` - architecture, dependencies, build/test commands, MCP tools, and feature map.
- `references/dadg-module-structure.md` - content module folders, RuntimeDataCache rules, and controlled submodule deployment.
- `references/dadg-feature-domains.md` - gameplay feature inventory and key code/data paths.
- `references/case-study-settlement-visual-crash.md` - a scene data bug that looked like an engine/C# crash (missing defender entities on the campaign map).
- `references/navmesh-setup-and-repair.md` - DADG campaign-map navmesh setup and regional repair with the `bannerlord-navmesh-preview` skill.
- `references/lord-hall-battle-london-example.md` - worked London lord's-hall battle conversion for the `bannerlord-lord-hall-battle` skill.
- `references/war-sails-ships.md` - DADG cog, carrack and English boat War Sails ship authoring workflow.

Before investigating a DADG bug or feature, grep the DADG brain (`brain/**/*.md` in the
dadg-agent repo; start at `brain/INDEX.md`) and the generic Bannerlord brain shipped by
bannerlord-agent. Machine and project values (debug config, log paths, anchors) are in the
DADG Bannerlord agent settings instruction.

For runtime debugging, CLR exceptions, Rider/GABS workflows, or fix/relaunch/verify
cycles, use the `bannerlord-debug` skill after loading the relevant project context.
