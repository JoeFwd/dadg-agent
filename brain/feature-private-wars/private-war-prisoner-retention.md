---
name: private-war-prisoner-retention
description: Decision: lords captured in a private war stay prisoners during the war and are released when it ends.
type: decision
topic: feature-private-wars
tags: [private-wars, prisoners]
sources: [doc/feudal-private-wars-manual-test-guide.md, doc/feudal-private-wars-design.md]
updated: 2026-10-26
---

# Private war prisoner retention

Vanilla releases captives when captor and captive are "not at war" (peace sweep, captivity check), which is always true inside one kingdom. `PrivateWarPrisonerRetentionPatch` blocks that release while the war is Active; escape attempts are never blocked. When the war concludes (score +-100 or principals split kingdoms) every captive the war created on the opposing side is released. Siege prisoners now come from the real wall assault (vanilla post-battle capture); lords who sat out inside the fief are not captured (2026-10-26).

Related: [[vanilla-hostility-consumer-sites]], [[private-war-real-siege-assault]]
