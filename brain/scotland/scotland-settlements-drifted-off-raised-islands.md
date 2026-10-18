---
name: scotland-settlements-drifted-off-raised-islands
description: 2026-08-15 diagnosis - 64 of 160 Scottish settlements invalid because they drifted off their raised terrain islands (only 14 have terrain > 10), not for lack of navmesh; fix is nudge back onto own island plus carve navmesh only over terrain > 10
type: incident
topic: scotland
tags: [scotland, terrain, islands, navmesh-studio, land-test, carve]
sources: [memory/scotland-settlements-drifted-off-raised-islands.md]
updated: 2026-10-18
---

# Scottish settlements drifted off raised islands (2026-08-15)

The navmesh studio's footprint sample (`server/web.py _sample_on_land`, [[navmesh-studio-tool]]) counts land iff **terrain.bin height > 10.0 AND not over a navmesh water face** (g3 in {8,10,11,18,19,22,24}). Height comes from terrain.bin, NOT the navmesh, so carving sea faces to land validates a site only if its terrain is already > 10; below 10 the height test fails first.

Of 64 invalid settlements (of 160): only **14** have terrain > 10 (carve-in-place candidates), **50** sit at <= 10. Outer Hebrides raised by task #21 (Stornoway, Kisimul, Rodel, Teampull Na Trionaid) read 5.2-8.8 at the settlement point, yet raised land exists within about 34 units of 58/64. The islands were raised (backup `terrain.bin.bak_islands_20260729_001149` proves #21 ran); a later agent moved settlements to real-world-derived coords that drifted them into sea. Six sites (Kisimul, Teampull Na Trionaid, Capail Mor, Gearraidh Bhailteas, Loch Hyrbol Tower, Teampull Eoin Bragar) have no terrain > 10 within 34 units.

**Fix = two coupled ops:** (1) nudge each drifted settlement back onto ITS OWN raised island, never onto another landmass; (2) carve navmesh sea->land only over faces on terrain > 10. User constraint: never raise or create terrain ("do not create new islands"). Carve guards in `scotland/carve.py`: England faces [0,7599) byte-identical, topology unchanged, round-trip asserted, .bak written.

Related: [[scotland-population-project]], [[dadg-vanilla-override-pattern]]
