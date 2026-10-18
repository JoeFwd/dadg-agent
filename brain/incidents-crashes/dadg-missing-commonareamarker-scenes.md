---
name: dadg-missing-commonareamarker-scenes
description: UNFIXED as of 2026-08-01 - DADG scenes missing CommonAreaMarker scripts - York, Lincoln, London, Newcastle, dadg_village_d/e, two hideouts, plus partial others
type: incident
topic: incidents-crashes
tags: [commonareamarker, scenes, york, lincoln, london, newcastle, unfixed]
sources: [memory/missing-commonareamarker-crash.md]
updated: 2026-10-18
---

# DADG scenes missing CommonAreaMarker (UNFIXED, counted 2026-08-01)

Mechanism and fix: [[missing-commonareamarker-crash]].

Scenes with common_area entities but ZERO CommonAreaMarker scripts: York (219 sp_npc), Lincoln (176), London (174), Newcastle (124), dadg_village_e (52), dadg_village_d (51), Hideout_bluebell_forest (0), Hideout_pele_tower (0).
Partial: Bristol 1/3, Coventry 2/3, Norwich 2/3, dadg_village_b 1/3. Healthy: Lancaster 3/3.

York's `navmesh.bin` validates clean, so the crash was wrongly looked for in navmesh topology first ([[navmesh-fragmentation-is-not-a-crash-cause]]).
