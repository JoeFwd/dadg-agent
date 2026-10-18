---
name: dadg-scottish-arming-sword-fix
description: The Scottish arming sword (2026-08-05) was ONE blade defect (mesh authored 5.353 low) that looked like two; fixed by recentring the FBX origin and previous_piece_offset 0.98, plus a 100x FBX scale failure afterwards
type: incident
topic: items-crafting
tags: [crafting, arming-sword, blade, guard, fbx]
sources: [memory/crafting-joint-gap-formula.md, memory/blade-mesh-origin-inflates-reach.md, memory/crafting-contact-profile-check.md, memory/blender-fbx-roundtrip-breaks-scale.md]
updated: 2026-10-18
---

# scottish_arming_sword joint fix (2026-08-05/06)

- Symptom: blade floated 1.23 units above the guard's central collar while tool JSON claimed -1.52 overlap ([[crafting-joint-gap-formula]]). It seemed to need two corrections on two pieces.
- **Resolution: one defect, on the blade.** The blade mesh was authored 5.353 low; its `previous_piece_offset="-7.82"` over-compensated. Recentring the FBX mesh origin in Blender and setting `previous_piece_offset="0.98"` fixed it. The guard's authored `next_piece_offset="4"` had been nearly right all along (correct 3.84). A wrong earlier attempt cut it to 2.0 after mistaking the decorative boss for a collar.
- Reach: declared 107.119 vs visible tip 101.779 before; 101.769 after (tip 101.782, all 24 cross-pair gaps within 0.003). See [[blade-mesh-origin-inflates-reach]].
- Contact profile 0% / 3.28 -> 15% / 1.75 (centre-only fix) -> 100% / 0.13 ([[crafting-contact-profile-check]]). Healthy DADG one-handers are 88-100% @ 0.11-0.15.
- The first Blender re-export passed every tool check and was still 100x oversized in game: [[blender-fbx-roundtrip-breaks-scale]].
