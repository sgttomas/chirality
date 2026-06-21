# Datasheet: DEL-01-03 Product Identity and Professional Boundary Copy

## Identification

| Field | Value |
|---|---|
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| PackageID | PKG-01 |
| PackageName | Product Governance and Reliance Boundaries |
| DeliverableID | DEL-01-03 |
| DeliverableName | Product Identity and Professional Boundary Copy |
| ResponsibleParty | TBD |
| Type | DOC_UPDATE |
| ContextEnvelope | S |
| Current lifecycle state | CHECKING (drafted earlier at `OPEN`; inspection transition recorded in `_STATUS.md`) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary product identity | Chirality desktop harness and bundled agent operating system | `docs/DIRECTIVE.md` header; `docs/PRD.md` header |
| Product posture | Local-first governed desktop harness for running AI agents against a user-selected filesystem workspace | `docs/DIRECTIVE.md` Section 1; `docs/PRD.md` Section 2 |
| Identity boundary | User-facing text must identify the product as Chirality, not Claude Code, Anthropic, a vendor CLI, or a feature-parity target | `docs/DIRECTIVE.md` Section 2.11; `docs/CONTRACT.md` K-SDK-4; `docs/PRD.md` Section 3.2 |
| Professional authority posture | Agents propose; humans approve and retain binding decision rights | `docs/DIRECTIVE.md` Section 3; `docs/CONTRACT.md` K-AUTH-1 through K-GATE-1 |
| Draft status of agent outputs | Agent outputs are drafts and decision support until accepted by an accountable human | `docs/DIRECTIVE.md` Section 3.1 and Section 3.4; `docs/PRD.md` Section 2 |
| Reliance-boundary posture | Product-critical boundaries must be documented, implemented, and tested in Chirality terms; prompt text alone is insufficient | `docs/DIRECTIVE.md` Section 2.9; `docs/CONTRACT.md` K-RELIANCE-1 and K-RELIANCE-2 |
| Domain-engine boundary posture | Domain engines own domain truth; Chirality governs interaction, proposals, records, and human gates | `docs/CONTRACT.md` K-DOMAIN-1 through K-DOMAIN-4; `docs/SPEC.md` Section 18 |

## Conditions

| Condition | Required treatment | Source |
|---|---|---|
| UI, documentation, packaging, runtime messages, and future domain notices mention the product | Use Chirality-owned product language; do not imply the product is Claude Code or an Anthropic product | `_CONTEXT.md` Deliverable Scope; `docs/DIRECTIVE.md` Section 2.11; `docs/PRD.md` FR-127 |
| Agent output, runtime event, validator result, SDK transcript, or domain-adapter output is presented to a user | Preserve draft/non-binding wording unless a human approval record exists | `docs/DIRECTIVE.md` Sections 2.3 and 3; `docs/CONTRACT.md` K-BIND-1 |
| Copy refers to approval, certification, code compliance, external validation, issuance, signature, seal, transmittal, or release for reliance | Reserve the action for accountable humans; do not attribute it to Chirality, agents, SDKs, tools, validators, runtime events, or domain adapters | `docs/DIRECTIVE.md` Section 3.2; `docs/CONTRACT.md` K-AUTH-1 and K-PROF-1 |
| Copy refers to SDK integration | Describe SDK use as implementation/provider detail behind Chirality-owned contracts, not as product identity or governance authority | `docs/DIRECTIVE.md` Sections 2.8 and 2.11; `docs/CONTRACT.md` K-ENGINE-3 |
| Copy refers to future domain engines | State that domain-operation acceptance is human-gated and domain outputs are not Chirality-owned solver truth | `docs/PRD.md` Section 8.17; `docs/SPEC.md` Section 18 |

## Construction

The deliverable is a documentation and copy-boundary package. Anticipated artifacts from `_CONTEXT.md` are:

- UI copy guidelines.
- Release review checklist.
- Boundary notice examples.

ASSUMPTION: These artifacts may be implemented as sections or downstream documents, but no final target file paths are specified in the available sources. Target file paths remain TBD until a human or later deliverable assigns them.

| Artifact | Current location in this deliverable | Final destination path | Source |
|---|---|---|---|
| UI copy guidelines | `Guidance.md` Principles, Considerations, Trade-offs, and Examples | TBD | `_CONTEXT.md` Anticipated Artifacts; decomposition DEL-01-03 AnticipatedArtifacts |
| Release review checklist | `Procedure.md` Verification and Release Review Evidence Template | TBD | `_CONTEXT.md` Anticipated Artifacts; `docs/DIRECTIVE.md` Sections 2.4 and 3.2 |
| Boundary notice examples | `Guidance.md` Examples | TBD | `_CONTEXT.md` Anticipated Artifacts; `docs/CONTRACT.md` K-AUTH-1 and K-DOMAIN-4 |
| Review notes | `Procedure.md` Review Note Record Template | TBD | `docs/DIRECTIVE.md` Section 2.5; `docs/CONTRACT.md` K-INVENT-1 and K-CONFLICT-1 |

## References

| RefID | Source | Use |
|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Founding intent, product identity, professional responsibility, evidence posture |
| REF-002 | `docs/CONTRACT.md` | Binding invariants for authority, identity, reliance boundaries, domain boundaries |
| REF-003 | `docs/SPEC.md` | Physical structures, persona composer professional-boundary reminders, domain future boundary |
| REF-004 | `docs/TYPES.md` | Stable identifiers, project truth, artifact vocabulary, human approval authority |
| REF-005 | `docs/PLAN.md` | Product identity and release/local-check posture |
| REF-006 | `docs/PRD.md` | Product requirements and accepted vNext runtime direction; D-APP-38 corpus `v1` records a matching authority-doc hash |
| REF-007 | `/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md` | Decomposition method context; no copy requirements extracted |
