---
name: build-webapp
description: Build and ship a personal web app on GitHub + Cloudflare Pages (+ Functions) + Supabase without leaving the free plans. Use for any code, test, release or deploy work on a personal web project, and when choosing a stack or a hosting setup.
---

# build-webapp

Reference: [`free-tier-playbook.md`](free-tier-playbook.md), copied from `ac-ua/c_ET/docs/free-tier-playbook.md`
(limits checked 2026-10-27; re-check the official pages once a quarter). This file is the short version.

## Stack
| Layer | Default | Notes |
|---|---|---|
| Code | private repo on `ac-ua` | one repo per app; `AGENTS.md` from `templates/project-repo/` |
| Front | static files on **Cloudflare Pages** | plain HTML/JS/CSS or a static build (Astro); cache-busting stamps on assets |
| API | **Pages Functions** under `/api/*` only (`_routes.json`) | everything else static |
| Data | **Supabase** (Postgres, auth, realtime) | RLS on every table; anon key is publishable, service-role key never leaves the server |
| Mail | Resend (100/day) | only when needed |

## Release rules (the ones that bite)
1. Work on a branch. **Every branch commit starts with `[CF-Pages-Skip]`**: no Cloudflare build.
2. Ship by merging to `main` with a commit **without** the marker: one production build per release.
3. Batch: a few releases a day at most, never one per small fix.
4. Docs, scripts, workflows or data only: merge (squash) with a `[CF-Pages-Skip] …` title.
5. Test **in the session** before shipping (syntax checks, Playwright harness, the project's checks). Don't rely on
   hosted CI. Run only what the change touches: once the end-to-end suite takes more than a few minutes, give the
   project a coverage map (which lines each suite runs) and pick the suites from the diff — Element Logbook's
   `tests/impact.mjs` is the pattern (README › Tests). CI runs the same plan.
6. GitHub Actions: trigger on `pull_request` / `workflow_dispatch` only; `timeout-minutes`, `concurrency`,
   artifacts ≤ 30 days (3 days for test artifacts, uploaded only on failure).
7. Supabase migrations are applied **before** merging the code that uses them. Keep a nightly external backup
   (pg_dump, private repo only) and restore-test it once. Daily activity keeps the project from pausing.
8. Cloudflare: preview branches off (or a short allow-list). Cache and **cap** every billed third-party call.

## Environment and data
- **Session variables are prefixed by project** (`BASECAMP_SUPABASE_URL`, not `SUPABASE_URL`) and scripts refuse any
  other project's URL. Each repo lists what a session needs in `docs/environment.json`; check it with
  `cloud-env-preflight` at the start of a session in a new or changed environment.
- Keys: the publishable (anon) key may go in host config and docs; the secret (service-role) key only in Cloudflare
  secrets or, when scripts truly need it, the session environment. Never ask Aurélien to paste a key or an OAuth
  callback URL in the chat.
- **One migration path per project**, written in its `docs/RELEASE.md`: e.g. `scripts/apply_supabase.py` through an
  `app_exec` function created once by `bootstrap.sql` (works without GitHub Actions or psql), or SQL Aurélien runs.
  Applied before merging the code that uses them.
- **Writes to production data** (database, library, users) need Aurélien's explicit OK in the request, through the
  app's own API when it has one; the auto-mode classifier blocks them otherwise.
- Seeds and imports are idempotent (re-runnable: skip what exists) and have a dry run by default (`--apply` to write).

## Cloudflare Pages pitfalls
- **The build output directory is relative to the root directory**: with root `web`, write `dist`, not `web/dist`.
- Build fails on `npm ci` with a lockfile made by a newer npm: regenerate it with the npm version Pages runs (10).
- Custom domain: the DNS lives where the domain's nameservers point (registrar or another host); keep the MX
  records when moving DNS; Supabase Auth needs the domain in Site URL and Redirect URLs, or sign-in loops back.
- `*.pages.dev` may be blocked from a cloud session: test the custom domain.

## Before every release
- [ ] The project's own checks pass in the session (its `AGENTS.md` lists them).
- [ ] Migrations applied, if any.
- [ ] Build Roadmap row updated (`build-roadmap`), ledger + guide updated (`config-guide`).
- [ ] Changelog line (in the repo, and in Notion if the project keeps one there).

The full ritual (feedback triage, paperwork, checks, go, live check, artifacts republished in place, recap) is the
skill `release-webapp`; each project writes its commands once in `docs/RELEASE.md`.

## Secrets
Aurélien pastes secrets himself into Cloudflare, GitHub or Supabase. Never in the chat, the repo, Notion or a memory.

## Signs of quota trouble
A GitHub job that fails in ~4 s with no runner and no log is a quota or billing block, not your code. Run tests
locally and wait for the 1st (UTC). See playbook §4. Anything that must not wait for Actions (migrations, backups
on demand) has a script that runs from the session.
