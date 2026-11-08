---
name: dadg-combat-overhaul
description: Hub - DADG's native combat layer: per-location armour materials, absorption, half-sword/non-tip tweaks and a T1-T6 weapon tier table, all through model decorators with no Harmony patch
type: reference
topic: feature-combat
tags: [combat, armour, damage, models]
sources: [doc/combat-overhaul-analysis.md (retired 2026-11-07), Core commit c817ca2, content commit 41022715]
updated: 2026-11-08
---

# DADG combat overhaul

DADG keeps the vanilla damage formula ([[vanilla-blow-damage-formula]]) and bends it with three game-model decorators. All the numbers live in `DellarteDellaGuerra/ModuleData/CustomXml/dadg_combat_items.xml`. Shipped on `develop` in Core and content on 2026-11-07.

## How a blow is resolved

1. **Material at the hit location.** `AgentArmourReader.MaterialAt` checks every armour piece the victim wears. The strongest material listed for the hit location wins. A location no piece lists counts as Cloth. Items missing from the table fall back on their XML `material_type`.
   - Head and neck use `head`. Torso uses `torso`. Shoulder uses `shoulder`. Arm uses `arm`, from the body armour and the gloves, so a gauntlet makes the whole arm Plate. Legs use `legs`, from the leg armour and any body armour with `leg_armor` above 0.
   - The cape slot is ignored for material, bevors included. Their `head_armor` still adds to the head value ([[head-armour-sums-all-slots]]).
2. **Armour value.** `DadgStrikeMagnitudeModel.CalculateAdjustedArmorForBlow` forwards to the wrapped model unchanged, preserving perks. There is no DADG armour-value multiplier. The interface's default implementation only returns base armour, so this forwarding override must remain.
3. **Swing and thrust magnitude.** The same model scales half-sword swings (`HalfSword`) and softens the vanilla 0.15 non-tip thrust penalty for spears and pikes (`NonTipThrust`, keyed by crafting template).
4. **Absorption.** `DadgAgentApplyDamageModel.ApplyGeneralDamageModifiers` multiplies final damage by `1 - Absorbed(material, blow, weaponClass)`, after the vanilla formula uses the full armour value ([[agent-apply-damage-model-decorator]]). XML is one nested `Absorption / Material / Blow / Default-or-WeaponClass` tree; a matching weapon entry replaces Default, so each hit uses one fraction. Both damage and the hit logger use this lookup.
   - Current trial fractions for cut / pierce / blunt: Cloth 0 / 0.03 / 0.03; Padded 0.05 / 0.02 / 0.1; Mail 0.15 / 0 / 0.11; Brigandine 0.25 / 0.03 / 0.1; Plate 0.4 / 0.18 / 0.16. The user requested a 0/5/15/25/40% cut progression on 2026-11-08, keeping every other setting unchanged: [[dadg-combat-cut-progression-trial]]. The prior log-derived rates and 80% plate cut baseline are preserved in [[dadg-combat-absorption-refit]] and [[dadg-combat-latest-siege-2026-11-08]].
   - Plate Cut overrides are `OneHandedSword=.88`, `TwoHandedSword=.94`, `TwoHandedPolearm=.52`; other weapon classes fall back to the .40 Default. Half-sword usages map to TwoHandedSword despite native polearm classification. These target low sword-cut damage and stronger poleaxe cuts; they have not yet been measured live. The preceding siege snapshots predate these overrides.
   - Firearms use the full armour value and always absorb 0, even if a firearm entry is supplied. Mounts, shield hits, back-shield hits and falls also bypass absorption.
   - Blow type follows the game's forced-blunt cases: alternative attack, fall, horse charge, empty hand or collision bone other than the weapon's attach bone. Firearm ammunition is classified separately.
5. **Tier and price.** `DadgItemValueModel.CalculateTier` returns the table tier for listed weapons, which also drives the price ([[crafted-weapons-ignore-tier-override]]).

The live strike chain is DADG → `NavalStrikeMagnitudeModel` → `SandboxStrikeMagnitudeModel`. `CustomGame` runs `InitializeGameStarter` too, so custom battles get the same models.

## Code map (Core `src/`)

- **Domain/Combat (pure).** `ArmourAbsorption`, `HalfSword`, `NonTipThrust`, `CombatItems`, `CombatItemCatalog`, `ArmourPiece`/`WornArmour`, enums `ArmourMaterial`, `BlowType`, `HitLocation`. The rule classes are instances built from the XML. `None` instances are neutral, meaning vanilla behaviour.
- **Infrastructure.** `Combat/Spi/CombatItemXmlRepository` parses the table. A missing or broken file logs an error and returns `CombatItems.Empty`, the neutral rules.
- **Integration.**
  - `DI/CombatServiceContainer.AddDadgCombat()` holds the registrations.
  - `Combat/CombatFeatureInstaller.InstallModels(starter)` is called from `SubModule.InitializeGameStarter`.
  - **Toggle.** `<CombatConfig><EnableCombatOverhaul>` in Core `config/dadg.config.xml`, read once when `CombatFeatureInstaller` is constructed, as jousting does. When it is false the three models and the balance logger are not installed, and a restart is needed. Crafted damage and armour values come from content XML, so they stay rebalanced.
  - `Combat/CombatBalanceMissionLogic` is the temporary `[combat-balance]` hit logger.
- **Tests.** `DellarteDellaGuerra.Domain.Tests/Combat/`. `ShippedCombatRules.cs` is a copy of the XML rule rows that the balance tests use. Update it when the XML changes.

Tuning: [[dadg-combat-rules-tuning]]. Weapons: [[dadg-weapon-ladder]]. Armour: [[dadg-armour-values]]. Why native and not RCM/RBM: [[dadg-combat-native-layer-over-rcm]]. What is still unverified: [[dadg-combat-open-work]].

Related: [[vanilla-blow-damage-formula]], [[agent-apply-damage-model-decorator]], [[head-armour-sums-all-slots]], [[crafted-weapons-ignore-tier-override]]
