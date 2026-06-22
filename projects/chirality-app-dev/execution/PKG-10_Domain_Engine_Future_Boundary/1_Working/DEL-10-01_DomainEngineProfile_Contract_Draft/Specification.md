# Specification: DEL-10-01 DomainEngineProfile Contract Draft

## Scope

This deliverable specifies a future-boundary draft for `DomainEngineProfile`: profile identity,
integration level, domain artifact roles, protected and agent-writable paths, deterministic tools,
operation-proposal contract hooks, and professional-boundary notices.

In scope:

- Future `DomainEngineProfile` documentation contract conforming to framework-root
  `agents/AGENT_DOMAIN_ENGINE.md` at commit `77a327727`.
- App-dev vocabulary alignment in `docs/TYPES.md` §11.
- Validation notes for deterministic profile acceptance.
- Future amendment checklist for accepting concrete profile instances after core harness stability.

Out of scope:

- Current-release implementation of domain-engine endpoints, source types, MCP tools, or path hooks.
- Engine-specific integration, including OpenPipeStress-specific runtime assumptions.
- Direct writes to protected domain-engine model paths.
- Professional approval, code compliance, certification, sealing, authentication, external validation, or
  solver-truth claims.

Sources: `_CONTEXT.md`; `_REFERENCES.md` REF-008; `agents/AGENT_DOMAIN_ENGINE.md` pinned at
`77a327727`; `docs/CONTRACT.md` §1.10; `docs/TYPES.md` §11; `docs/SPEC.md` §18; `docs/PRD.md` §8.17.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| DEL-10-01-REQ-001 | The contract draft MUST preserve `ResponsibleParty: TBD` until human assignment. | Inspect document identification sections. |
| DEL-10-01-REQ-002 | The contract draft MUST state that PKG-10 is future-boundary/gated scope, not current implementation. | Inspect Scope, Conditions, and Procedure gate checks. |
| DEL-10-01-REQ-003 | A generic `DomainEngineProfile` contract MUST precede any engine-specific integration. | Confirm no OpenPipeStress-specific runtime assumptions are embedded in the generic profile contract. |
| DEL-10-01-REQ-004 | A future `DomainEngineProfile` MUST include canonical identity, status, integration-level, path-role, deterministic-tool, operation-proposal-contract, and professional-boundary fields from framework `AGENT_DOMAIN_ENGINE.md` at `77a327727`. | Validate field list against `docs/TYPES.md` §11.1 and `_REFERENCES.md` REF-008. |
| DEL-10-01-REQ-005 | `profile_status` MUST use `NONE | DRAFT | VALIDATED | ADOPTED | STALE | INVALID | UNKNOWN`; integrated workflows require `ADOPTED`, while `MANUAL_BRIDGE` may explicitly record no adopted profile. | Inspect `docs/TYPES.md` §11.1 and future profile records. |
| DEL-10-01-REQ-006 | `integration_level` MUST use `MANUAL_BRIDGE | READ_ONLY | DOMAIN_CONTROLLED_WRITE | OPERATION_PROPOSAL | EXTERNAL_RESULT_STATE` and MUST NOT skip levels. | Inspect profile documentation and future amendment packets. |
| DEL-10-01-REQ-007 | Protected domain paths MUST be write-quarantined, and agent writes MUST be limited to profile-approved `agent_writable_paths`. | Future path policy separates authoritative/readable/protected/agent-writable path roles. |
| DEL-10-01-REQ-008 | Declared deterministic tools MUST include `id`, `mode`, `requires_human_confirmation`, `validate_result_schema`, and `apply_result_schema`; missing schema refs remain explicit `TBD`, not inferred. | Inspect deterministic-tool records and validation notes. |
| DEL-10-01-REQ-009 | The profile MUST carry an `operation_proposal_contract` covering lifecycle, risk classes, deterministic-check result schema, and accepted/applied requirements. | Inspect profile contract section and DEL-10-03 alignment. |
| DEL-10-01-REQ-010 | Applying a domain operation MUST require explicit human acceptance bound to K-AUTH-2 evidence and domain-engine-controlled apply or external terminal acceptance records. | Future operation workflow links application to the human gate and accepted/applied requirements. |
| DEL-10-01-REQ-011 | Boundary notices MUST state that Chirality does not approve, certify, seal, code-validate, externally validate, or own solver truth. | Review `professional_boundary` copy in future profile instances. |

## Standards

| Source | Applicable authority | Notes |
|---|---|---|
| `agents/AGENT_DOMAIN_ENGINE.md` at `77a327727` | Canonical domain-engine persona, minimal profile shape, and profile/proposal governance | REF-008; framework-root canonical under D-T0-01. |
| `docs/CONTRACT.md` §1.10 | App-dev K-DOMAIN invariants specializing framework K-DOMAIN without weakening them | Governs truth ownership, path quarantine, operation proposals, and professional boundary. |
| `docs/SPEC.md` §18 | Future specification boundary and candidate endpoint families | Candidate endpoints are provisional and must not be implemented as current-release scope. |
| `docs/TYPES.md` §11 | App-dev vocabulary target conforming to framework canon | Documents profile/proposal vocabulary only; it does not create source types. |
| `docs/PRD.md` §8.17 | Product requirements FR-106 through FR-115 | Current authority-corpus references are reconciled by D-APP-38. |
| `docs/PLAN.md` §R7 | Future amendment sequencing | Domain profiles come after core harness stability and human-gated R7 activation. |

## Verification

| Verification item | Method |
|---|---|
| Four-document completeness | Confirm `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present and non-empty. |
| Future-boundary preservation | Search for current-release implementation claims, source-type activation, MCP tool activation, path-hook implementation, or endpoint activation language; none should be present. |
| Source grounding | Check each non-trivial requirement against cited source sections and REF-008. |
| Canon conformance | Confirm the profile contract includes ProfileStatus, IntegrationLevel, role-classed paths, deterministic-tool schema hooks, operation-proposal contract, and structured professional boundary. |
| True TBD preservation | Confirm concrete profile instances, concrete result schema refs, adapter implementations, stores, and apply tooling remain `TBD` until a governed amendment accepts them. |
| Cross-document consistency | Confirm terminology uses `DomainEngineProfile`, `ProfileStatus`, `IntegrationLevel`, protected path, agent-writable path, deterministic tool, OperationProposal, and boundary notice consistently. |
| Future profile-instance review data | When concrete profile fixtures exist, review instance-level `professional_boundary` copy and profile values rather than relying only on the generic illustrative skeleton. |
| Status policy | Do not change `_STATUS.md` in this conformance tranche; `CHECKING -> ISSUED` remains out of scope. |

## Documentation

Required artifacts for this deliverable:

- Profile schema draft: this specification and the canonical shape recorded in `Datasheet.md`.
- Validation notes: deterministic validation requirements and true future implementation `TBD` schema refs.
- Future amendment checklist: operationalized in `Procedure.md`.

Existing dependency registers are not changed by this conformance tranche.
