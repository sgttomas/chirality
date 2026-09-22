# Dependencies: DEL-10-03 OperationProposal Record and Human Gate Workflow

## Dependency Tracking

| Field | Value |
|---|---|
| ProjectMode | FULL_GRAPH |
| SatisfactionThreshold | SEMANTIC_READY |
| StructuredRegister | `Dependencies.csv` v3.1 |
| InitialPopulationRule | Run `TASK + dependency-extract` after four-document authoring per human ruling on 2026-05-20; semantic lensing and P3 enrichment are skipped for dependency recording. |

## Declared Upstream

Descriptive mirror of `Dependencies.csv` (2026-09-22; no formal edge or basis change):

- `DEP-10-03-001` — OTHER; Domain Engine Future Boundary; SATISFIED.
- `DEP-10-03-002` — OTHER; OperationProposal records; SATISFIED.
- `DEP-10-03-003` — OTHER; Future domain-engine compatibility; SATISFIED.
- `DEP-10-03-004` — PREREQUISITE; Accepted future amendment authorizing domain-engine operation workflow implementation; PENDING.
- `DEP-10-03-005` — PREREQUISITE; Accepted DomainEngineProfile for the target engine; SATISFIED.
- `DEP-10-03-006` — PREREQUISITE; Protected Path and Proposal Path Policy; SATISFIED.
- `DEP-10-03-007` — PREREQUISITE; Deterministic adapter or validation tool for the operation; SATISFIED.
- `DEP-10-03-008` — CONSTRAINT; Explicit human gate definition and acceptance evidence; SATISFIED.

## Declared Downstream

No downstream-directed row is recorded in this local structured register; this does not assert absence of consumers elsewhere.

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
- 2026-07-18 D-APP-65 ruling (authority `execution/_Coordination/_DECISIONS/D-APP-65_PACKET_ACCEPTED_RECOMMENDATIONS_2026-07-18.md` §4 disposition 3): the "whether" question left open by the D-APP-53 annotation on DEP-10-03-004 is resolved — the owner ruled that D-APP-50/51/52 are **precursors to, not** the accepted amendment authorizing domain-engine operation-workflow implementation; the amendment remains a future owner act. The row's note now names the precursor set, `LastSeen` bumped to 2026-07-18, and the row **remains `PENDING` by design** as the defined future gate (`Status` `ACTIVE` unchanged); F-APP-3 reaffirmed. Schema linter PASS (8 rows, 0 errors, 0 warnings). No lifecycle transition (F-APP-4).

## Extracted Dependency Register

| DependencyID | Class | Type | Direction | Target | Status | Evidence |
|---|---|---|---|---|---|---|
| DEP-10-03-001 | ANCHOR | OTHER | UPSTREAM | PKG-10 | ACTIVE | SATISFIED |
| DEP-10-03-002 | ANCHOR | OTHER | UPSTREAM | SOW-069 | ACTIVE | SATISFIED |
| DEP-10-03-003 | ANCHOR | OTHER | UPSTREAM | OBJ-010 | ACTIVE | SATISFIED |
| DEP-10-03-004 | EXECUTION | PREREQUISITE | UPSTREAM | TBD | ACTIVE | PENDING |
| DEP-10-03-005 | EXECUTION | PREREQUISITE | UPSTREAM | open_pipe_stress; pec | ACTIVE | SATISFIED |
| DEP-10-03-006 | EXECUTION | PREREQUISITE | UPSTREAM | DEL-10-02 | ACTIVE | SATISFIED |
| DEP-10-03-007 | EXECUTION | PREREQUISITE | UPSTREAM | TBD | ACTIVE | SATISFIED |
| DEP-10-03-008 | EXECUTION | CONSTRAINT | UPSTREAM | TBD | ACTIVE | SATISFIED |

Counts: 8 ACTIVE rows; 3 ANCHOR rows; 5 EXECUTION rows; 0 RETIRED rows.

## Lifecycle Summary

Current structured-register mirror: 1 PENDING, 7 SATISFIED. Lifecycle labels and SatisfactionStatus are distinct; the complete formal register remains unchanged. Earlier run summaries below describe their dated basis.

## Run History

| Timestamp | Mode | Strictness | Decomposition | Warnings | ACTIVE Counts |
|---|---|---|---|---|---|
| 2026-05-20T21:07:16-0600 | UPDATE | CONSERVATIVE | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` located | HASH_MISMATCH_SOURCE; UNKNOWN_TARGETS | ANCHOR=3; EXECUTION=5; TOTAL=8 |
| 2026-07-10 | RECONCILIATION (D-APP-53) | n/a | located; anchors re-verified | 7 rows SATISFIED; DEP-10-03-004 annotate-only (owner-gated); REF-006 now MATCH; linter PASS 0/0 | ANCHOR=3; EXECUTION=5; TOTAL=8 |
| 2026-07-18 | RULING ANNOTATION (D-APP-65) | n/a | n/a (single-row note append) | DEP-10-03-004 note appended (precursors-not-amendment; stays PENDING as defined future gate; F-APP-3 reaffirmed); linter PASS 0/0 | ANCHOR=3; EXECUTION=5; TOTAL=8 |

## Current evidence navigation — 2026-09-22

Current contract carrier: `ScopeOfWork.md`; former Datasheet/Specification/Procedure/Guidance labels and old line anchors in formal rows are retained historical evidence locators. Current generic type source is `projects/chirality-runtime/packages/contracts/src/harness/domain-profile.ts`, consumed as `@chirality/runtime-contracts`; D-APP-118 retires the App facade. Retained registry/proposal tests are not proof of live Codex exposure. Formal row evidence/pin/LastSeen changes require the owning dependency reconciliation and are outside this record repair.

## Current evidence-locator refresh — 2026-09-22

3 formal rows now cite exact current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See `DDEPEND_PREVIEW_LOCATORS.csv` and the home `DDEPEND_CHANGES.csv`.

## Current evidence-locator refresh — 2026-09-22

3 formal rows now cite current `ScopeOfWork.md` quote spans and their containing headings where former standalone four-document sources were absorbed. Dependency IDs, classes, targets, Status and SatisfactionStatus are unchanged. Former file names and quotes remain in row Notes. This locator correction is not a new fulfillment or current implementation claim. See the selected `DDEPEND_PREVIEW*.csv` and the home `DDEPEND_CHANGES.csv`.

## Current dependency refresh — 2026-09-22

`TASK + bundled:chirality-root/dependency-extract`; `MODE=UPDATE`; `STRICTNESS=CONSERVATIVE`; `CONSUMER_CONTEXT=RECONCILIATION`; decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (accepted product descriptions frozen; no repin). Current ScopeOfWork.md, _CONTEXT.md, _REFERENCES.md and the accepted D-GOV-43/D-APP-127/131 boundary were read before this register update. Exact field postimages were previewed in `DDEPEND_PREVIEW.csv` and independently checked by WORKING_ITEMS before mutation. Existing IDs and declared provenance remain. Historical source wording/quotes are retained in row Notes. No native check, acceptance, or satisfaction change is inferred.

Rows now: ACTIVE=8; RETIRED=0; ACTIVE parent anchors=1. The active summary table above mirrors these formal rows. Historical run notes and dated tables below preserve their original context.
