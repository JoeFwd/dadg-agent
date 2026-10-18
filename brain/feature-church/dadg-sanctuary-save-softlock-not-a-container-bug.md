---
name: dadg-sanctuary-save-softlock-not-a-container-bug
description: 2026-08-12 sanctuary save/load soft-lock looked like a missing Dictionary<Hero,CampaignTime> definition, but vanilla already registers it; adding it would have been a duplicate
type: incident
topic: feature-church
tags: [sanctuary, savedefiner, churchsaveabletypedefiner, softlock]
sources: [memory/vanilla-save-container-definitions.md]
updated: 2026-10-18
---

# Sanctuary soft-lock was not a container bug (2026-08-12)

`SanctuaryCampaignBehavior._fugitiveSanctuaryStarts` is a `Dictionary<Hero, CampaignTime>` and DADG's definer omits it, which looked like the cause. Vanilla already registers it ([[vanilla-save-container-definitions]]), so adding it would have been a duplicate registration masking the real cause.

`ChurchSaveableTypeDefiner` legitimately registers `Dictionary<Hero, Settlement>` (vanilla lacks it) and carries one redundant `Dictionary<MobileParty, Settlement>` line that vanilla covers; harmless, left alone.

Related: [[dadg-abbey-church-system]]
