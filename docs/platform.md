# Platform — Aurélien's apps on one footing

How the personal apps (Sport, Finance, Camp de Base, and every future one) are hosted, signed into, backed up and
surfaced in the hub. Study with prototypes: « Brain · Plateforme des apps »
(https://claude.ai/artifact/R41dRr422fs6kwqKr1Fdcs). Element Logbook is the club's app and stays out of this.

## Decisions (Aurélien, 2026-10-29 and 2026-10-30)
1. **Federation, not fusion.** One repo, one database, one Pages project and one release cycle per app. What is shared:
   addresses, sign-in, the design system, the attention contract, the backup method.
2. **Everything on Cloudflare.** One **D1** database per app, files in **R2**, sign-in with **Cloudflare Access**. Camp
   de Base leaves Supabase; Finance starts on D1. **Element Logbook stays on Supabase** (separate club project).
3. **Addresses:** subdomains of `aureliencaye.com` (zone already on Cloudflare): `sport.`, `finance.`, `basecamp.`
   (Camp de Base, Aurélien's call 2026-10-30), later `hub.`. Each is the custom domain of its Pages project;
   `*.pages.dev` stays as a fallback.
4. **Backups:** weekly, per app, to the personal Drive `80_Backups/Apps/<App>` only, in clear (Aurélien's call,
   2026-10-30: the copy he can always reach, even if he loses every other access; no copy in R2, no encryption); D1 Time Travel (7 days on
   the free plan) covers the gap between two backups. **No app data in git**, ever (code, schemas, migrations and
   synthetic fixtures only).
5. **Hub:** stays the « Brain · Cockpit » artifact for now (it keeps Claude in the page); a Pages app later.

## Shared rules for every app
### Hosting
- Pages project **connected to the app's GitHub repo**, release = merge into `main` (`skills/build-webapp`). A project
  created by direct upload can never be connected: if one exists, create a connected project and move the domain.
- Functions under `/api/*` only (`_routes.json`). Workers for crons and syncs. Cron triggers are 5 per account in total:
  Sport's `sport-sync` uses two (nightly sync, track job); ask before adding another.
- Names: Pages project = D1 database = R2 prefix = the app key: `sport`, `finance`, `camp-de-base`.

### Sign-in: one Google login for every app (Cloudflare Access)
- **Google SSO, logged in once** (Aurélien's call, 2026-10-30): Cloudflare Access with **Google** as the login method
  (Zero Trust › Settings › Authentication › Login methods › Google, with an OAuth client Aurélien creates in Google
  Cloud and pastes into Cloudflare). The login happens on the team domain; its session then opens every other app
  without asking again.
- **One** Access application covering `sport.`, `finance.` and `basecamp.aureliencaye.com` (and their `pages.dev`
  hosts), policy: Aurélien's Google account only (TODO(Aurélien): which address), session 1 month. Team: Sport's
  existing Zero Trust team. Created once, by the Sport thread, and reused by the others (one more hostname each). The
  apps drop their own logins (Camp de Base's Supabase Google sign-in, Finance's planned Supabase TOTP): Access is the
  only door; Google's 2-step verification protects it.
- **Add a hostname to the shared application only once its DNS answers** (learned 2026-10-30): after the Google login,
  Access visits `/cdn-cgi/access/authorized` on every hostname of the application to set its cookie, so one hostname
  without DNS (NXDOMAIN) breaks the login for every app. Order: custom domain active on Pages → CNAME resolves → add the
  hostname (and its `pages.dev` hosts) to the application. Details: `ac-ua/sport` › `docs/access.md`.
- **The hub** (`hub.aureliencaye.com`) joins the same application the day it leaves the claude.ai artifact.
- Every Function verifies the `Cf-Access-Jwt-Assertion` JWT against the team's certs and the application's AUD (Sport's
  `functions/api/data/[name].js` is the reference implementation). Never trust the e-mail header alone.
- Sign out: `/cdn-cgi/access/logout` (design system: `.ds-signout`).
- Machine access (the hub, scripts): an Access **service token** per caller, never a shared password.

### The attention contract
Every app exposes what waits on Aurélien, computed from what it already knows, read-only:
```
GET /api/attention        (Access JWT or service token)
200 { "app": "sport", "generated_at": "2026-10-30T07:00:00Z",
      "items": [ { "id": "data_health:review:12", "title": "2 séances à fusionner ou garder séparées",
                   "severity": "warn",          // info | warn | bad
                   "kind": "review",            // alert | deadline | decision | review
                   "due": null, "url": "https://sport.aureliencaye.com/#data" } ] }
```
- `id` stable across calls; `title` in French, one line, says what to do; `url` opens the place in the app where it
  gets fixed. At most ~20 items, most urgent first. Empty list when all is well.
- Sources: Sport `data_health` (review items, stale sync), Finance `engine/insights.js` findings + pending
  reimbursements + routine deadlines, Camp de Base `GET /api/tower` alerts.
- Items are live: they are not copied to Notion. A real decision still becomes a Notion task through `session-close`.

### Weekly backup (same template in every app repo)
- `.github/workflows/backup-weekly.yml`: `schedule` once a week (Sunday, staggered: sport 03:11, finance 03:23,
  camp-de-base 03:37 UTC) + `workflow_dispatch`; `timeout-minutes: 10`; `concurrency`.
- Steps: `wrangler d1 export <db> --remote --output <app>-YYYY-MM-DD.sql` → gzip → (restore check when the app has one)
  → copy to Drive `80_Backups/Apps/<App>/` (folder id of `80_Backups` in `docs/personal-drive-map.md`) → check the file
  is on the Drive, or fail. Never a copy in R2 (same account as the data, and a store that could become paid).
- Retention: 8 weekly + 1 per month for 12 months on the Drive (the workflow prunes, only after today's file landed).
- Secrets (GitHub, pasted by Aurélien): a Cloudflare token limited to D1 read/export on this account; a
  Drive credential for the personal account (rclone config). Restore-test once into a scratch D1 and record it in the
  app's ledger.
- Files in R2 (photos, FIT, statements) are not exported weekly; R2 is their home and is durable. TODO(Aurélien):
  decide whether R2 files also need a monthly copy to the Drive.

### Design system
The app switcher and the app registry `apps.json` are design system **v1.9** (thread 4; v1.6–v1.8 went to full
screen, filter bars and more chart series in the meantime). Each app adopts v1.9 at its next release: copy
`apps.json` and `shell.js`, add `<div class="ds-apps" data-ds-apps></div>` under the brand. A new app or address is a
change to `skills/web-design-system/apps.json`, nowhere else.

## Threads (2026-10-30)
Each thread runs in its own cloud session as `builder` (`agents/builder.md`, `skills/build-webapp`,
`skills/release-webapp`), follows the app repo's `AGENTS.md`/`CLAUDE.md`, and ends with `session-close` (Projects row
state, Build Roadmap, ledger and configuration guide republished).

| # | Thread | Repo · environment | Done when |
|---|---|---|---|
| 1 | **Sport · hébergement** | `ac-ua/sport` · `app-sport` | Pages project connected to the repo; D1 `sport` loaded and synced nightly by `sport-sync`; `sport.aureliencaye.com` behind the shared Access application (created here, documented for the others); `/api/attention`; weekly backup running once; guide republished |
| 2 | **Finance · mise en ligne** | `ac-ua/finance` · TODO(Aurélien): an `app-finance` environment | `finance.aureliencaye.com` live behind Access, Pages connected; D1 `finance` from `db/schema.sql`; data moved from the artifact's store without loss (counts checked); Functions API used by the front; `/api/attention`; weekly backup; the artifact kept as read-only fallback until Aurélien retires it |
| 3 | **Camp de Base · migration** | `ac-ua/Base-Camp` · `Base Camp` | D1 `camp-de-base` with the full schema and data (row counts equal to Supabase), API on D1, photos in R2, Access instead of Google sign-in, `basecamp.aureliencaye.com`; `/api/attention` from the tower; weekly backup replaces the old backup workflow; Supabase project left **paused, not deleted** (deletion is Aurélien's call) |
| 4 | **Brain · hub** (after 1–3) | `ac-ua/brain` · `Default` | « Brain · Cockpit » points to the new addresses and shows each app's attention items next to the Notion tasks; design system v1.9 with the app switcher and `apps.json`; **architecture map** and **coherence review** (below). Done 2026-10-30 (v0.4.21) but the connector's setup by Aurélien |

### Thread 4 also delivers (Aurélien's call, 2026-10-30)
- **Architecture map** of every app as it really runs (Sport, Finance, Camp de Base, the hub; Element Logbook and the
  website shown apart): addresses, Pages projects, Workers and crons, D1 databases, R2 prefixes, Access application
  and hostnames, secrets by name, backups, `/api/attention`, links between apps, artifacts. Read from the repos, the
  ledgers and Cloudflare, not from this plan. Published as the artifact « Brain · Architecture des apps » (registry
  `docs/artifacts.md`), source in this repo, and summarised in this file.
- **Coherence review**, one short table per app: design-system version vs `FEEDBACK.md`, docs that still describe the
  old setup (Supabase, Google sign-in, `pages.dev` links, old backup workflows), leftovers to retire (Supabase project
  paused, old secrets, dead code paths), the security findings of 2026-10-30 (Finance tokens over-scoped, Sport
  `/status` public, `SYNC_TOKEN` in a URL) and their state. Fixes that are small and safe go in a PR per app;
  everything else becomes a Build Roadmap row or a Task for Aurélien. Nothing is deleted without his OK.

### Thread 4 decisions (2026-10-30)
An artifact cannot `fetch` other hosts (CSP), so the cockpit cannot call `/api/attention` itself. **Chosen: a remote
MCP server on Cloudflare, « Apps attention »** (`tools/attention-mcp`, Worker `attention-mcp`), added as a claude.ai
custom connector and declared in the cockpit's `mcp` capability. Why, against the hourly job writing into Notion:
- **Live, as the contract says** (« items are live, not copied to Notion »): the cockpit reads the apps when it opens
  or refreshes; a Notion copy would be up to an hour stale and would fill Notion with rows that are not decisions.
- **No cron and no Notion quota**: the account's crons are 2 of 5, and an hourly job would also spend Notion API calls
  and the free plan's history for nothing.
- **Reusable**: any Claude conversation with the connector can ask « what waits on me in my apps », not only the page.
- **Same security model as the apps**: the connector signs Aurélien in through Cloudflare Access (OIDC application,
  Google), only his address gets a token, and it reads the apps with one service token they already know how to limit.
- The cost: one Worker, one KV namespace and a one-time setup by Aurélien (`tools/attention-mcp/README.md`). Moving the
  hub to a Pages app later (`hub.aureliencaye.com`) needs none of this to change: it would call `/api/attention`
  with the same service token or the user's Access session.

### Architecture as it runs (2026-10-30)
Read in the repos, ledgers and the Cloudflare account; drawn in « Brain · Architecture des apps »
(`docs/cockpit/src/architecture.html`). Review of every app: `docs/platform-review.md`.

| | Camp de Base | Sport | Finance | Hub |
|---|---|---|---|---|
| Address | `basecamp.aureliencaye.com` | `sport.aureliencaye.com` | `finance.aureliencaye.com` | « Brain · Cockpit » artifact |
| Pages (Git) | `base-camp`, root `web/` | `sport`, build `scripts/build_app.py` | `finance`, output `app/` | — |
| Workers | — | `sport-sync` (2 crons, by hand) | — | `attention-mcp` (Workers Builds, to set up) |
| D1 / R2 | `camp-de-base` / `camp-de-base` (photos) | `sport` / `sport-raw` (FIT, GPX) | `finance` / — | — / KV `OAUTH_KV` |
| Access | « Apps · Aurélien », JWT checked; `OWNER_EMAILS` off | same, `ACCESS_EMAILS` | same, `ACCESS_EMAILS`; tokens read-only | OAuth through an Access OIDC app |
| Backups | Sunday 03:37 → Drive | 03:11 → Drive | 03:23 → Drive | — |
| Attention | tower alerts | `data_health` | insights, refunds, deadlines | reads the three |
| Design system | v1.7.1 | v1.8 | v1.7.1 | v1.9 |

Element Logbook (`logbook.element-training.com`, Supabase, Pages `element-logbook`) and the website
(`aureliencaye.com`, Pages `aureliencaye`) live apart; Sport reads Element's `/api/v1/sessions`.

## What Aurélien does by hand
- Cloudflare dashboard: custom domains, the Access application, D1/R2 creation if a session lacks a token that can do
  it. Each thread gives him the exact clicks.
- Secrets: pasted by him into Cloudflare, GitHub or the cloud environment; never in a chat or a repo.
- A cloud environment `app-finance` (variables named in `ac-ua/finance` `docs/environment.json`).
