---
name: dadg-banner-palette-remap-applied
description: FIXED 2026-09-12 - dead bannerlord.party colour ids remapped in DADG's dadg_clans.xml (48 English clan keys, 1358 substitutions); invisible on screen while POC is active
type: incident
topic: banners-clans
tags: [banner, palette, clans, fixed]
sources: [memory/banner-party-palette-mismatch.md]
updated: 2026-10-18
---

# Palette remap applied to DADG clans (FIXED 2026-09-12)

Fixed in `../DellarteDellaGuerraMap/ModuleData/clans/dadg_clans.xml`: 48 English clan keys, 1358 substitutions (141->138 x745, 145->142 x311, 140->139 x266, 40->172 x28), and in `CalradiaAtWar/**/CustomFactions.xml` (11 of 21 keys). DADG's 35 Scottish clans were authored against game ids and needed no change.

Caveat: the English XML fix is not visible on screen while POC is active, see [[poc-overrides-english-clan-banners]].

Generic rule and remap table: [[banner-party-palette-mismatch]].
