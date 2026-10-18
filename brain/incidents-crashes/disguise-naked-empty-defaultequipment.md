---
name: disguise-naked-empty-defaultequipment
description: The disguised-hero equipment roster resolves with one set but DefaultEquipment is empty, so the player spawns naked; cause unknown.
type: incident
topic: incidents-crashes
tags: [equipment, disguise, unfixed]
sources: [runtime-evidence/disguise-naked-equipment (2026-09-04)]
updated: 2026-10-18
---

# Disguised hero spawns naked (UNFIXED as of 2026-09-04)

The roster `npc_disguised_hero_equipment_template` resolves with `AllEquipments.Count` = 1, but `DefaultEquipment` is empty in all 12 slots at `SandBoxHelpers.cs:126`, although `dadg_equipment_sets.xml:1269` defines 6 items. Suspected a merge or an override leaving an empty element; not confirmed.

Related: [[bannerlord-xml-load-abort-semantics]]
