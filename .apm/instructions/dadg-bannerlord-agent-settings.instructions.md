---
description: DADG values for the generic bannerlord-agent skills (debug config, logs, anchors, cheats, installs) and where DADG knowledge lives.
---

# DADG Bannerlord Agent Settings

These are the project settings that the generic `bannerlord-agent` skills refer to.

## Rider / JetBrains debugging

- Run configuration: `DellarteDellaGuerra.Integration: Standalone`. `start_debug_session` also
  accepts `Standalone`.
- `project_path`: `D:/SteamLibrary/steamapps/common/Mount & Blade II Bannerlord/Modules/DellarteDellaGuerra.Core/src`.
  Pass it on every JetBrains MCP call. The `&` is literal; never HTML-escape it.
- The Standalone profile in `DellarteDellaGuerra.Integration/Properties/launchSettings.json`
  sets `GABP_SERVER_PORT`, `GABP_TOKEN`, `GABS_GAME_ID` and `GABS_BRIDGE_PATH`. `bridge.json`
  must match that profile's port and token.
- CLR exception breakpoints: `src/.rider-debugger-settings`, enforced by the
  rider-clr-exception-override Rider plugin. Edit the exception list there, not in Rider.
- Safe per-frame evaluation anchor:
  `src\DellarteDellaGuerra\DisplayCompilingShaders\CompilingShaderNotifier.cs` line 37
  (`_tickCount += dt;`). Lines 43 onward sit behind an early return. Use it only for one-shot
  evaluation breakpoints; never put a logging breakpoint there.

## Logs

- NLog file: `../log/dadg.log`, relative to `src/`.
- Mod log: `%USERPROFILE%\Documents\Mount and Blade II Bannerlord\Configs\ModLogs\default<YYYYMMDD>.log`.

## New game

DADG is a total conversion. Vanilla `start_new_game` / sandbox flows fail. The new-game menu
option is `DADGNewGame`.

## Cheat command families

Discover the exact surface first (`bannerlord.core.list_commands`,
`bannerlord.core.run_command {"command":"help"}`). The families below proved useful in past
playtests, with DADG and vanilla mixed:

- Private wars: `campaign.declare_private_war`, `campaign.list_private_wars`, `campaign.force_peace`
- Siege setup: `campaign.create_siege`, `campaign.force_besiege`, `campaign.complete_siege_prep`
- Ownership: `campaign.capture_settlement`, `campaign.get_settlement`, `campaign.show_settlements`
- Lords and prisoners: `campaign.capture_lord`, `campaign.is_prisoner`, `campaign.focus_hero`, `campaign.focus_mobile_party`
- Party: `campaign.add_troops`, `campaign.heal_player_party`, `campaign.add_morale_to_party`, `campaign.add_item_to_player_party`
- Factions: `campaign.join_kingdom`, `campaign.change_kingdom`, `campaign.print_strength_of_factions`
- CustomSpawns (only on CustomSpawns branches): `campaign.cs_spawn`, `campaign.cs_declare_war`, `campaign.cs_declare_peace`, `campaign.cs_clan_join_kingdom_as_mercenary`
- Missions: `mission.flee_enemies`, `mission.toggleDisableDying`, `mission.kill_all_allies`
- Cheat mode: `config.cheat_mode 1`

Never trust a command's "success". Verify the changed object directly.

## Modules and installs

| Path (from `Modules/`) | Content |
|---|---|
| `DellarteDellaGuerra.Core/src` | this source repo |
| `DellarteDellaGuerra` | items, armour, weapons, animations, music |
| `DellarteDellaGuerraMap` | England/Scotland campaign map, map XML, campaign UI |
| `DellarteDellaGuerraScenes` | custom mission scenes |

| Install | Status |
|---|---|
| `Mount & Blade II Bannerlord` | live 1.4.x; DADG builds deploy here |
| `Mount & Blade II Bannerlord-v1.3` | obsolete |
| `Mount & Blade II Bannerlord-v1.2` | obsolete |

Map branches matter. For example, the campaign-map distance cache differs between
`DellarteDellaGuerraMap` `develop` and `1.4/complete-navmesh`. Check the map repo's branch
before trusting map behaviour.

## Knowledge brains

- DADG brain: `src/submodules/dadg-agent/brain/` (start at `INDEX.md`). This holds mod
  features, map and settlements, incidents, branches and workflow.
- Generic brain: `src/submodules/bannerlord-agent/brain/`. This holds engine, format and tool
  lessons true for any mod.
- Write new lessons to these submodule checkouts, never to `apm_modules/` or `.claude/`.
  A lesson with a generic rule and a DADG incident becomes two linked notes. The Obsidian vault
  is `src/submodules/`, so links between the two brains resolve.
