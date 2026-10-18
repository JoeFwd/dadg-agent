---
name: private-war-improvement-backlog
description: Ranked backlog of private-war improvements (2026-10-13): foreign supporters fight alone, prize goes to principal, third-party fatigue, arbitration, summons.
type: reference
topic: feature-private-wars
tags: [private-wars, backlog, design]
sources: [doc/private-war-feature-ideas.md]
updated: 2026-10-18
---

# Private war improvement backlog

Problems: whole realms join over one friendship; supporters keep the prize (nothing applies the `PrizeAward`; `AwardTheClaim` only moves seats the defender still owns); third-party goal holders leave fatigue running toward the defender; the only exit is score +-100; supporters have no lasting stake; the kingdom war steals goal armies.

Latent bugs: untracked vassal fiefs; save field cap (`PrivateWarStateSerialiser` rejects records over 14 fields, older builds silently drop newer wars; raise the bound with each appended field); kingdom-change conclusion skips `ResolveWar`; cross-realm goal armies; bond gate not tied to a side; duplicated side rule; the player can be drafted silently through the suzerain chain.

Tiers (S under a day, M a few days, L subsystem):
1. Foreign supporters fight alone (S-M); prize to the principal (S); any change of goal owner resets fatigue and third-party holders pause it (S).
2. Arbitration and love-days with bonds (M); fatigue paused while besieging, minimum duration like vanilla's 150-day guard (S-M).
3. Summons with terms using vanilla CallToWar numbers: +10 accept, -50 refuse (M); oathbreaker penalty.

Historical anchors used: Scotland got Berwick for supporting Lancaster in 1461; the Isles were bought by the 1462 Treaty of Westminster-Ardtornish; Caister 1469.

Status: analysis only, nothing implemented as of 2026-10-18.

Related: [[private-wars-overview]], [[cross-border-marches-decisions]]
