---
name: pw-run-outcomes-2026-10-11
description: Natural-lifecycle observation of a private war (resolved by score decay) plus inconclusive goal-army and prosecution fix checks, 2026-10-11.
type: incident
topic: feature-private-wars
tags: [private-wars, lifecycle, goal-army]
sources: [runtime-evidence/private-wars-fresh-campaign-observation, runtime-evidence/private-wars-goal-army-fix-verification, runtime-evidence/private-war-prosecution-fixes]
updated: 2026-10-18
---

# Private-war run outcomes (2026-10-11)

- Fresh campaign observation (PASS): one full natural lifecycle ended `DefenderVictory` at score -100 after about 8 in-game months, and a successor war between the same clans was declared immediately.
- Goal-army fix verification (INCONCLUSIVE): over ~1.4 in-game years the attacker never formed a goal army and wars resolved only by score decay to -100, so the fix criterion was never exercised.
- Prosecution fixes: fixes A and C weakly supported, fix B unresolved. The run was cut short by a vanilla NRE in `PatrolPartiesCampaignBehavior.SpawnPatrolParty` at the rebel-owned `dadg_sco_st_andrews_town` (owner a rebel clan with khuzait culture); resuming from the pause killed the process. Why the rebel clan is khuzait is unexplained (see [[reused-culture-needs-complete-data]]).
- Open: why the Sinclair and Hamilton wars never produced siege bids.

Related: [[pw-no-solo-siege-playtest-2026-10-11]], [[constant-war-peace-loop]]
