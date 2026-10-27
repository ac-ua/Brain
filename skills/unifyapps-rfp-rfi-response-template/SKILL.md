---
name: unifyapps-rfp-rfi-response-template
description: Generate customer-ready UnifyApps RFP/RFI response documents by filling broad placeholders in a DOCX template while preserving all branding, images, layout, and standard sections from Deployment and Security Model onward. Uses a single master template (v3) with standardized styling, a fully embedded UnifyApps Platform Capabilities appendix (A.1-A.6), and refreshed standard sections. Bundles a capability-audit catalogue (knowledge/unifyapps_rfp_capability_audit.xlsx) of safer, defensible requirement wording and a Solution Architect knowledge base (knowledge/UnifyApps_SA_Knowledge_Base.txt) for grounding and differentiation.
---

# UnifyApps RFP/RFI Response Template Skill

## Purpose

Use this skill when the user asks to generate, complete, adapt, or customize a UnifyApps RFP/RFI response document using a reusable UnifyApps response template.

The skill is designed for enterprise presales responses where the first content sections must be generated for a specific customer and the standard platform/security/implementation sections must remain unchanged.

## Bundled Knowledge

Two knowledge collaterals are bundled with this skill in the `knowledge/` folder. Consult them as needed; they are load-on-demand references, not always-loaded context.

### Capability Audit Catalogue — `knowledge/unifyapps_rfp_capability_audit.xlsx`

Use `knowledge/unifyapps_rfp_capability_audit.xlsx` in RFP/RFI responses where it can show more value and differentiation.

This is a catalogue of platform requirements expressed in safer, defensible RFP wording, each graded across columns including: ID, Category, Requirement Area, Safer RFP Requirement Wording, Audit Level (e.g. Common, Moderate, Strong Differentiator, Highly Restrictive), Compliance Difficulty (1–5), Priority (Mandatory / Scored), Why This Makes Compliance Harder, Safer Notes / Equivalent Capability, Mandatory Flag, Audit Risk Comment, and Suggested Evaluation Treatment.

Consult it whenever differentiation helps in any presales response (RFP, RFI, vendor questionnaire, or capability/compliance matrix). Use it to:

- **Strengthen the Functional Capability Response** by aligning answers to the safer, defensible wording already vetted in the catalogue, and to highlight UnifyApps strengths in high-differentiation areas (Audit Level "Strong Differentiator" / Compliance Difficulty 4–5).
- **Lead with differentiation**: prioritize requirement areas marked as Strong Differentiator or Highly Restrictive — agent tool governance, prompt-to-build, LLM flexibility, AI registry, online evaluation, observability, governed memory — where competitors are weak.
- **Stay defensible**: apply the "Safer Notes / Equivalent Capability" guidance (e.g. add "or equivalent" when naming specific tools/frameworks) and respect the "Audit Risk Comment" so claims remain defensible.
- **Map evaluation treatment**: use the "Suggested Evaluation Treatment" (gate + scored evidence vs. scored differentiator) to shape how each answer is positioned.

To read it, use the `xlsx` skill conventions, e.g. `extract-text knowledge/unifyapps_rfp_capability_audit.xlsx` for a quick dump, or pandas for filtering by Audit Level / Priority. Do not overwrite it or claim compliance beyond what the Safe Positioning Rules below allow.

### Solution Architect Knowledge Base — `knowledge/UnifyApps_SA_Knowledge_Base.txt`

`knowledge/UnifyApps_SA_Knowledge_Base.txt` is the authoritative grounding source for platform claims, positioning, templates, sizing, safe wording, and use-case patterns. It is large (~6,800 lines); load it on demand rather than wholesale.

- Use `knowledge/UnifyApps_SA_Knowledge_Base_INDEX.txt` (a line-numbered section index) to locate the relevant section, then read only that range from the knowledge base.
- Most relevant sections for RFP/RFI work include: Platform Overview, Strategic Positioning / Traps, CCRAG Architecture, RFP/RFI Response Framework and Compliance Position Definitions, Common Safe RFP Wording, Sizing Methodology, Clarification Questions, Risk Review Checklist, Common Use Case Patterns, Standard Customer-Facing Assumptions, Out-of-Scope Language, Standard Executive Summary Pattern, and "Why UnifyApps" Points.
- Ground generated content (executive summary, solution overview, capability answers, assumptions, "Why UnifyApps") in this knowledge base rather than inventing platform claims. Where the knowledge base and the Safe Positioning Rules below differ, the Safe Positioning Rules take precedence.

## Template

There is one master template:

`templates/UnifyApps_RFP_RFI_Response_Master_Template_v3.docx`

It provides the full document structure with five placeholders for the AI-generated sections, standardized table styling (brand-purple `705AF5` headers with white bold text, dark-grey `404040` size-9 normal-weight body), knowledge-base-grounded UnifyApps Platform descriptions, and a fully embedded **UnifyApps Platform Capabilities** appendix (A.1 Enterprise Systems & Resources, A.2 AI Ontology & Data, A.3 AI Workflows, A.4 AI Applications, A.5 AI Agents, A.6 Governance, Security & Scalability), with the table of contents already wired to all sections including the appendix.

Always start every RFP/RFI response task from this template. Do not ask the user to choose a template.

## Source Template Rules

Do not recreate the response from scratch.

Do not convert the whole template to Markdown as the final output.

The final response must remain a DOCX to preserve layout, branding, images, page styling, screenshots, tables, headers, and footers.

## Placeholders to Replace

Replace exactly these placeholders:

1. `{{DOCUMENT_TITLE}}`
2. `{{EXECUTIVE_SUMMARY}}`
3. `{{OVERVIEW_PROPOSED_SOLUTION}}`
4. `{{UNDERSTANDING_OF_REQUIREMENTS}}`
5. `{{FUNCTIONAL_CAPABILITY_RESPONSE}}`

Each placeholder represents one full section.

Do not create many small placeholders inside the section.

Do not leave placeholder text in the final document.

## Standard Section Boundary

The heading **Deployment and Security Model** marks the start of standard content.

Everything from **Deployment and Security Model** to the end of the document must remain in place and must not be rewritten during normal use of this skill.

This includes, but is not limited to:

- Deployment and Security Model
- Platform On-Prem/Self Hosted Installation Requirements
- Security Compliance and Regulatory Certifications
- Project Implementation and Management Approach
- Roles and Responsibilities
- SLA and RACI
- UnifyApps Platform
- UnifyApps Platform Capabilities appendix: A.1 Enterprise Systems & Resources, A.2 AI Ontology & Data, A.3 AI Workflows, A.4 AI Applications, A.5 AI Agents, A.6 Governance, Security & Scalability
- Product screenshots and platform overview pages
- Closing page

Only modify the standard sections if the user explicitly requests changes to those sections.

The embedded Platform Capabilities appendix (A.1–A.6) is standard content. Do not regenerate, trim, or reorder it during normal RFP/RFI completion; leave it intact unless the user explicitly asks to edit the appendix. Because this content is already embedded in the template, there is no need to append a capabilities appendix separately.

## Required Inputs

When available, use:

- Customer name
- RFP/RFI title
- RFP/RFI requirement document
- Customer industry
- Required use case or platform scope
- Required deployment model
- Required integrations
- Required compliance/security constraints
- Any explicit response style requested by the user
- Any customer-specific restrictions or claims that must be avoided

If some inputs are missing, do not silently invent and bake in assumptions.

When assumptions are needed to proceed, first present the proposed assumptions to the user as a clearly labeled list and ask them to confirm or correct them. Only incorporate assumptions into the document after the user has validated them. If the user wants to proceed without reviewing, label every assumption explicitly in the document as an unvalidated assumption to be confirmed.

## Content Generation Rules

### Sentence Formatting (Period → New Line)

In long or multi-sentence paragraphs, **start a new line after each sentence-ending period.** Write one sentence per line so dense prose stays scannable in the DOCX.

- Apply this to narrative body content in the generated sections (Executive Summary, Overview Proposed Solution, Understanding of Requirements) and to multi-sentence response text.
- This applies to sentence-ending periods only. Do not break the line for periods inside abbreviations, decimals, version numbers, URLs, or list labels (e.g. "v3", "TLS 1.3", "e.g.", "1,328 GB").
- Inside table cells, keep this light: break only when a cell genuinely holds multiple full sentences; short single-sentence cells stay on one line.
- This is a formatting convention for readability; it does not change wording, length targets, or the safe-positioning rules below.

### Clarifications — Separate Document

Never embed open questions, "TBD", or "to be clarified with customer" notes inside the response document itself.

When the RFP/RFI has gaps, ambiguities, or items that genuinely need the customer's input, capture them in a **separate clarifications document** (a distinct DOCX or Markdown file, e.g. `<Customer>_Clarifications.docx`), not in the response. Produce this clarifications document whenever clarifications exist, and deliver it alongside the main response as a separate file. Keep the main response clean, complete, and customer-ready. Structure the clarifications document as a numbered list grouped by section or requirement area, with each item stating the question, why it matters, and (where useful) the options or default UnifyApps would otherwise assume.

### Lead With UnifyApps Differentiation

Whenever generating or responding with content, actively surface UnifyApps value as a differentiator — but only where it is relevant and makes sense for that requirement.

- In each substantive section and in capability answers, add a short, specific differentiator note (typically one to two sentences) explaining why the UnifyApps approach is stronger than the alternative or status quo, rather than only confirming compliance.
- Draw differentiators from `knowledge/unifyapps_rfp_capability_audit.xlsx`, prioritising rows marked **Strong Differentiator** or **Highly Restrictive** (high Compliance Difficulty) — e.g. agent tool-level governance, prompt-to-build, LLM flexibility / BYO LLM, AI registry, online evaluation, observability, governed memory — and phrase them using the catalogue's safer wording.
- Keep it proportionate and credible: a couple of sharp sentences where it strengthens the answer, not a sales pitch on every line. Do not force a differentiator where it is not relevant, and never let differentiation language override the Safe Positioning Rules below.

### Executive Summary

Keep this section short, precise, and executive-friendly.

Recommended length:

- 4 to 7 concise paragraphs
- Usually 0.5 to 1 page
- No long tables
- No deep technical implementation detail

The executive summary should:

1. State what the customer is seeking.
2. Summarize the business problem or transformation need.
3. Position UnifyApps as the proposed platform or operating layer.
4. Highlight only the most relevant capabilities.
5. State the expected business outcomes.
6. Mention integration, governance, security, and scalability at a high level.
7. Close with why UnifyApps is aligned to the requirement.

### Overview Proposed Solution

Make this section moderately detailed.

Recommended length:

- 1.5 to 3 pages
- Narrative plus tables

Include:

1. Proposed solution narrative.
2. Proposed solution objectives table.
3. Core solution components table.
4. High-level deployment and integration positioning.
5. Business and technical alignment.

Do not make this section generic. Align it to the customer requirement.

### Understanding of Requirements

This should be the most elaborated and customer-specific section.

Recommended length:

- 3 to 6 pages for a normal RFP/RFI
- Longer if the RFP/RFI is complex

Include:

1. Customer context.
2. Current-state understanding.
3. Target-state understanding.
4. Requirement interpretation.
5. Requirement mapping table.
6. Operating model understanding.
7. Critical success factors.
8. Assumptions and dependencies.

This section should prove that UnifyApps deeply understands the customer's requirements. It should not read like a generic sales pitch.

### Functional Capability Response

Use structured tables and direct answers.

Recommended length:

- 3 to 10+ pages depending on requirement volume

Include:

1. Functional response introduction.
2. Functional capability matrix.
3. Direct requirement-by-requirement answers.
4. Answers to customer-specific questions.
5. Compliance status with safe wording.
6. Dependencies, assumptions, and integration notes.
7. Differentiation where relevant.

Use these compliance labels:

- Fully Compliant
- Compliant with Configuration
- Compliant with Integration
- Requires Clarification
- Not in Scope / Partner / Customer Dependency

Use "Fully Compliant" only when defensible.

When building the functional capability matrix and requirement-by-requirement answers, cross-reference `knowledge/unifyapps_rfp_capability_audit.xlsx` to (1) reuse safer, defensible requirement wording, (2) lead with the highest-differentiation areas, and (3) apply each requirement's "Safer Notes" and "Audit Risk Comment" so claims stay defensible.

## Styling Standard

Keep all newly generated tables and response content consistent with the standardized house style:

- **Table header row**: brand purple fill `705AF5`, text white `FFFFFF`, bold, font size 9.
- **Table body cell**: white fill `FFFFFF`, text dark grey `404040`, normal weight (not bold), font size 9.
- **Response / body content** (table cells and response text): dark grey `404040`, font size 9, normal weight. Reserve bold for headings, defined feature labels, and header rows only.
- Use the fonts already in the template; do not introduce new fonts.

This styling standard applies to all generated tables and response content in the document.

## Safe Positioning Rules

Do not overpromise.

Do not claim that UnifyApps provides an LLM unless the source input explicitly says so.

Default to customer-approved LLM / BYO LLM wording.

Do not claim regulatory compliance is guaranteed.

Do not claim all integrations are out of the box unless the specific connector or integration path is confirmed.

Do not claim final AI decisions should be fully automated for regulated or high-impact decisions unless explicitly required and approved.

Use safe wording such as:

- "UnifyApps can support this through configuration and integration with the relevant enterprise systems."
- "Final feasibility depends on API availability, data quality, access permissions, and security review."
- "AI-generated recommendations should remain subject to human approval for regulated or high-impact decisions."
- "The solution assumes customer-provided LLM access unless otherwise agreed."

## Output Process

1. Use the master template — `templates/UnifyApps_RFP_RFI_Response_Master_Template_v3.docx`. Do not ask the user to choose a template.
2. Copy the template.
3. Read the customer RFP/RFI inputs, and consult the bundled knowledge — ground platform claims in `knowledge/UnifyApps_SA_Knowledge_Base.txt` (via its index) and cross-reference `knowledge/unifyapps_rfp_capability_audit.xlsx` for differentiation and safer wording.
4. Identify the customer name and any other named accounts strictly from the input files. If assumptions are required, present them to the user and get confirmation before incorporating them (see Required Inputs).
5. Generate content for the five placeholders. Weave in short, relevant UnifyApps differentiator notes (see Lead With UnifyApps Differentiation), drawing from the capability-audit catalogue where it makes sense.
6. Replace each placeholder with complete formatted content. Apply the standardized styling (purple `705AF5` table headers with white bold text; dark-grey `404040`, size-9, normal-weight body and response content). In long narrative paragraphs, start a new line after each sentence-ending period (see Sentence Formatting rule).
7. Preserve all headings and standard sections. Leave the embedded Platform Capabilities appendix (A.1–A.6) and the table of contents intact.
8. Verify no placeholder remains.
9. Verify no old customer-specific content remains in generated sections.
10. **Read through the entire output file end to end and confirm customer-name integrity**: the only customer/account name appearing anywhere in the generated sections must be the one taken from the input files. Check for any leftover or mixed customer names, account names, or project names from other engagements, sample text, or prior responses (including ones that may exist in the standard sections), and remove or correct any that do not match the input customer. Do not deliver until this passes.
11. If any clarifications are needed, produce them in a **separate clarifications document** (not inside the response) and deliver it alongside the main file.
12. Render or visually inspect the DOCX before delivering it when tooling allows.
13. Deliver the completed DOCX (plus the separate clarifications document if one was produced).

## Supporting References

Use:

- `reference/UnifyApps_RFP_RFI_Template_Content_Instructions.md` — the detailed shared section-by-section writing guidance (length, coverage, wording) for all five generated sections.
- `reference/UnifyApps_RFP_RFI_Template_Content_Instructions_v3.md` — the v3-specific structure notes (embedded Platform Capabilities appendix and standardized styling).
- `reference/UnifyApps_RFP_RFI_Template_Placeholder_Map_v3.md` — the placeholder map and replacement rules.

For grounding and differentiation, also use:

- `knowledge/unifyapps_rfp_capability_audit.xlsx` — capability-audit catalogue of safer requirement wording graded by differentiation strength.
- `knowledge/UnifyApps_SA_Knowledge_Base.txt` — full Solution Architect knowledge base (use `knowledge/UnifyApps_SA_Knowledge_Base_INDEX.txt` to navigate).

## Final Quality Gate

The final response must be customer-ready, defensible, and professional.

It must preserve the original template layout, branding, images, tables, page style, and standard content.

The generated sections must be customer-specific, not generic.

Before delivering, confirm all of the following:

- The whole output file has been read end to end, and the only customer/account/project name anywhere in the document is the one from the input files. No mixed, leftover, or sample customer names remain.
- Any assumptions in the document were validated with the user first, or are explicitly labeled as unvalidated assumptions to be confirmed.
- Clarifications, if any, live in a separate clarifications document — not inside the response.
- Relevant UnifyApps differentiators are surfaced concisely where they strengthen the answer, grounded in the capability-audit catalogue and consistent with the Safe Positioning Rules.
