# Specification: DEL-10-03 OperationProposal Record and Human Gate Workflow

## Scope

This deliverable defines a future-boundary data model and review workflow for `OperationProposal` records. It covers the proposal record shape, proposal-only status, lifecycle, K-AUTH-2-bound human gate, deterministic result-schema hooks, and review checklist for future domain-engine operations.

This deliverable excludes current-release domain operation execution, source types, domain MCP tools, domain adapter implementation, protected-path enforcement implementation, operation stores, apply tooling, and any claim that Chirality owns solver truth. Those items remain future amendment or sibling-deliverable scope.

Primary canon: `_REFERENCES.md` REF-008, `agents/AGENT_DOMAIN_ENGINE.md` pinned at `77a327727`. Under D-T0-01, the framework-root persona is canonical; app-dev `docs/TYPES.md` Section 11 conforms to it and must not weaken framework invariants.

## Requirements

| ID | Requirement | Source | Verification |
|---|---|---|---|
| REQ-10-03-001 | The future `OperationProposal` record MUST include the canonical fields: `proposal_id`, `profile_id`, `base_state`, `operation_name`, `status`, `lifecycle`, `created_at`, `created_by`, `input_refs`, `intended_changes`, `deterministic_checks`, `expected_output_refs`, `risks`, `assumptions`, `blockers`, `boundary_notice`, `required_human_gate`, `operation_risk_class`, `provenance_on_judgment_values`, and `storage_path`. | REF-008; `docs/TYPES.md` Section 11.2 | Compare proposed schema/checklist against the field table. |
| REQ-10-03-002 | `status` MUST be `proposal_only`; lifecycle MUST use `draft | ready_for_review | accepted | rejected | applied`. | REF-008; `docs/TYPES.md` Section 11.2 | Confirm proposal records distinguish status from lifecycle. |
| REQ-10-03-003 | Domain operations MUST be represented as `OperationProposal` records before application. | `docs/PRD.md` Section 8.17 FR-112; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-3 | Review workflow has a proposal-record step before any apply step. |
| REQ-10-03-004 | Accepted/applied lifecycle states MUST require explicit human approval bound to git SHA per K-AUTH-2. | REF-008; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-3 | Review checklist requires K-AUTH-2 evidence before accepted/applied states. |
| REQ-10-03-005 | Applied lifecycle state MUST also require domain-engine-controlled apply or an external terminal acceptance record. | REF-008; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-3 | Future apply workflow records an engine-controlled or external terminal result; absent implementation remains `TBD`. |
| REQ-10-03-006 | Proposal records MUST identify inputs, intended changes, deterministic checks, expected outputs, risks, assumptions, blockers, boundary notice, required gate, risk class, judgment-value provenance, and storage path. | REF-008; `docs/TYPES.md` Section 11.2 | Required fields are present and non-empty or explicitly `TBD` before review. |
| REQ-10-03-007 | Deterministic checks MUST resolve against profile-declared schema hooks: `validate_result_schema`, `apply_result_schema`, and `deterministic_check_result_schema`. | REF-008; `docs/TYPES.md` Section 11.1 | Review checklist blocks implementation readiness when concrete schema refs are missing. |
| REQ-10-03-008 | Agents MUST write proposals, summaries, and review aids, not protected domain-engine model truth. | `docs/PRD.md` Section 8.17 FR-111; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-2 | Review checklist confirms proposed outputs target proposal/review paths, not protected paths. |
| REQ-10-03-009 | Domain-engine outputs MUST NOT be represented as professional approval, code compliance, certification, sealing, authentication, external validation, or solver truth owned by Chirality. | `docs/PRD.md` Section 8.17 FR-115; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-4 | Review checklist includes professional-boundary copy check. |
| REQ-10-03-010 | Concrete evidence artifacts remain future implementation TBDs until accepted: profile instances, concrete schema refs, adapters, operation store, apply tooling, and review-checklist artifact path/schema. | `docs/PLAN.md` R7; `docs/SPEC.md` Section 18; REF-008 | Documentation preserves TBDs for concrete implementation artifacts without weakening canonical lifecycle semantics. |

## Standards

| Standard or Source | Applicability |
|---|---|
| `agents/AGENT_DOMAIN_ENGINE.md` at `77a327727` | Canonical operation-proposal field table, lifecycle, human gate, result-schema hooks, and boundary posture. |
| `docs/TYPES.md` Section 11.2 | App-dev vocabulary target conforming to framework canon. |
| `docs/PRD.md` Section 8.17 | Product requirements for future domain-engine compatibility. |
| `docs/CONTRACT.md` Section 1.10 | Binding app-dev invariants specializing framework K-DOMAIN without weakening it. |
| `docs/SPEC.md` Section 18 | Future API surface context; endpoint behavior details remain gated. |

## Verification

| Check | Method | Result Target |
|---|---|---|
| Schema completeness | Verify every canonical `OperationProposal` field appears in the record shape or checklist. | PASS/TBD |
| Status/lifecycle integrity | Verify `status = proposal_only` and lifecycle values match REF-008. | PASS/TBD |
| Human gate | Verify accepted/applied states require K-AUTH-2-bound human approval. | PASS/TBD |
| Apply result posture | Verify applied state also requires domain-engine-controlled apply or external terminal acceptance record, or remains blocked as implementation `TBD`. | PASS/TBD |
| Result schema hooks | Verify future deterministic checks reference profile-level validation/apply/check result schema hooks. | PASS/TBD |
| Protected path posture | Verify proposal outputs do not directly modify protected domain-engine paths. | PASS/TBD |
| Boundary language | Verify no text claims Chirality approves, certifies, code-validates, externally validates, seals, authenticates, or owns solver truth. | PASS/TBD |
| Future-boundary constraint | Verify implementation activation is excluded until governed amendment. | PASS/TBD |
| Review sufficiency evidence | Verify a future review-checklist result artifact is identified as a true implementation `TBD`, not as an unresolved framework blocker. | PASS/TBD |

## Documentation

Required artifacts for this deliverable:

- Proposal record shape.
- Gate workflow notes.
- Review checklist.

Additional documentation needed before implementation:

- TBD: exact proposal ID generation semantics.
- TBD: concrete `DomainEngineProfile` instance for the target engine.
- RESOLVED by cross-reference (2026-07-02, agent decision under
  `TRB-chirality-app-dev-DEL-10-03-2026-07-02`): concrete refs for the tier-0 engine
  instance are published — `validate_result_schema` / `apply_result_schema` =
  `projects/chirality-piping/schemas/operation_outcome.schema.json` (operation_applier
  `OperationOutcome`; `mode` = `validate_only` / `apply`),
  `deterministic_check_result_schema` =
  `projects/chirality-piping/schemas/rule_check_run_result.schema.json`
  (rule_check_runner `RuleCheckRunResult`); the Rust sources govern on disagreement.
  Residual `TBD`: the ADOPTED profile's hook fields await an owner tier-0 CHANGE
  (`_DomainEngines/profiles/open_pipe_stress.yaml:81,88,101,115`); engines other than
  open_pipe_stress supply their own refs.
- TBD: operation store and `storage_path` convention.
- TBD: adapter validation/apply tooling and result-record location. (Narrowed
  2026-07-02: the validation/apply result envelope is published — see the resolved
  refs above; the tooling and the app-dev-side result-record location remain `TBD`.)
- TBD: review checklist result artifact path/schema.
- TBD: concrete proposal instances and profile-specific boundary notice copy.
