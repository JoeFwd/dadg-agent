---
name: dadg-rochester-castle-scene-spec
description: Design spec for dadg_Rochester_castle: real dimensions, scale, asset mapping, and the worldmap-icon trap.
type: decision
topic: scenes-navmesh
tags: [scenes, rochester, siege]
sources: [docs/rochester-castle-spec.md]
updated: 2026-10-18
---

# Rochester castle scene spec

- Scene `dadg_Rochester_castle`; settlements.xml currently binds the placeholder `Brougham_castle` to `scene_name` and `scene_name_1..3` ([[settlement-scene-binding-by-wall-level]]). Associated village `village_Maidstone`.
- Real keep 21x21 m, 34.5 m parapet, 38 m turret tips, 3 square turrets + 1 round SE turret. Scene 800x800 m at near 1:1, bailey ~100x65 m (~20% enlarged), approach from E/SE, river Medway on the west.
- Assets: keep `dadg_fort_norman_keep_b`/`_c` scaled ~1.35x (measure in engine first); round turret `dadg_fort_english_round_tower_d`; curtain `dadg_english_fort_big_castle_wall_a`; mural towers `dadg_norman_english_fort_castle_wall_tower_a` (NW `_tower_b`); gate `dadg_castle_gate_outer_l1` (carries CastleGate and DestructableComponent); siege towers `siege_tower_12m_spawner` / `_9m_spawner`.
- Trap: `dadg_worldmap_rochester_keep` is a map icon only (scale 0.546, no physics or navmesh); never use in a battle scene.
- Wall spacing inferred from other castles: wall_a 19-43 m (often ~42), tower_a ~22-27 m.
- Rebind test targets: `dadg_Clare_castle_comp`, `dadg_Gloucester_castle_comp` (wall level 1).

Related: [[dadg-siege-scene-reference-castles]], [[siege-scene-hard-requirements]]
