---
name: dadg-map-capsule-naming-and-scotland-positions
description: DADG naming for settlement capsules in the Main_map scene, and the verified invariant across 160 Scotland settlements
type: reference
topic: map-settlements
tags: [settlements, capsule, scotland, main_map]
sources: [memory/map-settlement-position-two-files.md]
updated: 2026-10-18
---

# DADG map position specifics

Files in `DellarteDellaGuerraMap`: `ModuleData/settlements.xml` and `SceneObj/Main_map/scene.xscene`. The capsule entity is named `campaign_icon_capsule_dadg_region_<settlement_id>`; its child entity is named `<settlement_id>`. The position invariant held to 1e-13 across all 160 Scotland settlements. Rules and gotchas (BOM, z): [[map-settlement-position-two-files]].

Related: [[scotland-population-project]]
