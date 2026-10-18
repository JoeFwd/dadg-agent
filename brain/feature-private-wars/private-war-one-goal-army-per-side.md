---
name: private-war-one-goal-army-per-side
description: Decision: one goal army per side, with the principal taking priority, and goal armies must survive realm wars and NoActiveWar dispersal.
type: decision
topic: feature-private-wars
tags: [private-wars, army]
sources: [doc/private-war-attacker-win-analysis.md, doc/private-war-scarcity-analysis.md]
updated: 2026-10-18
---

# Private war one goal army per side

Each side gets one goal army, led by the principal when possible. Problems found by analysis (2026-10-13):

- A crown war between the two realms steals the goal army: the realm's war AI re-tasks it. Attackers who should win were failing because their army was taken.
- With supporters from another realm, `IsDesignatedSideLeader` and the member scan look only at the party's own kingdom, so each realm elects its own leader; `_goalArmyLeaders[(war, side)]` holds a single unsaved value, and `ReleaseBelligerentsFromForeignArmies` can strip the other realm's members.
- Vanilla's `NoActiveWar` dispersal disbands the army within hours ([[army-dispersal-noactivewar-check]]); fixed by `GoalArmyNoActiveWarDispersalPatch`.
- A gathering Besieger army points at a gathering fortress, not the target ([[gathering-army-aibehaviorobject-not-target]]).

Related: [[private-war-scarcity-stacked-filters]]
