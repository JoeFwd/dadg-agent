---
name: dadg-hebrides-island-float-terrain-fix
description: About 30 offshore Scottish settlements floated because their terrain sat at 7-9 m, below the 10.0 water plane; fix is raising the heightmap to ~13.5 m and repainting the BEACH weight to BASE.
type: howto
topic: scotland
tags: [scotland, terrain, water]
sources: [scotland/terrain_island_plan.md]
updated: 2026-10-29
---

# Floating island settlements

The terrain under about 30 offshore Scottish settlements sits at 7-9 m, below the DADG map's water plane (`water_level` 10.0), so they float. Fix: raise the heightmap under them to about 13.5 m. DADG sea-floor texels carry the BEACH layer at weight 255, so repaint WGHT to BASE or the raised islands render sandy.

Generic rule: [[campaign-settlement-height-from-terrain-raycast]]. Related: [[scotland-population-project]]
