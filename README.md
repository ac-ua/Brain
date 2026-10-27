# brain

Aurélien's AI workspace, independent of any machine and of any AI.

| Layer | Where | Answers |
|---|---|---|
| Knowledge and state | Notion (personal workspace): profile, memories, tasks, projects, roadmap, domain cards | *what, and where are we?* |
| Harness | this repo: rules, agents, skills, templates | *how do we do it?* |
| Execution | any AI that reads `AGENTS.md` / `SKILL.md` and speaks MCP | *do it* |
| Files | Google Drive (personal and work, kept apart) | inputs and outputs |

This repo holds only text we write ourselves. It is never a copy of Notion, and it holds no secrets. Rules and skills
hold no client names or pro data; archived docs in `docs/` are kept verbatim. Full design: [`docs/BLUEPRINT.md`](docs/BLUEPRINT.md). Notion IDs: [`docs/notion-map.md`](docs/notion-map.md).

## Layout
```
AGENTS.md        the constitution: rules, routing, session protocol (read first)
CLAUDE.md        @AGENTS.md
agents/          one file per capability: chief-of-staff, builder, content-studio
skills/          one SKILL.md folder per skill
domains/         how each capability applies in a domain
templates/       project repo skeleton, Notion database schemas
docs/            blueprint, Notion map, handoffs
tools/           raw material for future skills (explainer-video kit)
.claude/         Claude adapter: agents/ and skills/ are symlinks, minimal settings
.agents/skills   adapter for Codex and other AIs (symlink to skills/)
```

## Use it
**Claude Code, cloud session** (`claude.ai/code`): start a session on `ac-ua/brain` in the `perso-general`
environment. `CLAUDE.md` loads `AGENTS.md`; agents and skills load from `.claude/`. Say what you want to work on and
which domain; the `session-start` skill does the rest.

**Claude Code, local** (any Mac): `git clone https://github.com/ac-ua/brain` and run `claude` in it. To use the skills
from another project, symlink or copy `skills/<name>` into that project's `.claude/skills/`.
On the work Mac the repo is read-only (the proxy blocks pushes): ways of working go to the Brain Inbox in Notion.

**iPad or phone**: drive a cloud session from the Claude app. Nothing to install.

**Codex, ChatGPT or another AI**: point it at this repo. It reads `AGENTS.md`, finds skills in `.agents/skills/`, and
needs a Notion MCP connection for state. Claude-specific frontmatter (`tools`, `skills`) is ignored safely.

## Change it
- A fact or a state → Notion, right away.
- A way of working → a row in the Notion **Brain Inbox** (any session, any machine).
- The harness itself → a PR on this repo from a cloud session, merged by the session once re-read. A weekly routine
  (planned) turns accepted Brain Inbox rows into such a PR.
- Each merged release bumps `CHANGELOG.md` and gets a Build Roadmap row (Project = Brain).
