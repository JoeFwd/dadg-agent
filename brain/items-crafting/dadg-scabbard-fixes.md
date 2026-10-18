---
name: dadg-scabbard-fixes
description: DADG scabbard fixes 2026-08-08 - hanger and wakefield_hanger swapped to Scabbard03_black; castillon_b blade reseated by splitting distances (base 7.691 to 9.868, reach unchanged); DADG scabbard family table
type: incident
topic: items-crafting
tags: [scabbard, castillon_b, hanger, wakefield_hanger, scabbard-families]
sources: [memory/scabbard-length-families.md, memory/scabbard-anchored-to-blade-pivot.md, memory/scabbard-mouth-metric-pitfall.md]
updated: 2026-10-18
---

# DADG scabbard fixes (2026-08-07/08)

Meshes live in `AssetSources/shared/detail_kit/scabbards.fbx`, compiled to `Assets/shared/detail_kit/scabbards_geo.tpac` (15 scabbard objects). Families ([[scabbard-length-families]]):

| family | meshes |
|---|---|
| about -32.4 | shortmesser_scabbard |
| about -39.7 | griffinmesser_scabbard, 02_small_brown |
| about -52.1 | 02_red, 03_red, 03_black, scottish_arming |
| about -64.5 | 05_blue, 05_red, 04_green, 02_catherine |

- **hanger + wakefield_hanger** (blades 104.97 / 103.896, family -52) shipped with `Scabbard01_black`, a -64.5 mesh: 12.4 too long, mouth swallowing the grip. FIXED by swapping both to `Detail_Kit_Basic_Scabbard03_black`.
- **castillon_b** (`XV_blade`) sat 5.56 below the guard bbox top and was the only blade with no `<BuildData>`; base 7.691 was under the guard underside (8.279). FIXED by replacing `length="100.815"` with `distance_to_previous_piece="52.585" distance_to_next_piece="48.230"` (same sum): base 7.691 to **9.868** vs block top 9.870, scabbard mouth 7.565 to 9.743 (guard spans 8.279-13.249), reach **110.115 unchanged**. `glasgow_castillon_blade` uses `previous_piece_offset="9.12"`; zeroing it leaves the blade floating 8.97 above the guard. A first attempt raised 5.559 by aiming at seam == 0; the user spotted the floating blade in the render ([[scabbard-anchored-to-blade-pivot]]).
- wakefield_hanger's guard bbox is 25.3 tall (knucklebow sweep), castillon_b's cross only 4.97 tall and 27.7 wide; the user pushed back twice that "the scabbard is paired with the hilt instead of the cross" and was right ([[scabbard-mouth-metric-pitfall]]).
