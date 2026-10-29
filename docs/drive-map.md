# Work Drive map

Aurélien's work Google Drive (`ac@unifyapps.com`, My Drive). Pro files live here; Notion holds the context and the
links (`domains/work.md`). Layout applied on 2026-10-29. Folder ids never change when a folder is renamed or moved,
so tools and links keep working.

## Tree
```
My Drive
├── 00_Inbox            drop zone: anything not yet filed. Emptied at session close
├── 01_Accounts         one folder per client or partner, named like the Notion Account (CRM)
│   └── <Account>/      flat; add subfolders only past ~10 files (Decks, Demo, POC data, Workbook, Earlier versions)
├── 02_Assets           reusable, not tied to one account
│   ├── Pitch & Platform        corporate and pitch decks, platform docs, catalogs
│   ├── Security & Architecture security, infrastructure, architecture decks
│   ├── Competitive             UnifyApps vs X (Glean, Agentforce, Power Platform…)
│   ├── Use Cases               generic use cases, POVs, concepts
│   ├── Thought Leadership      white papers and articles read
│   └── Templates               masters to copy (CEP workbook, discovery workbook)
├── 03_Demos            demo recordings and builds not tied to an account (match Notion Demo Nuggets)
├── 04_Events           one folder per event: YYYY-MM <Event> (workshops, webinars, dinners, bootcamps)
├── 05_Internal         team and company: coverage, pods, enablement, rules of engagement, Admin, SA skills feedback
├── 99_Archive          superseded or duplicate files (Superseded/). Deleting is Aurélien's call
└── Google Meet         created by Meet/Gemini (recordings, notes, transcripts). Leave as is
```

## Rules
- **Where a new file goes:** client or partner → `01_Accounts/<Account>`; reusable → `02_Assets`; event → `04_Events`;
  unsure → `00_Inbox`. Never at the root.
- **Account folder name = Notion Account name**, without the suffix ("GeBBS", not "GeBBS - New Client"). Create the
  folder with the first file of a new opportunity, and link it in the opportunity brief's Assets section.
- **File names:** `YYYY-MM-DD <Account> - <what>` for dated client material (decks, recaps, transcripts); keep the
  version in the name (`v0.3`) rather than "Copy of". Existing names were left as they were.
- **Versions:** the current one stays in the account folder; older ones go to `<Account>/Earlier versions` while the
  deal is open, or to `99_Archive/Superseded`.
- **Nothing personal** in this Drive (rule in `AGENTS.md`). Nothing is ever moved from here to personal storage.
- Session close (`session-close`, `work-notes`): files created in the session are filed, `00_Inbox` is empty or its
  rest is listed in the brief.
- Moving files is free; deleting (even to the trash) needs Aurélien.

## Folder ids
| Folder | Id |
|---|---|
| 00_Inbox | `1aaDwUIpYbP6Mt-18Bub0aNzCu2b2ftvg` |
| 01_Accounts | `1UTVePwayZoWWdqeNxBuJXB1oRgMSBWrq` |
| 02_Assets | `1b4vEftWBpKpulVlsdfe-r_LcW49I71rA` |
| 02_Assets/Templates | `1CNRPV6rAYCc61pYK-I08wUBl458FfgRj` |
| 03_Demos | `1oWbzFq7ti70KYJhrsdGekhXLcOtCSJ43` |
| 04_Events | `12UaC5yRUQpoGH-lftNHLekdwzQE7WdNr` |
| 05_Internal | `1QfllvaDolVnvrDWtTvskDhziDDziv0sV` |
| 99_Archive | `1t6BAdXSJyTXB7RnUiAJZhthzTvz5m-xl` |

Templates: CEP workbook master `1Kr61vmC8Ji3VldN1nAWbEDaMvoB76xCTallEWc3iJ-s` (used by `cep-workbook-filler`).

Account folders on 2026-10-29: Altria, Belcorp, Citi, Corning, CRST, Credit Agricole (Sofinco), Daikin, Dechert, EFE,
GeBBS, Global Payments, Hofstra, Infinite Electronics, Iron Mountain, Ivoclar, MHW Bev Co, Pernod Ricard, Prime
Technical Services (holds `PTS POC – Source files`, read by the POC by folder id), Think Artha, Trane, UPS, Webster.
Find one with Drive search `title = '<Account>'` and parent `01_Accounts`.
