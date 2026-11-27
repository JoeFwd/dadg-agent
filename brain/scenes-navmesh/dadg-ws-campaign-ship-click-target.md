---
name: dadg-ws-campaign-ship-click-target
description: Root prefab correction for unclickable DADG ships: consolidate detailed physics and visual mesh on body_mesh while preserving both geometry frames.
type: incident
topic: scenes-navmesh
tags: [war-sails, ships, campaign-map, selection, prefab]
sources: [2026-11-27 WarSails GABS and Rider session, DellarteDellaGuerraMap NestedPrefabs and Tools/WarSailsShips/assemble_gameplay_roots.py]
updated: 2026-11-28
---

# DADG campaign ship click target

All three live ship prefabs had `body_mesh` on a render-only hull while the detailed collision was on a separate sibling. War Sails reads physics bounds on the tagged entity without including children, yielding a zero-size selection capsule for the cog caravan.

Reproduced against `caravan_template_empire_1`, Convoy of Emma the Wool Weaver, flagship `dadg_ws_kogge`, at approximately `(502.393, 370.4304)`. The party was visible, at sea, not in raft state or transitioning, and its naval root was registered for selection. Tagged-hull physics bounds were zero. A temporary capsule on its strategic root restored hovering and selecting, confirmed by the user; the native log also recorded a subsequent Caravan Master conversation.

The persistent fix moves each existing detailed `physics` block into its tagged visual hull in `NestedPrefabs/dadg_ws_{kogge,carrack,english_boat_b}_ship_nested/mesh_holder.xml` and removes the old `dadg_ws_*_detailed_collision.xml` sibling. The hull entity becomes identity; its old Z translation moves to the metamesh component (`-0.8`, `-1.4`, `+0.15` respectively), preserving rendered vertices and the already-shifted detailed collision. Shape names, materials, batching, other entities and instance GUIDs remain unchanged. `Tools/WarSailsShips/assemble_gameplay_roots.py` now generates and checks this structure.

Validation: all three active prefabs and three newly generated drafts passed targeted checks. Pre/post semantic comparison permitted only physics relocation and the equivalent visual-frame change. The full generator self-check still fails its unrelated climber `standing[1]` assertion; the unmodified baseline reproduces the same failure. No C# patch or compiled-asset edit was introduced.

Fresh-process validation is pending. Saving the live fixture failed with ButterLib's `ConcurrentDictionary<MBObjectExtensionDataStore.DataKey, object>` type-definition error, so the live campaign was preserved rather than restarted. The diagnostic click capsule applies only to the current convoy visual and can be lost when it refreshes. The permanent prefab changes load on the next process launch. Evidence and original files are under Core `src/.tmp/ship-click-root-fix/`.

Related: [[ws-campaign-ship-selection-requires-body-mesh-physics]], [[dadg-ws-custom-ships-conversion]], [[dadg-ws-kogge-carrack-deck-navigability]]
