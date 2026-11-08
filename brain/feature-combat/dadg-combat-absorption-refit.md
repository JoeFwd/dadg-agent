---
name: dadg-combat-absorption-refit
description: Fit of battle 9 and siege 10 to absorption-only combat; logged fractions, damage-anchored estimates, the user-selected 80% plate cut rate and unavoidable weapon-class drift
type: decision
topic: feature-combat
tags: [combat, absorption, balance, logs]
sources: [battle9.log, siege10.log, 1.4.8 DefaultStrikeMagnitudeModel.ComputeRawDamage, MissionCombatMechanicsHelper.ComputeBlowDamage]
updated: 2026-11-08
---

# Absorption-only refit against the actual battle logs

The user asked to keep the previous combat balance after removing `Resistance` and `SwordOnPlate`, and to recalculate every material/blow value against the battlefield and siege logs. Firearms must still use full armour with no absorption. When shown the conflict between sword and axe/polearm cuts on plate, the user explicitly selected **keep swords close to their old damage (~80% absorption)**.

## Inputs and corrections

The logs are in `C:/Users/Joe/AppData/Local/Temp/claude/D--SteamLibrary-steamapps-common-Mount---Blade-II-Bannerlord-Modules-DellarteDellaGuerra-Core-src/530e0b87-9c92-4c0f-bc7b-09fb06c4e5b4/scratchpad/`.

| Input | Hit lines | SHA-256 |
|---|---:|---|
| `battle9.log` | 23,222 | `964c6a134a4667d31758e59573a87a752128c3d5220886d6377e65a0aae738a0` |
| `siege10.log` | 8,393 | `71e859717e2ea92eef461ea9cb556d9ec471c6e34d9d78cd9af25904293a9ede` |

All hit lines parsed. Exclude 52 Boulder cannonball hits from the siege, leaving **31,563 personal-weapon hits** (222 firearm, 31,341 other). Include sword overrides, zero-armour hits and kicks; do not silently drop them. There are 102 zero-damage hits, all with zero reconstructed raw damage.

The initial `merge_fit.py` deliberately excluded sword overrides and assumed later soft-armour values: cloth pierce/blunt .25, padded pierce/blunt .30. The actual logs used .05 on all cloth blows and .10 on all padded blows. Mail used .20, brigandine .25, plate .40; firearms used zero. This refit targets the damage recorded in those logs, rather than the subsequent soft-armour design change.

## Estimation method and limits

Let `F(M,A,b)` be vanilla damage before final absorption:

```
r = M * 50 / (50 + A)
F = bluntFactor * r + (1 - bluntFactor) * max(0, r - armourFactor * A)
```

Blunt factors: cut .10, pierce/firearm .25, blunt .60. Armour factors: cut .50, pierce/firearm .33, blunt .20. Confirmed through the 1.4.8 source-search tool.

For each hit, compute `oldModel = F(raw, effective, blow) * (1 - loggedAbsorption)` and `fullModel = F(raw, armour, blow)`. Estimate damage with full armour and no absorption as `observedDamage * fullModel / oldModel`. A zero model falls back to `fullModel` (all 102 such hits have raw and damage zero). This anchor reproduces observed damage when armour/absorption stay unchanged, and avoids treating the formula proxy's uncorrected output as observed damage.

The logged `raw` reconstructs damage before armour from final inflicted damage and `AbsorbedByArmor`; it is **not the original strike magnitude**. It includes body-part/scaling effects and integer rounding. Logged `effective` also omits actual perk adjustments, and base armour is rounded to an integer. Therefore changing armour through this formula ratio remains an approximation, not an exact replay. Counterfactual deaths, attack choices and battle outcomes are not simulated.

For each material/blow pair, fit `absorption = 1 - sum(observedDamage) / sum(estimatedFullDamage)`. Pool hits from both logs, round to .01, and clamp negative values to zero. Keep firearms zero regardless of the fitted rate. Plate cut uses the user-selected .80 instead of the pooled .46 compromise.

Reproduction files (untracked, do not commit): Core `src/.tmp/refit_absorption.py`, `.tmp/refit_absorption.json`, `.tmp/apply_absorption_refit.py`. Source files are read only. The analysis self-checks counts, rate ranges and the unchanged-armour identity.

## Values and samples

| Material | Cut | Pierce | Blunt | Cut / pierce / blunt samples |
|---|---:|---:|---:|---|
| Cloth | .05 | .03 | .03 | 1,496 / 2,837 / 182 |
| Padded | .10 | .02 | .10 | 771 / 1,824 / 102 |
| Mail | .09 | 0 | .11 | 833 / 1,204 / 138 |
| Brigandine | .07 | .03 | .10 | 939 / 1,603 / 134 |
| Plate | **.80** | .18 | .16 | 10,795 / 7,553 / 930 |

Firearm absorption remains zero for every material; the full armour value still applies. All rates are final-damage fractions on top of vanilla armour. Existing XML fields handle the change; no production-code modifier or DLL change is needed. Restart to reload XML.

Verification: all 15 live XML values match `ShippedCombatRules`; the XML parses with no obsolete rule rows; all **27 focused Domain combat tests pass** after replacing the superseded soft-armour ordering test with a valid absorption-range check. No new solution build was needed for XML/test-data changes. The refactor/rates/buckler change were subsequently committed as Core `b6a9392`, content `4f557546` and initial notes `a1d1a1a`. The siege ending 11:44:13 then supplied live observations under these absorption rates: [[dadg-combat-latest-siege-2026-11-08]].

## Plate cut cannot preserve every weapon with one scalar

| Weapon class | Hits | Observed old mean | Estimated mean at .80 | Class-specific fit |
|---|---:|---:|---:|---:|
| One-handed sword | 5,568 | 2.75 | 2.76 | .801 |
| Two-handed sword | 58 | 8.95 | 7.91 | .774 |
| One-handed axe | 275 | 10.92 | 2.52 | .134 |
| Two-handed polearm | 4,894 | 16.62 | 4.18 | .204 |

The shared .80 rate keeps one-handed swords close but reduces axe/polearm cuts by about 75–77%. The pooled .458 fit, rounded to .46, would preserve combined cut damage but make swords much stronger. Different weapon mixes mean that even .46 would change total cut damage by about -8.5% in the field and +25.9% in the siege. The user explicitly chose the sword-preserving option. Reintroducing weapon-specific modifiers was not requested.

Earlier estimates of 2.6/11.9 old sword damage and 8.6/41 after the initial merge came from the unanchored formula model. The actual logged means are 2.75/8.95; use the anchored table above for this refit.

## Remaining drift with the chosen rates

| Material/blow | Field damage change | Siege damage change |
|---|---:|---:|
| Cloth cut / pierce / blunt | 0% / -.4% / -.5% | 0% / -.5% / +.1% |
| Padded cut / pierce / blunt | 0% / +.4% / 0% | 0% / -1.1% / 0% |
| Mail cut / pierce / blunt | -.7% / -6.9% / 0% | +.5% / -17.3% / +.2% |
| Brigandine cut / pierce / blunt | -2.0% / +.3% / -.1% | +4.1% / -5.9% / -1.0% |
| Plate pierce / blunt | -1.7% / -2.3% | +8.3% / +5.4% |

Mail pierce fits a negative fraction (-.089 pooled): full vanilla armour alone already reduces damage more than the previous scaled armour plus absorption. Zero absorption is the closest setting without adding damage; pooled damage remains about 8.1% below the old logs. This is a limit of the requested simplified rules.

Firearm estimated changes remain intentional: roughly -12% cloth, -17% padded, -30% mail/brigandine, -33% plate, because their former armour reductions were removed. Firearm sample sizes are 91 / 37 / 12 / 25 / 57 respectively, so mail especially has limited evidence.

Related: [[dadg-combat-overhaul]], [[dadg-combat-open-work]], [[dadg-combat-rules-tuning]]
