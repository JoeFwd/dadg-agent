---
name: scotland-navmesh-objectives-20260801
description: 2026-08-01 snapshot of the Scotland navmesh/settlement stage plan (Stage 4 reachability, Stage 5 deploy and load-verify) on 1.4/complete-navmesh; later notes supersede the settlement counts.
type: reference
topic: scotland
tags: [scotland, navmesh, settlements, plan]
sources: [bannerlord-navmesh-studio/dadg-navmesh-objectives.md]
updated: 2026-10-19
---

# Scotland navmesh objectives (2026-08-01 snapshot)

Status list kept in the Studio checkout until 2026-10-19 and moved here. It predates the 160/170 rebalances ([[scotland-settlement-rebalance-170]], [[scotland-settlements-drifted-off-raised-islands]]), so check those before treating any item as still open.

Target branch: `1.4/complete-navmesh`.

## Open objectives

**Stage 4 - navmesh reachability (pending).** Every new or moved settlement position must be reachable on the campaign navmesh.
- Carve/repair reachability for the new eastern settlement positions.
- Carve/repair reachability for the trimmed western positions.
- Verify each settlement sits on a navigable face and connects to the road network.

**Stage 5 - deploy, load-verify, commit (pending).**
- Deploy the generated `settlements.xml` + `scene.xscene` + navmesh into the running module.
- Build and load-verify in-game (no crash, settlements appear, map loads clean).
- Commit onto `1.4/complete-navmesh`.

**In flight then:** verify the navmesh in-game; deploy / build-load-verify / commit (overlaps Stage 5).

## Constraints

- Hand-authored England navmesh faces `[0, 7599)` must stay byte-identical.
- Never hand-edit `RuntimeDataCache/`; regenerate via Bannerlord tooling.
- Studio tool tests use read-only endpoints only (never `/api/save` or `/api/save_entities`).
- The user runs Bannerlord and shares screenshots; do not launch or kill the port-8770 server unexpectedly.

## Done by 2026-08-01

- Full land+sea navmesh generated and harmonised through v15 (coastline weld, hole-free coastal band, closed boundary loops, waterline retriangulation, navigable rivers/lakes, Outer Hebrides islets).
- Scotland settlement placement finalised (181), master data built (type/hierarchy/culture).
- Kingdom of the Isles + clans + heroes authored; 181 Scotland settlements XML authored.
- Two-kingdom Scotland XML (Stage 2) + `settlements.xml`/`scene.xscene` from master_160 (Stage 3).
- Outer Hebrides island terrain stamped into `terrain.bin`.
- Settlement-placement studio tool (backend + frontend, v2 footprints/labels/symbols).

Related: [[scotland-population-project]], [[scotland-navmesh-20260908-unverified]], [[dadg-hebrides-island-float-terrain-fix]]
