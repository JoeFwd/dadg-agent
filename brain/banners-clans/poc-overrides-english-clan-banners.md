---
name: poc-overrides-english-clan-banners
description: POC's clanBanner in poc.config.json wholesale-replaces the XML banner for all 55 English clans and is 54/55 stale, so heraldry edits to York/Lancaster clans are discarded at runtime; Scottish clans are protected only by accident
type: incident
topic: banners-clans
tags: [poc, banners, clanbanner, config, palette, heraldry]
sources: [memory/poc-overrides-english-clan-banners.md]
updated: 2026-10-18
---

# POC overrides English clan banners

`Modules/DellarteDellaGuerra/config/poc.config.json` carries a `clanBanner` for **all 55 English clans** (33 York + 22 Lancaster), keyed by clan **display name** (ordinal, case/whitespace-sensitive). `CampaignSnapshotFactory.cs:148` -> `CampaignStateWriter.cs:57` calls `Clan.SetBanner(clan, new Banner(...))`, a **wholesale replacement** of the banner from `dadg_clans.xml`. The config is **54/55 stale** (34 with a different layer count), so every heraldry edit to a York/Lancaster clan in XML is silently discarded in game. Edit both, or delete the `clanBanner` values. The override is invisible (XML looks authoritative, no log line).

Other keys: `kingdomBanner` replaces the kingdom banner; `primaryColor`/`secondaryColor` set `Clan.Color`/`Color2` and recolour the live banner in place; `mode` is a troop colour strategy with no effect on clan banners; `BearRulerBanner`, `BearRulerColors`, `BearRulerShield` are parsed but never consumed on the campaign clan path.

**Absent clans are protected:** they fall to `defaultConfig`, and with `"FollowKingdomColors": "false"`, `PlanCampaignBannerUseCase.cs:15` passes `bannerCodeToRestore: policy.CachedBannerCode` and POC's postfix on `Clan.UpdateBannerColorsAccordingToKingdom` re-restores the XML banner; that is why the 35 Scottish clans keep their keys. Ruling clans are exempt (`CampaignSnapshotFactory.cs:68`).

**The Scottish safety is accidental:** native `UpdateBannerColorsAccordingToKingdom` would wipe a key's colours, but `ChangePrimaryColor`/`ChangeIconColors` no-op when `BannerManager.GetColorId(color)` is -1. Neither Scottish kingdom colour is a palette colour (`FF1F5C1F`/`FFF2E9C9` Isles; `FFF0C848`/`FFB0202A` Crown). York's and Lancaster's `FFFFFFFF` ARE palette id 172, the reason POC is needed at all. Change a Scottish kingdom colour to a palette value and all 35 lose their tinctures at load.

**Dead code:** `PocConfigReaderOverriderPatch.cs:40` resolves `PocColor.PocColorMod.OnGameInitializationFinished`, gone in POC v2.0.1 (`PocColor.PocColorSubModule`); TargetMethod is null and it logs "failed to find the config file path instruction" each launch. Harmless since v2's `LegacyConfigLoader` auto-discovers `poc.config(.json)` under `Modules` to depth 3.

POC applies [[banner-party-palette-mismatch]]'s remap to codes it writes (`BannerCodePaletteMigrator.MigrateV12PaletteIds`) but not to codes loaded from XML.

**How to apply:** before editing an English clan's `banner_key`, check for a `clanBanner` in `poc.config.json`.

Related: [[dadg-clan-banner-keys-exceed-32-layers]]
