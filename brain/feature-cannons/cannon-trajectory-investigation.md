---
name: cannon-trajectory-investigation
description: RESOLVED - "cannonball flies shorter / must aim higher" is a data regression (muzzle velocity 120->90, commit 4509642) under an unchanged 0.2rad elevation cap, NOT a trajectory-formula or 1.4 change
type: incident
topic: feature-cannons
tags: [cannons, trajectory, muzzle-velocity, data-regression, resolved]
sources: [memory/cannon-trajectory-investigation.md]
updated: 2026-10-18
---

# Cannon trajectory: "aim higher / falls short" (RESOLVED 2026-07-23)

Reported after migrating the Cannons module from Bannerlord 1.2/1.3 to 1.4: the player must aim much higher to hit the same spot; shots fall short. Diagnosis only; no fix was authorised or applied.

**Root cause: a muzzle-velocity data cut under an unchanged elevation cap, not a physics/formula change and not the 1.4 migration.**

- The flight is the same drag-free vacuum parabola as 1.2/1.3. Confirmed live: at max barrel elevation the ball "flies very far"; drag is still zeroed (the `Boulder` air-friction patch still matches in 1.4). The launch patch rewrite (a29ac07) is behaviour-equivalent; aim/offset code untouched; native missile, air-friction and vertical-aim math identical 1.2.12 to 1.4.6.
- Commit **`4509642`** ("re-balance siege engine damage and health", 2026-03-31) rebuilt the cannon lineup in `../DellarteDellaGuerra/Prefabs/cannons.xml`. Player cannon: **BaseMuzzleVelocity 120 -> 90**; restrictions Top 0.2 / Bottom -0.1 -> Top 0.2 / Bottom **-0.5**.
- **The elevation ceiling never moved** (clamp maths: [[siege-weapon-release-angle-clamp-and-range]]). Both old and new restrictions give max release angle 0.2 rad (~11.5 degrees); widening Bottom only added downward aim. Live max shot pinned at exactly `rel=0.2`.
- At a fixed cap range goes with v squared: 120 -> 90 = (90/120)^2 = about 56% of old range; even the strongest new cannon (110) = 84%. Targets reachable before now fall short and cannot be compensated.
- Timing: the rebalance predates the 1.4 migration (75b2427), so it is a data regression the user likely first noticed on 1.4.

**Fix lever (data, not code; NOT applied):** in `../DellarteDellaGuerra/Prefabs/cannons.xml` raise `BaseMuzzleVelocity` toward 120 and/or raise `TopReleaseAngleRestriction` above 0.2 on the player cannons (veuglaire block ~L1153 = 90, falconet ~L397 = 100, ~L1509 = 110). That file is the REAL deployed prefab (a separate git repo), not greatcannon.xml/mortar.xml.

**Only remaining blind spot:** native 1.4.7 (War Sails); decompiled sources stop at 1.4.6. Unlikely, since live flight is a clean vacuum parabola.

**Statically ruled out (decompiled 1.3.15/1.4.6):** `AddCustomMissile` identical; `GetAirFrictionConstant` single overload, patch resolves; cannonball is `weapon_class="Boulder"` so the drag-zero Postfix targets it; `ArtilleryRangedSiegeWeapon.cs` migration changes were only StartingAmmoCount/AI selection; native `RangedSiegeWeapon` launch/gravity/muzzle unchanged 1.3.15 to 1.4.6; `MBGlobals.Gravity=9.806`; addRigidBody=false.

Related: [[bannerlord-live-version]], [[gabs-on-1-4-7]]
