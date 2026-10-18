---
name: private-war-frozen-goal-and-fatigue
description: Decision: each private war freezes one main-goal settlement at declaration, and uncapped fatigue drifts the score toward whoever holds it, guaranteeing termination.
type: decision
topic: feature-private-wars
tags: [private-wars, score, fatigue]
sources: [doc/feudal-private-wars-design.md]
updated: 2026-10-18
---

# Private war frozen goal and fatigue

Fatigue per day = k * (+1 if attacker holds the goal else -1), uncapped, so |score| always reaches 100 and the war ends in favour of the side accomplishing the main goal. If a third party holds the goal, drift goes against the attacker.

Epoch reset: fatigue accrues over `currentDay - GoalLastTakenDay`, not from the war start. When the goal changes hands, that stamp resets, so a capture lands the score near the objective value (about +-50) and the new holder needs about 50 more days to reach +-100. That gives the dispossessed side time to retake the goal.

Gap: `GoalLastTakenDay` is reset only by DADG's own capture path, so a vanilla or third-party capture does not reset it (listed in [[private-war-improvement-backlog]]).

The goal is frozen at declaration so later ownership churn cannot move it.

Related: [[private-war-scoring-v2]], [[private-wars-overview]]
