# DADG Brain

One durable lesson per note. Grep `**/*.md` for a symptom, API or file name; browse by topic below.

## banners-clans

- [[dadg-banner-charges-added-2026-09-12]] (incident): Seven banner charges repainted into DADG's custom_banner_icons atlas on 2026-09-12, with the slots overwritten and the CC BY credit requirement
- [[dadg-banner-palette-remap-applied]] (incident): FIXED 2026-09-12 - dead bannerlord.party colour ids remapped in DADG's dadg_clans.xml (48 English clan keys, 1358 substitutions); invisible on screen while POC is active
- [[dadg-clan-banner-keys-exceed-32-layers]] (reference): 36 DADG clan banner keys exceed 32 layers (worst 488) and now render in full on 1.4.7+ singleplayer; where the worked heraldry docs live
- [[map-banner-mesh-shared-with-banner-editor]] (reference): The vlandia_tier_1_banner mesh is shared by the map party banner and DADG's banner editor scene; the 2x map override is compensated by entity scale 0.754 in the editor scene
- [[poc-config-redirect-patch]] (reference): PocConfigReaderOverriderPatch redirects the POC mod's config reads to DADG's config/poc.config.json.
- [[poc-overrides-english-clan-banners]] (incident): POC's clanBanner in poc.config.json wholesale-replaces the XML banner for all 55 English clans and is 54/55 stale, so heraldry edits to York/Lancaster clans are discarded at runtime; Scottish clans are protected only by accident

## feature-cannons

- [[aiformationmanager-spent-cannon-budget-deadlock]] (incident): FIXED via an IsSpent latch - the cannons mod's AIFormationManager budgeted crew only for cannons with ammo but never detached spent ones, so spent guns soaked crew while working guns starved
- [[bodyguard-orderposition-drafts-distant-crew]] (incident): Cannon crew refills draft the man nearest Bodyguard's OrderPosition, which is stale-copied from Infantry, so wall-top defender cannons get reloaders from 35m away and 16m below who die en route
- [[cannon-b1-reloader-stall-2026-08-13]] (incident): Crew/bodyguard fix verification found reloaders frozen beside the ammo point; the ammo gate hypothesis was falsified and falconets were deactivated; open at 2026-08-13.
- [[cannon-loader-arrives-but-never-seats]] (incident): A cannon loader that loses its ball en route latches use_load as HasAIMovingTo forever; fixed by porting vanilla's trebuchet release branch into AmmoLoadHandler (not yet live-verified)
- [[cannon-trajectory-investigation]] (incident): RESOLVED - "cannonball flies shorter / must aim higher" is a data regression (muzzle velocity 120->90, commit 4509642) under an unchanged 0.2rad elevation cap, NOT a trajectory-formula or 1.4 change
- [[dadg-add-a-cannon-howto]] (howto): Adding a cannon to DADG is data-driven: cannons.xml, siege_engines.xml, cannon_items.xml, prefabs, FBX meshes, three UI sprites, scene spawners.
- [[dadg-cannon-crewing-fixes]] (reference): Index of DADG cannon crewing fixes in the Cannons submodule - dead falconets pruned in AIFormationManager.Update, ForcedUse off, StandingPoint TOCTOU, and the related crew-pool incidents
- [[dadg-cannons-mesh-folder-has-no-mtl]] (incident): 2026-09-02 cannonball pile rendered flat grey (material trailer "default"); Assets/cannons is the one mesh folder with no _mtl.tpac beside it, its material sits in Assets/firearms
- [[defender-cannons-firesafety-veto]] (incident): DADG defender wall cannons idle because the defender prefab has an 18 degree traverse arc; aiming an out-of-arc target slews the barrel to the clamp limit into the merlon and the fire-safety check vetoes (fix not yet live-verified)

## feature-church

- [[dadg-abbey-church-system]] (reference): DADG abbeys are Villages tagged in Core config/dadg.church_settlements.xml; each diocese needs exactly one Cathedral or the church feature silently deactivates; the system lives on UNMERGED feature/add-church
- [[dadg-sanctuary-save-softlock-not-a-container-bug]] (incident): 2026-08-12 sanctuary save/load soft-lock looked like a missing Dictionary<Hero,CampaignTime> definition, but vanilla already registers it; adding it would have been a duplicate

## feature-coop

- [[coop-compat-project]] (decision): DADG <-> BannerlordCoop compatibility effort (started 2026-10-11) - solo-first with a coop adapter submodule; reading Coop source for interop is authorised, copying is not

## feature-customspawns

- [[constant-war-peace-loop-customspawns]] (incident): FIXED 2026-08-06 - CustomSpawnsDiplomacyModel.IsAtConstantWar now lets forced-peace return false before vanilla; found via two Calradia at War spawn clans
- [[customspawns-army-infeasible]] (decision): Decision 2026-08-18 - CustomSpawns invasion parties cannot form an Army for a kingdomless clan like cs_humar; use BesiegerCamp
- [[customspawns-component-identity-outcome]] (incident): CustomSpawns identity moved onto party components (commit bc9e05f); old saves incompatible by design; NUnit adapter cannot run on .NET 10.
- [[customspawns-failed-invasion-recovery-healthy]] (incident): Live check on 2026-09-20 showed a retreated CustomSpawns invasion returns to a healthy retryable Search state.
- [[customspawns-partyowner-must-be-leader]] (incident): CustomSpawns besiege feature (2026-08-17) - a party capturing a castle NREd because PartyOwner/SetCustomOwner was clan.Leader, who has no party
- [[dadg-customspawns-capital-garrison-drain]] (incident): 2026-10-13 - CustomSpawns Humar capital (Charas) garrison fell 408 to 186 while every InvasionLordWarbands draw logged men=0; cause is vanilla garrison rebalance, not mod code

## feature-feudal-titles

- [[feudal-blood-claims-decay]] (reference): Blood claims are rebuilt from scratch on every change; strength decays by generation from the holder and his father.
- [[feudal-cadet-spinoff-decision]] (decision): Decision: intra-clan wars are fought by spinning the claimant into a runtime cadet clan that joins the parent kingdom, then reabsorbing it on defeat.
- [[feudal-hero-holders-decision]] (decision): Decision: titles name a hero and the holder's clan is derived, never cached; all ranks are hero-held.
- [[feudal-player-entry-brainstorm]] (reference): Brainstorm: give the player a ladder into the feudal system through gentry rungs (retaining, manors, offices, knighthood, promise of a barony).
- [[feudal-succession-rule]] (reference): Male-preference primogeniture with representation: own line, then siblings through the father, then clan head, else vacant.
- [[feudal-system-audit-findings]] (reference): Audit of the feudal system (doc/feudal-system-analysis.md): gaps found between design and code, including the engine-boundary issues that shaped later work.
- [[feudal-title-transfer-decision]] (decision): Decision: occupying a seat does not move the dignity; only grant, gift, barter, a king's decision, or peace transfers it.
- [[feudal-titles-overview]] (reference): Overview of the DADG feudal title system: static de jure tree from config, hero holders, occupants, claims, succession, encyclopedia UI.

## feature-other

- [[character-creation-roster-requirements]] (reference): Character creation age-menu flow dereferences the selected roster's Horse and HorseHarness, so every active DADG role battle set needs both.
- [[dadg-caravan-camel-alias]] (incident): FIXED 2026-10-11 - DADG reuses the aserai/khuzait culture ids for Anglo Irish and Lowland Scots; camel aliased to the mule in dadg_pre_native_items.xslt after Dumfries' rebel clan caravans crashed
- [[dadg-lord-defection-sources]] (incident): Why DADG clans change realm - day-1 vanilla random lord relations plus Honor -1 leaders, not DADG code; see doc/lord-defection-analysis.md

## feature-private-wars

- [[cross-border-marches-decisions]] (decision): Provisional decisions for cross-kingdom private wars: defender is the de jure holder, won claim takes title and de jure lands, titles migrate realms, never auto-escalate to a crown war.
- [[dadg-private-war-hostility-cpu-profile]] (incident): A PerfView capture showed private-war hostility / war-side / suzerainty / title-scan work using ~76% of main-thread CPU for the first ~50 s, collapsing to ~0.01% after a clan defection / kingdom-change event.
- [[dadg-private-war-same-kingdom-battles]] (incident): Private-war battles between same-kingdom lords never resolved (verified 2026-10-11 at Donnington, Beauchamp army vs Neville besiegers); MapEvent.Update diplomatic finish needs a scoped patch
- [[dadg-privatewars-gathering-army-fixes]] (incident): PrivateWars 2026-10-11 - three fixes for the AiBehaviorObject misread - _goalArmyLeaders recording, VetoSameKingdomSiegeRelief, and ReleaseBelligerentsFromForeignArmies
- [[faction-wars-v2-lost-submodule-commit]] (incident): PrivateWars 98ccbc97 is gone from every object store, but its source was recovered by decompiling the 2026-09-08 DLLs and PORTED onto develop as bd1fd24 (verified faithful)
- [[private-war-attacker-win-analysis]] (incident): Why attackers failed to win: the realm war stole the goal army, and cross-realm supporters elected rival leaders.
- [[private-war-frozen-goal-and-fatigue]] (decision): Decision: each private war freezes one main-goal settlement at declaration, and uncapped fatigue drifts the score toward whoever holds it, guaranteeing termination.
- [[private-war-improvement-backlog]] (reference): Ranked backlog of private-war improvements (2026-10-13): foreign supporters fight alone, prize goes to principal, third-party fatigue, arbitration, summons.
- [[private-war-one-goal-army-per-side]] (decision): Decision: one goal army per side, with the principal taking priority, and goal armies must survive realm wars and NoActiveWar dispersal.
- [[private-war-prisoner-retention]] (decision): Decision: lords captured in a private war stay prisoners during the war and are released when it ends.
- [[private-war-revert-policy]] (decision): Decision: at war end the attacker keeps only the prize; fiefs that moved between the two belligerents revert to the snapshot owners.
- [[private-war-scarcity-stacked-filters]] (incident): Why private wars were rare: five stacked filters, and the NoActiveWar dispersal that killed armies.
- [[private-war-scoring-v2]] (reference): Scoring v2 weights for private wars: goal 50, town 30, castle 10, prisoners 5 each, normalised battle bump capped at 50.
- [[private-war-sides-via-title-chain]] (decision): Decision: a clan's side in a private war is found by walking up the feudal title chain to the nearest belligerent principal, cutting at kingdom borders.
- [[private-war-synthetic-capture]] (decision): Decision: because same-kingdom AI sieges never form an assault MapEvent, DADG transfers the goal when siege preparations complete.
- [[private-wars-manual-test-howto]] (howto): How to playtest private wars by hand: load the privatewartest save, use campaign.* console commands, what confirms success.
- [[private-wars-overview]] (reference): Overview of DADG private wars: map-represented casus-belli wars between clans of one kingdom, driven by DADG, with score, fatigue and revert rules.
- [[private-wars-stay-in-kingdom-substrate]] (decision): Decision: private wars keep both clans in their kingdom and manufacture hostility pair-by-pair, rejecting splinter kingdoms and lone-clan ejection.
- [[pw-no-solo-siege-playtest-2026-10-11]] (incident): Four playtest attempts on 2026-10-11 of the private-war designated-leader siege bid; two native AVs, a navmesh gate fix, a foreign-army release fix that passed, and no siege bid observed.
- [[pw-run-outcomes-2026-10-11]] (incident): Natural-lifecycle observation of a private war (resolved by score decay) plus inconclusive goal-army and prosecution fix checks, 2026-10-11.
- [[pw-sides-dejure-crosses-kingdoms]] (incident): Private-war side resolution walked the de jure title chain, and kingdom_england's king is clan_lancaster, so the whole York kingdom resolved onto Lancaster's side; adapter now cuts at kingdom borders (uncommitted 2026-10-11)

## incidents-crashes

- [[dadg-coventry-navmesh-crash-misdiagnosis]] (incident): The Coventry scene navmesh crash was chased by byte-diffing compressed data; root cause never established. UNFIXED, worked around by restoring the stable file.
- [[dadg-gabs-launch-setup]] (reference): DADG's GABS launch profile - Standalone profile with module list and GABP env, committed on feature/add-church (7e03cb0); War Sails saves need Standalone.WarSails
- [[dadg-generated-test-scene-terrain-node-crash]] (incident): A generated DADG battle test scene crashed at load from stale/partial xscene terrain node records. FIXED by rebuilding node records and all 16 weightmap levels.
- [[dadg-missing-commonareamarker-scenes]] (incident): UNFIXED as of 2026-08-01 - DADG scenes missing CommonAreaMarker scripts - York, Lincoln, London, Newcastle, dadg_village_d/e, two hideouts, plus partial others
- [[dadg-warsails-campaign-perf-2026-10-04]] (incident): Findings of the 2026-10-04 War Sails campaign performance probe - fast-forward cost reproduced, no War Sails-specific cause proven; sea navmesh numbers and a material discrepancy.
- [[disguise-naked-empty-defaultequipment]] (incident): The disguised-hero equipment roster resolves with one set but DefaultEquipment is empty, so the player spawns naked; cause unknown.
- [[warsails-ship-crash-chain-2026-09-30]] (incident): Sequence of War Sails crashes 2026-09-30 to 2026-10-03 and what fixed each, with the FMOD hang left open.

## items-crafting

- [[cannonball-pile-material-investigation]] (incident): Cannonball pile looked matte because its material lacks use_specular; correction not yet applied as of 2026-09-07.
- [[crafting-offset-fix-plan-outcomes]] (incident): Per-template results of the crafting offset action plan: which families were normalised, which were removed from UsablePieces.
- [[dadg-cannonball-pile-fbx-scale-incident]] (incident): CannonBallPiles.fbx imported 100x too small (Lcl Scaling 0.01); the prefab scale="40" was a wrong compensation tuned against the collision proxy
- [[dadg-crafting-template-ids]] (reference): DADG forces crafting-menu order with numeric-prefixed template ids (01_OneHandedSword...10_Pike), owns all 12 templates, borrows icons, and has a regex trap in the template file
- [[dadg-firearm-long-reload-checkpoint]] (incident): Status of the long firearm reload content (handgonne, large bronze arquebus) as of 2026-10-02 - checkpoint only, clips incomplete, name mismatches between XML and C#.
- [[dadg-handle-offset-bulk-edit-incident]] (incident): 2026-08-04 bulk edit (commit 07d7150 on overhaul-crafting-v2) set 25 handle piece_offsets to length/2 and broke pikes, poleaxes, halberds, staves, maces and hafted axes; FIXED by restoring develop values
- [[dadg-scabbard-fixes]] (incident): DADG scabbard fixes 2026-08-08 - hanger and wakefield_hanger swapped to Scabbard03_black; castillon_b blade reseated by splitting distances (base 7.691 to 9.868, reach unchanged); DADG scabbard family table
- [[dadg-scottish-arming-sword-fix]] (incident): The Scottish arming sword (2026-08-05) was ONE blade defect (mesh authored 5.353 low) that looked like two; fixed by recentring the FBX origin and previous_piece_offset 0.98, plus a 100x FBX scale failure afterwards
- [[longsword-type-xxa-hilt-incident]] (incident): Smithy/campaign-start crash from a pre-crafted longsword whose hilt was not in the template UsablePieces; fixed by repointing to the two-handed template.

## map-settlements

- [[dadg-main-map-geometry-and-protected-england-faces]] (reference): DADG Main_map geometry, water levels, and the rule that England's hand-authored navmesh faces [0,7599) must stay byte-identical.
- [[dadg-map-capsule-naming-and-scotland-positions]] (reference): DADG naming for settlement capsules in the Main_map scene, and the verified invariant across 160 Scotland settlements
- [[dadg-navmesh-backport-london-hideout]] (incident): A develop-branch London and hideout-spawn navmesh fix was reapplied onto the complete navmesh with only protected-region-safe edits. FIXED.
- [[dadg-seaborne-village-raid-migration]] (reference): State of DADG seaborne village raid scenes - 73 of 426 villages sea-reachable, Grimsby variant installed, Southwark and Thorne need redesign.
- [[dadg-vanilla-override-pattern]] (reference): How DADG replaces vanilla kingdoms/clans/settlements - pre-XSLTs strip ALL vanilla first, so vanilla ids (sturgia/vlandia/battania) are safely reused; append to the single registered dadg_*.xml per type
- [[village-optimisation-2026-10-11]] (reference): Main_map village template rewrite on add-warsails: 280 English villages reduced, scene entities 72,559 to 52,679; visuals and FPS unverified.
- [[war-sails-main-map-migration-plan]] (decision): Plan to migrate DADG's campaign map to War Sails v1.2.8 (plan only, not executed in the sources).

## scenes-navmesh

- [[dadg-bridge-relocation-no-gos]] (decision): Why relocating the Wye/Oxford Roman piers and adding a Great Ouse approach were all judged no-go (grades 50+ deg, navmesh floating above terrain, nested town assembly).
- [[dadg-joust-v3-editor-fixes]] (incident): dadg_joust_v3 editor problems 2026-08-17/18 - orphan group GUID crash (4 barrier entities from the v2 donor) and terrain_ed.bin repaired by folding compiled heights back in
- [[dadg-joust-v3-terrain-paint]] (howto): How the widened joust arena was built: touched WGHT nodes, flatten height, feathering, filling weight deficits, donor hash recheck.
- [[dadg-main-map-bridge-navmesh-final-state]] (incident): Final deployed state of the DADG Main_map navmesh bridge/river work (2026-09-29) - 31 decks, counts, gates passed and what remains.
- [[dadg-navmesh-studio-settlement-placement]] (reference): DADG settlement-placement specifics of the navmesh studio - footprint radii town 8.475 / castle 3.572 / village none; only dadg_sco_* movable; water oracle height > 10.0
- [[dadg-rochester-castle-scene-spec]] (decision): Design spec for dadg_Rochester_castle: real dimensions, scale, asset mapping, and the worldmap-icon trap.
- [[dadg-roman-bridge-terrain14-banks]] (incident): UNFIXED - five Roman town bridge decks (Great Ouse, London, Severn, Wye, Oxford) sit between terrain-14 RuralArea banks that land parties cannot use; plus one London Gothic pier with no confirmed span.
- [[dadg-siege-scene-reference-castles]] (reference): Reference siege scenes and navmesh scale in DADG: Clun and Dartmouth as oracles, native scenes are 5-30x larger.
- [[dadg-ws-ship-navmesh-and-climber-fixes]] (incident): FIXED 2026-10-01 - DADG ship climbers re-yawed to the vanilla frame and ship navmeshes rebuilt coarse (kogge 94 / carrack 24 / boat 13 faces); carrack has no stairs to its upper decks so they are excluded; open-sea campaign navmesh stripped on purpose
- [[dadg-ws-ship-reimport-state]] (reference): 2026-10-02 state of DADG War Sails ship mesh reimports - slot 1 now Map dadg_ws_* aliases, slot 2 stale; English boat prefab still on v1 sail and old body
- [[dadg-york-navmesh-fragmentation]] (incident): York's navmesh.bin is valid but fragmented (74 components, 31 tiny islands vs Lancaster 37/7); ruled out as the civilian-mission crash cause on 2026-07-31, kept as a cleanup item
- [[framlingham-navmesh-hole]] (incident): FIXED 2026-09-10 - Framlingham siege stall was 335 connector faces g5=-51 (siege + level_1 only); promoted to g5=-3
- [[framlingham-siege-stall-diagnostic]] (incident): Live diagnostic of a Framlingham siege stall: cannon crew never released and the tower navmesh was an orphan island; the DADG-side crew finding was real but not the cause.
- [[lordshall-halls-archer-slot-and-navmesh-fixes-2026-08-31]] (incident): Lord's-hall scenes A-D and cathedral/London: 6 archer prefabs per hall converted to infantry, Hall A siege-bit navmesh patch, layout rules, and what remains untested.
- [[scene-water-audit-stokesay-moat]] (incident): Water audit: scenes with local water, Stokesay moat lost on re-save.
- [[scottish-navmesh-rework-outcome]] (incident): Outcome and open item of the 6-phase Scottish campaign navmesh rework (candidate deployed).

## scotland

- [[dadg-hebrides-island-float-terrain-fix]] (howto): Offshore Scottish settlements float because terrain sits below the 10.0 water plane; raise the heightmap, settlement Z comes from a physics raycast, not the navmesh.
- [[dadg-scotland-gate-av]] (incident): FIXED 2026-10-11 (uncommitted Map settlements.xml) - Kilchurn castle and Auchterarder village gates were on non-land faces and crashed every campaign playtest
- [[dadg-scotland-settlement-budget]] (decision): Consolidated Scotland plan: 160 settlements (Crown 100, Lordship of the Isles 60), ratios and kingdom boundary decisions.
- [[dadg-scottish-1471-banner-corrections]] (reference): The 2026-09-19 pass that rewrote Scottish kingdom/clan banner keys in poc.config.json for 1471 accuracy, including a CC BY flame icon for MacLeod of Lewis, and the checks used.
- [[dadg-v14-river-and-lake-detection]] (reference): Flow-accumulation river detection on the DADG heightmap: what was found, river bed heights, rivers not found, Spey divide caveat.
- [[offspring-child-roster-per-culture]] (incident): DADG's pre-XSLT strips every vanilla EquipmentRoster, so births crashed for battania (2026-10-11) and khuzait/mainland-Scotland (2026-10-13) heroes until child rosters were added (uncommitted)
- [[scotland-battania-culture-data-gaps]] (incident): Scottish content using the reused battania culture crashed campaign start twice (kingdom policies, then notable templates); status and candidate fixes as of 2026-07-28.
- [[scotland-map-border-fix]] (incident): Northern Scottish settlements were unreachable by the camera because border_max Y was 750; raised to 1120 in the main map scene.
- [[scotland-navmesh-20260908-unverified]] (incident): A 2026-09-08 Scotland navmesh deployment was never confirmed loaded natively; offline audit passes are not proof.
- [[scotland-population-project]] (reference): Scotland (Lordship of the Isles + Crown of Scotland) for the DADG map on branch 1.4/complete-navmesh - deployed 181-settlement Isles build, approved 160-settlement two-kingdom consolidation (Stage 1 geometry done, Stage 2/3 pending), locked decisions and gotchas
- [[scotland-settlement-rebalance-170]] (decision): Scotland settlement roster rebalanced to 170 (16 towns / 29 castles / 125 villages), deployed with region-grouped scene hierarchy and v1.4.8 distance cache.
- [[scotland-settlements-drifted-off-raised-islands]] (incident): 2026-08-15 diagnosis - 64 of 160 Scottish settlements invalid because they drifted off their raised terrain islands (only 14 have terrain > 10), not for lack of navmesh; fix is nudge back onto own island plus carve navmesh only over terrain > 10
- [[scottish-banners-docs-overview]] (reference): Pointer note: Scottish banner design docs (1471 re-audit, icon tiles, tartan set superseded, high-priority SDD).
- [[scottish-families-1471-reference]] (reference): Reference: the 35 Scottish clan holders and household members at the 1471 start, with historical dates and uncertainty markers.
- [[scottish-prefab-library-rollout-and-compaction]] (incident): Chain of Scottish prefab work (library, siegeable shells, rollout, compaction, layout v3) with commits, hashes and review catches.

## workflow-branches

- [[apm-hooks-shell-mismatch]] (howto): apm emits $env:CLAUDE_PROJECT_DIR in Claude Code hooks but hooks run under bash on Windows - fix the .apm/hooks templates, not the generated settings.json
- [[deliver-docs-as-md-not-artifacts]] (decision): Agent-workflow preference - design docs, plans and reports go to doc/<kebab-name>.md in the repo; never publish artifacts
- [[dependency-submodules-workflow]] (howto): Controlled dependencies live under src/submodules and are edited in place; rebuild DADG to deploy their DLLs.
- [[playtester-agent-stall-self-repair-risk]] (lesson): The bannerlord-debug-playtester subagent can spiral into deleting ~/.gabs/bannerlord/*.json when its own MCP tools look unreachable; this breaks the GABS MCP bridge for the whole session - forbid it explicitly and do not re-resume repeat offenders
- [[playtester-campaign-idle-rules]] (decision): Briefing rule - every unattended campaign observation prompt (e.g. private-war runs) must require parking the player in a friendly town's wait menu and re-checking speed 4 each poll
- [[safe-evaluation-breakpoint-anchor]] (howto): In DADG use DellarteDellaGuerra.Domain/DisplayCompilingShaders/DisplayShaderNumber.cs:25 as the evaluation breakpoint anchor for any campaign or mission code
- [[sendinput-foreground-guard]] (lesson): Agent-workflow rule - never SendInput to Bannerlord without a foreground-PID abort guard; Windows blocks focus stealing and keys land in the user's own app
- [[subagent-session-limit-resume]] (lesson): Background subagents that die on "session limit" can auto-resume after the reset and still complete; do not relaunch duplicates, and do not trust a 0-byte transcript or unchanged worktree as proof of death
- [[user-azerty-keyboard]] (lesson): The user plays on an AZERTY keyboard; Bannerlord binds by physical key position, so QWERTY-named hotkeys land elsewhere (War Sails "Z" ToggleSail = the W key)
- [[worktree-build-quirks]] (howto): DADG worktree builds fail on MAX_PATH and uninitialized submodules; verified subst + -m:1 + DADG_MODULES_ROOT recipe, plus the GameFolder deployment trap
