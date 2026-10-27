---
name: session-start
description: Load the minimum context to start working in the brain — AGENTS.md, the About me profile, the domain page (its context card), and the project's state. Use at the start of every session, or when switching to another domain or project.
---

# session-start

Goal: the right context in **~8–10k tokens**, nothing more. Load in this order and stop there.

1. **`AGENTS.md`** (already loaded by `CLAUDE.md` in Claude Code). Note the hard rules and the routing table.
2. **About me**: `fetch` Notion page `40619ca7989381599acfdce904faf34f`. Do not fetch the whole Memories database.
3. **Domain**: find the domain in the routing table, `fetch` its Notion domain page and read the context card at the
   top (< 60 lines); the sub-pages listed below it are opened only if the task needs them. Read `domains/<domain>.md`.
   Unsure of the domain → ask once.
4. **Project state** (only if the session is about a project):
   - the Projects row (repo, prod URL, artifacts);
   - the Build Roadmap view on the project page (In progress, To do);
   - open Tasks for the project or domain (a saved view, not a SQL query).
5. **Memories** (`collection://5b6902fc-e510-4975-b133-06e9273f602e`): only if a specific fact is missing, search by keyword or filter by Domain. One fact per row.
6. Say in two or three lines what you loaded and what you're about to do.

## Don't
- Load other domains, the Migration inbox, old transcripts or whole databases "just in case".
- Use Notion SQL queries when a view or `fetch` works (free plan: ~13 queries per hour).
- Load sub-agents for the start; skills are cheaper.

## Measuring
During the "Mac lost" drill, note the tokens used by steps 1–4 in the Session Log row (Changes field).
