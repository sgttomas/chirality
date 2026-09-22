# V-DEL-00-02 — verifier shard notes (R2, PKG-00)

Shard `DEL-00-02`, unit `DEL-00-02`, 15 selected items. Evidence was read from the frozen tree at
`00115c719` only. Git use was read-only `log`, `show` and `blame -L`. No errata file exists for
this unit, so there are no class e items. There are also no class c items in the selection.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a (LOW / self-flag / UNKNOWN) | 3 | 2 | 1 | 0 |
| n (30% of other non-ALIGNED) | 9 | 9 | 0 | 0 |
| b (15% of ALIGNED) | 3 | 3 | 0 | 0 |
| **Total** | **15** | **14** | **1** | **0** |

- **Distinct items refuted on a verdict field:** 1 of 15 (`DEL-00-02#CLM-014.2`, Disposition).
- **REFUTED lines:** the one refuted item has 6 lines: Disposition, ImplementationEvidence,
  VerificationEvidence, DirectionEvidence, CauseTag and RemainingWork. The last five follow from
  the Disposition.

## (ii) Patterns

1. **UNKNOWN recorded where the evidence can be checked inside the roots.** `CLM-014.2`
   (AC-001: every legacy source line is preserved) was left `UNKNOWN` because no parity artifact
   was found.
   - The check can be done with read-only `git show`. The pre-migration Datasheet,
     Specification, Procedure and Guidance files are available at `fae8e5117^`.
   - All 209 non-blank legacy lines appear in `ScopeOfWork.md` at `670a71ed0`. Only the heading
     levels changed.
   - At `00115c719`, 11 of those lines differ. They were changed by the owner-ruled D-APP-65 and
     D-APP-68 repairs (`_run_records/TASK_RUN_2026-07-19_DAPP68_concordance_repairs.md:12`).
   - My correct reading is `ALIGNED`. `PARTIALLY_IMPLEMENTED` is the alternative if ruled
     amendments count as non-preservation.
   - The worker's LEAST-CONFIDENT worry about a Root migration run outside the roots does not
     arise, because the check needs no out-of-root evidence.
2. **The stale D53A pointer is handled consistently.**
   - `CLM-003` and `CLM-005` are `STALE_SPECIFICATION`, with `CLM-005` as a SEE row.
   - `CLM-009` is `PARTIALLY_IMPLEMENTED` with `ALSO:STALE_SPECIFICATION`.
   - `REGISTER-2` is `STALE_SPECIFICATION`: REF-004 and REF-005 stayed CURRENT when `a1ab4ac29`
     (D-APP-56 R5 P42) demoted REF-003.
   - All of these reproduce: `_LATEST.md:1`, `_REGISTER.md:126`, `DAG_CLOSURE_CONTROL.md:9,64,99,109`
     and `_REFERENCES.md:9-13`. The D-APP-111 and D-APP-114 scopes do not name DEL-00-02, so
     MR-11 is correctly not applied.
3. **Minor anchor imprecisions that do not change any verdict.** They were not refuted.
   - `CLM-010.4` says the Owner_Workflow_Handoff rows are all "SUPERSEDED/CLOSED/DEFERRED".
     HOFF-SCC-001-009 is actually `COMPLETE_GRAPH_REDUCTION_ONLY`.
   - `CLM-003` cites `DAG_CLOSURE_CONTROL.md` lines 97-98. Those lines are a heading and a
     blank line; the 1034 snapshot text is at line 99.
   - `CLM-009` cites `CONTROL.md:3-10` for the SAFE_MOVES closure. The same lines also call
     SAFE_MOVES the "Current Snapshot", which is a further stale carrier that the ledger does
     not name.
   - `CLM-010.5` AssessmentEvidence `STILL CURRENT` relies on the in-file P43 superseding
     annotation (`Assessment_INSP-03_DEL-00-02.md:62-71`). `OVERTAKEN` would also be defensible,
     since the original INSP-03 row recorded PARTIAL.

Also checked and holding:

- `CLM-011` is `STALE_SPECIFICATION` / `PRE_V3_DRIFT`. App SPEC §6 has existed since
  2026-05-20 (blame `26fc253b5`, `docs/SPEC.md:363`). The TBD line dates from `670a71ed0`
  (2026-07-14).
- `REGISTER-3`: `_STATUS.md:4` is dated 2026-07-12, while the History entries at lines 28-29 are
  dated 2026-07-18 and 2026-07-19.
- None of the relied-on files appear in `TOUCHED_PATHS.csv`, so `PostReleaseBasis = NO` holds.

## (iii) Effort

- **Files read:** about 20 files at the frozen tree. These were the SoW, `_STATUS`,
  `_REFERENCES`, `CONTROL`, the INSP-03 assessment, two run records, `DAG_CLOSURE_CONTROL`,
  `_LATEST`, register rows, App SPEC §6, the Dependency_Closure_Report and closure_summary for
  the 1034/D53A/SAFE_MOVES snapshots, and the case files.
- **Git:** about 8 read-only `git` calls, including one scripted line-parity comparison of the
  legacy docs against the SoW.
- **Context budget:** not tight.
