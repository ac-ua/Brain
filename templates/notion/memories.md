# 🧠 Memories
One fact or state per row. Ways of working go to the Brain Inbox, not here.

| Property | Type | Values |
|---|---|---|
| Title | title | the fact, in one line |
| Type | select | Profile · Preference · Fact · Decision · People · Notes |
| Domain | select | the 9 domain values |
| Scope | select | Work · Perso |
| Project | relation → Projects (two-way, synced as "Memories") | |
| Detail | text | context, why it matters |
| Source | text | session, page or date it came from |
| Created, Last edited | created / last edited time | |

```sql
CREATE TABLE ("Title" TITLE, "Type" SELECT('Profile':purple, 'Preference':blue, 'Fact':green, 'Decision':orange, 'People':yellow, 'Notes':gray), "Domain" SELECT('Work':gray, 'Expeditions':blue, 'Sport':green, 'Content':pink, 'Admin & Finance':brown, 'Career':orange, 'Learning':purple, 'Life':yellow, 'Brain':red), "Scope" SELECT('Work':gray, 'Perso':blue), "Project" RELATION('<projects data source>', DUAL 'Memories'), "Detail" RICH_TEXT, "Source" RICH_TEXT, "Created" CREATED_TIME, "Last edited" LAST_EDITED_TIME)
```
