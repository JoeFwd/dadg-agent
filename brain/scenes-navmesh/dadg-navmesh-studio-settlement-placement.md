---
name: dadg-navmesh-studio-settlement-placement
description: DADG settlement-placement specifics of the navmesh studio - footprint radii town 8.475 / castle 3.572 / village none; only dadg_sco_* movable; water oracle height > 10.0
type: reference
topic: scenes-navmesh
tags: [navmesh-studio, settlement, footprint, scotland]
sources: [memory/navmesh-studio-tool.md]
updated: 2026-10-18
---

# Settlement placement in the studio (DADG)

Tool: [[navmesh-studio-tool]]. Footprint radii: town **8.475**, castle **3.572**, village none (`/api/entities` gives villages no radius, so `land_fraction` is always 1.00 for them). Authoritative position = settlements.xml posX/posY; the scene capsule `campaign_icon_capsule_dadg_region_<sid>` holds a derived offset ([[map-settlement-position-two-files]]). Only `dadg_sco_*` are movable. Water oracle: on_land = height > 10.0.

Examples of scene dirs: `DellarteDellaGuerraScenes\SceneObj\Framlingham_castle`, `DellarteDellaGuerraMap\SceneObj\Main_map`. Related: [[framlingham-navmesh-hole]], [[scotland-population-project]]
