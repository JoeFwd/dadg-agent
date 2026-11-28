---
name: claimant-vote-outside-private-wars
description: Interim decision (2026-11-28), because players want it: vanilla's claimant vote decides captured and abandoned fiefs; only a war fief changing sides in a private war gets no vote (PrivateWarClaimantVotePatch).
type: decision
topic: feature-feudal-titles
tags: [feudal, titles, kingdom-decision, settlement-claimant, private-wars]
sources: [doc/feudal-private-wars-design.md, doc/feudal-title-transfer-design.md]
updated: 2026-11-28
---

# Claimant vote outside private wars

**Interim, because players want it.** The claimant vote stays until the user has come up with a better, more fleshed-out solution (user, 2026-11-28).

Vanilla `SettlementClaimantCampaignBehavior` runs unchanged. `PrivateWarClaimantVotePatch` (PrivateWars submodule) prefixes its public `OnSettlementOwnerChanged` and, when a war fief (main goal or a key of `OriginalFiefOwners`) of an active private war changes hands between opposite sides, sets `openToClaim = false` and clears `Town.IsOwnerUnassigned`. The owner stays the one `PrivateWarSiegeOwnerPatch` names. War conclusion reverts fiefs with `ApplyByDefault`, which is never open to claim.

History: from 2026-10-26 the vote was removed by a replacement behaviour and kings kept open fiefs; a 2026-11-27 behaviour had kings grant them out. Both were removed on 2026-11-28 (the grant behaviour is in git at cee7075a). Fiefs kings gathered meanwhile are not flagged, so they get no retroactive vote. A vote already queued when a war is declared on that fief is not withdrawn.

A vote winner is applied `ByKingDecision`: the title follows as a Grant inside the title's kingdom, otherwise as a conquest. Leaving or destroyed clans keep no title claim: `ByLeaveFaction`/`ByClanDestruction` map to `SeatTransferKind.Administrative`, and `AssignTitleUseCase` creates the conquest claim for every transfer except Administrative.

Not verified in game (2026-11-28).

Related: [[feudal-title-transfer-decision]], [[kingdom-decision-lifecycle]], [[private-war-real-siege-assault]]
