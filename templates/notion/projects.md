# 📁 Projects
Registry of every project: where its code, files, artifacts and prod live.

| Property | Type | Values |
|---|---|---|
| Name | title | |
| Domain | select | the 9 domain values |
| Status | select | Idea · Active · Paused · Done |
| Repo | url | |
| Drive folder | url | |
| Artifacts | text | one "label: URL" per line |
| Prod URL | url | |
| Tasks, Roadmap | relations (synced from Tasks and Build Roadmap) | |

```sql
CREATE TABLE ("Name" TITLE, "Domain" SELECT('Work':gray, 'Expeditions':blue, 'Sport':green, 'Content':pink, 'Admin & Finance':brown, 'Career':orange, 'Learning':purple, 'Life':yellow, 'Brain':red), "Status" SELECT('Idea':gray, 'Active':green, 'Paused':yellow, 'Done':blue), "Repo" URL, "Drive folder" URL, "Artifacts" RICH_TEXT, "Prod URL" URL)
```
