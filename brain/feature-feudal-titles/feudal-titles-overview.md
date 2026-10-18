---
name: feudal-titles-overview
description: Overview of the DADG feudal title system: static de jure tree from config, hero holders, occupants, claims, succession, encyclopedia UI.
type: reference
topic: feature-feudal-titles
tags: [feudal, titles, overview]
sources: [doc/feudal-titles.md, doc/feudal-succession.md, doc/feudal-hero-titles-and-houses.md]
updated: 2026-10-18
---

# Feudal titles overview

CK3-style layer on Bannerlord politics: Barony < County < Duchy < Kingdom (Emperor rank exists in the domain). Tree comes from `config/titles.config.xml` (`Kingdom`/`Duchy`/`County`/`Barony` elements, unique `id`, optional unique `seat`, `kingClanId` or `holderClanId`, optional `heldSince` year); invalid or missing file degrades to vanilla.

Model: `Title(Id, Name, Rank, SeatSettlementId, HolderHeroId, OccupantClanId, ContestedSinceDay)`. The holder is a hero; his clan is derived each time via the genealogy port, never stored ([[feudal-hero-holders-decision]]). `OccupantClanId` is whoever holds the seat when that differs ([[feudal-title-transfer-decision]]).

Rules
- Conquest marks a held title contested without moving it; grant, gift, barter, or a king's decision inside the title's kingdom transfers it and gives the dispossessed clan a Strong Conquest claim. Peace regularises occupation (uti possidetis).
- Succession on any hero's death ([[feudal-succession-rule]]); claims rebuilt from bloodlines ([[feudal-blood-claims-decay]]).
- `heldSince x 84` days seeds ledger dates; the oldest top title is a house's primary title and chooses its liege. Shipped ties: de la Pole -> Mowbray, Talbot -> York, Hastings -> Talbot, Willoughby -> de Vere, Harrington -> Neville of Raby.
- No Harmony: a campaign behaviour (`FeudalTitleCampaignBehavior`), UI mixins and prefab extensions (`EncyclopediaClanPageMixin`, `EncyclopediaHeroPageMixin`) and a hierarchy screen.
- State persists as pipe-delimited strings under `DadgFeudalTitles` and `DadgFeudalClaims`; never reorder serialiser fields.

Architecture: Domain `Titles/` (pure), Infrastructure `Titles/` (parser, registries, `CampaignGenealogy`), `Titles/Api` (`FeudalServices` static locator; every consumer null-checks it), Integration DI in `DadgServiceContainer.RegisterTitleServices`.

Status: shipped. Petition, tension, attainder and levy machinery was built then deleted (2026-09-27).

Source docs: doc/feudal-titles.md, doc/feudal-succession.md, doc/feudal-title-transfer-design.md, doc/feudal-hero-claims-and-succession-design.md, doc/feudal-hero-titles-and-houses.md, doc/feudal-hero-titles-phase-1..4-implementation-plan.md, doc/feudal-system-analysis.md, doc/feudal-player-rise-brainstorm.md.

Related: [[private-wars-overview]], [[feudal-succession-rule]]
