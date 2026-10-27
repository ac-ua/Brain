---
name: brain-maintenance
description: Weekly upkeep of the brain — apply accepted Brain Inbox rows as one merged PR on ac-ua/brain, close the week (archive finished or blocked sessions, turning loose ends into Tasks), open the week (one empty session per planned piece of work), and send a French recap. Use for the Friday weekly routine, or when Aurélien says "brain maintenance", "maintenance du brain", "weekly sweep".
---

# brain-maintenance

Runs every Friday at ~01:00 America/New_York as a cloud scheduled task (fresh session, environment `perso-general`,
repo `ac-ua/brain`, Notion connector), listed in [`docs/routines.md`](../../docs/routines.md). Can also be run by hand.
Unattended: do every step, decide alone within the rules below, and report at the end.

## Hard rules
- **No deletion** of anything: no Notion page or row, file, branch, repo, session. Archiving a session is allowed
  (it is reversible).
- **No external send**: no mail, message or post. The final message is the only notification.
- **No secrets**, anywhere. **Never touch Sponso.**
- Never edit a Notion page Aurélien has reviewed; only rows of the databases named here.

## 1. Load context
- `AGENTS.md`, [`docs/sessions.md`](../../docs/sessions.md) (naming, environments), [`docs/notion-map.md`](../../docs/notion-map.md) (IDs).
- Notion free plan: read with `fetch` and saved views; SQL queries are capped at ~13/hour, use at most a few.
- Fetch each database once before writing to it.

| Database | Data source |
|---|---|
| Brain Inbox | `collection://49575d7c-0da1-43c9-a54d-5a0b3c8effc4` (view "Latest Brain Inbox") |
| Tasks | `collection://d2dce682-22a5-4e39-b0d3-75b9399b5c47` (views Today, Inbox, Perso, Work) |
| Build Roadmap | `collection://8ce17531-538f-4186-9f58-8a8c17c14a14` |
| Session Log | `collection://89c0d830-aec0-4bd7-b16f-f2d939db3d58` |
| Projects | `collection://127dc180-4e2f-4650-b120-0b4ff4cc9eab` (Brain row `40619ca79893817ba7cbc34ca914eed7`) |

## 2. Brain upkeep (one PR)
1. Read the Brain Inbox rows with Status `Accepted`. Add `New` rows only when they are clearly safe (wording, a
   missing step, a friction with an obvious fix; no new rule on autonomy, confidentiality or secrets); list each
   one you take in the recap.
2. Nothing to apply → no branch, no PR; go to step 3.
3. Branch `claude/brain-maintenance-<YYYY-MM-DD>` from `origin/main`. Apply each row with small edits to the file in
   its Detail; follow the style of the file you touch (English, concise, finished reference).
4. Bump `CHANGELOG.md`: a new patch version (`v0.x.y+1`) listing the changes, one line per row.
5. Commit, push, open one PR (body: one line per Inbox row with its title). Re-read the full diff; if anything is
   wrong or out of scope, fix it or drop that row. Merge (squash). If the merge API fails, fast-forward `main` only
   when `origin/main` is an ancestor of the branch; otherwise leave the PR open and say so in the recap.
6. Build Roadmap row: Project = Brain, Status `Done`, Version, Shipped on = today, Detail with the PR link.
7. Each applied Inbox row → `Applied`, PR link added to Detail. A row you could not apply stays as is; say why in
   the recap.

## 3. Close the week (sessions)
Use the claude-code-remote tools: `list_sessions` (mine: true) and `list_triggers`.

**Never archive:**
- the running maintenance session itself;
- a session bound to a trigger (the `persistent_session_id` of an enabled trigger);
- a session with activity in the last 48 h;
- a session whose title starts with `Keep ·`.

**Archive** any other session when:
- its status is completed or idle and it has had no activity for ≥ 2 days; or
- it is blocked on Aurélien: first create a Task (Status `Inbox`, Owner Aurélien, the session's needs-action text,
  the session title in the task so he can find it), then archive.

Local work-Mac sessions (environment `bridge`) follow the same rules.

## 4. Open the week (sessions)
Planned work only:
- Build Roadmap rows with Status `In progress` or Priority `P0 Now` (not Done or Dropped);
- Tasks due in the next 7 days, or with Status `Next` or `Doing`.

Group them **one session per project or topic, 5 at most** (most urgent first). Skip a group that already has a
live session for the same work. Call `list_environments`, then `create_session`:

| Work | Environment | Repo |
|---|---|---|
| Element Logbook | `app-element` | `ac-ua/c_ET` |
| Camp de Base | `app-base-camp` | `ac-ua/Base-Camp` |
| Personal website | `perso-general` | `ac-ua/website` |
| Brain, and any perso topic without code | `perso-general` | `ac-ua/brain` |

- Title `Area · subject`, as in [`docs/sessions.md`](../../docs/sessions.md) (`Element · v175 pick your team`).
- **No initial prompt**: nothing runs until Aurélien writes in it.
- Pro and client work cannot be created from the cloud: list the `Work · <client>` sessions to open on the work Mac
  in the recap instead.

## 5. Recap
1. One Session Log row (`session-close` format): Title `YYYY-MM-DD · Brain · weekly maintenance`, Domain Brain,
   Surface cloud, Summary, Changes (PR, archived and created sessions, tasks).
2. A short final message **in French** (it becomes the push notification), about 10 lines:
   - PR merged (link, version) or « aucune PR » ;
   - sessions archivées : nombre + titres ;
   - sessions créées : titres ;
   - tâches créées ;
   - sessions à ouvrir sur le Mac pro ;
   - bloqué : tâches en retard, `TODO(Aurélien)` restants dans `docs/routines.md`, PR non fusionnée.

## Run by hand
Same steps. Aurélien is present: ask before archiving a session you are unsure about, and before applying a `New`
Inbox row.
