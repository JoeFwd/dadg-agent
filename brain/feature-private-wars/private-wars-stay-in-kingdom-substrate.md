---
name: private-wars-stay-in-kingdom-substrate
description: Decision: private wars keep both clans in their kingdom and manufacture hostility pair-by-pair, rejecting splinter kingdoms and lone-clan ejection.
type: decision
topic: feature-private-wars
tags: [private-wars, design, kingdom]
sources: [doc/feudal-private-wars-design.md, doc/feudal-private-wars-tempkingdom-cost.md, doc/feudal-system-analysis.md]
updated: 2026-10-18
---

# Private wars stay in kingdom substrate

Decision: clans stay in their kingdom; DADG creates the war itself and makes the engine treat the pair as hostile at every consumer ([[vanilla-hostility-consumer-sites]]).

Why
- The MapFaction wall ([[mapfaction-wall-blocks-same-kingdom-hostility]]) makes a stance-based war impossible within a kingdom.
- Rejected: dual temporary splinter kingdoms (heavy: two kingdom objects per war, cost analysis in the temp-kingdom document, plus save and diplomacy side effects).
- Rejected: lone-clan ejection (autonomous join/war/peace, degraded services, 28-day discontinuation countdown for a landless clan).
- Rejected: an abstract war score that the engine never sees (the earlier option b in the feudal analysis): no map presence, no battles.
- Resilience win: kingdom membership is preserved natively, so a crash or save-load cannot leave clans stranded outside their realm.

Cost: about 8 clean model overrides plus a Harmony layer for the player encounter and menus. The work is the consumer list, not the war itself.

Related: [[private-wars-overview]]
