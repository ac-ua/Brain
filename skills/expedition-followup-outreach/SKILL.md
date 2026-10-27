---
name: expedition-followup-outreach
description: "Automated follow-up pipeline for Aurélien Caye's South Pole 2026 expedition outreach, covering both brand sponsorship AND research/science partnerships (same Notion database, distinguished by the \"Type\" property). Triggers when the user asks to \"run the follow-up skill\", \"do the follow-ups\", \"check who needs a follow-up\", or any equivalent phrasing. The skill scans the Notion database for entries with status \"Contacté\" or \"relancé\" whose last contact date is 15+ days ago, then creates Gmail draft replies in the correct threads and drafts new emails to secondary contacts, using the tone and rules that match each entry's Type. Updates Notion with full traceability. Never sends emails, only creates drafts."
---

# Expedition Follow-up Outreach Skill

Scans Notion for overdue contacts, creates Gmail draft replies in existing threads,
drafts new emails to secondary contacts, and updates Notion with full traceability.
Covers both brand/sponsor entries and research/science entries from the same database.

## On every run, load the right context — branch by Type

This database mixes two kinds of entries: brand partnerships (Type = Coprorate,
Equipment, Media & Others, Agence) and research partnerships (Type = Science).
They use different value exchanges and must never be written with the same tone.

For the brand/sponsor track, read `references/expedition-context.md`.
For the research/science track, read `references/science-context.md`.

Do not decide which one to load until Step 0 has identified the Type of the
specific entry being processed this run. Never blend the two: a Science entry
must never be written using sponsorship tiers or a financial ask, and a brand
entry must never be written using the "light protocol" research framing.

---

## STEP 0 — Identify entries that need follow-up

Search the Notion database collection://2ae19ca7-9893-80d6-b263-000b7171b431.

Run two searches: one for status "Contacté", one for status "relancé".

For each result, check the "Dernier Contact" date. Keep only entries where
Dernier Contact is 15 or more days before today.

For each eligible entry, note its "Type" property before doing anything else —
this determines which context file and tone rules apply for the rest of the run
(see branch above). If Type includes "Science", this is a research entry: follow
the "Research entries" notes throughout this skill wherever they differ from the
default (brand) instructions below.

Fetch its full Notion page to understand:
- How many contacts have been reached so far and who they are
- How many times each contact has been emailed (max 3 total per contact,
  meaning original + 2 follow-ups)
- How many distinct people have been contacted for this brand (max 5 total)
- What follow-up actions are already logged
- Whether any reply was received (if so, skip — no follow-up needed)

Build a prioritized list of brands to process, ordered by how long overdue
they are (most overdue first). Process one brand per run.

---

## STEP 1 — Determine what actions to take

For the chosen brand, map out the full contact history from the Notion page,
then decide which actions to create drafts for today. The logic:

**For the primary contact (the person originally emailed):**
- If they have received fewer than 3 emails total (original + follow-ups),
  create a reply draft in their existing Gmail thread.
- If they have already received 3 emails, do not contact them again.

**For secondary and tertiary contacts already documented in Notion:**
- If they have received fewer than 3 emails total, create a new email draft.
- If not yet contacted, this is their first email — treat it like a cold email
  using the same structure as the outreach skill.
- If already contacted once, create a reply in their thread.

**For contacts not yet in Notion:**
- If the brand has fewer than 5 distinct people contacted total, search for
  additional contacts online (LinkedIn, web search, company website).
- Document them in Notion under "Contacts identifiés" before drafting.

**Stop condition:**
If the brand has reached 5 distinct contacts all with 3 emails each (15 emails
total), mark status as "Ghost" and stop. Do not create any drafts.

**Research entries (Type = Science):** the same 3-email / 5-contact caps and the
same reply-vs-new-email logic apply. The only difference is who the additional
contacts are: for a lab, look for co-authors on the relevant paper, a lab
research-partnerships contact, or a PhD/postdoc working the same axis, rather
than a secondary brand contact like a marketing manager.

---

## STEP 2 — Find the Gmail threads

For each contact who needs a follow-up reply, search Gmail for the original
thread using:
- Sender or recipient email address
- Brand name in subject line
- Date range matching when the original was sent

Retrieve the thread ID. The draft reply must be created in that thread
(using replyToMessageId), not as a new email.

For new contacts being reached for the first time, no thread search is needed —
create a new email draft.

---

## STEP 3 — Write the follow-up emails

### For reply follow-ups (existing thread, same contact)

Language: match the original email language.

Structure:
- One sentence acknowledging the silence without being passive-aggressive.
  Do not say "I just wanted to follow up" or "Je me permets de relancer".
  Find a concrete reason to write: a new piece of information, a recent
  development about the brand, a content angle not mentioned before, or
  a timing argument (expedition departure approaching).
- One sentence restating the core ask briefly.
- CTA: "Would you be open to a quick call?" or French equivalent.

Max 80 words. No "—" anywhere. No bullet points. No signature.

Good patterns from past follow-ups:
- Reference something that happened recently at the brand (new product,
  campaign, news) that makes the timing feel relevant now.
- Reference the expedition timeline: "Avec un départ en novembre, je commence
  à finaliser mes partenariats clés."
- For English: "Wanted to resurface this as I'm locking in key partnerships
  ahead of my November departure."

**Research entries (Type = Science):** same structure and word count, but the
"concrete reason to write" and the "core ask" must come from science-context.md,
never from the brand patterns above. Good reasons to resurface: a new relevant
publication from the lab, a refinement of the light protocol offered, or the
November departure as a natural deadline for finalising which samples/measures
to include. Never reference "partenariats clés" in a commercial sense; frame it
as finalising the season's research collaborations.

### For new contact emails (first outreach to a secondary or tertiary contact)

Follow exactly the same structure as the outreach skill (cold email format):
- Personalized hook referencing something specific about the brand
- Expedition facts + why relevant to this brand
- Collaboration idea concrete and specific
- Two-line closing: "I'd love to explore whether there's an opportunity to
  collaborate. Would you be open to a quick call to see if there's a fit?
  I can also send you a one pager with more details."

No "—" anywhere. No bullet points. No signature. Max 180 words.

**Research entries (Type = Science):** use the cold-email structure from
`expedition-research-outreach`'s SKILL.md Step 3 instead (hook tied to the lab's
published work, expedition facts, the specific light protocol offered, then the
science closing line from science-context.md). Never use the brand "collaboration
idea" framing and never the brand closing line above; offering access/data is the
ask, not a partnership deal.

### Tone rules for all emails
- No "sponsorship", "sponsor", "parrainage"
- No "—" anywhere
- No bullet points or dashes
- No AI-sounding phrasing
- No signature
- Research entries only: never lead with or imply a financial ask; Aurélien is
  the one offering access and data, not requesting funding

---

## STEP 4 — Create Gmail drafts

For reply follow-ups: use replyToMessageId to place the draft in the correct thread.
For new contact emails: create as a new draft with the contact's email as recipient.

Never send. Draft only.

If a thread cannot be found in Gmail, create a new draft and note in Notion
that the thread was not found and the draft should be manually placed in reply.

---

## STEP 5 — Update Notion

Append to the brand's Notion page. Never delete or overwrite existing content.

For each new contact discovered and added, append under "Contacts identifiés":
- Name, title, email, confidence level, LinkedIn URL
- "À vérifier sur Hunter.io ou Snov.io avant envoi" if confidence is not High

For each draft created, leave three blank lines before the entry, then append a clearly labeled log block.

For brand entries (Type ≠ Science):

---

🔁 FOLLOW-UP — Relance créée le [DD/MM/YY]
Contact : [Name, Title] — [email]
Type : Reply dans thread existant / Nouvel email (premier contact) / Nouvel email (Xe contact)
Objet : [subject line]
Action : [one sentence on what angle was used in this follow-up]

[full email body]

For research entries (Type = Science), use the same shape but the science-track tag,
and name the axis so the log stays consistent with the original 🟢 OUTREACH SCIENCE entry:

---

🔁 FOLLOW-UP SCIENCE — Relance créée le [DD/MM/YY]
Axe : [1 Environnement / 2 Corps humain / 3 Isolement]
Contact : [Name, Title] — [email]
Type : Reply dans thread existant / Nouvel email (premier contact) / Nouvel email (Xe contact)
Objet : [subject line]
Action : [one sentence on what angle was used in this follow-up]

[full email body]

Then update Notion page properties:
- Status → "Followup Drafted"
- Dernier Contact → today's date (this tracks when the last action was taken,
  even if not yet sent — update again when actually sent if possible)
- Type property is left untouched (already set to Science from the original run)

---

## Ghost condition

If after checking the full contact history the brand has reached the maximum
(5 distinct contacts, each emailed 3 times), or if all remaining contacts
have already hit their 3-email limit:
- Update Status → "Ghost"
- Leave three blank lines then append:

---

👻 GHOST — [DD/MM/YY]
[X] contacts atteints, aucune réponse. Dossier clos.
- Do not create any drafts.

---

## Hard rules

Never delete any content from a Notion page.
Never send any email. Draft only.
Never use "—" anywhere in any email body.
Never use bullet points or dashes inside email bodies.
No signature in any email.
Reply follow-ups must be placed in the existing thread using replyToMessageId.
New contact emails must be new threads.
Max 3 emails per contact (original + 2 follow-ups).
Max 5 distinct contacts per brand.
Process one entry per run — the most overdue one, across brand and research entries combined.
Always check the Type property before writing anything. Science entries always use
science-context.md and the research tone/closing; never the brand tone, tiers, or
financial framing. Never blend the two contexts in a single email.
