---
name: defender-cannons-firesafety-veto
description: DADG defender wall cannons idle because the defender prefab has an 18 degree traverse arc; aiming an out-of-arc target slews the barrel to the clamp limit into the merlon and the fire-safety check vetoes (fix not yet live-verified)
type: incident
topic: feature-cannons
tags: [cannons, defender, ai, direction-restriction, fire-safety]
sources: [memory/defender-cannons-firesafety-veto.md]
updated: 2026-10-18
---

# Defender cannons never engage (fire-safety veto)

Symptom: in a siege, defender cannons sit idle with full crew and ammo and never engage the attacker cannons opposite.

**Measured live** (paused in `ArtilleryRangedSiegeWeapon.OnTick`, Coventry siege, 4+4 `veuglaire_cannon_body`):

| | DirectionRestriction | ReleaseAngle range |
|---|---|---|
| `dadg_veuglaire_spawner` (attacker) | 6.284 rad (360 deg) | -0.5 .. 0.2 |
| `dadg_veuglaire_defender_spawner` | **0.3142 rad (18 deg, +/-9)** | -0.5 .. 0.2 |

The arc is authored in `Modules/DellarteDellaGuerra/Prefabs/cannons.xml` since `3949978` (2026-06-21), probably deliberately (one defender per attacker lane).

1. Each defender can bear on **exactly one** attacker cannon (`IsTargetWithinDirectionRestriction` true for one, false for three).
2. Straight-line LOS to that one attacker failed for 3 of 4 defenders: two blocked by `dadg_english_small_fort_wall_merlon` 0.4-1.1 m from the muzzle, one by `empire_garden_wall_top_a_end` at 67 of 78 m. Selectors filter on `HasLineOfSightToTarget`.
3. Defenders then pick **formation** targets, which lead-prediction drags outside the arc. `AimAtTargetWorldUp` still calls `GiveExactInput` with the **clamped** direction, so the barrel slews to exactly +/-0.15708 rad and parks there pointing into the merlon (ray along the barrel hit it at 0.45/0.66 m; ray along the arc centre was clear). The muzzle is walled in only because it was aimed at something it cannot bear on.

**Rule: never let the AI aim at an out-of-arc target.** Check `IsTargetWithinDirectionRestriction` and drop the target *before* calling `AimAtTargetWorldUp`, since that slews to the clamp limit regardless and `IsSafeToFire` then vetoes the barrel it just mis-aimed.

**Fix** in `FieldBattleWeaponAI.TickWithTarget` (uncommitted, compiles, **not yet live-verified**): drop+blacklist out-of-arc targets; `ReadyToFire` (which aims) **before** `IsSafeToFire`; a `MaxAimSeconds` deadline that drops (does not blacklist) a target the aim never converges on (aiming legitimately stalls whenever `CanRotate() => State == WeaponState.Idle` is false, i.e. all through reloading). An earlier version reordered aim-before-safety **without** the arc guard and made things worse ("defenders don't shoot at all"): `ReadyToFire` can never be true for an out-of-arc target, so the target was held forever with the barrel jammed at the limit. Do **not** loosen `FireSafetyChecker` thresholds.

Still open: the defender emplacement at ~(420.6, 144.8, 14.8) is blocked by a merlon at ~1.08 m even along its arc centre: genuine placement, not code.

History: `a29ac07 "feat: support v1.4"` introduced an `ArtilleryTargetValidator`; `6e6b841 "refactor: remove debug cannon logs"` deleted it and silently reverted `CreateAIBehaviorObject`'s side condition (`Side != Attacker` back to `Side == Attacker`), a scope the message understates. AI class choice matches pre-1.4 (attackers `FieldSiegeWeaponAI`, defenders `FieldBattleWeaponAI`); the comment claiming otherwise is stale. `6e6b841` also replaced `IsTargetWithinDirectionRestriction => CanShootAtPoint(target)` with a **yaw-only** check, dropping vanilla's vertical release-angle test.

Related: [[cannon-trajectory-investigation]], [[standingpoint-tickaux-toctou]], [[safe-evaluation-breakpoint-anchor]]

Generic rule: [[artillery-detachment-weight-gated-on-ammo-point]], [[reloader-frozen-at-ammo-point-gate-hypothesis-falsified]]
