# Receipt — APP-SCA-APP-012-POST-ACCEPTANCE-2026-09-27

This is a derivative account of the SCA-APP-012 post-acceptance follow-ups.
Authority stays with SCA-APP-012, the owner's act and the sources below.

**Status: the owner decided the plan, DX-07 and TM-APP-051; incremental setup
is COMPLETE, and scope closure is `CLOSED`.** Still open:
- TM-APP-051 stays `DEFERRED` for the unimplemented summary/status widget
  (the row owner's item, not an SCA-APP-012 finding);
- the DepClosure and DecompCoverage observation-pointer moves, which are the
  manager's call;
- semantic lensing of the eight modified deliverables stays stale unless the
  owner selects a rerun.

## Owner decisions

Typed by the owner in chat on 2026-09-27 (verbatim; `CHAT_TRANSCRIPTION.md`):

> I Confirm the SCA-APP-012 incremental plan under FULL_GRAPH; DEP-02-03-008: retire; TM-APP-051: option 1.

| Decision | Applied as |
|---|---|
| Setup Phase 5.1 plan (FULL_GRAPH) | Plan executed. `SETUP_RUN_RECORD.md`; `SETUP_LOG.md` line `INCREMENTAL SCA-APP-012 setup COMPLETE`. Phase 5.0 not run (the `BASELINE` line already exists). FULL_GRAPH is named for this plan only; `_COORDINATION.md` is not edited |
| DEP-02-03-008: retire | DX-07: DEP-02-03-008 `RETIRED` (Status RETIRED, SatisfactionStatus NOT_APPLICABLE, the owner's words quoted in `Notes`), ID kept |
| TM-APP-051 option 1 | Federation preflight COMPLETE, then `_Coordination/_TaskManagement/ROW_MAINTENANCE_TM-APP-051_SCA-APP-012_DISPOSITION_2026-09-27.md` and the TM-APP-051 row delta: `ScaRef` SCA-APP-012, `LastReviewed` 2026-09-27, the §8 item 5 note appended; row kept `DEFERRED`; `Concern`, `Trigger` and the evidence fields (`EvidenceSha` included) unchanged |

## What each step wrote

| Step | Written | Result |
|---|---|---|
| Gate record and 5.5 VERIFY | `CHAT_TRANSCRIPTION.md`; `setup_verify/` | `scope-of-work` VERIFY PASS for all eight MODIFY contracts. Valid, 0 issues; contracts and `_STATUS.md` unchanged; nothing changes scope or lifecycle |
| Setup 5.6 `dependency-extract` | `Dependencies.csv` and `_DEPENDENCIES.md` of the 8 plus 16 deliverables; `dep_extract/`; `DEPENDENCY_EXTRACT_RESULTS.md` | 310 of 315 ACTIVE rows re-seen. Retired: DEP-02-03-009 (DX-01), DEP-02-03-008 (DX-07). Re-evidenced: DEP-02-03-004 (DX-02), DEP-02-03-007 (DX-06). Restated: DEP-08-03-007 `TargetName` (DX-03). DX-04 does not apply. Nothing added. The other registers changed only in `LastSeen` (44 rows in DEL-05-03, DEL-06-01, DEL-06-02, DEL-09-04; 18 CSVs byte-identical). Indexes refreshed under their existing headings. Function 5 checks pass; EVQ-006 84, unchanged |
| Setup 5.6 `audit-dep-closure` | `_Evaluation/DepClosure/CLOSURE_SCA_APP_012_POST_EXTRACTION_2026-09-27_2234/` | 51 current units PASS: 102 edges, 0 SCC, 0 orphans. Census 54 nodes, 102 edges, 0 SCC, 7 isolates (no new isolate). Two edges removed (DEL-02-03 → DEL-08-03, DEL-07-05 → DEL-02-03) |
| Setup 5.7 | `setup_report/SCAN_REPORT.md`; `SETUP_RUN_RECORD.md`; `SETUP_LOG.md` (COMPLETE) | 53 unblocked, 0 blocked, 0 held for a cycle; retired DEL-09-07 listed apart |
| TM-APP-051 | The row-maintenance record and the one `REGISTER.csv` row above | Recorded; `taskmgmt validate` PASS before and after; federation rerun after the write unchanged |
| `audit-scope-closure` | `_Evaluation/ScopeClosureAudit/ScopeClosure_SCA-APP-012_2026-09-27_2240/` (first SCA-APP-012 snapshot); `_LATEST.md` SCA-APP-012 row (method step 5) | `CLOSED`, 0 findings. All 24 actions (80 edits) verified; supersession 14/14 and the map check clean (exit 0, 0 findings, byte-for-byte); 9/9 reruns COMPLETED; DX-01 to DX-07 verified (`DX_Verification.csv`); retired-surface screen 0 hits (its control on the extraction basis finds DEP-02-03-004 and DEP-08-03-007) |
| MEMORY | One setup row in each of the eight modified deliverables, in each file's existing `## Runs` table or dated list | Links this receipt |

**Also written earlier in this run** (stage 1, reviewed at `d0da7590c` and
`63e5de1f2`):
- `INCREMENTAL_SETUP_PROPOSAL.md`, `DEPENDENCY_EXTRACT_EXPECTED_OUTCOMES.md`
  and `.csv`, and `TM_APP_051_PROPOSAL.md` (now carrying decided/run banners,
  except `TM_APP_051_PROPOSAL.md`, left byte-identical because the
  row-maintenance record binds its hash);
- `dep_closure/`, the pre-extraction reconfirmation;
- the `audit-decomp` snapshot `COV_SCA_APP_012_POST_ACCEPTANCE_2026-09-27_2200`;
- four MEMORY rows recording the accepted scope text.

## Observations

- **DEL-09-04 APP-R078.** Its 2026-09-23 retired-status clause says "Preserve
  source artwork and the renderer removal direction with DEL-02-01". No row is
  emitted: the clause states no direction, and DEP-02-01-013 (DEL-02-01 →
  DEL-09-04) already carries the relationship. It is noted in the DEL-09-04
  index for the register owner.
- **DX-05 screen wording.** The audit's screen adds the label "working-root
  scope API" to the DX-05 terms, so that it finds the same two pre-extraction
  rows as this run's stage-1 screen.
- **Pass 4 topology.** The amendment's ADD row (DEC-027) moves the highest
  decision-log ID recorded with the topology. The audit compares the rest of
  the topology and checks that move on its own.

## For the owner: what remains

1. **TM-APP-051** stays `DEFERRED`, open only for the summary/status widget
   that stays with DEL-02-03. Its `EvidenceSha` no longer matches the current
   DEL-02-03 `ScopeOfWork.md`; refreshing it is a separate row-maintenance
   choice.
2. **Pointers (manager's call; not moved):**
   - `_Evaluation/DepClosure/_LATEST.md` still names
     `CLOSURE_SCA_APP_011_ESR1_RULING_2026-09-27_1739`; the newer
     `CLOSURE_HGD_FC_RULING_2026-09-27_1923` and
     `CLOSURE_SCA_APP_012_POST_EXTRACTION_2026-09-27_2234` are unpointed;
   - `_Evaluation/DecompCoverage/_LATEST.md` still names
     `COV_SCA_APP_011_POST_ACCEPTANCE_2026-09-27_0500`;
     `COV_SCA_APP_012_POST_ACCEPTANCE_2026-09-27_2200` has 0 blockers.
3. **Semantic lensing** of the eight modified deliverables stays stale unless
   you select a rerun.

## Checks

These ran against `origin/main` on the final commit:
- this ledger's validator;
- Root G0–G4;
- conflict markers and run-record leaks;
- the dependency schema and register validators, and `taskmgmt validate`;
- `build_workflow_index.py --check` and `git diff --check`;
- `run_affected_tests.py`;
- export freshness.

The results are in the hand-off and in the loop receipt.

## Limits

- **Not changed:** scope, lifecycle and `_STATUS.md`, the decomposition, the
  accepted amendment snapshot, `_COORDINATION.md` and
  `_ScopeChange/_LATEST.md`.
- **Pointers.** Only the ScopeClosureAudit per-amendment row moved, as that
  method directs.
- **Nothing is pushed or merged by this run. No release.**
