---
name: customspawns-component-identity-outcome
description: CustomSpawns identity moved onto party components (commit bc9e05f); old saves incompatible by design; NUnit adapter cannot run on .NET 10.
type: incident
topic: feature-customspawns
tags: [customspawns, saves, outcome]
sources: [sdd/customspawns-component-identity, plans/customspawns-ai-workflow-investigation.md]
updated: 2026-10-18
---

# Customspawns component identity outcome

- Commit bc9e05f6 in the CustomSpawns submodule: `CsPartyData` and legacy repair removed; `CustomSpawnIdentity` (primary template id + primary/supporting flag) lives on `CustomSpawnsPartyComponent` and `CustomSpawnsBanditPartyComponent`.
- Existing CustomSpawns saves intentionally incompatible.
- Builds target v1.4.6 (`-p:OverrideGameVersion=v1.4.6`); no Harmony in CustomSpawns.
- Focused NUnit tests compile but cannot run: NUnit 3.13.3 adapter throws "Unknown framework version 10.0" on the .NET 10 preview SDK.
- Review fixes: keep native bandit semantics; add concrete type-definer assertions; drop the orphaned `SpawnDao` ctor parameter.
- The AI-workflow plan is investigation scope only; no implementation recorded.

Related: [[party-component-owned-identity-pattern]], [[customspawns-partyowner-must-be-leader]], [[customspawns-army-infeasible]]
