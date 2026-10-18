---
name: dadg-seaborne-village-raid-migration
description: State of DADG seaborne village raid scenes - 73 of 426 villages sea-reachable, Grimsby variant installed, Southwark and Thorne need redesign.
type: reference
topic: map-settlements
tags: [war-sails, raid, villages, grimsby, southwark, thorne]
sources: [doc/seaborne-village-raid-plan.md, doc/generic-seaborne-layouts.csv, doc/seaborne-village-inventory.csv, src/.tmp/seaborne-village-raid-plan-updated.md, src/.tmp/verify_grimsby_assignment.py, src/.tmp/prepare_port_fix_codex.py]
updated: 2026-10-18
---

# Seaborne raid scenes (as of 2026-09/10)

- 426 villages; 73 have port coords in `settlements.xml` AND a tagged sea drop-off in `Main_map/scene.xscene`. 3 use custom scenes, 70 reuse 20 Empire/Battania layouts. 55 other `dadg_village_coastal_a` villages lack ports/drop-offs and are not sea-accessible.
- Grimsby: `dadg_village_coastal_a_navalraid` installed and assigned (offline checks passed; in-game raid test pending). West shore has ~100 m for 3 landings.
- Southwark `dadg_village_southwark`: village ~300 m inland, bank 4.8 -> ~15 m; needs a graded dock. Not reassigned.
- Thorne `dadg_village_d_combe`: river ~1 ship wide; needs widening (runtime + editor terrain). Not reassigned.
- Port moves were staged for Chester_town (634.0157, 384.0320) and village_Southwark (849.3644, 197.4005) among others, via byte-surgical scene + XML edits and a validate-against-live-navmesh step.

Plan (2026-09-29): assign villages to generic seaborne layouts and add the raid levels, naval navmesh, landing points and port coordinates per [[seaborne-raid-scene-requirements]]. Two CSVs (`doc/generic-seaborne-layouts.csv`, `doc/seaborne-village-inventory.csv`) list the layouts and per-village assignments.

Checklist: [[seaborne-village-raid-scene-checklist]].
