---
name: customspawns-failed-invasion-recovery-healthy
description: Live check on 2026-09-20 showed a retreated CustomSpawns invasion returns to a healthy retryable Search state.
type: incident
topic: feature-customspawns
tags: [customspawns, invasion, recovery]
sources: [runtime-evidence/customspawns-failed-invasion-rider-only, runtime-evidence/customspawns-invasion-recovery-flags-rider-only]
updated: 2026-10-18
---

# Failed invasion recovers cleanly (PASS, 2026-09-20)

Branch `implement-new-party-behaviour`, debugger-only inspection. After a retreat: phase `Search`, target null, operation clock advancing 1/24 day per hour, patrolling home via `PatrolOrRemainApplicable` with CustomSpawns steering active, group unsuspended and unspent, no foothold. `LegacyRecoveryPhase` = 5 migrates to `Search` or `Approach`. Zero reinforcement values before a foothold are expected.

Two sibling "health" reports had no live process and are static inference only. Generic phase/threshold notes: [[invasion-style-party-state-machine-observed]].

Related: [[invasion-style-party-state-machine-observed]]
