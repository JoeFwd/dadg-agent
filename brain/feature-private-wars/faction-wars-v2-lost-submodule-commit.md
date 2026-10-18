---
name: faction-wars-v2-lost-submodule-commit
description: PrivateWars 98ccbc97 is gone from every object store, but its source was recovered by decompiling the 2026-09-08 DLLs and PORTED onto develop as bd1fd24 (verified faithful)
type: incident
topic: feature-private-wars
tags: [privatewars, submodule, recovery, port, worktree]
sources: [memory/faction-wars-v2-lost-submodule-commit.md]
updated: 2026-10-18
---

# Lost PrivateWars commit 98ccbc97 (RESOLVED by port, 2026-09-15)

Branch `feature/add-internal-faction-wars-v2` (tip `36db43b`) pinned `src/submodules/PrivateWars` at `98ccbc97de1356372f10455b98d5ad9e89c2b056`, which exists in no object store, is not on origin (re-verified 2026-09-14) and appears in no reflog. The commit is unrecoverable, but the source is not.

- Deployed binaries `Modules/Bannerlord.PrivateWars/bin/<platform>/Bannerlord.PrivateWars{,.Domain}.dll` (built 2026-09-08) were built from the lost commit and carry the phase-5/6 supporter surface: `PrivateWar` with `AttackerSupporters`/`DefenderSupporters`, `IDeclarePrivateWarUseCase.Execute` (8 params), `WarSideResolver.ResolveSide(clanId, war, getSuzerain)`, `DeclarePrivateWarUseCase`, `PrivateWarStateSerialiser`. Recovered tree kept at `Modules/DellarteDellaGuerra.Core/recovered-privatewars-98ccbc9/` (114 .cs).
- The **API DLL never existed** in that build set (zero `privatewarsapi` case-insensitively; four on-disk API DLLs are all 2026-08, `Supporters=no`). Stop hunting. Reconstruct from the pre-supporter API source (legacy repo `Modules/Bannerlord.PrivateWars`, HEAD `a18d664`; submodule copy 2026-08-11) plus the 9-arg target signature pinned by `PrivateWarDeclarationAdapter.cs`: `attackerClanId, defenderClanId, ClaimCasusBelli.ClaimType, titleId, mainGoalSettlementId, fiefSnapshot, day, attackerSupporters, defenderSupporters`.
- **DONE 2026-09-15:** ported as `bd1fd24` on submodule branch `develop` on top of `892339c` (merged, not overwritten: `98ccbc9` forked at `cdea5e3` and never held the claimant fix). 13 files, +150/-50; build clean, 15/15 tests pass. 5 of 6 ported Domain files decompile byte-identically to the lost commit. `origin/develop` also points at `bd1fd24`; the DADG gitlink was **not yet re-bumped**.
- Traps: once the campaign behaviour raises `WarResolved`, the API's own raise inside `ResolveWar` double-fires, so route everything through the lazy relay. `src/submodules/PrivateWars` in the main checkout was untracked on `develop` and unpushed, the same pattern that caused the loss.
- **2026-09-29:** the faction-wars-v2 worktree was removed; its submodule held 5 unpushed commits (`feature/cross-kingdom-private-wars`, tip `016a7bd`, atop `bd1fd24`). They were fetched into the main checkout as a local, still unpushed branch.

Method and general pitfalls: [[submodule-source-recovery-by-decompile-diff]]. Related: [[worktree-build-quirks]]
