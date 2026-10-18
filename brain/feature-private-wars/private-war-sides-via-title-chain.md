---
name: private-war-sides-via-title-chain
description: Decision: a clan's side in a private war is found by walking up the feudal title chain to the nearest belligerent principal, cutting at kingdom borders.
type: decision
topic: feature-private-wars
tags: [private-wars, sides, feudal]
sources: [doc/feudal-private-wars-design.md, doc/feudal-hero-claims-and-succession-design.md, doc/private-war-feature-ideas.md]
updated: 2026-10-18
---

# Private war sides via title chain

`WarSideResolver` walks up the suzerain chain; every vassal of a belligerent fights with it. Consequences and refinements:

- Sides are a pure function of the hierarchy, so defection ("traitorous vassals") is inexpressible. Chosen fix: per-war supporter sets consulted before the chain walk, not rewriting the permanent feudal map ([[feudal-cadet-spinoff-decision]]).
- The walk is cut at kingdom borders: England's crown is Lancaster's, and a York realm once resolved onto Lancaster's side before this cut ([[pw-sides-dejure-crosses-kingdoms]]).
- Pricing (`WarSideStrength.ResolveSide`) duplicates the rule used for fighting (`WarSideResolver`); change both together.
- Foreign supporters with a personal bond bring their whole vassal subtree today, which pulled an entire realm in over one friendship; the planned fix is that foreign supporters fight alone ([[private-war-improvement-backlog]]).
- A clan bonded to the defender can still rally to the attacker; the bond gate is not tied to a side.

Related: [[private-wars-overview]], [[private-war-one-goal-army-per-side]]
