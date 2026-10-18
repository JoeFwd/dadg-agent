---
name: feudal-cadet-spinoff-decision
description: Decision: intra-clan wars are fought by spinning the claimant into a runtime cadet clan that joins the parent kingdom, then reabsorbing it on defeat.
type: decision
topic: feature-feudal-titles
tags: [feudal, private-wars, cadet]
sources: [doc/feudal-hero-claims-and-succession-design.md]
updated: 2026-10-18
---

# Feudal cadet spinoff decision

Private-war APIs and the engine are clan-keyed (about 25 call sites enter from a Clan), so two brothers in one clan cannot be opponents. Making the war hero-aware would touch everything and still collide with a clan at the boundary. Chosen: create a cadet clan ([[clan-createclan-cadet-spinoff-recipe]]); because holders are derived, his titles follow automatically.

Aftermath: claimant wins, the cadet becomes a permanent house (canonical: Neville branches, Grey, Scrope); anything short of a win, including white peace, reabsorbs, to avoid piles of dead landless clans. Traitorous vassals are expressed by per-war supporter sets, not by re-parenting the feudal map. Status: designed, not built (daily claim evaluator `EvaluatePressClaimUseCase` and `SolicitSupportUseCase` planned).

Related: [[feudal-hero-holders-decision]], [[private-war-sides-via-title-chain]]
