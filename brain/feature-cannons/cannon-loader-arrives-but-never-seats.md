---
name: cannon-loader-arrives-but-never-seats
description: A cannon loader that loses its ball en route latches use_load as HasAIMovingTo forever; fixed by porting vanilla's trebuchet release branch into AmmoLoadHandler (not yet live-verified)
type: incident
topic: feature-cannons
tags: [cannons, siege, standing-point, ammo, latch]
sources: [memory/cannon-loader-arrives-but-never-seats.md]
updated: 2026-10-18
---

# Cannon loader arrives but never seats

Observed live 2026-09-03: attacker cannon in a running siege with `ammo=13`, `State=LoadingAmmo`, pilot seated on `use_reload_fire_l`, and `use_load` reporting `HasAIMovingTo` for **249 seconds straight** (t=571 to t=820) with no ammo movement. The gun never fired.

Probing the mover made it diagnosable:

```csharp
p.MovingAgent.IsActive()                                   // alive
p.MovingAgent.Position.Distance(p.GameEntity.GlobalPosition) // 0.2m
p.MovingAgent.Formation.FormationIndex                      // Bodyguard
```

The loader was alive, standing on the point, correctly assigned; it arrived and never seated. Root cause and engine rule: [[weapon-requirement-standingpoint-hasaimovingto-latch]].

**Fix** (`AmmoLoadHandler.Update`, `Ammo/Api/AmmoLoadHandler.cs`): the method only had a `loadAmmoPoint.HasUser` branch. Added the `else if (loadAmmoPoint.HasAIMovingTo)` branch vanilla's trebuchet already has: if the mover is not wielding the right `WeaponClass`, `StopUsingGameObject(true, StopUsingGameObjectFlags.None)`, which internally does `AIMoveToGameObjectDisable()` and clears the latch. No `SendAgentToAmmoPickup` equivalent is needed: a ball-less agent cannot be re-sent to `use_load` (`IsDisabledForAgent`), so the detachment routes it to the pickup point. Applied and compiles; **not yet live-verified** (the siege had ended and the deploy copy is blocked while Bannerlord.exe holds the DLL).

Distinct from [[aiformationmanager-spent-cannon-budget-deadlock]] (spent gun, fixed) and [[bodyguard-orderposition-drafts-distant-crew]] (crewman dies en route; here it made the trip). Related: [[standingpoint-tickaux-toctou]], [[artillery-detachment-weight-gated-on-ammo-point]].

Diagnostic note: always print `p.IsDeactivated` alongside occupancy; dropping that flag from the sample expression cost a cross-sample comparison.

Generic rule: [[reloader-frozen-at-ammo-point-gate-hypothesis-falsified]]
