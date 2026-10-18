---
name: private-war-synthetic-capture
description: Decision: because same-kingdom AI sieges never form an assault MapEvent, DADG transfers the goal when siege preparations complete.
type: decision
topic: feature-private-wars
tags: [private-wars, siege, capture]
sources: [doc/feudal-private-wars-manual-test-guide.md, doc/feudal-private-wars-design.md]
updated: 2026-10-18
---

# Private war synthetic capture

`PrivateWarSyntheticCapturePolicy`: when the besieger's preparations on the frozen goal are complete, the next hourly DADG callback transfers the fief exactly once. Defender strength is not a gate in this path.

Verified expectations: the old garrison disappears and exactly one replacement garrison exists; losing lords inside become prisoners of the besieger ([[private-war-prisoner-retention]]); fatigue epoch resets; the dispossessed side can form its own siege and retake it through the same path; the first holder must not trigger a second transfer because the finished camp is observed again.

Test shortcuts: `campaign.complete_siege_prep`, `campaign.create_siege`, `campaign.force_besiege` ([[private-wars-manual-test-howto]]).

Related: [[private-wars-overview]], [[siege-vanilla-1-4-facts]]
