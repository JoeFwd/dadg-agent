---
name: framlingham-navmesh-hole
description: FIXED 2026-09-10 - Framlingham siege stall was 335 connector faces g5=-51 (siege + level_1 only); promoted to g5=-3
type: incident
topic: scenes-navmesh
tags: [framlingham, navmesh, siege, g5]
sources: [memory/framlingham-navmesh-hole.md]
updated: 2026-10-18
---

# Framlingham castle siege stall (FIXED 2026-09-10)

Diagnosed 2026-09-09/10 and fixed in `DellarteDellaGuerraScenes/SceneObj/Framlingham_castle/navmesh.bin`. Mechanism, fix rule and false trails: [[navmesh-g5-level-bits-must-cover-all-castle-levels]].

Specifics: tower (28 faces, x 337.8-345.1, z 34.1-39.1) and rampart walk (135 faces, x 381.1-426.8, z 34.0-39.1, where the cannon crew stands) both became islands at level 2/3. After the fix siege at all three levels: 34 components, main 2568 faces, tower and rampart both in component 0. Backup `navmesh.bin.bak-20260910-211024`. The stair (x 348-355, y 393-400) was always continuous 22.5 to 39.08.

**Still open:** in-game confirmation at level 2/3 (proven in file only); a separate civilian-sheet bug (`g5 = -6`: tower is a 29-face orphan island plus two T-junction components), untouched. Sweep other castle scenes for faces with `siege` but only `level_1`. Evidence: `doc/framlingham-siege-stall-diagnostic.md` (Revision 2).

Related: [[navmesh-fragmentation-is-not-a-crash-cause]]

Generic rule notes: [[navmesh-duplicate-corner-face-crash]] records a duplicate-corner face (4844) found in the Framlingham_castle navmesh.

Generic rule: [[navmesh-level-mask-must-match-mission-mask]], [[navmesh-vertex-touch-is-not-an-edge-connection]], [[xscene-declares-level-bit-mapping]]
