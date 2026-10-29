---
name: cloud-env-preflight
description: Check, in one pass, that a cloud session's environment has everything a project needs — variables (set, right type, right project), allowed hosts, network secrets, tools — and give Aurélien one consolidated list of settings to fix before he starts a new session. Use at the start of any app session in a new or changed environment, when a script fails with 401, a missing variable or a blocked host, before a handoff to a new environment, and when Aurélien asks "qu'est-ce qu'il me reste à régler ?".
---

# cloud-env-preflight

Environment variables and allowed hosts are read when a session **starts**: every fix discovered one at a time costs
Aurélien a settings round-trip and a new session. Find everything at once, ask once.
Script: `scripts/preflight.py` (never prints a value; only set/missing, length, type and project match).

## 1. The manifest (once per project)
`docs/environment.json` in the project repo lists what a session needs (format in the script's header):
- **variables**: name, `public` or `secret`, what it's for, where Aurélien sets it, optional `prefix` (key type, e.g.
  `sb_secret_` vs `sb_publishable_`) and `match` (the project's own URL);
- **forbidden**: variables that must not be in this environment (another project's keys, a service-role key the
  session doesn't need);
- **hosts**: URLs the session must reach, with the expected status (a 401 can be "reachable");
- **tools**: binaries the scripts need.

No manifest yet → `python3 <brain>/skills/cloud-env-preflight/scripts/preflight.py scan .` lists the variable names
and hosts the code refers to; draft the manifest from it with Aurélien's project in mind, commit it.

## 2. Naming rule
Every variable a session uses is **prefixed by the project** (`BASECAMP_SUPABASE_URL`, `ELEMENT_API_TOKEN`), and the
scripts refuse any other project (check the URL's project ref). Two apps once shared `SUPABASE_*` names in one
environment and a script aimed at the wrong database. Production secrets used by the app itself stay in Cloudflare /
Supabase, not in the session.

## 3. Check
```bash
python3 <brain>/skills/cloud-env-preflight/scripts/preflight.py check docs/environment.json
```
Then give Aurélien **one** block, in French, numbered, with for each item: the screen (environment settings ›
variables / network › allowed hosts / network secrets; Cloudflare › Pages › Settings › Variables and secrets;
Supabase › Project Settings › API Keys), the exact name, which kind of value (publishable or secret, never the value
itself), and why. End with: "ensuite ouvre une nouvelle session sur cet environnement et dis-moi « preflight »".

## Known traps
| Symptom | Cause |
|---|---|
| `Tunnel connection failed` / 403 from the proxy | host not in the environment's allowed hosts |
| 401 from Supabase with a key that "is set" | publishable key in a secret slot, or the other project's key |
| A fixed variable still missing | the session started before the change: new session |
| `*.pages.dev` unreachable | preview domains are often not allowed: test the custom domain instead |
| `/api/health` = 200 | only proves the variables exist on Cloudflare, not that each key works: call one real read |
| A plugin or tool gone after restart | containers are fresh: install it in the setup script or the repo's SessionStart hook |

## Rules
- Never ask Aurélien to paste a key, token or OAuth callback URL (it carries tokens) into the chat; ask what he sees
  on the settings screen instead (names, key type, last characters at most).
- Never print a variable's value, even partly, in the chat or a log.
- Writes to a production database still need his explicit OK, even when the environment allows them.
- Record the manifest's variable names (not values) in the config guide's Deploy chapter (`config-guide`).
