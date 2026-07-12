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

- Copy can disclose SDK usage when it improves transparency, diagnostics, implementation context, or release evidence. It risks product-identity drift when the SDK brand becomes the subject of the product claim, appears to own governance semantics, or makes Chirality look like Claude Code, an Anthropic product, a vendor CLI, or a feature-parity target.
- Professional-boundary copy should be visible where a user could confuse output generation, validation, event logging, or domain-engine results with approval.
- Release review should include UI labels, empty states, permission prompts, status-transition messages, runtime/session summaries, documentation, packaging metadata, and domain-engine future notices. The checked-surface inventory for a given release remains TBD until the release owner identifies the affected surfaces.
- ASSUMPTION: "Boundary notice examples" will be used as reusable copy snippets, not as a substitute for implementation enforcement. This is inferred from the deliverable scope and the reliance-boundary requirements.

## Trade-offs

| Trade-off | Preferred posture |
|---|---|
| Transparent SDK disclosure vs. product identity drift | Disclose SDK use where appropriate, but keep Chirality as the product and contract owner. |
| Concise UI copy vs. professional-boundary clarity | Use concise language, but do not remove human-review and non-binding qualifiers where reliance confusion is plausible. For very short UI strings, pair concise labels with nearby help text, tooltip text, empty-state copy, or release notes when the label alone cannot carry the boundary without becoming misleading. |
| Friendly automation language vs. authority confusion | Prefer "helps draft", "organizes", "records", "checks", and "proposes" over "approves", "certifies", "issues", or "validates for reliance". |
| Future domain-engine capability vs. current scope | Present domain engines as future-boundary scope until governed amendment and implementation evidence exist. |

## Term Normalization

| Term | Copy treatment | Source basis |
|---|---|---|
| Draft | Non-binding working output that requires accountable human acceptance before reliance. | `docs/DIRECTIVE.md` Section 3.1; `docs/CONTRACT.md` K-BIND-1 |
| Proposal | A suggested change, operation, or copy treatment requiring review or acceptance. | `docs/DIRECTIVE.md` Section 2.4; `docs/CONTRACT.md` K-GATE-1 |
| Decision support | Assistance that informs judgment but does not replace accountable human decision rights. | `docs/DIRECTIVE.md` Section 3.4 |
| Summary | Non-authoritative condensation unless imported into governed project files and accepted. | `docs/DIRECTIVE.md` Sections 2.5 and 2.6 |
| Transcript | Runtime or SDK record used for diagnosis/review, not an approval record. | `docs/DIRECTIVE.md` Section 2.3; `docs/CONTRACT.md` K-SDK-3 |
| Runtime event | Audit evidence of what happened during a turn; not approval, issuance, code compliance, external validation, or reliance clearance. | `docs/DIRECTIVE.md` Section 2.3 |
| Validator result | Deterministic check evidence; not professional approval or external validation. | `docs/DIRECTIVE.md` Sections 2.4 and 3.2; `docs/CONTRACT.md` K-AUTH-1 |
| Approval record | Human-authored binding evidence tied to specific content, normally a git SHA. | `docs/DIRECTIVE.md` Section 2.4; `docs/CONTRACT.md` K-AUTH-2 |

Validators and runtime events cannot be treated as external validation or approval records because the sources separate evidence from human authority. They can show what was checked or what happened, but gate-relevant decisions still require versioned project files and accountable human acceptance.

## Examples

Acceptable examples, grounded in source posture:

| Context | Example copy | Source basis |
|---|---|---|
| Product description | "Chirality is a governed desktop harness for AI-assisted project work over local files." | `docs/DIRECTIVE.md` Section 1 |
| Draft output notice | "This output is draft assistance. An accountable human must review and accept it before reliance." | `docs/DIRECTIVE.md` Section 3.1 |
| SDK disclosure | "This runtime may use an SDK-backed engine behind Chirality-owned contracts and audit records." | `docs/DIRECTIVE.md` Sections 2.8 and 2.10 |
| Runtime event notice | "Runtime events record what happened during the turn; they are not approval records." | `docs/DIRECTIVE.md` Section 2.3 |
| Domain notice | "Domain-engine results require human review and do not represent Chirality-owned solver truth or professional approval." | `docs/CONTRACT.md` K-DOMAIN-4; `docs/PRD.md` FR-115 |
| Validator result notice | "This validator result is check evidence, not external validation or professional approval." | `docs/DIRECTIVE.md` Sections 2.4 and 3.2; `docs/CONTRACT.md` K-AUTH-1 |

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

Closed historical conflict: `CT-002` is superseded by the current D-APP-38 corpus snapshot; current `_REFERENCES.md`
records REF-006 `docs/PRD.md` as `MATCH`.

## Normalized Checklist Artifact

ADQ-03 materialized `docs/BOUNDARY_REVIEW_CHECKLISTS.md` as the shared professional-boundary and
scope-boundary checklist package. For DEL-01-03, that file supplies the UI copy review checklist,
release review evidence template, boundary notice examples, and finding template. It is CHECKING-stage
review evidence only; it does not assign `ResponsibleParty`, satisfy dependencies, issue this
deliverable, or approve release/professional reliance.
