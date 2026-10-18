---
name: scotland-population-project
description: Scotland (Lordship of the Isles + Crown of Scotland) for the DADG map on branch 1.4/complete-navmesh - deployed 181-settlement Isles build, approved 160-settlement two-kingdom consolidation (Stage 1 geometry done, Stage 2/3 pending), locked decisions and gotchas
type: reference
topic: scotland
tags: [scotland, settlements, kingdoms, clans, navmesh, consolidation, abbey, project]
sources: [memory/scotland-population-project.md]
updated: 2026-10-18
---

# Scotland population project (state as of 2026-07-31)

Goal: populate Scotland on the newer campaign navmesh, branch `1.4/complete-navmesh` of the **DellarteDellaGuerraMap** repo (a SEPARATE git repo from Core/src on `develop`). Sources: two KMZ pin sets and a Google Sheet in the user's downloads.

## Phase 1: deployed (Lordship of the Isles, 181 settlements)
Locked: ONE kingdom reusing `id="battania"` ([[dadg-vanilla-override-pattern]]), 17 clans as vassals, 181 settlements, navmesh REACHABILITY only (carve islets, do NOT touch `terrain.bin`), ships give offshore access.
Spliced into the registered DADG files with byte-exact `*.bak_scotland_*` backups: `dadg_kingdoms.xml` (ruler `dadg_sco_lord_clan_macdonald_isles`, seat `dadg_sco_finlaggan_town`), `dadg_clans.xml` (+17, `super_faction=Kingdom.battania`), `dadg_heroes.xml` (+17), `characters/dadg_lords.xml` (+17), `settlements.xml` (+181: 7 towns / 66 castles / 108 villages, ids `dadg_sco_*`, culture battania). `navmesh.bin`: 56 sea faces (idx >= 15912) g3 to land for 59 offshore settlements; England faces [0,7599) byte-identical; validated 0 dangling refs, 0 dup ids.
Non-obvious: module strings not added (inline `{=key}Name` fallback); offshore reachability needs War Sails naval (may be uninstalled, not a failure); DADG England has ZERO castles, so the 66 `is_castle="true"` are new (reuse vanilla battania scenes).
**Load crash FIXED (2026-07-28):** kingdom culture `Culture.battania` NREd in `Kingdom.InitializeKingdom`; changed to `Culture.empire` ([[reused-culture-needs-complete-data]]). Clans keep battania.
**Long Island shift (2026-07-30):** 23 westernmost Hebrides settlements (filter `z==10.0 & x<=340 & y>=840`) floated over deep water; applied uniform +45 m east / -8 m north to BOTH files ([[map-settlement-position-two-files]]). Gotcha: attr regex must be `(?<!\w)posX` or it also matches `gate_posX` (double shift). Uniform shift fixed only about 5/23; user pre-authorised; island enlargement follows. `terrain.bin` reverted to baseline (earlier `gen_islands.py` edits scrapped per user: "island already exists, just shift settlements east").
Remaining then: playtester re-verify, commit the 6 Map files only (EXCLUDING unrelated `dadg_skins.xslt`), leave `.bak_scotland_*` untracked, revert the temporary GABS block in `launchSettings.json` ([[dadg-gabs-launch-setup]]).

## Phase 2: consolidation (plan APPROVED 2026-07-31, authoring not started)
Rebuild from two KMZ sets: Crown of Scotland (224 pins east/south) and Lordship of the Isles (about 181 pins). User target **160 total across TWO kingdoms**, applying English-side ratios (about 71% of forts castles, about 3 villages/fort, towns rare) plus a NEW settlement type **ABBEY**. Final budget: Crown 100 (12t/16c/9ab/63v) + Isles 60 (3t/12c/5ab/40v); after the Campbell decision **15 towns / 29 castles / 14 abbeys / 102 villages**. Economy-first: strict-ratio Isles, plus 3 western market towns (Finlaggan, Stornoway, Dingwall). "Militia-heavy small forts" = a future code patch, not XML. Table 2 (21 Isles castles) in reserve. **Scaling:** start at 160; expand to 250+ if thin. Overlap: Inverness to Crown, Dingwall to Lordship, Argyll/Campbell to Crown. Plan: `scotland/consolidated_plan.md` + `research_crown.md`/`research_isles.md` (external tooling dir, not in repo).

**Stage 1 geometry DONE (2026-07-31):** `scotland/master_160.json` frozen; every fort fed 2-3 villages; village selection = nearest-unclaimed, least-fed-first, cap 3, uniform min-spacing floor vs all forts and placed villages (Crown 14.0, Isles 12.0, calibrated to England NN spread median 16.7 / p10 11.5; result min 3.4 / p10 12.1 / median 16.9 / p90 24.5). Village-to-fort binding is `bound="Settlement.<parent_id>"` (NOT `bound_settlement`). Gotcha: the scotland scripts dir has `inspect.py` shadowing stdlib; strip the script dir from `sys.path` before importing numpy. Isles villages are islands and need the on-land relax pass used in Phase 1.

**Stage 2 roster LOCKED (user sign-off):**
- Abbey scope A: abbeys authored as plain abbey-styled Villages; Core `feature/add-church` merge deferred ([[dadg-abbey-church-system]]).
- **Crown of Scotland:** reuse vanilla id `khuzait` (khuzait/aserai the only free ids), `culture="Culture.empire"`; ruler King James III Stewart, seat Edinburgh; 17 clans (16 seated + fief-less Home/Hume at Edinburgh); royal demesne Edinburgh, Stirling, Linlithgow, Blackness, Lochleven, St Andrews, Inverness, Doune. All Crown clans `Culture.empire`.
- **Campbell seat:** promote **Kilchurn** (467.1,775.7) village to castle (zero geometry), a Crown castle in Argyll on the Isles frontier (nearest fort MacLean's Duart 43.7).
- **Lordship of the Isles:** id `battania`, flip culture battania to empire (same NRE risk); 18 clans (13 seated + 5 fief-less MacKinnon/MacPhee/Keppoch/MacNeil-mainland/MacAlister, home Finlaggan). MUST-FIX: repoint reused Isles clan seats to clean manifest ids (deployed ones carry doubled suffixes like `dunvegan_castle_castle`; `mingarry` to `mingary`). New clan MacLeod of Lewis at Stornoway.
- Next: regen manifest with Kilchurn promotion, generate Stage 2 (kingdoms/clans/heroes/lords) and Stage 3 (settlements.xml + scene.xscene) fragments for review, deploy with byte-exact backups.

**Magnitude:** NOT a trim of the 181: the Crown half (about 100 settlements) is a brand-new build (projected posX/posY, new capsules, new navmesh reachability) plus two-kingdom split. Files to rewrite: settlements.xml, scene.xscene, dadg_kingdoms.xml, dadg_clans.xml, dadg_heroes.xml, dadg_lords.xml, navmesh.bin.

Related: [[offspring-child-roster-per-culture]], [[dadg-navmesh-studio-settlement-placement]], [[navmesh-studio-tool]]
