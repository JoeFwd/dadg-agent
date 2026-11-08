---
name: dadg-combat-open-work
description: What the DADG combat overhaul has and has not proven live (8 sieges, absorption in siege 8), what remains unmeasured, troop re-equip (weapons and the 2026-11-08 armour audit) and stripped-vanilla-weapon gaps, and the design calls still open for the user
type: reference
topic: feature-combat
tags: [combat, verification, troops, open-questions]
sources: [doc/combat-overhaul-analysis.md (retired 2026-11-07), [combat-balance] siege logs 7-8, live evaluation on 1.4.8 build 119303]
updated: 2026-11-08
---

# Combat overhaul: verified, unverified, open

## Absorption-only change (2026-11-08, now measured in a siege)

**Current weapon-class refinement:** after the cut trial below, the user requested sword cuts on plate around 1–3 (1H), 2–5 (2H), with polearm cuts around 10–15. Absorption now uses nested `Material / Blow / Default-or-WeaponClass` elements. Plate Cut overrides .88/.94/.52 for OneHandedSword/TwoHandedSword/TwoHandedPolearm replace the .40 Default; all other defaults stay as in the trial. Half-sword counts as a sword. Code, XML, fixture and logger are synchronized; 33 combat tests and the actual C# parser check pass. Release build/deployment succeeded with 23 warnings, 0 errors after an initial transient DLL access denial. No live siege under the weapon overrides has been analysed yet. The prior snapshots below remain historical baselines. Schema/tuning: [[dadg-combat-rules-tuning]].

**Current trial, now measured live:** the user subsequently requested cut absorption Cloth/Padded/Mail/Brigandine/Plate = 0/5/15/25/40%, with all other settings unchanged. Applied to XML and test fixture; 27 combat tests pass. The siege ending **12:53:13** records all 20 material/blow cells matching the trial, with 7,673 total hits / 1,199 recorded kill flags, or 7,626 / 1,166 after excluding 47 Boulder hits. Both summary tables reconcile exactly. Personal mean damage by material is Cloth 38.16, Padded 25.05, Mail 16.99, Brigandine 14.52, Plate 12.83. Plate cut means are sword 10.58, axe 6.45 and polearm 16.15, close to the same-hit estimates. See [[dadg-combat-cut-trial-siege-2026-11-08]] for details and limitations. The historical siege below used the previous rates, including 80% plate cut; its fixed comparison table and estimated trial effects remain unchanged in [[dadg-combat-cut-progression-trial]].

The user chose one absorption row per material and blow type, removing `Resistance` and `SwordOnPlate`. Firearms still meet the full armour value, with no absorption. Current fractions and code are in [[dadg-combat-overhaul]]. The DLL and XML must ship together and the game must restart.

The first fit excluded sword-on-plate hits and used the later per-blow soft-armour fractions rather than those recorded in the logs. It was superseded by [[dadg-combat-absorption-refit]], which uses all 31,563 personal-weapon hits in battle 9 and siege 10, anchors estimates to observed damage, and uses each logged absorption fraction. The user chose 80% plate cut absorption to keep swords close to their previous damage; this cannot also preserve axe/polearm cut damage with one shared setting. Current values are in [[dadg-combat-overhaul]].

Initial verification: all 30 Domain combat tests passed; the live XML parses and all 15 fractions match `ShippedCombatRules`; Release solution build passed with `-m:1` (25 warnings, 0 errors). The default parallel build hit an ExpandedTemplate `SubModule.xml` write race. The sandboxed test runner stalled; the focused run outside the sandbox finished in 84 ms. Domain, Infrastructure and Integration DLL SHA-256 hashes matched their deployed `Win64_Shipping_Client` copies. After the log-based refit, all 27 combat tests passed. Core `b6a9392`, content `4f557546`, initial notes `a1d1a1a` committed the refactor, rates and buckler HP change.

**Latest siege, ending 2026-11-08 11:44:13:** all 20 observed material/blow cells match the current XML, and the old `effective=` field is absent on every hit. Parsed 8,696 hits / 1,084 recorded post-hit-dead flags; 8,636 personal hits / 1,039 flags after excluding cannonballs. Both weapon and armour summary tables reconcile exactly. Plate one-handed sword cuts average 3.54 (siege 10: 3.03), axe cuts 2.18 (9.22), polearm cuts 5.71 (15.17). No two-handed sword hit was recorded. Shield blocks are excluded, so these logs cannot verify buckler HP. See [[dadg-combat-latest-siege-2026-11-08]] for full analysis and confounds. These recorded death flags are not proven unique or causal deaths.

Pre-playtest estimates: plate sword cut means were 2.75 to 2.76 one-handed and 8.95 to 7.91 two-handed (only 58 hits). Axe and polearm cuts on plate were predicted to fall about 75–77%. Mail pierce was predicted to fall about 8% even at zero absorption; matching the old resistance would require damage amplification. Firearms were predicted to fall about 12% on cloth, 17% on padding, 30% on mail/brigandine and 33% on plate, as required by using full armour without absorption. Those are model estimates; the latest siege above supplies observations from a different hit mix.

## Verified live (historical rules, before the absorption-only change)

- **Crafted stats.** All 106 weapon usages match `wsim` on speeds and handling. Damage matches on 104, and one is off by 1. All 66 ladder weapons show their game tier within 0.11 of the port.
- **Resistance.** Material multipliers, plate sword overrides and the ladder ran over 7 sieges.
- **Absorption and the per-location table** ran in siege 8 (7,898 hits). The expected fraction matched on 15 of 16 groups. Plate fell from 19.8 to 10.5 mean damage per hit.
- **Field battle 9 (2026-11-08, 23,222 hits, 3,929 kills, 955 attackers, 25 min)** ran the XML rule rows live. Analysis script: `battle9.py` (scratchpad, parses `[combat-balance t=]` lines).
  - Hits per kill by material: Cloth 2.9, Padded 3.8, Mail 4.9, Brigandine 5.6, Plate 9.1. Plate took 60% of hits, and 30% of all hits were on the head, mostly sallets.
  - On plate, blunt beats pierce, which beats cut: 5.8, 8.9 and 10.3 hits per kill, as designed.
  - **One-handed swords are nearly useless on plate.** A cut does a mean of 2.6 damage (median 1) and takes 40.6 hits to kill, over 3,329 swings, which is 24% of all plate hits. Thrusts do 6.2 damage (17 hits per kill). That comes from `SwordOnPlate cut=1.6`. It is the biggest balance outlier.
  - Polearms decide the fight: 67% of kills. Lances alone took 925 kills, and 392 lance hits did 100 or more damage.
  - Firearms seem to hit plate harder than cloth (132 damage against 77). That is a location bias: 37 of 50 plate hits were on the head or neck. Effective armour is about 13, which is correct. Every firearm hit kills in about 2.
  - Thrusts behind the tip cost two-handed polearms 490 hits at 2.9 damage. These were longspears, Flemish pikes, boar spears and half-sword usages of `castillon_c`/`_b_twohander`.
  - The 271 "Unarmed" hits are kicks (78 of 80 attackers also used weapons).
  - Bolts `ddg_bolt_a/b/c` log as T?, meaning they have no tier.
- **Siege 10 (2026-11-08, 8,393 hits, 1,144 kills, 14 min)** confirms the battle-9 picture, more strongly.
  - Hits per kill by material: Cloth 3.4, Padded 4.8, Mail 7.0, Brigandine 6.9, Plate 12.2. 49% of hits were on the head, from fighting on the walls and ladders.
  - One-handed swords made 49% of all hits and 31% of kills. On plate, a sword cut does 3.0 damage and takes 35 hits to kill.
  - T2 melee weapons on plate do 3.5 damage and take 26 hits to kill.
  - Thrusts behind the tip: 365 hits produced 2 kills.
  - Blunt weapons on plate take 3.4 hits per kill.
  - Veuglaire cannonballs: 52 hits, 36 kills, 106 mean damage.
  - On soft armour, cuts got the least through: cloth 62–73% against 75–79% for thrusts and blunt, padded about 47% against about 60%. The initial per-blow absorption change on 2026-11-08 used these historical values: cloth soaked 0.25 and padding 0.3 of thrusts and blunt. The predicted result is about 60% through cloth and about 45% through padding, with plate unchanged. The later absorption-only change above supersedes those values and predictions.
  - **141 hits landed on wholly unarmoured men** (`none`, armour=0 on the head, body and arms). The log carries no victim id, so these troops are unidentified. They may be troops whose stripped vanilla armour loaded as empty slots.

## Not measured

- **Two-handed grip on plate.** Only battle 9 measured it, on 55 cuts. Damage was 8.8 from a raw 123, about 7% of raw, against 5% for one-handed swords. That looks like rough parity, but both grips barely hurt plate.
- **Bone mapping.** Which skeleton bones map to `BoneBodyPartType` Shoulder and Arm was never read from the game.
- **Missile totals.** Weapon plus ammo is assumed; the sum happens in native code.
- **Firearm falloff with range.**
- **Other modes.** Jousting, naval (War Sails), autoresolve drift and existing-save crafted stats are unchecked. Crafted stats rebuild from pieces, so removing a piece is unsafe.

## Open data work

- **Re-equip troops to the ladder** in `DellarteDellaGuerraMap`. Of 741 troop/weapon pairs, 97 carry an item at least 2 tiers above them and 125 at least 2 below.
- **Armour against troop tier (audited 2026-11-08, nothing changed yet).** This covers 140 reachable fighting troops. Reachable means referenced by a culture, a party template or the 2026-11-05 live party dump, plus everything they upgrade into. It excludes heroes and the level-1 `spc_*` minor-faction hero templates. That gives 2,673 troop/armour pairs, using the live roster dump with the current table tiers and `tier_override`s.
  - Over-tiered, 2 or more tiers above the troop: body 102, head 45, gloves 43, legs 21. The worst cases are about 20 low troops wearing T5–T6 kit. `dadg_burg_cav_t1` and `dadg_burg_valet_t1` (both T2) wear full harness and leg harness. `vlandian_recruit` (T1) gets brigandines, mail and visorless froissart sallets (T4).
  - Under-tiered on head and body, 3 or more below: 19 troops. Examples are `vlandian_banner_knight` and `vlandian_champion` (T6) in T3 sallets and war hats, `forest_bandits_chief`, the caravan masters and guards, `sword_sisters_*` and `western_crossbow_t4/t5`.
  - Legs are structural. Leg items are only T1 (28 hosen), T2 (8), T3 (6), T5 (12) or T6 (2). There is no T4, so 401 pairs sit 2 or more below the troop.
  - Mixed kits: 91 troops have sets whose materials span 3 or more grades between locations. Usually that is a plate head over cloth legs (80 troops), cloth arms (36) or cloth shoulders (33). Examples are `vlandian_sergeant` (Plate/Brigandine/Padded/Cloth), `vlandian_swordsman` and `vlandian_sharpshooter_2` (plate torso, cloth shoulders and arms). Per-location materials punish this now. Whether it is wrong or simply period-correct for infantry is the user's call.
  - 41 T4+ troops have sets without gloves, so their arm takes the sleeve material.
  - FIXED 2026-11-08: `vlandian_banner_knight` was removed at the user's request. Its upgrade from `vlandian_squire_dismount` went with it, and its three CustomSpawns stacks (Percy of Egremont, Neville of Middleham, Courtenay earl) now use `vlandian_champion`. `vlandian_champion` lost its six T3 helmets, which became `close_helmet` and `warwick_helmet_02/03`. The Burgundian mercenaries keep their own armour, so their levels were raised instead: `dadg_burg_cav_t1` 12→26, `cav_t2` 21→31 and `valet_t1` 12→16. That makes the mercenaries more elite.
- **Troops reference vanilla weapons that `dadg_pre_native_items.xslt` strips.** That is 69 ids used 169 times. The slot loads empty, with no crash.
  - FIXED 2026-11-08: pool 1 (crossbows) of the militia archers is now on DADG crossbows and bolts. `vlandian_militia_archer` (T2) uses `ddg_crossbow_g` and `yew_longbow_weak`; `vlandian_militia_veteran_archer` (T3) uses `dadg_crossbow`. Six cultures use these troops in their militias.
  - FIXED 2026-11-08: the hidden vanilla `vlandian_cavalry` had no weapons and appeared only in the English patrol templates. It is now replaced by `vlandian_light_cavalry` (English Hobelar, also level 21).
  - The count of 69 included every troop, even unused ones. Recount using only the troops a culture, upgrade path or party template reaches before fixing the rest.
- **Mispriced shields.** `bucklers_a/_b/_c` show tier 15.89 and 193,295 gold, and `vlandian_recruit` carries them. Arrows, `bundle_of_arrows` and `linen_quiver` need real prices.
  - **Buckler HP fixed 2026-11-08:** `bucklers_a`, `bucklers_b` and `bucklers_c` in content `ModuleData/items/items.xml` were reduced from 1,020 to 250 HP, matching small targes and below ordinary shields (285–430 HP). Only HP changed; XML parsing and a full semantic comparison verified every other item field stayed unchanged. The untracked generator at Core `tools/combat/apply_combat_data.py` does not rewrite shield HP. XML reload requires a restart; no new build or live playtest was performed.
- **Tooltips and encyclopedia** don't show location armour yet.

## Open calls for the user (set by default)

1. Ladder shape: the T6 picks, longswords from T3, the long pike at T5.
2. Lethality: plate now wears down rather than being near-immune.
3. Firearm strength: an arquebus does about 95 on plate.
4. The hand-classified armour materials.
5. When to move to 1.5.x: the models need a rebuild and a recheck.

Related: [[dadg-combat-overhaul]], [[dadg-weapon-ladder]], [[dadg-armour-values]], [[dadg-combat-rules-tuning]]
