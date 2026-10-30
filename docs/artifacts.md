# Artifacts

claude.ai artifacts of the Brain project. Update each one in place (same link), never recreate it. Sources live in
this repo; pages under `docs/cockpit/` are built by `docs/cockpit/build.py` from `docs/cockpit/src/`.

| Title | Link | What it is | Source |
|---|---|---|---|
| Workspace blueprint | https://claude.ai/artifact/Cd9tm1hSrNh5bQ28QT4v3y | the brain's architecture, illustrated (French) | `docs/blueprint/workspace-blueprint.html` |
| Brain · Cockpit | https://claude.ai/artifact/UqbtEKheEFwqs7P61d6zdi | the cockpit, live on Notion: today (what waits on Aurélien, what waits in the apps through the « Apps attention » connector, top 3, inbox triage), app switcher (`apps.json`), domain map, projects, sessions, quotas (free tiers, from its own db, written weekly by `skills/free-tier-watch`), Claude panel | `docs/cockpit/src/cockpit.html` → `docs/cockpit/projects-cockpit.html` |
| Brain · Étude du cockpit | https://claude.ai/artifact/4xqmHuenUqj4EUZ292uoWF | research and design directions A, B, C for the cockpit | `docs/cockpit/cockpit-proposals.html` |
| Brain · Plateforme des apps | https://claude.ai/artifact/R41dRr422fs6kwqKr1Fdcs | how to unify the apps (federation, one sign-in, app switcher, `/api/attention`, hub), with two prototypes | `docs/cockpit/src/platform.html` → `docs/cockpit/platform.html` |
| Brain · Architecture des apps | https://claude.ai/artifact/1jYfdPk7UeMVkpJeBK6Vzb | how the apps really run (Camp de Base, Sport, Finance, the hub; Element Logbook and the website apart): addresses, Pages, Workers, D1, R2, Access, secrets by name, backups, attention; state at 2026-10-30 | `docs/cockpit/src/architecture.html` → `docs/cockpit/architecture.html` |
