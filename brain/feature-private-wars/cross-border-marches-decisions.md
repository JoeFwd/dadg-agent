---
name: cross-border-marches-decisions
description: Provisional decisions for cross-kingdom private wars: defender is the de jure holder, won claim takes title and de jure lands, titles migrate realms, never auto-escalate to a crown war.
type: decision
topic: feature-private-wars
tags: [private-wars, cross-border, feudal]
sources: [doc/cross-border-marches-design.md, doc/cross-kingdom-private-wars-analysis.md]
updated: 2026-10-18
---

# Cross border marches decisions

Context: a private war works across a border with no StanceLink, but capture then moves a fief into the attacker's kingdom, the title stays contested forever (no crown MakePeace follows), and the defender is ambiguous.

Provisional decisions (open until built; see the design document):
- D1: the defender is the de jure holder, not the seat occupant.
- A won claim takes the title plus its de jure lands.
- Titles may migrate realms; a house's primary title (oldest of its top-rank titles, see [[feudal-titles-overview]]) breaks ties for liege.
- A Weak claim cannot start a cross-border war (`WeakClaimPolicy`).
- Foreign supporters join only through a personal bond, and fight alone.
- Never auto-escalate a private war into a crown war.
- Reverts at war end use `ApplyByDefault` (Administrative), which clears occupation; a won war has no finalisation path yet.
Automatic claim-driven declaration remains same-kingdom only.

Related: [[private-war-improvement-backlog]], [[feudal-title-transfer-decision]]
