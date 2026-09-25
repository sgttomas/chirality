# Run Summary — COV_SCA005_POSTCHANGE_2026-09-25_1344

`RUN_STATUS = WARNINGS`

The run is valid and complete. Every check produced a verdict, and no input
failed. Blocker-severity findings are present, and all of them are expected
consequences.

## Headline

| Field | Value |
|---|---|
| Overall status | `BLOCKERS` |
| Closure readiness | `FAIL`, method-literal: 2 BLOCKERs, both `EXPECTED_CONSEQUENCE` |
| Closure readiness excluding expected consequences | `WARN`: 0 blockers; 4 warnings = 3 `PRE-EXISTING` + 1 `DEFECT` |
| Issues | 2 blockers / 6 warnings / 74 info |
| By classification | `EXPECTED_CONSEQUENCE` 2 B / 2 W / 15 I; `PRE-EXISTING` 0 / 3 / 59; `DEFECT` 0 / 1 / 0 |
| Audited basis | revision 1.5 `candidate_pending_checkpoint_3`, `37ea1084…a6cc` (commit `5d2770350`). It equals the accepted CP2 postimage except for the two pre-acceptance front-matter lines. The registers and PRD v2.3 equal their accepted postimages |
| Phase | SCA-005 checkpoint-3 post-change validation, before any pointer moves |

## Coverage

- **Packages:** 11/11.
- **Deliverables:** 64/66 have folders (62 active and 4 retired rows).
  DEL-02-08 and DEL-02-09 are absent under the A4 deferral.
- **Contexts:** 64/64 match their registers.
- **Lifecycle:** 26 `INITIALIZED`, 28 `OPEN`, 4 `CHECKING`, 2
  `IN_PROGRESS`, 4 `RETIRED`.
- **Contracts:** 32 `SOW_V1`, 32 `NONE`, 0 ambiguous.
- **Ledger:** 96 rows (70 IN / 18 OUT / 8 TBD). All IN rows resolve to
  declared, non-retired units. Reciprocity holds for 66/66 and the union rule
  for 62/62.
- **Objectives:** all 6 are supported and their evidence is internally
  consistent. 0 IN rows and 0 active deliverables lack an objective.
- **Telemetry and envelopes:** §7 telemetry equals the registers. Active
  envelopes are S 28 / M 32 / L 2 / XL 0.
- **Strict validator:** 0 errors and 2 DRB-008 warnings, as expected. Exit
  is 1 under `--strict`.
- **Dependency closure (pre-B3):** 119 edges, 0 SCCs, 0 bidirectional pairs.
  DEL-00-03 and DEL-01-05 are isolated, and `DEP-09-05-005` is still present.
- **Reliance-hold preflight:** `ALLOW` (exit 0).

## Every BLOCKER and WARNING

| Issue | Check | Severity | Entity | Classification | Reason |
|---|---|---|---|---|---|
| COV-001 | 2 | BLOCKER | DEL-02-08 | EXPECTED_CONSEQUENCE | No folder exists. The group-2 DECISION.md (Q-CP2-4 (a) "with A4 deferred"; D-PEC-92) defers creating it to PROJECT_SETUP and says such findings are "reported as a consequence of this decision, not repaired" |
| COV-002 | 2 | BLOCKER | DEL-02-09 | EXPECTED_CONSEQUENCE | Same as COV-001 |
| COV-006 | 6 | WARNING | DEL-01-03 | PRE-EXISTING | `IN_PROGRESS` with no anticipated set in the folder, because the bytes live under `projects/pec/v2/`. This was PRECHANGE COV-004 |
| COV-008 | 6 | WARNING | DEL-01-05 | PRE-EXISTING | Same pattern. This was PRECHANGE COV-006 |
| COV-042 | 6 | WARNING | DEL-08-02 | PRE-EXISTING | `CHECKING`, with the source-tree bytes outside the folder. This was PRECHANGE COV-040, and has been unchanged since SCA-004 |
| COV-070 | 8 | WARNING | SOW-095 | EXPECTED_CONSEQUENCE | The IN row references DEL-02-08, which is declared but has no folder (the A4 deferral, same clause as COV-001). Resolution at the declaration level passes |
| COV-071 | 8 | WARNING | SOW-096 | EXPECTED_CONSEQUENCE | Same as COV-070, for DEL-02-09 |
| COV-072 | 10 | WARNING | SCA-005 | **DEFECT** | The accepted `Propagation_Plan.md` (L45, L802, L904) and the C4 brief give the unrepinned `_CONTEXT.md` population as 40. The observed count is 42: 64 folders minus 22 A2 mirrors. This is a documentary count error that understates a stale population. B1's enumerating rule still selects all 42 |

## Retired-row representation: confirmed

The four retired deliverables (DEL-06-04, DEL-07-02, DEL-07-04, DEL-07-05)
raise **no BLOCKER and no WARNING**. They produce only 8 INFO findings:

- 4 in Check 6, carried from PRECHANGE with the reason changed and not
  escalated.
- 4 in Check 7, by design. The `RETIRED`-only BLOCKER cannot fire, because no
  objective lists a retired supporter.

They also pass Checks 3 (declared), 4 and 5 (MATCH with the
`(none — retired under SCA-005)` rendering), 8 (no IN row references them)
and 11 (`RETIRED` is recognized). Their `_STATUS.md` files equal the planned
A3 postimages, and their folders are retained intact.

One part of the plan's C4 expectation is not yet observable: the closure-tool
isolated-node warnings for the retired DELs. The retired registers still hold
ACTIVE edges until B3 (COV-080).

## Expected pre-acceptance posture: observations

| Briefed expectation | Observed | Issue |
|---|---|---|
| Pointers name revision 1.4 / SCA-004. Front matter is candidate status with a pre-acceptance `accepted:` line | Confirmed. The pointer and SCA-004 hashes describe revision 1.4, which is recoverable at `2b0572fe0` | COV-073 INFO |
| A4 deferred: DEL-02-08/09 rows present, folders absent | Confirmed | COV-001/002 BLOCKER; COV-068/069 INFO; COV-070/071 WARNING; COV-081 INFO |
| B3 not opened: 119 edges, 0 SCCs, isolated DEL-00-03/01-05, `DEP-09-05-005` present | Confirmed exactly | COV-079, COV-080 INFO |
| Four retired deliverables raise at most INFO | Confirmed | COV-033/037/039/040, COV-064..067 INFO |
| "40 `_CONTEXT.md`" and 64 `_REFERENCES.md` provenance lines still at revision 1.4; SOWs not refreshed | 64 `_REFERENCES.md` and the SOWs are as briefed. **The contexts are 42, not 40** | COV-077, 078, 082 INFO; COV-072 WARNING (DEFECT) |

Two further observations need the reviewer's attention:

- **COV-076 (INFO, EXPECTED_CONSEQUENCE, flagged).** The 22 A2 mirrors
  already call revision 1.5 `current_basis` before the checkpoint-3
  acceptance. These are the accepted exact bytes, but the claim is
  anticipatory. If checkpoint 3 is refused, the rollback must include them.
- **COV-075 (INFO).** The SCA-005 snapshot is mid-A5.
  `Post_Change_Coverage.json` and `RUN_SUMMARY.md` are absent until this run
  returns. The `Handoff_State.md` heading still says "Checkpoint-group-1".

## Pre/post headline (full detail in `PrePost_Comparison.md`)

| Metric | PRECHANGE | POSTCHANGE |
|---|---|---|
| Scope items | 94 (72/14/8) | 96 (70/18/8) |
| Deliverable rows | 64 | 66 (62 active / 4 retired) |
| Packages / objectives | 11 / 6 | 11 / 6 (unchanged) |
| Forward deliverable coverage | 100% | 96.97% (64/66) |
| Context fidelity | 100% | 100% |
| Unmapped IN rows | 11 | 0 |
| Unmapped active deliverables | 9 | 0 |
| Issues (blocker/warning/info) | 0/3/69 | 2/6/74 |

**Per-finding delta.** 62 carried, 6 resolved (the six TM-PEC-023-mapped
deliverables), 4 changed (3 unmapped rows became retired rows, and the empty
SCA-005 folder became the A5-in-progress snapshot) and 16 new (15 expected
consequences and 1 defect).

## Next action for the caller

- Copy this `coverage_summary.json` to `Post_Change_Coverage.json` (A5).
- Correct the 40 → 42 count in the SCA-005 `Handoff_State.md`/`RUN_SUMMARY.md`
  and in any B1 acceptance check. This audit made no correction.
- Carry every classification above into the checkpoint-3 presentation, and
  run the independent review that C4 requires.

This snapshot is derivative evidence. It accepts nothing and authorizes
nothing. The audit `_LATEST.md` pointer is unchanged.
