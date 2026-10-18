---
name: village-optimisation-2026-10-11
description: Main_map village template rewrite on add-warsails: 280 English villages reduced, scene entities 72,559 to 52,679; visuals and FPS unverified.
type: reference
topic: map-settlements
tags: [map, performance, scene]
sources: [src/doc/campaign-village-optimisation.md]
updated: 2026-10-18
---

# Village optimisation 2026 10 11

`tools/village_template_rewrite.py` rewrote each civilian farm to three plant meshes (scale x1.3), dropped decorative props and kept the seven L1 buildings in the looted variant. Results: entities 72,559 to 52,679 (-27.4%), meta-mesh components 55,967 to 37,207 (-33.5%), English civilian L2 meshes -48.3%; each optimised village is now 12/17/24/7 visible meshes for L1/L2/L3/looted. Scottish villages, priories (150 mesh instances) and 426 village sound emitters unchanged; ten abbey/special villages untouched. Scene has no BOM and LF endings. Validated by scripts only: no editor load, no in-game visual or FPS check, so the FPS gain and the enlarged plants are unverified. Applied only to `add-warsails`.

Source docs: src/doc/campaign-village-optimisation.md.
