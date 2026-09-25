# Run Summary — COV_SCA005_POSTSETUP_2026-09-25_1606

`RUN_STATUS = WARNINGS`

The run is valid and complete. Every check produced a verdict, and no input
failed. Warning-severity findings are present; no blocker is present.

## Headline

| Field | Value |
|---|---|
| Overall status | `WARNINGS` |
| Closure readiness | `WARN` (method-literal three-way verdict; not a lifecycle, readiness or reliance judgement) |
| Issues | 0 blockers / 3 warnings / 70 info |
| By classification | `PRE-EXISTING` 0 B / 3 W / 59 I; `EXPECTED_CONSEQUENCE` 0 / 0 / 11; `DEFECT` 0 / 0 / 0 |
| Audited basis | revision 1.5 `current_basis` `dc2b8479…9660`; registers and PRD v2.3 at their accepted values; D-PEC-93 poststate at commit `995af4f36` (31/31 product paths equal the proposal postimages) |
| Phase | D-PEC-93 post-setup re-audit, after the product writes and before publication |

## Coverage

- **Packages:** 11/11.
- **Deliverables:** 66/66 folders (62 active, 4 retired). DEL-02-08 and
  DEL-02-09 now exist.
- **Contexts:** 66/66 match their registers.
- **Lifecycle:** 26 `INITIALIZED`, 30 `OPEN`, 4 `CHECKING`, 2
  `IN_PROGRESS`, 4 `RETIRED`.
- **Contracts:** 32 `SOW_V1`, 34 `NONE`, 0 ambiguous.
- **Ledger:** 96 rows (70 IN / 18 OUT / 8 TBD); every IN row resolves to a
  declared, folder-backed, non-retired unit.
- **Objectives:** all six supported, every supporter folder-backed; evidence
  internally consistent; 0 IN rows and 0 active deliverables unmapped.
- **Strict validator:** 66 registers, 263 rows, 0 errors, 0 warnings, exit
  0.
- **Dependency closure:** 111 edges, 66 nodes, 0 SCCs, 0 bidirectional
  pairs, 0 orphans; isolated DEL-00-03, DEL-01-05, DEL-06-04, DEL-07-02,
  DEL-07-04, DEL-07-05; hub DEL-03-01 (25).
- **Reliance-hold preflight:** `ALLOW` (exit 0).

## Every WARNING

| Issue | Check | Severity | Entity | Classification | Reason |
|---|---|---|---|---|---|
| COV-004 | 6 | WARNING | DEL-01-03 | PRE-EXISTING | `IN_PROGRESS` with no anticipated set in the folder; the bytes live under `projects/pec/v2/`. Prior COV-006 |
| COV-006 | 6 | WARNING | DEL-01-05 | PRE-EXISTING | Same pattern. Prior COV-008 |
| COV-042 | 6 | WARNING | DEL-08-02 | PRE-EXISTING | `CHECKING`, with the source-tree bytes outside the folder. Prior COV-042 |

## New or changed INFO findings

| Issue | Check | Entity | Classification | Reason |
|---|---|---|---|---|
| COV-015 | 6 | DEL-02-08 | EXPECTED_CONSEQUENCE | New `OPEN` folder; no anticipated artifact yet (D-PEC-93 grants no SOW or artifact write) |
| COV-016 | 6 | DEL-02-09 | EXPECTED_CONSEQUENCE | Same as COV-015 |
| COV-069 | 10 | DEL-* (64 of 66) | EXPECTED_CONSEQUENCE | 64 reference packets at revision 1.4; the 2 new ones at 1.5 (B1 not selected). Prior COV-078, changed count |
| COV-071 | 10 | DEL-00-03; DEL-01-05; DEL-06-04; DEL-07-02; DEL-07-04; DEL-07-05 | EXPECTED_CONSEQUENCE | Closure-tool isolated units, exactly the six planned (plan §C4; D-PEC-93 topology) |
| COV-072 | 10 | 19 ACTIVE EXECUTION rows (10 registers) | PRE-EXISTING | Evidence quotes not verbatim; the same 19 rows as D-PEC-93 finding 1; byte-identical to the prior audited state; owner-ruled carried residual; not caused by the act |
| COV-073 | 10 | SCA-005 | EXPECTED_CONSEQUENCE | SCA-005 snapshot and both `_LATEST.md` pointers still describe the pre-act state (stale-conservative); D-PEC-93 did not open them |

## Dispositions of the briefed prior findings

Prior IDs are those of `COV_SCA005_POSTCHANGE_2026-09-25_1344`.

| Prior | Disposition | New ID |
|---|---|---|
| COV-001 (BLOCKER, DEL-02-08) | RESOLVED: folder created | — |
| COV-002 (BLOCKER, DEL-02-09) | RESOLVED: folder created | — |
| COV-006 (WARNING, DEL-01-03) | CARRIED, unchanged | COV-004 |
| COV-008 (WARNING, DEL-01-05) | CARRIED, unchanged | COV-006 |
| COV-042 (WARNING, DEL-08-02) | CARRIED, unchanged | COV-042 |
| COV-068 (INFO, OBJ-001) | RESOLVED: all 25 supporters folder-backed | — |
| COV-069 (INFO, OBJ-002) | RESOLVED: all 14 supporters folder-backed | — |
| COV-070 (WARNING, SOW-095) | RESOLVED: resolves to the DEL-02-08 folder | — |
| COV-071 (WARNING, SOW-096) | RESOLVED: resolves to the DEL-02-09 folder | — |
| COV-072 (WARNING, DEFECT, "40 not 42") | RESOLVED: every current handoff surface carries 42; SCA-005 `RUN_SUMMARY.md` records the correction | — |
| COV-077 (INFO, 42 contexts at 1.4) | CARRIED, unchanged (B1 not selected) | COV-068 |
| COV-078 (INFO, 64 references at 1.4) | CHANGED: now 64 of 66 (the 2 new packets are at 1.5) | COV-069 |
| COV-079 (INFO, `DEP-09-05-005`) | RESOLVED: row `RETIRED` | — |
| COV-080 (INFO, 18 ACTIVE rows in retired registers) | RESOLVED: 0 ACTIVE rows remain | — |
| COV-081 (INFO, DRB-008 ×2) | RESOLVED: validator 0/0, exit 0 | — |

Also resolved, outside the briefed list: prior COV-073, 074, 075 and 076
(pointer, SCA-004, A5 and anticipatory-provenance rows), by the checkpoint-3
acceptance and A6 that happened between the two runs.

## Against the briefed expectation

Every briefed expectation holds (full table in `Decomp_Coverage_Report.md`).
Differences in form, not substance:

- The method spells the overall status `WARNINGS`; `closure_readiness` is
  `WARN`.
- Prior COV-078 is carried with a changed count ("64 of 66"), because the two
  new reference packets already name revision 1.5.
- Five findings are new, not one: besides the isolated units (COV-071), the
  two new folders' artifact absences (COV-015, COV-016), the quote-currency
  residual (COV-072) and the stale-conservative SCA-005 handoff surfaces
  (COV-073). All are `INFO`.

## Pre/post headline (full detail in `PrePost_Comparison.md`)

| Metric | POSTCHANGE | POSTSETUP |
|---|---|---|
| Forward deliverable coverage | 96.97% (64/66) | 100% (66/66) |
| Context fidelity | 100% (64/64) | 100% (66/66) |
| Strict validator | 0 errors / 2 warnings (exit 1) | 0 / 0 (exit 0) |
| Closure edges / nodes / isolated | 119 / 64 / 2 | 111 / 66 / 6 |
| Issues (blocker/warning/info) | 2/6/74 | 0/3/70 |

**Per-finding delta.** 67 carried, 1 changed, 14 resolved, 5 new. No new
BLOCKER or WARNING.

## For the caller

- The snapshot folder holds the method's eight files plus
  `PrePost_Comparison.md`, and nothing else.
- `_Evaluation/DecompCoverage/_LATEST.md` is unchanged. Under D-PEC-93 the
  pointer decision belongs to the WORKING_ITEMS manager; this run makes no
  recommendation on it.
- No independent review of this snapshot was performed; D-PEC-93 provides a
  separate verifier.

This snapshot is derivative evidence. It accepts nothing and authorizes
nothing. It makes no CHECKING, ISSUED, acceptance, readiness or reliance
claim.
