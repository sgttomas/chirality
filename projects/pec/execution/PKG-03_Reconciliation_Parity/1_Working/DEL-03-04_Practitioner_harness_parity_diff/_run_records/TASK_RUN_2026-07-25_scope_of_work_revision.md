# TASK RUN — DEL-03-04 ScopeOfWork revision (D-PEC-63 batch B5 fan-in)

- **Date:** 2026-07-25
- **Agent:** sealed Agent 2 revision instance, dispatched by PROJECT_SETUP at the batch-B5 fan-in
- **Decision authority:** `D-PEC-63` (PEC Phase 2.2 SOW initialization wave), batch B5 fan-in refutation dispositions
- **Target:** `projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-04_Practitioner_harness_parity_diff/ScopeOfWork.md`
- **Mode:** minimal corrective revision. No renumbering, no reflow of untouched text, no record added or removed.
- **Lifecycle:** untouched. `_STATUS.md` not read-modified and not written.

## Findings applied

| Finding | Severity | Disposition | Status |
|---|---|---|---|
| F1 | MAJ | Quote `SOW-093`'s contiguous span in CON-004, removing the spurious ellipsis, so the Quotation record's "Exactly one is elided" is true | APPLIED |
| F4 | MIN | Correct the section attribution of `DEL-03-01`'s `CON-005` in CLM-012 | APPLIED |
| F5 | MIN | Restate CLM-004's `C10` `Source`-cell check as inclusion rather than identity | APPLIED |

## F1 — before / after

Location: CON-004 (Boundaries / Ontology section).

**Before**

> The `SOW-093` metric counts specifically "parity DriftFindings ... per
> reconcile", so the distinction is load-bearing for a consumer this contract
> may not oblige (CLM-013).

**After**

> The `SOW-093` metric counts specifically "parity DriftFindings per
> reconcile", so the distinction is load-bearing for a consumer this contract
> may not oblige (CLM-013).

**Basis.** `_Decomposition/ScopeLedger.csv` row `SOW-093` reads, contiguously,
"Report parity DriftFindings per reconcile as the §11 parity metric". The span
"parity DriftFindings per reconcile" is unbroken in the ledger, so the ellipsis
marked an omission that did not exist. The quotation remains attributed to
`SOW-093` (the ledger row); it was **not** re-attributed to `PRD.md` §11.

**Consequence.** Ellipsis census after this edit: exactly one ellipsis remains
in the document — the leading ellipsis of the `tools/REGISTRY.md`
`Description`-cell quotation in CLM-009 — which is exactly what the Quotation
record enumerates. The trailer's "Exactly one is elided … No other quotation in
this document omits text from the span it presents" is now literally true and
was left unchanged.

## F4 — before / after

Location: CLM-012, attribution line of the `DEL-03-01` `CON-005` blockquote.

**Before**

> (`DEL-03-01/ScopeOfWork.md`, Ontology section, `CON-005` quoted in full, not
> elided. …)

**After**

> (`DEL-03-01/ScopeOfWork.md`, Epistemology section, `CON-005` quoted in full,
> not elided. …)

**Basis.** In `DEL-03-01/ScopeOfWork.md`, `CON-005` sits at line 407, under the
`## Completion and Reliance Basis — Epistemology` heading (line 359); the
`## Deliverable Definition — Ontology` section ends at line 358. Quoted text
itself unchanged; only the section name in the carve-out was corrected.

## F5 — before / after

Location: CLM-004, the `C10` resolution check.

**Before**

> The resolution is checkable rather than assumed: the row's own `Source` cell
> is `PEC-RCN-005`, which is exactly the `SourceRef` of `SOW-020` (CLM-001,
> CLM-002), and its `Constraint` text carries the same word …

**After**

> The resolution is checkable rather than assumed: the row's own `Source` cell
> names `PEC-RCN-005` as its first locus — the whole of `SOW-020`'s `SourceRef`
> (CLM-001, CLM-002) — and its `Constraint` text carries the same word …

**Basis.** `SOFTWARE_DECOMP.md` §1.3 row `C10`'s `Source` cell is two-part:
"PEC-RCN-005, PRD §15". `SOW-020`'s `SourceRef` is the single locus
`PEC-RCN-005`. The relation is inclusion, not identity. The full `C10` row is
already quoted verbatim earlier in the same claim, so no new quotation was
introduced by this correction.

## Verification

- `python3 tools/scope_of_work/validate_scope_of_work.py "projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-04_Practitioner_harness_parity_diff"`

  `PASS format=SOW_V1 target=projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-04_Practitioner_harness_parity_diff`

- `python3 tools/scope_of_work/derive_review_checklist.py "…/DEL-03-04_Practitioner_harness_parity_diff"` → `item_count = 17` (UNCHANGED). Checklist JSON not persisted.
- Record counts unchanged: OUT 2, REQ 15, AC 17, VER 15, CLM 16, AX 10, TBD 5, CON 6.
- Frontmatter byte-identical (lines 1–8 untouched).
- Ellipsis census re-run after edits: one occurrence, at the CLM-009
  `tools/REGISTRY.md` quotation. Trailer accounting matches.

## Artifact hash

- `ScopeOfWork.md` sha256 `e007f5307fce88fd7e31957bb4676f35d83bc971de3e0278e3dae906bd8e4e02`

## Write scope

Exactly two paths written by this run: this run record and the target
`ScopeOfWork.md`. No control file, no register, no sibling deliverable, and no
coordination surface was written.
