---
name: dadg-ws-custom-ships-conversion
description: DADG's three custom War Sails ships (English boat B, kogge, carrack) - conversion scale/rotation, body offsets, masses, rudder pivots and drivers, staged SDF clip, and where the sources went after Map Tools/WarSailsShips was removed (git 776ac28).
type: reference
topic: scenes-navmesh
tags: [war-sails, ships, prefab, rudder, conversion]
sources: [Map repo commit 776ac28 Tools/WarSailsShips (README.md, runtime-validation.md, visual-fixes-20261114/REPORT.md, RUDDER_IMPORT.md), DellarteDellaGuerraMap/ModuleData/dadg_custom_ship_hulls.xml, dadg_custom_mission_ships.xml]
updated: 2026-11-24
---

# DADG custom War Sails ships: conversion facts

Three Scenes ship models were converted into War Sails ships and registered in Map:
- `ModuleData/dadg_custom_mission_ships.xml` holds the 3 mission ships.
- `ModuleData/dadg_custom_ship_hulls.xml` holds the 3 hulls. Each hull has a `sail` slot; the kogge and carrack also have `dadg_bow_gun`.
- The nested prefabs are `NestedPrefabs/dadg_ws_{english_boat_b,kogge,carrack}_ship_nested/`. Their floaters are generated, and they include burning, water-effect, wetness and rudder holders.

| Ship | Source scale / yaw | Body Z offset | Mass est. (kg) | Rudder pivot (root m) | Rest X rot (rad) | Rudder driver |
|---|---|---:|---:|---|---:|---|
| English boat B | 0.702 / -90 deg | +0.15 | 3,071 | (0.00054, -3.5099, 0) | 0.667 | native `rudder_rotation_entity` |
| Kogge | 0.758 / +90 deg | -0.8 | 151,651 | (-0.0083, -11.2498, 0) | 0.1726 | `ShipRudderVisualMissionLogic`, tag `dadg_rudder_visual` |
| Carrack | 8 / 180 deg | -1.4 | 105,912 | (0, -8.5164, 0) | 0.2689 | `ShipRudderVisualMissionLogic`, tag `dadg_rudder_visual` |

English boat A (0.66 / -90 deg) was converted but not used.

The kogge and carrack steer through a `controller` child, so the native code never turns their rudder blades. `DellarteDellaGuerra.Integration/Naval/ShipRudderVisualMissionLogic.cs` drives the blades instead (see [[ws-ship-rudder-and-burning-prefab]]). The English boat already has its +0.15 m waterline shift baked into its aisle collision, so do not apply it to the entity a second time.

Hull triangle counts:

| Ship | Convex | Detailed |
|---|---:|---:|
| English boat B | 230 | 928 |
| Kogge (cog) | 498 | 675 |
| Carrack | 1456 | 803 |

**SDF water-clip candidates** are staged but **not active**:

| Candidate | Volume | Cap |
|---|---:|---:|
| `sdf_dadg_ws_english_boat_b_v1` | 12.49 m3 | 0.8 m |
| kogge | 341.95 m3 | 2.15 m |
| carrack | 321.16 m3 | 2.45 m |

Map's `dadg_ws_sails_plain` material GUID is `80ca1705-aaed-4889-bba1-a8f291a0ccaf`. All ship materials and textures are Map-owned `dadg_ws_*` copies, because Map loads before Scenes. See [[editor-copy-asset-across-modules]].

**Where the sources live now.** The Map `Tools/WarSailsShips` package (917 files) was removed after 2026-11-24. It held the conversion/assembly Python, Blender sources, drafts, audits and reports.
- Recover any of it with `git -C DellarteDellaGuerraMap show 776ac28:Tools/WarSailsShips/<path>`, or check out that commit. Large files are in LFS.
- The live Blender sources sit beside the FBXs in Map `AssetSources`.
- The 2026-11-14 rudder/fire repair kit is in Core `src/artifacts/ship-visual-fixes-20261114/`.

Generic lessons extracted from the package:
- [[ws-ship-editor-authoring-steps]]
- [[ws-ship-rudder-and-burning-prefab]]
- [[fbx-import-unique-internal-names]]
- [[material-texture-pick-native-av]]
- [[editor-rename-drops-texture-cache]]

Related: [[dadg-ws-ship-reimport-state]], [[dadg-ws-kogge-carrack-deck-navigability]], [[dadg-ws-ship-navmesh-and-climber-fixes]]
