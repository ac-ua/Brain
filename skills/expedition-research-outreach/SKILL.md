---
name: expedition-research-outreach
description: >
  Automated research-partnership outreach pipeline for Aurélien Caye's South Pole
  2027 solo expedition. Triggers when the user asks to "run the research skill",
  "process the next lab", "do the science outreach", "contacte le prochain labo",
  or any equivalent. Also triggers when a specific lab or researcher is named as a
  target. The skill reads the "Idee recherche" Notion page, picks the next contact
  using the 2-1-1 axis rotation, then runs the full pipeline: lab research, contact
  discovery, email draft creation in Gmail, and Notion database update with
  Type = "Science". Fully autonomous end-to-end. One contact per run.
---

# Expedition Research Outreach Skill

Autonomous end-to-end science outreach: Notion queue → research → Gmail draft → Notion update.
Same structure as the sponsor skill, adapted for research partnerships. One contact per run.

## On every run, load first

Read `references/science-context.md`. It contains the expedition brief, the three
research axes with their light protocols, the tone rules, the email patterns, and the
seed contacts. It is the single source of truth for the run. Do not proceed without it.

Key mindset difference from the sponsor skill: this is NOT a sponsorship ask. Aurélien
OFFERS rare access and data and seeks a scientific collaboration plus credibility. Never
lead with money and never ask the lab to pay.

---

## STEP 0 — Pick the target from the "Idee recherche" page

### 0a — Read the queue page

Fetch this Notion page: https://app.notion.com/p/3a419ca7989380c58078d01c44481dcd

The page is organised into three sections, each a checklist of contacts:
- "Axe 1 — Environnement (prélèvements de neige)"
- "Axe 2 — Corps humain (physiologie, nutrition, froid)"
- "Axe 3 — Isolement / analogue spatial"

An unchecked item (`- [ ]`) is still to contact. A checked item (`- [x]` / ✅) is done.

**If the page is blank or has no axis sections yet**, build the structure first: create the
three axis headings with checklists, seeded from the "Seed contacts" in science-context.md,
plus a short legend at the top explaining the rotation. Then continue.

### 0b — Determine which axis is next (2-1-1 rotation)

Count the total number of checked ✅ items across all three axes = N.
Position in the cycle = N mod 4:
- position 0 → Axe 1
- position 1 → Axe 1
- position 2 → Axe 2
- position 3 → Axe 3

This reproduces the intended cadence: two from Axe 1, then one from Axe 2, then one from
Axe 3, then repeat. Within the designated axis, the target is the first unchecked item.

### 0c — If the designated axis has no unchecked contact

Research 1 to 3 new labs or researchers relevant to that axis (use the axis fit notes in
science-context.md, gaps you notice, recent publications). Cross-reference each against the
Sponso database collection://2ae19ca7-9893-80d6-b263-000b7171b431 to confirm no existing
page. Append them to the bottom of that axis's list on the queue page (append only, never
overwrite), then pick the first one you just added.

If new candidates are genuinely impossible to find for that axis right now, move to the next
axis in the cycle for this run and note briefly on the page why.

### 0d — Mark the chosen contact immediately

Before any web search or email writing, update the queue page to check the chosen item
(`- [x]` / ✅). This prevents a parallel run from picking the same target.

### 0e — Check the database for an existing page

Search the Sponso database for a page matching the chosen lab/researcher name. If one exists,
fetch it to read prior research and avoid duplication. If none exists, create one with
Marque = contact/lab name, Status = "Not Started", Type = "Science", then proceed.

---

## STEP 1 — Lab / researcher research

Run a minimum of 4 web searches:

1. The lab or researcher's current work, recent publications, and exact research focus
2. Whether they have already worked with expeditions, explorers, or field-collected samples
3. The specific method or programme that matches the axis (e.g. snow-impurity sampling,
   expedition calorimetry, ICE/space-analog protocols)
4. The researcher's current affiliation and home-market language (to confirm they are still
   there and which language to write in)

Write a Fit Summary of 4 to 6 bullet points covering:
- The lead angle for this specific lab (which axis, which method)
- One specific proof point to reference in the email (a named study, a programme, a recent
  paper, a stated research question) that is real and verifiable
- The precise light protocol Aurélien can offer this lab (from science-context.md)
- Anything to avoid

---

## STEP 2 — Contact discovery and verification

Goal: one primary contact who is the right person to evaluate the collaboration.

Priority order for role:
1. The principal investigator / team lead whose work matches the axis
2. A named researcher on the relevant recent paper
3. The lab's research-partnerships or scientific-collaboration contact
4. A generic lab or department inbox as last resort

Research process:
1. Search "[Lab] [researcher] site:linkedin.com" and the lab's own site
2. Search "[researcher name] email [institution]" and check recent papers for a corresponding
   author address (academic emails are often public in publications)
3. Confirm the researcher's current role: "[researcher] [institution] [current year]"
4. Check the seed patterns in science-context.md

Document up to 3 contacts, ranked:
- Primary: best-matched decision-maker
- Secondary: next best if no reply after 2 to 3 weeks
- Tertiary (if relevant): generic inbox or alternative route

For each contact output: full name and title, email (found or pattern-inferred), confidence
(High / Medium / Low), and LinkedIn URL if found. The Gmail draft is created for the primary
only. Note next to any uncertain email: "À vérifier sur Hunter.io ou Snov.io avant envoi."

---

## STEP 3 — Write the outreach email

### Language rule
French for French or francophone targets. English for other international targets.
Never mix languages in one email.

### Subject line
Short, specific, human. Lab or field + expedition angle. Not clickbait, not generic.
Examples of the register:
- "Antarctique : des prélèvements de neige le long d'un transacte inédit"
- "South Pole transect: snow samples for your microplastics work"
- "Un sujet solo pour vos protocoles d'expédition"
- "Solo Antarctic crossing: a data point for INSPIRE-type work"

### Email structure (follow strictly)

**Paragraph 1 — Specific hook**
One sentence tying the lab's real, named work to the expedition. Not a compliment. A factual
observation that shows homework was done (a named study, a programme, a research question the
lab has published on).

**Paragraph 2 — The expedition**
Two to three sentences, facts only: solo, unsupported, unassisted, Berkner Island to South
Pole, about 1,350 km, roughly 60 days, alone, November 2027, satellite-only connectivity.

**Paragraph 3 — What Aurélien can bring (the light protocol)**
Two to three sentences, concrete and specific to this lab's method: the exact light protocol
from science-context.md (snow bottles at GPS points / passive watch data + pre-post lab
measures / structured daily self-report). State plainly that it stays compatible with a solo
unsupported expedition and adds no heavy gear or daily hours. Make clear he is offering to
help their research, not asking them to fund him.

**Closing**
Two lines, using the standard closing from science-context.md (short call + one pager offer).

### Tone rules (strict)
- No word "sponsor", "sponsorship", "parrainage"
- No "—" character anywhere in the email body
- No bullet points or dashes inside the email body
- No AI-sounding phrasing, no superlatives
- Max ~180 words
- No attachment. Link to aureliencaye.com
- No signature
- Never lead with money or ask the lab to pay

---

## STEP 4 — Create Gmail draft

Use the Gmail MCP to create a draft:
- To: primary contact email
- Subject: subject line from Step 3
- Body: cold email body from Step 3, no signature

After creating the draft, label it "science": call `list_labels` to find the ID of the
"science" label (create the label in Gmail first if it doesn't exist yet), then call
`label_message` with the draft's message ID and that label ID. This keeps science-track
drafts easy to filter separately from sponsor outreach.

Do not send. Draft only. If Gmail is unavailable, output the full email in chat and note it.

---

## STEP 5 — Update the Notion database page

Open the contact's Sponso page. Append content at the bottom only. NEVER delete or overwrite
anything already there.

**If the page had no prior research content:**
Write "Pourquoi ce labo est pertinent" first (Fit Summary as flowing prose, no dashes), then
"Contacts identifiés" (primary with all details, plus alternatives if confidence is Medium or
Low, plus "À vérifier sur Hunter.io ou Snov.io avant envoi" where applicable).

**Always append at the bottom, regardless:**
Leave three blank lines before the entry, then a clear header. Format exactly:

---

🟢 OUTREACH SCIENCE — Draft créé le [DD/MM/YY]
Axe : [1 Environnement / 2 Corps humain / 3 Isolement]
Contact : [Name, Title] — [email used]
Objet : [subject line]
Apport proposé : [one sentence on the light protocol offered]

[full cold email body]

**If the only contact point is a form (no direct email found):**
Do not create a Gmail draft. Append at the very bottom:
⚠️ PAS D'EMAIL DIRECT — Ce contact n'est joignable que via formulaire : [URL]

**Then update the Notion page properties:**
- Status → "Drafted"
- Type → include "Science"
- Contact → primary contact email
- Dernier Contact → today's date

---

## Hard rules

Never delete any content from a Notion page.
Never send any email. Draft only.
Never use "—" anywhere in any email body.
Never lead with a financial ask or ask a lab to pay.
Never use the word "sponsor" or "sponsorship".
Never exceed the light-protocol boundary in science-context.md (no heavy gear, no daily
protocols that eat into skiing hours, nothing that could jeopardise the expedition).
Never process a contact whose queue item is already checked ✅.
One contact per run, chosen by the 2-1-1 axis rotation in Step 0.
Always tag the database entry Type = "Science".
Always label the Gmail draft "science".

---

## Edge cases

**Researcher still at the institution is uncertain:** note it in the Notion log, list
alternative emails, still create the Gmail draft with the best guess.

**Contact page has existing research but no outreach yet:** skip rewriting research sections,
use what is there to write the email, add only the log entry at the bottom.

**An axis is exhausted:** run Step 0c to research and append 1 to 3 new labs to that axis,
then run the full pipeline on the one you pick. If impossible, move to the next axis in the
cycle and note why.

**No Gmail connection:** output the full draft in chat with the subject labeled, still update
Notion with all content and today's date.

**Notion write needs approval and none is given:** output the full page update and the email
draft in chat so nothing is lost, and note what still needs to be applied.

