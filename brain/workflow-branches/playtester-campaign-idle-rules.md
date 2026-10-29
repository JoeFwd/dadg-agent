---
name: playtester-campaign-idle-rules
description: Briefing rule - every unattended campaign observation prompt (e.g. private-war runs) must require parking the player in a friendly town's wait menu and re-checking speed 4 each poll
type: decision
topic: workflow-branches
tags: [playtester, subagent, observation, wait-menu, agent-workflow]
sources: [memory/playtester-campaign-idle-rules.md]
updated: 2026-10-18
---

# Playtester campaign-idle briefing rules

The user, 2026-10-11, saw runs stall with the game paused and the playtester idle. Put the rules from [[campaign-menu-without-wait-zeroes-ai-dt]] in every campaign-observation playtester prompt, next to the existing "resume GABP bridge exceptions immediately" rule. The 2026-10-13 discovery that a non-wait menu zeroes AI dt is the silent trap behind it.

Generic rule: [[debugger-pause-kills-gabp-game]]
