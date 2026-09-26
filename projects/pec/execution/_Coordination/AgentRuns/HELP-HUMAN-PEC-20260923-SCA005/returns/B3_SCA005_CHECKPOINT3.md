# B3 return — SCA-005 checkpoint-3 preparation

WORKING_ITEMS (Type 1), node B3 of HELP_HUMAN run `HELP-HUMAN-PEC-20260923-SCA005`.
Brief `B3_SCA005_CHECKPOINT3.md`, SHA-256 `69c2296749cee727e1bd84b13f7a4ebcad93400f8ceb6267519e79601811b17f`. The brief is held by HELP_HUMAN and is not yet committed under `briefs/`.
Branch `claude/pec-sca005-cp3-execution`, cut from `origin/main` `2b0572fe049c8ffaa02d61b7dbbc3ae41bc589f6`. Package revision `958a23385`; this return is committed on top of it. The PR is not merged.

**Status:** checkpoint-3 package prepared and independently verified (verdict 01 PASS WITH MINOR, repaired; verdict 02 PASS); it now awaits the owner.
- Verifier verdict 01 was PASS WITH MINOR, with no blocking finding. I repaired its three MINOR findings in `958a23385`.
- The cycle-2 re-verification of those repairs returned **PASS** and is saved as verdict 02. No finding remains in the package; the only residual item (R-1, committing the B3 brief) belongs to HELP_HUMAN.

## Instruction and authority sources (SHA-256)

| Source | SHA-256 |
|---|---|
| `AGENTS.md` | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | `46689c36d5379029a34a5c5d26f109445e338fca82b86e590826bcbc39ad3846` |
| `agents/AGENT_WORKING_ITEMS.md` | `9ae4bea25bd95750a6878a9d53fbbbd7cd058d72c652a36baf4aa90601799665` |
| scope-change `WORKFLOW.md` | `58f5d1d53c655fdc5668d928f6087003590f40e321e25e3d9447805ee64a7a90` |
| scope-change `resources/contract.md` | `4453a719f1588c4eba08bdb4a979140ff3541ed5a29f04477ea58a844f344d02` |
| scope-change `resources/method.md` | `34187e83856853f655389625e3465e3c2cb9ff8ad38be1f4d138ee7470d167f5` |
| `Propagation_Plan.md` | `50cd0b1d91ea25cc8ecba28ce649278b376fb952feec09e007a26ca5bbf91350` |
| `Amendment_Preview.md` | `ad48cc5621d796a662addc03640a32f7f4cdafbf627ad6fda3f60bdede65ebe4` |
| group-2 `DECISION.md` / `ACCEPTED_MANIFEST.csv` | as merged in PR #909 |
| audit-decomp `WORKFLOW.md` | `4aaa7e10990ddd1b769ba09da78a03f9f491a6b6f3be6df08a1a8de93c26e3e6` |
| audit-decomp `contract.md` | `70a5abebc8ff34826415e1566715373a322baded2939325b5b73828d78401a0c` |
| audit-decomp `method.md` | `97df84022ccbec434aea9745296b93b6e549ef840acc0ca9df0a215e634d79c2` |
| `pec_reliance_hold.py` | `b1712e4b6e9f1476c577afd9170a4dd078beaa95878fa5f3b6c46a17b548cd0e` |
| `ACTIVE_RELIANCE_HOLDS.csv` (header only) | `f877d9316c7da76218399838aa6b69f1bb51bbd3e59b5b1d19b31f69ad741cbc` |
| relayed C4 report (`relay_C4.md`, below) | `189a12c5a78a8c97ab6279d1c961fbb5e4c9a54971d67a8fe74477ec5d48d2bf` |

## Preconditions (all PASS before any write)

- Every live preimage matched the plan: the 6 A1 files, the 22 `_CONTEXT.md` and the 4 `_STATUS.md`.
- Both pointer hashes matched.
- The group-2 manifest matched, except the two rows labelled "at package publication".
- The `D-PEC-92` row is on `origin/main`.
- The reliance-hold preflight (`dispatch-for-production`) returned ALLOW for all targets.

## Written files and hashes

For every Lane A path with its preimage and postimage, see the table in `_ScopeChange/SCA-005_2026-09-23_2139/RUN_SUMMARY.md` §"Actions taken". There are 32 paths, and all equal their planned hashes.
- **Decomposition:** `7cca5cdb…5c81` → `37ea1084a8219943a69057be377646c69a609a76728241963045d7cfb015a6cc`. This is the pre-acceptance form; the accepted form is `dc2b8479…9660`.
- **Registers and PRD:** byte-for-byte copies of `CP2_CANDIDATE`.

Snapshot files:

| File | SHA-256 |
|---|---|
| `Supersession_Map.csv` (accumulator: exit 0, 29 rows, 0 findings) | `4ca705ba090cafb9a74870a0095be490c1d507149767dac32ec52879c487240c` |
| `Post_Change_Coverage.json` | `912610ff55e7e53788cb07c972a5a27afe5e246ecadb042932d57776cc0c4deb` |
| `RUN_SUMMARY.md` | `e3480b782b9e219af1a0dcb569829df8d6014f617ffe826f2afc33529107196a` |
| `Decision_Log.md` | `85676c5326da5446e62698c70760a2c55eea011bc4e2810727e3509f393f4d7b` (was `db1a3518…`) |
| `Handoff_State.md` | `8dd8b250ce375ebe27eb921d79be3d8175badf3a4f1f93a9964eb9d8587a8126` (was `1a21d90a…`) |

The audit child wrote 9 files in `COV_SCA005_POSTCHANGE_2026-09-25_1344/`. Its `coverage_summary.json` is `912610ff…4deb`.

Verdict 01 is saved as `returns/B3_VERIFIER_VERDICT_01.md` (`49da32a663f82191099d1e208cec4788c7ee410115db1740fcd5cad45d1f9414`).

## Slot values

All slots are 2026-09-25, the application date and the package default:
- decomposition front matter `date:`;
- the §7 Revision row;
- the DL-20 date cell;
- the four `_STATUS.md` Last Updated and History dates;
- the PRD slots, which equal the group-2 act.

Because every slot equals the default, each slot-substituted hash equals its accepted hash.

## C1–C5

**C1 (containment): PASS.**
- 49 changed paths, all on the allowlist, and 32 of 32 at their exact hashes.
- No frozen or checkpoint-snapshot artifact changed, and neither did any other status or context file, SOW, dependency file, `_REFERENCES.md`, `v2/**` or foreign path.
- `git diff --check` flags only the CRLF line endings in the accumulator-written `Supersession_Map.csv`. That is deterministic tool output, byte-identical to a fresh run, and A5 forbids hand-editing it.

**C2 (structure): expected result.**
- Strict validator: 0 errors and 2 DRB-008 warnings, for DEL-02-08 and DEL-02-09. It exits 1 under `--strict`.
- `analyze_dep_closure.py`:
  - 119 edges, 0 SCCs and 0 bidirectional pairs;
  - isolated nodes DEL-00-03 and DEL-01-05;
  - `DEP-09-05-005` present.

  This is the pre-B3 topology the group-2 decision expects.

**C3 (successor assertions): 31 of 31 PASS.**

**C4 (audit): BLOCKERS by the method's count rule.**
- Counts: 2 blockers, 6 warnings and 74 info; `closure_readiness` is FAIL.
- The two blockers, COV-001/002, are the absent DEL-02-08/09 folders. They are an expected consequence of the A4 deferral.
- Excluding expected consequences, the audit has 0 blockers and 4 warnings (3 pre-existing, 1 defect) and would read WARN.
- COV-072 is the defect. The plan and the brief say 40 `_CONTEXT.md` files await the B1 re-pin, but the census finds 42. I recorded this as an evidence correction, not a plan change. No C3 assertion or closure field depends on the number.
- Retired rows produce INFO findings only.
- COV-076: the 22 A2 mirrors already name revision 1.5 as `current_basis`. This is recorded in the rollback notes and in the owner question.
- I verified the child's containment claim: only its folder changed, and `DecompCoverage/_LATEST.md` is unchanged.

**C5 (snapshot completeness): complete.** Every artifact is hashed in `Handoff_State.md`, and the checkpoint-1 and checkpoint-2 artifacts are byte-unchanged.

## Closure state fields

| Field | Value |
|---|---|
| `DecompositionTruthState` | `COMPLETE` |
| `DerivativePackageState` | `INCOMPLETE` |
| `ContentRemediationState` | `NOT_REQUIRED` |
| `DownstreamRerunState` | `FROZEN` |
| `MetadataAlignmentState` | `IN_PROGRESS` |
| `AuditState` | `BLOCKED` by the count rule; the classification-adjusted reading beside it is `WARN` |
| `ReadyForNextPhase` | `NO` |
| Closure verdict | `OPEN_PENDING_DERIVATIVE_CLOSURE` now; `CLOSED_FOR_SCOPE_CHANGE_ONLY` recommended on acceptance |

## Checkpoint-3 question set

The full set is in `RUN_SUMMARY.md` §"Checkpoint-3 owner question".
- **Q-CP3-A: accept the audited poststate.** Recommendation: accept.
- **Q-CP3-1: closure verdict on acceptance.**
  - (a) `CLOSED_FOR_SCOPE_CHANGE_ONLY`, with A4 and Lane B recorded open.
  - (b) `OPEN_PENDING_DERIVATIVE_CLOSURE` until a re-audit after A4 and B3.

  Recommendation: (a).

## Verifier cycles

| Cycle | Reviewed revision | Verdict | Result |
|---|---|---|---|
| 01 | `bbee14b03` | PASS WITH MINOR | See the findings below |
| 02 | `958a23385` | PASS | Saved as `returns/B3_VERIFIER_VERDICT_02.md`; residual R-1 is HELP_HUMAN's |

Verdict 01 findings:
- **MINOR-1:** the `git diff --check` wording. Repaired.
- **MINOR-2:** the timing of the foreign notices. Aligned to `DECISION.md` §Notices: HELP_HUMAN writes them during checkpoint-3 preparation, before or with the checkpoint-3 presentation.
- **MINOR-3:** the B3 brief is not committed. Committing it is HELP_HUMAN's write, and the citation now says where the brief is held.
- **NOTE-1 to NOTE-5:** NOTE-1, NOTE-4 and NOTE-5 were addressed in the text. NOTE-2 and NOTE-3 were accepted as they stand.

## Unresolved (for HELP_HUMAN)

1. Nothing is blocking. Verdict 02 is PASS.
2. Commit the B3 brief at `briefs/B3_SCA005_CHECKPOINT3.md` with SHA-256 `69c22967…11b17f` (MINOR-3).
3. Write the three foreign notices below, before or with the checkpoint-3 presentation.
4. Present checkpoint 3 to the owner. After acceptance, carry out A6 with the checkpoint-3 dates.
5. If the owner refuses checkpoint 3, restore every Lane A path, including the 22 A2 mirrors (COV-076).
6. Suggested Root follow-up, not in scope here: the accumulator writes CRLF files.

## Draft notice texts

The full texts are in the manager's handback. Their substance:
1. **To Root, `execution/_Coordination/NOTICE_2026-09-25_PEC_SCA-005_RETIRED_STATUS_METHOD_TOOL_MISMATCH.md`:** four Root surfaces disagree about RETIRED:
   - the scope-change method and contract, which require a RETIRED `_STATUS.md`;
   - `write_status.sh` L86 and L99–101, which admit only OPEN..ISSUED and exit 2;
   - `docs/SPEC.md` §3.2 and L985, which say RETIRED is never an active lifecycle value;
   - `adapter_project.py` L124–125, which rejects RETIRED for non-Root projects.

   PEC used hand-authored edits under Q-CP2-1 (a) and D-PEC-92, and does not depend on Root's answer.
2. **To Root, `…_ROOT_LOOP_INIT_HISTORICAL_LEDGERS.md`:** Root `execution/_Coordination/LOOP_INIT.md` L15 lists the App and Piping `loop/LOOP_RECEIPTS.md` files. Those ledgers are frozen (App at Receipt-264, Piping at Receipt-162; survey finding DR-17). Central `RECEIPT.md` files are now current.
3. **To the App and Piping loops, `…_ADAPTER_YAML_FEED_SURFACES.md` in each loop's `execution/_Coordination/`:** under O-B2, PEC reads the loops' surfaces through its own `loops.json` feed profiles. Their `_harness/adapter.yaml` declares none of those surfaces. DEL-02-07 reads `adapter.yaml` only as a parity peer. Nothing is needed from those loops, and PEC writes none of their files.

Every notice ends with the standard non-binding closing paragraph from the D-PEC-90 notice.

## Delegation record

| Child | Mechanism | Scope | Return |
|---|---|---|---|
| C4 audit-decomp (TASK) | Claude Code Agent tool; `pec-task`, `model: opus`; background | The COV folder only; no `_LATEST.md`; no git. Instruction-asserted, and verified afterwards. | Relayed to HELP_HUMAN (appendix below) |
| Verifier (TASK, read-only) | Claude Code Agent tool; `pec-reviewer`, `model: opus`; the tool forbids writing | Read-only | Verdict 01 saved; cycle 2 pending |

## Appendix: C4 child's report (relayed)

Relayed by HELP_HUMAN from `scratchpad/relay_C4.md` (SHA-256 `189a12c5…d2bf`).

Summary of the relay:
- **Result:** the audit wrote 9 files. It reads BLOCKERS by the count rule, with 2 blockers, 6 warnings and 74 info.
- **Classification counts:**

  | Classification | Blockers | Warnings | Info |
  |---|---|---|---|
  | EXPECTED_CONSEQUENCE | 2 | 2 | 15 |
  | PRE-EXISTING | 0 | 3 | 59 |
  | DEFECT | 0 | 1 | 0 |

- **Findings:** COV-001/002 are blockers expected from A4. COV-070/071 are expected warnings. COV-006/008/042 are pre-existing. COV-072 is the 40→42 defect. COV-076 is flagged. Retired rows raise INFO only.
- **Pre/post change:**
  - scope items 94 → 96;
  - deliverables 64 → 66 (62 active);
  - forward coverage 100% → 96.97%;
  - unmapped entries 11/9 → 0/0.
- **Boundary:** the child reports that it held its boundary and made no git operations.

The full relayed text is preserved in the scratchpad file.
