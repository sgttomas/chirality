# TASK RUN — DEL-03-06 ScopeOfWork revision (D-PEC-63 batch B6 fan-in)

- **Date:** 2026-07-25
- **Agent:** sealed Agent 2 revision instance, dispatched by PROJECT_SETUP at the batch-B6 fan-in
- **Decision authority:** `D-PEC-63` (PEC Phase 2.2 SOW initialization wave), batch B6 fan-in refutation dispositions
- **Target:** `projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-06_Rebuild_performance_bounds/ScopeOfWork.md`
- **Mode:** minimal corrective revision. No renumbering, no reflow of untouched text, no record added or removed, no scope change.
- **Lifecycle:** untouched. `_STATUS.md` not read-modified and not written.

## Findings applied

| Finding | Severity | Disposition | Status |
|---|---|---|---|
| F5 | MIN | CLM-002 cross-reference "(CLM-013)" → "(CLM-017)" | APPLIED |
| F6a | MIN | Recategorise the CON-006 `PEC-API-002` fragment in the quotation record | APPLIED |
| F7 | MIN | Add `TargetLocation` to CLM-009's "They differ as follows" table | APPLIED |

## F5 — before / after

Location: CLM-002, final clause of the `PEC-SVC-*` coverage enumeration.

**Before**

> …and `PEC-SVC-006` by self-observability logging under `SOW-057` (CLM-013).

**After**

> …and `PEC-SVC-006` by self-observability logging under `SOW-057` (CLM-017).

**Basis.** CLM-013 in this contract is the `[E-P31]` examined-SHA-baseline
record and names neither `SOW-057` nor `DEL-01-04`. CLM-017 is the boundaries
claim, which states "self-observability logging is `DEL-01-04` (`SOW-057`)".

## F6a — before / after

The quotation record placed `PEC-API-002` in the "complete rows or complete
sentences" category, but CON-006 quotes only "≤100 ms at p95 against the current
corpus", a fragment of the `PRD.md` §9.6 row "Orientation reads shall complete
in ≤100 ms at p95 against the current corpus (session-start critical path)."
The record was corrected rather than the quotation (smaller diff), and the
contract's other `≤100 ms` quotation — in CLM-017 — is separately categorised:
it is the complete `ScopeLedger.csv` `SOW-041` `ScopeItemStatement` cell,
"Complete orientation reads in ≤100 ms at p95 against the current corpus".

**Before**

> …the `PEC-SVC-003`, `PEC-K-01`, `PEC-K-02`, `PEC-K-07`, `PEC-K-10`,
> `PEC-API-002`, `OBJ-005`, and `PRD.md` §12 quotations are each complete rows
> or complete sentences of their sources; the twelve upstream…

**After**

> …the `PEC-SVC-003`, `PEC-K-01`, `PEC-K-02`, `PEC-K-07`, `PEC-K-10`,
> `OBJ-005`, and `PRD.md` §12 quotations are each complete rows or complete
> sentences of their sources; the `SOW-041` statement quoted in CLM-017 is a
> complete register cell, while the `PEC-API-002` span quoted in CON-006 —
> "≤100 ms at p95 against the current corpus" — is a short verbatim phrase of
> that requirement's `PRD.md` §9.6 row rather than the whole row; the twelve
> upstream…

The record's elision accounting is unaffected: this contract still has exactly
one elided quotation (the `DL-11` Decision cell in CLM-006, at two points), and
a short verbatim phrase omits nothing from the span it presents.

## F7 — before / after

Location: CLM-009, the "They differ as follows:" table.

`TargetLocation` differs between the two `EXECUTION` rows and was absent from
both the shared-column sentence preceding the table and from the table itself,
so "as follows" was not exhaustive. The column was added rather than the claim
softened.

**Before**

> | Register row | `TargetDeliverableID` / `TargetRefID` | `TargetName` | `Statement` | `Notes` |

**After**

> | Register row | `TargetDeliverableID` / `TargetRefID` | `TargetName` | `TargetLocation` | `Statement` | `Notes` |

Values taken from the live `Dependencies.csv` in this deliverable folder:

| Register row | `TargetLocation` |
|---|---|
| `DEP-03-06-003` | `execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command` |
| `DEP-03-06-004` | `execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-02_Incremental_reconcile_on_Git_delta` |

The preceding sentence enumerating the columns the two rows *share* correctly
did not list `TargetLocation` and was left untouched.

## Verification

- `python3 tools/scope_of_work/validate_scope_of_work.py "projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-06_Rebuild_performance_bounds"`

  `PASS format=SOW_V1 target=projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-06_Rebuild_performance_bounds`

- `python3 tools/scope_of_work/derive_review_checklist.py "…/DEL-03-06_Rebuild_performance_bounds"` → `item_count = 16` (UNCHANGED). Checklist JSON not persisted.
- Record counts unchanged: OUT 2, REQ 14, AC 16, VER 13, CLM 20, AX 12, TBD 5, CON 6.
- Frontmatter byte-identical (lines 1–8 untouched).
- Ellipsis census unchanged: one elided quotation (`DL-11`, two ellipses, lines
  182–183) and no other ellipsis in the document.

## Artifact hash

- `ScopeOfWork.md` sha256 `d8763664b28333df8a802c476c8796647eb4adc278196a0166a7ef4c456e41f7`

## Write scope

Exactly two paths written by this run: this run record and the target
`ScopeOfWork.md`. No control file, no register, no sibling deliverable, and no
coordination surface was written.
