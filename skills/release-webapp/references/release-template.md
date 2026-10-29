# How a release goes (<Project>)

Read by `release-webapp`. Commands only; the why lives in `AGENTS.md`.

## Version
- Current version: top entry of `<src/changelog.json>`; next = +1.

## Feedback and errors (triage)
- Read: `<GET https://…/api/v1/feedback?status=new>` (network secret for `<host>`), Notion cards with Project = <name>.
- Ignore an item: `<PATCH …>`.

## Migrations
- One path: `<python3 scripts/apply_supabase.py>` (or: Aurélien runs the SQL given in chat). Applied before merging.

## Paperwork
- Changelog: `<src/changelog.json>` (fields …).
- Config guide: Revisions row in `<docs/config-guide/body.html>`, then `<python3 docs/config-guide/build_guide.py>`.
- Ledger: `<docs/build-ledger.json>` (`json.dumps(indent=1, ensure_ascii=False)+'\n'`).
- User guide screenshots: `<node docs/guide/shots.mjs>`.

## Checks
- Full suite: `<cd tests && npm test …>` → expected counts today: <…>.
- Hosted checks: `<SUPABASE_URL=… python3 build.py && node tests/e2e/{csp,xss,pwa}.mjs dist>`.

## Deploy
- `<git push origin $H:main>` (fast-forward) or merge the PR. Release commit without `[CF-Pages-Skip]`.
- Live check: `<curl -s https://… | grep "<new string>">`.

## Artifacts to republish (in place)
| Artifact | URL | Rebuild |
|---|---|---|
| <App, claude.ai version> | <url> | `<env -u SUPABASE_URL -u SUPABASE_ANON_KEY python3 build.py>` |
| <Configuration guide> | <url> | `<…>` (page + `img/*.jpg` as files) |

## Notion
- Build Roadmap, Project = <name>; Area values: <…>.
