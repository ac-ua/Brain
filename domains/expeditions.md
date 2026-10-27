# Domain: Expeditions

Polar and adventure expeditions: planning, gear, logistics, budget, partners and sponsors, science partnerships.
Notion domain page: **🧭 Expeditions** (`83e58afbe55443f1b234ef36a63a3c1f`); its context card is at the top of the page.
It holds the goals and facts; this file only says how each capability works here.

## Where things live
| What | Where |
|---|---|
| Expeditions page (Notion) | `83e58afbe55443f1b234ef36a63a3c1f` |
| **Sponso** database (brands + science partners) | `collection://2ae19ca7-9893-80d6-b263-000b7171b431` — **never move or rename its statuses without a validated plan**: the outreach skills read and write it |
| Camp de Base app | repo `ac-ua/Base-Camp`, cloud environment `app-base-camp` |
| Camp de Base roadmap & changelog (Notion, to merge into Build Roadmap at migration) | `collection://6aec51dc-a4b4-4f69-be60-341dea003e59` |
| Old memories for this domain | 🧳 Brain — Migration inbox (`40619ca7989381cf9cb4dda8206db206`) |

## How each capability applies
**builder — Camp de Base.** The expeditions control tower (inventory, expeditions, packing, route, logistics, budget,
field mode, calendar, nutrition). The repo's `CLAUDE.md` and `docs/HANDOFF.md` win on conventions: answers in French,
`[CF-Pages-Skip]` on every branch commit, `python3 scripts/stamp_assets.py` after `web/*.js|css` changes, migrations via
`scripts/apply_supabase.py` **before** merging the code that uses them, one Notion changelog row per release.
Work in the `app-base-camp` environment (it holds the app's secrets).

**chief-of-staff — outreach and deadlines.** Sponsor, research and follow-up outreach run through three skills in this
repo (`skills/expedition-sponsor-outreach`, `skills/expedition-research-outreach`, `skills/expedition-followup-outreach`). They
create **Gmail drafts only** and update Sponso; Aurélien sends. Gmail connector = the sponsors mailbox.
Deadlines (permits, logistics payments, partner promises) go to Tasks with Domain = Expeditions.

**content-studio.** Expedition films and posts: see `domains/content.md`. Partner promises (what a sponsor gets in
content) are tracked in Camp de Base's partnerships module once it exists; until then, in Sponso.

## Rules
- Never send to a brand, a lab or the press without Aurélien. Drafts only.
- Partner and sponsor data stays in Notion/Camp de Base; no copy in this repo.

## TODO(Aurélien)
- Context card: current goals (expedition dates, funding target) — fill during the migration.
