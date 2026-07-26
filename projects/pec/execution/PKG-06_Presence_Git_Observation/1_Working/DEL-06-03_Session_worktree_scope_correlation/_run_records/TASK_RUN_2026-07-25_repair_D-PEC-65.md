# TASK RUN — 2026-07-25 — register evidence repair (D-PEC-65)

| Field | Value |
|---|---|
| Deliverable | DEL-06-03 Session×worktree×scope correlation |
| Package | PKG-06 Presence & Git Observation |
| Instrument | `D-PEC-65` §3.1 (RULED 2026-07-25) |
| Agent | sealed Agent 2 repair dispatch (file-tool-only) |
| File touched | `Dependencies.csv` (EXECUTION rows only) |

## Rows dispositioned

| DependencyID | Defect class | Disposition |
|---|---|---|
| DEP-06-03-001 | ANCHOR (read-only) | untouched |
| DEP-06-03-002 | ANCHOR (read-only) | untouched |
| DEP-06-03-003 | EVQ-003 + EVQ-004 (empty quote, `location TBD`) | REPAIRED |
| DEP-06-03-004 | EVQ-003 + EVQ-004 (empty quote, `location TBD`) | REPAIRED |

## Cells changed

**DEP-06-03-003** (→ DEL-06-01 Session presence records)
- `EvidenceFile`: PLAN exhibit → `execution/_Decomposition/Deliverables.csv`
- `SourceRef`: `location TBD` → `Deliverables.csv row DEL-06-01 (Description)`
- `EvidenceQuote`: (empty) → `Harness-reported session records (kind, engine/model attribution, role, loop/package binding, declared write scopes); identity/lifecycle stay daemon-owned.`
- Warrant: the target deliverable produces the session records (including
  declared write scopes) that the correlation joins.

**DEP-06-03-004** (→ DEL-06-02 Git/worktree scanner)
- `EvidenceFile`: PLAN exhibit → `execution/_Decomposition/Deliverables.csv`
- `SourceRef`: `location TBD` → `Deliverables.csv row DEL-06-02 (Description)`
- `EvidenceQuote`: (empty) → `Read-only scan of worktrees, branches, HEAD, ahead/behind, dirty path names/counts; never content.`
- Warrant: the target deliverable produces the worktree/branch scan results
  the correlation joins.

## Statement edits flagged

None in this file.

## Waivers declared

None. Both rows carry real quotable accepted-truth evidence.
