---
name: dadg-caravan-camel-alias
description: FIXED 2026-10-11 - DADG reuses the aserai/khuzait culture ids for Anglo Irish and Lowland Scots; camel aliased to the mule in dadg_pre_native_items.xslt after Dumfries' rebel clan caravans crashed
type: incident
topic: feature-other
tags: [caravan, camel, xslt, fixed]
sources: [memory/caravan-camel-icon-hardcoded.md]
updated: 2026-10-18
---

# DADG caravan camel NRE (FIXED 2026-10-11)

DADG reuses the `aserai` and `khuzait` culture ids for Anglo Irish and Lowland Scots. Seen 2026-10-11 when Dumfries rebelled: its rebel clan inherits the settlement culture (khuzait), so its caravans asked for vanilla's hardcoded `camel` item, which DADG strips.

Fix: `DellarteDellaGuerra/ModuleData/items/dadg_pre_native_items.xslt` has a third rule turning vanilla `Item[@id='camel']` into a copy of the mule with `is_merchandise=false`. Camel-monster items are still stripped.

The user prefers XML/XSLT fixes over Harmony code ("instead of patching it with code, check if there is a way to prevent it with xml/xslt").

Generic rule: [[caravan-camel-icon-hardcoded]]. See [[dadg-vanilla-override-pattern]].
