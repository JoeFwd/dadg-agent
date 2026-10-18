---
name: dadg-cannons-mesh-folder-has-no-mtl
description: 2026-09-02 cannonball pile rendered flat grey (material trailer "default"); Assets/cannons is the one mesh folder with no _mtl.tpac beside it, its material sits in Assets/firearms
type: incident
topic: feature-cannons
tags: [cannonball-pile, tpac, material, assets]
sources: [memory/tpac-material-binding-trailer.md]
updated: 2026-10-18
---

# Cannonball pile bound to "default" (2026-09-02)

Technique and diagnosis: [[tpac-material-binding-trailer]].

- `CannonBallPiles_geo.tpac`: trailer@160708, 142 bytes. FBX declared `Material 'cannonball_pile'` connected to `Model '<prefix>_cannonball_pile'`; material at `Assets/firearms/cannonball_pile_mtl.tpac`. The trailer still read `default`.
- DADG keeps `_geo.tpac` and `_mtl.tpac` in the same folder everywhere except `Assets/cannons/`, whose material sits in `Assets/firearms/`: the prime suspect for the lost binding.
- Same asset also had a scale bug: [[invisible-mesh-is-scale-not-shader]]; white pile later traced to AO: [[cannonball-pile-white-is-ao-coef]].
