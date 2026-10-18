---
name: dadg-handle-offset-bulk-edit-incident
description: 2026-08-04 bulk edit (commit 07d7150 on overhaul-crafting-v2) set 25 handle piece_offsets to length/2 and broke pikes, poleaxes, halberds, staves, maces and hafted axes; FIXED by restoring develop values
type: incident
topic: items-crafting
tags: [crafting, handle, piece_offset, regression]
sources: [memory/handle-piece-offset-semantics.md]
updated: 2026-10-18
---

# 25 handle offsets rewritten to length/2 (FIXED)

On 2026-08-04 DellarteDellaGuerra commit `07d7150` "fix other length" (branch `overhaul-crafting-v2`) rewrote 25 handle `piece_offset` values to `length/2`, breaking pikes, poleaxes, halberds, voulges, staves, maces and hafted axes at once ([[handle-piece-offset-semantics]]). Fixed by restoring the `develop` values, or re-deriving `current_offset - develop_hand_to_bottom` where the mesh had been re-measured.

`ddg_jedbugh_staff_shaft` had a bogus `length="10"` on `develop`; its target was chosen by hand (about 30) rather than restored.
