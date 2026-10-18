---
name: private-war-revert-policy
description: Decision: at war end the attacker keeps only the prize; fiefs that moved between the two belligerents revert to the snapshot owners.
type: decision
topic: feature-private-wars
tags: [private-wars, revert]
sources: [doc/feudal-private-wars-design.md]
updated: 2026-10-18
---

# Private war revert policy

At setup snapshot `OriginalFiefOwners` for both belligerents. On resolve, revert only settlements that moved between this war's two belligerents via `ChangeOwnerOfSettlementAction.ApplyByDefault`, except: the prize stays with the attacker on victory; fiefs owned by a third party are skipped; skip if the original owner is eliminated. White peace or defender win means full status quo ante and the attacker loses the casus belli.

Known gaps: the snapshot covers only the defender principal's own settlements, so vassal or supporter fiefs are neither scored nor reverted; a kingdom-change conclusion bypasses `ResolveWar`, so no revert runs.

Related: [[private-war-improvement-backlog]]
