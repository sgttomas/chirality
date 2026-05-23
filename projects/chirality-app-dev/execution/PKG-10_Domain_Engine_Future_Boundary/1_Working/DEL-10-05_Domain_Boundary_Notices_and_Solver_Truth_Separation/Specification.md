# Specification: DEL-10-05 Domain Boundary Notices and Solver Truth Separation

## Scope

This deliverable specifies boundary-notice and review requirements for future domain-engine surfaces in Chirality. It covers documentation/UI/event-record copy and review checks that preserve the distinction between:

- domain-engine authoritative truth,
- deterministic adapter or domain-tool outputs,
- Chirality proposals, summaries, manifests, and audit records,
- explicit human acceptance and professional reliance decisions.

This deliverable excludes activation or implementation of domain-engine endpoints, adapters, OpenPipeStress integration, protected-path mutation, or current-release domain operation execution. PKG-10 remains future-boundary/gated scope under decomposition OI-005 and DEC-006.

## Requirements

| ID | Requirement | Source | Verification |
|---|---|---|---|
| REQ-001 | Boundary notices MUST state that Chirality does not approve, validate, certify, issue, sign, seal, or externally validate professional work. | `docs/DIRECTIVE.md` Sections 2.4, 3.2; `docs/CONTRACT.md` K-AUTH-1 | Copy review confirms no automated approval/validation claim. |
| REQ-002 | Boundary notices MUST state that Chirality does not own solver truth and does not become the domain solver. | `docs/PRD.md` FR-106, FR-115; `docs/CONTRACT.md` K-DOMAIN-1, K-DOMAIN-4 | Copy review confirms solver-truth ownership is assigned to the domain engine/domain tool, not Chirality. |
| REQ-003 | UI/documentation/event copy MUST NOT represent domain-engine output as professional approval, code compliance, external validation, or Chirality-owned solver truth. | `docs/PRD.md` FR-115; decomposition SOW-071 | Checklist review flags prohibited claims. |
| REQ-004 | Domain operation copy MUST require explicit human acceptance before any applied operation is treated as accepted domain state. | `docs/PRD.md` FR-113; `docs/CONTRACT.md` K-DOMAIN-3 and K-GATE-1 | Operation-related copy includes human-gate language. |
| REQ-005 | Protected domain artifact copy MUST distinguish protected paths from agent-writable proposal or summary paths. | `docs/PRD.md` FR-110, FR-111; `docs/CONTRACT.md` K-DOMAIN-2; `docs/TYPES.md` Section 11.3 | Review confirms no direct agent-write language for protected model truth. |
| REQ-006 | OpenPipeStress examples, if used, MUST describe it as a possible fixture profile and not as Chirality core behavior. | `docs/PRD.md` FR-114; `docs/TYPES.md` Section 11.3 | Example review confirms fixture-only language. |
| REQ-007 | Any current-release mention of domain-engine endpoints or tools MUST be marked future/provisional and MUST NOT imply implementation is active. | `docs/SPEC.md` Section 18; `docs/PRD.md` KG-016; decomposition OI-005 | Scope review confirms future-boundary/gated wording. |
| REQ-008 | Unsupported domain-profile or solver-specific details MUST remain `TBD`, `ASSUMPTION`, `PROPOSAL`, or a human-ruling item. | Skill contract; `_REFERENCES.md` notes | Document review confirms no invented solver facts. |

## Standards

No external engineering code or domain-solver standard is selected by this deliverable. Governing project standards for this slice are the Chirality governance and product documents listed in `_REFERENCES.md`.

| Standard/Control | Status |
|---|---|
| Chirality professional-boundary invariants | Applicable from `docs/DIRECTIVE.md` and `docs/CONTRACT.md` |
| Chirality domain-engine future requirements | Applicable from `docs/PRD.md` FR-106 through FR-115 |
| DomainEngineProfile accepted schema | TBD: no accepted generic profile specification exists yet per `docs/PRD.md` KG-017 |
| Engine-specific solver validation standards | TBD: out of scope until a future amendment and domain profile identify the engine and governing standards |

## Verification

| Check | Pass Criteria |
|---|---|
| Prohibited claim scan | No copy says or implies Chirality approves, validates, certifies, issues, signs, seals, proves code compliance, externally validates, or owns solver truth. |
| Ownership separation scan | Domain-engine/tool outputs, Chirality records, and human acceptance are separately named. |
| Scope gate scan | Domain-engine operation execution remains future-boundary/gated scope. |
| Protected/proposal path scan | Protected domain paths are not described as agent-writable; proposal/review aid paths are distinct. |
| Fixture scan | OpenPipeStress is fixture/profile language only, not core runtime behavior. |
| Unsupported fact scan | Missing solver/profile specifics are marked TBD, ASSUMPTION, PROPOSAL, or human-ruling items. |

## Documentation

This deliverable produces and maintains:

- Boundary notice copy.
- Domain review checklist.
- UI/documentation examples.
- Human-ruling list for unresolved future-amendment details.
- Source-warning note for the PRD hash mismatch recorded in `_REFERENCES.md`.
