# 🛠️ Build Roadmap
Element Logbook roadmap schema, in English, shared by every build. One row per release or workstream.

| Property | Type | Values |
|---|---|---|
| Name | title | |
| Status | select | 🤖 Claude suggestion · Idea · To do · In progress · Done · Dropped |
| Priority | select | P0 Now · P1 Next · P2 Later · P3 Someday |
| Value | select | High · Medium · Low |
| Effort | select | S · M · L |
| Area | select | Brain: Harness · Notion · Routines · Infra · Domains · Skills. Camp de Base: Inventory · Expeditions · Partnerships · Comms & content · Accounting · Field mode. Element: Logging · Programming & coach · Progress & stats · Schedule & Mindbody · Exercise library · Admin & settings. Spanish: Vocabulary · Grammar · Sync & data · Tutor & curriculum. Shared: App & UX · Production & infra · Integrations. Add per project as needed. |
| Detail | text | |
| Version | text | |
| Shipped on | date | |
| Project | relation → Projects (two-way, synced as "Roadmap") | |

```sql
CREATE TABLE ("Name" TITLE, "Status" SELECT('🤖 Claude suggestion':purple, 'Idea':gray, 'To do':blue, 'In progress':yellow, 'Done':green, 'Dropped':red), "Priority" SELECT('P0 Now':red, 'P1 Next':orange, 'P2 Later':yellow, 'P3 Someday':gray), "Value" SELECT('High':green, 'Medium':yellow, 'Low':gray), "Effort" SELECT('S':green, 'M':yellow, 'L':red), "Area" SELECT('Harness':blue, 'Notion':gray, 'Routines':purple, 'Infra':brown, 'Domains':orange, 'Skills':pink), "Detail" RICH_TEXT, "Version" RICH_TEXT, "Shipped on" DATE, "Project" RELATION('<projects data source>', DUAL 'Roadmap'))
```
Per-project view: board grouped by Status, filter Project = the project's page.
