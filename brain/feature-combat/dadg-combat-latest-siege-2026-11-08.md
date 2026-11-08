---
name: dadg-combat-latest-siege-2026-11-08
description: Live absorption-only siege completed at 11:44 on 2026-11-08; 8696 hits reconcile with end summaries, sword/axe/polearm plate observations and sparse firearm evidence versus siege 10
type: reference
topic: feature-combat
tags: [combat, siege, absorption, balance, logs, playtest]
sources: [DellarteDellaGuerra.Core/log/dadg.log, siege10.log, CombatBalanceMissionLogic.cs, DadgStrikeMagnitudeModel.cs, dadg_combat_items.xml]
updated: 2026-11-08
---

# Latest completed siege: absorption-only rules observed live

The latest completed mission in the supplied log is the **2026-11-08 siege ending at 11:44:13**. It contains **8,696 logged body hits and 1,084 recorded kill flags**, including 60 cannonball hits / 45 kill flags. Personal weapons, missiles and unarmed attacks account for **8,636 hits / 1,039 flags**. Every hit parses and both end-of-mission tables reconcile exactly.

All observed absorption fractions match the new rules. There is no `effective=` field anywhere in this mission's hit records. This is runtime evidence for the absorption-only refit; the current XML alone would not establish what the run loaded. One-handed sword cuts on plate remain weak (3.54 mean damage), while axe cuts (2.18) and polearm cuts (5.71) show the intended substantial loss versus the previous resistance rules. There are **no two-handed sword hits**, so this run cannot validate that class.

## Source, mission boundary and reproduction

Read-only source: `D:/SteamLibrary/steamapps/common/Mount & Blade II Bannerlord/Modules/DellarteDellaGuerra.Core/log/dadg.log` (relative to Core `src`: `../log/dadg.log`). Snapshot: **36,906,465 bytes / 106,910 lines**, SHA-256 **`5de65ac666b0c6e3721e142e20cdd52b0bfdb05502556bf6a8f4948efef6f209`**. Internal record timestamps determine recency; filesystem mtime is not reliable here and the earlier 02:11 mission is not the latest one.

Exact one-based source ranges:

- **96,557**: `2026-11-08 11:25:57`, `[siege-ai t=0.1]`: three lanes, left/right `SiegeLadder,SiegeLadder,SiegeTower`, middle `BatteringRam`, inner/outer gates closed. **96,558**, `11:26:14`, `t=0.6`: `BehaviorWaitForLadders`, `BehaviorUseSiegeMachines` and deployed formations. These provide positive siege-assault evidence; a named settlement/scene ID is not present in this setup interval.
- **96,562–106,041**: first through last body-hit records, `11:29:19–11:43:52`, combat `t=32.5–868.5`, **836.0 seconds / 13m56s** of hit activity. Interspersed siege-AI records explain why this 9,480-line interval contains 8,696 hit lines.
- **106,053**: `11:44:12`, final siege diagnostic `t=887.7` (14m47.7s), both gates destroyed/open, attackers inside, formations assaulting walls. Wall clock includes deployment, pauses/loading and possibly debugging, so do not equate it with simulation time.
- **106,054–106,428**: 375 weapon summary rows; **106,429–106,910**: 482 armour summary rows; all timestamped `11:44:13`. `CombatBalanceMissionLogic.OnEndMission()` emits these tables. They prove the mission ended; they do not themselves prove a victory, settlement capture or casualty-screen result.

The prior completed siege's combat clock ends at `873.3` before this run resets to `32.5` on its first hit; the new siege diagnostics start at `0.1`. No later combat hit or mission-end summary follows this latest set in the snapshot. The log also contains many earlier missions and a later-starting high-clock field mission: do not take all hits since file start or use one naive clock-decrease split over the entire historical log.

Baseline: `C:/Users/Joe/AppData/Local/Temp/claude/D--SteamLibrary-steamapps-common-Mount---Blade-II-Bannerlord-Modules-DellarteDellaGuerra-Core-src/530e0b87-9c92-4c0f-bc7b-09fb06c4e5b4/scratchpad/siege10.log`, SHA-256 `71e859717e2ea92eef461ea9cb556d9ec471c6e34d9d78cd9af25904293a9ede`. All 8,393 baseline hits parse; 52 are Boulder cannonballs, leaving **8,341 personal hits**. Old runtime fractions were Cloth .05, Padded .10, Mail .20, Brigandine .25, Plate .40 for all non-firearm blows, firearm zero, with the former resistance/sword-on-plate logic.

Reproduction scratch files, deliberately untracked: Core `src/.tmp/latest-siege-analysis/analyse.py`, `results.json`, `tables.py`, `write_note.py`, `inspect.py` and `latest-hit-lines.log`. `analyse.py` parses the fixed line range and baseline, separates `WeaponClass=Boulder`, computes grouped statistics, and independently checks every summary key for hit count, kill count, maximum and mean (rounded to the logger's 0.1 precision). No code, XML, game state or existing brain note was changed by this analysis.

## What the logger measures

`CombatBalanceMissionLogic` logs human `StrikeAgent` collisions with a non-null attacker. It excludes horse charges, falls, shield-blocked blows and collisions with shields on backs. These are landed body hits, not swings/shots fired or block rates. **The buckler change from 1,020 to 250 HP cannot be verified from these logs**, nor can its runtime loading time be established here.

The logger defines `killed` as `affectedAgent.Health < 1` after the hit. This parser uses displayed `hp < 1` and matches every summary kill tally, so rounding causes no aggregate discrepancy in this snapshot. Nevertheless these are **recorded post-hit-dead flags, not verified distinct or causally attributable deaths**. Three zero-damage hits also carry a kill flag. The log lacks victim IDs, so no per-victim hit sequence, healing, unique-death count or true hits-to-kill/time-to-kill can be reconstructed. `by=` identifies the attacker, not the victim. A final blow on an already-injured opponent does not measure full-health lethality.

All “hits/kill” below mean the descriptive ratio `logged hits / recorded kill flags`. Materials are the struck location's material, not a whole soldier's armour class. `armour` is rounded base body-part armour; perks and other native adjustments may differ. `raw` is reconstructed from final damage plus absorbed armour and integer truncation; it is **not original strike magnitude**. Do not feed it uncorrected into the vanilla formula and report the result as observed damage.

## Rules actually observed

Each cell below gives **fraction (hit count)** across all logged hits, including cannonballs in Blunt. There is exactly one observed fraction per material/blow cell; there are no mixed old/new fractions.

| Material | Cut | Pierce | Blunt | Firearm |
| --- | --- | --- | --- | --- |
| Cloth | 0.05 (648) | 0.03 (687) | 0.03 (148) | 0.00 (7) |
| Padded | 0.10 (242) | 0.02 (307) | 0.10 (56) | 0.00 (2) |
| Mail | 0.09 (230) | 0.00 (206) | 0.11 (27) | 0.00 (1) |
| Brigandine | 0.07 (172) | 0.03 (258) | 0.10 (39) | 0.00 (2) |
| Plate | 0.80 (3,443) | 0.18 (1,974) | 0.16 (241) | 0.00 (6) |

All 15 non-firearm rates and all five firearm-zero cells agree with the live `ModuleData/CustomXml/dadg_combat_items.xml`. All **8,696** hit records omit `effective=`; old siege 10 records include that field. Current `DadgStrikeMagnitudeModel.CalculateAdjustedArmorForBlow` forwards its parameters unchanged to the wrapped model, and `ComputeRawDamage` also forwards. Together these observations are consistent with removal of DADG resistance and the sword-on-plate armour override. The absence of `effective=` alone would only show a logging-format change, so the conclusion uses per-hit fractions and current implementation as well. This log does not directly expose the final internal armour after native perks.

The native formula remains the basis: `r = M*50/(50+A)` and `damage = b*r + (1-b)*max(0,r-a*A)`, with `b=.10/.25/.60` and `a=.50/.33/.20` for cut/pierce/blunt before subsequent factors and final DADG absorption. Firearms use pierce armour handling and zero extra absorption. “Zero absorption” does not mean bypassing armour.

## Overall and material outcomes

All tables from here exclude cannonballs unless explicitly marked otherwise. Unarmed attacks and zero-damage hits remain included. Siege 10 is the old rules baseline, not an identical replay.

| Metric | Siege 10 | Latest |
| --- | --- | --- |
| Hits | 8,341 | 8,636 |
| Recorded kill flags | 1,108 | 1,039 |
| Mean damage | 15.99 | 14.84 |
| Median damage | 9.00 | 7.00 |
| Total logged damage | 133,360 | 128,187 |
| Hits / recorded kill | 7.53 | 8.31 |
| Head-hit share % | 49.20 | 51.54 |

Personal-hit count rises 3.5%, mean damage falls 7.2%, total logged damage falls 3.9%, and recorded kill flags fall 6.2%. The descriptive hit/kill ratio rises from 7.53 to 8.31 (+10.4%). Those changes include weapon mix, location, armour and skill differences; they are not a controlled estimate of the rules change.

| Location material | Latest hits | Mean damage | Median | Kill flags | Hits/kill | Siege 10 hits / mean / flags / hits-per-flag |
| --- | --- | --- | --- | --- | --- | --- |
| Cloth | 1,470 | 36.51 | 36.00 | 429 | 3.43 | 1,433 / 36.39 / 419 / 3.42 |
| Padded | 599 | 25.51 | 23.00 | 131 | 4.57 | 622 / 23.22 / 121 / 5.14 |
| Mail | 463 | 17.87 | 15.00 | 60 | 7.72 | 523 / 17.41 / 74 / 7.07 |
| Brigandine | 458 | 17.82 | 16.00 | 67 | 6.84 | 478 / 17.45 / 65 / 7.35 |
| Plate | 5,646 | 7.58 | 4.00 | 352 | 16.04 | 5,285 / 9.33 / 429 / 12.32 |

Plate receives **65.4% of personal hits** and **33.9% of personal kill flags**. Mean damage drops from 9.33 to 7.58 (−18.8%), and plate's descriptive ratio rises from 12.32 to 16.04 (+30.1%). This is the clearest aggregate change. Cloth is nearly unchanged in mean damage and ratio; other materials have smaller, mixed changes.

Location selection is pronounced: **75.4% of plate hits are head hits**, compared with 13.3% of cloth hits; Mail/Padded/Brigandine have no `Head`-classified body hits in this run. This is expected from helmets being plate, but it prevents reading the material table as a fair equal-location armour comparison.

Damage type by material (latest counts and flags, with old mean for comparison):

| Material / blow | Hits | Mean | Median | Kill flags | Hits/kill | Siege 10 n / mean |
| --- | --- | --- | --- | --- | --- | --- |
| Cloth / Cut | 648 | 43.02 | 43.00 | 214 | 3.03 | 667 / 41.71 |
| Cloth / Pierce | 687 | 31.29 | 31.00 | 181 | 3.80 | 669 / 31.23 |
| Cloth / Blunt | 128 | 29.80 | 9.00 | 29 | 4.41 | 91 / 32.76 |
| Cloth / Firearm | 7 | 69.43 | 63.00 | 5 | 1.40 | 6 / 75.50 |
| Padded / Cut | 242 | 28.77 | 24.00 | 56 | 4.32 | 266 / 23.16 |
| Padded / Pierce | 307 | 23.24 | 22.00 | 63 | 4.87 | 311 / 23.46 |
| Padded / Blunt | 48 | 22.52 | 22.50 | 11 | 4.36 | 42 / 18.45 |
| Padded / Firearm | 2 | 51.00 | 51.00 | 1 | 2.00 | 3 / 70.33 |
| Mail / Cut | 230 | 19.12 | 15.00 | 32 | 7.19 | 245 / 18.62 |
| Mail / Pierce | 206 | 15.88 | 14.00 | 22 | 9.36 | 234 / 16.65 |
| Mail / Blunt | 26 | 22.11 | 30.00 | 6 | 4.33 | 42 / 13.21 |
| Mail / Firearm | 1 | 30.00 | 30.00 | 0 | — | 2 / 47.00 |
| Brigandine / Cut | 172 | 20.58 | 17.00 | 31 | 5.55 | 209 / 18.45 |
| Brigandine / Pierce | 258 | 16.01 | 15.00 | 33 | 7.82 | 229 / 15.90 |
| Brigandine / Blunt | 26 | 16.15 | 4.00 | 3 | 8.67 | 38 / 18.76 |
| Brigandine / Firearm | 2 | 36.50 | 36.50 | 0 | — | 2 / 65.00 |
| Plate / Cut | 3,443 | 3.95 | 3.00 | 125 | 27.54 | 3,414 / 6.97 |
| Plate / Pierce | 1,974 | 11.77 | 7.00 | 171 | 11.54 | 1,675 / 11.60 |
| Plate / Blunt | 223 | 24.92 | 31.00 | 52 | 4.29 | 189 / 28.42 |
| Plate / Firearm | 6 | 69.00 | 78.50 | 4 | 1.50 | 7 / 104.71 |

Plate cuts fall from 6.97 to 3.95 mean (−43.4%); plate pierce is 11.77 versus 11.60 (+1.5%); plate blunt is 24.92 versus 28.42 (−12.3%). The broad blunt group includes unarmed contacts, so do not interpret its mean as a mace-only result. Mail pierce is 15.88 versus 16.65 (−4.7%); the earlier refit's expected loss with full vanilla armour and a zero-clamped absorption remains plausible, but this independent run does not isolate the model effect.

## Weapon mix and like-for-like material comparison

Weapon classes are the logger's current-usage classes; missile classes describe ammunition (`Arrow`, `Bolt`, `Cartridge`) even when the weapon ID names the launcher. Class totals include all blow types, including blunt contact and thrust/swing alternatives.

| Class | Hits | Hit share | Mean damage | Kill flags | Flag share | Hits/kill | Siege 10 n / mean / flags |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OneHandedSword | 4,525 | 52.4% | 10.84 | 417 | 40.1% | 10.85 | 4,101 / 9.99 / 358 |
| OneHandedAxe | 253 | 2.9% | 9.79 | 24 | 2.3% | 10.54 | 215 / 13.21 / 19 |
| TwoHandedPolearm | 2,561 | 29.7% | 18.18 | 420 | 40.4% | 6.10 | 2,868 / 20.73 / 558 |
| Mace | 98 | 1.1% | 37.80 | 33 | 3.2% | 2.97 | 97 / 36.89 / 29 |
| Arrow | 795 | 9.2% | 21.02 | 91 | 8.8% | 8.74 | 656 / 22.83 / 81 |
| Bolt | 208 | 2.4% | 34.62 | 36 | 3.5% | 5.78 | 213 / 34.30 / 33 |
| Cartridge | 18 | 0.2% | 61.39 | 10 | 1.0% | 1.80 | 20 / 81.05 / 11 |
| Javelin | 10 | 0.1% | 66.00 | 3 | 0.3% | 3.33 | 11 / 58.73 / 5 |
| Unarmed | 168 | 1.9% | 4.30 | 5 | 0.5% | 33.60 | 141 / 4.04 / 3 |

One-handed swords produce 52.4% of hits and 40.1% of kill flags; two-handed polearms produce 29.7% of hits and 40.4% of flags. Combined they account for 82.1% of hits. Polearms have fewer hits than siege 10 (2,561 versus 2,868) and lower total mean (18.18 versus 20.73); swords have more hits and a higher total mean (10.84 versus 9.99). These totals mix materials and blows.

For a closer comparison, each cell below is **old count→latest count; old mean→latest mean**, retaining all blows within the stated weapon class and material. An empty cell means no corresponding latest/baseline sample. These are observed matching categories, not matched attackers, victims, exact weapons or strike conditions.

| Class | Cloth | Padded | Mail | Brigandine | Plate |
| --- | --- | --- | --- | --- | --- |
| OneHandedSword | 529→597; 35.16→37.83 | 205→184; 21.11→26.08 | 239→206; 16.50→17.19 | 159→116; 17.21→17.72 | 2969→3422; 3.83→4.70 |
| OneHandedAxe | 29→44; 28.41→30.82 | 29→14; 18.45→20.07 | 11→12; 11.64→11.42 | 11→17; 8.00→11.12 | 135→166; 9.37→3.10 |
| TwoHandedPolearm | 569→515; 37.74→37.75 | 261→246; 25.07→26.10 | 151→159; 18.03→17.69 | 212→207; 18.58→18.75 | 1675→1434; 14.80→9.76 |
| Mace | 23→22; 49.96→50.50 | 7→15; 39.00→35.87 | 9→7; 27.44→35.71 | 5→6; 20.80→30.67 | 53→48; 34.06→33.77 |
| Arrow | 164→174; 33.33→34.20 | 69→91; 23.52→23.11 | 63→61; 17.75→18.85 | 52→71; 15.40→16.34 | 308→398; 19.37→15.95 |
| Bolt | 61→58; 40.98→41.10 | 24→29; 31.50→33.38 | 17→7; 29.59→25.43 | 22→24; 22.32→23.79 | 89→90; 34.35→34.44 |
| Cartridge | 6→7; 75.50→69.43 | 3→2; 70.33→51.00 | 2→1; 47.00→30.00 | 2→2; 65.00→36.50 | 7→6; 104.71→69.00 |
| Javelin | — | — | 1→3; 70.00→49.00 | — | 3→7; 69.33→73.29 |
| Unarmed | 35→53; 6.74→6.83 | 22→18; 3.54→3.78 | 26→7; 3.65→4.00 | 15→15; 3.33→3.33 | 43→75; 2.58→2.85 |

## Plate cuts: swords preserved, axes/polearms pay the chosen cost

This isolates `material=Plate`, `blow=Cut`, so it avoids mixing polearm piercing/blunt attacks with its cuts.

| Class | Old n | Old mean | Latest n | Latest mean | Latest median / max | Old→latest kill flags | Old→latest hits/flag |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OneHandedSword | 2,239 | 3.03 | 2,549 | 3.54 | 3.00 / 13.00 | 64→90 | 34.98→28.32 |
| OneHandedAxe | 134 | 9.22 | 154 | 2.18 | 2.00 / 6.00 | 6→3 | 22.33→51.33 |
| TwoHandedPolearm | 1,038 | 15.17 | 740 | 5.71 | 5.00 / 18.00 | 146→32 | 7.11→23.12 |
| TwoHandedSword | 3 | 11.00 | 0 | — | — | 0→0 | — |

One-handed sword mean increases **17.1%**, from 3.03 to 3.54. This stays in the low-single-digit damage range selected by the user, but it is not exact preservation: the latest cut sample has greater reconstructed raw (61.02 versus 53.17), slightly higher skill (96.54 versus 93.44), and more head hits (85.4% versus 82.5%), with similar mean base armour (42.35 versus 42.55). Its maximum falls 26→13 and median rises 2→3. None of this supports the earlier mistaken unanchored estimate that old sword damage was much larger.

Axes fall **76.3%**, 9.22→2.18, close to the earlier expectation of about a three-quarter reduction. Polearm cuts fall **62.4%**, 15.17→5.71, less than the pooled refit's estimated 75% loss. Latest polearm plate cuts have far more head hits (86.1% versus 70.6%), higher reconstructed raw (78.05 versus 60.70), higher skill (113.55 versus 105.38), and lower base armour (42.55 versus 45.65). Their more favourable hit mix can account for some of this difference; a precise causal split is unavailable. The observed reduction is still large and is the accepted shared-absorption compromise, not evidence that the new fraction failed to load.

Earlier **pooled battle 9 + siege 10** observations and damage-anchored refit estimates were: one-handed sword 2.75 old / 2.76 estimated at .80 (n=5,568), two-handed sword 8.95 / 7.91 (n=58), one-handed axe 10.92 / 2.52 (n=275), polearm cut 16.62 / 4.18 (n=4,894). Those estimates reuse old hit conditions; the latest independent siege changes those conditions. The estimates are not new observations and should not be compared to the latest values as though they were exact replay predictions. There is no current two-handed-sword evidence at all; siege 10 itself had only three such plate cuts.

## Thrusts behind the point

The log records 2,564 non-missile thrust-flagged contacts: **378 `tip=False`** and **2,186 `tip=True`**. Non-tip contacts average 2.68 damage (median 2, max 24), with seven recorded kill flags; siege 10 had 365, mean 2.93, two flags. Tip-true contacts average 15.60 versus 15.78 old. These gross groups include unarmed contacts, which do not demonstrate a weapon-thrust penalty; weapon-only slices follow.

| Class / material | Non-tip n / mean / flags | Tip-true n / mean / flags | Old non-tip n / mean |
| --- | --- | --- | --- |
| OneHandedSword / Cloth | 22 / 2.73 / 0 | 156 / 27.55 / 45 | 20 / 3.20 |
| OneHandedSword / Padded | 6 / 2.17 / 0 | 41 / 19.39 / 10 | 11 / 1.54 |
| OneHandedSword / Mail | 8 / 1.25 / 0 | 59 / 11.53 / 6 | 11 / 1.36 |
| OneHandedSword / Brigandine | 3 / 1.33 / 0 | 36 / 12.61 / 4 | 3 / 1.33 |
| OneHandedSword / Plate | 35 / 1.17 / 0 | 832 / 8.40 / 69 | 30 / 1.00 |
| TwoHandedPolearm / Cloth | 47 / 7.34 / 2 | 234 / 36.26 / 83 | 52 / 7.27 |
| TwoHandedPolearm / Padded | 8 / 3.25 / 0 | 129 / 24.29 / 33 | 8 / 3.00 |
| TwoHandedPolearm / Mail | 4 / 2.00 / 0 | 64 / 17.16 / 8 | 9 / 3.33 |
| TwoHandedPolearm / Brigandine | 5 / 2.60 / 0 | 118 / 16.28 / 20 | 7 / 2.71 |
| TwoHandedPolearm / Plate | 229 / 2.07 / 5 | 376 / 14.90 / 53 | 204 / 2.27 |

There are 74 sword non-tip contacts (zero flags) and 293 polearm non-tip contacts (seven flags), plus 11 unarmed non-tip contacts. Plate sword non-tip mean is 1.17 versus 8.40 for tip-true sword thrusts; plate polearm non-tip is 2.07 versus 14.90 tip-true. The strong reduction remains visible. This is observational evidence of low non-tip damage, not a direct verification of the per-template multiplier: polearm class combines pikes and other templates, and the log does not include crafting-template IDs or original magnitudes. Existing live XML retains pike .30 and lance .45 replacements for vanilla's .15; no lance-class hit occurs in this run.

## Firearms: 18 hits, too few for a balance conclusion

All 18 `Cartridge` hits classify as `Firearm`, use `absorbed=0.00`, and record skill=0. These are ammunition/current-usage skill values and should not be read as proof every shooter lacks firearm skill. Mean damage is **61.39** versus **81.05** old (20 hits), −24.3%; flags are 10 versus 11. The unchanged-looking 1.80 versus 1.82 hit/flag ratio is particularly uninformative at this sample size and with already-wounded victims.

| Material | Latest n | Mean / max | Kill flags | Old n / mean | Latest location mix |
| --- | --- | --- | --- | --- | --- |
| Cloth | 7 | 69.43 / 140.00 | 5 | 6 / 75.50 | Abdomen 2; Head 1; Legs 1; ShoulderRight 3 |
| Padded | 2 | 51.00 / 76.00 | 1 | 3 / 70.33 | ArmLeft 1; ShoulderRight 1 |
| Mail | 1 | 30.00 / 30.00 | 0 | 2 / 47.00 | ShoulderLeft 1 |
| Brigandine | 2 | 36.50 / 39.00 | 0 | 2 / 65.00 | ArmRight 1; ShoulderRight 1 |
| Plate | 6 | 69.00 / 97.00 | 4 | 7 / 104.71 | ArmLeft 1; Head 4; ShoulderRight 1 |

| Location | Latest n | Mean damage | Kill flags | Old n / mean |
| --- | --- | --- | --- | --- |
| Abdomen | 2 | 54.00 | 2 | 1 / 73.00 |
| ArmLeft | 2 | 59.50 | 2 | 1 / 34.00 |
| ArmRight | 1 | 39.00 | 0 | 1 / 65.00 |
| Head | 5 | 97.60 | 3 | 5 / 107.80 |
| Legs | 1 | 68.00 | 1 | — |
| ShoulderLeft | 1 | 30.00 | 0 | 5 / 65.00 |
| ShoulderRight | 6 | 42.17 | 2 | 3 / 61.00 |

Four of six plate firearm hits are head hits: damage **70, 87, 94, 97** (mean 87), two kill flags, base head armour 31–38. The other two plate hits are an arm hit for 43 at armour 24 and a shoulder hit for 23 at armour 72; both carry kill flags, showing why flags are not full-health lethality. The 23-damage heavy-plate hit is compatible with full armour still protecting against firearm damage. The cloth headshot deals 140 (armour 14); cloth's overall mean therefore mixes a very different location sample.

The new data is directionally consistent with the earlier inferred firearm loss from restoring full armour (estimated roughly −12% cloth, −17% padded, −30% mail/brigandine, −33% plate in pooled old hit conditions). It cannot validate those percentages: material cells contain **1–7 hits**, and even the head/non-head mixes differ. No new tuning conclusion is warranted from these 18 observations.

## Cannonballs kept separate

All 60 Boulder hits are Blunt and use the matching material's current blunt absorption. They average **104.40 damage**, median 112, maximum 184, total damage 6,264, and 45 recorded kill flags (1.33 hits/flag). Siege 10 had 52 hits, 36 flags, mean 105.81, total 5,502. Latest cannonballs contribute just **0.69% of all hits**, but **4.15% of all flags** and **4.66% of total damage**. Including them would distort firearm/weapon and material comparisons.

| Struck material | Boulder hits | Mean | Kill flags | Mean logged base armour |
| --- | --- | --- | --- | --- |
| Cloth | 20 | 109.40 | 19 | 4.15 |
| Padded | 8 | 117.38 | 7 | 5.75 |
| Mail | 1 | 17.00 | 0 | 0.00 |
| Brigandine | 13 | 109.54 | 10 | 1.15 |
| Plate | 18 | 94.22 | 9 | 23.72 |

Several cannon hits report nearly zero base armour despite a material such as Brigandine (mean armour 1.15); the single Mail hit has armour 0. The sample is 57 non-head hits versus three head hits. These projectile/impact armour readings and reconstructed raw values should not be used to fit ordinary melee armour effectiveness. The table reports what was logged, without assuming cannon damage follows the same practical conditions as hand weapons.

## Anomalies and evidence limits

- **36 zero-damage hits**, all TwoHandedPolearm with reconstructed raw=0; 35 Cut and one Blunt. Three have hp=0 (two Cloth cuts, one Padded cut) and therefore appear in both summary kill tallies. This is direct evidence that a recorded flag does not prove that logged damage caused a distinct death. No divide-by-zero or positive-raw/zero-damage hit occurs here.
- **135 zero-base-armour personal hits**, all Cloth: 83 Cut, 48 Pierce, four Blunt. Mean 34.17 damage, 34 kill flags; the material's absorption still logs normally. These should remain in observational totals, but they are not evidence of plate penetration or of resistance. Rounded zero armour is not the same thing as a complete naked-victim equipment record.
- **174 personal `T?` hits**: 168 Unarmed, three `ddg_bolt_c`, two `bundle_of_arrows`, one `linen_quiver`. Only six are armed ammunition fallback IDs, with zero kill flags. `WeaponOf` deliberately falls back to ammunition when the shooter cannot supply the matching active weapon, including dead shooters or switched weapons; these few records are not proof of six missing launcher tier rows. Cannon ammunition is separately unlisted and excluded from that personal count.
- Missile `at=NaN` is an unavailable collision-distance-on-weapon value, not a parser failure. No exact physical contact position is inferred from that field; landed damage remains usable. `by=` cannot recover missing victim identity.
- No Error/Fatal/Exception record appears from the latest mission setup through its final summary. The twelve warnings at lines **96,545–96,556**, `11:25:08`, are cannon-spawner prefab-attempt messages before combat; cannon impacts occur subsequently. No crash is shown at this mission end. Informational `town_order_*` tier fallbacks occur during prior startup and are not hit records.

## What this run establishes

1. The new material/blow absorption fractions are observed consistently in a completed siege; every hit and both summary tables reconcile. Source formatting and current armour forwarding are consistent with the removed resistance/sword override.
2. Low sword-on-plate cut damage survives. Axe/polearm plate cuts lose substantial damage as the user selected; the exact measured change depends on the new hit mix. Two-handed swords remain untested in this run.
3. Plate's aggregate descriptive hit/flag ratio rises; non-tip thrusts remain low damage. The data cannot isolate model causality, unique victims, true time-to-kill, buckler durability or victory/capture outcomes.
4. Firearm armour protection is present with zero extra absorption, but 18 hits are insufficient to validate a material balance or prior counterfactual percentages. Cannon observations remain separate.

Related: [[dadg-combat-absorption-refit]], [[dadg-combat-overhaul]], [[dadg-combat-open-work]], [[dadg-combat-rules-tuning]].
