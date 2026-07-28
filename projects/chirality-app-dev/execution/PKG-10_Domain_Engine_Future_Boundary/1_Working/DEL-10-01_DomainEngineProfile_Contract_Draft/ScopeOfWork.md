---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-10-01
package_id: PKG-10
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@7b0be4d8772a16e5a4774a17988479587d00acca
project_scope_refs: [SOW-066, SOW-067]
package_objective_refs: [OBJ-010]
---

# Scope of Work — DEL-10-01

## Purpose and Objective Traceability

This Scope of Work defines `DEL-10-01` in service of project scope [SOW-066, SOW-067] and package objectives [OBJ-010].

- **OUT-001** — The DEL-10-01 future-boundary generic DomainEngineProfile contract draft, comprising a profile schema draft, validation notes, and a future amendment checklist, while preserving future compatibility without immediate runtime implementation.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-10-01 DomainEngineProfile Contract Draft

> #### Datasheet: DEL-10-01 DomainEngineProfile Contract Draft
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DeliverableID | DEL-10-01 |
> | DeliverableName | DomainEngineProfile Contract Draft |
> | PackageID | PKG-10 |
> | PackageName | Domain Engine Future Boundary |
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | Type | API_CONTRACT |
> | ResponsibleParty | TBD |
> | ContextEnvelope | M |
> | Current posture | Future-boundary contract, not current implementation |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Contract subject | Future `DomainEngineProfile` profile contract conforming to framework-root canon at `77a327727`. | `_CONTEXT.md`; `_REFERENCES.md` REF-008; `docs/TYPES.md` §11.1 |
> | Canonical identity fields | `schema_version`, `id`, `name`, `engine_type`, `profile_version`. | `agents/AGENT_DOMAIN_ENGINE.md` REF-008; `docs/TYPES.md` §11.1 |
> | Profile lifecycle fields | `profile_status` using `NONE | DRAFT | VALIDATED | ADOPTED | STALE | INVALID | UNKNOWN`; `integration_level` using `MANUAL_BRIDGE | READ_ONLY | DOMAIN_CONTROLLED_WRITE | OPERATION_PROPOSAL | EXTERNAL_RESULT_STATE`. | `agents/AGENT_DOMAIN_ENGINE.md` REF-008; `docs/TYPES.md` §11.1 |
> | Path and artifact role fields | `domain_root_patterns`, `authoritative_artifacts`, `chirality_readable_artifacts`, `protected_write_paths`, `agent_writable_paths`. | `agents/AGENT_DOMAIN_ENGINE.md` REF-008; `docs/CONTRACT.md` §1.10 |
> | Tool contract fields | `deterministic_tools[].id`, `mode`, `requires_human_confirmation`, `validate_result_schema`, and `apply_result_schema`. | `agents/AGENT_DOMAIN_ENGINE.md` REF-008; `docs/TYPES.md` §11.1 |
> | Proposal contract field | `operation_proposal_contract` with lifecycle, risk classes, deterministic-check result schema, and accepted/applied requirements. | `agents/AGENT_DOMAIN_ENGINE.md` REF-008; `docs/TYPES.md` §11.1 |
> | Professional boundary field | Structured `professional_boundary.agent_must_not_claim` list. | `agents/AGENT_DOMAIN_ENGINE.md` REF-008; `docs/CONTRACT.md` §1.10 K-DOMAIN-4 |
> | True future TBDs | Concrete profile instances, concrete schema refs, adapter implementations, tool stores, operation stores, and apply tooling remain TBD until governed amendment. | `docs/PLAN.md` §R7; `docs/SPEC.md` §18 |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Value | Source |
> |---|---|---|
> | Release scope | D-APP-49 through D-APP-52 rule source types/guards, a closed registry, read tools, and pec-scoped loopback propose/refresh/validate tools live. Endpoints, apply, direct protected-path writes/hooks, and general domain-runtime activation remain future/gated. | `docs/SPEC.md` §18; D-APP-49 through D-APP-52 |
> | Sequencing | The ruled staged surface is live; any broader Domain Engine Profile or operation workflow proceeds only through its own governed amendment. | `docs/PLAN.md` §R7; `docs/PRD.md` §8.17 |
> | Engine-specific integration | A generic `DomainEngineProfile` contract precedes any engine-specific integration. | `docs/PRD.md` §8.17 FR-107 |
> | Protected path posture | Protected domain paths are write-quarantined; agents write proposals, summaries, and review aids only under profile-approved `agent_writable_paths`. | `docs/CONTRACT.md` §1.10 K-DOMAIN-2; REF-008 |
> | Human gate posture | Accepted/applied proposal transitions require human approval bound to git SHA per K-AUTH-2 and domain-engine-controlled apply or external terminal acceptance records. | `docs/CONTRACT.md` §1.10 K-DOMAIN-3; REF-008 |
> | Professional boundary | Domain-engine outputs must not be represented as professional approval, code compliance, certification, sealing, authentication, external validation, or solver truth owned by Chirality. | `docs/CONTRACT.md` §1.10 K-DOMAIN-4; REF-008 |
>

### CLM-005 — Construction

> ##### Construction
>

### CLM-006 — Canonical Profile Shape

> ###### Canonical Profile Shape
>
> ```yaml
> domain_profile:
>   schema_version: "1.0"
>   id: "<domain_engine_id>"
>   name: "<Domain Engine Name>"
>   engine_type: "<domain classification>"
>   profile_version: "0.1"
>   profile_status: "DRAFT"
>   integration_level: "MANUAL_BRIDGE"
>   domain_root_patterns:
>     - "<path or glob>"
>   authoritative_artifacts:
>     - "<engine-owned path or glob>"
>   chirality_readable_artifacts:
>     - "<manifest/summary/report path or glob>"
>   protected_write_paths:
>     - "<agent-prohibited path or glob>"
>   agent_writable_paths:
>     - "<proposal/review/checklist path or glob>"
>   deterministic_tools:
>     - id: "<tool.id>"
>       mode: "read_only"
>       requires_human_confirmation: false
>       validate_result_schema: "<schema ref or TBD>"
>       apply_result_schema: "<schema ref or TBD>"
>   operation_proposal_contract:
>     lifecycle: ["draft", "ready_for_review", "accepted", "rejected", "applied"]
>     risk_classes: ["engine_checkable", "engine_silent"]
>     deterministic_check_result_schema: "<schema ref or TBD>"
>     accepted_or_applied_requires:
>       - "human approval bound to git SHA per K-AUTH-2"
>       - "domain-engine-controlled apply or external terminal acceptance record"
>   professional_boundary:
>     agent_must_not_claim:
>       - "code compliant for reliance"
>       - "professionally approved"
>       - "externally validated"
> ```
>
> Source: `agents/AGENT_DOMAIN_ENGINE.md` pinned at `77a327727` and reflected in `docs/TYPES.md` §11.1.
>

### CLM-007 — Validation Notes

> ###### Validation Notes
>
> | Check | Draft rule | Source |
> |---|---|---|
> | Required fields present | A future validator should reject profiles missing identity, status, integration-level, path-role, deterministic-tool, operation-proposal-contract, or professional-boundary fields. | REF-008; `docs/PRD.md` §8.17 FR-108, FR-109 |
> | Deterministic validation | Profile validation must be deterministic before runtime exposure. | `docs/PRD.md` §8.17 FR-109; D-T0-06 |
> | Result schema refs | Missing `validate_result_schema`, `apply_result_schema`, or deterministic-check result schemas remain explicit `TBD`; chat must not infer them. | REF-008 |
> | Future-only exposure | Candidate domain endpoints/tools must remain provisional until governed future amendment. | `docs/SPEC.md` §18 |
> | Solver separation | Profile contract must preserve that domain engines own authoritative domain truth. | `docs/CONTRACT.md` §1.10 K-DOMAIN-1 |
>

### CLM-008 — References

> ##### References
>
> - `_CONTEXT.md`
> - `_REFERENCES.md`
> - `_DEPENDENCIES.md`
> - `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §PKG-10, SOW-066, SOW-067, DEC-006
> - `agents/AGENT_DOMAIN_ENGINE.md` pinned at `77a327727`
> - `docs/CONTRACT.md` §1.10
> - `docs/SPEC.md` §18
> - `docs/TYPES.md` §11
> - `docs/PLAN.md` §R7
> - `docs/PRD.md` §8.17, §10.10, §R7, KG-016 through KG-020
>

### CLM-009 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-148 distinguishes supplied ruled-amendment fields (profile instances and hook-field schema references) from genuine remaining TBDs (adapters, stores, endpoints, apply tooling, and per-instance notice review).

## Completion and Reliance Basis — Epistemology

### CLM-010 — Specification: DEL-10-01 DomainEngineProfile Contract Draft

> #### Specification: DEL-10-01 DomainEngineProfile Contract Draft
>

### CLM-011 — Scope

> ##### Scope
>
> This deliverable specifies a future-boundary draft for `DomainEngineProfile`: profile identity,
> integration level, domain artifact roles, protected and agent-writable paths, deterministic tools,
> operation-proposal contract hooks, and professional-boundary notices.
>
> In scope:
>
> - Future `DomainEngineProfile` documentation contract conforming to framework-root
>   `agents/AGENT_DOMAIN_ENGINE.md` at commit `77a327727`.
> - App-dev vocabulary alignment in `docs/TYPES.md` §11.
> - Validation notes for deterministic profile acceptance.
> - Future amendment checklist for accepting concrete profile instances after core harness stability.
>
> Out of scope:
>
> - `/api/domain/*` endpoints, operation apply, direct protected-path writes/hooks, and general domain-runtime activation. D-APP-49 through D-APP-52 separately authorize source types/guards, a closed registry, ruled read tools, and pec-scoped loopback propose/refresh/validate tools.
> - Engine-specific integration, including OpenPipeStress-specific runtime assumptions.
> - Direct writes to protected domain-engine model paths.
> - Professional approval, code compliance, certification, sealing, authentication, external validation, or
>   solver-truth claims.
>
> Sources: `_CONTEXT.md`; `_REFERENCES.md` REF-008; `agents/AGENT_DOMAIN_ENGINE.md` pinned at
> `77a327727`; `docs/CONTRACT.md` §1.10; `docs/TYPES.md` §11; `docs/SPEC.md` §18; `docs/PRD.md` §8.17.
>

### CLM-012 — Requirements

> ##### Requirements
>
> | ID | Requirement | Verification |
> |---|---|---|
> | DEL-10-01-REQ-001 | The contract draft MUST preserve `ResponsibleParty: TBD` until human assignment. | Inspect document identification sections. |
> | DEL-10-01-REQ-002 | The contract draft MUST distinguish the D-APP-49 through D-APP-52 staged-live surface from the still-gated endpoints, apply, protected-path hooks/writes, and general domain runtime. | Inspect Scope, Conditions, and Procedure gate checks. |
> | DEL-10-01-REQ-003 | A generic `DomainEngineProfile` contract MUST precede any engine-specific integration. | Confirm no OpenPipeStress-specific runtime assumptions are embedded in the generic profile contract. |
> | DEL-10-01-REQ-004 | A future `DomainEngineProfile` MUST include canonical identity, status, integration-level, path-role, deterministic-tool, operation-proposal-contract, and professional-boundary fields from framework `AGENT_DOMAIN_ENGINE.md` at `77a327727`. | Validate field list against `docs/TYPES.md` §11.1 and `_REFERENCES.md` REF-008. |
> | DEL-10-01-REQ-005 | `profile_status` MUST use `NONE | DRAFT | VALIDATED | ADOPTED | STALE | INVALID | UNKNOWN`; integrated workflows require `ADOPTED`, while `MANUAL_BRIDGE` may explicitly record no adopted profile. | Inspect `docs/TYPES.md` §11.1 and future profile records. |
> | DEL-10-01-REQ-006 | `integration_level` MUST use `MANUAL_BRIDGE | READ_ONLY | DOMAIN_CONTROLLED_WRITE | OPERATION_PROPOSAL | EXTERNAL_RESULT_STATE` and MUST NOT skip levels. | Inspect profile documentation and future amendment packets. |
> | DEL-10-01-REQ-007 | Protected domain paths MUST be write-quarantined, and agent writes MUST be limited to profile-approved `agent_writable_paths`. | Future path policy separates authoritative/readable/protected/agent-writable path roles. |
> | DEL-10-01-REQ-008 | Declared deterministic tools MUST include `id`, `mode`, `requires_human_confirmation`, `validate_result_schema`, and `apply_result_schema`; missing schema refs remain explicit `TBD`, not inferred. | Inspect deterministic-tool records and validation notes. |
> | DEL-10-01-REQ-009 | The profile MUST carry an `operation_proposal_contract` covering lifecycle, risk classes, deterministic-check result schema, and accepted/applied requirements. | Inspect profile contract section and DEL-10-03 alignment. |
> | DEL-10-01-REQ-010 | Applying a domain operation MUST require explicit human acceptance bound to K-AUTH-2 evidence and domain-engine-controlled apply or external terminal acceptance records. | Future operation workflow links application to the human gate and accepted/applied requirements. |
> | DEL-10-01-REQ-011 | Boundary notices MUST state that Chirality does not approve, certify, seal, code-validate, externally validate, or own solver truth. | Review `professional_boundary` copy in future profile instances. |
>

### CLM-013 — Standards

> ##### Standards
>
> | Source | Applicable authority | Notes |
> |---|---|---|
> | `agents/AGENT_DOMAIN_ENGINE.md` at `77a327727` | Canonical domain-engine persona, minimal profile shape, and profile/proposal governance | REF-008; framework-root canonical under D-T0-01. |
> | `docs/CONTRACT.md` §1.10 | App-dev K-DOMAIN invariants specializing framework K-DOMAIN without weakening them | Governs truth ownership, path quarantine, operation proposals, and professional boundary. |
> | `docs/SPEC.md` §18 | Future specification boundary and candidate endpoint families | Candidate endpoints are provisional and must not be implemented as current-release scope. |
> | `docs/TYPES.md` §11 | App-dev vocabulary target conforming to framework canon | Documents profile/proposal vocabulary only; it does not create source types. |
> | `docs/PRD.md` §8.17 | Product requirements FR-106 through FR-115 | Current authority-corpus references are reconciled by D-APP-38. |
> | `docs/PLAN.md` §R7 | Future amendment sequencing | Domain profiles come after core harness stability and human-gated R7 activation. |
>

### CLM-014 — Verification

> ##### Verification
>
> | Verification item | Method |
> |---|---|
> | Four-document completeness | Confirm `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present and non-empty. |
> | Future-boundary preservation | Search for current-release implementation claims, source-type activation, MCP tool activation, path-hook implementation, or endpoint activation language; none should be present. |
> | Source grounding | Check each non-trivial requirement against cited source sections and REF-008. |
> | Canon conformance | Confirm the profile contract includes ProfileStatus, IntegrationLevel, role-classed paths, deterministic-tool schema hooks, operation-proposal contract, and structured professional boundary. |
> | True TBD preservation | Confirm concrete profile instances, concrete result schema refs, adapter implementations, stores, and apply tooling remain `TBD` until a governed amendment accepts them. |
> | Cross-document consistency | Confirm terminology uses `DomainEngineProfile`, `ProfileStatus`, `IntegrationLevel`, protected path, agent-writable path, deterministic tool, OperationProposal, and boundary notice consistently. |
> | Future profile-instance review data | When concrete profile fixtures exist, review instance-level `professional_boundary` copy and profile values rather than relying only on the generic illustrative skeleton. |
> | Status policy | Do not change `_STATUS.md` in this conformance tranche; `CHECKING -> ISSUED` remains out of scope. |
>

### CLM-015 — Documentation

> ##### Documentation
>
> Required artifacts for this deliverable:
>
> - Profile schema draft: this specification and the canonical shape recorded in `Datasheet.md`.
> - Validation notes: deterministic validation requirements and true future implementation `TBD` schema refs.
> - Future amendment checklist: operationalized in `Procedure.md`.
>
> Existing dependency registers are not changed by this conformance tranche.
>

### CLM-016 — D-APP-56 ownership amendment (2026-07-12)

> ##### D-APP-56 ownership amendment (2026-07-12)
>
> Under R4-P27, this deliverable owns the ruled `domain-profile.ts` source-type mirror and the `domain-profile-registry.ts` registration mechanism and gate. The mechanism/content boundary is explicit: PEC entry content and fixture-validation evidence remain DEL-10-04 scope.

- **AC-001** — The Scope of Work identifies DEL-10-01 as a future-boundary generic DomainEngineProfile contract, covers SOW-066 and SOW-067 for OBJ-010, and preserves all four legacy source documents without semantic addition or omission.

## Production and Verification Method — Praxeology

### CLM-017 — Procedure: DEL-10-01 DomainEngineProfile Contract Draft

> #### Procedure: DEL-10-01 DomainEngineProfile Contract Draft
>

### CLM-018 — Purpose

> ##### Purpose
>
> Define the bounded procedure for maintaining the future `DomainEngineProfile` contract draft while preserving the F3 domain-engine implementation fence.
>

### CLM-019 — Prerequisites

> ##### Prerequisites
>
> | Prerequisite | Status |
> |---|---|
> | Deliverable-local context is present. | Satisfied: `_CONTEXT.md` exists. |
> | Authoritative references are accessible. | Satisfied: `_REFERENCES.md` includes REF-008 for framework `AGENT_DOMAIN_ENGINE.md` pinned at `77a327727`. |
> | Framework precedence is known. | Satisfied: D-T0-01 makes framework-root `AGENT_DOMAIN_ENGINE.md` canonical; app-dev `docs/TYPES.md` Section 11 conforms to it. |
> | Current status posture is preserved. | Required: read current state from `_STATUS.md`; this tranche performs no lifecycle transition or release-readiness act. |
> | Current scope remains future-boundary. | Required by `docs/SPEC.md` Section 18, `docs/PLAN.md` R7, and D-APP-39 F3. |
>

### CLM-020 — Steps

> ##### Steps
>
> 1. Confirm identity from `_CONTEXT.md`.
>    - DeliverableID: DEL-10-01.
>    - ResponsibleParty: TBD.
>    - Type: API_CONTRACT.
>    - Scope: future profile contract for engine identity, integration level, path/artifact roles, deterministic tools, operation-proposal contract, and professional boundary.
>
> 2. Confirm source posture from `_REFERENCES.md`.
>    - Use REF-008 as the canonical persona/profile source.
>    - Use app-dev `docs/TYPES.md` Section 11 only as the local vocabulary target conforming to REF-008.
>    - Do not create `Dependencies.csv`.
>
> 3. Read source slices for the domain-engine future boundary.
>    - `agents/AGENT_DOMAIN_ENGINE.md` at `77a327727` for Minimal Profile Shape, valid operation proposal table, lifecycle, and `operation_proposal_contract`.
>    - `docs/CONTRACT.md` Section 1.10 for app-dev K-DOMAIN invariants, which specialize framework `docs/CONTRACT.md` Section 1.12 without weakening it.
>    - `docs/SPEC.md` Section 18 for provisional future endpoint/tool boundary.
>    - `docs/TYPES.md` Section 11 for app-dev vocabulary.
>    - `docs/PLAN.md` R7 for future-amendment sequencing.
>    - `docs/PRD.md` Section 8.17 for FR-106 through FR-115.
>    - Decomposition PKG-10 / DEL-10-01 entry for local scope.
>
> 4. Draft or maintain the profile contract.
>    - Preserve canonical identity fields: `schema_version`, `id`, `name`, `engine_type`, and `profile_version`.
>    - Preserve canonical `ProfileStatus`: `NONE | DRAFT | VALIDATED | ADOPTED | STALE | INVALID | UNKNOWN`.
>    - Preserve canonical `IntegrationLevel`: `MANUAL_BRIDGE | READ_ONLY | DOMAIN_CONTROLLED_WRITE | OPERATION_PROPOSAL | EXTERNAL_RESULT_STATE`.
>    - Preserve path/artifact role fields: `domain_root_patterns`, `authoritative_artifacts`, `chirality_readable_artifacts`, `protected_write_paths`, and `agent_writable_paths`.
>    - Preserve deterministic tool fields, including `validate_result_schema` and `apply_result_schema`.
>    - Preserve `operation_proposal_contract`, including lifecycle, risk classes, deterministic-check result schema, and accepted/applied requirements.
>    - Preserve structured `professional_boundary`.
>
> 5. Mark only true future implementation details as `TBD`.
>    - Concrete profile instances.
>    - Concrete schema refs for validation/apply/deterministic-check results.
>    - Adapters, MCP tools, stores, endpoint handlers, protected-path hooks, and apply tooling.
>    - Concrete boundary notice copy for each accepted profile instance.
>
> 6. Preserve future-boundary constraints.
>    - Do not implement candidate endpoints.
>    - Do not define executable tool behavior.
>    - Do not authorize direct protected-path writes.
>    - Do not represent domain output as professional approval, code compliance, certification, sealing, authentication, external validation, or Chirality-owned solver truth.
>
> 7. Cross-check documents.
>    - Confirm `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` use consistent canonical terms.
>    - Confirm DEL-10-03 uses the same lifecycle and proposal contract fields.
>    - Confirm old compact-draft blockers are not reintroduced as unresolved human-ruling blockers.
>
> 8. Record the run without lifecycle transition.
>    - Keep `_STATUS.md` unchanged.
>    - Record conformance notes in `MEMORY.md` and coordination closeout.
>    - Let D-APP-38 reconciliation update authority-corpus hashes after authority-doc edits.
>

### CLM-021 — Verification

> ##### Verification
>
> | Check | Expected result |
> |---|---|
> | Four document files | Present and non-empty. |
> | Status state | Current state is read from `_STATUS.md`; no lifecycle transition is claimed. |
> | Responsible party | Remains `TBD`. |
> | Canon conformance | Profile vocabulary includes REF-008 identity, status, integration, path role, deterministic-tool, operation-proposal, and professional-boundary fields. |
> | True TBD posture | Concrete profiles, concrete schema refs, adapters, stores, path hooks, and apply tooling remain `TBD`. |
> | Dependency register | Existing `Dependencies.csv` remains separate derivative evidence and is not created or edited by this conformance tranche. |
> | Implementation activation | No domain-engine source type, endpoint, MCP tool, adapter, operation store, apply workflow, or protected-path write implementation is activated. |
>

### CLM-022 — Records

> ##### Records
>
> - `Datasheet.md`
> - `Specification.md`
> - `Guidance.md`
> - `Procedure.md`
> - `MEMORY.md`
> - `_STATUS.md`
> - D-APP-45 closeout packet

- **VER-001** — Verify the source-marker map and parity report against the four legacy documents, then verify the matrix binds OUT-001 and AC-001 to SOW-066, SOW-067, and OBJ-010.

## Governing Values and Decisions — Axiology

### CLM-023 — Guidance: DEL-10-01 DomainEngineProfile Contract Draft

> #### Guidance: DEL-10-01 DomainEngineProfile Contract Draft
>

### CLM-024 — Purpose

> ##### Purpose
>
> This guidance explains how to read and maintain the `DomainEngineProfile` contract draft as a future-boundary artifact. The draft preserves compatibility with future domain-engine integrations without activating domain execution in the current app-dev slice.
>
> Primary canon: `_REFERENCES.md` REF-008, `agents/AGENT_DOMAIN_ENGINE.md` pinned at `77a327727`. Under D-T0-01, the framework-root persona is canonical; app-dev `docs/TYPES.md` Section 11 conforms to it and must not weaken framework invariants.
>

### CLM-025 — Principles

> ##### Principles
>
> | Principle | Guidance | Source |
> |---|---|---|
> | Canon first | Maintain the profile shape from REF-008: identity fields, `ProfileStatus`, `IntegrationLevel`, path/artifact roles, deterministic tools, `operation_proposal_contract`, and professional boundary. | REF-008; `docs/TYPES.md` Section 11.1 |
> | Generic first | Keep the profile contract generic before any engine-specific integration. OpenPipeStress may be a future concrete profile, but it must not shape Chirality core runtime assumptions. | `docs/PRD.md` Section 8.17 FR-107 |
> | Future gated | Treat endpoints, tools, validators, adapters, operation stores, and path hooks as future platform interfaces until a governed amendment accepts them. | `docs/SPEC.md` Section 18; `docs/PLAN.md` R7 |
> | Truth separation | Domain engines own authoritative domain truth; Chirality governs interaction, profile records, proposals, review aids, and human gates. | `docs/CONTRACT.md` Section 1.10 K-DOMAIN-1 |
> | Path quarantine | Protected paths and agent-writable paths must remain distinct. Agents may draft proposals and summaries only under approved writable proposal/review paths. | `docs/CONTRACT.md` Section 1.10 K-DOMAIN-2; REF-008 |
> | Human acceptance | Accepted/applied proposal states require explicit human approval bound to K-AUTH-2 evidence and a domain-engine-controlled apply or external terminal acceptance record. | `docs/CONTRACT.md` Section 1.10 K-DOMAIN-3; REF-008 |
> | Professional boundary | Boundary notices must prevent solver outputs from being presented as professional approval, code compliance, certification, sealing, authentication, external validation, or solver truth owned by Chirality. | `docs/CONTRACT.md` Section 1.10 K-DOMAIN-4; REF-008 |
>

### CLM-026 — Considerations

> ##### Considerations
>
> - Use `docs/TYPES.md` Section 11.1 as the app-dev vocabulary target, but resolve conflicts against REF-008.
> - The older compact draft fields `DomainEngineOperationDescriptor` and `manifestRules` are superseded by canonical `deterministic_tools`, path/artifact role sets, and `operation_proposal_contract`; they are no longer human-ruling blockers for DEL-10-01.
> - Keep `validate_result_schema`, `apply_result_schema`, and deterministic-check result schema references explicit. A concrete schema may remain `TBD`, but the schema hook itself is canonical.
> - Keep OpenPipeStress references fixture-level only. A concrete OpenPipeStress profile remains future/gated and must not become an app-dev runtime assumption in this tranche.
> - Any future validator should be deterministic and reject invalid or incomplete profiles before runtime exposure.
> - Preserve `_STATUS.md` as-is. This conformance tranche does not authorize `CHECKING -> ISSUED`, release readiness, or R7 implementation.
>

### CLM-027 — True Future TBDs

> ##### True Future TBDs
>
> | Topic | Conservative position | Risk if loosened |
> |---|---|---|
> | Concrete profile instances | Leave engine instances, including OpenPipeStress, as future amendment scope. | An illustrative profile could be mistaken for accepted integration. |
> | Concrete schema refs | Record `validate_result_schema`, `apply_result_schema`, and deterministic-check result schema as explicit refs or `TBD`. | Prompt-inferred result schemas could become false contract surface. |
> | Adapter/tool implementation | Defer deterministic adapters, stores, MCP tools, endpoints, and path hooks. | Crosses F3 and activates domain runtime without tier-0 gate. |
> | Boundary notice copy | Require structured boundary fields now; review concrete text per profile instance later. | Generic copy may imply professional reliance in a domain-specific context. |
>

### CLM-028 — Example Generic Skeleton

> ##### Example Generic Skeleton
>
> ```yaml
> domain_profile:
>   schema_version: "1.0"
>   id: "TBD"
>   name: "TBD"
>   engine_type: "TBD"
>   profile_version: "0.1"
>   profile_status: "DRAFT"
>   integration_level: "MANUAL_BRIDGE"
>   domain_root_patterns: []
>   authoritative_artifacts: []
>   chirality_readable_artifacts: []
>   protected_write_paths: []
>   agent_writable_paths: []
>   deterministic_tools:
>     - id: "TBD"
>       mode: "read_only"
>       requires_human_confirmation: false
>       validate_result_schema: "TBD"
>       apply_result_schema: "TBD"
>   operation_proposal_contract:
>     lifecycle: ["draft", "ready_for_review", "accepted", "rejected", "applied"]
>     deterministic_check_result_schema: "TBD"
>   professional_boundary:
>     agent_must_not_claim:
>       - "code compliant for reliance"
>       - "professionally approved"
>       - "externally validated"
> ```
>
> This example is illustrative only. It is not an accepted runtime fixture and must not be treated as implementation-ready.
>
> Cross-reference (2026-07-02, agent decision under `TRB-chirality-app-dev-DEL-10-01-2026-07-02`): a concrete ADOPTED instance of this contract now exists — `_DomainEngines/profiles/open_pipe_stress.yaml` (tier-0, ADOPTED per D-T0-06) — and the concrete result-schema refs the example marks `TBD` are published for that instance: `projects/chirality-piping/schemas/operation_outcome.schema.json` (`validate_result_schema` / `apply_result_schema`; operation_applier `OperationOutcome`) and `projects/chirality-piping/schemas/rule_check_run_result.schema.json` (`deterministic_check_result_schema`; rule_check_runner `RuleCheckRunResult`). The Rust sources govern on disagreement; the ADOPTED profile's own hook fields still read `TBD` pending an owner tier-0 CHANGE. The example skeleton above stays as-is: its `TBD` placeholders are template positions, and other engines supply their own refs. Note the repo qualifier: piping DEL-10-03 (Local FEA handoff) published those schemas; app-dev DEL-10-03 is a different deliverable.
>

### CLM-029 — References

> ##### References
>
> - `_REFERENCES.md` REF-008
> - `agents/AGENT_DOMAIN_ENGINE.md` pinned at `77a327727`
> - `docs/CONTRACT.md` Section 1.10
> - `docs/SPEC.md` Section 18
> - `docs/TYPES.md` Section 11
> - `docs/PLAN.md` R7
> - `docs/PRD.md` Section 8.17, Section 10.10, KG-016 through KG-020
>

### CLM-030 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-148 distinguishes supplied ruled-amendment fields (profile instances and hook-field schema references) from genuine remaining TBDs (adapters, stores, endpoints, apply tooling, and per-instance notice review).

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-066 SOW-067 OBJ-010 | CLM-010 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
