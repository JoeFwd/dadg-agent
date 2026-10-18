---
name: feudal-blood-claims-decay
description: Blood claims are rebuilt from scratch on every change; strength decays by generation from the holder and his father.
type: reference
topic: feature-feudal-titles
tags: [feudal, claims]
sources: [doc/feudal-titles.md, doc/feudal-succession.md]
updated: 2026-10-18
---

# Feudal blood claims decay

`GenerateBloodClaimsUseCase` rebuilds all Inheritance claims on new campaign, load, owner change, peace cession and any hero death, anchored at the holder and his father. A holder's son gets Strong, his daughter Weak; a Strong claimant's children get Weak; Weak passes to nobody. So claims reach two generations and a female link costs a generation. Only the holder himself is barred, so same-clan brothers and passed-over sons hold Strong claims, which lets a house fight itself. Claim origins: Inheritance, Conquest (clan-level), Marriage and Purchase (defined, nothing produces them yet).

Related: [[feudal-succession-rule]], [[feudal-player-entry-brainstorm]]
