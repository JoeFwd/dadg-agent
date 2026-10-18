---
name: aiformationmanager-spent-cannon-budget-deadlock
description: FIXED via an IsSpent latch - the cannons mod's AIFormationManager budgeted crew only for cannons with ammo but never detached spent ones, so spent guns soaked crew while working guns starved
type: incident
topic: feature-cannons
tags: [cannons, siege, crew, detachment, fixed]
sources: [memory/aiformationmanager-spent-cannon-budget-deadlock.md]
updated: 2026-10-18
---

# Spent-cannon crew budget deadlock (FIXED 2026-09-03)

`AIFormationManager.Update` (`src/submodules/Cannons`) sizes the Bodyguard crew pool as:

```csharp
var cannonCount = artilleryFormation.Detachments.OfType<BaseFieldSiegeWeapon>()
    .Count(c => !c.IsOutOfAmmo);
var deficit = cannonCount * SeatsPerCannon - artilleryFormation.CountOfUnits;
```

Spent cannons are excluded from the **budget** but nothing removes them from `Detachments`: the attach path (line ~34) only refuses to *attach* a spent gun, and the pruning loop (lines ~40-42) filters on `IsDeactivated`, which is false for a merely-empty gun.

Measured live (defender side, 4 attached veuglaires, 2 out of ammo):

```
cannonCount(non-spent)=2  x2=4  units=4  DEFICIT=0
totalAttachedCannons=4    realSlotsDemanded=13
```

Supply is sized for 2 guns; demand is distributed by `DetachmentManager` across all 4. One working gun kept a permanently empty `use_reload_r`, one **spent** gun held a live crewman on its pilot seat, a fourth gun was unmanned while advertising weight 1, and `deficit == 0` refused to draft anyone.

Out of ammo is **terminal**: `CheckAmmo()` calls `SetForcedUse(false)` and deactivates every `AmmoPickUpPoint` once the reserve empties, so no crewman can refill a dry gun. Do not frame this as "starving the ammo runner". The code comment claiming "vanilla drops their detachment weight to float.MinValue" is false for this weapon class, see [[artillery-detachment-weight-gated-on-ammo-point]].

## Fix

A single `IsSpent` latch on `BaseFieldSiegeWeapon`: `IsOutOfAmmo && State == WeaponState.LoadingAmmo` (the moment vanilla treats the gun as finished, so the round still in the barrel is not wasted). It gates three places: `GetDetachmentWeightAux` returns `float.MinValue` (stops new assignment); the `AIFormationManager` prune loop detaches spent guns (nothing else releases seated men since `UsableMachine.IsAgentEligible` is hardcoded `true`); the budget then counts all still-attached cannons. Known transient: a fully unmanned spent gun never reaches `LoadingAmmo`, so it may briefly attract one crewman who advances the state machine and is then released.

Live-verified 2026-09-03 across three siege samples (t=571/676/820): all five spent guns held zero crew, `spentAttached` stayed 0 on both sides, and one cannon's full lifecycle (unmanned, seated, fired dry, `IsSpent`, formation torn down) was caught in flight. A `float.MinValue` weight on a non-spent gun is normal: it means the free seat is already claimed (`HasAIMovingTo`); read the standing points before suspecting a veto.

Related: [[setdisabledsynched-leaks-detachments]], [[formation-detachments-includes-strategicareas]], [[bodyguard-orderposition-drafts-distant-crew]]
