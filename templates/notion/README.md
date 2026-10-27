# Notion database schemas

The 6 databases of the brain, as created in phase 1. Each file lists properties, types and values, plus the DDL
accepted by the Notion MCP `create-database` tool, so a project or a domain can rebuild one identically
(e.g. a project shared outside that needs its own roadmap). Live IDs: `docs/notion-map.md`.

| File | Database | Parent |
|---|---|---|
| `tasks.md` | 📋 Tasks | workspace top level |
| `projects.md` | 📁 Projects | workspace top level |
| `build-roadmap.md` | 🛠️ Build Roadmap | workspace top level |
| `session-log.md` | 📓 Session Log | ⚙️ System |
| `brain-inbox.md` | 📥 Brain Inbox | ⚙️ System |
| `memories.md` | 🧠 Memories | ⚙️ System |

**Domain** select, everywhere: Work · Expeditions · Sport · Content · Admin & Finance · Career · Learning · Life · Brain.
Adding a domain = add the option to every Domain select, plus the routing row in `AGENTS.md`.

The brain's Memories replaces Notion Memory's own database for the brain: that one is a system database whose
schema the API can't change, so it is left as is.
