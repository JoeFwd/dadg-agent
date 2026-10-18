---
name: cannonball-pile-material-investigation
description: Cannonball pile looked matte because its material lacks use_specular; correction not yet applied as of 2026-09-07.
type: incident
topic: items-crafting
tags: [material, cannonball, tpac]
sources: [src/doc/investigations/cannonball-pile-material.md]
updated: 2026-10-18
---

# Cannonball pile material investigation

The pile material `cannonball_pile` (shader `stone_pile_deformer`) uses the same three textures as `musketball` but omits `use_specular`, which explains its matte look ([[material-without-use-specular-looks-matte]]). Mesh scale 40 was already corrected and depletion works. Proposed fix: enable `use_specular` in the editor, validate with argument Y=0,1,10,20 (expect 20,19,10,0 balls). Status: diagnosis verified, fix not applied or visually tested. A related white-pile cause is the ambient occlusion coefficient ([[cannonball-pile-white-is-ao-coef]]).

Source docs: src/doc/investigations/cannonball-pile-material.md.

Related: [[material-without-use-specular-looks-matte]]
