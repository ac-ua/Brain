# UnifyApps RFP/RFI Response Template - Content Instructions (Shared Writing Guidance)

## Purpose

This template is a reusable UnifyApps RFP/RFI response document. It is designed to preserve the original Word layout, branding, images, tables, page styling, and standard platform sections while allowing AI to generate only the customer-specific response sections.

Use the DOCX template as the source of truth. Do not rebuild the document in Markdown. Markdown is acceptable only for drafting content, but the final customer response must be produced in DOCX so the visual layout, images, tables, page breaks, and formatting are preserved.

## Fill Strategy

The template contains one placeholder for each AI-generated content section:

- `{{DOCUMENT_TITLE}}`
- `{{EXECUTIVE_SUMMARY}}`
- `{{OVERVIEW_PROPOSED_SOLUTION}}`
- `{{UNDERSTANDING_OF_REQUIREMENTS}}`
- `{{FUNCTIONAL_CAPABILITY_RESPONSE}}`

Only replace those placeholders.

Do not rewrite, summarize, remove, or restructure the standard content starting from the section titled **Deployment and Security Model** through the end of the document unless the user explicitly asks for it.

## Standard Section Boundary

The following sections are standard and must remain as-is:

- Deployment and Security Model
- Platform On-Prem/Self Hosted Installation Requirements
- Security Compliance and Regulatory Certifications
- Project Implementation and Management Approach
- Roles and Responsibilities
- SLA and RACI
- UnifyApps Platform
- Any following platform overview, screenshots, product description, or closing pages

These sections are considered reusable standard response content. Do not regenerate them as part of normal RFP/RFI completion.

## General Writing Rules

Write in a professional enterprise presales tone.

Be clear, direct, and commercially usable.

Separate confirmed customer requirements from UnifyApps positioning.

Do not invent customer facts.

Do not overpromise UnifyApps capabilities.

Do not claim that UnifyApps provides an LLM unless explicitly provided in the input.

Default to BYO LLM / customer-approved LLM wording unless the customer requirement says otherwise.

Avoid absolute commitments such as "guaranteed", "fully automated final decisioning", "no customer effort required", or "all integrations are available out of the box" unless explicitly confirmed.

Use customer-safe wording such as:

- "UnifyApps can support this through configuration and integration with the relevant enterprise systems."
- "Final feasibility depends on API availability, data quality, access permissions, and security review."
- "AI-generated recommendations should remain subject to human approval for regulated or high-impact decisions."
- "The solution assumes customer-provided LLM access unless otherwise agreed."
- "The proposed approach can be configured based on the customer's operating model, governance framework, approval hierarchy, and integration landscape."

## Section-Specific Instructions

### 1. `{{DOCUMENT_TITLE}}`

Replace with a concise title for the response.

Recommended format:

`<Customer Name> - <RFP/RFI Name> - UnifyApps Response`

Examples:

- `ABC Bank - Enterprise AI Governance Platform RFI - UnifyApps Response`
- `Government Entity - Digital Services Platform RFP - UnifyApps Response`
- `Telecom Operator - Agentic AI Automation RFI - UnifyApps Response`

Keep it short enough to fit on the cover page.

---

### 2. `{{EXECUTIVE_SUMMARY}}`

The executive summary must be precise, short, and business-focused.

Recommended length:

- 4 to 7 concise paragraphs
- Usually 0.5 to 1 page
- Avoid long tables
- Avoid deep technical detail

Coverage required:

1. State what the customer is seeking.
2. Summarize the business problem or transformation need.
3. Position UnifyApps as the proposed platform or operating layer.
4. Highlight the main capabilities relevant to the RFP/RFI.
5. State the business outcomes expected.
6. Mention integration, governance, security, and scalability at a high level.
7. Close with why UnifyApps is aligned to the customer's requirement.

Executive summary style:

- Short and confident.
- Do not repeat the whole proposal.
- Do not include excessive feature lists.
- Do not go deep into implementation details.
- Do not include unsupported claims.

Good executive summary wording pattern:

`<Customer Name> is seeking <solution category> to address <business need>. UnifyApps proposes <solution positioning> that enables <core outcomes>. The proposed approach brings together <core platform areas> to support <customer requirement areas>. Through <governance/integration/automation/AI capabilities>, UnifyApps can help <Customer Name> move from <current-state challenge> to <desired-state operating model>.`

---

### 3. `{{OVERVIEW_PROPOSED_SOLUTION}}`

The proposed solution overview should be moderately detailed. It should explain what UnifyApps proposes, how the solution is structured, and how it addresses the customer's requirements.

Recommended length:

- 1.5 to 3 pages depending on RFP complexity
- Use tables where useful
- Include solution objectives and core components

Coverage required:

1. Proposed solution narrative
   - Explain the UnifyApps solution at a high level.
   - Describe the proposed operating layer, application layer, automation layer, AI agent layer, data/knowledge layer, and integration layer where relevant.

2. Solution objectives table
   - Include a table with columns such as:
     - Objective
     - Proposed UnifyApps Approach
   - Keep each objective specific to the customer requirement.

3. Core solution components table
   - Include a table with columns such as:
     - Component
     - Description
   - Components should match the RFP/RFI scope.

4. Deployment/integration positioning at a high level
   - Keep details light because the standard deployment section already exists later in the document.

5. Business and technical alignment
   - Explain how the proposed solution aligns with the customer's business, governance, operational, integration, and scalability needs.

Do not make this section too short. It should provide enough substance for evaluators to understand the proposed solution before reading the detailed functional response.

---

### 4. `{{UNDERSTANDING_OF_REQUIREMENTS}}`

This is the section that should be the most elaborated and customer-specific.

The goal is to prove that UnifyApps deeply understands the customer's requirements, operating context, business drivers, pain points, scope, and success criteria.

Recommended length:

- 3 to 6 pages for a normal RFP/RFI
- Longer if the customer document is complex
- Use narrative plus requirement mapping tables

Coverage required:

1. Customer context
   - Explain what the customer is trying to achieve.
   - Mention the customer sector, business environment, operating model, and transformation context if provided.

2. Current-state understanding
   - Explain likely current challenges based only on the RFP/RFI content.
   - Examples: fragmented systems, manual processes, lack of governance, disconnected workflows, slow approvals, poor visibility, inconsistent data, limited automation, inconsistent AI oversight, etc.

3. Target-state understanding
   - Explain the desired future state.
   - Connect it to UnifyApps capabilities without turning the section into a sales pitch.

4. Requirement interpretation
   - Include a table with columns such as:
     - Requirement Area
     - Customer Requirement
     - UnifyApps Understanding
   - This table should be detailed and specific.

5. Operating model understanding
   - Explain stakeholders, workflow ownership, approvals, governance, risk management, data ownership, and integration dependencies where relevant.

6. Critical success factors
   - Explain what must be true for successful implementation.
   - Examples: confirmed scope, data readiness, integration access, security approvals, business ownership, UAT participation, and governance model alignment.

7. Assumptions and dependencies
   - Call out assumptions clearly.
   - Do not hide delivery dependencies.

This section should demonstrate strong reading comprehension. It should not be generic. It should use the customer's terminology and requirements where available.

Do not keep this section short unless the RFP/RFI itself is very small.

---

### 5. `{{FUNCTIONAL_CAPABILITY_RESPONSE}}`

This section should provide the structured functional response to the RFP/RFI requirements.

Recommended length:

- 3 to 10+ pages depending on requirement volume
- Use tables heavily
- Include direct answers to customer questions

Coverage required:

1. Functional introduction
   - Briefly summarize the functional scope being addressed.

2. Functional capability matrix
   - Include a table with columns such as:
     - Capability Area
     - Compliance Status
     - UnifyApps Response

3. Requirement-by-requirement response
   - If the RFP/RFI includes explicit questions, answer them one by one.
   - Use the customer's wording where possible.

4. Compliance status discipline
   - Use "Fully Compliant" only when the capability is clearly supported.
   - Use "Compliant with Configuration" when configuration is required.
   - Use "Compliant with Integration" when external systems, APIs, identity providers, LLMs, GRC tools, data platforms, or customer infrastructure are required.
   - Use "Requires Clarification" when the requirement is ambiguous.
   - Use "Not in Scope / Partner / Customer Dependency" where needed.

5. Safe implementation wording
   - For integrations, mention dependencies on API availability, credentials, environments, authentication, and customer security approvals.
   - For AI decisions, state that high-impact or regulated decisions should include human review.
   - For LLMs, default to customer-approved LLM or BYO LLM.

6. Differentiation
   - Explain where UnifyApps is strong: AI-native applications, workflow automation, agentic AI, connectors, LLM-agnostic approach, governed execution, RBAC, auditability, observability, human-in-the-loop controls, prompt-based creation/update, and enterprise integration.

7. Limitations and assumptions
   - Be honest about dependencies and non-native capabilities.
   - If a capability depends on integration with an external platform, say so.

Functional response should be clear, complete, and evaluator-friendly. It should not be just marketing text.

## Recommended Output Quality Standard

The completed response must:

- Address the actual customer requirement, not a generic UnifyApps pitch.
- Preserve all template headings and standard sections.
- Replace every placeholder exactly once.
- Remove the placeholder text from the final customer-ready document.
- Keep section titles and formatting intact.
- Keep images, tables, page styling, headers, footers, and standard sections intact.
- Avoid unsupported claims.
- Clearly state assumptions and dependencies.
- Be suitable for submission to an enterprise customer.

## Final Validation Checklist

Before finalizing the document, verify:

- `{{DOCUMENT_TITLE}}` is replaced.
- `{{EXECUTIVE_SUMMARY}}` is replaced.
- `{{OVERVIEW_PROPOSED_SOLUTION}}` is replaced.
- `{{UNDERSTANDING_OF_REQUIREMENTS}}` is replaced.
- `{{FUNCTIONAL_CAPABILITY_RESPONSE}}` is replaced.
- The section "Deployment and Security Model" and all following sections remain present.
- The standard sections were not rewritten unless explicitly requested.
- No old customer-specific content remains in the AI-generated sections.
- No accidental references to another customer remain.
- The response does not claim LLM inclusion unless explicitly requested.
- All compliance claims are defensible.
- The DOCX renders cleanly without broken layout, clipped tables, or missing images.
