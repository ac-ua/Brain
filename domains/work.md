# Domain: Work

Aurélien's job at UnifyApps (Solution Architect): accounts, POCs, demos, decks, configuration guides.
Notion domain page: **💼 Work** (`40619ca798938177a168dccd513c8e4b`); the Unify Apps tree (CRM, Demo Nuggets, Trainings)
sits under it. Practices and pitfalls: 🧠 Memories with Domain = Work.

**Notion is the system of record for work.** Each opportunity page in the CRM starts with a **deal brief**
(AI-maintained, ~60–100 lines): snapshot, people and stance, numbers (source, validated or not), solution and what is
built, dated decisions, open questions, next steps, assets, meeting log. Transcripts sit below it. Every `Work ·`
session reads the brief at start and updates it at close; durable learnings go to Memories. Skill `work-notes` does
it: transcripts and notes → the right Opportunity (client) or Projects row (cross work), brief on top, one
structured entry per meeting, tasks and learnings. Template: `skills/work-notes/references/template.md`.

## Where work runs
Pro work runs in a **local session on the work Mac** (browser, pro files, the team plugin). The work Mac reads `ac-ua/*`
but cannot push: ways of working found there go to the Brain Inbox.

## How each capability applies
**chief-of-staff.** Pro tasks in Tasks with Context = Work. Meeting prep and follow-ups from the pro connectors (work
Drive, Slack). Drafts only; Aurélien sends.

**builder.** Builds happen *inside the UnifyApps platform* (Orbit UAT: config apps, workflows, agents, Context Graph),
with the team plugin `Unifyapps-Internal/unifyapps-builder-skills` — not with `build-webapp`. Every build ends with a
Configuration Guide; every POC asset carries the customer tag; the platform fetches external data, not Claude.

**content-studio.** The story comes from `case-for-change` (storyline, deck lessons); slides are built with the
team plugin's `unifyapps-brand-deck` (Playbook v4), `unifyapps-format` only where the plugin isn't installed. Deck
conventions also in Memories (section arc, ~30% shorter, audit content kept out of client decks, yellow
`[to be confirmed]` placeholders). Demos: `demo-prep`. Messages: `message-drafting`.

## Skills
`work-notes` · `demo-prep` · `case-for-change` · `message-drafting` · `cep-workbook-filler` (account plans) ·
`poc-use-case-filler` · `unifyapps-rfp-rfi-response-template` · `unifyapps-format` (decks, fallback) · `explainer-video`.
All of them live in `ac-ua/brain`. The team plugin (`Unifyapps-Internal/unifyapps-builder-skills`) is shared by all
the Solution Architects, installed separately and never changed directly: it only receives platform learnings about
what it already covers, through its twice-weekly loop. None of Aurélien's own skills go there.

## Rules
- Nothing personal goes to pro systems. Pro files live in the work Drive (`ac@unifyapps.com`) and may be copied to
  the personal Drive: from the work Mac, through the Google Drive app's personal folder in Finder (2026-10-29).
- Work Drive layout (applied 2026-10-29, `docs/drive-map.md`): 00_Inbox · 01_Accounts/<Account> (named like the
  Notion Account) · 02_Assets · 03_Demos · 04_Events · 05_Internal · 99_Archive. Nothing at the root; the deal brief
  links the account folder.
- Pro context may be stored in Notion and this repo (Aurélien's call, 2026-10-27). Never secrets. Demo-environment
  logins he wrote on his Notion pages stay there (his call): don't remove them, don't copy them elsewhere.
