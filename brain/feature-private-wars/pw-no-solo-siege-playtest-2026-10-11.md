---
name: pw-no-solo-siege-playtest-2026-10-11
description: Four playtest attempts on 2026-10-11 of the private-war designated-leader siege bid; two native AVs, a navmesh gate fix, a foreign-army release fix that passed, and no siege bid observed.
type: incident
topic: feature-private-wars
tags: [private-wars, playtest, kilchurn, navmesh]
sources: [runtime-evidence/private-wars-no-solo-siege.feature.md]
updated: 2026-10-18
---

# Private wars: no-solo-siege verification (PARTIAL, 2026-10-11)

Fixture: save `agent_privatewar_before_20261011_0236`; Hamilton (attacker, 134 troops) vs Campbell (defender, 143 troops, same kingdom) over `dadg_sco_kilchurn_castle`; game 1.4.8 / War Sails 1.2.8.

- Attempt 1 and 2 (FAIL, defect separate from the feature): native `AccessViolationException` in `GetPathBetweenAIFaceIndicesWithRegionSwitchCost` within ~30 s at speed 2-4. Resolved stack: vanilla `AiMilitaryBehavior.AiHourlyTick` -> raid/siege scoring -> `NavalDLCMapDistanceModel` -> `SandBoxNavigationCache.GetRealDistanceAndLandRatioBetweenSettlements`, pair Kilchurn Castle <-> Kirkiboll village, with `IsOnLand` True vs False. Restoring the committed navmesh and distance caches did not help. No DADG frames in the stack.
- Root cause (found after attempt 2): `dadg_sco_kilchurn_castle` and `dadg_sco_auchterarder_village` had gates on a non-land navmesh face (index -1); fixed in `settlements.xml`. See [[dadg-scotland-gate-av]], [[settlement-gate-on-non-land-face-pathfinding-av]].
- Attempt 3 (partial): a scan at the safe anchor for gate/port positions not on a land face returned empty, and the AV did not recur over ~10 in-game days at speed 2. The attacker stayed an escort of the king's army the whole time. Halted by a vanilla NavalDLC NRE (see [[resuming-from-first-chance-exception-kills-process]]).
- Attempt 4: after `ReleaseBelligerentsFromForeignArmies` / `FilterOrdinaryMembers`, the attacker left the foreign army within ~2 days (criterion a PASS, repeated for a second clan pair). But both leaders were then wrecked by unrelated Lordship-of-the-Isles fighting (attacker's party destroyed and leader captured; its clan had only 2 heroes so no fallback). Criteria b-e unobserved.
- Odd readout seen in attempts 3-4: war score drifted negative (0 -> -33.9) while the reported battle count stayed 0; either score has a non-battle component or the reporting is inconsistent. Unresolved.

Tooling notes: `bannerlord.kingdom.get_clan` returned Method-not-found in this build; use debugger evaluation over `Clan.All` instead. Raw `pause_execution` lands on GC-unsafe native frames, so use the safe anchor.

Related: [[pw-run-outcomes-2026-10-11]], [[gathering-army-aibehaviorobject-not-target]], [[pw-sides-dejure-crosses-kingdoms]], [[safe-evaluation-breakpoint-anchor]]
