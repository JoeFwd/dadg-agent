---
name: dadg-deployment-banner-effect-id
description: Deployment captain tooltip NRE from six banners using the obsolete IncreasedDamageAgainstMountedTroops effect id; diagnosed, data fix pending.
type: incident
topic: incidents-crashes
tags: [banner, deployment, nre, xml, version-migration]
sources: [Rider launcher session f613f8ac-a98c-4949-a24c-12b6f78a0f73 2026-11-27, DellarteDellaGuerra/ModuleData/items/dadg_banner_modifiers.xml, DellarteDellaGuerra/ModuleData/items/items.xml]
updated: 2026-11-27
---

Jane Howard (`dadg_lord_4_4`) triggered a `NullReferenceException` in vanilla `OrderOfBattleVM.GetAgentTooltip`, through `SPOrderOfBattleVM.GetAgentTooltip`, `OrderOfBattleHeroItemVM.RefreshValues` and deployment initialization. Her `deer_bane_flag_t1` had a real BannerComponent but a null BannerEffect.

Runtime lookup of `IncreasedDamageAgainstMountedTroops` returned null; `IncreasedMeleeDamageAgainstMountedTroops` resolved. The installed custom XML still uses the former id at dadg_banner_modifiers.xml lines 117, 150, 183, 216, 249 and 282, plus items.xml line 2719. Native 1.5.7 banners and DefaultBannerEffects use the latter.

A read-only runtime scan found exactly six loaded banners with null effects: `deer_bane_flag_t1`, `boar_bane_flag_t2`, `horse_bane_flag_t3`, `spear_bracing_banner_t1`, `spear_wall_banner_t2`, `pike_wall_banner_t3`. Spear Bracing has definitions in both custom files.

Full 1.5.7 comparison: 46 custom XML banner definitions, 45 unique items. All effects and banner levels match SandBoxCore banners except the seven stale effect attributes above. The other ten distinct effect ids are registered. Native also registers DecreasedChargeDamage and IncreasedMoraleShockByMeleeTroops, neither referenced by these custom definitions. Bonus values come from the native DefaultBannerEffects registry. Correcting only these effect references preserves existing-save compatibility by the Campaign saved-game Items XML loading path; no live round trip performed.

Status: diagnosis confirmed; no gameplay/data fix applied or retested. The launcher crash session was left paused. Replace all seven stale XML references and restart/reload before deployment verification.

Related: [[banner-effect-id-must-match-runtime-registry]]
