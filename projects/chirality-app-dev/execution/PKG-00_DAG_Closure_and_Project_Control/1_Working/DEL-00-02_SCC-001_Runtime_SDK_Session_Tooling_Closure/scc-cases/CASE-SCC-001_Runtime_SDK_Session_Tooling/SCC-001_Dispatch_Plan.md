# SCC-001 Dispatch Plan

## Baseline

Accepted upstream snapshot: `execution/_Reconciliation/DepClosure/CLOSURE_SCC002_CHANGE_HANDOFF_2026-05-24_2020/`

SCC-001 remains the only strict active execution SCC:

- `scc_count = 1`
- 18 nodes
- 55 active internal concrete rows
- 12 bidirectional pairs

This case remains a control-plane evidence package. It does not initiate SCOPE_CHANGE, does not mutate product dependency registers, and does not close SCC-001.

## Sequential First Step

RECONCILIATION owns the normalized ruling workbook:

- `SCC-001_Ruling_Workbook.csv`

The workbook is the next decision surface. It indexes the 12 bidirectional pairs plus longer-cycle cross-links that can keep SCC-001 alive after pair-level cleanup.

## Parallel Evidence Batches

The following batches can run in parallel because they are read-only evidence classification tasks:

| Batch | Scope | Inputs | Output |
|---|---|---|---|
| Runtime/SDK core | `DEL-03-*`, `DEL-04-*` rows from packet `002` | Seed packet, dependency rows, `Task_Findings.csv` | Row classification proposals for `REM-SCC-001-005` through `009` |
| Session/audit records | `DEL-03-04`, `DEL-04-05`, `DEL-05-*` rows from packet `003` | Seed packet, dependency rows, `Task_Findings.csv` | Row classification proposals for `REM-SCC-001-010` through `012` plus adjacent storage/artifact links |
| Tooling/permissions/MCP | `DEL-06-*` rows from packet `004` plus `DEL-06-06` cross-links | Seed packet, dependency rows, `Task_Findings.csv` | Row classification proposals for `REM-SCC-001-013` through `016` plus cross-link findings |

Parallel outputs are findings only. They are not rulings and do not authorize edits.

## Sequential Gates

Run these one at a time because they affect downstream row treatment:

1. `DEL-04-01` SDK probe/version treatment, including `DEP-04-01-008` already `SATISFIED` while still `ACTIVE`.
2. `DEL-03-04` terminal taxonomy and low-confidence prerequisite rows.
3. `DEL-05-02` HarnessEvent writer/API ownership.
4. `DEL-06-01` permission-policy ownership before finalizing `DEL-06-02`, `DEL-06-03`, or `DEL-06-04`.
5. `DEL-06-04` write/edit enforcement ownership before finalizing `DEL-06-06`.

## Mutation And Closure Rules

- RECONCILIATION converts evidence into row-level ruling options.
- Human rulings decide any governance ambiguity or SCOPE_CHANGE referral.
- CHANGE applies only approved schema-compatible edits in owning product `Dependencies.csv` files.
- AUDIT_DEP_CLOSURE runs only after accepted owner workflow output exists.
- SCC-001 is not closed until a new immutable DepClosure snapshot reports `scc_count = 0`.

## First Recommended Tranche

The first CHANGE-ready tranche should be small and high-confidence:

1. `DEP-04-01-008` active/satisfied treatment.
2. Reciprocal interface-evidence rows already bucketed as `DEPENDENCY_WORKFLOW_READY`.
3. One independent PKG-06 permission tranche after `DEL-06-01` ownership is ruled.

If DepClosure shrinks SCC-001 but does not close it, repeat the workbook process on the residual SCC rather than editing the entire 55-row internal graph at once.
