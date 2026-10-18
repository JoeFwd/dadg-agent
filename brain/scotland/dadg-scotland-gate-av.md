---
name: dadg-scotland-gate-av
description: FIXED 2026-10-11 (uncommitted Map settlements.xml) - Kilchurn castle and Auchterarder village gates were on non-land faces and crashed every campaign playtest
type: incident
topic: scotland
tags: [kilchurn, auchterarder, gate_pos, pathfinding, av, fixed]
sources: [memory/scotland-port-village-pathfinding-av.md]
updated: 2026-10-18
---

# Scottish gate AV (FIXED 2026-10-11, uncommitted)

Mechanism, scan and fix: [[settlement-gate-on-non-land-face-pathfinding-av]].

- Crash: after about one in-game hour on save `agent_privatewar_before_20261011_0236` (and the saveauto1 lineage).
- Captured: party `dadg_sco_lord_clan_clanranald_party_1` (Lordship of the Isles, `battania`) scoring `dadg_sco_kilchurn_castle` (Crown, `khuzait`; at war), NavigationType All. Pair: `kilchurn_castle` (land) <-> `dadg_sco_kirkiboll_village` (port village, red herring).
- Cause: Kilchurn's gate was on the Loch Awe water face. The scan also flagged `dadg_sco_auchterarder_village`. HEAD `1536a18` "Align map ports with navigable water" reproduced it.
- It blocked every DADG campaign playtest including private-war verification; unrelated to PrivateWars code.

Related: [[scotland-population-project]]
