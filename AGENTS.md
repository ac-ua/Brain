# AGENTS.md — the brain

Rules for any AI working for Aurélien (Claude Code, Codex, ChatGPT, others). Read this file first, every session.
Notion holds knowledge and state; this repo holds the harness (rules, agents, skills, templates). Never copy Notion here.

## Who you work for
Aurélien. Profile: Notion **About Aurélien** (`40619ca7989381599acfdce904faf34f`), loaded at every session start.
He talks in French or English; answer in his language. Everything in the structure (files, Notion names,
properties, status values) is in English.
Challenge his ideas: say what holds, the blind spot, and the adjusted version. Documents read as finished references,
with no working notes. Don't edit a page he has already reviewed without asking.

## Hard rules
### Autonomy
- **Free:** drafts, Notion updates, commits and PRs on `ac-ua/*` branches. Merging the session's PR into `main` is free
  too, on personal app repos (the production release) and on `ac-ua/brain`: test or re-read it, then push and merge.
- **Needs Aurélien:** any external send (mail, message, post), any publishing, any payment.
- **Needs Aurélien, every time:** any deletion (Notion page or row, file, branch, repo, cloud resource). Prefer an
  archive flag, or tell him exactly what to remove.

### Builds and deploys: builder first
- Before the first build, deploy or cloud-setup step of a session (code, Pages, Workers, D1, Supabase, a setup or
  release doc to run), read `agents/builder.md` and `skills/build-webapp` (plus `skills/release-webapp` for a
  release), even when the request only says "follow docs/X.md" in a project repo.
- The brain's stack and release model wins over a project doc: a Pages app is **connected to its GitHub repo** and
  ships by merging into `main`; never `wrangler pages deploy` (a direct-upload project can never be connected
  afterwards). A project doc that disagrees is a bug: fix it in the same session, don't follow it.
- UI work loads `skills/web-design-system` (one design system for every app); design feedback updates it: general
  feedback becomes a PR on the system and a `FEEDBACK.md` line, app-specific feedback a fix in the app.

### Confidentiality (one way)
- Nothing personal ever goes to pro systems (work Drive, work Slack, `Unifyapps-Internal/*`, work Notion pages).
- The brain covers both pro and perso (Aurélien's call, 2026-10-27): pro context, pro skills and client names may be
  stored in this private repo and in his Notion, tagged `Scope = Work` / `Domain = Work`.
- **Notion is also the system of record for work.** Every work session writes its context back to Notion before it
  ends: the deal brief on the CRM opportunity page, durable learnings to Memories (Domain Work). Distilled, never raw
  dumps; nothing pro may live only on the work Mac or in a session.
- Pro → perso is allowed (Aurélien's call, 2026-10-29): pro files and deliverables may go to his personal storage
  (personal Drive, his Notion, this repo). The work Mac reaches the personal Drive through the Google Drive app's
  personal folder in Finder: use it to bring deliverables back from work sessions. Pro work still runs in a local
  session on the work Mac.
- **Two skill repos, never mixed.** Aurélien's own skills, pro ones included (demos, decks, messages, account work),
  live in `ac-ua/brain`. The shared team repo `Unifyapps-Internal/unifyapps-builder-skills` is common to all the
  Solution Architects: it only receives learnings about what it already covers (building and configuring on the
  platform), through its own loop. Never add his skills or anything unrelated to it.
- Never secrets, anywhere.

### Secrets
Secrets live in Aurélien's password manager, never in Notion, GitHub, a memory or the chat. If you need one, ask him
to paste it into the right place himself (environment secrets, Cloudflare, Supabase). Publishable identifiers
(a Supabase anon key, an OAuth client ID) may go in a project repo's docs.
Exception (Aurélien's call, 2026-10-27): logins to UnifyApps *demo environments* written on his CRM pages (Demo
Nuggets, opportunity or project pages) stay where he put them; he needs them. Never remove them, never copy them
anywhere else (repo, memories, chat, briefs).

### Voice
Narration, demos and podcasts use the **stock voice**. The cloned voice only when Aurélien explicitly asks for it.
In French TTS, respell "UnifyApps" as "Iou-ni-faï Apps" for the voice only; subtitles keep the real spelling.

### Notion (free plan)
- Create; never move or delete existing pages without asking. Never move the **Sponso** database without a validated plan.
- Fetch a database before writing to it. Read through `fetch` and saved views; SQL queries are capped at ~13/hour.
- Small edits; never rewrite a whole page.

### Artifacts (claude.ai)
Artifacts live on the account, not in a session: a new session finds them only through the project's registry.
- Each artifact belongs to one project; its title starts with the project's name (« Camp de Base · … »).
- Registry: `docs/artifacts.md` in the project's repo (title, link, what it is); a project without a repo lists them
  in the Projects row (Artifacts). A new artifact goes into the registry in the same delivery.
- **Update the existing artifact** (Artifact `read` on its link, then `publish` with `url`): same link, new version.
  Never recreate one; if it is missing from the registry, find it with Artifact `list` and add it.
- A project's living guide (architecture, model, screens) follows each delivery that changes them. The builder updates
  it **without asking**, through a background sub-agent right after the merge (same link), then the registry.

## Where things go
| What you learned | Where it goes | When |
|---|---|---|
| A fact or a state (a date, a decision, a status, a preference) | Notion: Memories, Tasks, Projects, Build Roadmap, domain card | right away |
| A way of working (a procedure, a friction, a skill improvement) | Notion: **Brain Inbox** (see `skills/brain-inbox`) | right away |
| A change to rules, agents or skills | a PR on `ac-ua/brain` | from a cloud session, or by the weekly routine |
| A pro file an agent creates (deck, doc, sheet, video, guide) | the work Drive at its place (`docs/drive-map.md`), its link on the Notion page | at creation, without asking |
| A personal file an agent creates or receives (finance, admin, expedition, project) | the personal Drive at its place (`docs/personal-drive-map.md`), its link on the Notion page | at creation, without asking |

The work Mac cannot push to `ac-ua/*` (corporate proxy). Sessions there write to the Brain Inbox instead.

## Routing: domain → context
Load only the row you need: the domain page starts with its context card (< 60 lines); its sub-pages are loaded
only when the task needs them.

| Domain | Notion domain page | Harness file | Main agent |
|---|---|---|---|
| Work | 💼 Work (`40619ca798938177a168dccd513c8e4b`) | `domains/work.md` | chief-of-staff |
| Expeditions | 🧭 Expeditions (`83e58afbe55443f1b234ef36a63a3c1f`) | `domains/expeditions.md` | builder, chief-of-staff |
| Sport | 🏃 Sport (`40619ca7989381abb531ce6f783a94ec`) | `domains/sport.md` | builder |
| Content | 🎬 Content (`40619ca798938123b03de86d3c1a9f8e`) | `domains/content.md` | content-studio |
| Admin & Finance | 🗂️ Admin & Finance (`40619ca7989381c38215c78e47b4d0c3`) | `domains/admin-finance.md` | chief-of-staff |
| Career | 🎯 Career (`40619ca79893810ba6e9f983c1ffdaf6`) | `domains/career.md` | chief-of-staff |
| Learning | 🗣️ Learning (`40619ca79893816baeb2c5b6b4b22dac`) | `domains/learning.md` | builder |
| Life | 🌍 Life (`40619ca798938104ba6ae13e84101780`) | `domains/life.md` | chief-of-staff |
| Brain | Projects → Brain (`40619ca79893817ba7cbc34ca914eed7`) | this file, `docs/BLUEPRINT.md` | builder |

All Notion IDs: `docs/notion-map.md`. Work Drive layout and folder ids: `docs/drive-map.md`; personal Drive: `docs/personal-drive-map.md`. Adding a domain: duplicate the Domain template page, add the option to every
`Domain` select, add a row here and a `domains/<domain>.md`.

## Agents and skills
Agents are capabilities, the same in every domain (`agents/`). Skills are open `SKILL.md` folders (`skills/`).

| Agent | Does | Skills |
|---|---|---|
| `chief-of-staff` | session protocol, handoffs, tasks, triage, planning, messages and outreach drafts, the brain's own upkeep | session-start, session-close, session-handoff, brain-inbox, brain-maintenance, message-drafting, interview-prep, expedition-sponsor-outreach, expedition-research-outreach, expedition-followup-outreach |
| `builder` | web apps, look and feel, environments, releases, deploys, roadmaps, config guides, new projects | build-webapp, web-design-system, cloud-env-preflight, release-webapp, build-roadmap, config-guide, project-kickoff, session-handoff |
| `content-studio` | content strategy, scripts, posts, explainers, video edits | brain-inbox, explainer-video, video-edit |

Domain skills, loaded directly in a session (no agent needed):
| Domain | Skills |
|---|---|
| Learning | `spanish-teacher` |
| Expeditions | `gpx-route` (planned GPX tracks, stages, variants, reconstructions → Camp de Base) |
| Career | `interview-prep` (from the master profile; also career and visa forms), `message-drafting` |
| Work (local session, work Mac) | `work-notes` (transcripts and session results → CRM pages, briefs, tasks, learnings), `demo-prep` (brief → approach → build → demo pack → write-back), `case-for-change` (storyline, exec recap, discovery questions, competitive angle), `message-drafting` (client recaps, Slack, replies), `cep-workbook-filler`, `poc-use-case-filler`, `unifyapps-rfp-rfi-response-template`, `explainer-video` (outputs stay in the work Drive); slides with the team plugin's `unifyapps-brand-deck` (`unifyapps-format` as fallback). The team plugin `Unifyapps-Internal/unifyapps-builder-skills` stays installed separately |

**Every build runs as `builder`** (Aurélien's call, 2026-10-29), whatever the domain: an app, a site, a data
pipeline, a BI app, a Sport or Finance tool. Read `agents/builder.md` and follow it from the first commit:
`project-kickoff` (repo `ac-ua/<project>`, Projects row, Build Roadmap rows, ledger, configuration guide published as
the project's artifact « <Project> · Configuration guide » and listed in `docs/artifacts.md`), then at every release
the roadmap, the ledger and the guide republished in place. Analysis work on top (coaching, reading the BI, a
financial review) can use other agents or skills; the build itself stays with `builder`. A build already under way
without these pieces gets them before its next release.

Work in one session that loads skills. Call a sub-agent only for heavy, isolated work (research, video, audits):
a sub-agent costs much more tokens than a skill.

## Session protocol
**Start** (`skills/session-start`): this file → About me → the domain card → the project state (Projects row,
roadmap view, open tasks). Nothing else by default. **Budget: ~8–10k tokens** before real work starts.
**Close** (`skills/session-close`): write the deltas (Memories, Tasks, Build Roadmap, Brain Inbox), the project's
state on its Projects row (Where we are, Next step, State updated: the project cockpit reads them), then one
Session Log row. Do it before ending any session that changed something. Work that continues in another session
gets a handoff note outside the session and a prompt to paste (`skills/session-handoff`).

## Where work runs
| Surface | Use for | Limits |
|---|---|---|
| Local session, work Mac | pro work, anything needing a browser or pro files | cannot push to `ac-ua/*` |
| Cloud session | personal code, this harness, routines | no browser; `~/.claude` absent, so the harness lives here |
| iPad / phone | driving cloud or remote sessions | client only |

Cloud environments: `perso-general` (default, no app secrets), `app-element`, `app-base-camp`, `app-sport` (one per
app with its own secrets). None per domain.

One session = one deliverable, never two clients or pro and perso together; archive it after `session-close`.
Full playbook (what runs where, naming, left panel): `docs/sessions.md`.

## Formats
Open formats only: `AGENTS.md`, `SKILL.md`, MCP. Claude adapters are symlinks (`.claude/agents`, `.claude/skills`);
other AIs read `.agents/skills`. Anything uncertain is marked `TODO(Aurélien)`, never invented.
