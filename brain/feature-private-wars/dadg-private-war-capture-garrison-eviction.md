---
name: dadg-private-war-capture-garrison-eviction
description: A private-war siege capture evicted the capturer's new garrison (then NRE in IsGarrisonStarving) because the MapEvent.Update "kingdom at war with itself" scope leaked into the inline capture path
type: incident
topic: feature-private-wars
tags: [private-wars, siege, garrison, crash, harmony-scope]
sources: [PrivateWars MapEventUpdatePrivateWarScopePatch.cs, vanilla 1.4.8 PartyDiplomaticHandlerCampaignBehavior, MapEvent.Update/FinishBattle]
updated: 2026-10-27
---
A scope opened around `MapEvent.Update` covers more than the battle: Update finishes a won battle inline
(`FinishBattle -> FinalizeEventAux -> SiegeCompleted -> ChangeOwnerOfSettlementAction.ApplyBySiege`), so
every `OnSettlementOwnerChanged` handler ran while `Kingdom.IsAtWarWith(itself)` answered true. Vanilla
`PartyDiplomaticHandlerCampaignBehavior.CheckSettlementSuitabilityForParties` then saw the capturer's fresh
garrison "at war" with its own castle and `LeaveSettlementAction`ed it. Next hourly `Clan.UpdateCurrentStrength`
-> morale model -> `SettlementHelper.IsGarrisonStarving(null)` = unhandled NRE, game dies.

Fix: `MapEventFinishBattleExitPrivateWarScopePatch` (prefix on private `MapEvent.FinishBattle`) closes the scope.
Verified 2026-10-27 from audit.sav: York took Conisbrough, garrison stayed, no crash over 7 days.

Lesson: any "pretend X" scope around `MapEvent.Update` must close before `FinishBattle`.

Related: [[dadg-private-war-same-kingdom-battles]]
