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
├── 99_Archive          dead material with no future use. Deleting is Aurélien's call
└── Google Meet         created by Meet/Gemini (recordings, notes, transcripts). Leave as is
```

## Filing at creation (automatic)
Every pro file an agent creates is saved straight to its place, then linked in Notion, in the same step and without
asking. Aurélien never uploads or files by hand.
1. **Place:** pick the folder by the rules below; create the account, event or sub-folder if missing (create, never
   delete or rename his folders).
2. **Save:** with the Drive connector (`create_file` with the folder id as `parentId`; Google Docs/Sheets/Slides when
   the content allows it). The Drive app on the work Mac syncs the **personal** Drive only, so it is no way into
   this Drive. A local output the connector cannot upload (large pptx, mp4, pdf) goes on the **upload list**: see
   below.
3. **Link:** the file's Drive link goes on the Notion page it belongs to: the opportunity brief's Assets (client), the
   Projects row (cross work), the Work card (internal or event), with one line on what it is and its date.
4. **Report:** tell Aurélien the path and the link in the recap.

## Upload list (what the connector could not upload)
At session close, every pro file that is still only local is listed, for Aurélien to drag in by hand:
- one file `TO-UPLOAD.md` in the session's output folder: for each file its local path, its target folder name and
  the target folder's Drive link (`https://drive.google.com/drive/folders/<id>`), its Notion page;
- the same list in the recap, as « Couldn't upload through the Drive connector: drag `<file>` into `<link>` ».
Once he has uploaded them, the next session links the files in Notion (step 3).

## Files shared with Aurélien
A Drive link he passes on (a deck a colleague made on GeBBS) is never copied: it gets a **shortcut**, without asking.
The Drive connector cannot create shortcuts, so an Apps Script does (`tools/drive-shortcuts/`):
1. Append a row to the Sheet **Drive shortcut queue** (`05_Internal`, id `1rwFq1rhc3Zeh0b2RnGIxwDRw6BcG5I5bTt9Yt5j49zw`)
   with the Sheets connector: date · file link · target (`<Account>` or `<Account>/<sub-folder>` under `01_Accounts`,
   or a folder link) · optional name. The script creates the shortcut within 5 minutes (and missing folders).
   **Target = where Aurélien will use it, not who it was made for**: a colleague's deck for another client that he
   reuses as material goes to `02_Assets/<sub-folder>` (e.g. Competitive), not to that client's folder. Unsure: ask.
2. Put the file's link on the Notion page right away (opportunity brief's Assets, « shared by <name> »).
3. Rows marked `Error` (no access, bad link) are reported to Aurélien by the next session.

## Rules
- **Where a new file goes:** client or partner → `01_Accounts/<Account>`; reusable → `02_Assets`; event → `04_Events`;
  unsure → `00_Inbox`. Never at the root.
- **Account folder name = Notion Account name**, without the suffix ("GeBBS", not "GeBBS - New Client"). Create the
  folder with the first file of a new opportunity, and link it in the opportunity brief's Assets section.
- **File names:** `YYYY-MM-DD <Account> - <what>` for dated client material (decks, recaps, transcripts); keep the
  version in the name (`v0.3`) rather than "Copy of". Existing names were left as they were.
- **Versions:** the current one stays in its folder; older ones are kept (history) in an `Earlier versions` sub-folder
  next to it, named `YYYY-MM-DD <name> (v1)`, `(v2)`… or `(draft 1)`.
- **Nothing personal** in this Drive (rule in `AGENTS.md`). Copies of pro files to the personal Drive are allowed.
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

Account folders on 2026-10-29: Altria, Citi, Corning, CRST, Credit Agricole (Sofinco), Daikin, Dechert, EFE,
GeBBS, Global Payments, Hofstra, Infinite Electronics, Iron Mountain, Ivoclar, Pernod Ricard, Prime
Technical Services (holds `PTS POC – Source files`, read by the POC by folder id), Think Artha, Trane, UPS, Webster.
Find one with Drive search `title = '<Account>'` and parent `01_Accounts`.
