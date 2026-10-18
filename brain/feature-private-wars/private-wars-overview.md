---
name: private-wars-overview
description: Overview of DADG private wars: map-represented casus-belli wars between clans of one kingdom, driven by DADG, with score, fatigue and revert rules.
type: reference
topic: feature-private-wars
tags: [private-wars, overview]
sources: [doc/feudal-private-wars-design.md, doc/feudal-and-private-wars-guide.md, doc/feudal-private-wars-manual-test-guide.md]
updated: 2026-10-18
---

# Private wars overview

A private war is a real, map-visible war between two clans of the same kingdom (for example York versus a rival lord) over a claimed title. The kingdom stays whole; DADG manufactures hostility for that clan pair only (see [[private-wars-stay-in-kingdom-substrate]]).

Key rules
- Lifecycle: declared (claim-driven AI or a debug command) -> active -> concluded at score +-100. Capture of the goal transfers possession but the war stays Active so the loser can retake it.
- Frozen main goal: the settlement driving the war is fixed at declaration, castles and towns only ([[private-war-frozen-goal-and-fatigue]]).
- Scoring v2: goal 50, town 30, castle 10, prisoners +-5 each, plus a capped battle bump ([[private-war-scoring-v2]]).
- Sides come from the feudal title chain ([[private-war-sides-via-title-chain]]); one goal army per side ([[private-war-one-goal-army-per-side]]).
- Same-kingdom sieges never run an assault MapEvent, so DADG completes them itself ([[private-war-synthetic-capture]]).
- Prisoners are held during the war, freed when it ends ([[private-war-prisoner-retention]]).
- Outcome: attacker victory keeps only the goal; everything else reverts ([[private-war-revert-policy]]).
- The player is excluded as claimant and as target.

Main classes: `PrivateWarCampaignBehavior`, `PrivateWarHostilityRegistry`, `ClaimPressureCampaignBehavior` (daily claim evaluation), `DadgEncounterModel`, `DadgSettlementAccessModel`, `DadgPlayerCaptivityCampaignBehavior`, `DadgSallyOutCampaignBehavior`, `PrivateWarSiegeDefenderPolicy`, `PrivateWarPrisonerRetentionPatch`, `GoalArmyNoActiveWarDispersalPatch`, `PrivateWarScoreCalculator`, `WarSideResolver`, `PrivateWarSyntheticCapturePolicy`. The generic engine lives in `src/submodules/PrivateWars/Bannerlord.PrivateWars`.

Status (2026-10-18): implemented and playtested in same-kingdom form. Cross-border wars and several quality improvements are open ([[cross-border-marches-decisions]], [[private-war-improvement-backlog]]).

Source docs: doc/feudal-private-wars-design.md, doc/feudal-and-private-wars-guide.md (Parts 4-5 outdated), doc/feudal-private-wars-implementation-plan.md, doc/feudal-private-wars-manual-test-guide.md, doc/feudal-private-wars-tempkingdom-cost.md, doc/private-war-feature-ideas.md.

Related: [[private-wars-manual-test-howto]], [[mapfaction-wall-blocks-same-kingdom-hostility]], [[feudal-titles-overview]]
