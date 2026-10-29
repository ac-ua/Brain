---
name: project-kickoff
description: Start a new personal project the same way every time — repo from the template, a Projects row, first Build Roadmap items, and the configuration guide skeleton. Use when Aurélien starts a new app, site or build ("new project", "on lance …", moving an artifact into a repo).
---

# project-kickoff

Everything a later session needs to pick the project up, created in one pass. Ask once for anything missing below;
mark the rest `TODO(Aurélien)`.

## Inputs
Name · one-line purpose · domain · repo name (`ac-ua/<repo>`) · public or private · stack (default: `build-webapp`) ·
existing artifact URL, if any.

## Steps
1. **Repo.** Aurélien creates the empty repo `ac-ua/<repo>` (creating repos is his call) and attaches it to the
   session. Then copy `templates/project-repo/` into it, fill the placeholders in `AGENTS.md`, and commit on a branch
   (`[CF-Pages-Skip]` marker if it will deploy to Cloudflare Pages). Open a PR.
   A web app starts from the design system (`web-design-system`): `tokens.css` copied as `web/ds.css`, `icons.js`
   built from the kit, the shared shell (side menu, theme switch), the mark from `brand/` unless it has its own.
2. **Ledger + guide.** In the repo: `python3 <brain>/skills/config-guide/scripts/ledger.py --ledger docs/build-ledger.json init …`
   (see `config-guide`), then fill chapter 1 of `docs/config-guide/guide.html` from the inputs, with the planned
   architecture. **Publish it now** as an artifact titled « <Project> · Configuration guide », write its link in the
   ledger (`ledger.py guide --url …`), in `docs/artifacts.md` (the registry) and in the Projects row (Artifacts).
   Every later release republishes it in place (same link).
3. **Projects row** (`collection://127dc180-4e2f-4650-b120-0b4ff4cc9eab`): Name, Domain, Status `Active`, Repo,
   Artifacts, Prod URL (when known), Drive folder (`TODO(Aurélien)` if unknown).
4. **Roadmap view.** On the project's page, add a linked Build Roadmap view filtered on Project = this project,
   grouped by Status.
5. **First roadmap items** (`build-roadmap`): `v0.1 — first deploy` (To do) plus the 2–5 items from the brief.
6. **Hosting** (if web): Cloudflare Pages project with preview branches off, Supabase project if needed. Aurélien
   creates accounts and pastes secrets; you write the steps in the guide's Deploy chapter.
7. **Cloud environment.** One environment per app (`app-<name>`). Write `docs/environment.json` (variables prefixed
   by project, allowed hosts, tools; `cloud-env-preflight`), the setup script or SessionStart hook for tools and
   plugins, and give Aurélien the whole settings list in one message. Write `docs/RELEASE.md` from
   `skills/release-webapp/references/release-template.md`.
8. **Started outside the repo** (a local session, an artifact, a mock-up): bring everything in through
   `session-handoff`; nothing stays in a local folder or a session.
9. **Close**: Session Log row, and a Brain Inbox row if the template missed something.

## Done when
Repo with `AGENTS.md`, ledger, guide published (link in `docs/artifacts.md` and the Projects row),
`docs/environment.json`, `docs/RELEASE.md` · Projects row ·
roadmap view and first items in the shared Build Roadmap · PR open.
