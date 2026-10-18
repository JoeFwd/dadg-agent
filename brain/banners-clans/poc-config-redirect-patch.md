---
name: poc-config-redirect-patch
description: PocConfigReaderOverriderPatch redirects the POC mod's config reads to DADG's config/poc.config.json.
type: reference
topic: banners-clans
tags: [poc, config, banners]
sources: [doc/poc.integration.md]
updated: 2026-10-18
---

# Poc config redirect patch

`PocConfigReaderOverriderPatch` redirects the POC integration's config reader so the runtime authority for clan colours and banners is `config/poc.config.json` in the DADG module. This is why clan XML banner edits can be overridden by POC ([[poc-overrides-english-clan-banners]]).

Source docs: doc/poc.integration.md.

Related: [[poc-overrides-english-clan-banners]]
