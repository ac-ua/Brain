---
name: poc-use-case-filler
description: >
  Use this skill whenever the user wants to fill in, populate, or complete an AI use case
  definition document from their notes — whether those notes are free-form text, bullet points,
  a voice transcript, or a mix. The skill takes raw notes about a customer's POC use case and
  produces a filled Word document (.docx) based on the standard Enterprise AI Use Case Definition
  & Prioritization Template. Trigger this skill whenever the user mentions: "fill the use case
  template", "populate the use case doc", "use case document from my notes", "POC template",
  "customer use case doc", or any variation of filling/completing the use case template from
  notes or meeting output. Also trigger when the user shares notes and a prospect/customer name
  and asks to produce a document for them.
---

# POC Use Case Template Filler

## Purpose

This skill takes a solution architect's raw notes from a customer discovery session and fills
the **Enterprise AI Use Case Definition & Prioritization Template** as a polished Word doc
to send to the customer for review.

The customer name is provided by the user for each engagement (e.g. "Koch"). Replace it in
every placeholder (e.g. `[KOCH TO CONFIRM]` → `[CUSTOMER_NAME TO CONFIRM]`).

---

## Scope

This skill fills **one** template: the Enterprise AI Use Case Definition & Prioritization doc. It does not cover:
- **A POC scoping document** written after a workshop: build it from the example scoping doc Aurélien attaches
  (follow its sections), the workshop readout and the opportunity brief in Notion (`work-notes`).
- **A client's intake form** (e.g. a Gen AI intake form): prefill field by field from the same sources; give
  paste-ready text per field (`message-drafting`) or fill the `.docx` they sent.
- **A revision from a recorded call**: transcribe the recording first (`work-notes`, recordings), then revise the
  doc and list each change with the passage it came from.
In all three, add nothing the client didn't say (no invented success metric); unclear → `[TO CONFIRM]`.

## Writing Style (Critical)

These documents go directly to enterprise customers. The writing must:

- Be **direct and specific** — use the customer's own language and systems when possible
- Avoid AI-sounding filler ("leveraging cutting-edge", "seamlessly", "robust solution")
- Avoid restating the obvious or over-explaining what a section is for
- Match the density of the examples: concise paragraphs or tight bullet lists, not essays
- Use `[CUSTOMER TO CONFIRM]` for gaps — not lengthy explanations of why info is missing
- For Part 4 (Architecture), be concrete about UnifyApps capabilities — name the specific
  modules, connectors, and agent types that apply (see UnifyApps Reference below)

**Calibration examples** (study these before writing):

Good Problem Statement style:
  "Koch HR Operations cannot efficiently resolve incoming ServiceNow HR tickets because support
  staff must manually triage each ticket, research historical precedent, identify resolution
  steps, and execute them across multiple disconnected systems."

Good Vision/Experience style:
  "When an HR ticket arrives in ServiceNow, the agent automatically analyzes it against
  historical ticket data, identifies the most likely resolution path with a confidence score,
  and presents the recommendation to the support staff member."

Good table cell style (Architecture):
  "Infor GHR transaction records (new hire forms, employee master data, job data); field
  definitions and expected value ranges from GHR schema; historical correction records"

---

## Color Convention

| Color | Hex | Usage |
|-------|-----|-------|
| Blue | 1F5C99 | All content filled from notes or inferred from context |
| Yellow highlight + red text | highlight yellow / color FF0000 | Missing info: [CUSTOMER TO CONFIRM] |

Rules:
- Never change existing template text (black stays black)
- Never invent facts — flag gaps as yellow placeholders
- Assumptions written in blue must be labeled inline: [ASSUMPTION: brief reason]
- Keep placeholder text short: [CUSTOMER TO CONFIRM] is usually enough; only add detail
  when it's genuinely unclear what they need to provide

---

## UnifyApps Platform Reference

Use this knowledge to fill Part 4 (Architecture Map) sections concretely. Do not make up
capabilities — stick to what is documented here.

### Core Modules
- Unify Agents — LLM-agnostic AI agent builder. Supports Simple Agents (FAQ, doc-based)
  and Advanced Agents (tool integrations, custom workflows, dynamic decision-making).
  Agents can be internal (employee-facing) or external (customer-facing).
- Unify Automations — workflow automation builder. Automations can be exposed as tools
  that agents invoke. Handles complex multi-step business processes.
- Unify Applications — no-code/low-code app builder for human interfaces (web + mobile).
  Used to build human-in-the-loop review and approval UIs.
- Unify Data — real-time data replication (ETL/Reverse ETL) between any source and
  destination. Supports master data management and golden record creation.
- Unify Integrations — 600+ pre-built OOTB connectors to enterprise apps and databases.
  Custom connectors supported via Connector SDK.

### Agent Capabilities
- RAG pipeline with vector embeddings for knowledge retrieval
- GraphRAG and Text2SQL for advanced knowledge access
- MCP server support — workflows exposed as MCP-compliant tools
- Built-in guardrails: content filters, denied topics, confidence scoring
- LLM-agnostic: Claude, GPT, Gemini, open-source models, or custom fine-tuned
- Deployment: SaaS cloud, AWS/Azure/GCP, VPC, or on-premise

### Notable OOTB Connectors (reference for Action Context)
ServiceNow, SharePoint, Infor, SAP, Salesforce, Workday, BambooHR, DocuSign, Slack, Teams,
Email (IMAP/SMTP), Amazon S3, Redshift, Snowflake, Coupa, ClickUp, Confluence, Asana,
Amazon Bedrock, and 600+ more.

### Governance
- Full chain-of-thought logging and source citation
- Human-in-the-loop approval built into agent workflows
- Audit trail per action with timestamps and attribution
- Role-based access control inherited across platform
- Confidence scoring with configurable thresholds for agent autonomy

### POC Deployment Pattern
- POC phase: UnifyApps SaaS-managed cloud, often with scrubbed/synthetic customer data
- Production: customer VPC (AWS, Azure, GCP) or on-premise

---

## Workflow

### Step 1 — Gather inputs and research the customer

Collect from the user:
1. Notes — free-form, bullets, transcript, or mix
2. Customer/prospect name — for placeholders (e.g. [ACME TO CONFIRM])
3. Project documentation — if the user is in a Claude Project with uploaded technical docs
   (architecture specs, integration guides, system inventories), use them to enrich Part 4.

Then — always before writing — do a web search on the prospect company:
- What they do, their industry, size, business model
- Key operational processes relevant to the use case (e.g. if it's an HR use case, understand
  how their HR function is structured; if it's a PBM, understand their implementation workflow)
- Any publicly known technology stack, compliance requirements, or regulatory context

Use this research to:
- Write the Problem Statement and Business Consequences with the right industry framing
- Validate that the systems mentioned in the notes make sense for that type of company
- Identify compliance context (HIPAA/PHI, SOX, GDPR, etc.) that should surface in Governance
- Make Part 2 (Vision) resonate with the customer's actual business model

Do NOT cite or attribute the research in the document — just use it to write with accuracy.
Flag in blue as [ASSUMPTION] if you are drawing on research rather than what the notes state.

### Step 2 — Parse and classify

Map every note to its template section. Classify each field:
- FILLED — clear from notes → blue text
- INFERRED — reasonable given context → blue text + [ASSUMPTION: ...]
- MISSING — no basis in notes → yellow [CUSTOMER TO CONFIRM]

| Section | What to look for |
|---------|-----------------|
| Header | Use case title, sponsor name/title, business unit, go-live target |
| Problem Statement | What cannot be done today and why — one or two sentences |
| Digital State | System names, where data lives, what humans do manually |
| Business Consequences | Numbers (cost, headcount, frequency), risk exposure, user impact |
| Vision/Experience | End state for the end user |
| Vision/Architecture | Systems connected, deployment model, phasing |
| Vision/Governance | HITL requirements, PII constraints, audit needs |
| ROI | Any figures mentioned; leave yellow if none |
| Part 4 Knowledge | Data sources → map to Unify Data + RAG |
| Part 4 Action Context | Systems to read/write → map to OOTB connectors |
| Part 4 Governance | Rules and compliance → map to UnifyApps guardrails |
| Part 4 Workflows | Steps the agent takes → numbered sequence |
| Part 4 Apps | Who reviews/approves → Unify Applications interfaces |
| Part 4 Agents | What runs autonomously → Unify Agents (Simple or Advanced) |
| Part 5 Scorecard | Leave blank — do not fill |

### Step 3 — Write Part 4 with UnifyApps specificity

Part 4 is where the platform knowledge matters most. Be concrete:

- Knowledge table: name actual data sources; reference Unify Data for ETL/MDM and
  Unify Agents RAG/GraphRAG for knowledge indexing
- Action Context: map each system to its OOTB connector by name (e.g. "ServiceNow OOTB
  connector", "Infor GHR API via Unify Integrations custom connector")
- Governance: reference UnifyApps confidence scoring, chain-of-thought logging, HITL
  approval workflow
- Workflows: sequential agent steps — short action-verb sentences per step (see examples)
- Apps: describe interface by role, built on Unify Applications no-code builder
- Agents: describe autonomous actions — use Advanced Agent for multi-step orchestration

#### Dynamic row counts for Workflows, Apps, and Agents tables

The template ships with example rows (5 Workflows, 3 Apps, 5 Agents). These are **illustrative
only — do not treat them as targets.**

For each of these three tables:
- **Remove** rows that have no realistic counterpart in the use case
- **Add** rows if the solution genuinely requires more steps, interfaces, or agent types
- The final row count should reflect what the solution actually needs — a simple use case may
  have 2 workflows and 1 agent; a complex orchestration may have 7+ steps

When editing the XML, duplicate or delete `<w:tr>` row elements accordingly. Never leave
placeholder/example rows in the document with empty or generic content just to fill space.

Part 5 (Prioritization Scorecard) is left blank. Do not fill scores or rationale — the customer completes this.

If project documentation is available in context, use it to fill in system-specific details
(API availability, connector status, data schema, etc.).

### Step 4 — Produce the Word document

Use unpack → edit XML → repack on the bundled template.

Template location: assets/template.docx

```bash
# Unpack
python /mnt/skills/public/docx/scripts/office/unpack.py assets/template.docx unpacked/

# Edit word/document.xml using str_replace (do NOT write Python scripts for XML edits)

# Repack
python /mnt/skills/public/docx/scripts/office/pack.py unpacked/ output.docx --original assets/template.docx
```

#### Page break before each Part heading (Parts 1-5)

Each Part heading (Part 1 through Part 5) uses `Heading2` style in the XML. Add
`<w:pageBreakBefore/>` to its `<w:pPr>` so each Part starts on a new page. Do this
for all 5 Part headings as a post-fill step using a Python string replacement:

```python
import re

def add_page_break_to_part_headings(content):
    # Match Heading2 paragraphs containing "Part N:" text
    # Pattern: find <w:pPr> inside a paragraph that contains "Part [1-5]:"
    def inject_pagebreak(m):
        para = m.group(0)
        if re.search(r'Part [1-5]:', para) and 'Heading2' not in para[:para.find('Part')]:
            # Not a heading - skip
            return para
        if '<w:pageBreakBefore/>' in para:
            return para  # already added
        return para.replace('<w:pStyle w:val="Heading2"/>', '<w:pStyle w:val="Heading2"/><w:pageBreakBefore/>', 1)
    return re.sub(r'<w:p\b[^>]*>.*?</w:p>', inject_pagebreak, content, flags=re.DOTALL)
```

Simpler alternative — do a direct targeted replacement for each of the 5 Part headings:

```python
# pageBreakBefore must sit AFTER keepNext/keepLines in the pPr element order.
# The Part heading paragraphs have this structure:
#   <w:pStyle w:val="Heading2"/>
#   <w:keepNext w:val="0"/>
#   <w:keepLines w:val="0"/>
#   <w:spacing .../>
# Insert pageBreakBefore after keepLines, before spacing:

content = content.replace(
    '<w:keepNext w:val="0"/>\n        <w:keepLines w:val="0"/>\n        <w:spacing',
    '<w:keepNext w:val="0"/>\n        <w:keepLines w:val="0"/>\n        <w:pageBreakBefore/>\n        <w:spacing',
    5  # 5 Part headings
)
```

**IMPORTANT — element order in `<w:pPr>`:** `<w:pageBreakBefore/>` must come after
`<w:keepNext>` and `<w:keepLines>` but before `<w:spacing>`. Placing it immediately
after `<w:pStyle>` causes a schema validation error (`keepNext` is not expected there).

Only apply to Part heading paragraphs. Verify there are exactly 5 instances of the
`keepNext/keepLines/spacing` pattern in Heading2 paragraphs before using the count limit.
If other Heading2 paragraphs share this exact structure, match by adjacent Part text instead.

#### Blue text (filled content)
```xml
<w:r>
  <w:rPr>
    <w:color w:val="1F5C99"/>
  </w:rPr>
  <w:t xml:space="preserve">Content here</w:t>
</w:r>
```

#### Yellow highlight (missing info) — MANDATORY for ALL [CUSTOMER TO CONFIRM] instances

**Every single `[CUSTOMER TO CONFIRM]` or `[CUSTOMER TO PROVIDE: ...]` in the document
MUST use yellow highlight + red text. No exceptions — including inline mentions within
otherwise blue paragraphs.**

```xml
<w:r>
  <w:rPr>
    <w:highlight w:val="yellow"/>
    <w:color w:val="FF0000"/>
  </w:rPr>
  <w:t xml:space="preserve">[RXBENEFITS TO CONFIRM]</w:t>
</w:r>
```

When a blue paragraph contains a mix of filled content and a gap, split into two runs:
```xml
<w:r>
  <w:rPr><w:color w:val="1F5C99"/></w:rPr>
  <w:t xml:space="preserve">Known content here. </w:t>
</w:r>
<w:r>
  <w:rPr><w:highlight w:val="yellow"/><w:color w:val="FF0000"/></w:rPr>
  <w:t xml:space="preserve">[RXBENEFITS TO CONFIRM] specific detail needed.</w:t>
</w:r>
```

As a final cleanup step after all edits, do a Python scan to catch any plain-text
`[CUSTOMER TO CONFIRM]` that ended up without yellow highlight:
```python
# Sanity check — should return 0
import re
plain = re.findall(r'(?<!highlight.*?)TO CONFIRM\](?!.*?highlight)', content)
print(f"Unformatted CONFIRM tags remaining: {len(plain)}")
```

#### Assumption inline (blue, labeled)
```xml
<w:r>
  <w:rPr>
    <w:color w:val="1F5C99"/>
  </w:rPr>
  <w:t xml:space="preserve">Content [ASSUMPTION: reason]</w:t>
</w:r>
```

#### Table cells (Your Input column — 3rd column)
Replace the inner <w:p> of the relevant <w:tc> with the colored run(s) above.

For multi-paragraph cells, use multiple <w:p> elements:
```xml
<w:p>
  <w:r><w:rPr><w:color w:val="1F5C99"/></w:rPr><w:t>First point</w:t></w:r>
</w:p>
<w:p>
  <w:r><w:rPr><w:color w:val="1F5C99"/></w:rPr><w:t>Second point</w:t></w:r>
</w:p>
```

### Step 5 — Validate and deliver

```bash
python /mnt/skills/public/docx/scripts/office/validate.py output.docx
```

Output filename: [CustomerName]_UseCase_[ShortTitle]_filled.docx
Example: Koch_UseCase_HCMDataQuality_filled.docx

Deliver with a brief summary (3-5 lines):
- Fields filled from notes
- Assumptions made (list them)
- Yellow placeholders for customer to complete

---

## Checklist Before Delivering

- [ ] Header fields all addressed (blue or yellow)
- [ ] All underscore lines replaced
- [ ] All "Your Input" table cells filled (never left blank)
- [ ] Part 5 scorecard left blank (customer fills this)
- [ ] Part 4 references specific UnifyApps modules and connectors by name
- [ ] Workflows / Apps / Agents tables have the right number of rows for the use case — no leftover example rows, no artificial padding
- [ ] Parts 1-5 each start on a new page (pageBreakBefore on Heading2 paragraphs)
- [ ] Every [CUSTOMER TO CONFIRM] is yellow highlight + red text — no plain-text instances
- [ ] No black text added
- [ ] No invented facts without [ASSUMPTION] label
- [ ] Writing is direct and concise — no AI filler phrases
- [ ] Validated with no errors

---

## Known XML Pitfall: Header Placeholder Replacements

When replacing inline placeholder text (underscore lines, blank fields) inside an existing
`<w:r>...</w:r>` run in the header section, the pattern closes the original run and opens new
ones. The original run's closing `</w:r>` tag will still be present in the XML and must be
removed, otherwise the document fails validation.

**Safe pattern for header field replacements:**

```python
# WRONG — leaves orphaned </w:r>
content = content.replace(
    '<w:t ...> ___...</w:t>',
    '<w:t> </w:t></w:r><w:r><w:rPr>...</w:rPr><w:t>Value</w:t></w:r>'
    # The original closing </w:r> from the parent run is still in the XML
)

# CORRECT — also strip the parent run's closing tag
content = content.replace(
    '<w:t ...> ___...</w:t>\n      </w:r>',
    '<w:t> </w:t></w:r><w:r><w:rPr>...</w:rPr><w:t>Value</w:t></w:r>'
)
```

Always inspect 1-2 lines after the placeholder text to check for a `</w:r>` that needs
to be consumed in the replacement string.
