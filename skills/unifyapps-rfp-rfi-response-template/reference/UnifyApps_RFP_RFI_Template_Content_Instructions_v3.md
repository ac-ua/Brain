# UnifyApps RFP/RFI Response Template v3 - Content Instructions

## What v3 Is

v3 is the master RFP/RFI response template — the only template used by this skill. It applies two things on top of the base structure:

1. **A fully embedded "UnifyApps Platform Capabilities" appendix (A.1–A.6)** built directly into the template, covering the platform's six functional modules and their capability areas as structured Capability + Description tables.
2. **A standardized house style** — purple `705AF5` table headers with white bold text, dark-grey `404040` size-9 normal-weight body — plus knowledge-base-grounded UnifyApps Platform descriptions and a consolidated standard-section set with the table of contents already wired to all sections including the appendix.

The placeholder list, the fill approach, the standard-section boundary concept, the writing rules, and the validation steps follow the shared writing guidance. Use this file together with `UnifyApps_RFP_RFI_Template_Content_Instructions.md` for the section-by-section writing guidance; this file documents the v3-specific structure (embedded appendix and styling).

## Source Template

`templates/UnifyApps_RFP_RFI_Response_Master_Template_v3.docx`

Do not rebuild the document in Markdown. The final customer response must be a DOCX so layout, branding, images, tables, headers, footers, standard sections, and the embedded capabilities appendix are preserved.

## Placeholders

Replace exactly these placeholders, each representing one full section:

1. `{{DOCUMENT_TITLE}}`
2. `{{EXECUTIVE_SUMMARY}}`
3. `{{OVERVIEW_PROPOSED_SOLUTION}}`
4. `{{UNDERSTANDING_OF_REQUIREMENTS}}`
5. `{{FUNCTIONAL_CAPABILITY_RESPONSE}}`

Follow the section-by-section length and coverage guidance in `UnifyApps_RFP_RFI_Template_Content_Instructions.md`. That shared guidance applies without change.

## Standard Section Boundary (extended in v3)

The heading **Deployment and Security Model** marks the start of standard content. Everything from that heading to the end of the document remains in place and must not be rewritten during normal use, unless the user explicitly requests changes.

In v3 the standard section set explicitly includes:

- Deployment and Security Model
- Platform On-Prem/Self Hosted Installation Requirements
- Security Compliance and Regulatory Certifications
- Project Implementation and Management Approach
- Roles and Responsibilities
- SLA and RACI
- UnifyApps Platform
- **UnifyApps Platform Capabilities appendix (A.1 Enterprise Systems & Resources, A.2 AI Ontology & Data, A.3 AI Workflows, A.4 AI Applications, A.5 AI Agents, A.6 Governance, Security & Scalability)**
- Product screenshots, platform overview pages, and closing page

The embedded Platform Capabilities appendix is standard content. Do not regenerate, trim, or reorder it during normal RFP/RFI completion. Leave it intact unless the user explicitly asks to edit the appendix.

## v3 Standardized Styling

When generating or editing content in v3, match the standardized house style so the document stays visually consistent.

### Tables

- **Header row**: brand purple fill `705AF5`, text white `FFFFFF`, bold, font size 9 (half-point value 18).
- **Body cells**: white fill `FFFFFF`, text dark grey `404040`, normal weight (not bold), font size 9 (half-point value 18).
- Use the same fonts already present in the template (Poppins family for headings, the established body font for content). Do not introduce new fonts.
- Keep tables full content width, fixed layout, with consistent cell padding.

### Response / Body Content

- Section response text inside table cells and response body content uses **dark grey `404040`, font size 9, normal weight (not bold)**.
- Do not bold entire response sentences. Bolding is reserved for headings, defined feature labels, and table header rows.

### Compliance Labels (unchanged)

- Fully Compliant
- Compliant with Configuration
- Compliant with Integration
- Requires Clarification
- Not in Scope / Partner / Customer Dependency

## Embedded Platform Capabilities Appendix

v3 ships with the full Platform Capabilities appendix already written and styled inside the template. It is grounded in the UnifyApps Key Platform Features documentation and is organized as:

- **A.1 Enterprise Systems & Resources** — Enterprise Connectivity, Integration Resilience & Governance, Enterprise Context & Reusability.
- **A.2 AI Ontology & Data** — Data Pipelines, Data Catalog, Master Data Management, Data Quality, Data Governance.
- **A.3 AI Workflows** — No-Code AI Workflow Builder, Monitoring/Debugging/Optimization, Governance & Auditability, API Gateway.
- **A.4 AI Applications** — No-Code Low-Code AI Application Builder, Customisation Capabilities, Performance Monitoring & Governance.
- **A.5 AI Agents** — No-Code Agent Builder, Knowledge & RAG, Enterprise Search, Governance & Observability, Memory & Learning, Evaluation, Interoperability, Model Library.
- **A.6 Governance, Security & Scalability** — AI Governance, Standard Platform Governance, Environment Management, Enterprise Security Standards, Compliance & Auditability, Platform Scalability.

Because this content is now embedded, there is no need to append it separately for v3 responses. Reference specific capability areas from this appendix when strengthening the Functional Capability Response.

## Safe Positioning Rules (unchanged)

- Do not overpromise.
- Do not claim UnifyApps provides an LLM. Default to customer-approved / BYO LLM wording.
- Do not claim regulatory compliance is guaranteed.
- Do not claim all integrations are out of the box unless the specific connector or path is confirmed.
- Do not claim fully automated final decisioning for regulated or high-impact decisions.

Use safe wording such as:

- "UnifyApps can support this through configuration and integration with the relevant enterprise systems."
- "Final feasibility depends on API availability, data quality, access permissions, and security review."
- "AI-generated recommendations should remain subject to human approval for regulated or high-impact decisions."
- "The solution assumes customer-provided LLM access unless otherwise agreed."

## Final Validation Checklist (v3)

- All five placeholders are replaced and no placeholder text remains.
- The section "Deployment and Security Model" and all following standard sections — including the embedded Platform Capabilities appendix (A.1–A.6) — remain present and unchanged (unless explicitly requested).
- New table headers use purple `705AF5` with white bold text; body cells use dark grey `404040`, size 9, normal weight.
- No old customer-specific content remains in the generated sections.
- No accidental references to another customer remain.
- The response does not claim LLM inclusion unless explicitly requested.
- All compliance claims are defensible.
- The DOCX renders cleanly without broken layout, clipped tables, or missing images, and the table of contents (including the appendix entries) is intact.
