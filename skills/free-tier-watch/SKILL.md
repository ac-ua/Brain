---
name: free-tier-watch
description: Weekly check that none of Aurélien's apps is about to leave a free plan — GitHub Actions minutes and artifact storage, Cloudflare Pages builds, Workers and Pages Functions requests, D1, R2, Supabase database and file storage, repository sizes — with a French recap sent by email and push at the end of the week. Use for the Friday scheduled run, or when Aurélien asks "où j'en suis des quotas", "est-ce que je dépasse l'offre gratuite", "free tier check".
---

# free-tier-watch

One report, every Friday evening: for each service, what is used, the free limit, the share, and the month-end pace.
Anything that cannot be measured is listed as « not measured », never guessed. Limits and the rules that keep usage
low live in `skills/build-webapp/free-tier-playbook.md`; what is measured lives in `services.json` (add a repo or a
resource there when a project starts).

## Run
```bash
cd <brain>/skills/free-tier-watch
python3 scripts/quota_report.py --json /tmp/quota.json > /tmp/quota.md; echo "exit $?"   # 2 = at least one alert
```
- **GitHub** (`gh api`, repo-scoped): repository size; Actions runs this month and billed minutes (private repos;
  public ones are free); artifact storage; **blocked Actions** (jobs refused: minutes used up or billing failed, runs
  end in seconds with no runner; the GitHub message is quoted); Cloudflare Pages production builds, estimated from
  merges into `main` without `[CF-Pages-Skip]`. A repo the session cannot reach is a gap: ask for it with `add_repo`
  (read) once, then rerun; if refused, keep it in « Not measured ».
- **Supabase** (no secret): each app's nightly backup writes a `usage-<run>` artifact with `usage.json` (database
  bytes, file storage bytes and count, dump size), kept 7 days. Without it, the last backup artifact's size is
  shown as a lower bound. Egress and monthly active users are dashboard-only (Organization › Usage).
- **Cloudflare** (`WATCH_CLOUDFLARE_API_TOKEN`, read-only, in `perso-general`): D1 size per database, busiest day of
  Workers + Pages Functions requests over 7 days, R2 storage, Pages deployments this month (exact, previews included).

Accounts: GitHub minutes and artifact storage are one pool for the whole `ac-ua` account; the account-level billing
page is not reachable from a session, so the per-repo sum is the measure and GitHub's own budget alerts (playbook §3)
are the backstop.

## Recap (French, short)
Order: what needs action now, then what to watch, then « tout va bien » in one line, then « non mesuré ».
- **🔴 alert** (≥ 80 %, a pace over the limit, or blocked Actions): what is at risk in plain words (e.g. « les
  sauvegardes de nuit ne tournent plus »), the date it resets if known (GitHub minutes: the 1st, 00:00 UTC), and
  the one action that fixes it, with the exact screen (GitHub › Settings › Billing and plans, Cloudflare › Pages ›
  Settings › Builds › Preview branches…).
- **🟠 watch** (≥ 50 %): the figure and the pace.
- Never change a setting, a plan or a payment method; never trigger a workflow to "test" (it costs minutes).
The run's final message is the recap: the scheduled task sends it by email and push.

## Setup (once, Aurélien)
1. Cloudflare › My Profile › API Tokens › Create token › Custom token, **read only**: Account › Account Analytics:
   Read, D1: Read, Workers Scripts: Read, Workers R2 Storage: Read, Workers KV Storage: Read, Cloudflare Pages: Read;
   account: his account only. Paste it as `WATCH_CLOUDFLARE_API_TOKEN` in the `perso-general` environment (and the
   account id as `WATCH_CLOUDFLARE_ACCOUNT_ID`, optional).
2. Each app with Supabase writes `usage.json` from its backup workflow (Camp de Base: done; Element Logbook: same
   step to add in `ac-ua/c_ET` `.github/workflows/backup.yml`).
3. GitHub › Settings › Billing and plans › Budgets and alerts: email at 75 / 90 / 100 % of included Actions minutes.

## Scheduled task
« Weekly free-tier check », Friday 17:47 America/New_York, fresh session in `perso-general`, push + email
(`docs/routines.md`).
