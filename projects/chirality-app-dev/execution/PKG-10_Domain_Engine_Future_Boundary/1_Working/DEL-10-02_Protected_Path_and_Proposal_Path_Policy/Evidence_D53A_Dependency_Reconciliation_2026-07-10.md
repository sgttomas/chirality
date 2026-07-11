# Evidence: D-APP-53 Dependency Reconciliation - DEL-10-02 (DRQ-07)

**Date:** 2026-07-10
**Deliverable:** DEL-10-02 Protected Path and Proposal Path Policy (PKG-10)
**Queue row:** DRQ-07 of `plans/PLAN_2026-07-10_pre_issuance_dependency_reconciliation.md`
**Authority:** `execution/_Coordination/_DECISIONS/D-APP-53_RULING_2026-07-10.md` (Option A, no riders)
**Register:** `Dependencies.csv` v3.1 (5 rows: 4 ACTIVE, 1 RETIRED)

## Epistemic status (disclaimer)

This is a derivative reconciliation record. It does not replace decomposition truth, source/test
evidence, decision records, or human lifecycle approvals. It authorizes no issuance: no
`CHECKING -> ISSUED` transition occurred or is implied (F-APP-4), `_STATUS.md` was not touched, and
no domain-engine implementation occurred (F-APP-3). All judgments rest on live-filesystem
verification performed 2026-07-10 in the DRQ-07 worktree.

## Per-row reconciliation

Open-row scope: DEP-10-02-003 and DEP-10-02-005 (rows -001/-002 already SATISFIED; -004 RETIRED
2026-05-24 under RUL-SCC-002-004 — untouched).

| DependencyID | Prior status | New status | Basis / left-open reason |
|---|---|---|---|
| DEP-10-02-003 | TBD | SATISFIED | The prerequisite `DomainEngineProfile` contract has materialized: canon `agents/AGENT_DOMAIN_ENGINE.md@77a327727`; inert type mirror `frontend/packages/harness-contract/src/domain-profile.ts` declaring `protected_write_paths`/`agent_writable_paths` (lines 120-121); ADOPTED instance `_DomainEngines/profiles/open_pipe_stress.yaml` (owner Gate 2, D-T0-06) with live `protected_write_paths` block. Closure attests the contract prerequisite only — target deliverable DEL-10-01 remains `_STATUS.md` CHECKING; no issuance implied. `ProposedMaturity=SEMANTIC_READY`; `LastSeen=2026-07-10`. |
| DEP-10-02-005 | TBD | TBD (left open) | Per plan §3.5: no live evidence exists for concrete protected/proposal path glob syntax or the exact hook API; the ADOPTED profile's hook/schema detail fields remain TBD pending an owner tier-0 CHANGE. Notes annotated with the live state; `LastSeen` bumped; `SatisfactionStatus` unchanged. |

## Hygiene

1. **`_DEPENDENCIES.md` summary desync repaired** (dated 2026-07-10 correction, history retained):
   the Counts and Lifecycle Summary tables still showed Status ACTIVE 5 / RETIRED 0 although the
   CSV has carried `DEP-10-02-004` as RETIRED since 2026-05-24 (RUL-SCC-002-004). Now synced:
   ACTIVE 4 / RETIRED 1; SatisfactionStatus SATISFIED 3 / TBD 1 / NOT_APPLICABLE (retired) 1. The
   Extracted Dependency Register table row for -004 now shows RETIRED with the retirement basis.
2. **Stale REF-006 posture noted:** the 2026-05-20 run-note hash-mismatch warning is historical;
   this deliverable's `_REFERENCES.md` now records REF-006 `docs/PRD.md` MATCH.
3. Run History appended with the 2026-07-10 reconciliation entry.

## Validation

`python3 projects/chirality-app-dev/execution/_Scripts/validate_dependencies.py .../DEL-10-02_Protected_Path_and_Proposal_Path_Policy/Dependencies.csv`
-> Status: PASS, Rows: 5, Errors: 0, Warnings: 0 (run 2026-07-11T02:19:44Z UTC = 2026-07-10 local).
