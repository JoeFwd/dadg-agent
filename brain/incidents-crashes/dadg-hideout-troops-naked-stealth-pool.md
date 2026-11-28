---
name: dadg-hideout-troops-naked-stealth-pool
description: Troops spawn naked in hideouts. ExpandedTemplate maps the Stealth mission mode to a stealth-only pool, and DADG has zero stealth="true" rosters, so the pool is empty and nothing falls back to battle gear
type: incident
topic: incidents-crashes
tags: [hideout, expanded-template, equipment, stealth]
sources: [static analysis 2026-11-26, ExpandedTemplate a4ea2a9 "Support stealth equipment types" 2026-09-07]
updated: 2026-11-26
---

# Hideout troops spawn naked (FIXED in ExpandedTemplate f6ac56a, 2026-11-26)

The chain:
1. The hideout mission runs in `MissionMode.Stealth` ([[hideout-mission-runs-in-stealth-mode]]).
2. ExpandedTemplate `EncounterTypeProvider` returns `EncounterType.Stealth` when the mode is Stealth.
3. `GetEquipmentPoolsUtil` then asks only `TroopStealthEquipmentPoolProvider`, which keeps rosters whose resolved flag is `stealth`.
4. DADG has no `stealth="true"` or `equipmentType="stealth"` rosters, so the pool is empty. Nothing falls back to the battle pool.
5. `EquipmentSetterPatch` then maps the empty pool to an empty `MBEquipmentRoster`. `Equipment.GetRandomEquipmentElements` returns an empty `Equipment`, and `FixedEquipment(true)` locks it in.

Affected: every non-hero troop that ExpandedTemplate overrides, bandits and the player's own soldiers alike. Unaffected: player-clan heroes (`CanOverrideEquipment`) and characters without a roster reference.

This regression came with ExpandedTemplate a4ea2a9 (2026-09-07). The user confirmed it live: dadg.log showed `No equipment found ... in Stealth encounter` for every hideout troop. Fix f6ac56a: `GetEquipmentPoolsUtil` falls back to the battle pool when a stealth encounter has no loadouts. Adding `stealth="true"` to every roster was rejected: about 4,900 rosters, and the 1,152 unflagged rosters would drop out of battle gear.

Unrelated finding from the same audit: `dadg_bandits.xml` has stale vanilla item ids. Most are in civilian rosters (e.g. `battania_woodland_outfit`, `patched_gambeson`, `bandit_fur_a`). A few are in battle sets: `ddg_crossbow`, `dunham_bevor`, and the double-prefixed `Item.Item.bucklers_b`. Each one only empties its own slot.

Related: [[disguise-naked-empty-defaultequipment]]
