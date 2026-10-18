---
name: scotland-map-border-fix
description: Northern Scottish settlements were unreachable by the camera because border_max Y was 750; raised to 1120 in the main map scene.
type: incident
topic: scotland
tags: [scotland, camera, border]
sources: [runtime-evidence/scotland-camera-pan-north-bound (2026-07-28)]
updated: 2026-10-18
---

# Camera could not pan north (FIXED 2026-07-28)

Live values were `border_max` (1000, 750) and height 620, so Dingwall (y = 925.9) was unreachable. Fix: edit the `border_max` entity position Y from 750 to 1120 in `../DellarteDellaGuerraMap/SceneObj/Main_map/scene.xscene` (about line 431925). Terrain, physics and flora already extended to 1120. Generic mechanism: [[map-border-entities-bound-camera]].

Related: [[map-border-entities-bound-camera]], [[scotland-population-project]]
