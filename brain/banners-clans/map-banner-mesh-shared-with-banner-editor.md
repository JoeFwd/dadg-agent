---
name: map-banner-mesh-shared-with-banner-editor
description: The vlandia_tier_1_banner mesh is shared by the map party banner and DADG's banner editor scene; the 2x map override is compensated by entity scale 0.754 in the editor scene
type: reference
topic: banners-clans
tags: [banner, mesh, editor-scene, scale, vlandia_tier_1_banner]
sources: [memory/map-banner-mesh-shared-with-banner-editor.md]
updated: 2026-10-18
---

# Map banner mesh shared with the banner editor

The DADG map override `DellarteDellaGuerraMap/Assets/ui/vlandia_tier_1_banner_geo.tpac` (2x larger, commit `385d136`) has exactly two users:
- the map item `campaign_banner_small` (hardcoded by MobilePartyVisual; kept by the whitelist in `dadg_pre_native_items.xslt`, every other vanilla banner is stripped);
- `DellarteDellaGuerraScenes/SceneObj/banner_editor_scene/scene.xscene`, entity tagged `banner`, which places the mesh directly (no item, no prefab).

On 2026-09-27 the editor entity scale went from 1.507 to 0.754 on all three axes to compensate. The mesh was doubled in X as well as Z, so a Z-only halving still looked too big and wide. Live-verified and approved.

Not done: duplicating the mesh (unwanted); an item `prefab=` does not help since no prefab named that exists (the item draws from `mesh=`); whether a real prefab would replace the mesh on the map was never live-tested.

**How to apply:** if the map banner mesh is resized again, rescale the editor entity to match (1.507 / new factor).

Related: [[banner-icon-atlas-editing]]
