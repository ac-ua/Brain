# Platform review — coherence and security (2026-10-30)

Thread 4 (`docs/platform.md` › Threads). Read in the repos (`ac-ua/sport` @ 5952598, `ac-ua/finance` @ 25aee39,
`ac-ua/Base-Camp` @ e0bdcaa), their ledgers, and the Cloudflare account (read-only token). Map of what runs:
« Brain · Architecture des apps » (`docs/artifacts.md`). Small safe fixes went out as PRs; the rest is a Build Roadmap
row or a Task for Aurélien (last section). Nothing was deleted.

## Across the apps
| Point | State | Next |
|---|---|---|
| **Backups have never run** | GitHub Actions refuses every job on the account until the monthly reset: October's free minutes are used up and the budget stays at $0 (Aurélien's call). The three `backup-weekly.yml` runs fall on Sunday 1 Nov, 03:11–03:37 UTC, just after the reset; until then only D1 Time Travel (7 days) protects the data | Claude: check the three first runs on 1 Nov (existing reminder); then the restore tests |
| Design system | v1.9 (app switcher, `apps.json`); Sport v1.8, Finance v1.7.1, Camp de Base v1.7.1. v1.8 is opt-in series only: nothing to adopt for Finance and Camp de Base | each app adopts v1.9 at its next release (`FEEDBACK.md`) |
| One AUD for three apps | a service token admitted by « Apps · Aurélien » opens every app. Finance limits it to `GET /api/attention` and `/api/health` (v0.6); Sport's API is read-only; **Camp de Base lets it read and write** | Camp de Base: same limit as Finance at its next release (Roadmap), before the hub token goes live if possible |
| Backup token | documented as account-wide **D1 Edit + R2 Edit** and shared by the three repos (`platform.md` asked for D1 read/export + R2 write): a leak from one repo can erase every D1 and the R2 originals | Aurélien: test D1 Read for `wrangler d1 export`; then one token per repo, the narrowest that works (Task) |
| rclone config | Drive scope `drive` (the whole personal Drive) in every app's GitHub secrets | Aurélien: re-authorise with `drive.file` on a dedicated backups folder (Task) |
| Backups in clear | SQL dumps in R2 and the Drive hold every row (the Strava refresh token included) | Sport ledger risk; encrypt before upload, key in the password manager (Roadmap, all apps) |
| Crons | 2 of the account's 5, both `sport-sync` (`17 9 * * *` nightly, `*/10 * * * *` tracks); `platform.md` said one | fixed in `platform.md` |
| Access hostnames | the read-only token cannot list Access applications; `base-camp.pages.dev` answers with the Access login (checked), so it is on the application | none |

## Sport (`ac-ua/sport`, v0.28)
| Point | State | Done / next |
|---|---|---|
| Design system | v1.8 (`docs/RELEASE.md`); `web/app/app.css` said v1.7 | fixed in #54 |
| Worker `GET /status` public | **closed in v0.28** (#52): `{ ok, at }` only without the token, the full status with `Authorization: Bearer <SYNC_TOKEN>`; **live once the Worker is deployed** (by hand, not done yet) | Aurélien: deploy `sport-sync` (ledger open item) |
| `SYNC_TOKEN` in a URL | **closed in #54**: `/strava/connect` shows a form and takes the token from the POST body; constant-time checks; the Worker deploy carries it | Aurélien: rotate `SYNC_TOKEN` after the deploy (it was typed into URLs) |
| Docs on the old setup | `docs/setup.md` C.4–C.5 (old Access app « Sport data », e-mail code, `ACCESS_*` in the dashboard); ledger assets (`pages` on sport-cw7, `access-shared` « e-mail only », `worker` without the track cron, `element_logbook` « API later », Strava secrets marked live) | Roadmap: ledger and setup.md refresh at the next Sport release |
| `docs/access.md` | says the Google OAuth client is « published in production »; a closed ledger item says « Testing mode ». One is wrong | Aurélien: check in Google Cloud › Google Auth Platform › Audience (Task) |
| setup.md D.4 | suggests DNS Edit and Access Apps Edit on the cloud-session token: a session could change the only sign-in door | Roadmap: drop the suggestion |
| Leftovers | the first direct-upload Pages project: not in the account any more (Pages projects: base-camp, finance, sport, element-logbook, aureliencaye) | none |

## Finance (`ac-ua/finance`, v0.6)
| Point | State | Done / next |
|---|---|---|
| Design system | v1.7.1; v1.8 optional | v1.9 at the next release |
| Service tokens | **closed in v0.6** (#14): read-only, `GET /api/attention` and `/api/health` only; writes need JSON and no foreign `Origin` | none |
| **Tokens over-scoped** | `claude-finance` (`FINANCE_CLOUDFLARE_API_TOKEN`, env `app-finance`) still documented with D1 Edit, Pages Edit, R2 Edit, Account Settings Read, account-wide: it can write Sport's and Camp de Base's D1. Setup is over; releases need D1 Edit only (migrations) | Aurélien: edit the token down to D1 Edit (Task); Roadmap: `docs/environment.json` and `setup-cloudflare.md` A.1 to the narrowed scope |
| Docs on the old setup | `docs/HANDOFF.md` (« part C pending »), `docs/ARCHITECTURE.md:5` (« prototype running as an artifact ») and `:63` (DDL is `db/d1/`, not `db/schema.sql`), `docs/RELEASE.md:9,21` (comments on the artifact, Postgres check), `db/schema.sql` header (Supabase), `docs/environment.json` notes, `docs/PLAN-cloudflare.md` without a « done » banner | Roadmap: one docs PR from the Finance thread (this session could only read the repo) |
| Leftovers | the read-only fallback artifact « Finance · Cockpit »; `scripts/migrate_artifact.mjs`, `verify_migration.mjs` (one-shot); `db/schema.sql` (Supabase target) | Aurélien decides when to retire the artifact; the scripts go with it |
| Backup workflow hygiene | `CLOUDFLARE_API_TOKEN` at job level, `npx wrangler@4` unpinned, actions not pinned by SHA (same template in the three repos) | Roadmap: tighten the template in `platform.md` and the three workflows |
| Restore test | only in memory; the scratch-D1 restore of `platform.md` is open | after the first backup (Claude) |

## Camp de Base (`ac-ua/Base-Camp`, v5)
| Point | State | Done / next |
|---|---|---|
| Design system | v1.7.1 (the reference); v1.8 nothing to adopt | v1.9 at the next release |
| Docs on the old setup | `docs/api.md` (pages.dev address, `API_TOKEN`), `docs/deploy.md` (nightly backup), `docs/environment.json` (preflight on the Supabase host, which fails once paused) | **fixed in #230** |
| Still to refresh | ledger assets still « live » on Supabase (`d-inventory`, `d-expeditions`, `d-packing`, `d-nutrition`, `d-schedule`, `d-route`, `d-migrations`, `s-supabase-url`, `s-dburl`…); OpenAPI description (« Bearer API_TOKEN… Supabase session »), unused `BUCKET`; `scripts/build_web.py` docstring; `web/scenarios.js` prompt naming `BASECAMP_SUPABASE_*` | Roadmap: next Camp de Base release |
| CORS | `Access-Control-Allow-Origin: *` with `Authorization` allowed (`web/functions/api/[[path]].js` `cors()`): a Supabase-era leftover; the app is same-origin | Roadmap: drop it at the next release (touches `web/`) |
| `OWNER_EMAILS` | supported but off (not in `wrangler.toml`, dashboard text variables are ignored) | Aurélien: add `OWNER_EMAILS` as a Pages **secret** (your Google address), as Sport and Finance did with `ACCESS_EMAILS` (Task) |
| Supabase | project paused, not deleted; `backup.yml` (pg_dump) and `supabase.yml` manual only; `supabase/` folder and import scripts kept as history | Aurélien decides: deletion of the project, the workflows, the Pages variables `SUPABASE_*`, `API_TOKEN`, the GitHub secrets `SUPABASE_DB_URL`, `BACKUP_REPO`, `BACKUP_REPO_TOKEN`, the env secret `BASECAMP_SUPABASE_SERVICE_ROLE_KEY` (Task, nothing deleted here) |
| Scratch D1 | `camp-de-base-restore-test` still in the account (Sport's was deleted after its test) | Aurélien: delete it once the restore test is recorded (Task) |
| `_blob/[[path]].js` | dead on Pages (`_routes.json` sends only `/api/*` to Functions; `_redirects` sends `/_blob/*` to `/api/files/`), kept for `wrangler pages dev` | none |
| Artifact titles | several outside the « Camp de Base · … » rule (« Base Camp Expeditions Guide », « Expedition Gear Planner ») | Roadmap: rename in place at the next guide update |

## For Aurélien
Tasks in Notion (Owner Aurélien), in the order that matters: deploy `sport-sync` then rotate
`SYNC_TOKEN`, narrow `claude-finance`, backup token and rclone scopes, `OWNER_EMAILS` on Camp de Base, the Google OAuth
client's mode, the Supabase leftovers and the scratch D1 (his call), and the « Apps attention » connector setup
(`tools/attention-mcp/README.md`).
