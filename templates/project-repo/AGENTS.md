# AGENTS.md — PROJECT

PURPOSE (one line). Owner: Aurélien. Domain: DOMAIN. Part of the brain (`ac-ua/brain`): its `AGENTS.md` hard rules
apply here too (autonomy, confidentiality, secrets, voice).

**Before any build, deploy or cloud setup:** read `ac-ua/brain` → `agents/builder.md` and `skills/build-webapp`
(`skills/release-webapp` for a release). They win over any doc in this repo on stack and deploy (Pages connected to
this repo, release = merge into `main`, never `wrangler pages deploy`); a doc here that disagrees gets fixed.

## Context
- Notion: Projects row `PROJECT_PAGE_ID`; roadmap = Build Roadmap filtered on this project.
- Configuration guide: `docs/config-guide/guide.html` (published at ARTIFACT_URL), generated from `docs/build-ledger.json`.
- Cloud environment: `ENVIRONMENT` (holds this app's secrets).

## Stack
STACK (default: static front on Cloudflare Pages, Functions under `/api/*`, Supabase). Free-tier rules:
`ac-ua/brain` → `skills/build-webapp`.
Look and feel: `ac-ua/brain` → `skills/web-design-system` (shared by all of Aurélien's apps). The app starts from its
`tokens.css` (copied as `web/ds.css`, never edited here) and its icon kit (`web/icons.js`, domain icons in
`data/icons.app.json`). Design feedback that applies to every app goes back to the brain (its `FEEDBACK.md`).

## Rules
- Work on the session branch. **Every branch commit starts with `[CF-Pages-Skip]`.** Release = PR merged into `main`.
- Docs, scripts, workflows or data only: squash-merge with a `[CF-Pages-Skip] …` title.
- Test in the session before shipping: CHECKS.
- Migrations applied before merging the code that uses them.
- After each release: Build Roadmap row, ledger (`ledger.py change …`), guide refresh. The release commands live in
  `docs/RELEASE.md` (skill `release-webapp`); what a session needs in `docs/environment.json` (`cloud-env-preflight`).
- Secrets: never in the repo or the chat. Aurélien pastes them into Cloudflare / GitHub / Supabase.
- Anything uncertain: `TODO(Aurélien)`.

## Layout
| Path | What |
|---|---|
| `docs/build-ledger.json` | record of features, screens, data, deploy, decisions, open items, changes |
| `docs/config-guide/` | the guide and its screenshots |
