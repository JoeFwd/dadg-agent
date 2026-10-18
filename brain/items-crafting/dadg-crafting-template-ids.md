---
name: dadg-crafting-template-ids
description: DADG forces crafting-menu order with numeric-prefixed template ids (01_OneHandedSword...10_Pike), owns all 12 templates, borrows icons, and has a regex trap in the template file
type: reference
topic: items-crafting
tags: [crafting, templates, icons, xslt]
sources: [memory/crafting-template-order-and-icons.md]
updated: 2026-10-18
---

# DADG crafting template ids

- Template ids are numerically prefixed (`01_OneHandedSword` ... `10_Pike`) in `DellarteDellaGuerra/ModuleData/items/dadg_crafting_templates.xml`. Rename = update the `CraftingTemplate id=`, every `crafting_template=` in `DDG_Weapons.xml`, and `str_crafting_template.<id>` in `dadg_module_strings.xml`.
- All 12 templates are DADG-owned (`dadg_pre_crafting_templates.xslt` strips all 12 vanilla ones).
- Icon aliases live in `DellarteDellaGuerraMap/GUI/DadgCraftingWeaponTypesSpriteData.xml`; it works only because DellarteDellaGuerraMap declares `Sandbox` as `LoadBeforeThis`. Borrowed icons: longsword to TwoHandedSword, tourney sword to OneHandedSword, pollaxe to TwoHandedAxe, halberd to TwoHandedPolearm, lance to Pike.
- **Scripted rename trap:** the template file mixes two attribute layouts. Most are `<CraftingTemplate id="x"` on one line, but Dagger and Javelin put `id=` on its own line, so a regex anchored on `CraftingTemplate id="..."` silently skips them. Census ids by parsing (`SelectNodes('//CraftingTemplate')`). Likewise `crafting_template=` refs in `DDG_Weapons.xml`: grep counts 73 but only 70 are live; the rest sit in a commented-out `peasant_hammer_2_t1` block that still references the stripped vanilla `TwoHandedMace`.

Generic rules: [[crafting-template-order-and-icons]]. Related: [[dadg-vanilla-override-pattern]]
