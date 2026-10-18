---
name: feudal-succession-rule
description: Male-preference primogeniture with representation: own line, then siblings through the father, then clan head, else vacant.
type: reference
topic: feature-feudal-titles
tags: [feudal, succession]
sources: [doc/feudal-succession.md]
updated: 2026-10-18
---

# Feudal succession rule

`ExecuteSuccessionUseCase` runs on any hero's death, before blood claims are rebuilt. Order: heir of body (sons eldest-first, then daughters; a dead child is replaced by his own descendants, depth-first), then collateral through the father (brothers, then sisters, one level only), then the clan head if alive, else vacant.

- A daughter inherits only when no son's line survives; a predeceased son's daughter beats the deceased's own daughter.
- Every title goes to one heir; only the dignity moves (occupation and contest stay).
- Heir's clan is not checked; marriage carries the title into the husband's house.
- Succession mints no claims; derivation does, right after.
- A visited set guards against authored cycles ([[authored-genealogy-cycles-overflow-the-stack]]).
Real-content checks: Warwick's five dignities go to his only daughter; Somerset passes to his eldest surviving brother; killing Warwick takes the realm from 399 to 339 claims. The older design document is stale on four points (representation for daughters, dead clan head, cycle guard, who mints claims).

Related: [[feudal-titles-overview]], [[feudal-blood-claims-decay]]
