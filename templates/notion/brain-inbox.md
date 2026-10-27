# 📥 Brain Inbox
Ways of working to fold into the harness. Usage: `skills/brain-inbox`.

| Property | Type | Values |
|---|---|---|
| Title | title | the change, as an imperative |
| Type | select | skill change · new skill · rule · friction |
| Domain | select | the 9 domain values |
| Status | select | New · Accepted · Applied · Rejected |
| Source session | text | Session Log title or session URL |
| Detail | text | what happened, what to change, which file |

```sql
CREATE TABLE ("Title" TITLE, "Type" SELECT('skill change':blue, 'new skill':green, 'rule':purple, 'friction':orange), "Domain" SELECT('Work':gray, 'Expeditions':blue, 'Sport':green, 'Content':pink, 'Admin & Finance':brown, 'Career':orange, 'Learning':purple, 'Life':yellow, 'Brain':red), "Status" SELECT('New':gray, 'Accepted':blue, 'Applied':green, 'Rejected':red), "Source session" RICH_TEXT, "Detail" RICH_TEXT)
```
