# Sessions

How Aurélien runs his AI sessions. Notion holds the state, this repo holds the how; sessions only execute.
Notion copy: ⚙️ System › **Sessions playbook** (`40619ca79893812a866ed99e24a6a4fc`).

## Principles
- **A session is disposable.** Nothing lives only in a session: facts and state go to Notion, ways of working to the
  Brain Inbox, code to GitHub. Any session can be archived without losing anything.
- **One session = one piece of work** (a deliverable, a release, an account's next step), not a domain or an agent
  forever. Long sessions cost more tokens and lose detail when they compact.
- **Agents are not sessions.** A session loads the skills it needs; heavy isolated work goes to a background sub-agent.
- **Never two clients in one session**, and never pro and perso together.

## Where each kind of work runs
| Work | Surface | Environment / folder | One session per | Name |
|---|---|---|---|---|
| Pro: a client account | Claude Code, local, work Mac | one folder per account | account × deliverable | `Work · GeBBS · demo v4` |
| Pro: cross-account (inbox, CRM, week prep, team plugin loop) | Claude Code, local, work Mac | work home folder | week | `Work · Ops · week 44` |
| Element Logbook code | Claude Code, cloud | `app-element` · `ac-ua/c_ET` | release or Build Roadmap row | `Element · v175 pick your team` |
| Camp de Base code | Claude Code, cloud | `app-base-camp` · `ac-ua/Base-Camp` | chantier or release | `CdB · chantier 4 inventory` |
| Sport data code | Claude Code, cloud | `app-sport` · `ac-ua/sport` | release or Build Roadmap row | `Sport · v0.14 Access` |
| Finance code (prototype, no secret yet) | Claude Code, cloud | `perso-general` · `ac-ua/finance` | release | `Finance · v0.2 bank flows` |
| Website, Spanish app, the brain | Claude Code, cloud | `perso-general` · its repo | PR | `Site · South Pole 2027` |
| Perso without code (Expeditions, Content, Sport coaching, Career, Admin, Life) | Claude Code, cloud | `perso-general` · `ac-ua/brain` | topic or task | `Exp · sponsor outreach` |
| Heavy media on personal material | cloud session, later a personal machine | `perso-general` | job | `Content · Canada doc` |
| Quick question on the go | Claude app chat (account skills + Notion connector) | — | throwaway | — |
| Spanish speaking practice | Claude app, voice (`spanish-teacher`) | — | practice | — |
| Driving any of the above from iPad or phone | Claude app → cloud sessions, or Remote Control to the work Mac | — | — | — |

Cloud environments: `perso-general` (default), `app-element`, `app-base-camp`, `app-sport`: one per app with its own
secrets, none per domain (Finance gets `app-finance` when its first secret arrives, v0.4–v0.5). In the Claude app they
are shown as **Default**, **Logbook**, **Base Camp** and **app-sport**; ids in `skills/brain-maintenance`.

claude.ai Projects are frozen: their content is copied into Notion (one page per Project under its domain); no new
Projects. Quick chats and Cowork keep no state: anything worth keeping goes to Notion or continues in a cloud session.

## Lifecycle
1. **Open** in the right place and name it `Area · subject`; say the domain or project. `session-start` loads the
   context (~8–10k tokens).
2. **Work.** Long jobs go to background sub-agents.
3. **Close** with `session-close`: Notion deltas, one Session Log row, code pushed and the tested PR merged.
4. **Archive** it in the left panel. The Session Log row and the PR are the handoff.
5. **Start a new session** rather than reopening an old one for a new deliverable, after a day on a big topic, or once
   the session has compacted.

## Left panel
- Only live work: about one session per active project plus the active pro accounts.
- A session blocked on Aurélien is not left open: its action becomes a Task, then the session is archived.
- Weekly sweep, every Friday night (Saturday ~00:52 America/New_York, `skills/brain-maintenance`), so the panel is
  clean on Saturday morning: archives finished and blocked sessions (blocked ones become Tasks first) and recreates
  only what is worth restarting (weekly sessions, long sessions still in use). Keep a session out of the sweep by
  starting its title with `Keep ·`.
- Scheduled routines run in their own sessions ([`routines.md`](routines.md)); they don't stay in the panel.
