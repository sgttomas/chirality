# TASK RUN — D-PEC-65 register evidence repair (DEL-09-06)

- **Date:** 2026-07-25
- **Instrument:** `execution/_Coordination/_DECISIONS/D-PEC-65_register_evidence_repair.md` (RULED §7)
- **Agent:** sealed ephemeral Agent 2 repair dispatch (file-tool-only), package `PKG-09_Dashboards`
- **File touched:** `Dependencies.csv` (EXECUTION rows only; ANCHOR rows read-only)

## Rows dispositioned

| DependencyID | Class found | Disposition | EvidenceFile after |
|---|---|---|---|
| DEP-09-06-003 | DUP (EVQ-001) | REPAIRED | `execution/_Decomposition/Deliverables.csv` |
| DEP-09-06-004 | DUP (EVQ-001) | REPAIRED | `execution/_Decomposition/Deliverables.csv` |
| DEP-09-06-005 | DUP (EVQ-001) | REPAIRED | `execution/_Decomposition/ScopeLedger.csv` |

Counts: 3 EXECUTION rows inspected, 3 repaired, 0 waived, 0 already-clean,
0 blocked. 2 ANCHOR rows untouched.

## Cells changed

- DEP-09-06-003 — locus `Deliverables.csv row DEL-08-05`; quote "SSE
  subscription for deltas and presence changes (dashboards; long-running
  managers). P2/P3 dashboards poll" — the P2/P3 dashboards poll the socket API
  that DEL-08-01 serves. The seeded row's second clause (the PKG-09 "New data
  classes" exclusion) lives in a different document and was dropped to keep
  file/locus/quote on one coherent source; the exclusion still stands in
  `SOFTWARE_DECOMP.md` §4 and is not needed to warrant this edge.
- DEP-09-06-004 — locus `Deliverables.csv row DEL-08-03`; quote "Machine-first
  response envelope carrying citations." (the citation-bearing envelope the
  drill-down consumes). Replaces the seeded cross-reference stub "as E-N06",
  which cited nothing.
- DEP-09-06-005 — locus `ScopeLedger.csv row SOW-007`; quote "Attach a
  citation (file path, anchor, and/or SHA) to every claim in an orientation
  response" — SOW-007 is covered by DEL-04-03, so the citation shapes the
  drill-down resolves are that deliverable's artifact.

`EvidenceFile` on all three re-pointed off the frozen D-PEC-62 PLAN exhibit.

## Statement edits flagged

None. The two `R1-F12/R3-F1:` and `R3-F1:` prefixes were left intact: each
statement does assert the dependency claim, so neither met the packet's
misstatement threshold for a flagged rewrite.

## Waivers declared

None. No `Dependencies_EvidenceWaivers.csv` created.

## Revision (closure-refutation remediation, 2026-07-25)

Sealed Agent 2 REVISION dispatch under `D-PEC-65` §3.1 (file-tool-only), applying
closure-refutation disposition **MAJ-3** exactly as specified. No other cell in
this file changed.

| DependencyID | Cell | Before | After |
|---|---|---|---|
| `DEP-09-06-003` | `SourceRef` | `Deliverables.csv row DEL-08-05` | `Deliverables.csv row DEL-08-01 Description column` |
| `DEP-09-06-003` | `EvidenceQuote` | `SSE subscription for deltas and presence changes (dashboards; long-running managers). P2/P3 dashboards poll` | `Local-only Unix-socket binding with token-scoped access classes (owner, harness, admin); auth-reuse choice tracked by OI-006.` |

`EvidenceFile` unchanged (`execution/_Decomposition/Deliverables.csv`).

Why: the row's target is `DEL-08-01`, but the cited locus was the `DEL-08-05` row —
evidence about a different deliverable. Re-grounded on the target's own
`Deliverables.csv` row, copying the exact span sibling `DEP-10-03-003` already uses
for the same target.

**Verbatim check:** the new quote is a contiguous single-line substring of
`projects/pec/execution/_Decomposition/Deliverables.csv`, row `DEL-08-01`,
`Description` column, and is byte-identical to the span at `DEP-10-03-003`.
`SourceRef` carries no quoted span. Row re-read post-edit: 29 columns intact.
