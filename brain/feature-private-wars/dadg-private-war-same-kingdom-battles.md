---
name: dadg-private-war-same-kingdom-battles
description: Private-war battles between same-kingdom lords never resolved (verified 2026-10-11 at Donnington, Beauchamp army vs Neville besiegers); MapEvent.Update diplomatic finish needs a scoped patch
type: incident
topic: feature-private-wars
tags: [privatewars, mapevent, donnington, scoring]
sources: [memory/same-kingdom-mapevent-diplomatically-finished.md]
updated: 2026-10-18
---

# Same-kingdom private-war battles never score

`StartPartyEncounterBattlePatch` creates the MapEvent for same-kingdom private-war foes, but nothing patched the diplomatic-finish check ([[same-kingdom-mapevent-diplomatically-finished]]). Verified live 2026-10-11 at Donnington (Beauchamp's army vs Neville's besieging army). This blocks the "battle scored in favour of the victor" goal until fixed.

Related: [[pw-sides-dejure-crosses-kingdoms]]
