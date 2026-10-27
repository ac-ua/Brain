# 📓 Session Log
One row per session, written by `session-close`.

| Property | Type | Values |
|---|---|---|
| Title | title | `YYYY-MM-DD · <domain> · <what>` |
| Date | date | |
| Domain | select | the 9 domain values |
| Surface | select | local Mac · cloud · iPad · other AI |
| Summary | text | 1–3 sentences, outcome first |
| Changes | text | what was created or changed, with links; what is left open |

```sql
CREATE TABLE ("Title" TITLE, "Date" DATE, "Domain" SELECT('Work':gray, 'Expeditions':blue, 'Sport':green, 'Content':pink, 'Admin & Finance':brown, 'Career':orange, 'Learning':purple, 'Life':yellow, 'Brain':red), "Surface" SELECT('local Mac':gray, 'cloud':blue, 'iPad':green, 'other AI':orange), "Summary" RICH_TEXT, "Changes" RICH_TEXT)
```
