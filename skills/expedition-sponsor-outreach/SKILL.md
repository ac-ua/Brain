---
name: expedition-sponsor-outreach
description: >
  Automated sponsorship outreach pipeline for Aurélien Caye's South Pole 2027 
  solo expedition. Triggers automatically when the user asks to "run the skill", 
  "process the next sponsor", "do the outreach", or any equivalent. Also triggers 
  when a specific brand is named as a target. The skill reads the Notion sponsor 
  database, picks the highest-priority untouched brand (status = "Not Started"), 
  runs the full pipeline: brand research, contact discovery, email draft creation 
  in Gmail, and Notion page update. Fully autonomous end-to-end.
---

# Expedition Sponsor Outreach Skill

Autonomous end-to-end outreach pipeline: Notion → research → Gmail draft → Notion update.

## On every run, load first

Read `references/expedition-context.md`. It contains Aurélien's expedition brief,
tone rules, email patterns, confirmed partners, and known contacts. It is the
single source of truth for the entire run. Do not proceed without reading it.

---

## STEP 0 — Pick the target from the prioritization page

### 0a — Read the prioritization page

Fetch this Notion page: https://app.notion.com/p/37319ca79893804fbd90c46c840c92f4

Read everything ABOVE the "📋 Sponsors déjà dans la base de données → ne pas contacter"
divider. This includes all brainstorm/priority sections above it (e.g. "Marques de
stylos de luxe", "A contacter (en vrac)", "Boite a idee", or any new section added
above the divider later).

Select the first company in that area that does NOT already have a ✅ in front
of its name. That is the target for this run.

If every item above the divider already has a ✅, move to Step 0b.

### 0b — If the list above the divider is exhausted

Everything below "📋 Sponsors déjà dans la base de données → ne pas contacter" is
already contacted and permanently off-limits for new outreach, regardless of its
status. Never pick a target from that section and never treat it as a source of
new candidates, even if a brand listed there has no dedicated Notion page.

Instead, identify 1 to 3 new brand candidates yourself, based on the expedition's
fit (categories and strategic notes in expedition-context.md, gaps you notice,
recent market news). Cross-reference each candidate against the sponsor database
collection://2ae19ca7-9893-80d6-b263-000b7171b431 to confirm it has no existing
page. Write the new candidate(s) into the "A contacter (en vrac)" list above the
divider (append only, never overwrite existing entries), then pick the best one
from what you just added as this run's target.

### 0c — Mark the chosen company immediately

Before doing anything else — before any web search, before any email writing —
update the prioritization page to add ✅ in front of the chosen company name.
This prevents another parallel Claude session from picking the same target.

### 0d — Check the sponsor database for an existing page

Search the sponsor database for a page matching the chosen company name.
If a page already exists, fetch it to read any prior research, contacts, or notes.
Do not duplicate content already written there.
If no page exists, create one with Status = "Not Started" and the appropriate Type,
then proceed.

---

## STEP 1 — Brand research

Run a minimum of 4 web searches:

1. Brand positioning, tagline, core values, recent campaigns
2. Explorer, endurance athlete, or expedition sponsorships and ambassadors
3. RSE / CSR / sustainability programs (relevant for Corporate targets)
4. Specific products relevant to the expedition, and primary language of their home market

Write a Brand Fit Summary of 4 to 6 bullet points covering:
- The lead angle (product validation / content / RSE / other)
- One specific proof point to reference in the email (a product name, a quote
  from a leader, a known ambassador, a recent campaign — something real and verifiable)
- Things to avoid mentioning
- Recommended tier (Supply Partner / Bronze / Silver / Gold / Title)

---

## STEP 2 — Contact discovery and verification

Goal: one primary contact who is the right decision-maker.

Priority order for role:
1. Head or Director of Partnerships or Sponsorship
2. Sports Marketing Manager or Brand Ambassador Manager
3. Head of Marketing or CMO (smaller brands)
4. RSE or CSR Manager (Corporate targets)
5. Generic partnerships or press inbox as last resort

Research process:
1. Search "[Brand] director partnerships sponsorship site:linkedin.com"
2. Search "[Brand] sports marketing manager explorer ambassador"
3. Search "[Brand] press contact partnership email"
4. Check known patterns in expedition-context.md
5. Search "[Contact Name] [Brand] [current year]" to confirm they still work there

Identify and document up to 3 contacts in total, ranked by relevance:

- Primary contact: the best decision-maker for this type of outreach
- Secondary contact: next best option if the primary does not respond after 2 to 3 weeks
- Tertiary contact (if relevant): a generic inbox, a CEO, or an alternative route

For each contact, output:
- Full name and title if found
- Email address constructed from known pattern or found directly
- Confidence: High (verified pattern + confirmed current role) /
  Medium (pattern inferred, role unconfirmed) / Low (generic inbox)
- LinkedIn URL if found

The Gmail draft is always created for the primary contact only.
Secondary and tertiary contacts are documented in Notion for manual use if needed.
Note clearly in Notion next to any uncertain email: "À vérifier sur Hunter.io ou Snov.io avant envoi."

---

## STEP 3 — Write the cold email

### Language rule
French if the brand's primary market is France or French-speaking.
English for all others. Never mix languages in one email.

### Subject line
Short, specific, and punchy. Study the patterns from past sent emails and match
the energy — not clickbait, not generic. Examples of what works:
- "South Pole expedition fueled by Chomps"
- "BLUETTI x South Pole: The Ultimate Off-Grid Power Test"
- "FindPenguins in Antarctica?"
- "Polarstep x South Pole"
- "MasterCard au Pole Sud: Priceless"
- "L'Oréal au Pole Sud"
- "Pebbls at South Pole?"

The subject should feel like it was written in 10 seconds by someone who knows
exactly why they're writing. Brand name + expedition angle + nothing more.

### Email structure (follow strictly)

**Paragraph 1 — Personalized hook**
One sentence that creates a direct, specific bridge between something real about
the brand and the expedition. This is not a compliment. It is a factual observation
that makes the reader think "this person did their homework."

Good examples from past emails:
- "I noticed Chomps became the official protein partner of Ikon Pass. I'm taking
  that ski + fuel story a little further south."
- "I specifically noted Illia Zahnitko's words at CES 2026: 'Meeting
  extreme-environment needs is central to our mission.'"
- "Je me permets de vous écrire car je prépare une expédition qui me semble en
  résonance directe avec l'univers d'American Express."

Never open with "I wanted to reach out", "Je me permets de vous contacter car",
or any other filler phrase. If you cannot find a specific hook, use the expedition
angle directly.

**Paragraph 2 — The expedition**
Two to three sentences. Facts only. Include: solo, unsupported, Berkner Island
to South Pole, about 1,350 km, roughly 60 days, alone in Antarctica, November 2027,
no resupply, no assistance, no backup equipment. Then one sentence on why it is
relevant to this specific brand.

**Paragraph 3 — The collaboration idea**
Two to three sentences on what a collaboration would look like and why it makes
sense for the brand specifically. Be concrete. Name a product, a use case, a
deliverable, a content angle. No vague "synergies" or "aligned values."

**Closing**
Two lines:
"I'd love to explore whether there's an opportunity to collaborate."
"Would you be open to a quick call to see if there's a fit? I can also send you a one pager with more details."

### Tone rules (strict)
- No word "sponsorship", "sponsor", "parrainage" anywhere
- No "—" character anywhere in the email body
- No bullet points or dashes inside the email body
- No AI-sounding phrasing
- No superlatives: not "unique", "incroyable", "extraordinaire", "unprecedented"
- Max 180 words total
- No signature — Aurélien adds it before sending

### Follow-up email (Day 10 to 12)
Same language as cold email. Max 70 words. One new angle or piece of information
not in the cold email (a recent news item, a specific product detail, a content
deliverable). Repeat the CTA. No "—" anywhere.

---

## STEP 4 — Create Gmail draft

Use the Gmail MCP to create a draft:
- To: primary contact email
- Subject: subject line from Step 3
- Body: cold email body from Step 3, no signature

Do not send. Draft only.

If Gmail is unavailable, output the full email in chat and note it clearly.

---

## STEP 5 — Update the Notion page

Open the brand's Notion page. Append content at the bottom only.
NEVER delete or overwrite anything already written on the page.

**If the page had no prior research content:**
Write "Pourquoi [Brand] est pertinent" first (Brand Fit Summary as flowing prose,
not bullet points with dashes), then "Contacts identifiés" (primary contact with
all details, plus alternative emails if confidence is Medium or Low, plus
"À vérifier sur Hunter.io ou Snov.io avant envoi" if applicable).

**Always append at the bottom, regardless:**

Leave three blank lines before the entry to create visual separation from existing content.
Then open with a clear header so the entry is immediately identifiable when scanning the page.

Format exactly like this:

---

🟡 OUTREACH — Draft créé le [DD/MM/YY]
Contact : [Name, Title] — [email used]
Objet : [subject line]
Valeur principale : [one sentence on the core value proposition used]

[full cold email body]

**If the only available contact point is a contact form (no direct email found):**
Do not create a Gmail draft. Instead, append at the very bottom of the Notion page:

⚠️ PAS D'EMAIL DIRECT — Ce contact n'est joignable que via formulaire : [URL du formulaire]

**Then update the Notion page properties:**
- Status → "Drafted"
- Contact → primary contact email address
- Dernier Contact → today's date

---

## Hard rules

Never delete any content from a Notion page.
Never send any email. Draft only.
Never use "—" anywhere in any email body.
Never use bullet points with dashes inside email bodies.
Never write AI-sounding phrasing.
Never process brands with Status = Partner, En discussion, Refus, Contacté,
relancé, Discount, Drafted, or empty.
Never process brands with Type = Media & Others.
Never pick a target from below the "📋 Sponsors déjà dans la base de données →
ne pas contacter" divider on the prioritization page — that section is reference
only, everything in it has already been contacted.
One brand per run, chosen autonomously based on conversion probability.
Choose the target using only search result titles and statuses — do not fetch
individual pages just to pick a brand.

---

## Edge cases

**Contact still at company is uncertain:** Note it in the Notion log. List
alternative emails. Still create the Gmail draft with the best guess.

**Brand page has existing research but no outreach yet:** Skip rewriting research
sections. Use what is already in the page to write the email. Add only the log
entry at the bottom.

**All brands above the divider exhausted:** Run Step 0b to propose 1 to 3 new
brand candidates, write them into the "A contacter (en vrac)" list above the
divider, then run the full pipeline on the one you pick. Never pull a new target
from below the divider.

**No Gmail connection:** Output the full draft in chat with subject line labeled.
Still update Notion with all content and today's date.
