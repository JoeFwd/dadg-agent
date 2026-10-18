---
name: dadg-ws-ship-reimport-state
description: 2026-10-02 state of DADG War Sails ship mesh reimports - slot 1 now Map dadg_ws_* aliases, slot 2 stale; English boat prefab still on v1 sail and old body
type: reference
topic: scenes-navmesh
tags: [war-sails, ships, reimport, prefab]
sources: [memory/reimport-keeps-second-material.md]
updated: 2026-10-18
---

# DADG ship reimport state (2026-10-02)

After the War Sails alias reimport, `english_boat_b_body.4`, `english_boat_b_sail_rig_static.0/.1` and `carrack_body.2` have slot 1 = Map `dadg_ws_*` alias while slot 2 still holds the old Scenes GUID (harmless; see [[reimport-keeps-second-material]]). The live English boat prefab still points at the v1 sail and old body; it needs the v4/aisle_v2 fresh import plus a prefab repoint.

Related: [[ws-sail-cloth-params-frozen]]

## Details moved from generic notes

- Sail cloth: full table in `DellarteDellaGuerraMap/Tools/WarSailsShips/diagnostics/sail-cloth-vs-vanilla-2026-10-02.md` (Map commits e19710f and 844e5e9); generic rule in [[ws-sail-cloth-params-frozen]].
- Sail vertex paint: authoring script `Tools/WarSailsShips/external-authoring/data/dadg_ws_remaining_sails_v1.py` lines 63-81 writes A=0 only for the top band and never B (reported by the user 2026-10-03); generic rule in [[ws-sail-vertex-paint-pins]].

Generic rule: [[war-sails-sail-cloth-requirements]], [[ws-ship-navmesh-boarding-face-rules]]
