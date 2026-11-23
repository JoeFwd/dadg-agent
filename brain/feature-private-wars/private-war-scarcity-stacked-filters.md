---
name: private-war-scarcity-stacked-filters
description: Why private wars were rare: five stacked filters, and the NoActiveWar dispersal that killed armies.
type: incident
topic: feature-private-wars
tags: [private-wars, analysis, scarcity]
sources: [doc/private-war-scarcity-analysis.md]
updated: 2026-11-23
---

# Private war scarcity stacked filters

Analysis 2026-10-13: AI-declared private wars almost never happened because five filters stacked (claim availability, same-kingdom gate, strength and desire gates, goal selection, and the declaration cooldown/eligibility). Even declared wars produced few real battles because goal armies were disbanded by vanilla's `NoActiveWar` check.

Status: the dispersal is FIXED by `GoalArmyNoActiveWarDispersalPatch`; filter tuning remains a design choice. See [[army-dispersal-noactivewar-check]].

Re-checked on 1.5.7 (2026-11-23, 1471->1479 campaign): zero natural declarations is by design, not a port regression. Every inter-house blood claim is Weak, and `WeakClaimPolicy` only lets a Weak claim through against a female or under-18 holder, so `press_claims` prints "claim too weak". The claims that do pass are on the claimant's own dignities. Those are pressed by a cadet pretender whose side is only his own party plus pledges, against the whole house and its vassals. That side never reaches `EvaluatePressClaimUseCase`'s 1.25:1 floor, so it prints "press score 0 < 0.8". `ClaimPressureOverRealContentTests.NoClaimIsWorthPressingWhileTheRealmIsAtPeaceWithItself` pins this (14/14 green on 1.5.7). That harness leaves out the 18 hand-authored `<Claim>` entries in `config/titles.config.xml` (a missing `strength` attribute means Strong). These are the only Strong claims between different houses, and live probes (`press_claims`, 1479 save) show all of them blocked. Five cross the York (`vlandia`) / Lancaster (`sturgia`) / Scotland (`khuzait`) realm line and stop at `NotSameRealm`: Neville of Middleham→Percy, Clifford→Stanley, Beaumont→Hastings, Herbert→Tudor and Tudor→York. The others involve a royal house (York→Herbert, Lancaster→Woodville, Lovell→Lancaster, Erskine/Crichton→Stewart) and stop at `RoyalHouseInvolved`. With the current content no natural claim war can fire.

Related: [[private-war-one-goal-army-per-side]]
