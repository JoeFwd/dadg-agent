---
name: feudal-title-transfer-decision
description: Decision: occupying a seat does not move the dignity; only grant, gift, barter, a king's decision, or an administrative change transfers it.
type: decision
topic: feature-feudal-titles
tags: [feudal, titles, transfer]
sources: [doc/feudal-title-transfer-design.md, doc/feudal-titles.md]
updated: 2026-10-26
---

# Feudal title transfer decision

Originally the title followed the seat instantly, so a foreign conqueror became an English earl by storming a wall. History says a title is a legal dignity moved by attainder, inheritance or royal grant, not by garrison.

Chosen: "Option C" deferred transfer. `OnSettlementOwnerChanged` maps the engine's detail ([[settlement-owner-change-details]]) to `SeatTransferKind`: Conquest (BySiege, ByRebellion, and ByKingDecision to an outsider) marks `OccupantClanId` and `ContestedSinceDay`; Grant (ByGift, ByBarter, ByKingDecision within the kingdom) moves the dignity and gives the old holder a Strong Conquest claim (id `{titleId}:{clanId}:conquest`); Administrative (ByLeaveFaction, ByClanDestruction, Default) moves it with no claim. A vacant title is simply taken. Peace no longer regularises occupation (cession removed 2026-10: an occupier only occupies).

Deleted afterwards: the attainder decision, petitions and tension, and the explicit grace clock, because the claimant election delayed same-kingdom transfers; that election itself is gone since 2026-10-26 ([[king-keeps-open-fiefs]]). Open: cross-kingdom finalisation when only a private war links the crowns ([[cross-border-marches-decisions]]).

Related: [[feudal-titles-overview]], [[kingdom-decision-lifecycle]]
