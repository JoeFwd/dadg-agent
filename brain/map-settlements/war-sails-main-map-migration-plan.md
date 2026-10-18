---
name: war-sails-main-map-migration-plan
description: Plan to migrate DADG's campaign map to War Sails v1.2.8 (plan only, not executed in the sources).
type: decision
topic: map-settlements
tags: [war-sails, map, plan]
sources: [plans/warsails-main-map-migration.md]
updated: 2026-10-18
---

# War sails main map migration plan

Status: EXECUTED at least in part (git history, Map repo, read-only check 2026-10-18). Commits: a96effa and 2c3774b (2026-09-22, first and second warsails migration parts), f157819 (2026-09-22, War Sails settlement ports), 1e2ca0c (2026-09-29, first warsails map that does not crash). Ship assets/authoring followed 2026-09-29 to 2026-10-04 (4d2babb, f5f15d9, e19710f, 844e5e9, b8bd534, 109d1e4). Whether every plan item (bridges, pirate clearance, three caches) landed was not verified; only .superpowers has no execution report.

The generic requirements (terrain ids, ports, bridges, water plane, caches, shipyard NRE) are in the bannerlord note. DADG consequence: every port town needs a shipyard, and distance caches must be regenerated for the DADG map, never copied from vanilla.

Related: [[warsails-main-map-migration-contract]], [[dadg-ws-ship-navmesh-and-climber-fixes]]
