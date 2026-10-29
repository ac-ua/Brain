# Changelog

The brain is versioned like any project: `v0.x` while the skeleton settles. Each release is a merged PR on
`ac-ua/brain` and a row in the Notion Build Roadmap (Project = Brain).

## v0.4.17 — every app has its builder files (2026-10-29)
- The personal website (`ac-ua/website#4`) and Camp de Base (`ac-ua/Base-Camp#211`) get the files `builder.md` asks
  for: ledger, configuration guide published as an artifact, `environment.json`, `RELEASE.md`, registry line.
  Camp de Base's `deploy.md` no longer says « push sur `main` ».
- `agents/builder.md`: Finance is in the project list.

## v0.4.16 — audit: outreach facts, maps, design system v1.3.1 (2026-10-29)
- Outreach skills (sponsor, research, follow-up) and their context files: South Pole **November 2027 from Berkner
  Island** (~1,350 km, ~60 days, sled over 110 kg, ALE), as on the Expeditions card; they still said November 2026
  from Hercules Inlet. Track record as stated on the card (Greenland 2023 was a team crossing, not solo; Finse 2026
  added). The « ~50 people in history » rarity line is now `TODO(Aurélien)` (it was the Hercules figure). Follow-ups
  handle contacts told the old date. `expedition-research-outreach` had two frontmatter blocks; one is left.
- `web-design-system` v1.3.1 (no visual change): `shell.js` closes the drawer from side links rendered later;
  `build_icons.py` takes `--glyphs` more than once.
- `docs/notion-map.md`: the five Projects rows it lacked (Sport data pipeline, Finance, Connector gateway, AI-native
  opportunity pages, Run club). `docs/sessions.md` and `brain-maintenance`: `app-sport` (id) and Finance.
  `domains/admin-finance.md`: Finance is built (`ac-ua/finance`). `AGENTS.md`: `interview-prep` listed under
  chief-of-staff, as in its agent file. `BLUEPRINT.md`: Finance is no longer a later idea.

## v0.4.15 — one design system for every app (2026-10-29)
- New builder skill `web-design-system`, extracted from Camp de Base: tokens (light, dark, context palettes), shell
  and `ds-` components in `tokens.css`, data-viz rules, the faceted icon kit (73 icons, 16 glyphs, a generic
  `build_icons.py`), the brand mark, and `FEEDBACK.md`.
- Feedback loop: design feedback in any app session updates the shared system (PR + `FEEDBACK.md` line) or, if
  app-specific, the app; from the work Mac, a Brain Inbox row. Rule in `AGENTS.md` and `agents/builder.md`.
- Wired into `build-webapp` (Stack), `project-kickoff` and the project template (new apps start from `tokens.css`
  and the icon kit) and `release-webapp` (UI check before shipping).

## v0.4.15 — cockpit A·B·C and the platform study (2026-10-29)
- « Brain · Cockpit » rebuilt on the design system (shell, tokens, icons, a faceted compass mark
  `docs/cockpit/brand/brain-mark.svg`): Aujourd'hui (what waits on Aurélien with decisions, top 3 with pins, inbox
  triage by keyboard or proposed by Claude), Domaines (one tile per domain), Projets, Sessions, and a Claude panel
  that answers on the live data and proposes task changes he confirms. Built from `docs/cockpit/src/` by
  `docs/cockpit/build.py`.
- « Brain · Plateforme des apps » (https://claude.ai/artifact/R41dRr422fs6kwqKr1Fdcs): how to unify Finance, Camp de
  Base and Sport as a federation (subdomains, one Cloudflare Access sign-in, an app switcher, a `/api/attention`
  contract, a hub), with two prototypes and open questions.
- `docs/artifacts.md`: the Brain's artifact registry.

## v0.4.14 — sessions are back in the cockpit (2026-10-29)
- « Brain · Cockpit »: the Claude sessions block is back (Aurélien wants it). When the Claude Code Remote connector
  does not answer in the page, the block shows the last 7 days of the Session Log instead (new view « Cockpit · recent »).

## v0.4.13 — the cockpit reads Notion only (2026-10-29)
- « Brain · Cockpit »: the Claude sessions block is removed (the Claude Code Remote connector does not load in
  artifacts); the page reads Notion only.

## v0.4.12 — the project cockpit (2026-10-29)
- « Brain · Cockpit » artifact (https://claude.ai/artifact/UqbtEKheEFwqs7P61d6zdi, `docs/cockpit/projects-cockpit.html`):
  reads Notion and the Claude Code session list live through the claude.ai connectors; shows what waits on Aurélien,
  one card per project (state, next step, his tasks, roadmap in progress, matching sessions) and lets him tick tasks
  Done. Nothing stored in the page.
- Notion: Projects gets `Where we are`, `Next step`, `State updated`; three « Cockpit · » views (`docs/notion-map.md`).
- `session-close` and `AGENTS.md`: every session writes its project's state and files Aurélien's to-dos as Tasks
  linked to the project.
- « Brain · Étude du cockpit » (https://claude.ai/artifact/4xqmHuenUqj4EUZ292uoWF, `docs/cockpit/cockpit-proposals.html`):
  research and design directions for the full cockpit.

## v0.4.12 — work and backups out of Admin (2026-10-29)
- `docs/personal-drive-map.md`: `70_Work & Career` (CV & Job Search, one folder per employer, pro deliverables);
  `80_Backups` (Phone Backup, Claude Backup; an app's backups stay with the app); Famileo US, Old Projects and Travel
  moved from 10_Admin to 40_Projects.

## v0.4.11 — the personal Drive has a map (2026-10-29)
- `docs/personal-drive-map.md`: personal Drive sorted and mapped (00_Inbox, 10_Admin, 20_Finance, 30_Expeditions,
  40_Projects, 50_Content, 60_Library, 70_Work, 99_Archive, One Life), rules, Notion links and folder ids. Finance is
  split by bank, tax year and flat so the finance app can read it by folder id.
- `AGENTS.md`: personal files are filed in the personal Drive and linked in Notion, like pro files in the work Drive.
- `domains/expeditions.md`, `domains/admin-finance.md`, `domains/content.md`: where their files live.

## v0.4.10 — every build runs as builder (2026-10-29)
- `AGENTS.md`: any build in any domain (Sport, Finance, data pipelines, BI apps) runs as `builder` from the first
  commit: kickoff, Projects row, Build Roadmap, ledger, configuration guide published as « <Project> · Configuration
  guide », registry; a build already under way gets the missing pieces before its next release. `app-sport` listed.
- `agents/builder.md`: Sport data in scope, any domain; « A project is set up when » checklist.
- `project-kickoff`: the guide is published at kickoff and linked in the ledger, the registry and the Projects row.
- `session-start`: a build session reads `agents/builder.md` first. `domains/sport.md`: Sport data project.

## v0.4.9 — shared files go where Aurélien uses them (2026-10-29)
- `docs/drive-map.md`: a shared file's shortcut target is where Aurélien will use it (a colleague's Medtronic deck
  reused for competitive benchmarking → `02_Assets/Competitive`), not the client it was made for.

## v0.4.8 — Demo Catalog (2026-10-29)
- Notion: Demo Nuggets page restructured (sections, table of contents; synced callouts and logins untouched) and a
  **Demo Catalog** database under it, seeded with 15 demos (use case, type, environment, health, audience, shown to,
  lessons). Belcorp and MHW Bev Co pages moved there as references.
- `demo-prep`: recommends from the catalog before proposing a build, and updates it at write-back.

## v0.4.7 — shortcuts for shared files (2026-10-29)
- `tools/drive-shortcuts/`: Apps Script bound to the Sheet « Drive shortcut queue » (work Drive, `05_Internal`).
  Agents append the shared link and the account; every 5 minutes the script adds the shortcut in
  `01_Accounts/<Account>` (never a copy). `docs/drive-map.md` updated; install once by Aurélien (README).
- Every opportunity page with a Drive folder now links it in Assets (or at the top when there is no brief yet).

## v0.4.6 — upload list, shared links, earlier versions (2026-10-29)
- `docs/drive-map.md`, `session-close`: the Mac's Drive app syncs the personal Drive only, so a pro file the connector
  can't upload goes on an upload list (`TO-UPLOAD.md` + recap with the target folder link) for Aurélien to drag in.
- Files shared with Aurélien: never copied; link in Notion, `Shift+Z` reminder until a tool can create shortcuts.
- Older versions are kept in `Earlier versions` sub-folders (renamed with date and v1/v2); `99_Archive/Superseded`
  and the empty `05_Internal/Backup` removed (Aurélien's go), with the personal Ironman guide.

## v0.4.5 — the work Drive has a map (2026-10-29)
- Work Drive reorganised (no file deleted): 00_Inbox · 01_Accounts/<Account> · 02_Assets · 03_Demos · 04_Events ·
  05_Internal · 99_Archive; ~85 loose files filed, 22 account folders named like the Notion Accounts.
- New `docs/drive-map.md`: tree, filing rules, folder ids. Linked from `AGENTS.md`, `domains/work.md`, and the skills
  that save pro files (`work-notes`, `session-close`, `demo-prep`, `case-for-change`, `cep-workbook-filler`,
  `explainer-video`).
- Rule: every pro file an agent creates is saved straight to its place in the work Drive (sub-folders created as
  needed) and its link written on the Notion page, without asking (`AGENTS.md` « Where things go », drive-map).
- `.claude/settings.json`: Drive read, create, move and copy run without a prompt; trash and sharing still ask.

## v0.4.4 — confidentiality is one way: perso → pro only (2026-10-29)
- `AGENTS.md`, `domains/work.md`, `docs/BLUEPRINT.md`, `session-close`, `explainer-video`: the rule « never move pro
  files to personal storage » is removed. Only personal → pro is forbidden; pro files and deliverables may go to the
  personal Drive, Notion and this repo (Aurélien: « c'est un problème de move du perso vers le pro »).
- The work Mac brings deliverables back to the personal Drive through the Google Drive app's personal folder in Finder.

## v0.4.3 — the guide follows without asking (2026-10-28)
- `AGENTS.md` (Artifacts), `agents/builder.md`, `release-webapp`: after each delivery that changes the architecture,
  the model or the screens, the builder updates the project's living guide through a background sub-agent, without
  asking Aurélien, then bumps the registry line (Aurélien, Camp de Base session: « tu ne dois pas me demander pour
  update le guide »).

## v0.4.2 — artifacts stay with their project (2026-10-28)
- `AGENTS.md`, new hard rule « Artifacts »: one project per artifact (title starts with the project's name), a
  registry per project (`docs/artifacts.md` or the Projects row), update the existing artifact (same link), never
  recreate; the project's guide follows each delivery that changes the architecture or screens.
- `session-start` reads the registry; `session-close` checks it and the guide (Camp de Base: the Expeditions Guide
  had stayed at v5 for two days because no session knew where it was).

## v0.4.1 — gpx-route: rotated screenshots (2026-10-28)
- `gpx-route`: reconstructing from a map screenshot fits scale and rotation on two known points, checks on a topo
  map, confirms the valley with Aurélien's sketch, and refreshes an imported track in place (Brain Inbox, Kyrgyzstan
  2021: a rotated Google Maps screenshot put the first version in the wrong valley).

## v0.4.0 — skills from the session audit (2026-10-27)
From an audit of 55 Claude Code sessions (17 Aug – 27 Oct 2026): repeated tasks became skills, frictions became
fixes.
- New skills: `session-handoff` (resume note outside the session, environment inventory, smoke test, prompt to
  paste), `release-webapp` (feedback triage → paperwork → checks → go → live check → artifacts in place → card;
  per-project `docs/RELEASE.md`), `cloud-env-preflight` (`scripts/preflight.py`: variables, key types, project match,
  allowed hosts, tools in one pass; per-project `docs/environment.json`), `demo-prep`, `case-for-change` (with deck
  lessons), `message-drafting` (with tone rules), `interview-prep`, `video-edit` (with tooling per machine),
  `gpx-route` (`scripts/route.py`: trail routing or great-circle legs, terrain altitude, stages, Garmin symbols).
- `explainer-video`: document mode (scrolling doc), `data-pointer` (ring + cursor on the box being discussed),
  target length and depth in the brief, script checked against Aurélien's questions, web facts cross-checked, real
  images downloaded, `compress` step (under 29 MB), never the cloned voice for work.
- Fixes: `build-webapp` (project-prefixed variables, keys, one migration path, production writes need his OK,
  Pages pitfalls), `build-roadmap` (use the fetched select options, shared database only), `config-guide`
  ("what you still have to do" checklist, one guide URL), `project-kickoff` (environment, `RELEASE.md`),
  `session-start` (handoff, preflight, work Mac), `session-close` (handoff, local memories), `work-notes`
  (recordings, account questions, handoff toggle), `poc-use-case-filler` (scope), `unifyapps-format` (fallback to
  the team plugin's `unifyapps-brand-deck`).
- Rule: Aurélien's skills, pro included, live in `ac-ua/brain`; the shared team repo only receives platform
  learnings through its loop (`AGENTS.md`, `domains/work.md`).

## v0.3.1 — demo logins stay on the CRM pages (2026-10-27)
- Exception to the secrets rule: demo-environment logins Aurélien wrote on his Notion pages stay there; never
  removed, never copied elsewhere (`AGENTS.md`, `domains/work.md`, `work-notes`, `session-close`).

## v0.3.0 — work-notes: AI-native CRM pages (2026-10-27)
- Skill `work-notes`: transcripts, notes and work-session results → the right Opportunity or Projects page under
  Work › Unify Apps, AI-maintained brief on top, one structured toggle per meeting (raw transcript nested), linked
  Account and People, tasks, learnings. Templates in `references/template.md` (Notion copy: 📋 Opportunity template).

## v0.2.3 — Notion is the system of record for work (2026-10-27)
- `AGENTS.md`, `session-close`, `domains/work.md`, blueprint: every work session writes its deal brief (CRM
  opportunity page) and learnings (Memories) to Notion; the old "generic lessons only, no client names" rule is gone.
- `brain-inbox`: client names allowed in pro lessons; no secrets.

## v0.2.2 — weekly sweep: clean panel, roll over only what's needed (2026-10-27)
- `brain-maintenance` runs Friday night (Saturday ~00:52 New York) and no longer opens sessions for planned work: it
  only replaces an archived session worth restarting (weekly sessions, long sessions still in use).

## v0.2.1 — weekly brain maintenance (2026-10-27)
- Skill `brain-maintenance`, run every Friday ~01:00 America/New_York by a cloud scheduled task: applies accepted
  Brain Inbox rows as one merged PR, archives finished or blocked sessions (blocked ones become Tasks), opens one
  empty session per planned piece of work (max 5), and sends a French recap.
- `docs/routines.md` (active), `docs/sessions.md` (left panel, `Keep ·` titles), `chief-of-staff` and `AGENTS.md`
  updated.

## v0.2.0 — full migration (in progress)
- Account skills moved into the repo: the 3 expedition outreach skills, `spanish-teacher`, and the pro skills
  (`unifyapps-format`, `cep-workbook-filler`, `poc-use-case-filler`, `unifyapps-rfp-rfi-response-template`).
- Confidentiality rule updated: the brain covers pro and perso; nothing personal goes to pro systems.
- Skills index per domain in `AGENTS.md`; one-source rule for skills in `README.md`.
- All 8 domains have a Notion domain page (context card + Projects/Tasks views) and a real `domains/*.md`;
  routing table and `docs/notion-map.md` point to them. 🗄️ Archive page created.
- App repos (Base-Camp, c_ET, website) point to the brain and the shared Build Roadmap (separate PRs).
- Skill `explainer-video`: two-voice podcast with progressive-reveal slides (stock voices, pronunciation dictionary,
  per-clip check; MP4 with subtitles, MP3, SRT, script), generalised from the kit in `tools/explainer-video/`, which
  stays as the reference episode. Usable from Content and from Work (work Mac, outputs in the work Drive).
- `docs/sessions.md` (and Notion › System › Sessions playbook): one session per deliverable, what runs where,
  naming, left-panel hygiene; claude.ai Projects frozen.
- `docs/routines.md`: every routine (cloud, GitHub Actions, Supabase pg_cron, work Mac), active and planned, and how
  to add one.

## v0.1.1 — merging is free on app repos (2026-10-27)
- A tested session PR is merged into `main` without asking, on personal app repos and on `ac-ua/brain`
  (`AGENTS.md`, `builder`, `session-close`).
- `domains/expeditions.md`: Camp de Base releases go to the Build Roadmap; the old changelog database is archived.

## v0.1.0 — skeleton (2026-10-27)
- `AGENTS.md` constitution: hard rules (autonomy, confidentiality, secrets, voice), routing table, session protocol,
  startup budget. `CLAUDE.md` points to it.
- 3 agents: `chief-of-staff`, `builder`, `content-studio`.
- 7 skills: `session-start`, `session-close`, `brain-inbox`, `project-kickoff`, `build-webapp` (with the free-tier
  playbook), `build-roadmap`, `config-guide` (ledger + HTML guide).
- 8 domain files; Expeditions and Content have a first real version, the others are stubs.
- Templates: project repo (AGENTS.md, build ledger, config guide skeleton) and the 5 Notion database schemas.
- Docs: blueprint (text + HTML source), Notion map, phase 0 handoff. Explainer-video kit in `tools/`.
- Claude and Codex adapters (symlinks).
- Expeditions and Content migrated: Notion context cards with Projects/Tasks views, routing table updated.
- Archived docs (handoff, blueprint source) kept verbatim.
