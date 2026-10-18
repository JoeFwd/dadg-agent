---
name: dadg-gabs-launch-setup
description: DADG's GABS launch profile - Standalone profile with module list and GABP env, committed on feature/add-church (7e03cb0); War Sails saves need Standalone.WarSails
type: reference
topic: incidents-crashes
tags: [gabs, launchsettings, war-sails, profile]
sources: [memory/gabs-on-1-4-7.md, memory/gabs-start-launches-wrong-install.md]
updated: 2026-10-18
---

# DADG GABS launch setup

Generic recipe: [[gabs-on-1-4-7]].

- The repo `launchSettings.json` Standalone profile needs the module list plus env `GABP_SERVER_PORT=4825`, `GABS_GAME_ID=bannerlord`, `GABP_TOKEN` and `GABS_BRIDGE_PATH` (credentials omitted here). Committed on `feature/add-church` as `7e03cb0` (user-approved 2026-07-21); on v1.2/v1.3 checkouts it stays a local uncommitted edit.
- `bannerlord-gabs-start` skill project_path for the live install: the `DellarteDellaGuerra.Core/src` folder of the main Bannerlord install.
- **2026-09-29:** War Sails saves need the `Standalone.WarSails` profile (Standalone + `NavalDLC`, same GABP env; Rider shows "DellarteDellaGuerra.Integration: Standalone.WarSails"). `Launcher.Standalone` sets no GABP env, so GABS can never connect to a game started from it. The session-reset skill deletes bridge.json, so rewrite it after every reset.
- 2026-08-12: `~/.gabs/config.json` had pointed `games_start` at the obsolete v1.3 install; see [[gabs-start-launches-wrong-install]].
