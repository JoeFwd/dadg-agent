---
name: dadg-joust-v3-terrain-paint
description: How the widened joust arena was built: touched WGHT nodes, flatten height, feathering, filling weight deficits, donor hash recheck.
type: howto
topic: scenes-navmesh
tags: [scenes, terrain, joust]
sources: [terrain_paint.py, generate_dadg_joust_v3.py]
updated: 2026-10-18
---

# dadg_joust_v3 terrain edit

6x6 grid of 100 m nodes; the widened arena touches only WGHT nodes 27 and 28. Heights flattened to raw 30,583 (28.000 m) over x=406..458, y=396..462 with smoothstep feathers; rebuild HGHT and NRML nodes 22 and 28. Mesh layers are cleared over the arena floor; pixels whose surviving weight sum is below 64 get the deficit put on native soil/mud slot 9 (36 of 9,135 pixels, 705 weight units). The generator re-hashes the donor scenes (e.g. `dadg_tournament_a`) after writing to prove they were untouched.

Related: [[zgr6-terrain-bin-format]]
