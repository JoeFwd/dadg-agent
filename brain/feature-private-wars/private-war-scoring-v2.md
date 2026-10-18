---
name: private-war-scoring-v2
description: Scoring v2 weights for private wars: goal 50, town 30, castle 10, prisoners 5 each, normalised battle bump capped at 50.
type: reference
topic: feature-private-wars
tags: [private-wars, score, weights]
sources: [doc/feudal-private-wars-design.md]
updated: 2026-10-18
---

# Private war scoring v2

Score is attacker-positive, clamped to +-100: `S = clamp(stateTerms + BattleScore + fatigue)`.

State terms (recomputed each tick)
- Main goal 50 flat, town 30, castle 10. Settlements of the whole side (principal plus sub-vassals) count; a defender holding an attacker-side fief subtracts its weight.
- Prisoners: +-5 each for a captive who belongs to the opposing principal's clan; vanishes on release or escape.

Accumulated term (the only persisted one): `BattleScore += BATTLE_WEIGHT * clamp(enemyForceDefeated / losingSideTotalStrength, 0, 1)`, signed by winner, capped to +-`BATTLE_SCORE_CAP`. Both constants start at 50. Normalising by the whole losing side makes one decisive battle worth more than many skirmishes. Village raids do not score (deferred).

Related: [[private-war-frozen-goal-and-fatigue]]
