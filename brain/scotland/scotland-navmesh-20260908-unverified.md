---
name: scotland-navmesh-20260908-unverified
description: A 2026-09-08 Scotland navmesh deployment was never confirmed loaded natively; offline audit passes are not proof.
type: incident
topic: scotland
tags: [navmesh, scotland, verification]
sources: [runtime-evidence/scotland-navmesh-20260908]
updated: 2026-10-18
---

# Scotland navmesh deployment: INCONCLUSIVE

Files were deployed with recorded hashes and an offline audit reported 7,599 protected face records and 179 positions synced. But the native editor never reloaded the files and native capture hung twice, so no native load result exists.

Lessons: do not save stale in-memory editor state over deployed files; an offline graph audit does not prove the engine loads the mesh ([[navmesh-faces-must-be-tris-or-quads]], [[navmesh-presence-probe-in-rider]]). Later fixes for settlement gates on non-land faces are in [[dadg-scotland-gate-av]], [[settlement-gate-on-non-land-face-pathfinding-av]].

Related: [[navmesh-presence-probe-in-rider]]
