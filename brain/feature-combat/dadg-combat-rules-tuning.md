---
name: dadg-combat-rules-tuning
description: How to retune DADG combat - rule rows in dadg_combat_items.xml need no rebuild; the two untracked generators own weapon and armour rows and overwrite hand edits; edit the live content module; read [combat-balance] logs
type: howto
topic: feature-combat
tags: [combat, tuning, xml, tools]
sources: [Core tools/combat/*.py (untracked), session 2026-11-07]
updated: 2026-11-08
---

# Tuning DADG combat

`dadg_combat_items.xml` has three blocks, in this order. Each block has one owner.

| Block | Rows | Owner |
|---|---|---|
| Rules | `Absorption`, `HalfSword`, `NonTipThrust` plus their comment | Hand-edited. Both generators keep them verbatim |
| Weapons | `<Tier id= tier= />` | `tools/combat/apply_combat_data.py` |
| Armour | `<Armour id= torso= shoulder= arm= legs= head= />` | `tools/combat/apply_armour_data.py` |

**Rules are read at game start, so retuning values needs a restart, not a rebuild.** Absorption uses a predictable element hierarchy: `Absorption / Material / BlowType / Default-or-WeaponClass`. All leaf values are final-damage absorption fractions on top of the full item armour value. A matching weapon entry replaces Default; a missing class uses Default, and a missing material/blow absorbs 0. Firearms always absorb 0. Fractions must be finite, at least 0 and below 1. Invalid names, duplicate entries, attribute rows and invalid fractions fail loading with the repository's existing error log/neutral fallback.

For example, the Plate branch contains:

```xml
<Plate>
  <Cut>
    <Default>0.4</Default>
    <OneHandedSword>0.88</OneHandedSword>
    <TwoHandedSword>0.94</TwoHandedSword>
    <TwoHandedPolearm>0.52</TwoHandedPolearm>
  </Cut>
  <Pierce><Default>0.18</Default></Pierce>
  <Blunt><Default>0.16</Default></Blunt>
</Plate>
```

`CombatWeaponClass` defines the supported weapon entry names. `AgentArmourReader.WeaponClassOf` maps current usage to them, treating half-sword as TwoHandedSword. Damage and the logger use the same selected fraction. The previous resistance/SwordOnPlate armour-value rules remain removed; these are final absorption overrides, not additional stacked multipliers. A missing `HalfSword` or `NonTipThrust` turns that rule off. Update `DellarteDellaGuerra.Domain.Tests/Combat/ShippedCombatRules.cs` with XML changes. The nested parser and XML must ship together; the old attribute schema is rejected.

## Generators

They live in Core `tools/combat/`. They are deliberately **untracked**: the user said not to commit `tools/`.
- **`apply_combat_data.py <content module> <Native module>`** owns weapons. It splits the long pike head, sets piece weights and damage types, solves blade `damage_factor` from target stats, patches ranged damage and values, validates, and prints the stat table. `wsim.py` is its port of the game's crafted-weapon calculation.
- **`apply_armour_data.py <content module>`** owns armour: values, `weight`, `tier_override`, `material_type` and the table's armour rows.
- **Both are idempotent, but they overwrite hand edits.** Any factor, price or armour value tuned by hand must go into the script first.
- `apply_combat_data.write_table` preserves the complete nested Absorption block and its comment; its item validation skips rule elements. The function was checked in isolation without running weapon edits. If adding another rule element, extend its keep-regex. `apply_armour_data` keeps everything before the first `  <Armour `.

## Content location

Edit `Modules/DellarteDellaGuerra/ModuleData/...` on develop, which the game loads. The redundant content worktree `Core/src/.worktrees/dadg-combat-overhaul` was removed on 2026-11-08.

## Measuring

`CombatBalanceMissionLogic` writes one `[combat-balance t=...]` Debug line per hit on a person to the DADG log. At mission end it writes Info tables per weapon and per armour piece.
- `raw=` adds the absorbed damage back, so it stays comparable with logs from before absorption existed. `absorbed=` is the fraction taken off.
- `armour=` is the item value before perks. The old `effective=` material-scaled value was removed with resistance.
- The logger is temporary. Remove it once the balance settles.

Related: [[dadg-combat-overhaul]], [[dadg-weapon-ladder]], [[dadg-armour-values]], [[bannerlord-xml-load-abort-semantics]]
