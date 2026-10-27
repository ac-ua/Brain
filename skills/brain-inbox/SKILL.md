---
name: brain-inbox
description: Log an improvement to the brain — a skill change, a new skill, a rule, or a friction — in the Notion Brain Inbox, so a later PR on ac-ua/brain can apply it. Use whenever a session discovers a better way of working, hits a recurring friction, or Aurélien says "note that for the brain".
---

# brain-inbox

The Brain Inbox is how the harness learns, from any machine, including the work Mac that can't push to GitHub.
Database: **Brain Inbox** under ⚙️ System, data source `collection://49575d7c-0da1-43c9-a54d-5a0b3c8effc4`.

## Fields
| Property | Type | Values / content |
|---|---|---|
| Title | title | the change, as an imperative: "session-start: skip About me when …" |
| Type | select | `skill change` · `new skill` · `rule` · `friction` |
| Domain | select | Work · Expeditions · Sport · Content · Admin & Finance · Career · Learning · Life · Brain |
| Status | select | `New` (default) → `Accepted` → `Applied` · or `Rejected` |
| Source session | text | Session Log title or the session URL |
| Detail | text | what happened, what to change, which file (`skills/x/SKILL.md`, `AGENTS.md` …) |

## Rules
- One row per change. Write it when it happens, not at the end of the week.
- A **fact** (date, status, preference) is not a Brain Inbox row: it goes to Memories or the domain card.
- No secrets. A pro lesson may name the client when it helps; client facts themselves go to the CRM, not here.
- Only Aurélien moves a row to `Accepted` or `Rejected`. The PR that applies it sets `Applied`.

## Examples
| Title | Type | Domain | Detail |
|---|---|---|---|
| build-webapp: run `stamp_assets.py --check` before every PR | skill change | Expeditions | Camp de Base cache stamps were stale twice; add the check to the release list |
| New skill: rushes-index | new skill | Content | Index footage on the personal Drive into a Notion catalog (transcript, shots, tags) |
| Never post to a sponsor thread from a cloud routine | rule | Expeditions | Draft only; Aurélien sends |
| Notion SQL quota hit during session-start | friction | Brain | Two queries per start is too many; use saved views |

## Applying (weekly: `brain-maintenance`)
A cloud session reads `Accepted` rows, changes the files, opens one PR on `ac-ua/brain`, bumps `CHANGELOG.md`, and
sets each row to `Applied` with the PR link in Detail once merged.
