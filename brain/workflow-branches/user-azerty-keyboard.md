---
name: user-azerty-keyboard
description: The user plays on an AZERTY keyboard; Bannerlord binds by physical key position, so QWERTY-named hotkeys land elsewhere (War Sails "Z" ToggleSail = the W key)
type: lesson
topic: workflow-branches
tags: [azerty, keyboard, hotkeys, inputkey, agent-workflow]
sources: [memory/user-azerty-keyboard.md]
updated: 2026-10-18
---

# The user has an AZERTY keyboard

Bannerlord's `InputKey` values are scan codes for physical key positions, so a hotkey that docs or code call "Z" (War Sails ToggleSail, InputKey 44) is the key labelled **W** on the user's keyboard. Likewise Q<->A and W<->Z.

**Why:** on 2026-10-03, "Z doesn't trigger the sails" was just this; pressing W works. Not a DADG bug (same session: [[ws-fmod-sail-sound-hang]]).

**How to apply:** when telling the user which key to press, give the AZERTY key (or say "the key Bannerlord shows in the hint"). Check the layout before debugging a "key does nothing" report.

Related: [[sendinput-foreground-guard]]

Generic rule: [[ws-naval-quirks]]
