---
name: dadg-disabled-english-hideout-camps
description: English hideout camp models can remain visible after their settlement definitions are commented out; coastal pirate culture also prevents land-hideout spawning.
type: incident
topic: map-settlements
tags: [hideouts, settlements, campaign-map, bandits]
sources:
  - DellarteDellaGuerraMap/ModuleData/settlements.xml
  - DellarteDellaGuerraMap/SceneObj/Main_map/scene.xscene
  - TaleWorlds.CampaignSystem 1.5.7 BanditSpawnCampaignBehavior.IsBanditFaction
updated: 2026-11-27
---

An English camp model on the campaign map does not establish that a hideout exists in campaign data. Ten authored hideouts had matching scene entities but fully commented settlement definitions: forest 2-5, seaside 2-4, and mountain 2-4.

The camp between Reading, Bracknell and Farnham Castle is `hideout_forest_4`, at (780.521, 171.095). Its `dadg_hideout_camp` scene child retains `wm_hideout`, `Town Entity Manager`, and hideout raycast physics. The missing active settlement definition explains why the visible tents were not interactive.

Restoring coastal definitions with their original `sea_raiders` culture is insufficient. Native 1.5.7 `BanditSpawnCampaignBehavior.IsBanditFaction` excludes clans with naval navigation and cultures with `CanHaveSettlement == false`. DADG's sea-raider culture disables settlements and its War Sails clan uses the naval pirate template. Restored coastal land camps can instead use the existing `forest_bandits` culture while retaining `Hideout_pirate_camp` and the authored DADG prefab.

Native spawning chooses a subset of eligible hideouts under its normal population cap. An enabled site need not be occupied immediately after reloading a campaign. Newly added settlements in an existing save also need their default visible state distinguished from discovery state; new-game hideout hiding runs in `Hideout.OnInit`, via `Settlement.OnGameCreated`.

Related: [[dadg-map-capsule-naming-and-scotland-positions]], [[dadg-navmesh-backport-london-hideout]]
