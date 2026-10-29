---
name: dadg-ws-hook-item-stripped
description: FIXED 2026-10-25 - DADG's dadg_pre_native_items.xslt stripped NavalDLC's "hook" item, causing the War Sails sea-battle FMOD hang; hook (plus burning_arrows/bolts and ship grapeshot) whitelisted
type: incident
topic: incidents-crashes
tags: [war-sails, fmod, hang, xslt, item-stripping, fixed]
sources: [memory/ws-fmod-sail-sound-hang.md]
updated: 2026-10-29
---

# DADG stripped the War Sails hook item (FIXED 2026-10-25)

`DellarteDellaGuerra/ModuleData/items/dadg_pre_native_items.xslt` drops every Item not on its allow-list. NavalDLC loads before DADG, so its `hook` item was removed, which caused the sea-battle FMOD hang described in [[ws-fmod-sail-sound-hang]].

Fix: `hook` added to the allow-list. Verified in 2 sea battles on 2026-10-25. The same pass also whitelisted `burning_arrows` and `burning_bolts` (swapped onto the crew of ships with the brazier upgrade) and the ship ballista/mangonel grapeshot ids. Still stripped on purpose: the NavalDLC storyline items and the tournament axes.

Leftover low fps in sea battles is a separate issue (see [[dadg-warsails-campaign-perf-2026-10-04]]).

Same class of bug: [[dadg-caravan-camel-alias]]. See [[dadg-vanilla-override-pattern]].
