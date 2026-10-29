---
name: warsails-ship-crash-chain-2026-09-30
description: Sequence of War Sails crashes 2026-09-30 to 2026-10-25 and what fixed each.
type: incident
topic: incidents-crashes
tags: [war-sails, crash, chain]
sources: [runtime-evidence/ws runs]
updated: 2026-10-29
---

# War Sails crash chain

1. `SailVisual.GetDimensions` NRE: no ClothSimulator, fixed by saving Cloth Editor settings on all 7 sail meshes (FIXED).
2. `MissionSail.UpdateForcedWindOfSailsAndTopBanner` NRE: added a `sail_faction_flag` child (tags `bd_banner_b`, `banner_with_faction_color`) to each sail prefab (FIXED). See [[war-sails-sail-cloth-requirements]].
3. Native AV in `Mission.Tick`: DADG's `dadg_full_movement_set.xml` had swimming/diving = -1 for `longpike` and `firearm`; set to `swim_unarmed`/`dive_unarmed` (FIXED 2026-10-01, 30-minute battle clean). See [[ws-movement-set-swim-dive-slots-must-be-defined]].
4. FMOD update-thread livelock: DADG's item pre-XSLT stripped NavalDLC's `hook` item, so hook_grab sounds spammed ~350/s; whitelisted (FIXED 2026-10-25). See [[ws-fmod-sail-sound-hang]], [[dadg-ws-hook-item-stripped]].
5. Mod soundtrack ids collided with Native when native music was kept: [[ws-psai-duplicate-ids-with-native-soundtrack]].
6. Port-screen figurehead tooltip NRE after battle: [[ws-naval-quirks]].

Related: [[ws-sail-cloth-params-frozen]], [[ws-ship-navmesh-boarding-face-rules]]
