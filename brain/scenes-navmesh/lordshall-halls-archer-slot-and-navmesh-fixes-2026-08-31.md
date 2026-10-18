---
name: lordshall-halls-archer-slot-and-navmesh-fixes-2026-08-31
description: Lord's-hall scenes A-D and cathedral/London: 6 archer prefabs per hall converted to infantry, Hall A siege-bit navmesh patch, layout rules, and what remains untested.
type: incident
topic: scenes-navmesh
tags: [lords-hall, scene, navmesh]
sources: [runtime-evidence/keep-* reports]
updated: 2026-10-18
---

# Lord's hall fixes (2026-08-31)

- Spawn NRE: halls A-D had 21 infantry and 6 archer helpers; archers off an enabled navmesh face were dropped, so 27 defenders hit a null slot. Fix: convert 6 archer prefabs per hall to `sp_defender_infantry_lords_hall` at the same positions (24 substitutions). Cathedral and London already have 27 infantry. The user confirmed Hall A fixed; halls B-D untested and the original null never inspected.
- Hall A navmesh: only 1 face loaded (mask 5) because faces 0..38 lacked the siege bit; XOR 4 on 39 payload bytes fixed it, user reported it "seems to work".
- Layout: infantry hold the breach, archers in a rear row of three on the defenders' right, moved back 1.0 m; B and D rear archers were added then removed on request.
- 12 mapped scenes cover 139 settlements; 5 custom scenes serve 95.

Generic: [[lordshall-defender-slots-filtered-by-navmesh]], [[navmesh-level-mask-must-match-mission-mask]].

Related: [[lordshall-defender-slots-filtered-by-navmesh]], [[navmesh-level-mask-must-match-mission-mask]]
