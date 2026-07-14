# Dependencies: DEL-10-03 OperationProposal Record and Human Gate Workflow

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

TBD - no accepted dependency edges have been extracted yet.

## Declared Downstream

TBD - no accepted dependency edges have been extracted yet.

## Run Notes

- ORCHESTRATOR initialized this file during PREPARATION scaffolding on 2026-05-20.
- Do not compute blocked/available state for this deliverable until `Dependencies.csv` exists and the project-level FULL_GRAPH register has been checked for cycles.
- 2026-05-20 dependency-extract UPDATE used `STRICTNESS=CONSERVATIVE`, `CONSUMER_CONTEXT=NONE`, `SCOPE=DEL-10-03`, `RUN_ROOT=/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/execution`, and decomposition authority `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- Source documents used: `_CONTEXT.md`, `_REFERENCES.md`, `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, existing `_DEPENDENCIES.md`, and the decomposition authority. `_SEMANTIC.md` was not read or consumed by human ruling.
- Anchor doc selected: `Datasheet.md` with `_CONTEXT.md` and decomposition cross-checks. Execution doc order selected: `Procedure.md`, `Specification.md`, `Guidance.md`, `Datasheet.md`.
- PKG-10 future-boundary/gated posture preserved: extracted rows do not activate domain-engine work and keep future implementation targets as `UNKNOWN`/`TBD` unless an explicit source names a deliverable.
- `[WARNING] HASH_MISMATCH_SOURCE`: `_REFERENCES.md` records a hash mismatch for `docs/PRD.md`; dependency extraction used only accessible deliverable-local summaries and recorded this as a warning, not an accepted-source repair.
- `[WARNING] UNKNOWN_TARGETS`: Future amendment authority, accepted target-engine profile, deterministic adapter/tool contract, and human gate evidence format remain `UNKNOWN`/`TBD`.
- 2026-07-10 D-APP-53 reconciliation (plan DRQ-08; authority `execution/_Coordination/_DECISIONS/D-APP-53_RULING_2026-07-10.md`, Option A): rows re-verified against the live tree. Closed `PENDING -> SATISFIED`: DEP-10-03-001/-002/-003 (anchors live in decomposition), -005 (ADOPTED `open_pipe_stress.yaml`, D-T0-06; registry D-APP-51), -006 (sibling DEL-10-02 policy authored and reconciled; adopted-profile path blocks), -007 (`validate_domain_engine_profile.py`; `domain-proposal-tools.ts` D-APP-52; operation_outcome/rule_check_run_result schemas), -008 (`operation-proposal.ts` `required_human_gate`; K-DOMAIN-3/K-AUTH-2 SHA-bound approval evidence). DEP-10-03-004 annotate-only per plan §3.5 (whether D-APP-50/51/52 constitute the accepted amendment is an owner call; F-APP-3 reaffirmed) — stays PENDING. Dated correction: the 2026-05-20 UNKNOWN_TARGETS warning is now partially resolved (profile, adapter/tool, and gate-evidence targets have live evidence); the future-amendment target remains the open owner-gated item. See `Evidence_D53A_Dependency_Reconciliation_2026-07-10.md`. No lifecycle transition (F-APP-4).

## Extracted Dependency Register

| DependencyID | Class | Type | Direction | Target | Status | Evidence |
|---|---|---|---|---|---|---|
| DEP-10-03-001 | ANCHOR | OTHER | UPSTREAM | PKG-10 Domain Engine Future Boundary | ACTIVE | `_CONTEXT.md` |
| DEP-10-03-002 | ANCHOR | OTHER | UPSTREAM | SOW-069 OperationProposal records | ACTIVE | decomposition scope ledger |
| DEP-10-03-003 | ANCHOR | OTHER | UPSTREAM | OBJ-010 Future domain-engine compatibility | ACTIVE | `Datasheet.md` |
| DEP-10-03-004 | EXECUTION | PREREQUISITE | UPSTREAM | Accepted future amendment authorizing domain-engine operation workflow implementation | ACTIVE | `Procedure.md` |
| DEP-10-03-005 | EXECUTION | PREREQUISITE | UPSTREAM | Accepted DomainEngineProfile for the target engine | ACTIVE | `Procedure.md` |
| DEP-10-03-006 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-10-02 Protected Path and Proposal Path Policy | ACTIVE | `Procedure.md` |
| DEP-10-03-007 | EXECUTION | PREREQUISITE | UPSTREAM | Deterministic adapter or validation tool for the operation | ACTIVE | `Procedure.md` |
| DEP-10-03-008 | EXECUTION | CONSTRAINT | UPSTREAM | Explicit human gate definition and acceptance evidence | ACTIVE | `Specification.md`; `Procedure.md` |

Counts: 8 ACTIVE rows; 3 ANCHOR rows; 5 EXECUTION rows; 0 RETIRED rows.

## Lifecycle Summary

| Status | Count |
|---|---:|
| ACTIVE | 8 |
| RETIRED | 0 |

| SatisfactionStatus | Count |
|---|---:|
| SATISFIED | 7 |
| PENDING | 1 |

(Synced to CSV state 2026-07-10, D-APP-53 reconciliation; previously PENDING 8. The remaining PENDING row is owner-gated DEP-10-03-004.)

| DependencyClass | Count |
|---|---:|
| ANCHOR | 3 |
| EXECUTION | 5 |

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE Counts |
|---|---|---|---|---|---|
| 2026-05-20T21:07:16-0600 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` located | HASH_MISMATCH_SOURCE; UNKNOWN_TARGETS | ANCHOR=3; EXECUTION=5; TOTAL=8 |
| 2026-07-10 | RECONCILIATION (D-APP-53) | n/a | located; anchors re-verified | 7 rows SATISFIED; DEP-10-03-004 annotate-only (owner-gated); REF-006 now MATCH; linter PASS 0/0 | ANCHOR=3; EXECUTION=5; TOTAL=8 |
