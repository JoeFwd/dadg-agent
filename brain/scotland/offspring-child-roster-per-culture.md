---
name: offspring-child-roster-per-culture
description: DADG's pre-XSLT strips every vanilla EquipmentRoster, so births crashed for battania (2026-10-11) and khuzait/mainland-Scotland (2026-10-13) heroes until child rosters were added (uncommitted)
type: incident
topic: scotland
tags: [offspring, rosters, battania, khuzait, scotland, equipment]
sources: [memory/offspring-child-roster-per-culture.md]
updated: 2026-10-18
---

# Child rosters per hero culture (DADG)

`dadg_pre_equipment_sets.xslt` (Map module) deletes EVERY vanilla `EquipmentRoster`; only empire child rosters were restored. Mechanism: [[offspring-needs-child-equipment-roster-per-culture]].

- 2026-10-11: battania male/female added to `DellarteDellaGuerraMap/ModuleData/equipment/dadg_equipment_sets.xml` after a `clan_macdonald_isles` birth crashed at Winter 13, 1471.
- 2026-10-13: a `clan_douglas_angus` girl crashed at Winter 6, 1471. Mainland Scotland is `Culture.khuzait` (54 heroes), so khuzait male/female were added too.
- Both edits **uncommitted** at the time. Hero cultures now: empire 406, khuzait 54, battania 38, all covered. Minor-faction cultures (vakken, vlandia, aserai, nord) still uncovered.

Rule: any culture given to noble heroes for [[scotland-population-project]] needs its child rosters.

Generic rule: [[reused-culture-needs-complete-data]]
