---
name: dadg-weapon-ladder
description: DADG weapons follow a vanilla-anchored T1-T6 ladder (troop level 6/11/16/21/26/31), ~10% per tier, role over tier; target stats, shared blades, gaps and the polearm weight compromise
type: reference
topic: feature-combat
tags: [combat, weapons, crafting, tiers]
sources: [doc/combat-overhaul-analysis.md (retired 2026-11-07), tools/combat/apply_combat_data.py, live check on 1.4.8 build 119303]
updated: 2026-11-07
---

# DADG weapon ladder

Before the ladder, DADG damage followed no tier logic. Every 1H sword was piece tier 3, swings ran 59–108 with no link to troop level, and values sat far above vanilla (DADG's top 2H swing was 165, vanilla's T5 median 128). The ladder replaced that. **The per-item assignments live in `apply_combat_data.py`** (`WEAPON_TIERS`) and in the `<Tier>` rows. That code is the source of truth, not this note.

## Rules

- Tiers follow troop tiers: level 6 → T1, 11 → T2, 16 → T3, 21 → T4, 26 → T5, 31+ → T6.
- Vanilla values are the anchor. Each tier adds about 10%.
- Role beats tier: a T3 pollaxe outhits a T6 sword and pays in speed.
- A family needn't fill all six tiers. Longswords start at T3, and peasant tools fill T1.

## Target stats (swing/thrust)

| Family | T1 | T2 | T3 | T4 | T5 | T6 |
|---|---:|---:|---:|---:|---:|---:|
| 1H sword | 48/26 | 56/30 | 64/34 | 70/38 | 76/42 | 82/46 |
| Longsword (1H grip) | – | – | 68/38 | 74/42 | 80/46 | 86/50 |
| 2H sword | – | – | 92/42 | 102/46 | 112/50 | 122/54 |
| 1H axe, pick | 44/– | 58/– | 68/– | 76/– | 82/– | 88/– |
| Mace, hammer (Blunt) | 26/– | 36/– | 46/– | 54/– | 62/– | 68/– |
| Staff, club (Blunt) | 44/20 | 54/24 | 64/28 | – | – | – |
| Polehammer, maul (Blunt) | – | – | – | 72/38 | 80/42 | 88/46 |
| Pollaxe, 2H axe | – | – | 105/30 | 118/34 | 130/38 | 142/42 |
| Bill, halberd, glaive | 64/24 | 76/28 | 88/32 | 100/36 | 112/40 | 124/44 |
| Peasant 2H tools | 50/24 | – | – | – | – | – |
| Spear | –/24 | –/28 | –/32 | –/36 | –/40 | –/44 |
| Pike | – | –/30 | –/34 | –/38 | –/42 | –/46 |
| Lance | – | – | – | –/42 | –/46 | –/50 |
| Javelin | – | –/60 | –/78 | –/96 | –/110 | –/124 |

All targets land within 1, except where a blade is shared:
- `ddg_lochaber_axe_head`: the Lochaber axe gets 131 and `execution_axe` 107 (target 118).
- `lance_head_01`: `lance_b` gets 46, `lance_a_*` 40 (target 42).
- `rigsby_axe` keeps its thrust of 30.

The long pike got its own blade, split from `ddg_england_twohandedpolearm_longspearhead`.

## Data facts

- **Damage lives on the blade's `damage_factor`** in `DDG_CraftingPieces.xml`. Editing a factor moves every item on that blade, including the `dadg_hardcoded_weapons.xslt` copies (`battania_mace_1_t2`, `short_sword_t3`).
- **Weight changes speed and base magnitude, so solve factors after geometry.** Never hand-edit factors; the script solves them.
- **Damage types were corrected.** Leadhammer, pollhammer, warclub, quarterstaff and brogitstaff are Blunt. The scythe and sickle swings are Cut, and the pickaxe swing is Pierce. Tourney weapons should be Blunt.
- **Polearm weights are a compromise.** The first targets dropped bills to swing speed 59, so bills sit at 1.25–1.9 and pikes at 1.76–2.66, below vanilla's 1.9 and 2.2 because DADG's are longer. The Old Halberd is still slow: swing 43.
- **Ranged weapons are hand-authored** and use `tier_override`. Firearm values (handgonne 90, arquebus 105, bronze 120 plus the ball) are first guesses.

## Gaps

- 1H axe has no T4–T6.
- Bill has no T6, polehammer no T6, lance no T5–T6.
- Only one dagger exists, and no troop carries it.

Related: [[dadg-combat-overhaul]], [[dadg-combat-rules-tuning]], [[crafted-weapons-ignore-tier-override]], [[crafted-weapon-stats-driven-by-weaponflags]]
