---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-10-03
package_id: PKG-10
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@7b0be4d8772a16e5a4774a17988479587d00acca
project_scope_refs: [SOW-069]
package_objective_refs: [OBJ-010]
---

# Scope of Work — DEL-10-03

## Purpose and Objective Traceability

This Scope of Work defines `DEL-10-03` in service of project scope [SOW-069] and package objectives [OBJ-010].

- **OUT-001** — OperationProposal record and human-gate workflow contract for DEL-10-03 under SOW-069 and OBJ-010, preserving proposal-only status and future-boundary scope.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-10-03 OperationProposal Record and Human Gate Workflow

> #### Datasheet: DEL-10-03 OperationProposal Record and Human Gate Workflow
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DeliverableID | DEL-10-03 |
> | DeliverableName | OperationProposal Record and Human Gate Workflow |
> | PackageID | PKG-10 |
> | PackageName | Domain Engine Future Boundary |
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | Type | DATA_MODEL_CHANGE |
> | ResponsibleParty | TBD |
> | ScopeItem | SOW-069 |
> | SupportedObjective | OBJ-010 |
> | ContextEnvelope | M |
> | Current posture | Future-boundary workflow contract, not current implementation |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Boundary posture | Future platform compatibility; not current-release domain operation execution. | `_CONTEXT.md`; `docs/PRD.md` Section 8.17 |
> | Record type | `OperationProposal` future domain operation proposal record. | REF-008; `docs/TYPES.md` Section 11.2 |
> | Required identity/control fields | `proposal_id`, `profile_id`, `base_state`, `operation_name`, `status`, `lifecycle`, `created_at`, `created_by`, `storage_path`. | REF-008; `docs/TYPES.md` Section 11.2 |
> | Required review fields | `input_refs`, `intended_changes`, `deterministic_checks`, `expected_output_refs`, `risks`, `assumptions`, `blockers`, `boundary_notice`, `required_human_gate`, `operation_risk_class`, `provenance_on_judgment_values`. | REF-008; `docs/TYPES.md` Section 11.2 |
> | Proposal-only status | `status` is `proposal_only`. | REF-008; `docs/TYPES.md` Section 11.2 |
> | Lifecycle enum | `draft`, `ready_for_review`, `accepted`, `rejected`, `applied`. | REF-008; `docs/TYPES.md` Section 11.2 |
> | Gate requirement | Accepted/applied lifecycle states require explicit human approval bound to git SHA per K-AUTH-2. | REF-008; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-3 |
> | Apply requirement | Applied lifecycle state also requires domain-engine-controlled apply or external terminal acceptance record. | REF-008; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-3 |
> | Result schema hooks | Proposal checks route through profile-declared `validate_result_schema`, `apply_result_schema`, and deterministic-check result schema hooks. | REF-008; `docs/TYPES.md` Section 11.1 |
> | Domain-truth ownership | Domain engines own authoritative domain truth; Chirality governs interaction, proposals, records, and human gates. | `docs/CONTRACT.md` Section 1.10 K-DOMAIN-1 |
> | Protected path relationship | Agents write proposals, summaries, and review aids, not protected domain-engine model truth. | `docs/PRD.md` Section 8.17; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-2 |
> | Professional boundary | Domain-engine output must not be represented as professional approval, code compliance, certification, sealing, authentication, external validation, or solver truth owned by Chirality. | `docs/PRD.md` Section 8.17; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-4 |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Value | Source |
> |---|---|---|
> | Activation condition | Future amendment required before domain-engine operation execution is active. | `docs/PLAN.md` R7; `_CONTEXT.md` Package Scope |
> | Current implementation state | Domain-engine implementation is not activated by this deliverable. | D-APP-39 F3; `docs/SPEC.md` Section 18 |
> | Upstream precedence | Framework-root `AGENT_DOMAIN_ENGINE.md` at `77a327727` is canonical; app-dev `docs/TYPES.md` Section 11 conforms to it. | D-T0-01; REF-008 |
> | Resolved former blockers | Required-human-gate semantics and result-schema hooks are resolved by canon; concrete result-schema refs published 2026-07-02 (`projects/chirality-piping/schemas/operation_outcome.schema.json`, `projects/chirality-piping/schemas/rule_check_run_result.schema.json`); remaining evidence artifacts (operation store, records, review checklist) implementation `TBD`. | REF-008; D-T0-01; piping DEL-10-03 |
> | Upstream dependencies | TBD - no accepted dependency edges have been extracted. | `_DEPENDENCIES.md` |
> | Downstream dependencies | TBD - no accepted dependency edges have been extracted. | `_DEPENDENCIES.md` |
>

### CLM-005 — Construction

> ##### Construction
>
> | Component | Description | Source |
> |---|---|---|
> | Proposal record shape | Future `OperationProposal` table with canonical fields and proposal-only status. | REF-008; `docs/TYPES.md` Section 11.2 |
> | Base state | Identifies the accepted state or artifact baseline against which a proposal is made. | REF-008 |
> | Deterministic checks | Proposal field listing checks expected before review; the check result payload is published 2026-07-02 (`projects/chirality-piping/schemas/rule_check_run_result.schema.json`); the ADOPTED profile's hook refs remain `TBD` pending an owner tier-0 CHANGE. | REF-008; `docs/PRD.md` Section 8.17; piping DEL-10-03 |
> | Human gate workflow | Proposal cannot reach accepted/applied lifecycle states without K-AUTH-2-bound human approval. | REF-008; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-3 |
> | Review checklist | Must verify field completeness, base state, deterministic checks, outputs, risks, assumptions, blockers, required human gate, protected-path posture, and professional-boundary language. | REF-008; `docs/PRD.md` Section 8.17 |
>

### CLM-006 — References

> ##### References
>
> - `_CONTEXT.md`
> - `_DEPENDENCIES.md`
> - `_REFERENCES.md`
> - `agents/AGENT_DOMAIN_ENGINE.md` pinned at `77a327727`
> - `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
> - `docs/CONTRACT.md` Section 1.10
> - `docs/DIRECTIVE.md` professional and domain-boundary principles
> - `docs/PLAN.md` future domain-engine items
> - `docs/PRD.md` Section 8.17
> - `docs/SPEC.md` domain endpoint list and future profile note
> - `docs/TYPES.md` Sections 11.1-11.3
>

### CLM-007 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-150/151/152 record that tier-0 CHANGE landed, open_pipe_stress and pec are ADOPTED/registered, and the extracted register is reconciled. Proposal-ID semantics, store/checklist artifacts, concrete instances, and declared-section ownership remain genuine TBDs.

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-10-03 OperationProposal Record and Human Gate Workflow

> #### Specification: DEL-10-03 OperationProposal Record and Human Gate Workflow
>

### CLM-009 — Scope

> ##### Scope
>
> This deliverable defines a future-boundary data model and review workflow for `OperationProposal` records. It covers the proposal record shape, proposal-only status, lifecycle, K-AUTH-2-bound human gate, deterministic result-schema hooks, and review checklist for future domain-engine operations.
>
> This deliverable excludes operation apply, `/api/domain/*` endpoints, direct protected-path writes/hooks, general domain-runtime activation, and any claim that Chirality owns solver truth. D-APP-49 through D-APP-52 separately authorize source types/guards, a closed registry, read tools, and pec-scoped loopback propose/refresh/validate tools; those staged surfaces remain outside this four-document contract except as governing context.
>
> Primary canon: `_REFERENCES.md` REF-008, `agents/AGENT_DOMAIN_ENGINE.md` pinned at `77a327727`. Under D-T0-01, the framework-root persona is canonical; app-dev `docs/TYPES.md` Section 11 conforms to it and must not weaken framework invariants.
>

### CLM-010 — Requirements

> ##### Requirements
>
> | ID | Requirement | Source | Verification |
> |---|---|---|---|
> | REQ-10-03-001 | The future `OperationProposal` record MUST include the canonical fields: `proposal_id`, `profile_id`, `base_state`, `operation_name`, `status`, `lifecycle`, `created_at`, `created_by`, `input_refs`, `intended_changes`, `deterministic_checks`, `expected_output_refs`, `risks`, `assumptions`, `blockers`, `boundary_notice`, `required_human_gate`, `operation_risk_class`, `provenance_on_judgment_values`, and `storage_path`. | REF-008; `docs/TYPES.md` Section 11.2 | Compare proposed schema/checklist against the field table. |
> | REQ-10-03-002 | `status` MUST be `proposal_only`; lifecycle MUST use `draft | ready_for_review | accepted | rejected | applied`. | REF-008; `docs/TYPES.md` Section 11.2 | Confirm proposal records distinguish status from lifecycle. |
> | REQ-10-03-003 | Domain operations MUST be represented as `OperationProposal` records before application. | `docs/PRD.md` Section 8.17 FR-112; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-3 | Review workflow has a proposal-record step before any apply step. |
> | REQ-10-03-004 | Accepted/applied lifecycle states MUST require explicit human approval bound to git SHA per K-AUTH-2. | REF-008; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-3 | Review checklist requires K-AUTH-2 evidence before accepted/applied states. |
> | REQ-10-03-005 | Applied lifecycle state MUST also require domain-engine-controlled apply or an external terminal acceptance record. | REF-008; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-3 | Future apply workflow records an engine-controlled or external terminal result; absent implementation remains `TBD`. |
> | REQ-10-03-006 | Proposal records MUST identify inputs, intended changes, deterministic checks, expected outputs, risks, assumptions, blockers, boundary notice, required gate, risk class, judgment-value provenance, and storage path. | REF-008; `docs/TYPES.md` Section 11.2 | Required fields are present and non-empty or explicitly `TBD` before review. |
> | REQ-10-03-007 | Deterministic checks MUST resolve against profile-declared schema hooks: `validate_result_schema`, `apply_result_schema`, and `deterministic_check_result_schema`. | REF-008; `docs/TYPES.md` Section 11.1 | Review checklist blocks implementation readiness when concrete schema refs are missing. |
> | REQ-10-03-008 | Agents MUST write proposals, summaries, and review aids, not protected domain-engine model truth. | `docs/PRD.md` Section 8.17 FR-111; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-2 | Review checklist confirms proposed outputs target proposal/review paths, not protected paths. |
> | REQ-10-03-009 | Domain-engine outputs MUST NOT be represented as professional approval, code compliance, certification, sealing, authentication, external validation, or solver truth owned by Chirality. | `docs/PRD.md` Section 8.17 FR-115; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-4 | Review checklist includes professional-boundary copy check. |
> | REQ-10-03-010 | Concrete evidence artifacts remain future implementation TBDs until accepted: profile instances, concrete schema refs, adapters, operation store, apply tooling, and review-checklist artifact path/schema. | `docs/PLAN.md` R7; `docs/SPEC.md` Section 18; REF-008 | Documentation preserves TBDs for concrete implementation artifacts without weakening canonical lifecycle semantics. |
>

### CLM-011 — Standards

> ##### Standards
>
> | Standard or Source | Applicability |
> |---|---|
> | `agents/AGENT_DOMAIN_ENGINE.md` at `77a327727` | Canonical operation-proposal field table, lifecycle, human gate, result-schema hooks, and boundary posture. |
> | `docs/TYPES.md` Section 11.2 | App-dev vocabulary target conforming to framework canon. |
> | `docs/PRD.md` Section 8.17 | Product requirements for future domain-engine compatibility. |
> | `docs/CONTRACT.md` Section 1.10 | Binding app-dev invariants specializing framework K-DOMAIN without weakening it. |
> | `docs/SPEC.md` Section 18 | Future API surface context; endpoint behavior details remain gated. |
>

### CLM-012 — Verification

> ##### Verification
>
> | Check | Method | Result Target |
> |---|---|---|
> | Schema completeness | Verify every canonical `OperationProposal` field appears in the record shape or checklist. | PASS/TBD |
> | Status/lifecycle integrity | Verify `status = proposal_only` and lifecycle values match REF-008. | PASS/TBD |
> | Human gate | Verify accepted/applied states require K-AUTH-2-bound human approval. | PASS/TBD |
> | Apply result posture | Verify applied state also requires domain-engine-controlled apply or external terminal acceptance record, or remains blocked as implementation `TBD`. | PASS/TBD |
> | Result schema hooks | Verify future deterministic checks reference profile-level validation/apply/check result schema hooks. | PASS/TBD |
> | Protected path posture | Verify proposal outputs do not directly modify protected domain-engine paths. | PASS/TBD |
> | Boundary language | Verify no text claims Chirality approves, certifies, code-validates, externally validates, seals, authenticates, or owns solver truth. | PASS/TBD |
> | Future-boundary constraint | Verify implementation activation is excluded until governed amendment. | PASS/TBD |
> | Review sufficiency evidence | Verify a future review-checklist result artifact is identified as a true implementation `TBD`, not as an unresolved framework blocker. | PASS/TBD |
>

### CLM-013 — Documentation

> ##### Documentation
>
> Required artifacts for this deliverable:
>
> - Proposal record shape.
> - Gate workflow notes.
> - Review checklist.
>
> Additional documentation needed before implementation:
>
> - TBD: exact proposal ID generation semantics.
> - TBD: concrete `DomainEngineProfile` instance for the target engine.
> - RESOLVED by cross-reference (2026-07-02, agent decision under
>   `TRB-chirality-app-dev-DEL-10-03-2026-07-02`): concrete refs for the tier-0 engine
>   instance are published — `validate_result_schema` / `apply_result_schema` =
>   `projects/chirality-piping/schemas/operation_outcome.schema.json` (operation_applier
>   `OperationOutcome`; `mode` = `validate_only` / `apply`),
>   `deterministic_check_result_schema` =
>   `projects/chirality-piping/schemas/rule_check_run_result.schema.json`
>   (rule_check_runner `RuleCheckRunResult`); the Rust sources govern on disagreement.
>   Residual `TBD`: the ADOPTED profile's hook fields await an owner tier-0 CHANGE
>   (`_DomainEngines/profiles/open_pipe_stress.yaml:81,88,101,115`); engines other than
>   open_pipe_stress supply their own refs.
> - TBD: operation store and `storage_path` convention.
> - TBD: adapter validation/apply tooling and result-record location. (Narrowed
>   2026-07-02: the validation/apply result envelope is published — see the resolved
>   refs above; the tooling and the app-dev-side result-record location remain `TBD`.)
> - TBD: review checklist result artifact path/schema.
> - TBD: concrete proposal instances and profile-specific boundary notice copy.
>

### CLM-014 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-150/151/152 record that tier-0 CHANGE landed, open_pipe_stress and pec are ADOPTED/registered, and the extracted register is reconciled. Proposal-ID semantics, store/checklist artifacts, concrete instances, and declared-section ownership remain genuine TBDs.
>

### CLM-015 — D-APP-56 ownership amendment (2026-07-12)

> ##### D-APP-56 ownership amendment (2026-07-12)
>
> Under R4-P27, this deliverable owns the ruled proposal-tool surface in `domain-proposal-tools.ts` (`propose`, `refresh`, and `validate`), including registration, proposal envelopes, and gates. Only PEC-profile-scoped fixture interaction is evidence for DEL-10-04. This amendment does not unlock DEP-10-03-004 or any D-APP-53 Option-C-gated work.

- **AC-001** — The DEL-10-03 OperationProposal record and human-gate workflow preserves the exact legacy source content, proposal-only boundary, and human approval gate while remaining bounded to SOW-069 and OBJ-010.

## Production and Verification Method — Praxeology

### CLM-016 — Procedure: DEL-10-03 OperationProposal Record and Human Gate Workflow

> #### Procedure: DEL-10-03 OperationProposal Record and Human Gate Workflow
>

### CLM-017 — Purpose

> ##### Purpose
>
> Define the future workflow for producing and reviewing `OperationProposal` records while preserving protected-path, human-gate, result-schema, and professional-boundary constraints. This procedure is a design procedure for the future workflow; it does not activate domain-engine operation execution.
>

### CLM-018 — Prerequisites

> ##### Prerequisites
>
> - Framework canon source: `_REFERENCES.md` REF-008, `agents/AGENT_DOMAIN_ENGINE.md` pinned at `77a327727`.
> - Accepted future amendment authorizing domain-engine operation workflow implementation: TBD.
> - Accepted `DomainEngineProfile` for the target engine: TBD.
> - Protected path and proposal path policy: TBD, sibling deliverable DEL-10-02.
> - Deterministic adapter or validation tool for the operation: TBD.
> - Concrete `validate_result_schema`, `apply_result_schema`, and deterministic-check result schema refs: published 2026-07-02 — `projects/chirality-piping/schemas/operation_outcome.schema.json` (validate/apply envelope) and `projects/chirality-piping/schemas/rule_check_run_result.schema.json` (deterministic-check result); the ADOPTED profile's hook fields remain `TBD` pending an owner tier-0 CHANGE.
> - Operation store and review-checklist result artifact path/schema: TBD.
> - Declared upstream dependencies: TBD, no accepted dependency edges extracted yet.
>

### CLM-019 — Steps

> ##### Steps
>
> 1. Confirm future-boundary authorization.
>    - Verify that the work remains proposal/workflow design unless a governed amendment authorizes implementation.
>    - Source: `_CONTEXT.md`; `docs/PLAN.md` R7; D-APP-39 F3.
>
> 2. Create a draft `OperationProposal` record.
>    - Populate each canonical field from REF-008 / `docs/TYPES.md` Section 11.2.
>    - Set `status` to `proposal_only`.
>    - Set `lifecycle` to `draft`.
>    - Use `TBD` for unavailable implementation values.
>    - Keep `ResponsibleParty` outside the proposal workflow as `TBD` until human assignment.
>
> 3. Identify baseline, inputs, and intended changes.
>    - Fill `base_state` with the accepted baseline or mark it `TBD`.
>    - Fill `input_refs` with the future domain artifacts or proposal inputs to be reviewed.
>    - Fill `intended_changes` with proposed changes.
>    - Do not write directly to protected domain-engine model truth.
>
> 4. Define deterministic checks.
>    - Populate `deterministic_checks` with the checks expected before review.
>    - Tie checks to profile-level `validate_result_schema`, `apply_result_schema`, and deterministic-check result schema hooks.
>    - Mark exact payloads, pass/fail schema, adapter/profile reference, evidence path, and failure reason field as `TBD` until an adapter/profile contract is accepted. (Since 2026-07-02 the pass/fail result shapes are published — `projects/chirality-piping/schemas/rule_check_run_result.schema.json` carries per-check status, computed/limit values, findings, and diagnostic codes; adapter/profile reference and evidence path remain `TBD`.)
>
> 5. Identify expected outputs, risks, assumptions, and blockers.
>    - Populate `expected_output_refs` with proposal/review artifacts or approved future adapter outputs.
>    - Populate `risks`, `assumptions`, and `blockers`; use `TBD` for items requiring domain expert review.
>    - Record `operation_risk_class` and provenance for judgment values.
>
> 6. Set the required human gate.
>    - Populate `required_human_gate` with the required gate name or mark it `TBD`.
>    - Do not move to `accepted` or `applied` without explicit human approval bound to git SHA per K-AUTH-2.
>    - Do not move to `applied` without domain-engine-controlled apply or external terminal acceptance record.
>
> 7. Review protected-path and professional-boundary posture.
>    - Confirm agents write proposals, summaries, and review aids only.
>    - Confirm proposal text does not claim professional approval, code compliance, certification, sealing, authentication, external validation, or Chirality-owned solver truth.
>
> 8. Maintain lifecycle semantics.
>    - `draft`: initial incomplete or working proposal.
>    - `ready_for_review`: proposal has required fields populated or explicitly marked `TBD`, deterministic checks are identified, and unresolved blockers are visible in the review checklist.
>    - `accepted`: explicit human approval has been recorded and bound to git SHA per K-AUTH-2.
>    - `rejected`: human reviewer or policy rejects the proposal and records the rejection reason in the same evidence family as acceptance.
>    - `applied`: accepted proposal is applied by domain-engine-controlled apply or external terminal acceptance record, with result evidence stored according to the accepted profile/workflow.
>

### CLM-020 — Verification

> ##### Verification
>
> | Verification Item | Pass Condition |
> |---|---|
> | Field completeness | Every canonical `OperationProposal` field is populated or marked `TBD`. |
> | Status/lifecycle | `status` is `proposal_only`; lifecycle values match REF-008. |
> | Human gate | Accepted/applied states require K-AUTH-2-bound human approval. |
> | Deterministic checks | Checks are listed or marked `TBD`; no prompt-only safety claim is made. |
> | Result schema hooks | Validation/apply/check result schema hooks are present; concrete refs may remain `TBD`. |
> | Protected path safety | No step instructs agents to write protected domain-engine model truth. |
> | Boundary notice | No step or record represents Chirality as professional approver, code-compliance verifier, certifier, sealer, authenticator, external validator, or solver truth owner. |
> | Future-boundary posture | Procedure does not activate current-release domain operation execution. |
> | Review sufficiency evidence | Future review checklist result records field completeness, protected-path posture, boundary-language review, gate readiness, deterministic-check readiness, and unresolved implementation blockers or marks the result artifact as `TBD`. |
>

### CLM-021 — Records

> ##### Records
>
> - Draft `OperationProposal` record.
> - Deterministic check plan or `TBD` placeholder.
> - Deterministic check result record: the runner-side result shape is published (2026-07-02) as `projects/chirality-piping/schemas/rule_check_run_result.schema.json` (`CheckOutcome`: check id, status, computed/limit values, findings, diagnostic codes); the app-dev-side record wrapper (adapter/profile reference, evidence path) remains `TBD` future schema.
> - Human gate acceptance/rejection record: TBD future artifact carrying K-AUTH-2-bound approval/rejection evidence.
> - Review checklist result: TBD future artifact recording schema completeness, protected-path posture, boundary-language review, human-gate readiness, deterministic-check readiness, and unresolved implementation blockers.
> - Boundary notice review result.
> - Adapter validation/apply result: the result envelope is published (2026-07-02) as `projects/chirality-piping/schemas/operation_outcome.schema.json` (operation/change identifiers, validation states, diff preview, diagnostics, honest acceptance receipt); the app-dev-side implementation artifact (accepted proposal reference, output references, failure/rollback note, record location) remains `TBD`.
>

### CLM-022 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-150/151/152 record that tier-0 CHANGE landed, open_pipe_stress and pec are ADOPTED/registered, and the extracted register is reconciled. Proposal-ID semantics, store/checklist artifacts, concrete instances, and declared-section ownership remain genuine TBDs.

- **VER-001** — Verify DEL-10-03 source-marker coverage and byte parity against the exact legacy four-document source, and confirm SOW-069 and OBJ-010 traceability, proposal-only status, and the preserved human gate.

## Governing Values and Decisions — Axiology

### CLM-023 — Guidance: DEL-10-03 OperationProposal Record and Human Gate Workflow

> #### Guidance: DEL-10-03 OperationProposal Record and Human Gate Workflow
>

### CLM-024 — Purpose

> ##### Purpose
>
> This deliverable preserves future compatibility for domain-engine operation workflows without turning Chirality into a domain solver. It defines how future domain operations should be represented as proposed, reviewable, human-gated records before any protected domain state can be changed.
>
> Primary canon: `_REFERENCES.md` REF-008, `agents/AGENT_DOMAIN_ENGINE.md` pinned at `77a327727`.
>

### CLM-025 — Principles

> ##### Principles
>
> - Treat `OperationProposal` as a future proposal and audit record, not as permission to execute a domain operation by itself.
> - Keep authoritative domain truth in the domain engine. Chirality governs interaction, proposals, records, review aids, and human gates.
> - Keep protected domain paths separate from profile-approved agent-writable proposal paths.
> - Preserve `status = proposal_only`; use `lifecycle` for `draft`, `ready_for_review`, `accepted`, `rejected`, and `applied`.
> - Require deterministic checks and profile-declared result-schema hooks before a future operation can be considered implementation-ready.
> - Require explicit human approval bound to git SHA per K-AUTH-2 before accepted/applied lifecycle states.
> - Preserve professional-boundary language: Chirality must not claim professional approval, code compliance, certification, sealing, authentication, external validation, or solver truth ownership.
>

### CLM-026 — Considerations

> ##### Considerations
>
> | Topic | Guidance | Source |
> |---|---|---|
> | Future scope | Draft record/workflow surfaces only; do not activate domain-engine implementation in this package. | `_CONTEXT.md`; `docs/PRD.md` Section 8.17; D-APP-39 F3 |
> | Proposal fields | Use the REF-008 field table as the minimum record shape. | REF-008; `docs/TYPES.md` Section 11.2 |
> | Base state | Include `base_state` so review can compare proposed changes against a named accepted state or artifact baseline. | REF-008 |
> | Deterministic checks | Define check names and expected outcomes before review; concrete result payloads and schema refs remain true implementation TBDs. | REF-008; `docs/PRD.md` Section 8.17 FR-112 |
> | Human gate | Accepted/applied states require explicit human approval bound to git SHA per K-AUTH-2. | REF-008; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-3 |
> | Applied state | Applied state additionally requires domain-engine-controlled apply or external terminal acceptance record. | REF-008 |
> | Protected paths | Proposal outputs should be written to proposal/review locations, not protected model truth. | `docs/PRD.md` Section 8.17 FR-110/FR-111 |
> | Professional boundary | Review copy and event records should avoid language that makes Chirality the approving professional, code-compliance verifier, external validator, certifier, sealer, authenticator, or solver owner. | `docs/CONTRACT.md` Section 1.10 K-DOMAIN-4 |
>
> The former "7 TBD blockers" around required-human-gate semantics and result-schema hooks are resolved by framework canon. Do not re-derive them locally. Preserve only concrete implementation TBDs: profile instances, concrete schema refs, adapters, operation stores, apply tooling, review-checklist artifact path/schema, and concrete proposal records.
>

### CLM-027 — Terminology Map

> ##### Terminology Map
>
> | Term | Meaning in this deliverable | Current disposition |
> |---|---|---|
> | `status` | Canonical proposal-only posture. | Required value: `proposal_only`. |
> | `lifecycle` | Proposal progression: `draft`, `ready_for_review`, `accepted`, `rejected`, `applied`. | Canonical values; implementation artifacts remain future-gated. |
> | Human gate | The workflow point that prevents accepted/applied lifecycle states without accountable human action. | Required by REF-008 and K-DOMAIN-3. |
> | Explicit human approval | K-AUTH-2-bound human approval evidence for accepted/applied lifecycle states. | Canonical requirement; concrete evidence artifact remains implementation `TBD`. |
> | `required_human_gate` | The `OperationProposal` field naming the required gate. | Required field; concrete value vocabulary may be profile/workflow-specific. |
> | Deterministic result schema | Schema hooks used by validation/apply/check results. | Canonical hooks required; concrete refs published 2026-07-02: `projects/chirality-piping/schemas/operation_outcome.schema.json` (validate/apply), `projects/chirality-piping/schemas/rule_check_run_result.schema.json` (deterministic check); the ADOPTED profile's hook fields await an owner tier-0 CHANGE. |
> | Review checklist result | Future artifact recording schema completeness, protected-path posture, boundary-language review, gate readiness, deterministic-check readiness, and unresolved implementation blockers. | Implementation `TBD` until artifact path/schema is accepted. |
>

### CLM-028 — Example Minimal Proposal Shape

> ##### Example Minimal Proposal Shape
>
> ```json
> {
>   "proposal_id": "TBD",
>   "profile_id": "TBD",
>   "base_state": "TBD",
>   "operation_name": "TBD",
>   "status": "proposal_only",
>   "lifecycle": "draft",
>   "created_at": "TBD",
>   "created_by": "TBD",
>   "input_refs": [],
>   "intended_changes": [],
>   "deterministic_checks": [],
>   "expected_output_refs": [],
>   "risks": [],
>   "assumptions": [],
>   "blockers": [],
>   "boundary_notice": "TBD",
>   "required_human_gate": "TBD",
>   "operation_risk_class": "engine_checkable",
>   "provenance_on_judgment_values": "TBD",
>   "storage_path": "TBD"
> }
> ```
>
> Values are `TBD` because no accepted engine profile, adapter, operation store, or operation instance exists in this future-boundary deliverable.
>

### CLM-029 — Review Checklist

> ##### Review Checklist
>
> | Check | Question |
> |---|---|
> | Base state | Is `base_state` identified and reviewable? |
> | Inputs | Are all `input_refs` identified and reviewable? |
> | Intended changes | Are `intended_changes` specific enough for review? |
> | Deterministic checks | Are checks named, tied to profile schema hooks, and ready to produce deterministic evidence? |
> | Expected outputs | Are `expected_output_refs` proposal/review artifacts or approved adapter outputs, not direct protected-path writes by agents? |
> | Risks/assumptions/blockers | Are known risks, assumptions, and blockers explicit? |
> | Human gate | Is `required_human_gate` explicit, and is accepted/applied blocked until K-AUTH-2-bound approval exists? |
> | Lifecycle | Does `status` remain `proposal_only`, with lifecycle carrying progression? |
> | Review evidence | Does a future checklist result artifact record boundary-language, protected-path, human-gate, deterministic-check, and unresolved implementation-blocker findings or mark the artifact as `TBD`? |
> | Boundary notice | Does the proposal avoid claims of professional approval, code compliance, certification, sealing, authentication, external validation, or Chirality-owned solver truth? |
>

### CLM-030 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-150/151/152 record that tier-0 CHANGE landed, open_pipe_stress and pec are ADOPTED/registered, and the extracted register is reconciled. Proposal-ID semantics, store/checklist artifacts, concrete instances, and declared-section ownership remain genuine TBDs.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-069 OBJ-010 | CLM-008 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
