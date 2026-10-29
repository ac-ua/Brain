# Drive shortcut queue

Adds a **shortcut** (never a copy) in the work Drive for any Drive file shared with Aurélien, so a colleague's GeBBS
deck shows up in `01_Accounts/GeBBS`. The Drive connector cannot create shortcuts; this Apps Script can, and it needs
no secret and no network access from the session: agents only write a row in a Google Sheet.

- Queue: Google Sheet **Drive shortcut queue** in `05_Internal`
  (`1rwFq1rhc3Zeh0b2RnGIxwDRw6BcG5I5bTt9Yt5j49zw`), columns: Requested · File link · Target folder · Shortcut name ·
  Status · Shortcut link · Note.
- Script: `Code.gs`, bound to that Sheet, runs every 5 minutes as `ac@unifyapps.com`.

## Install (once, ~2 minutes, Aurélien)
1. Open the Sheet → **Extensions → Apps Script**.
2. Replace the content of `Code.gs` with this folder's `Code.gs`, save.
3. Pick `setup` in the function list → **Run** → allow access (Drive, Sheets) with `ac@unifyapps.com`.
   It installs the 5-minute trigger and processes the queue once.

## How agents use it
1. Append a row with the Sheets connector (`update_values` on the next empty row of the first sheet):
   date, the file link Aurélien gave, the target (`<Account>` or `<Account>/<sub-folder>` under `01_Accounts`, or a
   folder link), optional name. Leave Status empty.
2. Put the file's link on the Notion page right away (opportunity brief's Assets, « shared by <name> »).
3. Within 5 minutes Status reads `Done` (or `Exists`) with the shortcut's link; `Error` with the reason in Note
   (usually: no access to the file). A later session reads errors from the Sheet and tells Aurélien.

Never copies, moves or deletes; it only creates shortcuts and missing folders on the target path.
