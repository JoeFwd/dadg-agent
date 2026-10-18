---
name: dadg-scottish-1471-banner-corrections
description: The 2026-09-19 pass that rewrote Scottish kingdom/clan banner keys in poc.config.json for 1471 accuracy, including a CC BY flame icon for MacLeod of Lewis, and the checks used.
type: reference
topic: scotland
tags: [banners, scotland, poc-config, heraldry]
sources: [src/.tmp/apply_scottish_1471_corrections.py, src/.tmp/verify_scottish_1471.py, src/.tmp/verify_macleod_flame.py]
updated: 2026-10-18
---

# Scottish 1471 banner corrections

- Scope: 12 `clanBanner`/`kingdomBanner` paths in `../DellarteDellaGuerra/config/poc.config.json`: kingdoms Lordship of the Isles and Crown of Scotland; clans MacDonald of the Isles, MacKenzie, MacLean, MacLeod of Lewis (Isles) and Stewart, Douglas of Angus, Crichton, Halyburton, Home, Ruthven (Crown). The applier makes a timestamped `.bak_1471_*` backup; the verifier diffs current vs backup and expects only those 12 paths to differ.
- The verifier also asserts none of the dead banner-icon ids {40,128,129,132,140,141,144,145} are used ([[banner-party-palette-mismatch]]).
- Keys follow the banner key format ([[banner-key-format-and-32-layer-cap]]); the 1471 John MacDonald banner is a long multi-layer key on base icon 505.
- MacLeod of Lewis flame: new charge in `AssetSources/ui/custom_banner_icons_03.psd`, tile (3,2) of 512 px = icon 135; verified by composite readback (<= 2 changed pixels, max channel delta <= 3). The source SVG is CC BY 4.0, so `CREDITS.md` must carry the attribution (checked by the verify script).
- poc.config.json overrides XML banners wholesale ([[poc-overrides-english-clan-banners]]).

Related: [[banner-icon-atlas-editing]]
