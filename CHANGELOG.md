# Changelog

The brain is versioned like any project: `v0.x` while the skeleton settles. Each release is a merged PR on
`ac-ua/brain` and a row in the Notion Build Roadmap (Project = Brain).

## v0.4.0 — skills from the session audit (2026-10-28)
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
