---
name: scottish-prefab-library-rollout-and-compaction
description: Chain of Scottish prefab work (library, siegeable shells, rollout, compaction, layout v3) with commits, hashes and review catches.
type: incident
topic: scotland
tags: [scotland, prefabs, outcome]
sources: [sdd/scottish-campaign-prefabs, sdd/scottish-siegeable-prefab-shells, sdd/scottish-prefab-rollout, sdd/scottish-prefab-compaction, sdd/scotland-layout-v3]
updated: 2026-10-18
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
