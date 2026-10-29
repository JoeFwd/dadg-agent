---
name: safe-evaluation-breakpoint-anchor
description: In DADG use DellarteDellaGuerra.Domain/DisplayCompilingShaders/DisplayShaderNumber.cs:25 as the evaluation breakpoint anchor for any campaign or mission code
type: howto
topic: workflow-branches
tags: [rider, breakpoint, anchor, displayshadernumber]
sources: [memory/safe-evaluation-breakpoint-anchor.md]
updated: 2026-10-18
---

# DADG evaluation anchor

Set a suspending breakpoint on `DellarteDellaGuerra.Domain/DisplayCompilingShaders/DisplayShaderNumber.cs:25` (`if (!config.IsShaderNumberNotifierEnabled)`). It is reached from `CompilingShaderNotifier.OnTick` (a `GameHandler` added in `SubModule.cs`), so it runs on the main thread and is live in both campaign and mission. The upstream guard `if (LoadingWindow.IsLoadingWindowActive || _tickCount <= 1) return;` throttles it to about once per second. It is DADG's own source, so no decompiled-source friction. Rules: [[evaluate-in-debugger-without-freezing-the-game]].

Generic rule: [[artillery-detachment-weight-gated-on-ammo-point]], [[debugger-pause-kills-gabp-game]], [[navmesh-presence-probe-in-rider]], [[rider-breakpoint-condition-no-ampersand]]
