---
name: dadg-combat-data
description: Regenerate DADG combat data: the T1-T6 weapon ladder, damage factors, and the per-body-part armour material table in dadg_combat_items.xml. Use when changing how an armour maps to materials per body part, adding armour or ladder weapons, or solving weapon damage factors.
---

# DADG Combat Data

`scripts/apply_combat_data.py` writes the combat data into the content module. `scripts/wsim.py` is its weapon stat simulator and must stay beside it.

## Run

```powershell
python scripts\apply_combat_data.py <DellarteDellaGuerra module> <Native module>
```

It splits the long pike's head, sets piece weights and damage types, solves damage factors, patches ranged damage, values and `arm_armor` caps, writes `ModuleData/CustomXml/dadg_combat_items.xml`, then validates and prints the stat table. Two runs in a row give the same result.

A run overwrites anything tuned by hand since the last one. Factors tuned from battle logs live in `DDG_CraftingPieces.xml`, not in `LADDER`, so move them into the script first or edit the XML directly.

## How armour maps to materials

| Item | Rule |
|---|---|
| Body armour | First match in `BODY_RULES` by item id gives (torso, sleeves). No match: the XML `material_type` goes on both |
| Shoulder, arm | Both take the sleeve value, so they can't differ yet |
| Body armour legs | The torso material, if `leg_armor` is above 0 |
| Helmets, gloves | XML `material_type` |
| Leg armour | XML `material_type`, except `LEG_RULES` ids (`maillestrips`, `legsplints`) |

`FALLBACK` maps XML materials: Cloth to Cloth, Leather to Padded, Chainmail to Mail, Plate to Plate.

`BODY_RULES` came from the arm faces of the 74 of 136 body meshes that could be read from FBX, corrected by hand, and from item names for the rest. Material names mislead: `brigadine.001` covers both torso and cloth sleeves on `brigandine_a/b/c`. The 74 items with no rule use the XML fallback, and their meshes may never have been read.

An item can hold only one `ItemComponent`, and a second `<Armor>` replaces the first, so per-part materials have to stay in this table.

The copies in the mod repo's `tools/combat/` are the same scripts. Keep them in step.
