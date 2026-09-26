# PEC Remaining census — comparison with the D-PEC-83 concordance

Status: **census evidence for a retirement proposal**. Nothing was removed,
ticked or transferred. Prepared by the RR1 WORKING_ITEMS manager (undertaking
`HELP-HUMAN-PEC-20260926-REMAINING-RETIREMENT`) on 2026-09-26.

## Basis

- Source state: fetched `origin/main` `6281273fa7bd96b66703009e6325db2fa74815b3`
  (branch `claude/pec-remaining-retirement-account` cut from it). The branch
  was later rebased onto `origin/main` `f90320c1d` (PR #946, the `D-PEC-96`
  ruling); no `projects/pec/execution/PKG-*` file changed, and a rebuild of
  the census there produced byte-identical output.
- Census: `REMAINING_CENSUS.csv` in this folder, built by a stdlib Python
  parser that anchors on each file's single `## Remaining` heading, requires
  every byte of the section body to belong to a keyed item block (no stray
  bullets or prose), and records each block's text, `Depends:` line, gate
  lines, extra annotation lines and the block's SHA-256.
- Concordance inputs (read-only):
  - `execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05/R1_R4_2026-09-05/SYNTHESIS/APPLICATION_PREPARATION/FULL_01/APPLICATION_MANIFEST.json`,
    SHA-256 `47db5a1358c0eb7baf40457efa205ae02748498abce2a9046e8970020727283d`
    (the manifest `D-PEC-83` A-A names);
  - `.../FULL_01/PROPOSED_ITEMS.csv`, SHA-256
    `91be362163e94b0225fbea85c6ecbf9eed3a47f9f3f05b8bcf936dfb2c569b75`;
  - `.../FULL_01/CARRIER_DISPOSITIONS.csv`, SHA-256
    `0c9b6116240de26211f6cfae681860c33475eee35516d0848a0d7383a1a514c0`;
  - `.../R5_APPLICATION_D83_2026-09-05/APPLICATION_RESULTS.json`, SHA-256
    `74de0cb04586a0259c02730b9b7063f870186ca8bfa3eef7350548d044b102ba`
    (Receipt 174 application: `PASS`).

## Counts

| Measure | D-PEC-83 concordance | Current source (census) | Finding |
|---|---:|---:|---|
| Deliverable `_STATUS.md` population | 64 (carrier population) | 66 | `DEL-02-08` and `DEL-02-09` were created later under `D-PEC-93`; neither has a Remaining section |
| Candidate carriers | 58 | — | 57 ordinary + 1 frozen (`DEL-01-05`) |
| Carriers applied / sections present | 57 applied (`applied_target_count`) | **57** sections | Same 57 deliverables |
| Items proposed | 92 | — | 89 ordinary + 3 frozen |
| Items applied / present | 89 (`applied_item_count`) | **89** keyed items | Every key present exactly once; 0 missing, 0 extra |
| Frozen carrier | 1 excluded (`DEL-01-05`, 3 items, `FrozenRebindRequired=true`) | Not applied; `DEL-01-05/_STATUS.md` has no Remaining section | Carried in the census as 3 `FROZEN_UNAPPLIED_CARRIER` keys |
| Census keys | — | **92** (89 live + 3 frozen), all unique | Finite population for the account |

Text identity: for all 89 live items the item text, `Depends:` value and gate
line(s) equal the concordance's `ProposedText`, `Depends` and `ItemGate`
byte for byte. Every live key is in its deliverable's ordinary manifest entry.
There is no source drift in the item bodies since application.

Changes since application (all inside the item blocks, recorded by later
rulings, none altering the applied text):

| Keys | Change | Record |
|---|---|---|
| `DEL-01-03-REM-001`–`-003` | Ticked `[x]` | `DEL-01-03/_STATUS.md` History, 2026-09-24, under `D-PEC-87_RULING_2026-09-24.md` L-1a, citing three `REMAINING_EVIDENCE_*` reports |
| `DEL-06-04-REM-001`, `DEL-07-02-REM-001`, `DEL-07-04-REM-001`, `DEL-07-05-REM-001` | Ticked `[x]` with a `NOT_SELECTABLE_UNTIL …` annotation and "Closed unexecuted by retirement, not completed". The reinstatement condition is trigger T-RT for DEL-06-04, DEL-07-02 and DEL-07-05; for DEL-07-04 it is "a later owner direction and accepted scope-change amendment" (no T-RT). Each condition is also recorded in the decomposition registers (`ScopeLedger.csv`, `Deliverables.csv`, `SOFTWARE_DECOMP.md`) | Each deliverable's History, 2026-09-25, SCA-005 checkpoint 3 (`D-PEC-92` Lane A "four `_STATUS.md` retirements") |

## Classes in the census

| Census class | Keys | D-PEC-83 route |
|---|---:|---|
| `ORDINARY_OPEN` | 82 | EVIDENCE 70, PRODUCT_OBLIGATION 6, DOCUMENTARY 6 |
| `TICKED` | 3 | EVIDENCE (DEL-01-03) |
| `RETIRED_DELIVERABLE_CLOSED_UNEXECUTED` | 4 | EVIDENCE (DEL-06-04, DEL-07-02, DEL-07-04, DEL-07-05) |
| `FROZEN_UNAPPLIED` | 3 | CONFIRMED_SCANNER_REPAIR 2, EVIDENCE 1 (DEL-01-05) |
| **Total** | **92** | |

Lifecycle of the 57 section-bearing deliverables: `OPEN` 27, `INITIALIZED` 25,
`IN_PROGRESS` 1 (`DEL-01-03`), `RETIRED` 4. **None is `CHECKING` or
`ISSUED`.** The four `CHECKING` deliverables (`DEL-00-01`, `DEL-00-03`,
`DEL-08-02`, `DEL-10-01`) carry no Remaining section, and neither do
`DEL-01-05` (IN_PROGRESS since the `D-PEC-84` L reversal), `DEL-01-06`,
`DEL-02-08`, `DEL-02-09` or `DEL-04-04`.

Scope of Work presence: 26 of the 57 sections belong to deliverables with a
`ScopeOfWork.md` (57 of the 89 live items); 31 sections (32 items) belong to
deliverables without one. One deliverable (`DEL-01-03`) has a `MEMORY.md`.

## Outside the census

The concordance also records 73 held or conditional residuals
(`HeldOrConditionalResidualIDs` in `CARRIER_DISPOSITIONS.csv`), including all
proposals for the five `NO_APPLICATION_HELD_OR_CONDITIONAL` carriers. They
were never written to any Remaining section. Their home remains the accepted
`D-PEC-83` R-A report (`CARRIER_DISPOSITIONS.csv` and
`RESIDUAL_RECOMMENDATIONS.csv` in the concordance package); retiring the
sections neither moves nor closes them, so none is lost. The gaps in the live
key numbering (for example `DEL-03-02-REM-015`, `DEL-04-01-REM-003`) are these
held residuals.

## Rebuild

`build_census.py` (manager scratch, stdlib, CPython 3.13.7) reproduces the CSV
from the tree; the run basis records its hash. The CSV is derivative
evidence, not authority: each row cites its source path and SHA-256.
