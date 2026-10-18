---
name: cannon-b1-reloader-stall-2026-08-13
description: Crew/bodyguard fix verification found reloaders frozen beside the ammo point; the ammo gate hypothesis was falsified and falconets were deactivated; open at 2026-08-13.
type: incident
topic: feature-cannons
tags: [cannons, reloader, siege]
sources: [runtime-evidence/cannon-crew-bodyguard-fix-verification, runtime-evidence/cannon-assault-startup-gabs-blocker, runtime-evidence/cannonattack14-edinburgh-load-blocker]
updated: 2026-10-18
---

# Cannon B1 stall (UNFIXED root cause as of 2026-08-13)

Generic facts and measurements are in [[reloader-frozen-at-ammo-point-gate-hypothesis-falsified]]. DADG specifics:
- 12 cannons in the scenario; four stuck veuglaires had `ReloaderAgentOriginalPoint == ammo_pos_g`; falconets showed `IsDeactivated = True` and `IsUsableBySide = False`. The `Deactivate()` caller is unproven.
- Scaled pool rule in use: `if (artilleryFormation.CountOfUnits <= artilleryFormation.Detachments.Count) TransferUnits(artilleryFormation, 1)`.
- The player branch of `AIFormationManager.Update` only tested `userFormations.Count == 0` (stale `UserFormations`), unlike the AI branch which evicts; see [[siegeweapon-forceduse-steals-crew]].

Fixture blockers (environment, not mod bugs):
- 2026-08-09: GABS submodule failed with `FileNotFoundException MCMv5 5.10.2.0` in `StartServer` ([[gabs-ui-driving-traps]]).
- 2026-08-09 (1.4.6): save fixture invalid; `ArgumentOutOfRangeException` on a `List` indexer while deserializing the Settlement XML cannon list of `dadg_sco_edinburgh_town`; no assault scene reached.

Related: [[cannon-loader-arrives-but-never-seats]], [[defender-cannons-firesafety-veto]], [[bodyguard-orderposition-drafts-distant-crew]]
