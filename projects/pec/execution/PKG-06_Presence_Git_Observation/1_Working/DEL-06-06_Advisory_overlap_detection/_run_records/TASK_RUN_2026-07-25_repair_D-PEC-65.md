# TASK RUN — 2026-07-25 — register evidence repair (D-PEC-65)

| Field | Value |
|---|---|
| Deliverable | DEL-06-06 Advisory overlap detection |
| Package | PKG-06 Presence & Git Observation |
| Instrument | `D-PEC-65` §3.1 (RULED 2026-07-25) |
| Agent | sealed Agent 2 repair dispatch (file-tool-only) |
| File touched | `Dependencies.csv` (EXECUTION rows only) |

## Rows dispositioned

| DependencyID | Defect class | Disposition |
|---|---|---|
| DEP-06-06-001 | ANCHOR (read-only) | untouched |
| DEP-06-06-002 | ANCHOR (read-only) | untouched |
| DEP-06-06-003 | EVQ-003 + EVQ-004 (empty quote, `location TBD`) | REPAIRED |

## Cells changed

**DEP-06-06-003** (→ DEL-06-03 Session×worktree×scope correlation)
- `EvidenceFile`: `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` → `execution/_Decomposition/SOFTWARE_DECOMP.md`
- `SourceRef`: `location TBD` → `SOFTWARE_DECOMP.md §2.1 SSOW row SOW-031`
- `EvidenceQuote`: (empty) → `Detect and surface advisory overlaps (write scopes, shared branches, same merge target) without ever blocking`
- Warrant: SOW-031 (this deliverable's own scope item) names the inputs
  overlap detection must compare — declared write scopes and shared branches
  per session — which are exactly the session × worktree × declared-scope
  join DEL-06-03 produces.

## Statement edits flagged

None in this file.

## Waivers declared

None. The row carries real quotable accepted-truth evidence.
