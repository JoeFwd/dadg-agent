---
name: king-keeps-open-fiefs
description: Decision (2026-10-26): vanilla's post-capture claimant vote is removed by replacing SettlementClaimantCampaignBehavior; the king keeps fiefs opened to claim, and leaving/destroyed clans keep no claim.
type: decision
topic: feature-feudal-titles
tags: [feudal, titles, kingdom-decision, settlement-claimant]
sources: [doc/feudal-private-wars-design.md, doc/feudal-title-transfer-design.md]
updated: 2026-10-26
---

# King keeps open fiefs

Vanilla `SettlementClaimantCampaignBehavior` flags `Town.IsOwnerUnassigned` when a fief changes hands open to claim (siege, a clan leaving, a clan destroyed), and its daily tick raises a `SettlementClaimantDecision` to auction it. `DadgSettlementClaimantCampaignBehavior` (PrivateWars submodule, swapped in by `SubModule.ReplaceVanillaBehaviors` via `RemoveBehaviors<T>`) never sets the flag and has no daily tick, so the vote is never created and nothing has to be suppressed after the fact.

It keeps the stock duties: finalising a village raid MapEvent that is no longer a war, cancelling pending claimant votes for a settlement that changed hands, returning the player's stash. On load it clears flags and queued votes left by vanilla saves. Explicit votes (a relinquished fief, a passed annexation) remain vanilla.

Leaving or destroyed clans keep no claim: `ByLeaveFaction`/`ByClanDestruction` map to `SeatTransferKind.Administrative`, and `AssignTitleUseCase` creates the conquest claim for every transfer except Administrative.

Shortcut: kings accumulate open fiefs until a planned delegation behaviour grants them to clans.

Related: [[feudal-title-transfer-decision]], [[kingdom-decision-lifecycle]], [[private-war-real-siege-assault]]
