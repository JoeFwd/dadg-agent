---
name: dadg-ws-ship-navmesh-and-climber-fixes
description: FIXED 2026-10-01 - DADG ship climbers re-yawed to the vanilla frame and ship navmeshes rebuilt coarse (kogge 94 / carrack 24 / boat 13 faces); carrack has no stairs to its upper decks so they are excluded; open-sea campaign navmesh stripped on purpose
type: incident
topic: scenes-navmesh
tags: [war-sails, kogge, carrack, climbers, navmesh, coarsen_nav, open-sea]
sources: [memory/ws-climber-yaw-convention.md, memory/ws-coarse-navmesh-rebuild.md, memory/ws-open-sea-navmesh-stripped.md]
updated: 2026-10-18
---

# DADG War Sails ship fixes (2026-10-01 and 2026-10-11)

**Climbers (FIXED 2026-10-01).** `assemble_gameplay_roots.py` assumed local +Y was outboard and used +-pi/2; fixed in all 3 `climbers_holder.xml` files and the script. Backups in `Tools/WarSailsShips/backups/2026-10-01-pre-climber-yaw/`. Convention: [[ws-climber-yaw-convention]].

**Coarse ship navmesh (2026-10-01).** The dense navmeshes (~2900 faces) were replaced by coarse single-component meshes (kogge 94, carrack 24, boat 13 faces) made with the scratchpad tool `coarsen_nav.py` + `coarsen_cfg.json` (cfg "ramps" = xyz quads burned in, also usable as flat floor patches). Backups in `Tools/WarSailsShips/backups/2026-10-01-pre-coarse-navmesh/`.
- The carrack model has NO stairs between main deck and middeck (only a baluster rail over a 1.5 m drop) and none to the forecastle. The earlier stairs audit claiming a "grand staircase" was wrong, as the solid render showed. Upper decks stay off the navmesh until a stair prop exists.
- Lesson: a navmesh ramp through solid geometry gets agents stuck; verify stairs in a solid render, not from an audit's text. Adding a carrack stair prop is a model change; afterwards add a cfg ramp and rerun.

**Open-sea campaign navmesh stripped (user decision 2026-10-11).** On DellarteDellaGuerraMap `add-warsails`, `SceneObj/Main_map/navmesh.bin` had its open-sea faces (g3=19) removed as an FPS A/B test (32,587 faces left; backup `navmesh.bin.pre-seastrip.bak`). The user said "the navmesh stays as is now": do not restore it or treat it as stray work. Pathfinding measured <1% of the main thread in PerfView, so FPS investigation moved to campaign-map entity count and native map visuals.

Related: [[ws-ship-navmesh-boarding-face-rules]], [[dadg-ws-ship-reimport-state]]

Generic rule: [[seaborne-village-raid-scene-checklist]], [[warsails-main-map-migration-contract]]
