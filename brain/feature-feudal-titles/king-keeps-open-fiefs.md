---
name: king-keeps-open-fiefs
description: Superseded 2026-11-28 by claimant-vote-outside-private-wars. History of the removed design where captured fiefs got no claimant vote and kings granted them out.
type: decision
topic: feature-feudal-titles
tags: [feudal, titles, kingdom-decision, settlement-claimant, fief-grant, superseded]
sources: [doc/feudal-private-wars-design.md, doc/feudal-title-transfer-design.md]
updated: 2026-11-28
---

# King keeps open fiefs (superseded)

**Superseded 2026-11-28** by [[claimant-vote-outside-private-wars]]: vanilla's claimant vote is back for every fief outside private wars, and none of the code below exists any more.

**No claimant vote (from 2026-10-26).** `DadgSettlementClaimantCampaignBehavior` (PrivateWars submodule) replaced vanilla's `SettlementClaimantCampaignBehavior` and never set `Town.IsOwnerUnassigned`, so a captured or abandoned seat stayed with the king.

**Royal grants (2026-11-27).** DADG's `RoyalFiefGrantCampaignBehavior` had each AI king grant one town or castle a day, taken from those whose title his clan did not hold de jure. `FiefGrantPolicy` chose the de jure holder, then the strongest claimant, then the most useful unlanded clan on non-negative terms with the king. The code is in git at cee7075a.

Related: [[claimant-vote-outside-private-wars]], [[feudal-title-transfer-decision]]
