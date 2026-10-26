---
name: private-wars-manual-test-howto
description: How to playtest private wars by hand: load the privatewartest save, use campaign.* console commands, what confirms success.
type: howto
topic: feature-private-wars
tags: [private-wars, testing, console]
sources: [doc/feudal-private-wars-manual-test-guide.md]
updated: 2026-10-26
---

# Private wars manual test howto

Setup: load save `privatewartest`, open the console (Alt+~), `config.cheat_mode 1`.

Commands (namespace `campaign.`, defined in `src/submodules/PrivateWars/Bannerlord.PrivateWars/Cheats/PrivateWarDebugCommands.cs`): `declare_private_war <attacker> <defender> [goal]`, `list_private_wars`, `capture_settlement`, `capture_lord`, `is_prisoner`, `force_peace`, `change_kingdom`, `force_besiege`, `create_siege`, `complete_siege_prep`. Do not use `force_battle` mid-siege: it pulls parties off the siege.

Success: the attacker marches to the goal with order Besieging; once prep completes and it is strong enough it assaults the walls (real battle, the player can join from the join_siege_event menu); a won fief goes to the interim owner with no kingdom vote; lords who fought are prisoners; status flips to Concluded only at score +-100; score lands near +-50 after a capture then climbs over about 50 days; nameplates recolour immediately on start and end (use Encyclopedia Track to follow the attacker).

Pitfall: long runs die around in-game day 39 on a vanilla come-of-age equipment crash, unrelated to DADG.

Related: [[private-war-real-siege-assault]]
