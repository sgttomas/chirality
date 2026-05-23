# Guidance: DEL-01-03 Product Identity and Professional Boundary Copy

## Purpose

This deliverable gives product and release writers a conservative boundary for Chirality copy. Its purpose is to preserve Chirality identity and human-only professional authority across UI, documentation, packaging, runtime messages, and future domain notices.

The governing posture is:

- Chirality is a governed desktop harness, not a vendor CLI wrapper.
- The SDK may be privileged as implementation substrate, but Chirality owns product semantics, runtime contracts, audit posture, permission policy, professional-boundary language, and user-facing product identity.
- Agents, tools, SDKs, validators, transcripts, and runtime events assist; accountable humans decide what can be relied upon.

Sources: `docs/DIRECTIVE.md` Sections 1, 2.8, 2.11, and 3; `docs/CONTRACT.md` K-AUTH-1, K-ENGINE-3, K-SDK-4.

## Principles

| Principle | Guidance | Source |
|---|---|---|
| Name Chirality first | Use "Chirality" for product identity. Mention external SDK/provider details only when useful and only as implementation detail. | `docs/DIRECTIVE.md` Section 2.11 |
| Keep assistance non-binding | Prefer "draft", "proposal", "decision support", "review", "evidence", and "human acceptance" over "approved", "certified", "issued", or "validated" unless referring to a human approval record. | `docs/DIRECTIVE.md` Section 3; `docs/CONTRACT.md` K-BIND-1 |
| Preserve human gates | Copy should make clear that humans approve reliance-affecting transitions, release actions, issue actions, residual risk, and professional judgments. | `docs/DIRECTIVE.md` Section 3.2; `docs/CONTRACT.md` K-GATE-1 |
| Avoid prompt-only safety claims | Do not describe prompt text, model instruction, or SDK default behavior as sufficient enforcement for product-critical boundaries. | `docs/DIRECTIVE.md` Section 2.9; `docs/CONTRACT.md` K-RELIANCE-2 |
| Separate runtime evidence from approval | Runtime events and transcripts explain what happened; they do not approve work. | `docs/DIRECTIVE.md` Section 2.3; `docs/CONTRACT.md` K-BIND-1 |
| Keep domain truth separate | Future domain-engine copy should distinguish Chirality interaction governance from domain-engine truth and professional review. | `docs/CONTRACT.md` K-DOMAIN-1 through K-DOMAIN-4 |

## Considerations

- Copy can disclose SDK usage, but should avoid centering SDK brand names in product-facing identity surfaces unless needed for transparency, diagnostics, or implementation context.
- Professional-boundary copy should be visible where a user could confuse output generation, validation, event logging, or domain-engine results with approval.
- Release review should include UI labels, empty states, permission prompts, status-transition messages, runtime/session summaries, documentation, packaging metadata, and domain-engine future notices.
- ASSUMPTION: "Boundary notice examples" will be used as reusable copy snippets, not as a substitute for implementation enforcement. This is inferred from the deliverable scope and the reliance-boundary requirements.

## Trade-offs

| Trade-off | Preferred posture |
|---|---|
| Transparent SDK disclosure vs. product identity drift | Disclose SDK use where appropriate, but keep Chirality as the product and contract owner. |
| Concise UI copy vs. professional-boundary clarity | Use concise language, but do not remove human-review and non-binding qualifiers where reliance confusion is plausible. |
| Friendly automation language vs. authority confusion | Prefer "helps draft", "organizes", "records", "checks", and "proposes" over "approves", "certifies", "issues", or "validates for reliance". |
| Future domain-engine capability vs. current scope | Present domain engines as future-boundary scope until governed amendment and implementation evidence exist. |

## Examples

Acceptable examples, grounded in source posture:

| Context | Example copy | Source basis |
|---|---|---|
| Product description | "Chirality is a governed desktop harness for AI-assisted project work over local files." | `docs/DIRECTIVE.md` Section 1 |
| Draft output notice | "This output is draft assistance. An accountable human must review and accept it before reliance." | `docs/DIRECTIVE.md` Section 3.1 |
| SDK disclosure | "This runtime may use an SDK-backed engine behind Chirality-owned contracts and audit records." | `docs/DIRECTIVE.md` Sections 2.8 and 2.10 |
| Runtime event notice | "Runtime events record what happened during the turn; they are not approval records." | `docs/DIRECTIVE.md` Section 2.3 |
| Domain notice | "Domain-engine results require human review and do not represent Chirality-owned solver truth or professional approval." | `docs/CONTRACT.md` K-DOMAIN-4; `docs/PRD.md` FR-115 |

Avoid examples:

| Context | Avoid | Reason |
|---|---|---|
| Product identity | "Chirality is Claude Code for professional workflows." | Violates product identity boundary. |
| Approval | "The agent approved this deliverable." | Violates human-only approval boundary. |
| Validation | "Chirality certifies this result as code-compliant." | Violates professional-boundary and domain-truth boundaries. |
| Reliance boundary | "The prompt prevents unsafe writes." | Prompt text alone is not a sufficient safety boundary. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-001 | Dispatch path used `PKG-01_Governance_and_Product_Boundaries`, but the matching folder on disk is `PKG-01_Product_Governance_and_Reliance_Boundaries`. | User dispatch path | `_CONTEXT.md` PackageName and actual folder path | Run record; final report | Treat actual matching DEL-01-03 folder as resolved scope; preserve stable PackageID/DeliverableID. | TBD |
| CT-002 | `docs/PRD.md` hash differs from `_REFERENCES.md` expected hash. | `_REFERENCES.md` REF-006 expected/actual hash | User dispatch override says mismatch is source warning, not blocker | All PRD-sourced requirements | Use PRD as accessible source with warning; do not treat mismatch as blocker. | TBD |

