---
name: longsword-type-xxa-hilt-incident
description: Smithy/campaign-start crash from a pre-crafted longsword whose hilt was not in the template UsablePieces; fixed by repointing to the two-handed template.
type: incident
topic: items-crafting
tags: [crafting, longsword, crash]
sources: [runtime-evidence/smithy-longsword-crash (2026-08-03)]
updated: 2026-10-18
---

# Longsword pre-crafted item crash (FIXED 2026-08-03)

Pre-crafted item `type_xxa` (template `ddg_longsword_template`) used Handle `type_xxa_hilt`, which had been removed from that template's `UsablePieces`, so `CraftingOrder.InitializeCraftingOrderOnLoad` NREd at campaign start. Fix: repoint `type_xxa` to the TwoHandedSword template. `type_xxa_hilt` is two-handed exclusive (verified live; first misattributed to the one-handed description). Three benches then passed 14 piece selections.

Live finding: Halfsword and TwoHanded usages are unreachable for longsword (`dadg_Halfsword.AvailablePieces` has zero Handle pieces; `dadg_TwoHandedSword` covers 0 of 17 longsword handles).

Generic: [[precrafted-item-piece-must-be-in-template-usable-pieces]].

Related: [[precrafted-item-piece-must-be-in-template-usable-pieces]], [[crafting-usage-vs-bench-list-rules]]
