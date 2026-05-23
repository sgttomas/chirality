# Specification: DEL-10-01 DomainEngineProfile Contract Draft

## Scope

This deliverable specifies a future-boundary draft for `DomainEngineProfile`: engine identity, protected paths, proposal paths, operations, manifests, and boundary notices.

In scope:

- Future `DomainEngineProfile` field contract.
- Validation notes for deterministic profile acceptance.
- Future amendment checklist for accepting the profile contract after core harness stability.

Out of scope:

- Current-release implementation of domain-engine endpoints or tools.
- Engine-specific integration, including OpenPipeStress-specific assumptions.
- Direct writes to protected domain-engine model paths.
- Professional approval, code compliance, external validation, or solver-truth claims.

Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §PKG-10; `docs/SPEC.md` §18; `docs/PRD.md` §8.17.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| DEL-10-01-REQ-001 | The contract draft MUST preserve `ResponsibleParty: TBD` until human assignment. | Inspect document identification sections. |
| DEL-10-01-REQ-002 | The contract draft MUST state that PKG-10 is future-boundary/gated scope, not current implementation. | Inspect Scope, Conditions, and Procedure gate checks. |
| DEL-10-01-REQ-003 | A generic `DomainEngineProfile` contract MUST precede any engine-specific integration. | Confirm no OpenPipeStress-specific assumptions are embedded in the generic profile contract. Source: `docs/PRD.md` §8.17 FR-107, FR-114. |
| DEL-10-01-REQ-004 | A future `DomainEngineProfile` MUST include engine identity, optional version, protected paths, proposal paths, artifact types, operations, manifest rules, and boundary notices. | Validate field list against `docs/TYPES.md` §11.1 and `docs/PRD.md` §8.17 FR-108. |
| DEL-10-01-REQ-005 | Domain profile validation MUST be deterministic before runtime exposure. | Future validator fails invalid or incomplete profiles before exposing them to runtime. Source: `docs/PRD.md` §8.17 FR-109. |
| DEL-10-01-REQ-006 | Protected domain paths MUST be write-quarantined. | Future path policy separates protected paths from proposal paths. Source: `docs/CONTRACT.md` §1.10 K-DOMAIN-2; `docs/PRD.md` §8.17 FR-110. |
| DEL-10-01-REQ-007 | Agents MUST write proposals, summaries, and review aids rather than protected domain-engine model truth. | Future profile/policy review confirms agent-writable paths are proposal paths only. Source: `docs/PRD.md` §8.17 FR-111. |
| DEL-10-01-REQ-008 | Applying a domain operation MUST require explicit human acceptance. | Future operation workflow links application to human gate. Source: `docs/SPEC.md` §18; `docs/PRD.md` §8.17 FR-113. |
| DEL-10-01-REQ-009 | Boundary notices MUST state that Chirality does not approve, validate, or own solver truth. | Review `boundaryNotice` copy in future profile instances. Source: `docs/CONTRACT.md` §1.10 K-DOMAIN-4; `docs/PRD.md` §8.17 FR-115. |
| DEL-10-01-REQ-010 | `DomainEngineOperationDescriptor` shape is TBD until an authoritative source defines it. | Confirm descriptor fields are not invented in this draft. Source: `docs/TYPES.md` §11.1. |
| DEL-10-01-REQ-011 | `manifestRules` schema is TBD until an authoritative source constrains the `unknown` type. | Confirm manifest schema is not over-specified. Source: `docs/TYPES.md` §11.1. |

## Standards

| Source | Applicable authority | Notes |
|---|---|---|
| `docs/CONTRACT.md` §1.10 | Domain-engine invariants K-DOMAIN-1 through K-DOMAIN-4 | Governs truth ownership, path quarantine, operation proposals, and professional boundary. |
| `docs/SPEC.md` §18 | Future specification boundary and candidate endpoint families | Candidate endpoints are provisional and must not be implemented as current-release scope. |
| `docs/TYPES.md` §11 | Future domain-engine vocabulary and interface targets | Defines `DomainEngineProfile` and `OperationProposal`; references undefined `DomainEngineOperationDescriptor`. |
| `docs/PRD.md` §8.17 | Product requirements FR-106 through FR-115 | Source warning: PRD hash mismatch recorded in `_REFERENCES.md`; treated as source warning only per dispatch. |
| `docs/PLAN.md` §R7 | Future amendment sequencing | Domain profiles come after core harness stability. |

## Verification

| Verification item | Method |
|---|---|
| Four-document completeness | Confirm `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present and non-empty. |
| Future-boundary preservation | Search for current-release implementation claims or endpoint activation language; none should be present. |
| Source grounding | Check each non-trivial requirement against cited source sections. |
| Unknown preservation | Confirm descriptor and manifest details remain `TBD` where sources do not define them. |
| Cross-document consistency | Confirm terminology uses `DomainEngineProfile`, protected path, proposal path, deterministic adapter, boundary notice, and OperationProposal consistently. |
| Status transition | Set `_STATUS.md` to `INITIALIZED` only after all four documents are non-empty. |

## Documentation

Required artifacts for this deliverable:

- Profile schema draft: this specification and the TypeScript shape recorded in `Datasheet.md`.
- Validation notes: deterministic validation requirements and TBD schema gaps recorded here.
- Future amendment checklist: operationalized in `Procedure.md`.

No `Dependencies.csv` is produced by this deliverable run.
