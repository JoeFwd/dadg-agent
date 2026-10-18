---
name: dadg-v14-river-and-lake-detection
description: Flow-accumulation river detection on the DADG heightmap: what was found, river bed heights, rivers not found, Spey divide caveat.
type: reference
topic: scotland
tags: [scotland, rivers, terrain]
sources: [dadg_rivers/v14 findings]
updated: 2026-10-18
---

# Rivers from the heightmap (v14)

A plain height threshold drowned in noise above ~10.5, so v14 used D8 flow accumulation (priority-flood fill, steepest descent, accumulation >= 500 px, valleyness test). Found 11 river candidates (Barrow, Suir, Munster Blackwater, Boyne, Liffey, Spey upper/lower, Nairn, Great Glen mid, Clyde, Tweed) and 6 lake pockets. Beds sit at 9.91-11.17 m, mostly above the 10.0 waterline, so carving means lowering beds by up to ~1.2 m. Inland below-10 pockets: 19 of >= 25 m^2, all shallow (max 0.53 m); Lough Neagh is the only compact one over 500 m^2.

NOT found (do not invent): Nore, Slaney, Lagan, Forth, Tay, Dee, Annan/Nith. The Spey upper course drains the wrong way (SW into the Glen) across a ~24 m wide divide saddle: open decision.

The v13 carve built 9 systems (27,989 v / 33,225 f), g5 -202 for Irish and -1 for Scottish units, 1 ford inserted, no river component left without sea connection.

Related: [[dadg-main-map-geometry-and-protected-england-faces]]
