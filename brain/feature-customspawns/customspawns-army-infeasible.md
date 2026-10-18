---
name: customspawns-army-infeasible
description: Decision 2026-08-18 - CustomSpawns invasion parties cannot form an Army for a kingdomless clan like cs_humar; use BesiegerCamp
type: decision
topic: feature-customspawns
tags: [customspawns, army, besiegercamp, decision]
sources: [memory/customspawns-army-infeasible.md]
updated: 2026-10-18
---

# CustomSpawns: no Army, use BesiegerCamp (2026-08-18)

On branch `implement-new-party-behaviour` the goal was letting CustomSpawns invasion parties form an `Army`. Verdict: **not buildable** for a kingdomless minor clan such as `cs_humar` (null `Kingdom` crashes the player's encounter menu mid-siege; leaderless members NRE in influence cost). Engine details and the BesiegerCamp alternative: [[army-requires-kingdom-use-besiegercamp-setter]].

Live asymmetry in this mod: `CustomSpawnsPartyComponent` *does* override `Leader` (only besieging main parties get a generated lord), so main-party-has-hero / companions-don't. Escort AI forced onto `EscortParty` coexists with camp enrolment by design.

Related: [[customspawns-partyowner-must-be-leader]], [[bannerlord-live-version]]

Generic rule: [[army-creation-hourly-tick-lifo-shared-cache]], [[invasion-style-party-state-machine-observed]]
