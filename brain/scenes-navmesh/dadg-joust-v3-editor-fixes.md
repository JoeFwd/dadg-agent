---
name: dadg-joust-v3-editor-fixes
description: dadg_joust_v3 editor problems 2026-08-17/18 - orphan group GUID crash (4 barrier entities from the v2 donor) and terrain_ed.bin repaired by folding compiled heights back in
type: incident
topic: scenes-navmesh
tags: [dadg_joust_v3, joust, group_object, terrain_ed, donor-scene]
sources: [memory/xscene-orphan-group-guid-crash.md, memory/xscene-editor-vs-runtime-data-split.md]
updated: 2026-10-18
---

# dadg_joust_v3 editor fixes

**Orphan group crash (2026-08-17, FIXED).** 4 `_barrier_16x04m` entities were copied from the `dadg_joust_v2` donor carrying its group `{79AE2E40-1BD5-462A-BED1-CBD56C7546FC}` ("stuff"), but `editor_data` was merged from the other donor (`dadg_tournament_a`) which declared only "crowd" and "tents". Fixed by adding the missing `<group_object name="stuff" .../>`. Mechanism: [[xscene-orphan-group-guid-crash]].

**Terrain editor desync (2026-08-18).** The scene's terrain work existed only in `terrain.bin`; `terrain_ed.bin` was a donor copy. Repaired by folding compiled heights and layer weights back into `terrain_ed.bin` (only vertices differing by >3 quantisation steps), removing the editor-save hazard. Method: [[xscene-editor-vs-runtime-data-split]]. Flora cleanup on the same scene: [[terrain-flora-weight-offset-threshold]].
