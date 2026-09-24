# Decomposition Coverage Report — SCA-005 pre-change

**Variant:** `SOFTWARE` · **Decomposition:** revision **1.4**
(`current_basis`, SHA-256
`7cca5cdbb1ba4bd866391abf00998bc80f587a23505a6f5b6bceb8df48b65c81`) ·
**Scope:** `ALL` · **Status:** `WARNINGS` (0 blockers / 3 warnings / 69 info)
· **Closure readiness:** `WARN`

**Expected source:**
`projects/pec/execution/_Decomposition/_LATEST.md` revision 1.4
`current_basis`. SCA-004 is closed `CLOSED_FOR_SCOPE_CHANGE_ONLY`, and
`_ScopeChange/_LATEST.md` names `SCA-004_2026-08-02_2325`. D-PEC-86 SCA-005
Gate 1 is cited separately. The owner opened it by direction on 2026-09-23,
and it is not a checkpoint-1 acceptance. **Expected phase:** `SCA-005
checkpoint group 1 pre-change baseline`.

| # | Check | Verdict |
|---|---|---|
| 1 | Forward packages | `PASS`: 11/11 |
| 2 | Forward deliverables | `PASS`: 64/64 |
| 3 | Reverse coverage | `PASS`: no reverse-only package, deliverable, non-`DEL` or non-`1_Working` folder |
| 4 | ID consistency | `PASS`: all folder IDs and parent packages equal the declared IDs |
| 5 | Context fidelity | `PASS`: 64/64 `_CONTEXT.md` match `Deliverables.csv`, including `ContextEnvelope` |
| 6 | Artifact presence / contract shape | `WARNING` ×3, `INFO` ×58. 3/64 anticipated sets found. 32 valid `SOW_V1`, 32 absent at `OPEN`, 0 ambiguous |
| 7 | Objective mapping | `PASS` for all six objectives. `INFO` ×9 for the accepted unmapped-deliverable residue |
| 8 | Ledger integrity | `PASS`: 94 rows (`72 IN / 14 OUT / 8 TBD`). All 72 `IN` package and deliverable references resolve |
| 9 | Derivative parity | `SKIPPED`: not owned by the SOFTWARE variant |
| 9b | Package-shape conformance | `PASS`: the companion inventory and authority roles are explicit and consistent |
| 10 | Active snapshot / handoff state | `PASS`: SCA-004 is uniquely active, complete and honest. `INFO` ×2 (stale-conservative pointer fields; non-active SCA-005 candidate folder) |
| 11 | Lifecycle distribution | `PASS`: 26 `INITIALIZED`, 32 `OPEN`, 4 `CHECKING`, 2 `IN_PROGRESS`. No unrecognized state |

Formal comparison mode was not requested and is `SKIPPED`. An informational
delta is given below.

## Coverage and context evidence

All 11 declared packages (`SOFTWARE_DECOMP.md` §4, lines 365–375) and all 64
declared deliverables (§5 compact tables, and `Deliverables.csv` rows 2–65)
have exact filesystem folders under `projects/pec/execution/PKG-*/1_Working/`.
No undeclared folder exists. The §5 compact control fields (name, type,
envelope, phase, covers) match `Deliverables.csv` for all 64 rows.
`ContextBudgetQA.csv` envelopes and packages match for 64/64. Every
`_CONTEXT.md` agrees with its register row on these fields: DeliverableID,
name, package ID and name, type, `ContextEnvelope`, `PhaseHint`, covered scope
items, supported objectives, responsible party, description, anticipated
artifacts and envelope notes. All 64 provenance blocks now name revision 1.4.

## Objective evidence (Check 7)

Objectives resolve from the `ScopeLedger.csv` `ObjectiveIDs` column. There
are six: OBJ-001..OBJ-006.

| Objective | IN scope items (ledger) | Supporting deliverables (`SupportsObjectives`) |
|---|---|---|
| OBJ-001 | 22 | 20 |
| OBJ-002 | 12 | 12 |
| OBJ-003 | 13 | 12 |
| OBJ-004 | 11 | 10 |
| OBJ-005 | 9 | 7 |
| OBJ-006 | 9 | 9 |

For every objective, the scope-item set and the deliverable set equal the §3
objective-side view (`SOFTWARE_DECOMP.md` lines 322–327, "Mapped Scope Items"
and "MappedDeliverables" with ranges expanded). Each set also equals the set of
deliverables reached through the ledger rows. Every supporting deliverable
folder exists, and no objective depends only on `RETIRED` units. The §7
metrics also agree with the registers (line 532 `94 (72 IN / 14 OUT / 8 TBD)`;
line 539 `IN items without objective mapping 11`). Nine deliverables and 11
`IN` rows remain unmapped residue. That is the TM-PEC-023 blank population,
which D-PEC-86 I-3 carries into SCA-005 intake without selecting any mapping.

## Artifact and lifecycle evidence (Checks 6 and 11)

Deliverable-local matching found three anticipated sets: the ADR set for
`DEL-00-01` (`artifacts/v2/ADRs.md`), the SPEC for `DEL-00-03`
(`artifacts/v2/SPEC.md`), and the measurement method and baseline for
`DEL-10-01` (`artifacts/STEP0_COST_BASELINE_METHOD.md`,
`artifacts/STEP0_COST_BASELINE.md`). The other 58 absences are informational
at `OPEN` or `INITIALIZED`.

Three absences are warnings under Step 6's escalation rule:

- **COV-004 `DEL-01-03`** is `IN_PROGRESS` (`_STATUS.md:3`; D-PEC-85 P-A
  production start 2026-09-08). "Store lifecycle module + guard + tests" is
  not inside the deliverable folder. The D-PEC-85 candidate bytes live under
  `projects/pec/v2/src/pec_v2/` and `projects/pec/v2/tests/storage/`, and no
  artifact acceptance is recorded.
- **COV-006 `DEL-01-05`** is `IN_PROGRESS` (`_STATUS.md:3`; the D-PEC-84 L
  CHECKING→IN_PROGRESS reversal of 2026-09-07). "CI/lint check + posture note"
  is not inside the deliverable folder. The bytes live under
  `projects/pec/v2/tools/` and `projects/pec/v2/tests/enforcement/`.
- **COV-040 `DEL-08-02`** is `CHECKING`. This warning is unchanged from SCA-004.

These warnings are evidence about where the artifacts are located. They do
not dispute the accepted or candidate source bytes, or any ruling about them.

Lifecycle is 26 `INITIALIZED`, 32 `OPEN`, 4 `CHECKING` (`DEL-00-01`,
`DEL-00-03`, `DEL-08-02`, `DEL-10-01`) and 2 `IN_PROGRESS` (`DEL-01-03`,
`DEL-01-05`). Every non-`OPEN` deliverable carries a `SOW_V1` contract.
`DEL-01-03/MEMORY.md` is the only sibling memory file, and it is consistent
with `IN_PROGRESS`. It was read as non-authoritative context.

## Active snapshot and handoff evidence (Check 10)

`_ScopeChange/_LATEST.md` resolves uniquely to `SCA-004_2026-08-02_2325/`.
That snapshot contains the SOFTWARE core artifact set:

- `Brief`
- `Impact_Assessment`
- `Propagation_Plan`
- `Amendment_Actions.csv`
- `Pre_Change_Coverage.json` and `Post_Change_Coverage.json`
- `Decision_Log`
- `Handoff_State`
- `RUN_SUMMARY`
- the cumulative header-only `Supersession_Map.csv`
- `Amendment_Preview` and the Gate 2–4 records

Both `RUN_SUMMARY.md` and `Handoff_State.md` expose all seven fixed state
fields, and neither claims more than the evidence supports
(`ReadyForNextPhase = NO`, `DerivativePackageState = INCOMPLETE`). Every hash
they cite matches the live bytes:

- the decomposition, ledger and deliverables
- `ContextBudgetQA.csv` and `Companion_Inventory.csv`
- `DEL-01-06/_CONTEXT.md` (`24f357cc…94b2`)
- the pre- and post-change coverage files (`183c6d94…2813`, `0d3ec0a8…d9ec`)
- the supersession map

`_Decomposition/_LATEST.md` and `_Evaluation/DecompCoverage/_LATEST.md` are
consistent with it.

- **COV-071 (INFO):** both pointers still state
  `MetadataAlignmentState NOT_STARTED` and list 63 contexts and 64 references
  as stale. However,
  `_Coordination/PROJECT_SETUP_SCA004_METADATA_ALIGNMENT_2026-08-03/HANDOFF_STATE.md`
  records 64/64 current, and the live provenance agrees. The pointers are
  stale-conservative, not cleaner than the evidence. Refreshing them is a
  candidate SCA-005 handoff item. The pointer's audit citation (1 warning) is
  also as of SCA-004 closure. The current count is 3, caused by lifecycle
  changes after closure, not by decomposition drift.
- **COV-072 (INFO):** `_ScopeChange/SCA-005_2026-09-23_2139/` exists and was
  empty at scan time. It is the non-active candidate write target that D-PEC-86
  §4 opens, and the pointer does not name it.

## Informational delta against `COV_SCA004_POSTCHANGE_2026-08-03_1442`

- Decomposition package: the SHA-256 of `SOFTWARE_DECOMP.md`,
  `ScopeLedger.csv`, `Deliverables.csv`, `ContextBudgetQA.csv` and
  `Companion_Inventory.csv` are all identical to the SCA-004 postimage. There
  is no structural, mapping or topology change.
- New warnings: COV-004 (`DEL-01-03`) and COV-006 (`DEL-01-05`) moved from
  INFO to WARNING only because their lifecycle moved to `IN_PROGRESS`. There is
  no new blocker.
- INFO stays at 69. Check-6 INFO fell from 60 to 58, check-7 INFO is
  unchanged at 9, and check-10 INFO rose from 0 to 2.
- Lifecycle moved from 28/32/4 (INITIALIZED/OPEN/CHECKING) to 26/32/4 plus
  2 `IN_PROGRESS`. Contracts are unchanged at 32 `SOW_V1` / 32 `NONE`.
- Context provenance repinned to revision 1.4 in 64/64 (it was 1/64 at
  SCA-004 closure). The strict register validator now reports 255 dependency
  rows, up from 254, because of the `DEL-01-06` SOW-077 anchor. There are zero
  findings.
- Labeling clarification: the SCA-004 post-change QA called 20/12/12/11/7/9
  "scope-item counts". Those are in fact supporting-deliverable counts, except
  OBJ-004's 11. The exact counts are in the table above, and both sets agree
  with §3.
- The untracked `DEL-01-03/_run_records/REMAINING_EVIDENCE_DEL-01-03-REM-00{1,2,3}/`
  folders (D-PEC-86 I-4 in-flight output) were observed. They were not counted
  as anticipated artifacts, and they do not change `_STATUS.md`.

## What to fix for a cleaner rerun

1. The three Check-6 warnings clear only if artifact-location practice or the
   audit's folder-local rule changes (for example, a deliverable-local
   artifact manifest that points to the v2 source paths), or if lifecycle
   moves. That is out of scope for this audit, and no repair is implied.
2. Refresh the pointer handoff fields (COV-071) within an authorized SCA-005
   or PEC-maintenance act.
3. The nine unmapped deliverables (COV-062..070) remain an owner row-by-row
   selection at SCA-005 checkpoint 2.

## Findings and next action

No blocker or structural-coverage defect was found. SCOPE_CHANGE may consume
this immutable snapshot as the SCA-005 checkpoint-group-1 pre-change baseline
and record the three warnings accurately. This derivative evidence does not
accept checkpoint 1 or authorize any amendment. The audit pointer remains
unchanged because the sealed brief overrides the pointer-update step.
