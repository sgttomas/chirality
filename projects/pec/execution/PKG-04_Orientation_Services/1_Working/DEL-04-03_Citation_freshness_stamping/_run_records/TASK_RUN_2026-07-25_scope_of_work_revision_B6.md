# TASK RUN — DEL-04-03 ScopeOfWork revision (D-PEC-63 batch B6 fan-in)

- **Date:** 2026-07-25
- **Agent:** sealed Agent 2 revision instance, dispatched by PROJECT_SETUP at the batch-B6 fan-in
- **Decision authority:** `D-PEC-63` (PEC Phase 2.2 SOW initialization wave), batch B6 fan-in refutation dispositions
- **Target:** `projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/ScopeOfWork.md`
- **Mode:** minimal corrective revision. No renumbering, no reflow of untouched text, no record added or removed, no scope change.
- **Lifecycle:** untouched. `_STATUS.md` not read-modified and not written.

## Findings applied

| Finding | Severity | Disposition | Status |
|---|---|---|---|
| F2a | MAJ | Name the three orphaned boundary owners in CLM-016 and extend the CLM-015 PhaseHint claim | APPLIED |
| F4 | MIN | CLM-012 attribution "Ontology section" → "Epistemology section" | APPLIED |
| F8 | MIN | Re-attribute the `SOW-018` quotation in CON-002 to `SOW-018` alone | APPLIED |

## F2a — before / after

REQ-010 excludes acts whose owners CLM-016 did not name: socket binding, token
check, subscription, and adoption measurement. CLM-016's own claim is that "each
is cited to its owner", so the omission made that claim false. Traceability
completion only — no scope moved.

Location: CLM-016 (Boundaries).

**Before**

> …the orientation latency budget is `DEL-08-04` (`SOW-041`); the universal
> drill-down component … is `DEL-09-06` … ; the orientation defect-rate
> spot-check that measures `SOW-007` is `DEL-10-04` (`SOW-059`, `P2`). This
> contract produces only the citation layer and its tests.

**After**

> …the orientation latency budget is `DEL-08-04` (`SOW-041`); the local-only
> Unix-socket binding and its token-scoped access classes are `DEL-08-01`
> (`SOW-003`, `SOW-040`) and the SSE delta/presence subscription is `DEL-08-05`
> (`SOW-044`, `P4`); the universal drill-down component … is `DEL-09-06` … ; the
> orientation defect-rate spot-check that measures `SOW-007` is `DEL-10-04`
> (`SOW-059`, `P2`) and harness poll-adoption measurement is `DEL-10-12`
> (`SOW-060`, `P3`). This contract produces only the citation layer and its
> tests.

**Register facts verified before writing**

| Deliverable | `Deliverables.csv` name | `CoversScopeItems` | `PackageID` | `PhaseHint` |
|---|---|---|---|---|
| `DEL-08-01` | Unix-socket server + token-scoped access | `SOW-003;SOW-040` | `PKG-08` | `P1` |
| `DEL-08-05` | SSE delta/presence subscription | `SOW-044` | `PKG-08` | `P4` |
| `DEL-10-12` | Poll-adoption measurement | `SOW-060` | `PKG-10` | `P3` |

`ScopeLedger.csv` confirms `SOW-003` → `DEL-08-01`, `SOW-040` → `DEL-08-01`,
`SOW-044` → `DEL-08-05`, `SOW-060` → `DEL-10-12`.

Location: CLM-015 (Phase staging).

**Before**

> Other deliverables named as owners of adjacent scope are `P1` (`DEL-01-01`,
> `DEL-01-03`, `DEL-01-05`, `DEL-03-01`, `DEL-03-02`, `DEL-04-02`, `DEL-08-04`)
> and `P2` (`DEL-04-04`).

**After**

> Other deliverables named as owners of adjacent scope are `P1` (`DEL-01-01`,
> `DEL-01-03`, `DEL-01-05`, `DEL-03-01`, `DEL-03-02`, `DEL-04-02`, `DEL-08-01`,
> `DEL-08-04`), `P2` (`DEL-04-04`), `P3` (`DEL-10-12`), and `P4` (`DEL-08-05`).

The claim's closing sentences ("No consumer precedes this deliverable's phase",
"no claim in this contract stages any named deliverable into a different phase")
remain true and untouched: all three additions are cited only as owners of scope
this deliverable does not touch.

## F4 — before / after

Location: CLM-012, blockquote attribution.

**Before**

> (`DEL-04-01/ScopeOfWork.md`, Ontology section; quoted in full, not elided.

**After**

> (`DEL-04-01/ScopeOfWork.md`, Epistemology section; quoted in full, not elided.

**Basis.** In `DEL-04-01/ScopeOfWork.md`, `CON-003` sits at line 319, between
`## Completion and Reliance Basis — Epistemology` (line 278) and
`## Production and Verification Method — Praxeology` (line 322).

## F8 — before / after

Location: CON-002, origin axis.

**Before**

> — `SOW-018` / `PEC-RCN-003`, "Run reconciliation incrementally, keyed on Git
> delta since the last examined SHA", covered by `DEL-03-02` —

**After**

> — `SOW-018`, "Run reconciliation incrementally, keyed on Git delta since the
> last examined SHA" (`SourceRef` `PEC-RCN-003`, whose own `PRD.md` §9.2 wording
> differs), covered by `DEL-03-02` —

**Basis.** `ScopeLedger.csv` row `SOW-018` `ScopeItemStatement` is the quoted
string exactly; its `SourceRef` cell is `PEC-RCN-003`. `PRD.md` §9.2 states
`PEC-RCN-003` differently: "Reconciliation shall run incrementally, keyed on Git
delta since the last examined SHA." The quotation is therefore `SOW-018`'s and
`PEC-RCN-003` is cited as its `SourceRef` without sharing the quotation.

## Verification

- `python3 tools/scope_of_work/validate_scope_of_work.py "projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping"`

  `PASS format=SOW_V1 target=projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping`

- `python3 tools/scope_of_work/derive_review_checklist.py "…/DEL-04-03_Citation_freshness_stamping"` → `item_count = 15` (UNCHANGED). Checklist JSON not persisted.
- Record counts unchanged: OUT 2, REQ 15, AC 15, VER 14, CLM 17, AX 11, TBD 4, CON 4.
- Frontmatter byte-identical (lines 1–8 untouched).
- Quotation record untouched and still true: this contract remains at zero
  elisions (`grep -c '…'` = 0). F8 shortened no quoted span; it re-attributed an
  existing complete-cell quotation.

## Artifact hash

- `ScopeOfWork.md` sha256 `9d0d95bcd027aaa5d6cefbdc31dcc52e5f3dad8e6edc81bdf047921392e4d96f`

## Write scope

Exactly two paths written by this run: this run record and the target
`ScopeOfWork.md`. No control file, no register, no sibling deliverable, and no
coordination surface was written.
