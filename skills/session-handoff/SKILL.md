---
name: session-handoff
description: Hand work over to another session — a resume note written outside the session (repo or Notion), the inventory of artifacts, environment and access the next session needs, a smoke test, and a ready-to-paste prompt. Use before any restart or new session ("prépare la passation", "écris le prompt pour la prochaine session", "handoff", "on continue dans une session cloud"), when moving work from the work Mac to the cloud or back, when moving a project to a new environment, and whenever a step needs a restart (new environment variables, a plugin install).
---

# session-handoff

A session is disposable; the handoff is what survives it. The next session must be able to start from the note and
the prompt alone, without reading this session's transcript. `session-close` writes the deltas to Notion;
this skill writes what the **next session** needs. Template: [`references/handoff-template.md`](references/handoff-template.md).

## When
- A step needs a restart: environment variables or allowed hosts changed (they are read at session start), a plugin
  or hook was installed, the context compacted.
- The work moves: work Mac ↔ cloud, one cloud environment → another, a long session → a fresh one.
- The session ends with work left for later, or Aurélien asks for "the prompt for the next session".

## 1. Choose where the note lives (never the session's scratch folder)
| Work | Note goes to | The next session finds it by |
|---|---|---|
| Personal app or site | the repo: `docs/HANDOFF.md` (or `docs/MOVE.md` for an environment move), committed and pushed | the prompt names the file |
| The brain | `docs/HANDOFF-YYYY-MM-DD.md` on `ac-ua/brain` | same |
| Pro work (work Mac) | the CRM opportunity or Projects page in Notion (`work-notes`): a `Handoff` toggle under the brief; files stay in the work Drive | the prompt names the page |
| Personal, no repo | a Notion page under the domain or project page | same |

Rules for the path:
- **Work Mac → cloud** for personal work: the work Mac can't push to `ac-ua/*`. Put the files in a Notion page or an
  artifact (Aurélien opens it on the iPad and pastes), or let Aurélien push from another device. **Never route
  personal files through the work Drive.**
- **Cloud → work Mac** for pro work: pro material never goes to `ac-ua/*` or a cloud session. If a pro piece was
  started in the cloud by mistake, write the note to Notion, remove what was pushed (ask first: it is a deletion) and
  continue locally.
- Moving a project to a new environment: everything must already be in the repo, Notion or the account; the note
  says where each piece is.

## 2. Write the note (template)
1. **State in one paragraph:** what the work is, what is done, the current version or commit.
2. **Where everything is:** repo and branch, production URL, Notion pages and rows, Drive folders, artifacts (URL,
   how each is rebuilt, its runtime capabilities and database collections; "update in place, never a new URL").
3. **What the environment needs** (names only, never values): variables, network secrets, allowed hosts, connectors,
   tools and setup script. Use `cloud-env-preflight` to list them from the repo.
4. **Next steps,** numbered, each with its done-when. Mark what waits on Aurélien.
5. **Rules learned in this session** that aren't yet in the repo's `AGENTS.md` or the brain (then also log them with
   `brain-inbox` so they stop living in handoffs).
6. **Smoke test:** 3–7 checks the next session runs first (branch on top of `main`, tests green, API answers, artifacts
   readable with writer access, Notion row readable).
7. **Open items** with dates.

Keep it under ~120 lines; link to longer docs rather than copying them.

## 3. The prompt to paste
Give it in a code block, in Aurélien's language, ready to paste into the new session:

```
<Area> · <subject>. Environment: <env>. Repo: <repo> (attach it).
Lis d'abord <path or Notion link> puis <AGENTS.md / CLAUDE.md>. Lance le smoke test (§6), dis-moi ce qui manque,
puis enchaîne sur l'étape <n> : <one line>.
```
Name the environment and the repo to attach; say if Aurélien must change a setting first (and which).

## 4. Before leaving
- Commit and push the note (or save the Notion page) and check it is readable from outside: open the pushed file or
  the page link.
- Run `session-close` if the session changed anything.
- Tell Aurélien in three lines: where the note is, the prompt, what he must do before starting the next session.

## Don't
- Leave the only copy of a guide, a decision or a source file in a scratch folder or a session memory.
- Put secrets, tokens or demo logins in a note or a prompt. Name where they live instead.
- Write the next session's work into this one's branch name or brief when the new session will have its own branch.
