---
name: dadg-york-navmesh-fragmentation
description: York's navmesh.bin is valid but fragmented (74 components, 31 tiny islands vs Lancaster 37/7); ruled out as the civilian-mission crash cause on 2026-07-31, kept as a cleanup item
type: incident
topic: scenes-navmesh
tags: [york, lancaster, navmesh, fragmentation]
sources: [memory/york-navmesh-fragmentation.md]
updated: 2026-10-18
---

# York navmesh fragmentation (checked 2026-07-31)

York's `navmesh.bin`: 6876 verts / 12289 edges / 5405 faces, structurally sound, 74 components with 31 islands of <=2 faces, vs Lancaster 37 / 7. Investigated as a crash suspect and ruled out; the actual cause is [[dadg-missing-commonareamarker-scenes]]. Keep as a lower-priority pathfinding cleanup. Generic lesson: [[navmesh-fragmentation-is-not-a-crash-cause]].
