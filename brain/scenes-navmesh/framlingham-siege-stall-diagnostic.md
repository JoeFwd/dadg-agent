---
name: framlingham-siege-stall-diagnostic
description: Live diagnostic of a Framlingham siege stall: cannon crew never released and the tower navmesh was an orphan island; the DADG-side crew finding was real but not the cause.
type: incident
topic: scenes-navmesh
tags: [framlingham, navmesh, siege, cannons]
sources: [src/doc/framlingham-siege-stall-diagnostic.md]
updated: 2026-10-18
---

# Framlingham siege stall diagnostic

Observed: 67 agents, zero casualties and no movement for 19.7 s. Defenders were cannon crew in the Bodyguard formation, which is excluded from `Team.FormationsIncludingEmpty`, so vanilla tactics never order them; `AIFormationManager` deficit was 0 so surplus crew was never released ([[aiformationmanager-spent-cannon-budget-deadlock]]). But the decisive cause was data: no navmesh under the tower and a stair pocket, because the level_1 tower navmesh was an island and connector faces were hidden (see [[framlingham-navmesh-hole]] and [[navmesh-vertex-touch-is-not-an-edge-connection]]). Revision 2 of the source corrected the g5 bit decoding ([[xscene-declares-level-bit-mapping]]). Status: FIXED by connector faces.

Source docs: src/doc/framlingham-siege-stall-diagnostic.md.

Related: [[navmesh-vertex-touch-is-not-an-edge-connection]], [[framlingham-navmesh-hole]]
