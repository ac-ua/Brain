---
name: release-webapp
description: Ship a release of a personal web app the same way every time — triage feedback into the release, changelog in users' words, config guide and ledger, full test suite, hosted checks, visuals shown, deploy on Aurélien's go, live check, artifacts republished in place, Build Roadmap card, French recap. Use for every release of Element Logbook, Camp de Base, the website or any app built with build-webapp ("on livre", "envoie en prod", "ship v175", "go"), and to prepare the next release from user feedback and error reports.
---

# release-webapp

`build-webapp` says how to build for free; this skill is the **release ritual**. Each project writes its own
commands once in `docs/RELEASE.md` (template: [`references/release-template.md`](references/release-template.md));
the skill runs them in order and never skips a step silently. The project's `AGENTS.md` / `CLAUDE.md` wins on
conventions. Until a project has `docs/RELEASE.md`, use the release section it already documents (Element Logbook:
`docs/MOVE.md` §3 and `HANDOVER.md`; Camp de Base: `CLAUDE.md` and `docs/deploy.md`) and write `docs/RELEASE.md` from
it in that release.

## 0. Before: what goes in (feedback triage)
When the project collects feedback or error reports (in-app Feedback, client errors, Notion cards, screenshots
Aurélien sends):
1. Read the new items (project API or Notion), group duplicates, classify: bug · UX · request · noise.
2. Bugs: reproduce in a test first when possible. Noise and user errors: set them to Ignored through the app's
   own API, never by editing the database by hand.
3. Requests → Build Roadmap rows (`🤖 Claude suggestion` unless Aurélien asked for them).
4. Propose the release content in 3–6 lines; batch: a few releases a day at most.
"Diagnose, don't fix" means: write the diagnosis and a prompt for another session (`session-handoff`), no code.

## 1. Build on the branch
Every branch commit starts with `[CF-Pages-Skip]`. Migrations: confirm with Aurélien, apply **before** merging the
code that uses them, by the project's one documented path (`docs/RELEASE.md` §Migrations), and record which.

## 2. Release paperwork (all of it, every release)
| Piece | What |
|---|---|
| Changelog | new top entry (version, date, 2–6 word title, 1–4 points in plain words; members' wording separate from staff/admin wording where the app has both) |
| Config guide | Revisions row (newest first) + chapters touched + rebuild (`config-guide`) |
| Living guide (artifact) | updated in place by a background sub-agent after the merge, never asked first; registry line bumped |
| Ledger | `docs/build-ledger.json` change entry, same formatting as the file |
| User guide | text for any visible change; screenshots refreshed when the project has a shots script |
| Architecture | only when services, functions or connections changed |

## 3. Checks (all green, in the session)
The project's full suite (unit, db, type check, end-to-end) and its hosted-build checks (CSP, XSS, PWA…). Paste the
pass/fail counts. A red test is fixed or the release waits; never skip or disable a test.

## 4. Show, then go
Show what changes for the user (screenshots or the rebuilt artifact) in two or three lines. **Deploy only on
Aurélien's go** ("go", "envoie en prod"): the release commit without the marker reaches `main` (fast-forward or PR
merge, per the project).

## 5. After deploy
1. **Live check:** wait until production serves the new version (curl a string of the new code or the version
   endpoint); a build failure is now the top task.
2. **Artifacts:** rebuild and republish each one listed in `docs/RELEASE.md` **in place** (`Artifact read` the URL,
   then publish to the same URL). Builds for claude.ai run without the hosted variables (`env -u …`).
3. **Notion:** Build Roadmap row → Done, Version, Shipped on (`build-roadmap`; fetch the select options first).
4. **Recap to Aurélien in French**, three lines: version and what changed for users, checks (counts), what waits on
   him.

## Releasing several at once
Batch fixes into one release; if two sessions work on the same repo, only one merges: the other rebases on the
new `main` and waits. Say which session holds the release.

## Don't
- Deploy without his go, or mention "admin / developer / prototype" wording to members.
- Publish an artifact to a new URL when one exists.
- Leave a step out of the recap: if a piece was skipped (no guide change), say so.
