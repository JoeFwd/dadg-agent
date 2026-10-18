---
name: dadg-roman-bridge-terrain14-banks
description: UNFIXED - five Roman town bridge decks (Great Ouse, London, Severn, Wye, Oxford) sit between terrain-14 RuralArea banks that land parties cannot use; plus one London Gothic pier with no confirmed span.
type: incident
topic: scenes-navmesh
tags: [bridges, navmesh, roman, terrain-14]
sources: [src/.tmp/final-bridge-candidate/live-deployment-report.md, src/.tmp/roman-corridor-design/README.md, src/.tmp/astra-bridge-final-review/final-v2-gate.md]
updated: 2026-10-18
---

# Roman bridge bank limitation (UNFIXED as of 2026-09-29)

- Great Ouse and London connect to passable land on one side; Severn, Wye, Oxford on neither (deck face isolated).
- Cause: the town sits on terrain 14 faces and default land navigation excludes 14 ([[campaign-navmesh-terrain-type-ids]]).
- Corridor study: 0.30 m trial strips; max whole-route width with 0.40 m building-origin disks: Great Ouse 0.20 m, Severn 0.21 / 0.54, Wye 0.20 / 0.24. Needed 0.6-0.8 m. Best leads: Great Ouse southward bank-edge strip, Severn northwest approach. No blind terrain relabel was done.
- London Gothic pier near (850.457, 199.012): sole end anchor sits inland, expected far end 1.2 m short of the far bank; no deck invented.
- Inventory: 35 Gothic piers, 20 Roman pier parts grouped into 5 bridges, 69 Gothic end objects = 40 crossing centres; no bridge meshes near the Clyde.

Related: [[navmesh-bridge-two-bank-route-gate]], [[dadg-main-map-bridge-navmesh-final-state]]
