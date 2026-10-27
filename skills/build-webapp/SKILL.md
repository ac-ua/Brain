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
   hosted CI.
6. GitHub Actions: trigger on `pull_request` / `workflow_dispatch` only; `timeout-minutes`, `concurrency`,
   artifacts ≤ 30 days (3 days for test artifacts, uploaded only on failure).
7. Supabase migrations are applied **before** merging the code that uses them. Keep a nightly external backup
   (pg_dump, private repo only) and restore-test it once. Daily activity keeps the project from pausing.
8. Cloudflare: preview branches off (or a short allow-list). Cache and **cap** every billed third-party call.

## Before every release
- [ ] The project's own checks pass in the session (its `AGENTS.md` lists them).
- [ ] Migrations applied, if any.
- [ ] Build Roadmap row updated (`build-roadmap`), ledger + guide updated (`config-guide`).
- [ ] Changelog line (in the repo, and in Notion if the project keeps one there).

## Secrets
Aurélien pastes secrets himself into Cloudflare, GitHub or Supabase. Never in the chat, the repo, Notion or a memory.

## Signs of quota trouble
A GitHub job that fails in ~4 s with no runner and no log is a quota or billing block, not your code. Run tests
locally and wait for the 1st (UTC). See playbook §4.
