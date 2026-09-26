# Run Summary — COV_SCA006_POSTCHANGE_2026-09-26_0051

`RUN_STATUS = WARNINGS`

The run is valid and complete. Every check produced a verdict and no input
failed. Warning-severity findings are present; no blocker is present.

## Headline

| Field | Value |
|---|---|
| Overall status | `WARNINGS` |
| Closure readiness | `WARN` (method-literal three-way verdict; not a lifecycle, readiness, acceptance or reliance judgement) |
| Issues | 0 BLOCKER / 3 WARNING / 71 INFO / 12 EXPECTED_CONSEQUENCE (86 rows) |
| Audited basis | revision 1.6 pre-acceptance `3ef0412a…9b29`; registers and PRD v2.4 equal to the accepted CP2 candidates; commit `5e0169f5e` |
| Phase | SCA-006 checkpoint-3 preparation, pre-acceptance poststate (Lane A1, A2, A4 applied; A5 in progress; A6 not done) |
| Expected consequences cite | `D-PEC-97` with SCA-006 `Propagation_Plan.md` §A1/§A2/§A5/§A6 and §B1/§B2/§B3/§B7 |

## Observed counts (for the manager's C3 cross-check)

- **Scope items:** 100 (74 IN / 18 OUT / 8 TBD); §2 tables and §7 agree.
- **Packages:** 11; per-package IN 3/8/9/7/7/3/6/3/8/7/13 (PKG-04 7, PKG-08
  8, PKG-10 13).
- **Deliverable rows:** 68 (64 active / 4 RETIRED: DEL-06-04, DEL-07-02,
  DEL-07-04, DEL-07-05). `ContextBudgetQA.csv` 68 rows.
- **Folders:** 66. DEL-08-06 and DEL-10-13 have none (plan §B1).
- **Active envelopes:** S 28 / M 34 / L 2 / XL 0. All rows: S 29 / M 37 / L 2.
- **Objectives:** 6. Supporters: OBJ-001 27 (25 folder-backed), OBJ-002 14,
  OBJ-003 14, OBJ-004 11, OBJ-005 7, OBJ-006 9.
- **Unmapped:** 0 IN items without package, deliverable or objective; 0
  active deliverables without an objective. Union rule holds on 64/64 active
  rows; reciprocity 68/68.
- **Open / resolved issues:** 10 / 3. **Vocabulary:** 29 terms.
- **Lifecycle (66 folders):** 26 `INITIALIZED`, 30 `OPEN`, 4 `CHECKING`, 2
  `IN_PROGRESS`, 4 `RETIRED`. **Contracts:** 32 `SOW_V1`, 34 `NONE`.
- **Strict validator:** 66 registers, 263 rows, 68 deliverables declared, 0
  errors, 2 warnings (DRB-008 ×2: DEL-08-06, DEL-10-13), exit 1 by design.
- **Closure:** 111 edges, 66 nodes, 0 SCCs, 0 bidirectional pairs, 0
  orphans; isolated DEL-00-03, DEL-01-05, DEL-06-04, DEL-07-02, DEL-07-04,
  DEL-07-05; hub DEL-03-01 (25). Byte-identical to the baseline.
- **Reliance-hold preflight:** `ALLOW` for all seven targets (exit 0).

## Every WARNING

| Issue | Check | Entity | Reason |
|---|---|---|---|
| COV-008 | 6 | DEL-01-03 | `IN_PROGRESS`; anticipated set not in the folder (bytes under `projects/pec/v2/`). Carried (baseline COV-004) |
| COV-010 | 6 | DEL-01-05 | Same pattern. Carried (baseline COV-006) |
| COV-046 | 6 | DEL-08-02 | `CHECKING`; source-tree bytes outside the folder. Carried (baseline COV-042) |

All three are pre-existing and unrelated to SCA-006.

## Every EXPECTED_CONSEQUENCE

| Issue | Check | Entity | Plan | Would be |
|---|---|---|---|---|
| COV-003 | 2 | DEL-08-06 folder absent | §B1 | BLOCKER |
| COV-004 | 2 | DEL-10-13 folder absent | §B1 | BLOCKER |
| COV-073 | 8 | SOW-099 → DEL-08-06 (no folder) | §B1 | WARNING |
| COV-074 | 8 | SOW-100 → DEL-10-13 (no folder) | §B1 | WARNING |
| COV-075 | 9 | DEP-09-06-003 quote not verbatim | §B3 | WARNING |
| COV-076 | 9 | DEP-10-03-003 quote not verbatim | §B3 | WARNING |
| COV-077 | 9 | 63 `_CONTEXT.md` at revision 1.5 | §B7 | WARNING |
| COV-078 | 9 | 66 `_REFERENCES.md` at revision 1.5 / PRD v2.3 | §B7 | WARNING |
| COV-079 | 9 | 3 A2 mirrors anticipate "revision 1.6 (`current_basis`)" | §A2 | WARNING |
| COV-080 | 9 | No register traces SOW-097..100 (DEL-04-03, DEL-08-03 anchors) | §B2 | WARNING |
| COV-084 | 10 | Pointers on revision 1.5 / SCA-005; pre-acceptance front matter | §A6, §A1 | WARNING |
| COV-085 | 10 | SCA-006 candidate snapshot mid-A5 | §A5, §C5 | WARNING |

B1, B3 and B7 match the plan exactly: two folders; exactly two stale quotes,
with DEP-09-06-004 and DEP-10-12-004 still verbatim; 63 contexts and 66
references. COV-079, COV-080, COV-084 and COV-085 are also plan-foreseen but
were not in the brief's list.

## Baseline COV-068 / 069 / 072 / 073

| Baseline | Disposition | Attributed to |
|---|---|---|
| COV-068 (42 contexts at 1.4) | RESOLVED: 0 at 1.4 | `D-PEC-95` N2 (PR #924, `abfd0897b`) |
| COV-069 (64 references at 1.4) | RESOLVED: 0 at 1.4 | `D-PEC-95` N2 |
| COV-072 (19 non-verbatim quotes) | RESOLVED: all 19 verbatim | `D-PEC-95` N3 |
| COV-073 (stale SCA-005 handoff surfaces and pointers) | PARTIALLY RESOLVED. The pointers are current for revision 1.5. The SCA-005 `Handoff_State.md` and `RUN_SUMMARY.md` stay byte-identical and stale-conservative, carried as COV-086 `INFO` | `D-PEC-95` N1 (pointers); the ruling's option P kept the snapshot files unchanged |

None of these is reported as an SCA-006 effect. None is classified
`EXPECTED_CONSEQUENCE`: the resolved ones produce no row, and the residual is
INFO-grade (`Decision_Log.md` D-9).

## Unforeseen finding

**COV-083 (`INFO`).** Revision 1.6 carries unchanged from 1.5 the statement
that PEC's own registry row "declares the `remaining-loop` profile now". It
appears in SOW-094, the DEL-01-06 Description and the §9 "feed profile"
examples. The owner's 2026-09-26 direction on the unruled D-PEC-96 proposal
drops `remaining-loop` ("revision 4: drop remaining-items and
remaining-loop"). It is not an SCA-006 defect, and no accepted decision has
changed the basis yet. Checkpoint-3 acceptance would pin this text while the
direction is pending.

Also new but pre-existing: COV-001 and COV-002 (`INFO`). `audit_structure.py`
is newly required, and it finds the packages lack `0_References/`,
`2_Checking/` and `3_Issued/` (SPEC §12.2: SHOULD), and the tool roots
`_Aggregation/`, `_Estimates/` and `_Sources/` are absent.

## Pre/post headline

| Metric | Baseline | This run |
|---|---|---|
| Forward deliverable coverage | 100 % (66/66) | 97.06 % (66/68) |
| Context fidelity | 100 % (66/66) | 100 % (66/66) |
| Strict validator | 0 / 0 (exit 0) | 0 errors / 2 DRB-008 (exit 1) |
| Closure edges / nodes / isolated | 111 / 66 / 6 | unchanged, byte-identical |
| Issues (B / W / I / EC) | 0 / 3 / 70 / — | 0 / 3 / 71 / 12 |

**Per-finding delta.** 68 carried, 2 changed, 3 resolved, 16 new. There is no
new BLOCKER or WARNING.

## For the caller

- The snapshot holds the method's files (`Brief.md`, `RUN_SUMMARY.md`,
  `QA_Report.md`, `Decision_Log.md`, `Decomp_Coverage_Report.md`,
  `Decomp_Coverage_IssueLog.csv`, `Decomp_Coverage_Matrix.csv`,
  `coverage_summary.json`). It also holds the deterministic tool output
  `structure.json`, its input `inventory.json`, and `PrePost_Comparison.md`.
- No `_LATEST.md` was touched. The audit-pointer decision belongs to the
  manager; this run makes no recommendation on it.
- A5 can copy this run's `coverage_summary.json` to
  `Post_Change_Coverage.json`. Doing so is the manager's act, not this run's.
- The live tree moved during the run: the manager committed `5e0169f5e` (A5
  `Supersession_Map.csv`, C3 evidence). No audited input changed; all were
  re-hashed after emission.
- No independent review of this snapshot was performed. Plan §C4 item 3
  provides a separate review instance.

This snapshot is derivative evidence. It accepts nothing and authorizes
nothing. It makes no CHECKING, ISSUED, acceptance, readiness or reliance
claim.
