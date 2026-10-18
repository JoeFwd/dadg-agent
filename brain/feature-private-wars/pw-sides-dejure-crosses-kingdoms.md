---
name: pw-sides-dejure-crosses-kingdoms
description: Private-war side resolution walked the de jure title chain, and kingdom_england's king is clan_lancaster, so the whole York kingdom resolved onto Lancaster's side; adapter now cuts at kingdom borders (uncommitted 2026-10-11)
type: incident
topic: feature-private-wars
tags: [privatewars, warsideresolver, suzerain, dejure, supporters, cross-realm]
sources: [memory/pw-sides-dejure-crosses-kingdoms.md]
updated: 2026-10-18
---

# Private-war sides crossed kingdoms

`WarSideResolver` climbs `GetSuzerain` until it reaches a principal. `SuzeraintyPolicy` is purely de jure and `titles.config.xml` gives `kingdom_england kingClanId="clan_lancaster"`, so every English clan's chain ends at Lancaster, including clans of the in-game York kingdom at war with Lancaster.

Observed 2026-10-11 (Kenilworth war, lancaster vs clinton): York, Fitzalan, Grey of Ruthin and Stafford lords raised goal armies and besieged Kenilworth as Attacker; Lancaster-kingdom lords marched to DefendSettlement against them. The run-1 "third-party" goal handover likely had the same cause.

**Fix (uncommitted 2026-10-11):** `FeudalHierarchyAdapter.GetSuzerain` skips any liege whose `Clan.Kingdom` differs from the clan's own; revision bumped on `OnClanChangedKingdomEvent`.

**Not a regression (2026-10-13, run 3):** in Lancaster vs Fitzhugh the Isles joined through the SUPPORTER path: `Candidates` admits a clan of another realm if bonded to a principal (kin, or relation > 50); `WarSideResolver` stops at a supporter so its whole same-kingdom subtree follows; macdonald_isles is king of kingdom_isles, so the whole Lordship joined and Calder raised a goal army 4 s after declaration. Lancaster won the barony on paper but an Isles clan still holds the castle. Details: `doc/private-war-attacker-win-analysis.md`.

**Why hidden:** "side parties" diagnostics list only the principal's own kingdom, so cross-realm members were invisible; the only symptom was a siege leader missing from the list.

**How to apply:** when an actor shows up unexpectedly, resolve its side through the suzerain chain first.

Related: [[gathering-army-aibehaviorobject-not-target]], [[same-kingdom-mapevent-diplomatically-finished]]
