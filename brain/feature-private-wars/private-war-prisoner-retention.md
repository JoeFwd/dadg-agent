---
name: private-war-prisoner-retention
description: Decision: lords captured in a private war stay prisoners during the war and are released when it ends.
type: decision
topic: feature-private-wars
tags: [private-wars, prisoners]
sources: [doc/feudal-private-wars-manual-test-guide.md, doc/feudal-private-wars-design.md]
updated: 2026-10-18
---

# Private war prisoner retention

Vanilla releases captives when captor and captive are "not at war" (peace sweep, captivity check), which is always true inside one kingdom. `PrivateWarPrisonerRetentionPatch` blocks that release while the war is Active; escape attempts are never blocked. When the war concludes (score +-100 or principals split kingdoms) every captive the war created on the opposing side is released. On a synthetic capture, the losing lords in the fief are made prisoners by DADG because no assault ran.

Related: [[vanilla-hostility-consumer-sites]], [[private-war-synthetic-capture]]
