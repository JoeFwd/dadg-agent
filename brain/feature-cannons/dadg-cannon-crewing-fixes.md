---
name: dadg-cannon-crewing-fixes
description: Index of DADG cannon crewing fixes in the Cannons submodule - dead falconets pruned in AIFormationManager.Update, ForcedUse off, StandingPoint TOCTOU, and the related crew-pool incidents
type: reference
topic: feature-cannons
tags: [cannons, crewing, aiformationmanager, index]
sources: [memory/setdisabledsynched-leaks-detachments.md, memory/siegeweapon-forceduse-steals-crew.md, memory/standingpoint-tickaux-toctou.md]
updated: 2026-10-18
---

# DADG cannon crewing fixes (hub)

- Dead falconets pruned in `AIFormationManager.Update` (`submodules/Cannons`): [[setdisabledsynched-leaks-detachments]].
- `SetForcedUse(false)` after `base.OnInit()`: [[siegeweapon-forceduse-steals-crew]], diagnosed live as `UserFormations = [Bodyguard(8), Ranged(12)]`, `IsDeactivated=false`, `ForcedUse=True` on a paused `dadg_veuglaire`.
- Crew-pool sizing: [[formation-detachments-includes-strategicareas]], [[bodyguard-orderposition-drafts-distant-crew]], [[aiformationmanager-spent-cannon-budget-deadlock]].
- Reload NRE: [[standingpoint-tickaux-toctou]] (DADG: `AmmoPickupHandler.OnCarriedProjectileDropped`).
- Loader/ammo point: [[cannon-loader-arrives-but-never-seats]], [[artillery-detachment-weight-gated-on-ammo-point]], [[defender-cannons-firesafety-veto]].

The ForcedUse hijack ([[siegeweapon-forceduse-steals-crew]]) was diagnosed on a paused `dadg_veuglaire`.
