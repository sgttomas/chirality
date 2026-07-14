# Procedure: DEL-10-01 DomainEngineProfile Contract Draft

## Purpose

Define the bounded procedure for maintaining the future `DomainEngineProfile` contract draft while preserving the F3 domain-engine implementation fence.

## Prerequisites

| Prerequisite | Status |
|---|---|
| Deliverable-local context is present. | Satisfied: `_CONTEXT.md` exists. |
| Authoritative references are accessible. | Satisfied: `_REFERENCES.md` includes REF-008 for framework `AGENT_DOMAIN_ENGINE.md` pinned at `77a327727`. |
| Framework precedence is known. | Satisfied: D-T0-01 makes framework-root `AGENT_DOMAIN_ENGINE.md` canonical; app-dev `docs/TYPES.md` Section 11 conforms to it. |
| Current status posture is preserved. | Required: read current state from `_STATUS.md`; this tranche performs no lifecycle transition or release-readiness act. |
| Current scope remains future-boundary. | Required by `docs/SPEC.md` Section 18, `docs/PLAN.md` R7, and D-APP-39 F3. |

## Steps

1. Confirm identity from `_CONTEXT.md`.
   - DeliverableID: DEL-10-01.
   - ResponsibleParty: TBD.
   - Type: API_CONTRACT.
   - Scope: future profile contract for engine identity, integration level, path/artifact roles, deterministic tools, operation-proposal contract, and professional boundary.

2. Confirm source posture from `_REFERENCES.md`.
   - Use REF-008 as the canonical persona/profile source.
   - Use app-dev `docs/TYPES.md` Section 11 only as the local vocabulary target conforming to REF-008.
   - Do not create `Dependencies.csv`.

3. Read source slices for the domain-engine future boundary.
   - `agents/AGENT_DOMAIN_ENGINE.md` at `77a327727` for Minimal Profile Shape, valid operation proposal table, lifecycle, and `operation_proposal_contract`.
   - `docs/CONTRACT.md` Section 1.10 for app-dev K-DOMAIN invariants, which specialize framework `docs/CONTRACT.md` Section 1.12 without weakening it.
   - `docs/SPEC.md` Section 18 for provisional future endpoint/tool boundary.
   - `docs/TYPES.md` Section 11 for app-dev vocabulary.
   - `docs/PLAN.md` R7 for future-amendment sequencing.
   - `docs/PRD.md` Section 8.17 for FR-106 through FR-115.
   - Decomposition PKG-10 / DEL-10-01 entry for local scope.

4. Draft or maintain the profile contract.
   - Preserve canonical identity fields: `schema_version`, `id`, `name`, `engine_type`, and `profile_version`.
   - Preserve canonical `ProfileStatus`: `NONE | DRAFT | VALIDATED | ADOPTED | STALE | INVALID | UNKNOWN`.
   - Preserve canonical `IntegrationLevel`: `MANUAL_BRIDGE | READ_ONLY | DOMAIN_CONTROLLED_WRITE | OPERATION_PROPOSAL | EXTERNAL_RESULT_STATE`.
   - Preserve path/artifact role fields: `domain_root_patterns`, `authoritative_artifacts`, `chirality_readable_artifacts`, `protected_write_paths`, and `agent_writable_paths`.
   - Preserve deterministic tool fields, including `validate_result_schema` and `apply_result_schema`.
   - Preserve `operation_proposal_contract`, including lifecycle, risk classes, deterministic-check result schema, and accepted/applied requirements.
   - Preserve structured `professional_boundary`.

5. Mark only true future implementation details as `TBD`.
   - Concrete profile instances.
   - Concrete schema refs for validation/apply/deterministic-check results.
   - Adapters, MCP tools, stores, endpoint handlers, protected-path hooks, and apply tooling.
   - Concrete boundary notice copy for each accepted profile instance.

6. Preserve future-boundary constraints.
   - Do not implement candidate endpoints.
   - Do not define executable tool behavior.
   - Do not authorize direct protected-path writes.
   - Do not represent domain output as professional approval, code compliance, certification, sealing, authentication, external validation, or Chirality-owned solver truth.

7. Cross-check documents.
   - Confirm `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` use consistent canonical terms.
   - Confirm DEL-10-03 uses the same lifecycle and proposal contract fields.
   - Confirm old compact-draft blockers are not reintroduced as unresolved human-ruling blockers.

8. Record the run without lifecycle transition.
   - Keep `_STATUS.md` unchanged.
   - Record conformance notes in `MEMORY.md` and coordination closeout.
   - Let D-APP-38 reconciliation update authority-corpus hashes after authority-doc edits.

## Verification

| Check | Expected result |
|---|---|
| Four document files | Present and non-empty. |
| Status state | Current state is read from `_STATUS.md`; no lifecycle transition is claimed. |
| Responsible party | Remains `TBD`. |
| Canon conformance | Profile vocabulary includes REF-008 identity, status, integration, path role, deterministic-tool, operation-proposal, and professional-boundary fields. |
| True TBD posture | Concrete profiles, concrete schema refs, adapters, stores, path hooks, and apply tooling remain `TBD`. |
| Dependency register | Existing `Dependencies.csv` remains separate derivative evidence and is not created or edited by this conformance tranche. |
| Implementation activation | No domain-engine source type, endpoint, MCP tool, adapter, operation store, apply workflow, or protected-path write implementation is activated. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `MEMORY.md`
- `_STATUS.md`
- D-APP-45 closeout packet
