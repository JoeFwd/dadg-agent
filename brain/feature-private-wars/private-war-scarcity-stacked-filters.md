---
name: private-war-scarcity-stacked-filters
description: Why private wars were rare: five stacked filters, and the NoActiveWar dispersal that killed armies.
type: incident
topic: feature-private-wars
tags: [private-wars, analysis, scarcity]
sources: [doc/private-war-scarcity-analysis.md]
updated: 2026-10-18
---

# Private war scarcity stacked filters

Analysis 2026-10-13: AI-declared private wars almost never happened because five filters stacked (claim availability, same-kingdom gate, strength and desire gates, goal selection, and the declaration cooldown/eligibility). Even declared wars produced few real battles because goal armies were disbanded by vanilla's `NoActiveWar` check.

Status: the dispersal is FIXED by `GoalArmyNoActiveWarDispersalPatch`; filter tuning remains a design choice. See [[army-dispersal-noactivewar-check]].

Related: [[private-war-one-goal-army-per-side]]
