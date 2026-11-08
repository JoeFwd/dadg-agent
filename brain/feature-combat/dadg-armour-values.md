---
name: dadg-armour-values
description: DADG armour classes, value bands, helmet coverage formula, weights and tier_override per class, set from a Blender ray-cast of each FBX; and why mesh material names mislead sleeve detection
type: reference
topic: feature-combat
tags: [combat, armour, items, blender]
sources: [doc/combat-overhaul-analysis.md (retired 2026-11-07), tools/combat/apply_armour_data.py, armour_stats.csv]
updated: 2026-11-07
---

# DADG armour values

`apply_armour_data.py` owns every value below. A Blender pass cast rays at each armour FBX. It recorded the strongest layer on each body part and, for helmets, the share of skull, face and neck covered. The old data had a Flemish jack at 12 body armour, almost every body armour at 11.3 kg, and every piece of mail or better showing Tier 6.

## Body (one class per item → arm, leg, weight, tier, materials)

| Class | Body | Tier | Weight kg |
|---|---|---:|---|
| Full harness | 64–70 (gilt 74–76) | 6 | 16–17 |
| Cuirass with mail | 57–60 | 5 | 12–14 |
| Irish harness | 60 | 5 | – |
| Brigandine with plate arms | 50–54 | 5 | 9–14 |
| Brigandine over mail | 46–48 | 4 | 9–14 |
| Brigandine / breastplate | 40–46 | 4 | 9–14 |
| Mail | 38–40 | 4 | 9–12 |
| Jack with mail | 28–32 | 3 | 5–9 |
| Padded jack | 23–27 | 2 | 5–9 |
| Clothing | ≤10 | 1 | 1.5 |

- The Flemish jack has mail under the cloth, so it is Mail on torso and legs: 32 body armour, Tier 3.
- The mailshirt with livery coat went from 64 to 38.
- Shoulders carry their own material, so a brigandine with cloth sleeves reads Cloth on the shoulder and arm.

## Helmets

`head = 20 + 0.48 × (0.3 skull + 0.4 face + 0.3 neck)`, ×0.9 for munition sallets.

- Great bascinets, Warwick helmets and the frogmouth: 61–63.
- Flemish helmet 58, armets 56, close helmet 50.
- Visored sallets 42–46, kettle hats 38, open sallets 37.
- An opened visor costs 4–9, so the V toggle is a real trade-off.
- Helmet tier follows the computed value.

## Legs, gloves, weights

- Full leg harness 32–36 (gilt and Henry 40), 6 kg. Poleyn hosen 12. Splints 16 (Brigandine). Mail strips 14 (Mail).
- Plate gauntlets 22, fluted and gilt 24–26, mittens 20. All gloves weigh 1.2 kg.
- Closed helmets weigh 3.8 kg, visored sallets 3.0, open helmets 2.4.
- Prices were not changed.

## Mesh material names are a weak signal

The sleeve and part detection reads FBX material names per bone group (arm bones `l_upperarm_twist`, `l_foretwist` and the `r_` pair). Known traps:
- **One material for the whole garment.** `brigadine_a/_b/_c` use `brigadine.001` on the sleeves too, and so does the `brigandine_over_mail` family.
- **Outer layers hide what's underneath.** `livery_coat_over_mail` reads as cloth.
- **Some names say nothing.** `Material.027` can't be mapped.
- **The game reads `_geo.tpac`, not the FBX** ([[fbx-edits-need-tpac-reimport]]). The two could differ.

Some materials were hand-classified from item names, without reading the meshes. The user has not reviewed them yet: [[dadg-combat-open-work]].

Related: [[dadg-combat-overhaul]], [[head-armour-sums-all-slots]], [[crafted-weapons-ignore-tier-override]]
