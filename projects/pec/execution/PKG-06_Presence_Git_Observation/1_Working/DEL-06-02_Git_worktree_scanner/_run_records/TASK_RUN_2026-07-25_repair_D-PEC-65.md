# TASK RUN — 2026-07-25 — register evidence repair (D-PEC-65)

| Field | Value |
|---|---|
| Deliverable | DEL-06-02 Git/worktree scanner |
| Package | PKG-06 Presence & Git Observation |
| Instrument | `D-PEC-65` §3.1 (RULED 2026-07-25) |
| Agent | sealed Agent 2 repair dispatch (file-tool-only) |
| File touched | `Dependencies.csv` (EXECUTION rows only) |

## Rows dispositioned

| DependencyID | Defect class | Disposition |
|---|---|---|
| DEP-06-02-001 | ANCHOR (read-only) | untouched |
| DEP-06-02-002 | ANCHOR (read-only) | untouched |
| DEP-06-02-003 | EVQ-003 + EVQ-004 (empty quote, `location TBD`) | REPAIRED |

## Cells changed

**DEP-06-02-003** (→ DEL-01-02 Presence-tier schema & entity model)
- `EvidenceFile`: `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` → `execution/_Decomposition/SOFTWARE_DECOMP.md`
- `SourceRef`: `location TBD` → `SOFTWARE_DECOMP.md §2.1 SSOW row SOW-002`
- `EvidenceQuote`: (empty) → `Implement the presence-tier entity model: Session, Worktree/GitRef, PresenceRecord, HierarchyEdge, ScopeClaim`
- Warrant: SOW-002 (→ DEL-01-02 in `ScopeLedger.csv`) defines the
  `Worktree/GitRef` presence-tier entity this scanner writes.

## Statement edits flagged

None in this file.

## Waivers declared

None. The row carries real quotable accepted-truth evidence.
