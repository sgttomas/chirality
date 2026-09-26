# Return C4 — SCA-005 post-change audit (TASK `pec-task`/opus, audit-decomp; child of B3)

HELP_HUMAN filing of the audit child's final report, verbatim below the rule. The report reached HELP_HUMAN because the host routed it to the dispatcher; HELP_HUMAN extracted it from the child's SubagentHandback call (extracted text SHA-256 `189a12c5a78a8c97ab6279d1c961fbb5e4c9a54971d67a8fe74477ec5d48d2bf`) and relayed it to B3, which verified the child's containment. Its audit snapshot is `execution/_Evaluation/DecompCoverage/COV_SCA005_POSTCHANGE_2026-09-25_1344/`.

---

## C4 post-change audit for SCA-005 (audit-decomp, SOFTWARE, full scope): complete

The revision-1.5 decomposition passed every structural check the method owns. The run found 2 blockers, 6 warnings and 74 info findings. Neither blocker is a defect: both come from the owner's A4 deferral. There is 1 defect, and it is a count error in the accepted plan, not in the decomposition.

**Output folder:** `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/agent-a05f45a57936b1abf/projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA005_POSTCHANGE_2026-09-25_1344/`

**Before writing:**
- All nine brief hashes matched: the instructions, the method files, the decomposition and the four registers.
- The live decomposition equals the accepted CP2 postimage `dc2b8479…9660` except front-matter lines 5 and 8.
- The registers and PRD v2.3 equal their accepted postimages byte-for-byte.
- The reliance-hold preflight (`dispatch-for-production`) returned `ALLOW`, exit 0.

**Files written (SHA-256):**

| File | SHA-256 |
|---|---|
| `Brief.md` | `c39a0d1d3091d632800b8e50c4984d1f60af2bea3f5e75779ee4bb62e3370e8f` |
| `Decision_Log.md` | `514bec98187a30210f72026bc6cbda1ef2d0af738b97ef0af7158e616cfc61ec` |
| `Decomp_Coverage_IssueLog.csv` | `e4a9633a7df410c416826d944eb6bc4f41cd6bfb36cf248c9c5ed31aba46af5c` |
| `Decomp_Coverage_Matrix.csv` | `e80b958b9aac7c0db0e9d4155298535f9cb7192096318806baf2f9a4ae447cad` |
| `Decomp_Coverage_Report.md` | `30ba94c63d0d8bacc175229a1f1e63416d9058a99b8e7ff5d7ce61a00fdeed0c` |
| `PrePost_Comparison.md` | `a288b3285cc53fb129825e5835137748ca40e55244dc3a5c0e81fad58c820432` |
| `QA_Report.md` | `b00455b3eb21c307362d1691e84a24affbb32b570fe91cfec981fcaa9379fde9` |
| `RUN_SUMMARY.md` | `b56645edc909fda426f9aeda38de2fcb30c7aa35d83f5504cd6b5d8bdbd03b07` |
| `coverage_summary.json` | `912610ff55e7e53788cb07c972a5a27afe5e246ecadb042932d57776cc0c4deb` |

## Verdict

- **Status:** `overall_status = BLOCKERS`, `closure_readiness = FAIL`, following the contract's count rule. I did not downgrade the method's severities.
- **Excluding expected consequences:** 0 blockers and 4 warnings, which would read `WARN`. The JSON carries this as `closure_readiness_excluding_expected_consequences` together with per-classification counts.
- **`RUN_STATUS`:** `WARNINGS`. The run is valid and complete.

| Classification | Blocker | Warning | Info |
|---|---|---|---|
| EXPECTED_CONSEQUENCE | 2 | 2 | 15 |
| PRE-EXISTING | 0 | 3 | 59 |
| DEFECT | 0 | 1 | 0 |

## Every blocker and warning

- **COV-001 / COV-002 (Check 2, BLOCKER, EXPECTED_CONSEQUENCE):** the DEL-02-08 and DEL-02-09 folders do not exist. The group-2 `DECISION.md` defers them to PROJECT_SETUP (Q-CP2-4 (a) "with A4 deferred", D-PEC-92) and says such findings are "reported as a consequence of this decision, not repaired".
- **COV-006 / COV-008 / COV-042 (Check 6, WARNING, PRE-EXISTING):** DEL-01-03 (IN_PROGRESS), DEL-01-05 (IN_PROGRESS) and DEL-08-02 (CHECKING) have no anticipated artifacts inside their folders; the bytes live under `projects/pec/v2/`. These are PRECHANGE COV-004, COV-006 and COV-040, unchanged.
- **COV-070 / COV-071 (Check 8, WARNING, EXPECTED_CONSEQUENCE):** SOW-095 and SOW-096 point to DEL-02-08 and DEL-02-09, which are declared but have no folders. Same A4 clause. I read "existing production units (from Check 2)" as meaning folders exist (Decision_Log D-6); the references do resolve to declared units.
- **COV-072 (Check 10, WARNING, DEFECT):** the accepted `Propagation_Plan.md` (L45, L802 in B1, L904) and your brief say 40 `_CONTEXT.md` files still await re-pinning. The real count is 42: 64 folders minus the 22 A2 mirrors, confirmed by census. The 42 are listed in `QA_Report.md`. B1's rule ("not written in A2") still selects all 42, so only the stated count and any count-based check are wrong. I did not correct it.

## Retired rows: confirmed on the real files

DEL-06-04, DEL-07-02, DEL-07-04 and DEL-07-05 raise no blocker and no warning. They produce 8 info findings:
- 4 in Check 6, carried from PRECHANGE with the reason changed and not escalated.
- 4 in Check 7 (COV-064..067), by design. The "supported only by RETIRED units" blocker cannot fire because no objective lists a retired supporter.

They also pass Checks 3, 4, 5, 8 and 11:
- Check 5 matches with the `(none — retired under SCA-005)` rendering.
- Check 11 recognizes `RETIRED`.
- Their `_STATUS.md` files equal the planned A3 postimages, and all 26 A2/A3 postimage hashes match.

The plan's expected closure-tool isolated-node warnings for the retired deliverables do not appear yet. Their registers still hold 18 ACTIVE rows until B3 (COV-080).

## Your expected pre-acceptance posture, as observed

- **Pointers still on revision 1.4 / SCA-004** (COV-073, info): confirmed. The pointer hashes no longer match the working tree, but revision 1.4 is exactly recoverable at `2b0572fe0`.
- **Pre-B3 dependency state:** confirmed exactly.
  - 119 edges, 0 strongly connected components, 0 bidirectional pairs.
  - DEL-00-03 and DEL-01-05 are isolated.
  - `DEP-09-05-005` is still present (COV-079).
  - The validator reports 0 errors and the 2 DRB-008 warnings (COV-081).
- **Derivative currency:** 64 `_REFERENCES.md` (COV-078) and all 32 SOWs (COV-082) are unchanged, as expected. The contexts are 42, not 40 (COV-077 and COV-072).
- **COV-074 (info, pre-existing):** the pointer metadata fields that understate the earlier repairs are carried over from PRECHANGE COV-071.

Two items need the reviewer's attention:
- **COV-076 (info, expected, flagged):** the 22 A2 mirrors already say revision 1.5 is `current_basis`, before checkpoint-3 acceptance. They are the accepted exact bytes, but the pre-acceptance treatment given to the decomposition front matter was not applied to them. If checkpoint 3 is refused, rollback must include them.
- **COV-075 (info):** the SCA-005 snapshot is mid-A5. `Post_Change_Coverage.json` and `RUN_SUMMARY.md` are absent, and the `Handoff_State.md` heading still says "Checkpoint-group-1".

## Pre/post headline against COV_SCA005_PRECHANGE_2026-09-23_2139

| Metric | PRECHANGE | POSTCHANGE |
|---|---|---|
| Scope items (IN/OUT/TBD) | 94 (72/14/8) | 96 (70/18/8) |
| Deliverable rows | 64 | 66 (62 active / 4 retired) |
| Packages / objectives | 11 / 6 | 11 / 6 |
| Forward deliverable coverage | 100% | 96.97% |
| Context fidelity | 100% | 100% |
| Unmapped IN rows / active deliverables | 11 / 9 | 0 / 0 |
| Lifecycle | 26 INITIALIZED / 32 OPEN / 4 CHECKING / 2 IN_PROGRESS | 26 / 28 / 4 / 2 plus 4 RETIRED |
| Active envelopes (S/M/L) | 28/34/2 | 28/32/2 |
| Issues (blocker/warning/info) | 0/3/69 | 2/6/74 |

Per finding: 62 carried, 6 resolved (the TM-PEC-023-mapped deliverables), 4 changed and 16 new (15 expected, 1 defect).

## Checks I could not run or did not perform

- No independent review of this snapshot; C4 requires a separate reviewer.
- C1, C3 and C5 are only partly covered, as evidence rather than as the lanes themselves.
- `_run_records`, the retired `_DEPENDENCIES.md` mirrors and the SOW text were not audited for content.
- Check 9 is skipped because the method does not assign it to the SOFTWARE variant.
- Artifact matching is limited to each deliverable folder.

## Notes

- **Concurrent commits:** you committed `5d2770350` (A1–A3) and `7e8374ae2` (the B3 interim return) in this worktree during the run. A second census over the committed tree matched the first, so the audited bytes are those of `5d2770350`.
- **Scratch folder:** the closure tool overwrote a pre-existing scratchpad `depclosure/` folder, which lives outside the repo.
- **Boundaries held:** I made no git operations and wrote nothing outside the output folder. `_Evaluation/DecompCoverage/_LATEST.md` is unchanged (`0084d218…7432`).

**Next steps for you:** copy `coverage_summary.json` to `Post_Change_Coverage.json` (A5), correct 40 to 42 in the SCA-005 handoff and summary, then run the independent review.
