# Datasheet: DEL-10-03 OperationProposal Record and Human Gate Workflow

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-10-03 |
| DeliverableName | OperationProposal Record and Human Gate Workflow |
| PackageID | PKG-10 |
| PackageName | Domain Engine Future Boundary |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| Type | DATA_MODEL_CHANGE |
| ResponsibleParty | TBD |
| ScopeItem | SOW-069 |
| SupportedObjective | OBJ-010 |
| ContextEnvelope | M |
| Current posture | Future-boundary workflow contract, not current implementation |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Boundary posture | Future platform compatibility; not current-release domain operation execution. | `_CONTEXT.md`; `docs/PRD.md` Section 8.17 |
| Record type | `OperationProposal` future domain operation proposal record. | REF-008; `docs/TYPES.md` Section 11.2 |
| Required identity/control fields | `proposal_id`, `profile_id`, `base_state`, `operation_name`, `status`, `lifecycle`, `created_at`, `created_by`, `storage_path`. | REF-008; `docs/TYPES.md` Section 11.2 |
| Required review fields | `input_refs`, `intended_changes`, `deterministic_checks`, `expected_output_refs`, `risks`, `assumptions`, `blockers`, `boundary_notice`, `required_human_gate`, `operation_risk_class`, `provenance_on_judgment_values`. | REF-008; `docs/TYPES.md` Section 11.2 |
| Proposal-only status | `status` is `proposal_only`. | REF-008; `docs/TYPES.md` Section 11.2 |
| Lifecycle enum | `draft`, `ready_for_review`, `accepted`, `rejected`, `applied`. | REF-008; `docs/TYPES.md` Section 11.2 |
| Gate requirement | Accepted/applied lifecycle states require explicit human approval bound to git SHA per K-AUTH-2. | REF-008; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-3 |
| Apply requirement | Applied lifecycle state also requires domain-engine-controlled apply or external terminal acceptance record. | REF-008; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-3 |
| Result schema hooks | Proposal checks route through profile-declared `validate_result_schema`, `apply_result_schema`, and deterministic-check result schema hooks. | REF-008; `docs/TYPES.md` Section 11.1 |
| Domain-truth ownership | Domain engines own authoritative domain truth; Chirality governs interaction, proposals, records, and human gates. | `docs/CONTRACT.md` Section 1.10 K-DOMAIN-1 |
| Protected path relationship | Agents write proposals, summaries, and review aids, not protected domain-engine model truth. | `docs/PRD.md` Section 8.17; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-2 |
| Professional boundary | Domain-engine output must not be represented as professional approval, code compliance, certification, sealing, authentication, external validation, or solver truth owned by Chirality. | `docs/PRD.md` Section 8.17; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-4 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Activation condition | Future amendment required before domain-engine operation execution is active. | `docs/PLAN.md` R7; `_CONTEXT.md` Package Scope |
| Current implementation state | Domain-engine implementation is not activated by this deliverable. | D-APP-39 F3; `docs/SPEC.md` Section 18 |
| Upstream precedence | Framework-root `AGENT_DOMAIN_ENGINE.md` at `77a327727` is canonical; app-dev `docs/TYPES.md` Section 11 conforms to it. | D-T0-01; REF-008 |
| Resolved former blockers | Required-human-gate semantics and result-schema hooks are resolved by canon; concrete result-schema refs published 2026-07-02 (`projects/chirality-piping/schemas/operation_outcome.schema.json`, `projects/chirality-piping/schemas/rule_check_run_result.schema.json`); remaining evidence artifacts (operation store, records, review checklist) implementation `TBD`. | REF-008; D-T0-01; piping DEL-10-03 |
| Upstream dependencies | TBD - no accepted dependency edges have been extracted. | `_DEPENDENCIES.md` |
| Downstream dependencies | TBD - no accepted dependency edges have been extracted. | `_DEPENDENCIES.md` |

## Construction

| Component | Description | Source |
|---|---|---|
| Proposal record shape | Future `OperationProposal` table with canonical fields and proposal-only status. | REF-008; `docs/TYPES.md` Section 11.2 |
| Base state | Identifies the accepted state or artifact baseline against which a proposal is made. | REF-008 |
| Deterministic checks | Proposal field listing checks expected before review; the check result payload is published 2026-07-02 (`projects/chirality-piping/schemas/rule_check_run_result.schema.json`); the ADOPTED profile's hook refs remain `TBD` pending an owner tier-0 CHANGE. | REF-008; `docs/PRD.md` Section 8.17; piping DEL-10-03 |
| Human gate workflow | Proposal cannot reach accepted/applied lifecycle states without K-AUTH-2-bound human approval. | REF-008; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-3 |
| Review checklist | Must verify field completeness, base state, deterministic checks, outputs, risks, assumptions, blockers, required human gate, protected-path posture, and professional-boundary language. | REF-008; `docs/PRD.md` Section 8.17 |

## References

- `_CONTEXT.md`
- `_DEPENDENCIES.md`
- `_REFERENCES.md`
- `agents/AGENT_DOMAIN_ENGINE.md` pinned at `77a327727`
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
- `docs/CONTRACT.md` Section 1.10
- `docs/DIRECTIVE.md` professional and domain-boundary principles
- `docs/PLAN.md` future domain-engine items
- `docs/PRD.md` Section 8.17
- `docs/SPEC.md` domain endpoint list and future profile note
- `docs/TYPES.md` Sections 11.1-11.3

## D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-150/151/152 record that tier-0 CHANGE landed, open_pipe_stress and pec are ADOPTED/registered, and the extracted register is reconciled. Proposal-ID semantics, store/checklist artifacts, concrete instances, and declared-section ownership remain genuine TBDs.
