---
name: dadg-navmesh-backport-london-hideout
description: A develop-branch London and hideout-spawn navmesh fix was reapplied onto the complete navmesh with only protected-region-safe edits. FIXED.
type: incident
topic: map-settlements
tags: [navmesh, backport, london]
sources: [backport commit_msg]
updated: 2026-10-18
---

# Backport onto complete navmesh

Status: FIXED. Reapplied develop's London/hideout fix: 2 vertex moves (v5838, v7746) and 4 faces g3 14 -> 1 (f2204, f3304, f5135, f5137), touching only the protected region. Checks: crash-class clean over 34,093 faces, one global manifold component, the 550-edge border coordinate-identical.

Related: [[dadg-main-map-geometry-and-protected-england-faces]], [[navmesh-faces-must-be-tris-or-quads]]
