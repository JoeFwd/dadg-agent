---
name: dadg-coventry-navmesh-crash-misdiagnosis
description: The Coventry scene navmesh crash was chased by byte-diffing compressed data; root cause never established. UNFIXED, worked around by restoring the stable file.
type: incident
topic: incidents-crashes
tags: [navmesh, incident, coventry]
sources: [old navmesh folder: crash_bytes_*, apply_fix.py, build_hybrid.py]
updated: 2026-10-18
---

# Coventry navmesh crash investigation

Status: UNFIXED at root cause; workaround only. Several commits of the Coventry scene navmesh crashed on load. Analysis scripts diffed the raw RNM1 bytes and produced theories (separator chunks, an id overflow at 32760, merged islands, 67 extra EOF bytes) - all invalid because the body is LZ4 ([[navmesh-reverse-engineering-decompress-first]]).

Remedies used: restore the stable LFS version (`apply_fix.py`) or a hybrid of a later geometry with the stable terminal chunk (`build_hybrid.py`). A decompress-and-structure-diff against the stable commit would settle it. Check [[navmesh-faces-must-be-tris-or-quads]] and [[navmesh-duplicate-corner-face-crash]] candidates first.

Related: [[nmg8-nmg9-scene-navmesh-format]]
