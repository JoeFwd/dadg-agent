---
name: dadg-combat-cut-trial-siege-2026-11-08
description: Completed 12:53 cut-progression trial siege compared with the frozen 11:44 baseline; 7673 hits reconcile, all runtime fractions match, observed material means progress and plate cuts become more lethal
type: reference
topic: feature-combat
tags: [combat, siege, absorption, balance, logs, playtest]
sources: [DellarteDellaGuerra.Core/log/dadg.log, latest-siege-analysis/latest-hit-lines.log, dadg-combat-cut-progression-trial, CombatBalanceMissionLogic.cs]
updated: 2026-11-08
---

# Cut-progression trial: siege completed at 12:53

The trial ran with the intended **cut absorption 0 / .05 / .15 / .25 / .40** for Cloth/Padded/Mail/Brigandine/Plate, and unchanged pierce/blunt/firearm fractions. All **7,673 hits** parse and reconcile with both mission-end tables. Excluding 47 cannonballs leaves **7,626 personal hits and 1,166 recorded kill flags**.

The observed mean-damage progression is now **Cloth 38.16 > Padded 25.05 > Mail 16.99 > Brigandine 14.52 > Plate 12.83** across all personal blows, and **45.67 > 29.70 > 15.77 > 13.79 > 11.98** for cuts alone. Plate remains the lowest mean-damage material, while plate cuts cause substantially more finishing flags: one-handed swords average **10.57**, axes **6.45**, polearm cuts **16.15**. Their approximately threefold increase is closely explained by changing plate's retained damage from .20 to .60.

This establishes the intended direction in a live siege, not a controlled whole-soldier durability ladder. Victim identity is absent, materials describe hit locations, and a kill flag only means post-hit HP below one. The descriptive hit/flag ratio is **9.04 on plate versus 9.90 on brigandine**, so those ratios do not form a strict final-step progression. No setting is refitted or changed by this analysis.

## Fixed sources and mission boundary

Appended source: `D:/SteamLibrary/steamapps/common/Mount & Blade II Bannerlord/Modules/DellarteDellaGuerra.Core/log/dadg.log` (`../log/dadg.log` from Core `src`). Snapshot **40,400,352 bytes / 116,909 lines**; SHA-256 **`617c28d43c1e9b48f1564685d8c53e32a2551ada48a0ff7fdc97365944b9fd00`**. Internal timestamps determine recency.

- **107,313**, `2026-11-08 12:32:23`, `[siege-ai t=0.1]`: three assault lanes, left/right ladders and towers, middle battering ram, closed outer/inner gates. **107,314**, `12:32:26`, `t=0.6`: deployed formations using siege machines; middle lane becomes unusable with no machine. These are positive siege-assault evidence; no named settlement/scene ID is claimed.
- **107,316–115,963**: first/last body-hit records, **12:32:33–12:53:05**, combat **t=7.0–1107.6** (1,100.6 seconds / 18m20.6s of hit activity). The 8,648-line interval contains 7,673 hit lines and interspersed diagnostics. All hits in the appended segment belong to this completed block.
- **115,965**, `12:53:09`, final siege diagnostic **t=1111.7**: attackers inside, both gates open but not destroyed, assault-wall formations. **115,966–116,351**: 386 weapon-summary rows; **116,352–116,909**: 558 armour-summary rows, ending **12:53:13**. `OnEndMission` emits these summaries. Mission completion is evidenced; victory or settlement capture is not established by these records.
- A preceding setup begins at **107,286**, `12:30:05`, `t=0.1`, before a second clock reset at 107,313. No combat hit occurs in that earlier setup. The final analysis bounds the completed hit/summary block above rather than pooling all setup records or all historical summaries. Wall-clock elapsed time includes pauses/setup and is not simulation duration.

Frozen comparator: Core `src/.tmp/latest-siege-analysis/latest-hit-lines.log`, **8,696 hits / 8,636 personal hits**, siege ending **11:44:13**. Its SHA-256 is **`729568de664948402c7f9881581eda0d488c339ea1aa2a33d0cf76d3881a2c0f`**; the full original log snapshot's hash was `5de65ac666b0c6e3721e142e20cdd52b0bfdb05502556bf6a8f4948efef6f209`. The frozen source and `results.json` were read without modification. This comparison uses that immediate absorption-only baseline, not the older resistance/sword-override siege 10.

New reproducibility files are isolated under Core `src/.tmp/cut-trial-siege-analysis/`: `prepare.py`, `analyse.py`, `extra.py`, `results.json`, `extra-results.json`, `latest-hit-lines.log`, `inspect.py`, and `write_note.py`. The adapted parser hard-bounds hit lines 107316–115963 and summary scanning through 116909. It independently reconciles **every** summary key's hit count, kill count, maximum and displayed mean (0.1 precision): **386/386 weapon rows and 558/558 armour rows, zero discrepancies**, each table totalling **7,673 hits / 1,199 flags** including cannonballs. No game, XML, code or existing note was modified; no build/test was run.

## Runtime fractions, not merely the current XML

Each cell is **observed fraction (hit count)**. Cannonballs are included here in Blunt. Each material/blow cell contains exactly one fraction, with no mixed baseline/trial values.

| Material | Cut | Pierce | Blunt | Firearm |
| --- | --- | --- | --- | --- |
| Cloth | 0.00 (565) | 0.03 (637) | 0.03 (106) | 0.00 (9) |
| Padded | 0.05 (208) | 0.02 (349) | 0.10 (38) | 0.00 (7) |
| Mail | 0.15 (187) | 0.00 (226) | 0.11 (29) | 0.00 (4) |
| Brigandine | 0.25 (174) | 0.03 (288) | 0.10 (46) | 0.00 (3) |
| Plate | 0.40 (2,586) | 0.18 (1,972) | 0.16 (224) | 0.00 (15) |

All 20 observed cells match the intended trial. There are **zero `effective=` fields** in 7,673 hit records. This continues the absorption-only implementation: native armour handling is retained and firearms have zero additional absorption, not armour bypass. Current XML alone would not prove that the running mission loaded the trial; the per-hit fractions do.

The baseline cut fractions were .05/.10/.09/.07/.80. Thus the retained-damage factors for identical hit conditions are **1/.95, .95/.90, .85/.91, .75/.93 and .60/.20**, respectively. Pierce, blunt, firearm, half-sword and non-tip settings were intended to remain unchanged. The available per-hit fields directly verify absorption; they do not independently expose original strike magnitude or every internal modifier.

## Personal hits: totals and observed progression

All remaining comparisons exclude `WeaponClass=Boulder` on both sides; they include unarmed contacts and zero damage. “Flags” means the logger's `affectedAgent.Health < 1` after a hit. “Hits/flag” is descriptive, **not true hits-to-kill, unique kills or time-to-kill**. Displayed HP<1 reproduces all summary flags in this snapshot, but missing victim IDs prevent reconstructing deaths or repeated hits on the same soldier.

| Metric | Frozen 11:44 | Trial 12:53 |
| --- | --- | --- |
| Personal hits | 8,636 | 7,626 |
| Recorded flags | 1,039 | 1,166 |
| Mean damage | 14.84 | 18.47 |
| Median damage | 7.00 | 13.00 |
| Total logged damage | 128,187 | 140,827 |
| Hits/flag | 8.31 | 6.54 |
| Head-hit share % | 51.54 | 45.66 |

Mean personal damage rises **24.4%**, median 7→13, despite **11.7% fewer hits**. Total logged damage rises 9.9%, flags rise 12.2%, and hits/flag falls 21.3% (8.31→6.54). The trial lasts longer in simulation than the baseline; counts and ratios cannot isolate the rules from changes in battle flow or surviving forces.

| Material | Trial n / hit share | Baseline→trial mean | Trial median | Baseline→trial flags | Baseline→trial hits/flag | Old-mix estimate |
| --- | --- | --- | --- | --- | --- | --- |
| Cloth | 1,305 / 17.1% | 36.51→38.16 | 36.00 | 429→404 | 3.43→3.23 | 37.51 |
| Padded | 593 / 7.8% | 25.51→25.05 | 23.00 | 131→119 | 4.57→4.98 | 26.15 |
| Mail | 443 / 5.8% | 17.87→16.99 | 15.00 | 60→63 | 7.72→7.03 | 17.24 |
| Brigandine | 505 / 6.6% | 17.82→14.52 | 12.00 | 67→51 | 6.84→9.90 | 16.33 |
| Plate | 4,780 / 62.7% | 7.58→12.83 | 9.00 | 352→529 | 16.04→9.04 | 12.40 |

The saved old-mix estimates (37.51/26.15/17.24/16.33/12.40) were rescalings of previous observations, not targets or exact predictions for a different battle. New means broadly show the intended order; brigandine is lower than its old-mix estimate because its incoming cut and pierce samples also weaken. Padded's all-blow mean falls slightly even though its cut fraction was reduced, illustrating how aggregate mix can obscure the direct scalar effect.

Sampling remains skewed. Plate is **62.7%** of personal hits (baseline 65.4%); Cloth 17.1%, Padded 7.8%, Mail 5.8%, Brigandine 6.6%. **68.3% of plate hits are `Head`** versus 16.6% of cloth; Padded/Mail/Brigandine have zero `Head` hits. This run also contains `Neck` records, which should not be silently counted as `Head`. The combined head/neck percentages and exact struck-location comparisons are used where relevant below. Materials are per struck location, not per troop loadout.

## Cuts alone and scalar-normalized comparison

`U = inflictedDamage / (1 - loggedAbsorption)` approximately removes the final material absorption from an observed hit. It preserves all other differences (weapon, location, armour, native perks, skill, hit geometry, integer rounding). Therefore comparing U helps distinguish the changed fraction from the changed sample, but is not a replay of original magnitudes or a matched-victim experiment.

| Material | Baseline→trial cut n | Baseline→trial mean | Trial median / max | Baseline→trial flags | Baseline→trial hits/flag | Baseline→trial U / change |
| --- | --- | --- | --- | --- | --- | --- |
| Cloth | 648→565 | 43.02→45.67 | 45.00 / 125.00 | 214→221 | 3.03→2.56 | 45.28→45.67 / +0.9% |
| Padded | 242→208 | 28.77→29.70 | 27.50 / 94.00 | 56→55 | 4.32→3.78 | 31.97→31.26 / -2.2% |
| Mail | 230→187 | 19.12→15.77 | 12.00 / 65.00 | 32→28 | 7.19→6.68 | 21.01→18.55 / -11.7% |
| Brigandine | 172→174 | 20.58→13.79 | 11.00 / 56.00 | 31→17 | 5.55→10.24 | 22.13→18.38 / -16.9% |
| Plate | 3443→2586 | 3.95→11.98 | 9.00 / 52.00 | 125→293 | 27.54→8.83 | 19.74→19.97 / +1.2% |

Cloth/Padded changes closely track their mild scalar changes after mix effects. Mail and brigandine cuts fall more than the fraction alone predicts: **U falls 11.7% and 16.9%**, respectively, while mean cut base armour is nearly unchanged (Mail 31.04→31.33; Brigandine 33.70→33.90). Their reconstructed raw also falls (Mail 47.42→44.36; Brigandine 53.80→48.04). Those observations support weaker incoming samples as an additional cause; reconstructed raw remains a rounded diagnostic, not strike magnitude.

Plate mean cut damage rises **3.04×**, 3.95→11.98, while U rises just **1.2%**, 19.74→19.97, and mean cut base armour is virtually identical (42.32→42.33). The increase is overwhelmingly consistent with the selected .80→.40 fraction change. The aggregate normalized plate increase coexists with slight declines inside its main weapon classes because polearm cuts now form a larger share of plate cuts (27.8% versus 21.5%).

Same material, same blow type across both runs (all personal hits):

| Material | Cut old→trial (trial n) | Pierce old→trial (trial n) | Blunt old→trial (trial n) | Firearm old→trial (trial n) |
| --- | --- | --- | --- | --- |
| Cloth | 43.02→45.67 (565) | 31.29→31.43 (637) | 29.80→35.35 (94) | 69.43→72.22 (9) |
| Padded | 28.77→29.70 (208) | 23.24→22.23 (349) | 22.52→21.45 (29) | 51.00→42.57 (7) |
| Mail | 19.12→15.77 (187) | 15.88→17.62 (226) | 22.11→18.39 (26) | 30.00→29.25 (4) |
| Brigandine | 20.58→13.79 (174) | 16.01→14.07 (288) | 16.15→18.80 (40) | 36.50→43.33 (3) |
| Plate | 3.95→11.98 (2586) | 11.77→12.35 (1972) | 24.92→26.02 (207) | 69.00→38.93 (15) |

Unchanged fractions still produce changed observations: plate pierce 11.77→12.35, plate blunt 24.92→26.02, mail pierce 15.88→17.62, brigandine pierce 16.01→14.07. Plate-pierce mean base armour is stable (46.26→46.24), raw rises 42.19→43.80 and Head share falls 57.9%→52.1%; plate blunt armour is similarly stable (39.86→39.96), raw rises 56.42→58.08. Brigandine-pierce armour rises 39.26→40.27 while raw falls 41.50→37.02. These are sampling/conditions changes under the same fractions, so not every observed change should be assigned to cut tuning.

## Plate cuts by weapon: more lethal finishing hits, protection retained

| Plate Cut class | Baseline→trial n | Baseline→trial mean | Trial median / max | Baseline→trial flags | Baseline→trial hits/flag | Baseline→trial U |
| --- | --- | --- | --- | --- | --- | --- |
| OneHandedSword | 2549→1761 | 3.54→10.57 | 8.00 / 38.00 | 90→188 | 28.32→9.37 | 17.72→17.62 |
| OneHandedAxe | 154→104 | 2.18→6.45 | 6.00 / 20.00 | 3→7 | 51.33→14.86 | 10.91→10.75 |
| TwoHandedPolearm | 740→719 | 5.71→16.15 | 13.00 / 52.00 | 32→98 | 23.12→7.34 | 28.53→26.91 |
| TwoHandedSword | 0→2 | —→42.50 | 42.50 / 44.00 | 0→0 | — | —→70.83 |

The saved old-mix estimates were sword **10.63**, axe **6.55**, polearm cut **17.12**. Observed trial means are **10.57 / 6.45 / 16.15** (−0.5% / −1.5% / −5.7% relative to those estimates). These agree closely in direction and scale with the intended threefold retained-damage increase; the residuals are not evidence of a different fraction loading.

Sword flag incidence rises **3.5%→10.7%**, axe **1.9%→6.7%**, polearm cut **4.3%→13.6%**. Those are finishing/post-hit-dead flags, not one-hit-kill rates. **No plate cut reaches 100 damage**: maxima are 38 sword, 20 axe, 52 polearm; the two two-handed sword cuts deal 41 and 44. Thus the log shows more lethal finishing cuts while still showing substantial plate protection against a single blow. The two two-handed sword hits, both Head, cannot establish that class's balance.

Hit conditions for the three adequately sampled plate-cut classes:

| Class | Base armour old→trial | Raw old→trial | Skill old→trial | Head % old→trial | U change |
| --- | --- | --- | --- | --- | --- |
| OneHandedSword | 42.35→41.81 | 61.02→57.00 | 96.54→96.11 | 85.41→82.00 | -0.5% |
| OneHandedAxe | 40.66→42.46 | 44.68→44.85 | 83.12→82.21 | 72.73→74.04 | -1.4% |
| TwoHandedPolearm | 42.55→43.61 | 78.05→73.30 | 113.55→110.93 | 86.08→75.38 | -5.7% |

Polearm cuts shift away from Head more than the other classes and strike slightly higher base armour; this helps explain their lower normalized result. Native perks, victim/attacker selection and contact geometry remain unmeasured confounders. The logger's skill and reconstructed raw are diagnostics, not an exact causal model.

Location matters more than the pooled class mean: trial one-handed sword plate-Head cuts average **11.96** (n=1,444), plate-Chest **2.30** (n=20), shoulder-left/right **2.86/2.23** (n=102/61), and Neck **7.22** (n=45). Polearm plate-Head cuts average **20.08** (n=542), Chest **2.45** (n=11), shoulder-left/right **3.77/3.02** (n=53/42), Neck **15.25** (n=8). Head/Neck and body samples should not be treated as identical plate coverage. There is no per-victim reconstruction of whether these hits overcame one complete armour kit.

## Weapon mix, maces and non-tip contacts

| Class | Baseline→trial hits | Trial hit share | Baseline→trial mean | Baseline→trial flags |
| --- | --- | --- | --- | --- |
| Arrow | 795→1555 | 20.4% | 21.02→17.10 | 91→181 |
| Bolt | 208→227 | 3.0% | 34.62→31.99 | 36→32 |
| Cartridge | 18→38 | 0.5% | 61.39→46.82 | 10→9 |
| Javelin | 10→2 | 0.0% | 66.00→49.00 | 3→1 |
| Mace | 98→113 | 1.5% | 37.80→39.06 | 33→43 |
| OneHandedAxe | 253→177 | 2.3% | 9.79→14.07 | 24→24 |
| OneHandedSword | 4525→3171 | 41.6% | 10.84→16.11 | 417→481 |
| TwoHandedPolearm | 2561→2200 | 28.8% | 18.18→20.83 | 420→386 |
| TwoHandedSword | 0→12 | 0.2% | —→71.92 | 0→5 |
| Unarmed | 168→131 | 1.7% | 4.30→3.31 | 5→4 |

Sword hit share falls **52.4%→41.6%**, polearms **29.7%→28.8%**, and Arrow rises **9.2%→20.4%**. This is a meaningfully different fight: the middle battering-ram lane was initially unusable, gates ultimately opened intact, and the simulation lasted longer. Those facts do not isolate why the weapon mix changed, but they rule out treating it as an identical replay with one scalar changed.

Maces retain unchanged blunt fractions. They average **39.06** damage over 113 hits / 43 flags (baseline 37.80, 98 / 33). Against plate, mace mean is **37.93** (n=57, 22 flags), previously 33.77 (n=48, 14 flags); **94.7%** of new mace plate hits are Head, versus 91.7% before, with raw rising 74.90→83.67. The observed mace advantage over cuts remains, but is heavily selected toward helmet hits and cannot be reduced to a class-only multiplier comparison.

Non-tip (`tip=False`) contacts remain weak: **354**, mean **2.71**, median 2, max 22, nine flags; baseline 378, mean 2.68, seven flags. These include seven unarmed contacts; weapon-only counts are **52 sword / 295 polearm**. Plate non-tip sword mean **1.08** (n=24, one flag), polearm **2.14** (n=248, seven flags), versus **1.17/2.07** before. Low non-tip damage persists; the log does not expose template IDs/original magnitudes and cannot directly verify every per-template penalty.

## Firearms and cannonballs

Firearm fractions are unchanged at zero in all materials. There are **38 hits / nine flags**, mean **46.82**, median 42.5, max 224; baseline 18 / ten, mean 61.39. This independent sample is still sparse and its mean/flag changes cannot be caused by the cut-absorption scalar itself. Current-usage ammunition skill logs as zero, which is not proof every shooter has zero firearm skill.

| Material | Baseline→trial firearm n | Baseline→trial mean | Trial flags | Trial locations |
| --- | --- | --- | --- | --- |
| Cloth | 7→9 | 69.43→72.22 | 5 | Abdomen 1; Chest 2; Head 1; ShoulderLeft 2; ShoulderRight 3 |
| Padded | 2→7 | 51.00→42.57 | 2 | ArmRight 1; Chest 2; ShoulderLeft 1; ShoulderRight 3 |
| Mail | 1→4 | 30.00→29.25 | 0 | ArmLeft 1; ArmRight 1; ShoulderLeft 1; ShoulderRight 1 |
| Brigandine | 2→3 | 36.50→43.33 | 0 | Abdomen 1; ArmRight 2 |
| Plate | 6→15 | 69.00→38.93 | 2 | Chest 1; Head 5; Neck 4; ShoulderLeft 1; ShoulderRight 4 |

Plate firearm mean falls 69.00→38.93, but Head share changes 66.7%→33.3%, raw 145.83→91.07, and base armour 39.17→46.40. Five plate Head hits average **47.40** (range 40–63); four Neck hits **59.00** (44–96); six remaining plate body hits average **18.50**, zero flags. The two plate firearm flags occur in one Head and one Neck contact. Full armour protection is compatible with these observations, but material cells of 3–15 hits do not support a new firearm tuning conclusion. The **224-damage cloth Head hit has armour 0** and disproportionately raises the small cloth sample mean; it is not a plate-penetration anomaly.

Cannonballs are **47 Boulder / Blunt hits**, 33 flags, mean **92.28**, median 110, max 124, total 4,337 (baseline 60 / 45, mean 104.40). They contribute 0.61% of all hits, 2.75% of all flags and 2.99% of logged damage. All are non-Head, with mean logged base armour only **6.83**. Cannon material/body/impact conditions differ from ordinary weapons; they remain excluded from material, firearm and personal-weapon conclusions.

## Anomalies, warnings and limits

- **29 zero-damage hits**, all polearm, all reconstructed raw=0. One carries a kill flag: source line **110,144**, `12:40:12`, `t=334.8`, `ddg_poleaxe_poleaxea`, Cloth Head, `damage=0 hp=0`. This directly demonstrates why flags are not verified causal kills. Both summary tables retain that flag. Baseline had 36 zero-damage hits / three such flags.
- **120 zero-base-armour personal hits**, all Cloth, mean 44.22, 41 flags. They remain in totals; the 224-damage unarmoured firearm Head hit is included. Rounded base armour and reconstructed raw do not provide an exact record of native final armour/perks.
- **140 personal `T?` hits**: 131 Unarmed plus nine ammunition fallback records (one bundle_of_arrows, two linen_quiver, one ddg_bolt_b, five ddg_bolt_c). These have one armed fallback flag. The logger intentionally uses ammunition when it cannot recover a matching wielded launcher (for example a dead/switched shooter), so this alone is not evidence of missing launcher tier rules. Cannon ammunition is separate.
- Missile `at=NaN` is unavailable collision-distance-on-weapon data, not a parser failure. Missing victim IDs prevent unique kills, armour-kit survival curves, healing/death reconstruction or actual time-to-kill. Head and Neck are distinct labels in this run.
- No Error/Fatal/Exception is recorded in the appended setup/combat/summary interval. **24 warnings** are cannon-prefab attempts: twelve at **107,274–107,285**, `12:29:58`, before the first setup, and twelve at **107,301–107,312**, `12:32:17`, before the completed mission's clock reset. Subsequent cannon hits and final summaries are present. Completion does not itself prove victory/capture.
- Combat-balance excludes shield blocks, shield-back collisions, charges and falls. **Buckler HP loading, damage and durability are not measured**, so this run does not validate the 250 HP change or quantify its effect on the new combat mix.

The result supports the requested gameplay direction: mean damage separates Cloth→Padded→Mail→Brigandine→Plate in both all-blow and cut-only samples, while plate cuts become meaningfully more lethal finishing blows. The loaded fractions and class-level scaling are verified; whole-victim durability, exact causal casualty changes and sparse two-handed-sword/firearm balance remain outside the evidence. No further setting change is inferred or proposed.

Related: [[dadg-combat-cut-progression-trial]], [[dadg-combat-latest-siege-2026-11-08]], [[dadg-combat-absorption-refit]], [[dadg-combat-open-work]].
