---
name: demo-prep
description: Prepare a UnifyApps pre-sales demo end to end — read the opportunity in the Notion CRM, propose the approach and get Aurélien's OK before building, build on the platform with the team plugin, then the demo script and run sheet, the demo video, the configuration guide, an optional single-file site for Vercel, and the write-back to the opportunity page. Use when Aurélien prepares a demo, a POC walkthrough or a solution presentation for a client ("prépare la démo pour X", "build the demo for the call on Friday", "on refait la démo avec le feedback de Y"), and when feedback on a demo comes back.
---

# demo-prep

Chains what already exists; it doesn't replace it. The **team plugin** (`unifyapps`, installed separately) does the
platform work; this skill is Aurélien's own way of running a demo from brief to write-back. Runs in a **local session
on the work Mac**, in the account's folder; outputs go to the work Drive (`01_Accounts/<Account>`, `docs/drive-map.md`), context to Notion. Never in a cloud session,
never pushed to `ac-ua/*` or to `Unifyapps-Internal/*` (the team repo only takes platform learnings, through its loop).

## 1. Brief (from Notion, not from memory)
Read the opportunity page brief (`work-notes` keeps it current): client, problem, people and their stance, what was
already shown, open questions, the date and audience of the call, what the AE asked for. Ask once for what's missing:
call date, audience (exec / technical / end users), duration, must-show moments, environment (Orbit UAT, which
workspace), the customer tag for assets.

## 2. Approach first, then build
Write the approach in one screen and **wait for Aurélien's OK before building** (he has had to ask for this several
times):
- the story in 3–5 moments (the "aha" first), the data it uses, what is real vs mocked;
- the build list: objects, workflows, agents, config apps, context graph, connections (team plugin:
  `unifyapps-solution-playbook` for past builds, `unifyapps-usecase-studio` for the plan, `unifyapps-builder` /
  `unifyapps-config-apps` / `unifyapps-context-graph` to build);
- reuse: what exists in the environment already (native settings over custom screens, the platform's own governance);
- risks and what needs his input.
Colour and label conventions in diagrams: say what each colour means; "live in production" only for what is live.

## 3. Build
With the team plugin, in the test workspace first; every asset carries the customer tag. Production or shared
environments: **only on Aurélien's explicit go** in this request. Keep a running list of what was built (names,
links) for the guide. Data the platform needs is fetched by the platform, not pasted by Claude.

## 4. Demo pack
| Piece | How |
|---|---|
| Demo script + run sheet | timed beats (what to click, what to say, fallback if it breaks); presenter's version and a one-page run sheet |
| Demo video | team plugin `demo-studio` (real click-through, stock voice; English unless asked). Over 29 MB → also a compressed copy |
| Explainer of what changed | `explainer-video` (slides or document mode with pointer), when Aurélien wants to understand or share the change |
| Configuration guide | team plugin `unifyapps-config-guide`; **one guide artifact per build**, updated in place |
| Deck | `case-for-change` for the story, the team plugin `unifyapps-brand-deck` for the slides |
| Single-file site (optional) | one self-contained `index.html` (inline CSS/JS/images) for Vercel drag-and-drop; **always say the full path** of the file and of the folder to drop |

## 5. Feedback round (vN → vN+1)
When comments come back (client, AE, colleague, Aurélien): list each comment → change → where it was applied, show
the plan if a comment changes the approach, rebuild, bump the version in the guide and the pack, and give a short
"what changed" (text, or an explainer if asked). "Corrige mais ne régénère pas la vidéo" → fix sources only.

## 6. Write-back (before the session ends)
`work-notes`: the brief's Solution and Assets sections (links to the guide, video, deck, site, Drive folder), a
meeting-log entry for the demo, next steps, learnings → Memories (Domain Work). Platform learnings worth sharing with
the team → the team plugin's weekly learnings loop, nothing else.

## Rules
- Never Aurélien's cloned voice for anything pro.
- Demo-environment logins stay where he wrote them on the CRM pages; never copied into scripts, videos or decks.
- Show before building, show before shipping; never delete a client asset without asking.
