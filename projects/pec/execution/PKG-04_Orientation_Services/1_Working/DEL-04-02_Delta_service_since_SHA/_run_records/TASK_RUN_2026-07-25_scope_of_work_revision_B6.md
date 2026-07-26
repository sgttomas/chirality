# TASK RUN — DEL-04-02 ScopeOfWork revision (D-PEC-63 batch B6 fan-in)

- **Date:** 2026-07-25
- **Agent:** sealed Agent 2 revision instance, dispatched by PROJECT_SETUP at the batch-B6 fan-in
- **Decision authority:** `D-PEC-63` (PEC Phase 2.2 SOW initialization wave), batch B6 fan-in refutation dispositions
- **Target:** `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-02_Delta_service_since_SHA/ScopeOfWork.md`
- **Mode:** minimal corrective revision. No renumbering, no reflow of untouched text, no record added or removed, no scope change.
- **Lifecycle:** untouched. `_STATUS.md` not read-modified and not written.

## Findings applied

| Finding | Severity | Disposition | Status |
|---|---|---|---|
| F2b | MAJ | Name the orphaned parity-diff owner in CLM-015 and extend the CLM-014 PhaseHint claim | APPLIED |
| F6b | MIN | Move the `PEC-PRS-007` and `PEC-K-07` quotations into the quotation record's short-phrase category | APPLIED |

## F2b — before / after

REQ-011 excludes "run no parity diff" and asserts "each is cited to its owner in
CLM-015", but CLM-015 named no owner for that act. Traceability completion only
— no scope moved.

Location: CLM-015 (Boundaries).

**Before**

> …classifying and reporting drift between successive snapshots is `DEL-03-03`
> (`SOW-019`); deterministic evaluation of gate preconditions…

**After**

> …classifying and reporting drift between successive snapshots is `DEL-03-03`
> (`SOW-019`); parity-diffing PEC derivations against practitioner-harness
> output is `DEL-03-04` (`SOW-020`); deterministic evaluation of gate
> preconditions…

**Register facts verified before writing.** `ScopeLedger.csv` `SOW-020`:
`InOutStatus` `IN`, statement "Parity-diff PEC derivations against
practitioner-harness output; surface discrepancies as DriftFindings resolved
against live sources", `SourceRef` `PEC-RCN-005`, `PackageID` `PKG-03`,
`DeliverableIDs` `DEL-03-04`. `Deliverables.csv` `DEL-03-04`:
"Practitioner-harness parity diff", `PKG-03`, `CoversScopeItems` `SOW-020`,
`PhaseHint` `P1`.

Location: CLM-014 (Phase staging).

**Before**

> `P1` (`DEL-01-01`, `DEL-01-05`, `DEL-03-01`, `DEL-03-03`, `DEL-04-01`, …)

**After**

> `P1` (`DEL-01-01`, `DEL-01-05`, `DEL-03-01`, `DEL-03-03`, `DEL-03-04`,
> `DEL-04-01`, …)

`DEL-03-04` is `P1`, so the claim's `P2`/`P3` exception lists and its closing
sentences are unaffected and untouched.

## F6b — before / after

The quotation record placed `PEC-PRS-007` and (via the `PEC-K-*` wildcard)
`PEC-K-07` in the "complete rows, complete cells, or complete sentences"
category. Both quotations in REQ-002 are shorter than that:

- `PEC-PRS-007`'s `PRD.md` §9.4 row reads "Presence data is operational only and
  shall never appear in record-tier citations (PEC-K-05)."; the contract quotes
  it without the trailing parenthetical.
- `PEC-K-07`'s `PRD.md` §6 row reads "**Ingest is best-effort; reconciliation is
  guaranteed.** Streams optimize freshness; the reconciler over file truth is
  the source of every record-tier fact."; the contract quotes only the
  post-semicolon clause.

Both were recategorised as short verbatim phrases; neither quotation itself was
altered (that would have been the larger diff).

**Before**

> …and its `TBD-004`, quoted whole. The `PEC-K-*`, `PEC-ORI-*`, `PEC-GAT-*`,
> `PEC-PRS-007`, `PEC-API-002`, `OBJ-001`, `OBJ-002`, `PRD.md` §4.2, §7.3, and
> §8 quotations are each complete rows, complete cells, or complete sentences of
> their sources; … and the `D-PEC-62` acceptance phrases quoted in AX-010 are
> short verbatim phrases, identified there as such.

**After**

> …and its `TBD-004`, quoted whole. The `PEC-K-*` quotations other than
> `PEC-K-07`, and the `PEC-ORI-*`, `PEC-GAT-*`, `PEC-API-002`, `OBJ-001`,
> `OBJ-002`, `PRD.md` §4.2, §7.3, and §8 quotations, are each complete rows,
> complete cells, or complete sentences of their sources; … the `D-PEC-62`
> acceptance phrases quoted in AX-010 are short verbatim phrases, identified
> there as such; and two further short verbatim phrases are quoted in REQ-002 —
> the `PEC-K-07` span, which is the post-semicolon clause of that row rather
> than the whole row, and the `PEC-PRS-007` span, which presents that row
> without its trailing parenthetical "(PEC-K-05)".

The record's opening claim — "no quotation in this document is elided … and no
ellipsis appears anywhere in this document" — remains true: `grep -c '…'` = 0,
and a short verbatim phrase omits nothing from the span it presents.

## Verification

- `python3 tools/scope_of_work/validate_scope_of_work.py "projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-02_Delta_service_since_SHA"`

  `PASS format=SOW_V1 target=projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-02_Delta_service_since_SHA`

- `python3 tools/scope_of_work/derive_review_checklist.py "…/DEL-04-02_Delta_service_since_SHA"` → `item_count = 16` (UNCHANGED). Checklist JSON not persisted.
- Record counts unchanged: OUT 2, REQ 15, AC 16, VER 15, CLM 17, AX 13, TBD 4, CON 5.
- Frontmatter byte-identical (lines 1–8 untouched).
- Heading set and Output and Evaluation Matrix untouched.

## Artifact hash

- `ScopeOfWork.md` sha256 `a7dcc4d45c01194138191ad2eb996aefdf0f0b5a6782192a5f0110f09dd06d86`

## Write scope

Exactly two paths written by this run: this run record and the target
`ScopeOfWork.md`. No control file, no register, no sibling deliverable, and no
coordination surface was written.
