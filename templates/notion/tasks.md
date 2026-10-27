# 📋 Tasks
One task list for everything. The Work / Perso switch is the Context property.

| Property | Type | Values |
|---|---|---|
| Name | title | |
| Status | status | Inbox (to do, default) · Next (to do) · Doing (in progress) · Waiting (in progress) · Done (complete) |
| Domain | select | the 9 domain values |
| Context | select | Work · Perso |
| Owner | select | chief-of-staff · builder · content-studio · Aurélien |
| Due | date | |
| Priority | select | P0 Now · P1 Next · P2 Later · P3 Someday |
| Project | relation → Projects (two-way, synced as "Tasks") | |

```sql
CREATE TABLE ("Name" TITLE, "Status" STATUS('Inbox':gray:to_do, 'Next':blue:to_do, 'Doing':yellow:in_progress, 'Waiting':orange:in_progress, 'Done':green:complete), "Domain" SELECT('Work':gray, 'Expeditions':blue, 'Sport':green, 'Content':pink, 'Admin & Finance':brown, 'Career':orange, 'Learning':purple, 'Life':yellow, 'Brain':red), "Context" SELECT('Work':gray, 'Perso':blue), "Owner" SELECT('chief-of-staff':purple, 'builder':blue, 'content-studio':pink, 'Aurélien':green), "Due" DATE, "Priority" SELECT('P0 Now':red, 'P1 Next':orange, 'P2 Later':yellow, 'P3 Someday':gray), "Project" RELATION('<projects data source>', DUAL 'Tasks'))
```
