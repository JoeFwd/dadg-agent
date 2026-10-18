---
name: dadg-hebrides-island-float-terrain-fix
description: Offshore Scottish settlements float because terrain sits below the 10.0 water plane; raise the heightmap, settlement Z comes from a physics raycast, not the navmesh.
type: howto
topic: scotland
tags: [scotland, terrain, water]
sources: [scotland/terrain_island_plan.md]
updated: 2026-10-18
---

# Floating island settlements

Cause: terrain under ~30 offshore settlements sits at ~7-9 m, below the water plane (water_level 10.0). Settlement entities take Z from `Scene.GetHeightAtPoint` (physics raycast on terrain), not the navmesh, so raising the heightmap (target ~13.5 m) lifts them; shorelines form where terrain crosses 10. No water-mask edit needed. Navmesh Z re-lift is cosmetic. Sea-floor texels carry the BEACH layer at weight 255, so raised islands render sandy unless WGHT is repainted to BASE. Editable offline with the ZGR6 writer ([[zgr6-terrain-bin-format]]).

Related: [[scotland-population-project]]
