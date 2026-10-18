---
name: dadg-bridge-relocation-no-gos
description: Why relocating the Wye/Oxford Roman piers and adding a Great Ouse approach were all judged no-go (grades 50+ deg, navmesh floating above terrain, nested town assembly).
type: decision
topic: scenes-navmesh
tags: [bridges, relocation, no-go, slopes]
sources: [src/.tmp/wye-relocation-candidate/REPORT.md, src/.tmp/oxford-relocation-candidate/REPORT.md, src/.tmp/ouse-approach-remesh-candidate/NO-GO.md, src/.tmp/severn-bend-terrain-candidate/decision.md]
updated: 2026-10-18
---

# Bridge relocation trials, all no-go (nothing deployed)

- Wye (Hereford bridge): moving 4 piers to the narrow crossing at yaw 22.5 deg worked topologically (deck face 47742 reused, 27 water components, strict XY zero-classes) but banks climbed 2.2-2.3 m in 1.5 m (55-57 deg, ~150% grade). Parent bridge and town children must stay at the old site.
- Oxford: proposed crossing near (759.93, 210.13); portal widths 1.25-1.73 m vs a 2.96 m gap; nav shore Z 10.32 / 10.38 vs decoded terrain 9.99 / 9.50 (navmesh floats 0.33 / 0.88 m above ground). Existing deck F47757 is town-integrated and must stay.
- Great Ouse near (866.0, 345.2): banks ~3 m apart, 53-55 deg approach slopes; lowering >= 13 vertices by up to 1.63 m over 31 faces, shared with terrain 14/18. Old King's Lynn piers (nested `town_main/bridge`) are 9 m away and cannot move.
- Severn bend terrain: see [[navmesh-river-must-match-terrain-and-mask]].

Rule: before staging a relocation, compute bank grade (<= 20 deg), navmesh-vs-terrain Z at the shoreline, and whether the pier parents are nested in a town.

Related: [[scene-transforms-lack-mesh-bounds]]
