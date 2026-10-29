# <Project or topic>: handoff (<YYYY-MM-DD>)

For the next session. Read this first, then <AGENTS.md / CLAUDE.md / the Notion brief>.
Current state: <version / commit / last delivery>, <live since …>.

## 1. Where everything is
| What | Where |
|---|---|
| Code | `ac-ua/<repo>`, production = `main`; work branch: the one the session is given |
| Live | <URL> (<host>, preview builds off) |
| Data | <Supabase project / Notion DB / Drive folder> |
| Roadmap | Notion Build Roadmap, `Project` = <name> |
| Artifacts | <title> — <URL> — rebuilt by `<command>` — capabilities <…> — database <collections> (update in place) |

## 2. What the environment needs (names only)
| Kind | Name | Where Aurélien sets it | Check |
|---|---|---|---|
| Variable | `<PROJECT>_SUPABASE_URL` | environment settings | `cloud-env-preflight` |
| Network secret | header for `<host>` | environment › network secrets | `curl …` → 200 |
| Allowed host | `<host>` | environment › network | reachable |
| Connector | Notion | claude.ai connectors | fetch a page |
| Tools | Python 3, Node 22, `npm ci` in … | setup script / SessionStart hook | `node -v` |

## 3. Next steps
1. <step> — done when <…>.
2. <step> — **waits on Aurélien**: <…>.

## 4. Rules learned here
- <rule> (also logged in the Brain Inbox: <link>)

## 5. Smoke test
1. `git log -1 origin/main` = <commit>; the work branch is on top of it.
2. Full test suite green: `<command>`.
3. API / site answers: `<curl>` → <expected>.
4. Artifacts: `Artifact read <url>` → writer access.
5. Notion: <row or page> readable.

## 6. Open items
- <date>: <item>.

## Prompt for the next session
```
<Area> · <subject>. Environment: <env>. Repo: <repo>.
Lis d'abord docs/HANDOFF.md, lance le smoke test (§5), dis-moi ce qui manque, puis enchaîne sur l'étape 1.
```
