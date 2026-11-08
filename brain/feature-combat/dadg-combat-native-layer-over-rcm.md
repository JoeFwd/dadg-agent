---
name: dadg-combat-native-layer-over-rcm
description: Decision 2026-11-06 - DADG built its own combat layer instead of depending on Realistic Combat Mod (Nexus 11507) or RBM; RCM's keyword classifier, firearm blind spot and XSLT side effects, RBM's 1.4.8 drop
type: decision
topic: feature-combat
tags: [combat, rcm, rbm, dependencies]
sources: [doc/combat-overhaul-analysis.md (retired 2026-11-07), RCM 1.4.2 decompile, RBM commit 4e491d9]
updated: 2026-11-07
---

# Native combat layer, not RCM or RBM

DADG has its own combat layer ([[dadg-combat-overhaul]]). Neither RCM nor RBM is a dependency, and agents should not propose them again unless their facts change.

**Realistic Combat Mod (RCM)** is by Ulfkarl, Nexus 11507, v1.4.2. It is a closed 129 KB DLL with no licence file. It is not part of RBM. It was read from a decompile and never run.
- **It classifies armour from keywords** in item ids and names. 92 of 115 DADG helmets came out as medium plate. Partial plate rated too high and mail too low, and it gives one material per item. That kills per-part materials such as cloth-sleeved brigandines, which were the reason for building our own.
- **Firearms get no rules of their own.** A 280 arquebus shot did about 11 to a plate chest.
- **It counts the blade factor twice** (damage ∝ factor^1.5), and polearm thrusts get ×2.3 on non-plate.
- **Four of its 39 XSLTs touch every item.** If it loads after DADG, they rewrite armour value, weight and `tier_override`, and break `flying_mesh` (a musket ball flies as `musketball_hidden`). Its page advises loading it last.
- **Its config path is hardcoded and it is single-player only.** That rules it out for coop: [[coop-compat-project]].

**RBM (RealisticBattleProject)**
- v4.6.0 dropped 1.4.8, and v4.8.x needs 1.5.6+.
- It changes data meanings: head armour median 67 vs DADG's 24, and bow `missile_speed` means draw weight.
- It replaces `MBObjectManager.MergeTwoXmls` and patches combat, agents and AI wholesale.
- It has no visible firearm handling and no licence.

**What was taken from the analysis:** the vanilla formula leaves plate close to immune to cuts (a 100 cut does 3.7 to 85 armour) while a bullet nearly one-shots it. The fix needed armour per hit location, a material per blow type, and a weapon ladder ([[dadg-weapon-ladder]]). The ladder must never ship alone on the vanilla formula: lower swings make plate even stronger.

Related: [[dadg-combat-overhaul]], [[vanilla-blow-damage-formula]], [[bannerlord-xml-load-abort-semantics]]
