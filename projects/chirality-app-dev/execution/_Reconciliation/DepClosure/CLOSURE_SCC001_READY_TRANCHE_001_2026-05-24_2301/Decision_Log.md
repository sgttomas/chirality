# Decision Log - SCC-001 Ready Tranche 001

## Defaults

- `FILTER_ACTIVE_ONLY = true`
- `NORMALIZE_IDS = true`
- Edge filter: `DependencyClass = EXECUTION`, `TargetType = DELIVERABLE`
- Scope: ALL

## Human / Governance Decisions Applied

- Use RECONCILIATION as dependency governance owner for SCC-001.
- Use CHANGE as mutation owner for approved dependency-row edits.
- Do not initiate SCOPE_CHANGE.
- Do not amend decomposition truth or product text.
- Treat this tranche as graph reduction, not final closure.

## Row Treatment Decision Applied Before Audit

CHANGE retired the selected non-blocking or already-satisfied rows named in `Brief.md` using schema-compatible `Status=RETIRED` and `SatisfactionStatus=NOT_APPLICABLE`.

## Audit Decision

The snapshot is accepted as evidence of graph reduction only. SCC-001 closure is not claimed because `Evidence/closure_summary.json` reports `scc_count = 2`.
