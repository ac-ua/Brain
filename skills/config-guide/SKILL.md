---
name: config-guide
description: Keep a personal project's configuration guide current — a build ledger (JSON record of every feature, screen, data store, deploy piece, decision and open item) and a plain-language HTML guide generated from it. Use at project kickoff, after every release or material change, before handing a project to another session or person, and when Aurélien says "update the guide" or "how is X put together".
---

# config-guide

Personal version of the configuration-guide pattern, modelled on Element Logbook (`ac-ua/c_ET`: `docs/build-ledger.json`,
`docs/config-guide/`). The idea: the guide isn't written from memory at the end. Every change is recorded in the
**ledger** as it happens, and the guide is refreshed from it, so it stays complete by construction.

```
<project>/docs/
  build-ledger.json          ← every change appends here (scripts/ledger.py)
  config-guide/
    guide.html               ← the guide (from assets/guide-template.html)
    img/NN-name.jpg          ← real screenshots
```

## 1. Kickoff
```bash
L="python3 <brain>/skills/config-guide/scripts/ledger.py --ledger docs/build-ledger.json"
$L init --project "<Name>" --tag <TAG> --owner "Aurélien" --use-case "<what it solves>" --use-case "…"
cp <brain>/skills/config-guide/assets/guide-template.html docs/config-guide/guide.html
```
Fill chapter 1 (what it is, who for, the problems) right away.

## 2. During the build: record as you go
```bash
$L add --kind feature --id offline --name "Offline mode" --purpose "log a session without network" --status live
$L add --kind screen  --id today   --name "Today" --purpose "the day's workout with your weights"
$L add --kind data    --id logs    --name "Session logs" --purpose "one row per logged session" --where "Supabase: public.logs"
$L add --kind deploy  --id pages   --name "Cloudflare Pages" --purpose "static front + /api functions"
$L decide --what "Levels are variations of one exercise" --why "one history per movement"
$L open-item --what "Strava not connected" --kind choice --owner Aurélien
$L change --summary "v1.3: coach programming"
```
Kinds: `feature screen data backup deploy integration secret-ref metric artifact other`. `secret-ref` records
*where* a secret lives (e.g. "Cloudflare env RESEND_KEY"), never its value.

## 3. Refresh the guide (after each release)
`$L check --guide docs/config-guide/guide.html` lists ledger assets the guide doesn't mention yet. Update the
chapters, bump the guide version in the ledger (`$L guide --version vN --url <artifact url>`), add a line to the
"What changed" chapter. If the guide is published as an artifact, republish from the repo file.

## Chapters (personal builds)
1. **What it is** — the project from zero: who it's for, the problems it solves.
2. **Features** — each feature: what it does, how to use it, its status (live / sample / not finished).
3. **Screens** — one section per screen, with a real screenshot.
4. **Data & backups** — every store and record type, where it lives, how it's backed up and restored.
5. **Deploy** — hosting, environments, release steps, where each secret lives (names only), free-tier limits.
6. **Decisions & open items** — from the ledger.
7. **What changed** — guide revisions.

## Rules
- Plain language; no working notes in the guide. Honest labels: live, sample data, not finished.
- No secrets, no client names. Screenshots from the real app, with no personal data of other people.
