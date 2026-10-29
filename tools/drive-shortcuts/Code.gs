/**
 * Drive shortcut queue — work Drive (ac@unifyapps.com).
 *
 * Bound to the Google Sheet "Drive shortcut queue" (05_Internal). Agents append a row
 * (File link, Target folder, optional Shortcut name); every 5 minutes this script creates
 * the shortcut in the target folder and writes Status, Shortcut link and Note back.
 * It never copies, moves or deletes a file. Install: see README.md.
 */

// 01_Accounts in the work Drive (docs/drive-map.md).
const ACCOUNTS_FOLDER_ID = '1UTVePwayZoWWdqeNxBuJXB1oRgMSBWrq';
const COL = { link: 1, target: 2, name: 3, status: 4, shortcut: 5, note: 6 }; // 0-based

/** Run once by hand: authorises the script and installs the 5-minute trigger. */
function setup() {
  ScriptApp.getProjectTriggers()
    .filter(t => t.getHandlerFunction() === 'processQueue')
    .forEach(t => ScriptApp.deleteTrigger(t));
  ScriptApp.newTrigger('processQueue').timeBased().everyMinutes(5).create();
  processQueue();
}

/** Creates a shortcut for every row that has a link and no status yet. */
function processQueue() {
  const sheet = SpreadsheetApp.getActive().getSheets()[0];
  const rows = sheet.getDataRange().getValues();
  for (let r = 1; r < rows.length; r++) {
    const row = rows[r];
    if (!row[COL.link] || row[COL.status]) continue;
    let result;
    try {
      result = createShortcut_(String(row[COL.link]), String(row[COL.target] || ''), String(row[COL.name] || ''));
    } catch (e) {
      result = ['Error', '', String(e && e.message || e)];
    }
    sheet.getRange(r + 1, COL.status + 1, 1, 3).setValues([result]);
  }
}

function createShortcut_(link, target, name) {
  const targetId = extractId_(link);
  if (!targetId) throw new Error('No Drive file id in the link');
  const folder = resolveFolder_(target);

  // Already there? Don't add a second shortcut.
  const existing = folder.getFilesByType(MimeType.SHORTCUT);
  while (existing.hasNext()) {
    const f = existing.next();
    if (f.getTargetId() === targetId) return ['Exists', f.getUrl(), folder.getName()];
  }

  const shortcut = DriveApp.createShortcut(targetId);
  shortcut.moveTo(folder);
  if (name) shortcut.setName(name);
  return ['Done', shortcut.getUrl(), folder.getName() + ' · ' + new Date().toISOString().slice(0, 16)];
}

/** File id from a Drive / Docs / Sheets / Slides URL, or a bare id. */
function extractId_(link) {
  const m = link.match(/\/d\/([A-Za-z0-9_-]{20,})/) || link.match(/[?&]id=([A-Za-z0-9_-]{20,})/) ||
            link.match(/\/folders\/([A-Za-z0-9_-]{20,})/) || link.match(/^([A-Za-z0-9_-]{20,})$/);
  return m ? m[1] : '';
}

/**
 * Target: a folder link or id, or a path under 01_Accounts like "GeBBS" or "GeBBS/Shared decks".
 * Missing folders on the path are created (never renamed or deleted). Empty: 01_Accounts itself.
 */
function resolveFolder_(target) {
  target = target.trim();
  const id = extractId_(target);
  if (id && (target.includes('drive.google.com') || !target.includes('/'))) {
    try { return DriveApp.getFolderById(id); } catch (e) { /* not an id: treat as a path */ }
  }
  let folder = DriveApp.getFolderById(ACCOUNTS_FOLDER_ID);
  target.split('/').map(s => s.trim()).filter(Boolean).forEach(part => {
    const it = folder.getFoldersByName(part);
    folder = it.hasNext() ? it.next() : folder.createFolder(part);
  });
  return folder;
}
