---
name: dadg-ws-kogge-carrack-deck-navigability
description: 2026-10-23 - DADG kogge and carrack upper decks made AI-walkable (stairs collision + rebuilt conforming navmeshes, carrack 353 / kogge 228 faces); not live-tested; caveats on kogge ladder-steep stairs, carrack poop-rail clip and 2 boarding ids; swivel gun work in progress
type: incident
topic: scenes-navmesh
tags: [war-sails, kogge, carrack, stairs, navmesh, bo_editor_cube, swivel-gun]
sources: [session 2026-10-23, doc/ws-ship-decks-and-swivel-guns.md]
updated: 2026-10-23
---

# Kogge and carrack deck navigability (2026-10-23)

This supersedes the "carrack has no stairs, upper decks excluded" state in [[dadg-ws-ship-navmesh-and-climber-fixes]]. Both DADG War Sails ships now have AI-pathable upper decks. **This has not been live-tested yet.**

**Changes:**
- **Carrack:**
  - Stairs added, with stair collision in `DellarteDellaGuerraMap/NestedPrefabs/dadg_ws_carrack_ship_nested/*`.
  - Navmesh `NavMeshPrefabs/dadg_ws_carrack_navmesh.bin` rebuilt to **353 faces**.
  - Backup: `<scratchpad>/backup_carrack_stairs_20261023/`.
- **Kogge:**
  - 30 physics-only `bo_editor_cube` stair treads added in `dadg_ws_kogge_ship_nested/mesh_holder.xml`.
  - Navmesh replaced with a conforming **228-face** mesh.
  - Spawn points moved onto faces in `spawn_point_holder.xml`.
  - Backup: `<scratchpad>/backup_kogge_20261023/`.
- The scratchpad backups are session temp folders, so they are not durable.

**Caveats:**
- The kogge stairs are about **62°**, effectively ladders, and the castle notches they enter are narrow.
- The carrack's B stairs clip the poop-deck rail.
- The carrack navmesh carries **2 boarding ids**. Re-check them against [[ws-ship-navmesh-boarding-face-rules]] if boarding misbehaves.

**Follow-on, in progress:** each ship gets one bow swivel falconet built on the ShipBallista script. See `doc/ws-ship-decks-and-swivel-guns.md`, [[ws-one-siege-weapon-per-ship]] and [[ws-ship-upgrade-slot-mechanism]].

Related: [[ws-ship-deck-stairs-need-collision]], [[dadg-ws-ship-navmesh-and-climber-fixes]], [[ws-ship-ballista-prefab-requirements]]
