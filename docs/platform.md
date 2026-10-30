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
4. **Backups:** weekly, per app, to R2 and to the personal Drive `80_Backups/Apps/<App>`; D1 Time Travel (7 days on
   the free plan) covers the gap between two backups. **No app data in git**, ever (code, schemas, migrations and
   synthetic fixtures only).
5. **Hub:** stays the « Brain · Cockpit » artifact for now (it keeps Claude in the page); a Pages app later.

## Shared rules for every app
### Hosting
- Pages project **connected to the app's GitHub repo**, release = merge into `main` (`skills/build-webapp`). A project
  created by direct upload can never be connected: if one exists, create a connected project and move the domain.
- Functions under `/api/*` only (`_routes.json`). Workers for crons and syncs. Cron triggers are 5 per account in total:
  Sport's `sport-sync` uses one; ask before adding another.
- Names: Pages project = D1 database = R2 prefix = the app key: `sport`, `finance`, `camp-de-base`.

### Sign-in: Cloudflare Access
- **One** Access application covering `sport.`, `finance.` and `basecamp.aureliencaye.com` (and their `pages.dev`
  hosts), policy: Aurélien's e-mail only, session 1 month. Team: Sport's existing Zero Trust team. Created once, by the
  Sport thread, and reused by the others (one more hostname each).
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
- Steps: `wrangler d1 export <db> --remote --output <app>-YYYY-MM-DD.sql` → gzip → `wrangler r2 object put
  backups/<app>/…` → copy to Drive `80_Backups/Apps/<App>/` (folder id of `80_Backups` in `docs/personal-drive-map.md`).
- Retention: 8 weekly + 1 per month for 12 months, in R2 and on the Drive (the workflow prunes).
- Secrets (GitHub, pasted by Aurélien): a Cloudflare token limited to D1 read/export and R2 write on this account; a
  Drive credential for the personal account (rclone config). Restore-test once into a scratch D1 and record it in the
  app's ledger.
- Files in R2 (photos, FIT, statements) are not exported weekly; R2 is their home and is durable. TODO(Aurélien):
  decide whether R2 files also need a monthly copy to the Drive.

### Design system
Apps stay on their current version (v1.5.1) during these threads; the app switcher (v1.6, `apps.json`) comes with
the hub thread and each app adopts it at its next release.

## Threads (2026-10-30)
Each thread runs in its own cloud session as `builder` (`agents/builder.md`, `skills/build-webapp`,
`skills/release-webapp`), follows the app repo's `AGENTS.md`/`CLAUDE.md`, and ends with `session-close` (Projects row
state, Build Roadmap, ledger and configuration guide republished).

| # | Thread | Repo · environment | Done when |
|---|---|---|---|
| 1 | **Sport · hébergement** | `ac-ua/sport` · `app-sport` | Pages project connected to the repo; D1 `sport` loaded and synced nightly by `sport-sync`; `sport.aureliencaye.com` behind the shared Access application (created here, documented for the others); `/api/attention`; weekly backup running once; guide republished |
| 2 | **Finance · mise en ligne** | `ac-ua/finance` · TODO(Aurélien): an `app-finance` environment | `finance.aureliencaye.com` live behind Access, Pages connected; D1 `finance` from `db/schema.sql`; data moved from the artifact's store without loss (counts checked); Functions API used by the front; `/api/attention`; weekly backup; the artifact kept as read-only fallback until Aurélien retires it |
| 3 | **Camp de Base · migration** | `ac-ua/Base-Camp` · `Base Camp` | D1 `camp-de-base` with the full schema and data (row counts equal to Supabase), API on D1, photos in R2, Access instead of Google sign-in, `basecamp.aureliencaye.com`; `/api/attention` from the tower; weekly backup replaces the old backup workflow; Supabase project left **paused, not deleted** (deletion is Aurélien's call) |
| 4 | **Brain · hub** (after 1–3) | `ac-ua/brain` · `Default` | « Brain · Cockpit » points to the new addresses and shows each app's attention items next to the Notion tasks; design system v1.6 with the app switcher and `apps.json` |

### Known constraint for thread 4
An artifact cannot `fetch` other hosts (CSP), so the cockpit cannot call `/api/attention` directly. Options to settle
in thread 4: a small remote MCP server on Cloudflare (`get_attention`, behind Access with OAuth) added as a claude.ai
custom connector and declared in the artifact's `mcp` capability (preferred); or an hourly job writing attention
items into a Notion database; or the hub moves to a Pages app.

## What Aurélien does by hand
- Cloudflare dashboard: custom domains, the Access application, D1/R2 creation if a session lacks a token that can do
  it. Each thread gives him the exact clicks.
- Secrets: pasted by him into Cloudflare, GitHub or the cloud environment; never in a chat or a repo.
- A cloud environment `app-finance` (variables named in `ac-ua/finance` `docs/environment.json`).
