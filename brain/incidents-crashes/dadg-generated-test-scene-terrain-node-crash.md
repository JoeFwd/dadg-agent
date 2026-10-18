---
name: dadg-generated-test-scene-terrain-node-crash
description: A generated DADG battle test scene crashed at load from stale/partial xscene terrain node records. FIXED by rebuilding node records and all 16 weightmap levels.
type: incident
topic: incidents-crashes
tags: [terrain, incident, crash]
sources: [blscene/compose.py, bisect/dump_analysis.txt]
updated: 2026-10-18
---

# Generated scene crash: terrain node records

Status: FIXED. The composer produced scenes with a 257-px template record on 129-px data, and later with weightmap levels only for used layers; each crashed in TaleWorlds.Native at load. `_rebuild_terrain_nodes` now rewrites every node record and fills all 16 levels.

Generic rule and register analysis: [[xscene-terrain-node-records-must-match-terrain-bin]].
