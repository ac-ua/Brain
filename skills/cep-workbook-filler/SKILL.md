---
name: cep-workbook-filler
description: >
  Creates and updates UnifyApps CEP (Customer Engagement Plan / account planning) Google Doc workbooks - the multi-tab MEDDPICC-style doc covering Challenge/Educate, Economic Buyer, Champion, Decision Committee, Competition, Budget, and 25+ other tabs. Use this skill whenever the user asks to "fill the CEP workbook", "create/build a CEP for [account]", "start a workbook for [prospect]", "update the [account] workbook", "put together an account plan", or shares call transcripts, decks, or notes and asks to get them into the workbook. Also trigger when the user names a Google Doc account-planning workbook link and asks to populate or refresh it with new call or meeting information. Handles both starting a brand-new workbook for a new account (by copying the master template) and updating an existing filled workbook with new information, date-stamping every addition so the update history stays visible.
---

# CEP Workbook Filler

The CEP workbook is a single Google Doc with roughly 35 tabs (Google Docs' native tabs feature, not spreadsheet tabs). Each tab covers one MEDDPICC / account-planning topic - Economic Buyer, Champion, Decision Committee, Budget, Competition, and so on. Read `references/sections.md` before filling anything: it lists every tab and the built-in definition of what belongs in it, plus example phrasing pulled from a well-filled workbook. Correct tab targeting is the core of doing this well - getting a fact into the wrong tab is as bad as leaving it out.

There is no API for writing into a specific Google Docs tab, so filling happens through the browser (`mcp__claude-in-chrome__*` tools): open the doc, click into the target tab in the left sidebar, click into the body, and type.

## Two modes

**New account** - no existing workbook, or the user wants to start fresh.
Copy the master template (Drive file id `1Kr61vmC8Ji3VldN1nAWbEDaMvoB76xCTallEWc3iJ-s`) with the Drive `copy_file` tool, title the copy "{Account Name} Workbook", put it in the account's work Drive folder (`01_Accounts/<Account>`, see `docs/drive-map.md`; the template itself sits in `02_Assets/Templates`), then fill it tab by tab as described below. Every tab starts empty except for its italic instruction text.

**Existing account** - the user gives a link to an already-started workbook plus new source material (a follow-up call, a new deck, updated notes).
Open that doc directly and add to it. Never delete or rewrite what's already there - see "Updating vs. overwriting" below.

## Ground rules

Read these before touching the doc - they matter more than getting through all the tabs quickly.

- **Never invent.** Only write something in a tab if it is explicitly stated in the source material the user gave you (transcript, deck, notes, email). If a tab has no supporting material, leave it blank. Don't guess, don't pad it with generic sales language, don't infer a detail (a title, a budget number, a timeline) that wasn't actually said.
- **When in doubt, leave it out.** If you're not sure a detail belongs in a section, or not sure it's actually grounded in the source, don't add it.
- **Keep the italic instruction text.** It's the tab's built-in definition of scope. Don't delete or edit it - add real content below it.
- **Match the doc's existing voice.** Narrative tabs (Challenge/Educate, Current State, Negative Consequences, Future State, Value...) read as prose paragraphs. Structured tabs (Economic Buyer, Champion, Coaches, Detractors, the Decision Committee tabs, Partners tabs) use bold labels (Name / Role / LinkedIn / Motivation) plus bullets. `references/sections.md` has real excerpts of both styles.
- **Committee/Partner parent tabs are checklists, not detail tabs.** "Decision Committee" and "Partners" are summary checklists of roles; the actual names, titles, and LinkedIn profiles go in their child tabs (AI/IT/Business Decision Committee; Services Partner / Cloud-Tech Partner).
- **Leave the "Client Workbook Checklist" tab alone** unless the user explicitly asks you to check off a stage - it's a sales-process tracker, not a content tab. Only use "General Notes" for material that is real and grounded but doesn't cleanly fit any other tab.

## Updating vs. overwriting

When a tab already has content and you're adding something new from a fresh source:

- **Append, never delete.** Add the new material after what's already there.
- **Date-stamp every addition** so there's a clear record of when each fact was added:
  `<existing content> [Aug 3, 2026] <new content>`
- **Corrections don't erase history.** If new information contradicts something already written (a timeline slipped, a stakeholder changed), don't delete the old line - add the correction with its date so both are visible and anyone reading the doc can see how the deal evolved.
- Use today's date (check it rather than assuming) for the bracketed tag.

## Step by step

1. **Confirm the account name**, and if updating an existing workbook, **get the doc link**. Ask if either is missing rather than guessing.
2. **Read all source material in full** before touching the doc - transcripts, decks, notes, whatever the user provides. Do this first so you're mapping from a complete picture, not tab-by-tab guessing as you go.
3. **Go through `references/sections.md` tab by tab.** For each tab, check whether the source material has anything grounded that belongs there per that tab's definition. Draft content only for tabs with real material; skip the rest.
4. **Get the target doc:**
   - New account: `copy_file` the template, rename it "{Account Name} Workbook", note the new doc's URL and file id.
   - Existing account: use the URL the user gave you.
5. **Fill it via the browser.** Navigate to the doc. The tab list lives in the left sidebar of Google Docs - click into each tab you're filling, click into the body (below the italic instructions, or after the last existing line if updating), and type the drafted content. Start a line with "- " for a bullet (Docs auto-formats it). Don't let manual bolding of labels slow you down if it's fiddly to select-and-bold via keystrokes - getting the real content in correctly matters more than perfect formatting fidelity.
6. **Report back**: which tabs were filled or updated, which were left blank and why (no grounded source material for that tab), and the doc link.

## Reference

`references/sections.md` - full tab list, each tab's built-in definition, and example excerpts (Economic Buyer, Champion) showing the expected tone and structure.
