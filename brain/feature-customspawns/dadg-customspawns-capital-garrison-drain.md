---
name: dadg-customspawns-capital-garrison-drain
description: 2026-10-13 - CustomSpawns Humar capital (Charas) garrison fell 408 to 186 while every InvasionLordWarbands draw logged men=0; cause is vanilla garrison rebalance, not mod code
type: incident
topic: feature-customspawns
tags: [customspawns, charas, humar, garrison, minimumcapitalgarrison]
sources: [memory/vanilla-garrison-rebalance-on-enter.md]
updated: 2026-10-18
---

# Charas garrison drain (found 2026-10-13)

CustomSpawns enforces `MinimumCapitalGarrison` 400, yet the Humar capital (Charas) fell from 408 to 186 while every `InvasionLordWarbands` draw logged men=0. Empty replacement lords visited Charas, took vanilla's proportional share, then lost battles. Mechanism and numbers: [[vanilla-garrison-rebalance-on-enter]].

Implication: the floor must be enforced by patching or offsetting `ManageGarrisonForParty`, not by gating the spawn draw.
