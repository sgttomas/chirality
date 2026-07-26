# TASK RUN — 2026-07-25 — register evidence repair (D-PEC-65)

| Field | Value |
|---|---|
| Deliverable | DEL-06-01 Session presence records |
| Package | PKG-06 Presence & Git Observation |
| Instrument | `D-PEC-65` §3.1 (RULED 2026-07-25) |
| Agent | sealed Agent 2 repair dispatch (file-tool-only) |
| File touched | `Dependencies.csv` (EXECUTION rows only) |

## Rows dispositioned

| DependencyID | Defect class | Disposition |
|---|---|---|
| DEP-06-01-001 | ANCHOR (read-only) | untouched |
| DEP-06-01-002 | ANCHOR (read-only) | untouched |
| DEP-06-01-003 | EVQ-003 + EVQ-004 (empty quote, `location TBD`) | REPAIRED |
| DEP-06-01-004 | EVQ-001 (locus/quote duplication) | REPAIRED |

## Cells changed

**DEP-06-01-003** (→ DEL-01-02 Presence-tier schema & entity model)
- `EvidenceFile`: `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` → `execution/_Decomposition/Deliverables.csv`
- `SourceRef`: `location TBD` → `Deliverables.csv row DEL-01-02 (Description)`
- `EvidenceQuote`: (empty) → `Schema and types for Session, Worktree/GitRef, PresenceRecord, HierarchyEdge, ScopeClaim; expected-loss-on-rebuild semantics.`
- Warrant: the target deliverable's register row defines the Session and
  PresenceRecord types this deliverable's presence writer instantiates.

**DEP-06-01-004** (→ DEL-07-03 Hooks CLI bridge)
- `EvidenceFile`: PLAN exhibit → `execution/_Decomposition/SOFTWARE_DECOMP.md`
- `SourceRef`: duplicated quote text → `SOFTWARE_DECOMP.md §2.1 SSOW row SOW-036`
- `EvidenceQuote`: duplicated locus text → `Implement the harness hooks CLI bridge (session start/stop, status, scope declaration), declared and attributable`
- Warrant: SOW-036 (→ DEL-07-03 in `ScopeLedger.csv`) is the bridge that
  carries session start/stop and scope declaration — the presence facts
  DEL-06-01 records.

## Statement edits flagged

None in this file.

## Waivers declared

None. Both rows carry real quotable accepted-truth evidence; no
`Dependencies_EvidenceWaivers.csv` was created.
