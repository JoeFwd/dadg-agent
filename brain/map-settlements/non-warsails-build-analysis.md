---
name: non-warsails-build-analysis
description: One DADG Map module that loads with and without War Sails - NavalDLC is an Optional dependency, and Core's NavalXmlSelector drops either the naval XMLs or the dadg_no_naval_* strip XSLTs from XmlResource before any merge. Committed 2026-11-25 on feature/no-warsails (Core + Map); live no-WS map load, water and caravans pass.
type: decision
topic: map-settlements
tags: [war-sails, navaldlc, build, packaging, map, xml]
sources: [DellarteDellaGuerraMap/SubModule.xml, DellarteDellaGuerraMap/ModuleData/settlements.xml, culture/dadg_cultures.xml, clans/dadg_clans.xml, 1.5.7 ModuleInfo.cs, LauncherModsVM.cs, XmlResource.cs, MBObjectManager.cs, Town.cs, Settlement.cs, CultureObject.cs, CaravansCampaignBehavior.cs]
updated: 2026-11-25
---

# Non-War Sails build: one Map module for both

Status: COMMITTED 2026-11-25 on `feature/no-warsails` in Core and Map. Spawns modules are out of scope.
Travel without WS is Codex's port-sea variant: `Modules/Scripts/non_warsails_navigation` (DADG Scripts repo) generates
`SceneObj/dadg_main_map_no_warsails` (sea faces turned into `Fording`, an opening at each of the 135
ports) and bakes `settlements_distance_cache_NoWarSails.bin`. Core's `CampaignNavigationSelector`
loads both when NavalDLC is absent and checks the cache's scene/navmesh CRCs. Regenerate with
`Scripts/non_warsails_navigation/GENERATE_CACHE.md` after every `Main_map` or `settlements.xml` edit.
An interrupted bake leaves `Modules/DADG.CrossingCacheBake` behind, and the next bake refuses to start
until it is deleted.

The user rejected a separate add-on module and asked for one Map module that works both ways. Core C#
was already NavalDLC-optional; all of the coupling was Map data.

## How it works
1. **Optional dependency.** Map `SubModule.xml` keeps
   `<DependedModule Id="NavalDLC" DependentVersion="v1.3.7" Optional="true"/>`. The native
   `ModuleInfo` reads `Optional`. `LauncherModsVM` neither auto-selects an optional dependency nor
   blocks when it is missing. When NavalDLC is present, the entry still orders it before Map, which
   matters because Map's pre-XSLTs strip NavalDLC's settlements, cultures and clans from the merged
   docs. BLSE metadata carries `optional="true"`.
2. **Selection in Core: `Naval/NavalXmlSelector.Apply()`**, the first call in
   `SubModule.OnSubModuleLoad`. `Module.LoadSubModules` fills `XmlResource.XmlInformationList` for
   every module before it loads any submodule DLL, and the merge (`MBObjectManager.CreateMergedXmlFile`)
   only runs when a game starts, so entries can still be removed (match `ModuleName` + `Name` = path):
   - **NavalDLC active**: drop the three `dadg_no_naval_*` nodes.
   - **NavalDLC absent**: drop the naval nodes:
     - `dadg_custom_mission_ships`, `dadg_custom_ship_hulls`
     - `characters/dadg_naval_characters`, `dadg_naval_party_templates`, `dadg_naval_items`
     - `dadg_naval_siegeengines`, `dadg_ship_upgrade_pieces`, `dadg_ship_slots`
     - `dadg_post_naval_ship_upgrade_pieces`
3. **Strip XSLTs, no-WS only.** Each is an XSLT-only XmlNode placed right after its main node, so it
   runs on the merged doc (same pattern as `dadg_post_naval_ship_upgrade_pieces`):
   - `dadg_no_naval_settlements.xslt` removes:
     - 27 `<Location id="port">`. Only NavalDLC adds `port` to `town_complex`, so
       `Settlement.Deserialize` NREs on `SetSceneName`.
     - 27 `building_shipyard`. `Town.Deserialize` dereferences the null BuildingType on a new game.
     - 135 `port_posX`/`port_posY`. These keep `HasPort` false. Otherwise `CaravansCampaignBehavior`
       asks for a template with `ShipHulls`, and none exist without the naval templates.
   - `culture/dadg_no_naval_cultures.xslt` removes, from 5 cultures:
     - `shipwright`, `shipyard_worker`, `fishing_party_template` and
       `settlement_patrol_template_coastal`
     - 10 `*_naval_caravan_template_*` caravan entries
     - 14 `available_ship_hulls` children
   - `clans/dadg_no_naval_clans.xslt` changes the sea_raiders clan's `default_party_template` from
     NavalDLC's `northern_pirates_template` to DADG's `sea_raiders_template`.

   Verified offline: I ran all three with lxml on the real files, and the counts above went to 0 with
   nothing else touched. A script scan of the DellarteDellaGuerra and Map XML found no other
   references to NavalDLC-only ids outside the dropped files.

Default if Core fails to load: both sets stay registered. With War Sails, the strips would then remove
the ports. This is acceptable because Map is unusable without Core anyway.

## Water plane and river: fine without WS (live 2026-11-25)
Screenshots from the no-WS run show the sea and rivers rendering normally, so no material swap is needed.
The analysis that came before the test:
- The Main_map `water_plane` entity (tag `snapped_water_body`, mesh `editor_plane_high`) uses
  `dadg_naval_worldmap_water`.
- The `river_script` `river_generator` uses `Material=naval_worldmap_river`.
- Both material tpacs live in Map (`Assets/ddg_mainmap/dadg_naval_worldmap_water_mtl.tpac`,
  `naval_worldmap_river_mtl.tpac`). They reference shaders and textures by GUID, and the targets are
  probably in NavalDLC's compressed `AssetPackages`. Offline it cannot be told whether they resolve
  without NavalDLC.
- Vanilla fallbacks are `worldmap_water` (SandBox, on `editor_cube`, argument `1.7,0,23.23,-0.3`) and
  `worldmap_river_mat`.
- If the sea renders wrong without WS:
  - Swap the `water_plane` mesh material at map scene load when NavalDLC is absent.
  - The river is generated at load from the variable, so either patch the material before generation
    or re-author the river material on a Native shader in the editor.
- The `water_flowmap` and `CampaignMapAmbientOccluder` scripts on both entities have no C# class in
  1.5.7, so they are probably engine-native and not DLC-gated. Confirm this in the same launch.

## Island travel (user's PoC; facts for reference)
- Base `DefaultPartyNavigationModel` allows only land types plus Bridge, Fording and Beach, so the
  islands are unreachable without WS.
- Vanilla only toggles faces temporarily (`Scene.cs` ~342-493, `updateIslandIndices:false`). A
  persistent toggle probably needs `true` and must be reapplied on every new game and every load.
- Distance cache: the last active module that has
  `ModuleData/DistanceCaches/settlements_distance_cache_<Type>.bin` wins. With a single module there
  is one Default cache for both variants. If the crossings change Default reachability, the cache has
  to be redirected at runtime (no second module can override it). Validity is CRC-of-files, so runtime
  toggles do not invalidate it.

## Live results (2026-11-25, `Standalone.NoWarSails`)
- PASS: naval XMLs are not loaded, and the new campaign reaches the map on the NoWarSails cache. The
  earlier crash came from an incomplete bake that stopped at index 137/139.
- PASS: water and river render.
- PARTIAL: 96 caravans moved over 6 days with no exceptions.
- PASS (later runs): London town menu has no shipyard. Island travel works both ways for the player
  and AI through port landings. WS regression passes (ports, shipyard, sailing).
- Kisimul (a castle on its own islet, no `port_pos`) was walled in. `build_port_sea.py` now gives
  every portless settled island one `landing_only` landing at the shore nearest its gate.
- Wall breach: an order to an unreachable point leaves `_pathMode=false`. Vanilla `DoAIMove` then
  steers straight at the target and accepts any step onto a face of the same island. The generated
  sea shares the land's island, so that step crossed the thin MOUNTAIN strip. After the crossing,
  `IsCurrentlyAtSea=true` sent the London encounter to NavalDLC's missing `port_menu` (an NRE in
  `MenuContext.HandleStates`). Fix in `CampaignNavigationSelector`, applied only without NavalDLC:
  - A `DoAiPathMode` postfix clamps the no-path target with
    `GetLastPointOnNavigationMeshFromPositionToDestination`.
  - The clamp is skipped when the party already stands on invalid terrain. Otherwise UnderBridge
    parties froze in place.
  - The `IsCurrentlyAtSea` setter is forced to false.
  
  Evidence for the fix is `runtime-evidence/no-warsails-island-travel.feature.md` (runs 3–4).
- The variant folder ships only `navmesh.bin`. Without NavalDLC, `CampaignNavigationSelector`
  copies the other `Main_map` files into it before `Scene.Read`, renaming the xscene root. Each copy
  keeps its source's write time, and a file is recopied whenever the two times differ. Verified live
  (run 5): the first load copies about 36 MB in about 5 s, and a reload copies nothing.
- A runtime navmesh swap (`ClearNavMesh` + `ImportNavigationMeshPrefab`) is unproven. The import is
  used only for mission prefabs (dynamic, ID-shifted faces). `SetNavMeshRegionMap` is applied before
  `Read`, and `SettlementPositionScript.OnInit` reads the cache and its CRC during `Read`.
- NOT YET: a raid and a battle.
- Noise that is not caused by this change: the EquipmentRosters.xsd `battle`/`siege`/`pool` errors
  appear in WS runs too.

## Verification plan
1. Deploy. The 2026-11-24 build compiled with 0 errors, but the copy failed because the running game
   had the DLLs locked.
2. Launch without NavalDLC. GABS and Rider are `Standalone.WarSails*`, so a non-WS profile is needed.
3. New DADG campaign:
   - `rgl_log` shows no XML/unresolved-reference errors.
   - Main_map water and river render.
   - A coastal town can be entered, has a build queue without a shipyard, and can be sieged.
   - A former port village can be raided.
   - Caravans spawn from a former port town.
4. Repeat with NavalDLC:
   - ports and shipyards are present
   - sea battles work
   - fleet sail orders work
   - the existing WS save still loads

Related: [[war-sails-main-map-migration-plan]], [[warsails-main-map-migration-contract]], [[dadg-vanilla-override-pattern]], [[bannerlord-xml-load-abort-semantics]], [[ws-open-sea-navmesh-stripped]], [[ws-fmod-sail-sound-hang]]

## FPS dip on unreachable targets (probe 2026-11-25)

Ordering the player to Ireland (unreachable without War Sails) drops fps 170 → 45-60, standing still included:
vanilla retries the failed path every frame ([[failed-party-path-retried-every-frame]]), and each failed A* over
the 31k-face generated sea costs ~11 ms (≈20 ms max, vs ≈3 ms worst with War Sails). The shore clamp
(`StopDirectMoveAtShore`) costs ~0.1 ms/frame and is not the cause. Not fixed yet.
