---
name: scottish-navmesh-rework-outcome
description: Outcome and open item of the 6-phase Scottish campaign navmesh rework (candidate deployed).
type: incident
topic: scenes-navmesh
tags: [scotland, navmesh, outcome]
sources: [plans/scottish-navmesh.md, sdd/scottish-navmesh/progress.md]
updated: 2026-10-18
---

# Scottish navmesh rework outcome

Status: Phase 5 candidate deployed.

- Hashes: original `8596156a...`, Phase 3 base `ab2606ab...`, Phase 5 candidate `0fc1ae1239b21d233fc42196681c170e097e80d64bc717ba4329bb4ca932da6f`.
- Faces [0,7599) are protected (original English faces); all edits append children.
- Phase 4 candidate ab2606ab: 35,133 faces (from 34,093), 183 Mountain faces (g3=7) added, lakes unchanged at 244, non-water coverage 94.958% -> 95.013% on an identical 2 m audit. Changes 292 original faces, appends 1,040 faces, protected faces [0,7599) hash-identical. Path1 mountain pass has a known 6 m bottleneck (not 8 m).
- Phase 6 editor/runtime acceptance: BLOCKED 2026-09-05 (no Bannerlord editor window or process; active hash equalled the candidate). All editor checks remain deferred; Ensure Faces Not Below Ground is forbidden on the active scene.
- Unresolved: a historic coverage figure of about 92.35% could not be reproduced; treat it as unverified.
- Lessons are generic and live in the bannerlord notes.

Related: [[navmesh-surgery-rules-for-existing-meshes]], [[scotland-population-project]]

Generic rule: [[navmesh-editor-runtime-acceptance-checklist]]
