---
name: dadg-vanilla-override-pattern
description: How DADG replaces vanilla kingdoms/clans/settlements - pre-XSLTs strip ALL vanilla first, so vanilla ids (sturgia/vlandia/battania) are safely reused; append to the single registered dadg_*.xml per type
type: reference
topic: map-settlements
tags: [xslt, kingdoms, clans, settlements, total-conversion]
sources: [memory/dadg-vanilla-override-pattern.md]
updated: 2026-10-18
---

# DADG vanilla-override pattern

DADG (DellarteDellaGuerraMap) total-converts factions/settlements via **pre-XSLT strip + real-XML add**, registered in `DellarteDellaGuerraMap/SubModule.xml` `<Xmls>` (each type loads the `dadg_pre_*` transform BEFORE the real `dadg_*.xml`):

- `kingdoms/dadg_pre_kingdoms.xslt` = identity copy plus `<xsl:template match="Kingdom"/>` deleting EVERY vanilla kingdom; then `kingdoms/dadg_kingdoms.xml`.
- `clans/dadg_pre_clans.xslt` (`match="Faction"`) then `clans/dadg_clans.xml`.
- `dadg_pre_settlements.xslt` (`match="Settlement"`) then `settlements.xml`.
- Same for heroes (`dadg_pre_heroes.xslt`) and NPCCharacters (`dadg_pre_npccharacters.xslt`).

**DADG reuses vanilla faction ids safely:** `id="sturgia"` = House of Lancaster, `id="vlandia"` = House of York, `id="battania"` = Lordship of the Isles (Scotland work). Nothing vanilla leaks in; the DADG file redefines the id fresh.

To add a faction/settlement: APPEND to the existing registered `dadg_*.xml` (one file per type), not a new file. Namespaced ids (`dadg_sco_*`) avoid collisions. See [[scotland-population-project]].

**Kingdom culture caveat:** DADG's `Culture.battania` has a null `DefaultPolicyList`, so a kingdom with `culture="Culture.battania"` crashes on load ([[reused-culture-needs-complete-data]]). Lancaster, York and the Scotland kingdom use `Culture.empire`. Clans/settlements may still use `Culture.battania`.

Generic rule: [[crafting-usage-vs-bench-list-rules]], [[map-settlement-position-two-files]], [[ws-sail-cloth-params-frozen]]
