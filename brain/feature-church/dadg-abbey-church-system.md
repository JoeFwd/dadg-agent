---
name: dadg-abbey-church-system
description: DADG abbeys are Villages tagged in Core config/dadg.church_settlements.xml; each diocese needs exactly one Cathedral or the church feature silently deactivates; the system lives on UNMERGED feature/add-church
type: reference
topic: feature-church
tags: [church, abbey, diocese, config, unmerged]
sources: [memory/dadg-abbey-church-system.md]
updated: 2026-11-03
---

# DADG abbey / church system

The abbey is not a new settlement type ([[settlement-component-types-no-custom-type]]): it is an ordinary **Village** in `settlements.xml`, styled with abbey name/mesh, then **registered by id** in Core `config/dadg.church_settlements.xml`. `ChurchSettlementsXmlProvider` loads it; `ChurchSettlements.cs` maps id to kind (Abbey/Priory/Cathedral), driving abbot/prior/bishop titles and behaviours (notable abbot, donation, tithe/mass, sanctuary, bishop favour, pilgrimage). Mechanically a Village: market via bound town, no garrison, not besiegeable, production from `village_type`; wealthy vs estate = `hearth` (750 vs ~300).

**Config shape:** `<ChurchSettlements>` > `<Diocese id name>` > `<ChurchSettlement id kind [shrine="true"]>`. **Load-bearing: each Diocese MUST contain exactly one Cathedral or the whole church feature silently deactivates** (`ChurchSettlementsXmlProvider.Validate`). Diocese ids unique; a settlement in one diocese only; kind in {Abbey,Priory,Cathedral}; every id must exist in settlements.xml.

**Merge status (2026-07-31):** entirely on Core branch `feature/add-church` (~10 commits, ~7000 lines: domain ChurchSettlementKind/Data/ports, provider + models, ChurchSettlements.cs, behaviours ChurchCampaignBehavior/AbbotDialog/tithe/mass/sanctuary/pilgrimage, ChurchSaveableTypeDefiner, DI wiring in `DadgServiceContainer.cs`/`SubModule.cs`, config). **NOT merged into develop.** The Map `feature/add-church` branch is unrelated (priest robes only). Core config ships only 16 English church settlements; Scots abbey Villages (`dadg_sco_iona_abbey_and_nunnery`, `_saddell_abbey`, `_oronsay_priory`, `_old/new_fearn_abbey`) exist on the Map but are not yet in the config.

**Impact on [[scotland-population-project]]:** the 14 planned abbeys are abbey-styled Villages bound to a nearby fort (not clan seats, excluded from claiming villages). Real church mechanics need merging/porting `feature/add-church` AND grouping the 14 into dioceses each with one Cathedral (e.g. St Andrews). Without it they are villages with abbey names. Scope decision for the user.

## St Andrews ownership deferred, 3 November 2026

The user explicitly deferred St Andrews to the church branch during the spring-1471
ownership audit. Preserve `dadg_sco_st_andrews_town` owner `clan_lindsay` and the
`county_fife` regional title placeholder `clan_stewart` for this pass. Neither is
historical episcopal ownership. Patrick Graham was **bishop** in early 1471;
archbishop belongs to 1472. Do not create a hereditary Graham estate to replace
the missing institution. The exact mismatched pair is temporarily pinned in
`StartingOwnershipOverRealContentTests`; remove/revise that exception when church
ownership and succession are implemented.

Handoff: Core `doc/church-st-andrews-1471.md`, with evidence and acceptance work for
`feature/add-church`'s `doc/church-v0.4-bishops-and-favour.md` and
`doc/church-v0.6-diocese-view.md`. The secular audit corrected the other 26 mismatches
and added Douglas of Lochleven; it did not solve the church estate.
