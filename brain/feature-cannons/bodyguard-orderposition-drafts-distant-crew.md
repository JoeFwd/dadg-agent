---
name: bodyguard-orderposition-drafts-distant-crew
description: Cannon crew refills draft the man nearest Bodyguard's OrderPosition, which is stale-copied from Infantry, so wall-top defender cannons get reloaders from 35m away and 16m below who die en route
type: incident
topic: feature-cannons
tags: [cannons, siege, formation, crew, defender]
sources: [memory/bodyguard-orderposition-drafts-distant-crew.md]
updated: 2026-10-18
---

# Defender cannon crew refills come from far away

Symptom: defender wall cannons "barely get new reloaders" and rarely fire, though the crew pool is correctly sized.

**Not** a deficit-math or transfer-guard bug. Measured live (Coventry siege, 4 defender veuglaires): Bodyguard = 8 units / 4 detachments = exactly `SeatsPerCannon * cannons`, `deficit == 0` in steady state. The `IsSplittableByAI` / `TransferUnitsAux` no-op theory is **ruled out**: every defender formation reports splittable and refills do happen.

The chain (engine mechanism generalised in [[formation-transferunits-selective-pop-uses-stale-orderposition]]):

1. `AIFormationManager.cs:59` calls `Formation.TransferUnits` which routes to `OrderController.TransferUnits` (`OrderController.cs:1628`) with `useSelectivePop = count < source.CountOfUnits && target.CountOfUnits > 0`, true for a 1-unit refill from a 93-man Infantry formation into a non-empty Bodyguard.
2. That makes `Formation.cs:2001` pop the units nearest `target.OrderPosition`.
3. Bodyguard's OrderPosition is stale: on the first-ever draft the target is empty, so `CopyOrdersFrom(this)` copies the Infantry order position permanently.

Caught at a refill (`deficit == 1`, breakpoint on `AIFormationManager.cs:57`):

```
side=Defender BG.units=7 BG.detach=4 deficit=1
BG.OrderPosition        = (407.67, 173.34)     ground z = -1.87
BG.CachedMedianPosition = (407.94, 173.13, -1.87)
machinePos (cannon)     = (390.65, 143.26, 14.32)
```

That is **34.6 m horizontally, 16.2 m below** the cannon needing crew. Replacements cross the bailey, climb the wall under fire and **die en route**; the apparent "churn" of the assigned `use_reload_r` agent was deaths (one unconscious at 0 health, one gone from `Mission.AllAgents`), not reassignment.

Also: `Bodyguard` is **not** in `Team.FormationsIncludingEmpty` (indices 0-7), so the donor at `AIFormationManager.cs:57` is always **Infantry** (courtyard, z 1-11) even when HeavyInfantry already has men on the wall at z 16-17.

Fix direction (not applied as of this note): set BG's order position to the cannon before transferring; then pick the donor formation by proximity instead of `FirstOrDefault`. Do **not** raise `SeatsPerCannon` above 2: surplus crew made agents contest the same seats.

Related: [[defender-cannons-firesafety-veto]], [[standingpoint-tickaux-toctou]], [[setdisabledsynched-leaks-detachments]], [[safe-evaluation-breakpoint-anchor]]

Generic rule: [[formation-detachments-includes-strategicareas]]
