# TASK RUN — D-PEC-65 register evidence repair (DEL-09-01)

- **Date:** 2026-07-25
- **Instrument:** `execution/_Coordination/_DECISIONS/D-PEC-65_register_evidence_repair.md` (RULED §7)
- **Agent:** sealed ephemeral Agent 2 repair dispatch (file-tool-only), package `PKG-09_Dashboards`
- **File touched:** `Dependencies.csv` (EXECUTION rows only; ANCHOR rows read-only)

## Rows dispositioned

| DependencyID | Class found | Disposition | EvidenceFile after |
|---|---|---|---|
| DEP-09-01-003 | DUP (EVQ-001) | REPAIRED | `execution/_Decomposition/Deliverables.csv` |
| DEP-09-01-004 | DUP (EVQ-001) | REPAIRED | `execution/_Decomposition/Deliverables.csv` |
| DEP-09-01-005 | DUP (EVQ-001) | REPAIRED | `execution/_Decomposition/ScopeLedger.csv` |
| DEP-09-01-006 | DUP (EVQ-001) | REPAIRED | `execution/_Decomposition/Deliverables.csv` |

Counts: 4 EXECUTION rows inspected, 4 repaired, 0 waived, 0 already-clean,
0 blocked. 2 ANCHOR rows untouched.

## Cells changed

All four rows: `EvidenceFile` re-pointed off the frozen D-PEC-62 PLAN exhibit
onto the accepted rev-1.2 registers; `SourceRef` replaced with a quote-free
register-row locus; `EvidenceQuote` replaced with a verbatim single-line span
from the cited row.

- DEP-09-01-003 — locus `Deliverables.csv row DEL-09-06`; quote
  "A PKG-09-internal shared component: built and sequenced first, consumed by
  the other six views as a declared dependency".
- DEP-09-01-004 — locus `Deliverables.csv row DEL-09-07`; quote
  "individually documented, Explain-shaped; rendered by the DEL-09-01..05 views".
- DEP-09-01-005 — locus `ScopeLedger.csv row SOW-045`; quote
  "Dashboard — Overview: the orientation return per loop" (DEL-04-01's serve).
- DEP-09-01-006 — locus `Deliverables.csv row DEL-09-01`; quote
  "Per-loop orientation view: git state, newest receipt, gates that matter,
  open tranches, parked lanes with unparking acts" (the gates the DEL-05-01
  evaluators supply).

## Statement edits flagged

None in this deliverable.

## Waivers declared

None. Every row carried real quotable accepted-basis text; no
`Dependencies_EvidenceWaivers.csv` was created.

## Revision (closure-refutation remediation, 2026-07-25)

Sealed Agent 2 REVISION dispatch under `D-PEC-65` §3.1 (file-tool-only), applying
closure-refutation disposition **MAJ-4** exactly as specified. No other cell in
this file changed.

| DependencyID | Cell | Before | After |
|---|---|---|---|
| `DEP-09-01-006` | `EvidenceFile` | `execution/_Decomposition/Deliverables.csv` | `execution/_Decomposition/ScopeLedger.csv` |
| `DEP-09-01-006` | `SourceRef` | `Deliverables.csv row DEL-09-01` | `ScopeLedger.csv row SOW-023` |
| `DEP-09-01-006` | `EvidenceQuote` | `Per-loop orientation view: git state, newest receipt, gates that matter, open tranches, parked lanes with unparking acts` | `Shape gate verdicts as Explain objects (rule, threshold, contributing citations), advisory only` |

Why: the row's target is `DEL-05-01`, but the cited locus was this deliverable's
own `DEL-09-01` row — evidence about the consumer, not the producer, so it could
not warrant the dependency. Re-grounded on `SOW-023` (the scope item `DEL-05-01`
covers), copying the exact span sibling `DEP-09-07-007` already uses for the same
target.

**Verbatim check:** the new quote is a contiguous single-line substring of
`projects/pec/execution/_Decomposition/ScopeLedger.csv`, row `SOW-023`,
`ScopeItemStatement` column, and is byte-identical to the span at `DEP-09-07-007`.
`SourceRef` carries no quoted span. Row re-read post-edit: 29 columns intact.
