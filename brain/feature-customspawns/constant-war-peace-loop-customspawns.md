---
name: constant-war-peace-loop-customspawns
description: FIXED 2026-08-06 - CustomSpawnsDiplomacyModel.IsAtConstantWar now lets forced-peace return false before vanilla; found via two Calradia at War spawn clans
type: incident
topic: feature-customspawns
tags: [customspawns, diplomacy, constant-war, fixed]
sources: [memory/constant-war-peace-loop.md]
updated: 2026-10-18
---

# CustomSpawns constant-war peace loop (FIXED 2026-08-06)

`CustomSpawnsDiplomacyModel.IsAtConstantWar` was fixed 2026-08-06 so the forced-peace policy can return false before delegating to vanilla. Found via Calradia at War's `cs_southern_enslavers` (aserai) and `cs_northern_liberators` (sturgia) spawn clans: outlaw minor factions sharing culture with a kingdom, producing an endless alternating peace-message spam.

Generic rule: [[constant-war-peace-loop]].
