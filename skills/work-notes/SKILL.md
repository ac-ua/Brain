---
name: work-notes
description: Turn work notes, call transcripts, meeting notes or a work session's results into structured Notion pages in Aurélien's UnifyApps CRM — the right Opportunity (client work) or Project (cross work) page, with an AI-maintained brief on top, one structured entry per meeting, linked People and Account, tasks and durable learnings. Use whenever Aurélien pastes or shares a transcript or notes ("voici le transcript", "structure mes notes", "mets à jour l'opportunité X", "ajoute ce call à GeBBS"), at the end of any Work session, or when a new opportunity or work project starts.
---

# work-notes

Notion is Aurélien's system of record for work. This skill keeps it AI-native: every page starts with a brief a
session can load in seconds, meetings are structured instead of pasted, and nothing pro lives only on a Mac or in a
session. Template and examples: [`references/template.md`](references/template.md).

## Where things go (Work › Unify Apps)
| Database | Data source | Holds |
|---|---|---|
| 📝 Opportunities | `collection://28e19ca7-9893-805c-80b7-000bf7bd294c` | everything tied to a client: one page per opportunity (`<Account> - <New Client / use case>`), property `Activity Level` (0. Burning … 5. Closed Lost), relations `📁 Account`, `🧑‍🤝‍🧑 People` |
| 📂 Accounts | `collection://28e19ca7-9893-80f2-a33a-000ba01373b4` | one page per company: short profile, link to its opportunities |
| 🧑‍🤝‍🧑 People | `collection://28f19ca7-9893-8091-8239-000bf5a55a98` | UnifyApps-side people (Role: Solution Architect, Sales, Leader, Partner; Region) |
| 🏗️ Projects | `collection://28119ca7-9893-8046-bc4a-000bdfe51def` | cross work not tied to one client (apps, events, enablement, skills loop); `Status`, `target` |
| 🧠 Memories | `collection://5b6902fc-e510-4975-b133-06e9273f602e` | durable learnings, Domain Work |
| 📋 Tasks | `collection://d2dce682-22a5-4e39-b0d3-75b9399b5c47` | Aurélien's own to-dos, Context Work |

Client contacts are not rows in People: they go in the brief's People section (name, title, role in the deal).

## Steps
0. **Recordings** (mp4, m4a, a meeting with no transcript): transcribe locally on the work Mac (`mlx-whisper`, see
   `skills/video-edit/references/tooling.md`), and for screen-shared calls take one frame a minute to tie what was
   shown to what was said. The transcript then goes through the steps below like any other; the recording stays in
   the work Drive.
1. **Classify the input.** Client meeting or deal work → Opportunity. Internal or cross work → Project. Several
   topics in one transcript → split them. A durable lesson (platform fact, practice, pitfall) → also Memories.
2. **Find the page.** Search Notion by account and opportunity name. A page exists for most topics: enrich it.
   None fits → create it from the template (Opportunity: set Activity Level, link or create the Account; Project:
   Status). Fetch the data source before creating a row.
3. **Add the meeting entry** in the page's **Meeting log**, newest first, as an h3 toggle
   `DD/MM/YYYY · <type> · <title>` (types: discovery, demo, workshop, internal sync, solutioning, exec review…).
   Inside: Attendees · Summary (3–6 lines) · Decisions · Next steps (owner, date) · Numbers/facts heard (with who
   said them) · then a nested toggle `Transcript` holding the raw transcript or notes as given. Never paste a
   transcript outside that nested toggle.
4. **Update the brief** at the top (template sections). Change only what the meeting changed; date new decisions;
   move answered questions out of Open questions; keep figures with their source and status (client figure / our
   model / validated). Refresh `last update` in the heading. Keep it ≤ ~100 lines: older detail lives in the log.
5. **Relations and properties.** Link the Account and the UnifyApps People present. Set Activity Level only when
   the meeting clearly moves it (say so in the reply).
6. **Spin-offs.** Aurélien's own next steps → Tasks (Context Work, Due if stated, link the page in the task).
   Durable learnings → Memories (Domain Work, Scope Work), one row each, deduplicated. A change to how work is done
   → Brain Inbox.
7. **Account questions** ("what does X know of the platform", "which calls did he attend", "a short paragraph on
   this account, same style as the other one"): answer from the brief and the meeting log, citing the entries;
   short blurbs go through `message-drafting`.
8. **Work that continues in another session:** add a `Handoff` toggle under the brief (`session-handoff`): state,
   next steps, where the files are, the prompt for the next session. Remove it once picked up.
9. **Reply in three lines:** what was written where (links), what changed in the brief, what needs his eye
   (unclear attendee, conflicting figure, Activity Level change).

## Rules
- Distil, don't dump: decisions, facts, numbers and next steps in the brief; raw text only in the nested toggle.
- Separate what the client said, what UnifyApps proposed and what Claude suggests; never record a suggestion as a
  decision. Unsure → `[to confirm]`.
- Never secrets: API keys and real passwords stay in the password manager. Demo-environment logins Aurélien wrote on
  a page stay where they are (his call); don't remove them and don't copy them into the brief or anywhere else.
- Existing content written by Aurélien stays untouched: add the brief above it and new entries in the log; don't
  rewrite or reorder his notes.
- Files stay in the work Drive; the page holds links and names.
- Builds happen in the UnifyApps platform; link their Configuration Guide in Assets.
- Notion free plan: fetch and search, no SQL loops. Fetch before `update_content`; copy `old_str` exactly.
- Big pages (over ~100k characters): read the brief and the latest log entries first; read old transcripts only if
  needed.

## Related
`cep-workbook-filler` (detailed MEDDPICC account plan in the work Drive; the brief links to it) ·
`poc-use-case-filler` · `demo-prep` · `case-for-change` · `message-drafting` · `unifyapps-format` (or the team
plugin's `unifyapps-brand-deck`) · `explainer-video` · `session-handoff` · `session-close` (Work sessions end with
this skill).
