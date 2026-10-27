# Changelog

The brain is versioned like any project: `v0.x` while the skeleton settles. Each release is a merged PR on
`ac-ua/brain` and a row in the Notion Build Roadmap (Project = Brain).

## v0.2.0 — full migration (in progress)
- Account skills moved into the repo: the 3 expedition outreach skills, `spanish-teacher`, and the pro skills
  (`unifyapps-format`, `cep-workbook-filler`, `poc-use-case-filler`, `unifyapps-rfp-rfi-response-template`).
- Confidentiality rule updated: the brain covers pro and perso; nothing personal goes to pro systems.
- Skills index per domain in `AGENTS.md`; one-source rule for skills in `README.md`.

## v0.1.0 — skeleton (2026-10-27)
- `AGENTS.md` constitution: hard rules (autonomy, confidentiality, secrets, voice), routing table, session protocol,
  startup budget. `CLAUDE.md` points to it.
- 3 agents: `chief-of-staff`, `builder`, `content-studio`.
- 7 skills: `session-start`, `session-close`, `brain-inbox`, `project-kickoff`, `build-webapp` (with the free-tier
  playbook), `build-roadmap`, `config-guide` (ledger + HTML guide).
- 8 domain files; Expeditions and Content have a first real version, the others are stubs.
- Templates: project repo (AGENTS.md, build ledger, config guide skeleton) and the 5 Notion database schemas.
- Docs: blueprint (text + HTML source), Notion map, phase 0 handoff. Explainer-video kit in `tools/`.
- Claude and Codex adapters (symlinks).
- Expeditions and Content migrated: Notion context cards with Projects/Tasks views, routing table updated.
- Archived docs (handoff, blueprint source) kept verbatim.
