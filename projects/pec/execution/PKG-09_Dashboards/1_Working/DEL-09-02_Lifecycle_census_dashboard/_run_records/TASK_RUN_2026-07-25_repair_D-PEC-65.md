# TASK RUN — D-PEC-65 register evidence repair (DEL-09-02)

- **Date:** 2026-07-25
- **Instrument:** `execution/_Coordination/_DECISIONS/D-PEC-65_register_evidence_repair.md` (RULED §7)
- **Agent:** sealed ephemeral Agent 2 repair dispatch (file-tool-only), package `PKG-09_Dashboards`
- **File touched:** `Dependencies.csv` (EXECUTION rows only; ANCHOR rows read-only)

## Rows dispositioned

| DependencyID | Class found | Disposition | EvidenceFile after |
|---|---|---|---|
| DEP-09-02-003 | DUP (EVQ-001) | REPAIRED | `execution/_Decomposition/Deliverables.csv` |
| DEP-09-02-004 | DUP (EVQ-001) | REPAIRED | `execution/_Decomposition/Deliverables.csv` |
| DEP-09-02-005 | EMPTY (EVQ-003/004) | REPAIRED | `execution/_Decomposition/SOFTWARE_DECOMP.md` |
| DEP-09-02-006 | DUP (EVQ-001) | REPAIRED | `execution/_Decomposition/ScopeLedger.csv` |

Counts: 4 EXECUTION rows inspected, 4 repaired, 0 waived, 0 already-clean,
0 blocked. 2 ANCHOR rows untouched.

## Cells changed

All four rows: `EvidenceFile` re-pointed off the frozen D-PEC-62 PLAN exhibit;
`SourceRef` replaced with a quote-free locus; `EvidenceQuote` replaced with a
verbatim single-line span from the cited locus.

- DEP-09-02-003 — locus `Deliverables.csv row DEL-09-06`; shared-component quote.
- DEP-09-02-004 — locus `Deliverables.csv row DEL-09-07`; rendered-by-views quote.
- DEP-09-02-005 — the empty-evidence row. Grounded on the accepted rev-1.2
  Vocabulary Map, which states outright that the record-tier `Package`/
  `Deliverable` entities are the ones PEC "models and renders, e.g. in
  DEL-01-01/DEL-09-02" — the census-side warrant for depending on the
  reconciler that builds that tier. Locus `§9 Vocabulary Map row work-domain
  package`.
- DEP-09-02-006 — locus `ScopeLedger.csv row SOW-046`; quote
  "Dashboard — lifecycle census across registered loops' packages/deliverables
  with stuck-age and workflow-completeness views" (the registered-loops set
  DEL-01-06 maintains).

## Statement edits flagged

None in this deliverable.

## Waivers declared

None — including for the class-(b) empty row DEP-09-02-005, which had real
quotable accepted-basis text. No `Dependencies_EvidenceWaivers.csv` created.

## Revision (closure-refutation remediation, 2026-07-25)

Sealed Agent 2 REVISION dispatch under `D-PEC-65` §3.1 (file-tool-only), applying
closure-refutation disposition **MAJ-5** exactly as specified. No other cell in
this file changed.

| DependencyID | Cell | Before | After |
|---|---|---|---|
| `DEP-09-02-005` | `SourceRef` | `§9 Vocabulary Map row work-domain package` | `§4 Packages table row PKG-03` |
| `DEP-09-02-005` | `EvidenceQuote` | `v2's own record-tier entities named ``Package``/``Deliverable`` (PRD §7.1 — *other loops'* lifecycle units that PEC models and renders, e.g. in DEL-01-01/DEL-09-02)` | `The guaranteed path from file truth to record tier: one-command rebuild, incremental Git-delta reconcile, drift classification, harness parity diffing, stream-loss recovery guarantee, store-only writes, rebuild performance bounds` |

`EvidenceFile` unchanged (`execution/_Decomposition/SOFTWARE_DECOMP.md`).

Why: the superseded locus was a vocabulary-disambiguation cell — it defines a term
and names this deliverable only as an illustration; it does not warrant a
dependency on `DEL-03-01`. Re-grounded on the §4 package charter for `PKG-03`,
exactly as sibling `DEP-09-03-005` does for the same target.

**Verbatim check:** the new quote is a contiguous single-line substring of
`projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md`, §4 Packages table, row
`PKG-03`, Scope Description cell — one cell, no table-delimiter crossing — and is
byte-identical to the span at `DEP-09-03-005`. `SourceRef` carries no quoted span.
Row re-read post-edit: 29 columns intact.
