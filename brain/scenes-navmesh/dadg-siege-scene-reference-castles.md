---
name: dadg-siege-scene-reference-castles
description: Reference siege scenes and navmesh scale in DADG: Clun and Dartmouth as oracles, native scenes are 5-30x larger.
type: reference
topic: scenes-navmesh
tags: [scenes, siege, navmesh]
sources: [docs/siege-scene-design.md]
updated: 2026-10-18
---

# Reference castles

Oracle scenes: `Clun_castle` (817 entities, 6,328 faces; g6=1 on 2,866) and `Dartmouth_castle` (913 entities, 6,138 faces; g6=1 on 2,535). Native `khuzait_castle_siege_001` has 1,004 entities. Native siege navmeshes run 29,792-188,606 faces versus ~6,000 for DADG, with ~25 distinct g3 ids per DADG castle. Dartmouth ladder spawners use OnWallNavMeshId 211/311/201/301 matching authored g3 values.

Related: [[siege-dynamic-navmesh-id-convention]], [[navmesh-face-field-meanings-g1-g6]], [[dadg-rochester-castle-scene-spec]]
