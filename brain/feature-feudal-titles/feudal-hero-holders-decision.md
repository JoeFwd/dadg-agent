---
name: feudal-hero-holders-decision
description: Decision: titles name a hero and the holder's clan is derived, never cached; all ranks are hero-held.
type: decision
topic: feature-feudal-titles
tags: [feudal, titles, hero]
sources: [doc/feudal-hero-claims-and-succession-design.md, doc/feudal-hero-titles-and-houses.md]
updated: 2026-10-18
---

# Feudal hero holders decision

`HolderClanId` was deleted in favour of `HolderHeroId`. Reason: engine politics is clan-anchored, but heroes marry and change clan, and a cached clan needs re-sync passes (cadet spinoff, marriage). Deriving through `IGenealogy.GetClanOf` makes those free. Consequences: brothers can hold separate titles and fight each other; a daughter's titles marry out with her; claim exclusion becomes "cannot claim what you personally hold".

Resolved decisions: succession ordering as in [[feudal-succession-rule]]; all ranks hero-held; the player is excluded as claimant and target; cadet clan is reabsorbed on defeat; cross-kingdom claims per [[cross-border-marches-decisions]]. Houses (grouping cadet branches such as Neville of Raby/Middleham/Bergavenny) are a static config idea, not built.

Related: [[feudal-titles-overview]], [[herokilled-event-and-clan-leader-handover-race]]
