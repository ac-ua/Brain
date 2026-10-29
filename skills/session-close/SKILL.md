---
name: session-close
description: Write a session's deltas back to Notion before ending — facts to Memories, Tasks, Build Roadmap, ways of working to the Brain Inbox, and one Session Log row. Use at the end of every session that changed something, or when Aurélien says "close", "wrap up", "on s'arrête".
---

# session-close

Write only what changed. Small edits; never rewrite a whole page. Fetch a database before writing to it.
IDs in `docs/notion-map.md`.

## 1. Sort what you learned
| It is… | It goes to |
|---|---|
| A fact or state about Aurélien, a person, a decision | **Memories** (`collection://5b6902fc-e510-4975-b133-06e9273f602e`; one fact per row, with Type, Domain, Scope, Project, Source) |
| Something to do | **Tasks** (Status, Domain, Context, Owner, Due, Priority, Project) |
| Progress on a build | **Build Roadmap** row (Status, Version, Shipped on) |
| A stable fact of a domain | the domain card, one line, and its "Last update" |
| A way of working: a procedure, a friction, a skill or rule to improve | **Brain Inbox** (see `brain-inbox`) |

Facts never go to the Brain Inbox, ways of working never go to Memories.

## 2. Write the deltas
- Update existing rows rather than adding duplicates (search by title first).
- Close finished tasks (Status = Done). Move roadmap items you shipped to Done with `Shipped on`.
- Artifacts: every artifact made or updated is in the project's registry (`docs/artifacts.md` or the Projects row),
  and the project's guide is up to date when the architecture or screens changed.
- Code: commit, push the session branch and merge the PR once tested (on an app repo, it is the release; the same
  on `ac-ua/brain`).

## 3. One Session Log row
| Property | Value |
|---|---|
| Title | `YYYY-MM-DD · <domain> · <what>` |
| Date | today |
| Domain | main domain of the session |
| Surface | local Mac / cloud / iPad / other AI |
| Summary | 1–3 sentences, outcome first |
| Changes | what was created or changed, with links (PRs, pages, rows); what is left open |

## 4. Work continues elsewhere?
If the next step needs another session (a restart, another environment, the work Mac, later), write the handoff
with `session-handoff` (note outside the session + prompt to paste) before archiving.

## 5. Tell Aurélien
Three lines max: what changed, what's waiting on him, where to look.

## Work sessions
Notion is the system of record for work: nothing pro may live only on the work Mac or in a session. Run `work-notes`
on the session's results; it does what follows.
- Update the **deal brief** at the top of the CRM opportunity page (Work › Unify Apps › Opportunities): snapshot,
  people, numbers, solution, dated decisions, open questions, next steps, assets (artifact links, config guides,
  Drive files), one line in the meeting log. Create the opportunity (and account) if missing.
- Durable learnings (platform facts, practices, pitfalls) → Memories, Domain Work.
- Distil: decisions and facts, not transcripts. Never secrets; demo-environment logins already on a page stay there, never copied elsewhere.
- Pro *files* live in the work Drive (copies in the personal Drive are allowed); Notion holds the context and the links.
- Lessons written to a local session memory (deck lessons, client preferences) are not saved: copy them to
  Memories or, for a way of working, to the Brain Inbox.
