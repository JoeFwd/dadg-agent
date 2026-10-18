---
name: dadg-warsails-campaign-perf-2026-10-04
description: Findings of the 2026-10-04 War Sails campaign performance probe - fast-forward cost reproduced, no War Sails-specific cause proven; sea navmesh numbers and a material discrepancy.
type: incident
topic: incidents-crashes
tags: [performance, war-sails, navmesh, campaign]
sources: [src/.tmp/warsails-perf/findings.txt]
updated: 2026-10-18
---

# War Sails campaign perf (inconclusive)

- Frame dt: paused 14.4 ms, normal 16.5, fast-forward 21.4 (p95 32 ms). Campaign.Tick avg 0.35 / 1.8 / 5.6 ms, max 106 ms on fast. In the fast stage TickPartialHourlyAi 2.7 ms avg and TickPeriodicEvents 1.5 ms avg (max 98.8 ms); the culprit listener was not identified.
- Native MBMapScene.TickVisuals ~4.8-5.6 ms even paused. Hiding the sea / lowering water quality saved only ~0.5 ms (within drift).
- Nameplate cost (568 settlements) was 4.5 ms in one moving capture but 0.4-0.7 ms later; not reproduced.
- Navmesh: pre-WarSails 42,592 faces / 20,670 sea faces / 60 water components; DADG now 44,324 / 20,443 / 54 (96.9% of water faces in one component); official NavalDLC 20,258 / 2,849 / 3. Sea faces are 7.2x official but mostly pre-existing: no fragmentation explosion. Entities 92,571 -> 92,823; one 2744x2744 water plane (as official); 7 old lake planes removed.
- Asset discrepancy (unproven FPS impact): custom main sea material has empty materialFlags/shaderFlags (official has render_front_to_back/no_modify_depth_buffer/needs_forward_rendering and use_depth/refraction/use_decals), vector arg 1 = 0 not 10, native normal-map variant.
- Next tests: find the expensive periodic-event listener during a stall; reduced open-sea graph copy or matched pre-WarSails baseline; native profile of TickVisuals. Do not simplify the production navmesh without proof.

Method: [[campaign-perf-measurement-method]]. See also [[dadg-private-war-hostility-cpu-profile]], [[ws-fmod-sail-sound-hang]].
