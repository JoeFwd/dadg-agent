---
name: scottish-prefab-library-rollout-and-compaction
description: Chain of Scottish prefab work (library, siegeable shells, rollout, compaction, layout v3) with commits, hashes and review catches.
type: incident
topic: scotland
tags: [scotland, prefabs, outcome]
sources: [sdd/scottish-campaign-prefabs, sdd/scottish-siegeable-prefab-shells, sdd/scottish-prefab-rollout, sdd/scottish-prefab-compaction, sdd/scotland-layout-v3]
updated: 2026-11-21
---

# Scottish prefab library rollout and compaction

Status: integrated into the DellarteDellaGuerraMap repo.

- Siegeable shells: map commits a1a1a64 and 675a7fb.
- Rollout: d83adab.
- Compaction: 5601a09, f0892a5, 804bc08, c86a55c; final scene SHA `772ac2c1...`, prefab SHA `2341a149...`.
- Layout v3: settlements SHA `62A17DC5...`, scene SHA `0DF5ED9B...`.

Final-review catches on the siegeable shells (branch codex/scottish-siegeable-prefabs, base e8116d2, tip 790162a): the preview card top was at z=0 but the script and report claimed 0.015 (cube centre -0.12, scale 0.12), which hid or exposed foundations by ~0.022 local units; and the prefab guide lacked the concrete Town/Castle shell inventory (map_settlement_circle, town_wall, four bo_town vs three bo_castle colliders, castle gate tags). Compaction Task 2 ended as commit a8cf913 on top of ec50b48: 888 generated-art groups replaced across 179 Scottish roots (16 major burgh, 27 stone castle, 17 abbey, 2 lesser burgh, 12 kirk, 105 fermtoun), 2,101 rigid root moves, 180 outside byte spans identical. Status DONE_WITH_CONCERNS: native physics/navigation and live runtime unverified.

Review catches: abbey west range detached after compaction (fixed to within 0.15); 145 collision roots left unmoved though the report said moved; shell preview ground did not match prefab-local ground; layout deployment hit a Windows atomic replace failure (use one-use swap backups).

Related: [[settlement-shell-prefab-structure-rules]], [[xscene-byte-preserving-span-edits]], [[scotland-population-project]], [[map-settlement-position-two-files]]

Generic rule: [[raycast-collision-roots-must-follow-relocated-art]]

## Grounding, courtyards and urban interiors — 2026-11-21

Installed in the v1.4 map module, uncommitted: 118 root-Z corrections, 73 small
same-land-body coastal nudges (maximum3 units), scene/settlement XML kept in sync.
125 port/drop-off/blockade marker world frames countertransformed and verified.
Terrain/navmesh/prefab libraries unchanged. Compaction retained old donor decals:
864 obsolete leaves removed,42 inset sturgia courtyards kept, all selection
circles preserved. Sixteen actual Town interiors now use11 existing Native urban
frontages, inn, market props and retained kirk;171 measured plan-clearance checks
pass. Individual terrain fitting adjusts288 decorative mesh heights without
changing wall/gate/siege shells or XY. No royal-status reclassification.

GABS fresh-process `politicalmap` load:177 Scottish scene roots agree with XML
and installed candidate; max root-ground error .068825. All16 urban interiors
and42 courtyards loaded. Last height-only pass previewed live and persisted:
288 fitted meshes match target world Z exactly, max native-ground error .044477.
Final scene SHA256 `5da5cd78dd028ab7302a360301da6384da3ce25e8d0b2aa1906f3b22fa862835`.
Source/evidence: Core `tools/scottish_prefab_grounding/` and
`runtime-evidence/scottish-prefab-grounding-20261121.feature.md`.

Limits remain:26 island/coastal footprints deferred; some village field edges
still intersect water/uneven ground despite correct root origins. Berwick's
different root is absent in the tested save and unchanged. No siege/performance
verification. Expanded interiors cost additional mesh leaves. Root-height
success alone must not be reported as complete footprint grounding.

## Foundation and flowmap correction — continuation 2026-11-21

The original root-height pass buried Native Battanian houses: their origins are
partway up the walls (`mi_bat_house_a` minimumZ=-.3064). Use actual exported LOD0
foundation vertices, never an origin-only village check. The continuation
expands only pure decorative merged leaves:4,061 parts in135 Scottish villages,
with existing source transforms and all functional/level structure protected.
126 physical houses receive small within-hull nonoverlapping XY improvements;
11 steep houses use narrower existing cottages with total height preserved.
Crawford is visibly above ground after a fresh load. Some coloured striped
patches really are separate donor crop decals; do not infer roofs from them.

The26 deferred building footprints now fit their existing land bodies:
24 additional root/XML nudges(max2.916),49 shoreline world frames retained;
Kirkevaag/Kisimul complete fortified roots uniformly scaled.6,388 descendant
frames proportionate. Pitsligo/Portmahomack use explicit small-cottage overrides.
Native8,543actual-hull probes are dry(min10.02). An older padded probe below
water is.381outside Weaver's installed geometry. Terrain/navmesh unchanged.
Native positions of4,417 expected mesh instances agree within.000123;
177roots agree with XML,max native root error.04973. Berwick remains absent.
Sixteen Towns now have larger visible churches. One Abergeldie cottage retains
a.220downhill foundation gap; rigid slope fitting is not universally exact.

Courtyard snow must follow existing snow_flowmap_texture/global season factors
and existing political-map suppression. Assigning deferred_decal_worldmap to a
Decal component reports the shader but stays green in game. Proven fix:
ScottishCourtyardSnow clones deferred_decal_material_worldmap, copies sturgia
texture slots0/2/4, uses native decal_mesh unitbox with args(1,1,0,0), terrain-only
flags, and hides the original Decal. Native winter preview and Kingdom→Off
toggle show courtyard snow disappearing/restoring with terrain. No manual date
whitening or new TPAC/RDC material. Production Release build passed0errors.

Tools/evidence:Core tools/scottish_prefab_grounding, especially continuation.py,
village_fit.py,coastal_refine.py,SNOW.md. Final fresh-production-load evidence is
recorded separately from the earlier origin-only report. Campaign visuals and
mask checks do not establish siege operation or performance.

Continuation completed:168donor farm decals share72dry plots across24villages;
5,832native crop probes min10.0767.12narrow-cottage substitutions total, including
Abergeldie90%-height cottage removing its prior.220gap. Native foundations still
meet slopes unevenly(max gap.22875,burial.24223 across617village houses).

User's blurry roofs were NOT C houses. Runtime hide isolation proved D
north_frontage_4/south_frontage_3. Five `mi_vla_house_d.lod[1-5].1` meshes carry
hideout material despite correct LOD0Arabic roof UVs. Restore only those five
to native arab_map_icons on isolated deep copies; preserve the other14parts.
ScottishBurghRoof attaches to32houses. Fresh-load audit:32initialized,
160fixedLODs,0wrong/othermaterialchanges,sharedNative5LODrefs unchanged.
Correcttiles and winter snow verified. No new texture/TPAC/RDC needed.
Finalscene366b8270caceb65952ac2043bbe14fb75b6fc5d8ede25a1904162865ebead44c;
latest evidence runtime-evidence/scottish-prefab-foundations-flowmap-20261121.feature.md.

Rampart LOD continuation: native wall_2s has149faces atLOD0–3,36atLOD4;
mini_gatehouse_2 has1698atLOD0–3,122atLOD4–5. Runtime experiments proved
MetaMesh.SetLodBias(-2) retains coping/crenellations at camera30/50 while
preserving distant simplification. Prefer this to forcing maxLOD3. Attach
ScottishFortificationLod only to3178decorative wall/gate leaves across42roots,
including exclusive wall levels. This avoids a local/reference-assembly
GetChildrenRecursive strong/weak entity signature mismatch. No per-frame work.
Fresh-load audit:42roots,3178scripts/uniqueMMs,0wrongtargets,0geometry/material/
LODmaskchanges. Roof audit still32initialized/160corrected. Finalscene
7020a3dd295545a14e376315030456a377444b5fec6bdb971f1e259396da7630.
Evidence: runtime-evidence/scottish-rampart-lods-20261121.feature.md. An extra
camera check later hit a debugger pause and the test process ended; successful
Inverness production screenshot175027 and audit precede it. No performance
benchmark or siege verification claimed.
