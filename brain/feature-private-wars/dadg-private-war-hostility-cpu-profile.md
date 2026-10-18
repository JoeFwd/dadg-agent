---
name: dadg-private-war-hostility-cpu-profile
description: A PerfView capture showed private-war hostility / war-side / suzerainty / title-scan work using ~76% of main-thread CPU for the first ~50 s, collapsing to ~0.01% after a clan defection / kingdom-change event.
type: incident
topic: feature-private-wars
tags: [private-wars, performance, perfview, titles]
sources: [src/.tmp/perfview-analysis/comparison.csv, src/.tmp/perfview-analysis/summary.json, src/.tmp/perfview-analysis/find-transition.py]
updated: 2026-10-18
---

# Private-war hostility CPU hot spot

Capture: ~302 s, 1.55 M samples. Inclusive CPU by frame-name bucket: private_wars 41.6 s, hostility 35.8 s, war_side 35.8 s, suzerainty 36.3 s, title_scan 35.8 s (nested, overlapping), shader_compile 94 s (other threads), gc 4.9 s, ai_hourly 0.2 s, claim_pressure 0.5 s, nameplates 0.05 s.

Main thread, seconds 10-50: 37,660 ms CPU of which hostility 28,525 ms (75.7%). Seconds 60-100: 39,268 ms of which hostility 4 ms (0.01%). The step change coincides with ~50.5 s events matching `ChangeKingdomAction.ApplyByJoinToKingdomByDefection` (clan defection, 239 samples) and `PrivateWarCampaignBehavior.OnClanChangedKingdom` / `ResolveWar`.

Reading: hostility/suzerainty/title-scan evaluation was pathologically expensive in one world state and cheap after a defection reshuffled kingdoms. Fix status is not recorded in the sources; verify in current code before assuming it is resolved.

Related: [[pw-sides-dejure-crosses-kingdoms]], [[dadg-lord-defection-sources]], [[campaign-perf-measurement-method]]
