---
name: private-war-real-siege-assault
description: Decision (2026-10-26): private-war sieges end in a real wall assault the player can join; a won fief goes to the war's interim owner, not the king. Replaces the old synthetic prep-complete capture.
type: decision
topic: feature-private-wars
tags: [private-wars, siege, capture, assault]
sources: [doc/feudal-private-wars-design.md, doc/feudal-private-wars-manual-test-guide.md]
updated: 2026-10-26
---

# Private war real siege assault

A same-kingdom private-war siege is fought: a real wall-assault MapEvent with live casualties. Until 2026-10-26 DADG instead transferred the goal synthetically the hour preparations completed (`SiegeCaptureAdapter`, deleted); the user rejected that as "not a siege".

Four engine gates, four fixes (all in `src/submodules/PrivateWars/Bannerlord.PrivateWars/Patches`):
- `EncounterManager.StartSettlementEncounter` only assaults when `IsAtWarAgainstFaction` holds, false inside one kingdom. `PrivateWarAssaultGatePatch` answers true to exactly one same-faction call, armed only for a non-player besieger set to AssaultSettlement on a private-war enemy's fief. A broad scope would wrongly admit neutral lords via `SiegeEvent.CanPartyJoinSide`.
- `MapEvent.Update` finishes same-kingdom battles diplomatically on tick 1: the private-war battle scope now covers fortification battles (a settlement party fights for its owner's clan).
- `KingdomManager.SiegeCompleted` hands the fief to the king: `PrivateWarSiegeOwnerPatch` redirects `ApplyBySiege` to the interim owner (`PrivateWarCaptureOwnerPolicy`: the capturer, or the claimant if marching in the capturing army without leading it).
- Every `join_siege_event` menu option is gated on `CanPartyJoinSide`: `PlayerSiegeJoinPatch` lets the player join the side opposite their clan's private-war enemy.

Consequences: the AI assaults only once preparations are complete and it judges the assault winnable, so a weak besieger can sit outside a strong garrison. Only lords who fought are captured; lords sitting inside the town are no longer swept up. AI lords passing by still cannot join (player-only shortcut).

Status: built and unit-tested, not yet runtime-verified.

Related: [[private-wars-overview]], [[private-war-prisoner-retention]], [[king-keeps-open-fiefs]], [[siege-vanilla-1-4-facts]], [[private-wars-manual-test-howto]]
