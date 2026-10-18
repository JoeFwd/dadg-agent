---
name: dadg-privatewars-gathering-army-fixes
description: PrivateWars 2026-10-11 - three fixes for the AiBehaviorObject misread - _goalArmyLeaders recording, VetoSameKingdomSiegeRelief, and ReleaseBelligerentsFromForeignArmies
type: incident
topic: feature-private-wars
tags: [privatewars, army, gathering, veto, fixed]
sources: [memory/gathering-army-aibehaviorobject-not-target.md]
updated: 2026-10-18
---

# PrivateWars gathering-army bugs (FIXED 2026-10-11)

Rule and mechanism: [[gathering-army-aibehaviorobject-not-target]].

1. The side-leader selector dropped a new army's leader right after creation, so a different lord raised another army almost every day. Fix: record the leader in `_goalArmyLeaders` at ReplaceMembers time.
2. Vanilla Defender scoring drew the besieger's own side onto a private-war siege. Fix: zero those scores via `PartyThinkParams.SetBehaviorScore` (`VetoSameKingdomSiegeRelief`).
3. (Evening) `ReleaseBelligerentsFromForeignArmies` used the same AiBehaviorObject test on the daily tick and stripped every member out of the side's own gathering goal army: logs showed "joined by" then "lost ... behaviour=EscortParty" one tick later, no siege ever formed, wars resolved by score decay. It now also accepts the leader recorded in `_goalArmyLeaders`.

Cost a day of playtests to pin down.

Related: [[pw-sides-dejure-crosses-kingdoms]]
