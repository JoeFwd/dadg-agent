---
name: dadg-cannonball-pile-fbx-scale-incident
description: CannonBallPiles.fbx imported 100x too small (Lcl Scaling 0.01); the prefab scale="40" was a wrong compensation tuned against the collision proxy
type: incident
topic: items-crafting
tags: [cannons, fbx, scale, prefab]
sources: [memory/blender-fbx-roundtrip-breaks-scale.md]
updated: 2026-10-18
---

# Cannonball pile scale incident (2026-09-15)

- 2026-08-06: a no-edit Blender round-trip of `GriffinMesser.fbx` was the test case that isolated the `FBX_SCALE_NONE` corruption. On 2026-08-05 the Scottish arming sword passed every tool check and was still 100x oversized in game.
- 2026-09-15: `CannonBallPiles.fbx` imported 100x **small**. The long-healthy commit `b2e0f20` had `UnitScaleFactor = 1` and no model-level `Lcl Scaling`; `e1d88bd` had `UnitScaleFactor = 100` with `Lcl Scaling = 0.01`.
- The pile had been compensated with `scale="40"` in `Prefabs/cannons.xml`, but the real error was exactly 100: the pile's balls are the same 98-vertex sphere as the `small_cannonball` item mesh and their radius ratio is 100.0000. The 40 had been dialled against `bo_small_cannonball`, the *collision proxy*, which is itself 2.5x smaller than the visual ball, leaving the mesh at 40% of correct size.

Same asset, other bugs: [[cannonball-pile-white-is-ao-coef]] (white shading), and invisibility in battle came from the mesh being stripped from the live prefab while surviving in the editor-only `_ghost` prefab.

Generic rules: [[blender-fbx-roundtrip-breaks-scale]].

Generic rule: [[invisible-mesh-is-scale-not-shader]]
