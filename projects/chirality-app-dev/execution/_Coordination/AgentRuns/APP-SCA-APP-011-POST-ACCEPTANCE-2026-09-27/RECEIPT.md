# Receipt — APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27

This is a derivative account of the SCA-APP-011 post-acceptance follow-ups.
Authority stays with SCA-APP-011, the owner's act and the sources below.

**Status: the owner decided all four items, incremental setup is COMPLETE,
and scope closure is `CLOSED_WITH_OBSERVATIONS`.** Still open:
- owner proposal ESR-1, now four retire candidates;
- HGD-1 and HGD-3;
- two observation-pointer moves, which are the manager's call;
- the DEL-02-03-REQ-009 residual.

## Owner decisions

Typed by the owner in chat on 2026-09-27 (verbatim; `CHAT_TRANSCRIPTION.md`):

> Confirm baseline SCA-APP-010 (accepted up to 2026-09-07) and the SCA-APP-011 incremental plan under FULL_GRAPH; HGD-2: retire DEP-02-01-008; APP-R058: option 1.

| Decision | Applied as |
|---|---|
| Setup Phase 5.0 baseline | `_Coordination/SETUP_LOG.md` created with its `BASELINE` line (accepted up to 2026-09-07, latest SCA-APP-010) |
| Setup Phase 5.1 plan | Plan executed. `SETUP_RUN_RECORD.md`; `SETUP_LOG.md` line `INCREMENTAL SCA-APP-011 setup COMPLETE` |
| HGD-2 | DEP-02-01-008 `RETIRED` (with DEP-02-01-007, already accepted). HGD-2 closed in DEL-02-01 `_DEPENDENCIES.md`, with the owner's words quoted |
| APP-R058 option 1 | Federation preflight COMPLETE, then `_Coordination/_TaskManagement/ROW_MAINTENANCE_APP-R058_SCA-APP-011_CLOSURE_2026-09-27.md`. The hold is moot for the App, not released. `ROWS.csv` unchanged |

## What each step wrote

| Step | Written | Result |
|---|---|---|
| Setup 5.0 and 5.5 VERIFY | `SETUP_LOG.md` (baseline); `CHAT_TRANSCRIPTION.md`; `setup_verify/` | `scope-of-work` VERIFY PASS for all nine MODIFY contracts. Valid, 0 issues; contracts and `_STATUS.md` unchanged; nothing changes scope or lifecycle |
| Setup 5.6 `dependency-extract` | `Dependencies.csv` and `_DEPENDENCIES.md` of the 9 plus 16 deliverables; `dep_extract/`; `DEPENDENCY_EXTRACT_RESULTS.md` | 311 rows re-seen. Retired: DEP-02-02-005 to 009 and DEP-02-01-007/008. Restated: DEP-07-05-025, DEP-08-03-010, DEP-08-02-003/005, DEP-07-05-015 and DEP-02-01-013. Kept with a note: DEP-02-03-009. Added: DEP-07-04-009. ESR-1 after review: eight rows re-evidenced to current sources (D-APP-110 ruling record; decomposition Scope Ledger), four held as retire candidates. Indexes refreshed under their existing headings. Function 5 checks pass |
| Setup 5.6 `audit-dep-closure` | `_Evaluation/DepClosure/CLOSURE_SCA_APP_011_POST_EXTRACTION_2026-09-27_1656/`; rebound after review in `CLOSURE_SCA_APP_011_ESR1_REEVIDENCE_2026-09-27_1725/` | 51 current units PASS: 0 SCC, 0 orphans, 3 isolates as before. Five edges removed and one added; the review fixes changed no edge |
| Setup 5.7 | `setup_report/SCAN_REPORT.md`; `SETUP_RUN_RECORD.md`; `SETUP_LOG.md` (COMPLETE) | 53 unblocked, 0 blocked, 0 held for a cycle; retired DEL-09-07 listed apart |
| APP-R058 | The row-maintenance record above | Recorded |
| `audit-scope-closure` rerun | `_Evaluation/ScopeClosureAudit/ScopeClosure_SCA-APP-011_2026-09-27_1726/`, which supersedes 1701 and, through it, the 0505 snapshot; `_LATEST.md` SCA-APP-011 row (method step 5) | `CLOSED_WITH_OBSERVATIONS`, with one observation (DX-15). All 29 actions verified; all 13 reruns COMPLETED, with export freshness now checked deterministically; DX-01 to DX-16 all verified |
| `audit-decomp` | Nothing | Not due. Its inputs, including the decomposition, still hash-verify, so the 0500 snapshot remains current |
| MEMORY | One entry in each of the 25 deliverables: a row next to this run's existing row in the 9 modified deliverables, and a `## Runs` row in the 16 neighbours (SPEC §8) | Links this receipt |

**Also written earlier in this run** (proposal phase, reviewed at `54d96f2a6`
and `0ca5ffcca`):
- `INCREMENTAL_SETUP_PROPOSAL.md`, `DEPENDENCY_EXTRACT_EXPECTED_OUTCOMES.md`
  and `.csv`, and `APP_R058_PROPOSAL.md`;
- `dep_closure/`, the pre-extraction reconfirmation;
- the `audit-decomp` snapshot `COV_SCA_APP_011_POST_ACCEPTANCE_2026-09-27_0500`;
- the pre-setup scope-closure snapshot 0505;
- nine MEMORY rows recording the group-3 acceptance.

## For the owner: what remains

1. **ESR-1: four retire candidates.** Twelve ACTIVE rows cited `_STATUS.md`
   `## Remaining` text that the owner-directed 2026-09-23 finite Task
   Management account retired.
   - **Why they were held.** That accepted instrument preserved the rows:
     - the closeout says "the accepted `Dependencies.csv` rows and source quotes
       remain unchanged";
     - the current-source note in each affected `_DEPENDENCIES.md` makes the
       register rows the gating authority.
     The instrument takes precedence over the workflow's own unseen-row
     retirement.
   - **Correction.** An earlier version of this receipt attributed "adds no
     prerequisite" to the closeout and used it to argue for retiring the rows.
     The phrase is from the current-source note, and it supports keeping them.
   - **Re-evidenced (eight rows).**
     - DEP-02-02-022 and DEP-02-04-017, 018, 019, to the D-APP-110 ruling record.
     - DEP-07-01-010, DEP-08-01-018, 019 and DEP-08-04-013, to the
       decomposition Scope Ledger.
     No edge changed.
   - **Retire candidates (no current source).** DEP-02-02-021, DEP-02-04-015,
     DEP-02-04-016 and DEP-02-01-014.
     - No blocker changes: three are SATISFIED, and the fourth is met by its
       target's lifecycle.
     - Retiring removes four edges, and no cycle can form.
     - DEP-02-04-015 and 016 are the strict halves D-APP-110 kept. The SD-003
       decompose itself is unaffected.
   - **Proposed reply:** "ESR-1: retire DEP-02-02-021, DEP-02-04-015,
     DEP-02-04-016 and DEP-02-01-014."
   - Details: `DEPENDENCY_EXTRACT_RESULTS.md`.
2. **HGD-1** (DEP-02-01-006 direction) is still open.
3. **HGD-3** is still open and not decided. Its premise changed: with
   DEP-02-02-005 and DEP-02-01-007 retired, the four-node cycle it guarded
   against no longer arises.
4. **Pointers (manager's call; not moved):**
   - `_Evaluation/DepClosure/_LATEST.md` to
     `CLOSURE_SCA_APP_011_ESR1_REEVIDENCE_2026-09-27_1725`;
   - `_Evaluation/DecompCoverage/_LATEST.md` to
     `COV_SCA_APP_011_POST_ACCEPTANCE_2026-09-27_0500` (0 blockers).
5. **DEL-02-03-REQ-009.** It still names PIPELINE `TASK*` preselection after
   E80 withdrew the old Pipeline routing examples. Aligning its wording is a
   DEL-02-03 scope question for a later change, not a decision asked here.

## Checks

These ran against `origin/main` `78e74f590` on the final commit:
- this ledger's validator;
- Root G0–G4;
- conflict markers and run-record leaks;
- `build_workflow_index.py --check` and `git diff --check`;
- export freshness.

The results are in the hand-off and in the loop receipt.

## Limits

- **Not changed:** scope, lifecycle and `_STATUS.md`, the decomposition, the
  accepted amendment snapshot, and `_COORDINATION.md`.
- **Pointers.** Only the ScopeClosureAudit per-amendment row moved, as that
  method directs.
- **ESR-1 retire candidates** stay ACTIVE until the owner decides. The closure
  audit counts them as recorded edges.
- **EVQ-006** (report-only) flags 644 App register rows whose `EvidenceFile`
  does not resolve from the project root. The finding predates this run (651
  before it).
- **No release.**
