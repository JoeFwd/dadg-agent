---
name: dadg-scene-season-audit
description: 2026-11-28 audit of season support in production DADG scenes - 8 have no seasonal entities, 17 are partial (mostly no winter variant), southwark_navalraid hides everything in autumn/winter; terrain is seasonal everywhere except tournaments
type: reference
topic: scenes-navmesh
tags: [seasons, season_mask, xscene, audit, terrain]
sources: [DellarteDellaGuerraScenes/SceneObj/*/scene.xscene, scratchpad season_audit.py (2026-11-28)]
updated: 2026-11-28
---

# DADG scene season audit (2026-11-28)

Scope: every `SceneObj/*/scene.xscene` referenced by DADG / Map / Scenes / Spawns ModuleData or by C# code.

## How season support was measured

- **Entities.** `season_mask` on a `<game_entity>`: the low 4 bits are summer=1, autumn=2, winter=4, spring=8; the upper bits (240) are ignored. This order is inferred from the `_fall`=242 and `_summer`=249 hills, and from vanilla puddles=11.
- **Trees.** The `mesh_seasonal_material` script (Summer/Fall/Winter/SpringMaterial) swaps the material per season.
- **Terrain.** Each layer in `<terrain>` has `<summer>/<fall>/<winter>/<spring>` children. The winter layers use the `snow_*` textures.

**Caveat.** The audit did not expand `prefab="..."` instances, so seasonality that lives inside a prefab was missed. For example, the `tree_far_forest` prefab in `Scenes/Prefabs/cabbage.xml` already has `mesh_seasonal_material` on its 14 trees. The seasonal-tree counts below are therefore lower bounds.

**Probe, 2026-11-28 (not tested in game).** `dadg_hills_01` got field_03's backdrop of 17 hill spots × 3 seasons as `dadg_rollin_hills_*` prefab instances:
- Positions remapped by the 900/700 terrain ratio.
- z re-based on edge heights read from terrain.bin.
- The edit is uncommitted, pending a Custom Battle season check.

## Terrain

- Every production scene has all 4 terrain season blocks on every layer.
- The exceptions are `dadg_tournament_a`, `dadg_tournament_c` and `dadg_joust_v3`: their winter blocks have no snow textures.
- So the missing seasons below are entity and tree problems, not terrain problems.

## No seasonal entities at all (8)

These scenes look the same in every season apart from the terrain:

- Dartmouth_castle
- Stokesay_castle
- Hideout_pirate_camp
- dadg_hills_01 (only sp_battle_set carries a mask, 240)
- dadg_village_smithfield
- dadg_tournament_a
- dadg_tournament_c
- dadg_joust_v3

## Partial (17)

**No winter variant at all.** Ivy, flora and props are only hidden in winter, and nothing snowy replaces them:

- Carisbrooke_castle
- Clun_castle
- Corfe_castle
- Eilan_donan_castle (169 `ground_plane` set to summer/autumn/spring only)
- Piel_castle
- Hideout_pele_tower
- dadg_village_b_wharram_percy
- dadg_village_c_appleton
- dadg_village_coastal_a
- dadg_village_coastal_a_navalraid
- dadg_village_d_combe
- dadg_village_f_lacock
- dadg_village_fortingall

**All 4 seasons covered, but no seasonal tree materials:**

- Brougham_castle
- Caister_castle (114 `flora_green_j` also vanish in autumn)
- Hideout_bluebell_forest

**Likely bug:** `dadg_village_southwark_navalraid`.

- All 1136 entities are `season_mask="249"`, which is summer and spring only.
- So fences, props and sickles disappear in autumn and winter.
- The unused `dadg_village_southwark` has the same problem.

## Fully seasonal (19)

- Bristol
- Brough_castle (only 2 tree scripts)
- Coventry
- Framlingham_castle
- Lancaster
- Lincoln
- London
- Newcastle
- Norwich
- Skipton
- York
- dadg_field_01, dadg_field_02, dadg_field_03, dadg_field_04
- dadg_village_a
- dadg_village_e_grenstein
- dadg_village_stalbans

## Not relevant

Interiors have no season content and don't need any: castle_hall_*, cathedral_interior_a, dadg_dungeon_*, dadg_inn_a, main_menu_a.

## Reference pattern for adding seasons

Use `dadg_field_03` as the template (Scenes commit 63da299, "seasons to some fields"):

- **Hills backdrop.** Three `rollin_hills` entities, `dadg_rollin_hills_summer`, `_fall` and `_winter`, each carrying its own season_mask.
- **Trees.** Each `tree_far_a` gets a `mesh_seasonal_material` script (tree_far / _fall / _winter / _spring).
- **Masks.** Season masks follow these conventions:
  - 9 for crops and green flora
  - 11 for ivy and benches (hidden in winter)
  - 3 for harvest fields
  - 4 for snowy roads and water planes
  - 7 for hay and wagons

Related: [[dadg-editor-material-warning-audit]], [[scene-water-audit-stokesay-moat]]
