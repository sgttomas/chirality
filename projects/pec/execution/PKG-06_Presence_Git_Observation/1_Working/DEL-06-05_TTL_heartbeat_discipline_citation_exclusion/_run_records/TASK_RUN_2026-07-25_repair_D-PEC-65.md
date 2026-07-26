# TASK RUN — 2026-07-25 — register evidence repair (D-PEC-65)

| Field | Value |
|---|---|
| Deliverable | DEL-06-05 TTL/heartbeat discipline & citation exclusion |
| Package | PKG-06 Presence & Git Observation |
| Instrument | `D-PEC-65` §3.1 (RULED 2026-07-25) |
| Agent | sealed Agent 2 repair dispatch (file-tool-only) |
| File touched | `Dependencies.csv` (EXECUTION rows only) |

## Rows dispositioned

| DependencyID | Defect class | Disposition |
|---|---|---|
| DEP-06-05-001 | ANCHOR (read-only) | untouched |
| DEP-06-05-002 | ANCHOR (read-only) | untouched |
| DEP-06-05-003 | ANCHOR (read-only) | untouched |
| DEP-06-05-004 | EVQ-003 + EVQ-004 (empty quote, `location TBD`) | REPAIRED |

## Cells changed

**DEP-06-05-004** (→ DEL-06-01 Session presence records)
- `EvidenceFile`: `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` → `execution/_Decomposition/SOFTWARE_DECOMP.md`
- `SourceRef`: `location TBD` → `SOFTWARE_DECOMP.md §2.1 SSOW row SOW-030`
- `EvidenceQuote`: (empty) → `Carry TTLs and last-heartbeat age on presence records; never assert liveness beyond last heartbeat`
- Warrant: SOW-030 (this deliverable's own scope item) states that TTLs and
  heartbeat age are carried *on presence records* — the records DEL-06-01
  produces.

## Statement edits flagged

None in this file.

## Waivers declared

None. The row carries real quotable accepted-truth evidence.
