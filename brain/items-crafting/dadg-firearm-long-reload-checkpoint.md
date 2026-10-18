---
name: dadg-firearm-long-reload-checkpoint
description: Status of the long firearm reload content (handgonne, large bronze arquebus) as of 2026-10-02 - checkpoint only, clips incomplete, name mismatches between XML and C#.
type: incident
topic: items-crafting
tags: [firearms, animation, reload, handoff]
sources: [src/.tmp/reload-content-HANDOFF.md, src/.tmp/activate-firearm-reload-data.ps1]
updated: 2026-10-18
---

# Long reload checkpoint (branch `codex/firearm-reload-fixes`, from `add-scotland`)

- Content: actions `act_reload_firearm_long` (as_reload_mid_phase) and `act_reload_firearm_long_continue` (as_reload_last_phase); usage set `firearm_long` reusing the `firearm` movement set; `handgonne` and `lgarquebus_bronze` use it, `english_arquebus_1` keeps the short vertical reload. Stats unchanged.
- Source clip `reload_new.fbx` (`firearms_reload2_rough`, keys 0-536 @ 25 FPS = 21.44 s). Native start clip `new_animation_clip` covers keys 0-168 (6.72 s); the continuation clip for 168-536 (14.72 s) is NOT created.
- Mismatch to resolve: action XML names `reload_firearm_long_new` / `firearm_reload_long_continue_new`; Core C# uses `new_animation_clip` and `firearm_reload_long_continue_new`. Align both to real native clip names. Not ready to ship even though item XML already selects the long usage.
- Failed renamed probe `reload_firearm_long_new_anm.tpac` and its rdc are kept untracked as evidence ([[animation-clip-rename-breaks-resources]]).
- Resume: finish both clips with native editor saves, align names, rebuild, run the nine lifecycle tests, then verify all three guns in first person (cancel, inventory change, prop cleanup, ground clearance). An unsaved scene dialog was left open; do not assume save/discard.
- Helper `activate-firearm-reload-data.ps1` backs up the four XMLs then injects the actions idempotently.
