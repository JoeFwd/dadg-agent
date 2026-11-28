---
name: dadg-companion-introduction-missing-capital
description: Companion introduction NRE from absent town_ES4; public dialogue replacement implemented with London fallback, deployment and live save round trip pending.
type: incident
topic: incidents-crashes
tags: [conversation, companion, wanderer, settlement, nre]
sources: [Rider live exception inspection 2026-11-27, DellarteDellaGuerraMap/ModuleData/settlements.xml line 12, DellarteDellaGuerraMap/ModuleData/strings/comment_strings.xsl line 135]
updated: 2026-11-27
---

Speaking to a wanderer with template `spc_wanderer_vlandia_9` crashed in vanilla `LordConversationsCampaignBehavior.conversation_wanderer_introduction_on_condition`: setting `IMPERIALCAPITAL` dereferenced the absent settlement `town_ES4`. This is the hardcoded lookup described in [[wanderer-introduction-hardcodes-imperial-capital]].

Live Rider evidence: `$exception.ToString()` showed `NullReferenceException` through `ConversationSentence.RunCondition`, `ConversationManager.ProcessPartnerSentence` and `MissionConversationVM.ExecuteContinue`. Evaluating `Settlement.FindFirst(x => x.StringId == "town_ES4") == null` returned true. Evaluating the name for `town_V6` returned `· London ·`, matching the map XML. DADG's surgeon backstory in `comment_strings.xsl` still uses `{IMPERIALCAPITAL}`.

Implementation (2026-11-27): `DellarteDellaGuerra/Dialogue/Api/Campaign/DadgWandererDialogueBehavior.cs` registers three higher-priority NPC lines, safely fills the native story variables and uses London with a text fallback. No Harmony or reflection is used. The native hiring and lord-conversation behavior remains installed. A separate persisted dictionary tracks repeated templates; older saves start this cosmetic history empty, so a story may repeat once. The exact dictionary container is already registered by vanilla. Missing-history and persistence tests pass.

The Map module has 68 authored eight-field companion stories, 50 political texts and adapted noble/company introductions. Removed 189 later-loading placeholder overrides, restored four removed political-text dependencies, and registered the full wanderer/world-lore transforms last. On 2026-11-28 the 652 new localization keys were converted to eight alphanumeric characters and the files grouped by culture, template, speaker and dialogue use. Native lookup IDs are retained. The installed content passes transform-order and source-catalogue coverage validation; all XSL compiles under .NET. Details: `src/doc/dialogue-overhaul.md`.

Correction (2026-11-28): the oath/rhyme wording in the native override language XML is only source-catalogue content. It does not replace English C# literals; that part remains incomplete. See [[english-localization-uses-inline-source]].

Status: source compiles and two targeted tests pass. Seven content files installed. A normal Release deployment is blocked by the game's DLL lock (`Bannerlord.Cannons.API.dll`). During implementation the original crash session was replaced externally by a running `Launcher.Standalone` session; it was left running, and the user has not yet authorized its restart. A real existing-save load/conversation/save/reload check remains pending.

Related: [[wanderer-introduction-hardcodes-imperial-capital]]
