---
name: customspawns-partyowner-must-be-leader
description: CustomSpawns besiege feature (2026-08-17) - a party capturing a castle NREd because PartyOwner/SetCustomOwner was clan.Leader, who has no party
type: incident
topic: feature-customspawns
tags: [customspawns, capture, nre, besiege]
sources: [memory/customspawns-partyowner-must-be-leader.md]
updated: 2026-10-18
---

# CustomSpawns captures need owner == leader

Debugging the besiege feature on branch `implement-new-party-behaviour` (2026-08-17). `CustomSpawnsPartyComponent` set both `PartyOwner` and `Party.SetCustomOwner(...)` to `clan.Leader`, a hero sitting in a settlement with no party, so a successful castle capture NREd. The rule and mechanism: [[partycomponent-owner-must-be-own-leader]]. The generated lord was fine (`CreateSpecialHero` fills `BornSettlement`).

Related: [[customspawns-army-infeasible]]

Generic rule: [[invasion-style-party-state-machine-observed]], [[party-component-owned-identity-pattern]]
