---
name: dadg-main-map-bridge-navmesh-final-state
description: Final deployed state of the DADG Main_map navmesh bridge/river work (2026-09-29) - 31 decks, counts, gates passed and what remains.
type: incident
topic: scenes-navmesh
tags: [navmesh, bridges, rivers, main-map, war-sails]
sources: [src/.tmp/final-bridge-candidate/live-deployment-report.md, src/.tmp/studio-candidate-scene/LIVE-RECEIPT.md, src/.tmp/river-quad-merge-candidate/REPORT.md]
updated: 2026-10-18
---

# Main_map bridge + river navmesh (add-warsails)

Status: DEPLOYED 2026-09-29 (live `../DellarteDellaGuerraMap/SceneObj/Main_map/navmesh.bin`).

- 31 terrain-1 decks over retained river water: 26 Gothic + 5 Roman (incl. London and Oxford Thames Roman crossings).
- Live versions: bridge promotion (47,758 faces, 37,414 verts), then river quad/sliver cleanup (47,737 faces, 85,293 edges). 35 local repartitions kept exact outer XY footprint; 13 triangle-pair quad merges (Tweed, Dee, Tees, Ure, Ribble, Wye, Clyde); Severn underbridge sliver fixed (0.46 -> 10.9 deg).
- Thames vertices, face loops, terrain labels untouched (reference); London stays a town crossing.
- Isolated dry Clyde face 41172 reclassified terrain 11 -> 1 (wet components 112 -> 111).
- Gates passed: topology 0 errors, strict XY zero-classes ([[navmesh-xy-overlap-classification-gate]]), 26/26 Gothic two-bank routes, 27 water components retained, 11-river centerline audit with zero dry samples, zero wet samples lacking water navmesh, zero wrong-sea-id.
- Not done: outer river banks not reshaped; bends remain angular where vertex spacing is under target (needs coordinated terrain/mask work, [[navmesh-river-must-match-terrain-and-mask]]). Roman banks and one London Gothic pier open: [[dadg-roman-bridge-terrain14-banks]].

Map constants: water navmesh Z ~10.28, deck Z 10.45, "wet" terrain height <= 10.085 m.

Related: [[navmesh-bridge-deck-over-water-construction]], [[dadg-bridge-relocation-no-gos]]
