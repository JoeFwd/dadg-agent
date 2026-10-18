---
name: crafting-offset-fix-plan-outcomes
description: Per-template results of the crafting offset action plan: which families were normalised, which were removed from UsablePieces.
type: incident
topic: items-crafting
tags: [crafting, outcome]
sources: [sdd/action-plan reports 004a-008]
updated: 2026-10-18
---

# Crafting offset fix plan outcomes

Status: content integrated (3 files); compiled TPAC/RDC regeneration pending.

- One-handed sword: normalised with an 18-piece fallback; IX blade `previous_piece_offset=-3.0` kept.
- Axe/mace: Rigsby removed from usable pieces; writhen piece 0.88.
- Two-handed melee: Brogit/Quarterstaff paired fix.
- Halberd (`ddg_halberd`): Jedburgh and Halberd-B normalised; Italian billhook removed from `UsablePieces`. Empty `default_polearm_guard/pommel` slots are intentional.
- Gaelic two-handed sword (IR-13): four `gaelic_fancy_*` pieces removed from `ddg_twohandedsword_template/UsablePieces`; defs and `gaelic_fancy_longsword` CraftedItem stay.
- Task 008: `is_hidden="true"` on `dadg_spear_blade_32` (Iron Fork) and `dadg_spear_blade_29` (Fork Head); both stay referenced by pike and halberd.
- Final sweep at scales 90/100/110: 130 positive candidates, all loose-bounds; no new gaps.
- Task 006 integration passed review; Task 007A compiled-asset check FAILED (swords TPAC changed in all 106 child meshes); 007B repaired the FBX materials. Integration base c6390f86.

Related: [[crafting-connector-offset-normalization-method]], [[fbx-reexport-must-preserve-material-names]], [[handle-piece-offset-semantics]]
