---
name: dadg-editor-material-warning-audit
description: Read-only audit of 115 editor material warnings; 108 Scottish submeshes reference two Scenes materials from Map, with separate empty primary bindings and ship secondary references.
type: incident
topic: scenes-navmesh
tags: [editor, materials, tpac, module-order, scottish-map, ships]
sources: [user popup transcript 2026-11-13 20:56-20:57, installed TPACs inspected with TpacTool.Lib, installed Map and Scenes SubModule.xml, tools/scottish_model_optimisation/native-v6-final-audit.json]
updated: 2026-11-13
---

# Editor material warning audit

The supplied 115 `Unable to find material for mesh` warnings include several different binding problems. They are not 115 independently missing material files.

Read-only inspection of the installed TPACs established:

- 108 Scottish submesh warnings across 14 merged metameshes: 66 primary references to `dadg_map_icons_01` (`7cf0d846-6245-4186-ba0b-9b2c2f9e1c99`) and 42 to `objects_a` (`19e3f691-be23-4bdf-8d5a-0bb3eb160136`). Both material definitions exist under Scenes/Assets, while the geometry is Map/Assets/scottish_campaign/dadg_scottish_merged_v3_geo.tpac. Every affected part repeats across LOD0-5.
- Scenes depends on Map, and the previous editor session log loads Map before Scenes. A forward material dependency is the leading explanation for these 108 warnings; no relaunch/order experiment was performed. The earlier native-v6 audit verified these material GUIDs as existing, but did not establish a warning-free fresh editor startup.
- Map's `dadg_ws_english_boat_b_canvas_01` primary material is Scenes' `sails_plain` (`4eacf4ac-9cbc-4d83-9c71-45087e4fb322`). The two `dadg_ws_english_boat_b_sail_rig_static` parts have valid Map primary aliases but retain Scenes secondary GUIDs for `sho_rope` and `plank_fine_a`. The popup does not identify the failing slot; do not claim the rig primary materials are absent.
- Main content's weapons/override/spear_guard_replace_geo.tpac overrides `spear_banner_12`, `spear_blade_8`, and `spear_handle_25` with empty primary GUIDs. The first two have zero vertices/faces (possibly intentional suppression); the handle has 1,297 vertices and 1,301 faces. Native core_game.tpac has nonempty primary bindings for all three.
- Main content's cannons/cannons_geo.tpac has an empty primary GUID on `dadg_siege_falconet_mantlet.1`, with 1,226 vertices and 624 faces.

Also found independently: Main content's Assets/shields/burgundian_a_mtl.tpac is 259 bytes of unresolved Git LFS pointer conflict text (`<<<<<<< HEAD` / `>>>>>>> add-new-clothing`), not a TPAC. The preceding editor session logged an invalid package warning under Assets/shields. This is separate from the 115 supplied material warnings.

Potential repair: put shared material ownership in an earlier common module and rebind dependent meshes through the editor; inspect empty primary slots while preserving intentional empty overrides; clean obsolete ship secondary bindings. Simply reversing Map and Scenes conflicts with Scenes' declared Map dependency. No asset edits, cache regeneration, or live visual verification were performed during this audit.

Related: [[dadg-ws-ship-reimport-state]], [[reimport-keeps-second-material]], [[tpac-material-binding-trailer]]
