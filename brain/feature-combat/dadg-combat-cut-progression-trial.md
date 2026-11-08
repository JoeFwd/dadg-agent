---
name: dadg-combat-cut-progression-trial
description: User-requested 0/5/15/25/40 percent cut absorption trial; saved pre-trial siege material table and rates, unchanged non-cut settings, projected damage and completed live siege verification
type: decision
topic: feature-combat
tags: [combat, absorption, tuning, trial, snapshot]
sources: [dadg-combat-latest-siege-2026-11-08, content commit 4f557546, user request 2026-11-08]
updated: 2026-11-08
---

# Cut absorption progression trial

The user asked to preserve the material comparison table, then try **Cloth/Padded/Mail/Brigandine/Plate cut absorption of 0/5/15/25/40%**, keeping every other setting unchanged. Applied to live content XML and `ShippedCombatRules`. This supersedes the previous 80% plate cut decision for the trial; do not silently restore the earlier sword-preserving rate.

## Snapshot before this trial

These are observed personal-weapon/missile/unarmed hits, excluding Boulder cannonballs. The first column is siege 10 under the former resistance rules. The second is the completed siege ending **2026-11-08 11:44:13** under absorption-only rules with 80% plate cut. This is a fixed baseline, not a table to overwrite after the next run.

| Material | Siege 10 mean damage | Pre-trial latest mean damage | Latest hits | Hits per recorded kill flag: siege 10 -> latest |
|---|---:|---:|---:|---|
| Cloth | 36.39 | 36.51 | 1,470 | 3.42 -> 3.43 |
| Padded | 23.22 | 25.51 | 599 | 5.14 -> 4.57 |
| Mail | 17.41 | 17.87 | 463 | 7.07 -> 7.72 |
| Brigandine | 17.45 | 17.82 | 458 | 7.35 -> 6.84 |
| Plate | 9.33 | 7.58 | 5,646 | 12.32 -> 16.04 |

The pre-trial siege has 8,636 personal hits and 1,039 recorded kill flags (8,696/1,084 including cannonballs). Its source snapshot SHA-256 is `5de65ac666b0c6e3721e142e20cdd52b0bfdb05502556bf6a8f4948efef6f209`, with hit records on source lines 96,562–106,041. Full source paths, reconciliation and observed fractions are in [[dadg-combat-latest-siege-2026-11-08]]. The baseline content is committed as `4f557546`; the analysis is in notes `68cae02`, recorded by Core `905178f`.

These material groups have different weapons, hit locations and victims. They do not isolate armour effectiveness. Recorded kill flags mean post-hit HP below 1, not verified unique or causal deaths; the descriptive ratios are not actual hits-to-kill.

## Trial settings and rollback values

| Material | Previous cut | Trial cut | Pierce (unchanged) | Blunt (unchanged) |
|---|---:|---:|---:|---:|
| Cloth | 5% | **0%** | 3% | 3% |
| Padded | 10% | **5%** | 2% | 10% |
| Mail | 9% | **15%** | 0% | 11% |
| Brigandine | 7% | **25%** | 3% | 10% |
| Plate | 80% | **40%** | 18% | 16% |

Only the five `cut` attributes changed in `DellarteDellaGuerra/ModuleData/CustomXml/dadg_combat_items.xml`. Item armour, weapon stats, HalfSword, NonTipThrust and buckler HP remain as before. Firearms continue to use full armour and zero absorption. To revert this trial, restore only the Previous cut column in the XML and test fixture; avoid restoring entire files over unrelated work.

## Estimated effects on the frozen pre-trial hit sample

Because only final cut absorption changes, rescale each observed cut as `oldDamage * (1 - trialCut) / (1 - oldCut)`. Other hits stay unchanged. This is an estimate: logged damage is rounded to integers, the underlying unrounded damage is unavailable, and changing lethality would alter later combat events. Do not predict new kills or battle duration from these rescaled hits.

| Material | Cut damage change | Cut mean: observed -> estimated | All-hit mean: observed -> estimated |
|---|---:|---|---|
| Cloth | +5.3% | 43.02 -> 45.28 | 36.51 -> 37.51 |
| Padded | +5.6% | 28.77 -> 30.37 | 25.51 -> 26.15 |
| Mail | -6.6% | 19.12 -> 17.86 | 17.87 -> 17.24 |
| Brigandine | -19.4% | 20.58 -> 16.60 | 17.82 -> 16.33 |
| Plate | **+200%** | 3.95 -> 11.84 | 7.58 -> 12.40 |

Reducing plate absorption from 80% to 40% lets 60% rather than 20% of post-armour cut damage through: three times the previous amount. On that same pre-trial sample, plate cut means by class would be:

| Class | Hits | Observed old mean | Estimated trial mean |
|---|---:|---:|---:|
| One-handed sword | 2,549 | 3.54 | 10.63 |
| One-handed axe | 154 | 2.18 | 6.55 |
| Two-handed polearm | 740 | 5.71 | 17.12 |

No two-handed sword hit exists in this sample, so there is no corresponding estimate. The progression makes extra cut absorption increase with material while retaining vanilla armour's separate protection. Mail and brigandine's observed cut damage also reflects different weapons and locations; their absolute averages need not rank perfectly in a live run.

## Verification and next measurement

All **27 focused Domain combat tests passed** at this trial stage. The prior every-material-positive-cut assertion was replaced with a strictly increasing cut-absorption check, since cloth now absorbs zero cuts. XML parsing and semantic comparison verified that only five cut attributes changed; all 15 fractions matched the test fixture. Non-cut damage is unchanged in the estimate. No game-code rebuild was required for this value-only trial; restart reloads rules.

**Live result:** the subsequent siege ending **2026-11-08 12:53:13** ran all the intended trial fractions. Its 7,673 hit records and both summary tables reconcile. Excluding cannonballs, mean damage is now Cloth 38.16, Padded 25.05, Mail 16.99, Brigandine 14.52, Plate 12.83. Plate cut means are sword 10.58, axe 6.45 and polearm 16.15. These are new observed results, not replacements for the frozen tables above. Full analysis and hit-mix qualifications: [[dadg-combat-cut-trial-siege-2026-11-08]].

Untracked reproduction files: Core `src/.tmp/set_cut_progression_trial.py`, `.tmp/cut-progression-trial/before.xml`, and `.tmp/cut-progression-trial/estimates.json`, using the frozen `.tmp/latest-siege-analysis/latest-hit-lines.log`. The baseline tables and rate values above remain durable if temporary files are removed.

For further sieges, continue checking logged cut fractions are exactly 0/.05/.15/.25/.40 and compare per material and weapon class with the frozen baseline. Keep cannonballs separate. Shield blocks are not recorded, so the hit logger cannot establish buckler durability.

Related: [[dadg-combat-overhaul]], [[dadg-combat-latest-siege-2026-11-08]], [[dadg-combat-absorption-refit]], [[dadg-combat-open-work]].

## Subsequent weapon-class rules

The user then requested low sword cuts on plate while retaining stronger polearm cuts. The defaults in the trial table are retained, now in nested XML. Plate Cut entries OneHandedSword .88, TwoHandedSword .94 and TwoHandedPolearm .52 replace the .40 Default for those classes. This corresponds to multiplying the trial's final cut damage by .20/.10/.80, without stacking a second reduction. Expected latest-siege class means are about 2.1/4.3/12.9; the two-handed sword estimate has only two baseline hits. Half-sword modes use the sword entry. Thirty-three combat tests, the actual nested C# parser check and Release build pass. These overrides require the matching DLL and XML and have not yet been playtested. The observed and estimated tables above remain unchanged snapshots of the earlier trial.
