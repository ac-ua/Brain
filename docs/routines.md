# Routines

Every job that runs on a schedule, or is meant to, across the brain and the projects. Times are as configured; GitHub
and Supabase cron run in UTC.

Where it runs: **cloud routine** (Claude Code scheduled task in the cloud, runs with the Mac off) · **GitHub Actions**
(scheduled workflow in a project repo) · **Supabase pg_cron** (database job inside an app) · **work Mac scheduled task**
(Claude desktop app, runs only when the Mac is on) · **manual** (Aurélien, from a reminder).

## Active
| Name | What it does | Schedule | Where it runs | Reads / writes | Status | Owner (skill or file) |
|---|---|---|---|---|---|---|
| Weekly brain maintenance | Applies accepted Brain Inbox rows as one merged PR on `ac-ua/brain`; archives finished or blocked sessions (blocked ones become Tasks); rolls over only the sessions worth restarting (weekly ones, long ones still in use); recap in French | Friday night (Saturday ~00:52 America/New_York) | cloud routine (scheduled task, fresh session per run, `perso-general`, repo `ac-ua/brain`) | reads Brain Inbox, Tasks, Build Roadmap, sessions and triggers; writes a PR, CHANGELOG, Build Roadmap, Brain Inbox status, Tasks, Session Log, a push notification | active | `skills/brain-maintenance` |
| Nightly full test suite (Element Logbook) | Runs the whole test suite on `ac-ua/c_ET` `main`; reports in French by push notification | every night 02:51 America/New_York (created 2026-10-15) | cloud routine | reads the repo; writes nothing (read-only) | active | the routine itself; tests in `ac-ua/c_ET` `tests/` |
| Check the c_ET backup after the minutes reset | One-off reminder: check that the Element Logbook nightly backup ran green once the GitHub Actions minutes are back | 2026-11-01 08:15 UTC, once | cloud routine | reads the `backup.yml` run; writes a notification | active (one-off) | `ac-ua/c_ET` `docs/MOVE.md` |
| Element Logbook database backup | `pg_dump` of the Supabase database (sign-in accounts, then the `public` schema), gzipped | every day 07:23 UTC, and on demand | GitHub Actions (`ac-ua/c_ET` `.github/workflows/backup.yml`) | reads Supabase (secret `SUPABASE_DB_URL`); writes a run artifact kept 30 days | active; blocked 16–31 Oct 2026 (Actions minutes used up), due back 2026-11-01 | `ac-ua/c_ET` `.github/workflows/backup.yml`, `DEPLOY.md` §5 |
| Camp de Base database backup | `pg_dump` of the `public` schema (gzipped) plus one CSV per table and row counts; also keeps the free Supabase project from pausing | every night 03:17 UTC, and on demand | GitHub Actions (`ac-ua/Base-Camp` `.github/workflows/backup.yml`) | reads Supabase (secret `SUPABASE_DB_URL`); writes to a private backup repo (`latest/`, `daily/`, 30 days) when `BACKUP_REPO` is set, otherwise a run artifact kept 30 days. TODO(Aurélien): confirm which of the two is live | active | `ac-ua/Base-Camp` `.github/workflows/backup.yml`, `docs/deploy.md` |
| Element Logbook programming sync | Calls the app's sync, which adds the Google Sheet's new dates as draft workouts | every day 04:00 UTC | Supabase pg_cron (`programming-sync`) | reads the Google Sheet; writes draft workouts | active | `ac-ua/c_ET` `db/migrations/043_programming_sync_cron.sql` |
| Element Logbook usage clean-up | Deletes usage events older than 13 months | every day 05:30 UTC | Supabase pg_cron (`usage-events-cleanup`) | writes `public.app_events` | active | `ac-ua/c_ET` `db/migrations/044_usage_reporting.sql` |
| Element Logbook alert digest | Emails the owner a digest, only when something happened | every day 13:00 UTC | Supabase pg_cron (`report-digest`) | reads the app's reports; sends one mail to the owner | active | `ac-ua/c_ET` `db/migrations/044_usage_reporting.sql` |
| Element Logbook error-report pruning | Deletes error reports older than 90 days | every day 04:17 UTC | Supabase pg_cron (`element-prune-client-errors`) | writes `public.client_errors` | TODO(Aurélien): active only if migration 007 was re-run after pg_cron was turned on | `ac-ua/c_ET` `db/migrations/007_client_errors_feedback.sql` |
| Expedition outreach: sponsors, research, follow-ups | One run of each outreach skill: next sponsor, next lab, overdue follow-ups. Drafts only, never sends | every morning ~08:00–08:40 | work Mac scheduled tasks | reads the Notion outreach database and pages; writes Gmail drafts and Notion updates | active. TODO(Aurélien): confirm they are still scheduled, and the time of each | `skills/expedition-sponsor-outreach`, `skills/expedition-research-outreach`, `skills/expedition-followup-outreach` |
| UnifyApps plugin learnings loop | The team plugin (`Unifyapps-Internal/unifyapps-builder-skills`) is never changed directly: each user's learnings are sent by scheduled tasks, reviewed twice a week into a release, and installed back by scheduled tasks | per the plugin's setup (sends, reviews and updates on fixed weekdays) | work Mac scheduled tasks | the plugin's own repo and `~/.claude` on the work Mac | active | the plugin's `README.md` |

## Planned and ideas
| Name | What it does | Schedule | Where it runs | Reads / writes | Status | Owner (skill or file) |
|---|---|---|---|---|---|---|
| Morning brief | A short daily brief to start the day. TODO(Aurélien): contents and channel | daily, morning | cloud routine | TODO(Aurélien) | idea | `chief-of-staff` |
| Pro learnings to the brain | Extracts generic lessons (no client names) from the UnifyApps learnings into the Brain Inbox | every 2 weeks | work Mac scheduled task (pro material stays there) | reads the pro learnings; writes Brain Inbox | idea | `skills/brain-inbox` |
| Monthly plugin copy | Copies the team plugin into this private repo as a backup | monthly | TODO(Aurélien) | reads the plugin repo; writes `backups/` | idea | TODO(Aurélien) |
| Monthly brain retro | Reviews the brain's roadmap, changelog and Session Log; feeds the weekly maintenance | monthly | cloud routine | reads Build Roadmap (Project = Brain), Session Log; writes Brain Inbox | idea | `chief-of-staff` |
| Notion export reminder | Reminds Aurélien to run the native Notion export (Markdown + CSV) to the personal Drive | monthly | cloud routine (reminder), export manual | writes a notification | idea | `docs/BLUEPRINT.md` decision 6 |
| Artifact source backup | Backs up the source and data of claude.ai artifacts | monthly | TODO(Aurélien) | writes `backups/` | idea | `backups/artifact-data/README.md` |

## How to add a routine
1. Create it where it belongs: a **cloud scheduled task** for anything personal that should run with the Mac off; a
   **GitHub Actions workflow** in the project repo for project jobs (follow `skills/build-webapp`: `timeout-minutes`,
   `concurrency`, artifacts ≤ 30 days; scheduled workflows cost minutes every run); a **work Mac scheduled task** for
   anything that touches pro material.
2. Add a row to this file (Active, or Planned and ideas while it isn't running yet).
3. Add or update its Build Roadmap row (`skills/build-roadmap`) in the project it belongs to.
4. A routine that sends, publishes or deletes anything needs Aurélien's approval first; secrets go in the platform's
   secret store, pasted by him.
