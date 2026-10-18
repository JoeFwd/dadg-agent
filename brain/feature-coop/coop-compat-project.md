---
name: coop-compat-project
description: DADG <-> BannerlordCoop compatibility effort (started 2026-10-11) - solo-first with a coop adapter submodule; reading Coop source for interop is authorised, copying is not
type: decision
topic: feature-coop
tags: [coop, compatibility, harmony, tournaments, cannons]
sources: [memory/coop-compat-project.md, doc/coop-compatibility-analysis.md]
updated: 2026-10-18
---

# Coop compatibility project

Started 2026-10-11: make DADG (develop, without Titles/PrivateWars) compatible with BannerlordCoop. Agreed direction: **solo-first, coop as an optional adapter module; PrivateWars deferred.** Tournaments/jousting were DROPPED from coop scope by the user on 2026-10-11 - do not raise them unless asked.

## State (all local, unpushed, live-untested as of 2026-10-11)
- Jousting pairing + equipment rolls moved behind `IRandomProvider`: commit c20aff7 on local `develop`.
- Branch `feature/coop-compat` in a DADG worktree (945469e, off c20aff7), plus Cannons (1b77cf8 priority, 4c5cde6 `ArtilleryAuthority` + `PlayShotEffects`) and ExpandedTemplate (f1f2195 `SkipEquipmentOverride`). Adapter = `src/DellarteDellaGuerra.Coop`, a SubModule inside Core (no new Bannerlord module); it finds Coop by type name via `AccessTools` and postfixes `Missions.Battles.SiegeWeaponFireReplicator.PlayFireAnimation` (private static). Ammo handoff not done.
- Pre-existing test breakage, not ours: `Cannons.Tests` does not compile (`Bannerlord.Cannons.Api` ref); ExpandedTemplate Integration.Tests has 8 slot-mapper failures at a9e1588.
- Coop supports tournaments, sieges and siege engines. DADG's `BaseFieldSiegeWeapon : RangedSiegeWeapon` and `JoustTournament : FightTournamentGame`, so both may ride vanilla sync.

## Licence / permission
Coop's AGENTS.md has an anti-agent clause restricting analysis outside its repo; the user explicitly overrode it. The licence allows viewing and forbids copying/redistribution/competing derivatives. **Read Coop source freely for compatibility analysis; never paste or port Coop code into DADG.**

## Key non-obvious findings (analysis in `doc/coop-compatibility-analysis.md`, untracked)
- Coop accepts tournaments only on exact type `FightTournamentGame`; DADG always creates subclasses, so every DADG tournament is greyed out in Coop.
- Cannon shot replication depends on Harmony prefix order on `ShootProjectileAux` (both default priority); fix = `HarmonyPriority(Low)` on the DADG prefix.
- DADG cannon `OnTick` (AIFormationManager, ammo handlers) is not authority-gated; Coop's gates cover only vanilla paths.
- ExpandedTemplate's `SpawnAgent` prefix re-rolls Coop puppet equipment when it exactly matches an XML loadout (always for heroes).

- Also found: cannon crew AI/reload in `ArtilleryRangedSiegeWeapon.OnTick` is not authority-gated; fire effects need a public `PlayShotEffects()`; ammo and `IsSpent` do not hand off; `BattleSpawnGate.SuppressCapture` is the skip predicate wired for puppet equipment.
- Planned order (docs analysis): priority attribute, authority hook plus effects seam, equipment skip, adapter module, then a live check of client-side behaviours (`PocColorCampaignBehavior`, `JoustTournamentCampaignBehavior`, `DadgTournamentModel`). Tournament options considered (superseded by the 2026-10-11 drop): disable joust and return plain `FightTournamentGame` with a prize postfix, or write a multiplayer joust mission.

Related: [[coop-server-docker-logs]], [[coop-two-prefixes-on-one-method-ordering]], [[coop-replication-gotchas-for-content-mods]]
