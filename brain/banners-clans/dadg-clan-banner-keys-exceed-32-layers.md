---
name: dadg-clan-banner-keys-exceed-32-layers
description: 36 DADG clan banner keys exceed 32 layers (worst 488) and now render in full on 1.4.7+ singleplayer; where the worked heraldry docs live
type: reference
topic: banners-clans
tags: [banner, clans, layers]
sources: [memory/banner-key-format-and-32-layer-cap.md]
updated: 2026-10-18
---

# DADG clan keys over the 32-layer cap

**36 clan keys in `dadg_clans.xml` exceed 32 layers** (worst: `clan_morley`, 488 layers) because compound charges are built from primitives: a cross pattee is 8 layers, a cross crosslet 6, so a coat of ten crosses needs 80. On 1.4.7+ these render in full in the campaign. They would not network-serialise in multiplayer.

Worked examples with blazons and codes: `src/doc/scottish-clan-heraldic-banners.md` (35 armorial coats, 3-12 layers each); `src/doc/scottish-clan-tartan-banners.md` is the superseded tartan set.

Generic rules: [[banner-key-format-and-32-layer-cap]]. Related: [[dadg-vanilla-override-pattern]]
