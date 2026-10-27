<!-- Copied from ac-ua/c_ET docs/free-tier-playbook.md (commit dbf2801, 2026-10-27). Update both, or update here and note it in c_ET. -->

# Free-tier playbook — GitHub, Cloudflare, Supabase (and friends)

Drop this file into a project (or paste it into CLAUDE.md / the session's instructions) so every build session works
the same way: ship often, stay on the free plans, never get blocked. Limits checked on 27 Oct 2026 — re-check the
official pages once a quarter.

## 1. The limits that actually bite

| Service | Free limit | What eats it |
|---|---|---|
| GitHub Actions (private repo) | **2,000 minutes / month** (reset 1st, 00:00 UTC). Each job is billed rounded **up** to the minute. No payment method → every job is refused at start (fails in ~4 s, no runner, no log). 500 MB artifact storage (GB-hours, monthly average) | CI on every push, many parallel jobs (each pays its own setup + rounding), long artifact retention |
| GitHub Actions (public repo) | unlimited on standard runners | — (but secrets/data must be fine in public) |
| Cloudflare Pages | **500 builds / month**, 1 concurrent build, 20 min max | **every push to any branch builds** (preview + production) |
| Cloudflare Workers / Pages Functions | 100,000 requests / day, 10 ms CPU / request, 50 subrequests | functions on routes that could be static; check `_routes.json` includes only `/api/*` |
| Supabase | 500 MB DB, 2 GB disk (read-only at 95 %), 5 GB uncached + 5 GB cached egress, 50k MAU, 200 realtime connections, 2 M realtime messages; **paused after 7 days without activity**; **no backups on Free** | full reloads on every app open / reconnect, realtime fan-out, no external backup |
| Resend | 100 emails / day, 3,000 / month | loops, per-user notifications |
| Google APIs | free; Calendar 600 req/min/user, Sheets 60 reads/min/user. OAuth sensitive scope unverified → **100 users for the project's lifetime**; consent screen in *Testing* → tokens expire after 7 days | polling, unverified consent screen |
| Strava | 200 req / 15 min, 2,000 / day; 1 athlete until app review | polling instead of webhooks |
| Mindbody | free call allowance, then billed per call (confirm in the developer portal) | uncached schedule reads |

## 2. Rules for every session

### Git and deploys
1. **Work on a branch; deploy by fast-forwarding `main`.** Nothing else pushes to `main`.
2. **Every commit on the work branch starts with `[CF-Pages-Skip]`** (Cloudflare skips builds whose head commit says so;
   also `[CI Skip]`, `[Skip CI]`). Only the release commit that goes to `main` has no marker → at most 2 builds per release
   (1 if previews are off, see §3).
3. A change that doesn't touch the deployed site (docs, notes, tests, CI files) goes to `main` **with** the marker: no build.
4. **Batch releases**: a few per day at most; never one deploy per small fix.
5. Before deploying, run the full test suite **locally / in the session** (free). Don't rely on hosted CI for every push.

### GitHub Actions
6. CI workflows trigger on `pull_request` and `workflow_dispatch` only — not on every push to `main`.
   Add `concurrency: { group: ${{ github.workflow }}-${{ github.ref }}, cancel-in-progress: true }` and `paths-ignore: ['docs/**', '**.md']`.
7. Prefer **one job** (or 2 shards) over many parallel jobs: each job repeats setup and is rounded up to a whole minute.
8. Set `timeout-minutes` on every job. Cache `~/.npm` (`setup-node` with `cache: npm`) and `~/.cache/ms-playwright`.
9. Upload test artifacts **only on failure** (`if: failure()`), `retention-days: 3`. Keep backups small (gzip) and ≤ 30 days.
10. Budget: CI ≈ 0 by default; scheduled jobs ≤ ~5 % of the 2,000 minutes (a 1-minute nightly job ≈ 30 min/month).

### Supabase
11. **Keep an external nightly backup** (pg_dump in a 1-minute scheduled GitHub Action, artifact 30 days, private repo only).
    Restore-test it once.
12. Load incrementally where possible (since `updated_at`), not the whole catalog on every app open; on realtime events
    reload one row, not a table.
13. Daily real activity (or a small daily write from pg_cron / a scheduled job) keeps the project from pausing.
14. Never ship the service-role key to the client or the repo; secrets live in Cloudflare / Supabase Vault.

### Cloudflare
15. Functions only under `/api/*` (`_routes.json`); everything else static and cached.
16. Cache third-party responses (KV/DB with a TTL) and **count every billed third-party call** with a hard monthly cap on the
    server (serve the cache when the cap is reached).

### Third parties
17. Webhooks over polling (Strava, Mindbody). Batch Sheets reads. Handle 429s with backoff, never retry in a loop.
18. Google OAuth: consent screen **In production**, narrowest scopes; plan verification before 100 users of a sensitive scope.

## 3. One-off owner settings per project

- **Cloudflare** › Pages project › Settings › Builds › Branch control › Preview branches: **None** (or Custom: only branches
  you want previews for). Optional Build watch paths: exclude `docs/*`, `tests/*`, `*.md`.
- **GitHub** › Settings › Billing & Licensing › Budgets and alerts: email alerts at 75 / 90 / 100 % of included Actions usage.
- **Supabase** › Organization › Usage: glance monthly (DB size, egress). Spend cap stays on.
- **Google Cloud** › OAuth consent screen: In production.

## 4. When something fails in seconds with no log

GitHub jobs that fail in ~4 s with no runner and no log = quota or billing block, not your code. Check Billing & Licensing ›
Usage; minutes return on the 1st (UTC). Meanwhile stop scheduled/CI runs from piling up and run the suite locally.
