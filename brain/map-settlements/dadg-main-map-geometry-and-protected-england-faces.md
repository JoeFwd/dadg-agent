---
name: dadg-main-map-geometry-and-protected-england-faces
description: DADG Main_map geometry, water levels, and the rule that England's hand-authored navmesh faces [0,7599) must stay byte-identical.
type: reference
topic: map-settlements
tags: [map, navmesh, england]
sources: [dadg-navmesh-objectives.md, dadg_rivers findings]
updated: 2026-10-18
---

# DADG Main_map facts

- 1120 m square, heightmap 2049^2 at 0.5469 m/px, height range 0-15.62, ocean water level Z=10.0. World y = row * px with no flip (564/600 face samples agreed).
- England hand-authored navmesh faces [0, 7599) are protected: any generated or merged mesh must keep them byte-identical.
- England has 7 water-plane entities (material `water_vlandia_lake`, z ~10.12-10.13), 12 river splines at z 10.127 (only 13-53% of length below 10.0) and 8 waterfalls. Ireland and Scotland have none: their rivers and lakes are heightmap carving only.
- Target branch for the full mesh: `1.4/complete-navmesh`. Remaining stages: reachability and load-verify/commit.

Related: [[dadg-v14-river-and-lake-detection]], [[campaign-navmesh-river-lake-conventions]]
