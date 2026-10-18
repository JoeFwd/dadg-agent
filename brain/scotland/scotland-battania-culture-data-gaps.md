---
name: scotland-battania-culture-data-gaps
description: Scottish content using the reused battania culture crashed campaign start twice (kingdom policies, then notable templates); status and candidate fixes as of 2026-07-28.
type: incident
topic: scotland
tags: [scotland, culture, crash]
sources: [runtime-evidence/scotland-campaign-load, runtime-evidence/scotland-kingdom-load-gate]
updated: 2026-10-18
---

# Battania culture gaps (2026-07-28, 1.4.7)

1. `Kingdom.InitializeKingdom` NRE (`Kingdom.cs:530`): `Culture.DefaultPolicyList` null for the kingdom's `battania` culture. Fixed by switching the kingdom culture in `dadg_kingdoms.xml` to `Culture.empire`.
2. Next crash: `DefaultHeroCreationModel.GetRandomTemplateByOccupation` ArgumentNullException on the first settlement processed (`dadg_sco_finlaggan_town`, culture battania, occupation Artisan): `NotableAndWandererTemplates` null. Candidate fixes (not applied in the evidence): point those settlements at a complete culture, or populate battania's templates (likely also lord templates). Later runs show Scottish content loading, so this was resolved afterwards; the child-roster variant is in [[offspring-child-roster-per-culture]].

Generic rule: [[reused-culture-needs-complete-data]].

Related: [[reused-culture-needs-complete-data]], [[dadg-vanilla-override-pattern]]
