---
name: dadg-lord-defection-sources
description: Why DADG clans change realm - day-1 vanilla random lord relations plus Honor -1 leaders, not DADG code; see doc/lord-defection-analysis.md
type: incident
topic: feature-other
tags: [defection, relations, kingdoms, analysis]
sources: [memory/dadg-lord-defection-sources.md, doc/lord-defection-analysis.md]
updated: 2026-10-18
---

# DADG lord defection sources (analysis 2026-10-13)

DADG has only two code paths moving a clan between realms: the claim award (`ClaimPressureCampaignBehavior.AwardTheClaim`, only on a cross-border attacker win) and cadet-branch creation. Neither explains realm switching seen in `saveauto3`.

- **Evidence:** across all dadg logs only one private war ended in an attacker win (Paston over Beauchamp, inside one realm). Over ~350 days, 10 lords switched anyway: 7 York to Lancaster, 3 Lancaster to York, plus Home from Scotland to the Isles.
- **Cause:** vanilla `DiplomaticBartersBehavior` defections (mechanics in [[vanilla-clan-defection-and-relation-drains]]). DADG seeds and changes no relations.
- **Root cause (2026-10-13):** vanilla `CharacterRelationCampaignBehavior.UpdateFriendshipAndEnemies` randomises lord-to-lord relations at new game with `SetPersonalRelation` (no event). DADG's small map, tier >=5 clans and the ruler square-root mean nearly every leader-to-own-ruler pair rolls, about half negative. 16 of 36 clan leaders have Honor -1 (reliability 0.3) and leave at about -40 rather than -75. Live: Crichton left at -93 and Lovell defected at -22 within 2 weeks with zero logged relation changes before.
- **Correction (same day):** in a second run Stafford defected at +34 and Fitzalan at -1. `ConsiderDefection` is a purchase (see generic note). All 4 English defections went vlandia to sturgia.

**How to apply:** diff `super_faction` in `DellarteDellaGuerraMap/ModuleData/clans/dadg_clans.xml` against a live kingdom-to-clan snapshot; `Clan.LastFactionChangeTime` dates each move. Vanilla logs no defection notices to rgl; the CustomSpawns DailyLogger records detail but is not loaded in DADG runs; log `OnClanChangedKingdom` (FeudalHierarchyAdapter) to see which detail fired. GABS `hero.get_relationships` is broken (always returns the player).

Full formulas and fix options: `doc/lord-defection-analysis.md`.

Related: [[vanilla-clan-defection-and-relation-drains]]
