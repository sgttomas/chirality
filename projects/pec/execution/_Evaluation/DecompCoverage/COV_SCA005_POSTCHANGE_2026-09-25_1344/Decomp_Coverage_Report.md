# Decomposition Coverage Report — SCA-005 post-change

| Field | Value |
|---|---|
| Variant | `SOFTWARE` |
| Decomposition | revision **1.5**, `candidate_pending_checkpoint_3` (SHA-256 `37ea1084a8219943a69057be377646c69a609a76728241963045d7cfb015a6cc`) |
| Scope | `ALL` |
| Status | **`BLOCKERS`** (2 blockers / 6 warnings / 74 info) |
| Closure readiness | **`FAIL`**, method-literal |
| Excluding expected consequences | `WARN` |
| Defects | 1, a `WARNING` |

**Expected source.** The SCA-005 candidate revision 1.5, applied under the
owner's checkpoint-group-2 acceptance of 2026-09-25
(`_ScopeChange/checkpoint_snapshots/SCA-005_GROUP-2_2026-09-25/DECISION.md`,
register row D-PEC-92) with Lane A4 deferred. The candidate SCA snapshot is
`_ScopeChange/SCA-005_2026-09-23_2139/`.

**Expected phase.** SCA-005 checkpoint-3 post-change validation, before any
pointer moves. The live decomposition equals the accepted CP2 postimage
(`dc2b8479…9660`) except for the two pre-acceptance front-matter lines. All
four registers and PRD v2.3 equal their accepted postimages byte-for-byte.

| # | Check | Verdict |
|---|---|---|
| 1 | Forward packages | `PASS`: 11/11 |
| 2 | Forward deliverables | `BLOCKER` ×2. 64/66 folders found. DEL-02-08 and DEL-02-09 are absent, an `EXPECTED_CONSEQUENCE` of the A4 deferral |
| 3 | Reverse coverage | `PASS`: no reverse-only package or deliverable folder. The four retired folders are declared rows |
| 4 | ID consistency | `PASS`: every folder ID and parent package equals the declared value |
| 5 | Context fidelity | `PASS`: 64/64 `_CONTEXT.md` match `Deliverables.csv`, including `ContextEnvelope` and the retired-row rendering |
| 6 | Artifact presence / contract shape | `WARNING` ×3 (`PRE-EXISTING`) and `INFO` ×58. 3 anticipated sets found. 32 `SOW_V1`, 32 `NONE`, 0 ambiguous |
| 7 | Objective mapping | `PASS` for all six objectives. `INFO` ×6: 4 retired rows by design, and 2 objectives each with 2 folderless supporters |
| 8 | Ledger integrity | `WARNING` ×2 (`EXPECTED_CONSEQUENCE`). 96 rows (`70 IN / 18 OUT / 8 TBD`). Every `IN` reference resolves to a declared unit, but SOW-095 and SOW-096 point to folderless units |
| 9 | Derivative parity | `SKIPPED`: not owned by the SOFTWARE variant |
| 9b | Package-shape conformance | `PASS`: companion inventory present and consistent, roles explicit, duplication justified (DL-15) |
| 10 | Active snapshot / handoff state | `WARNING` ×1 (`DEFECT`: the "40" stale-context count) and `INFO` ×10. SCA-004 remains the unique, complete, honest active snapshot |
| 11 | Lifecycle distribution | `PASS`: 26 `INITIALIZED`, 28 `OPEN`, 4 `CHECKING`, 2 `IN_PROGRESS`, 4 `RETIRED`. No unrecognized state |

## How to read the verdict

`overall_status = BLOCKERS` and `closure_readiness = FAIL` follow the
contract's count rule. Both blockers are Check-2 absences of the DEL-02-08 and
DEL-02-09 folders. The owner deferred Lane A4, so these folders do not exist
yet. The group-2 decision records that any audit finding stemming only from
those absent folders "is reported as a consequence of this decision, not
repaired". Full closure between the decomposition and the filesystem cannot
be reached until PROJECT_SETUP creates the folders under its own packet.

With `EXPECTED_CONSEQUENCE` findings set aside, the run has 0 blockers and 4
warnings: 3 `PRE-EXISTING` Check-6 artifact-location warnings and 1
`DEFECT`, the documentary count error COV-072. It would read `WARN`
(`Decision_Log.md` D-4, D-5).

## Coverage and context evidence

The run matched the declared packages and deliverables against the
filesystem:

- **Packages.** All 11 declared packages (§4, lines 378–388) have exact
  folders.
- **Deliverables.** Of the 66 declared deliverables (§5 compact tables;
  `Deliverables.csv` rows 2–67), 64 have exact folders under
  `projects/pec/execution/PKG-*/1_Working/`: 60 active and 4 retired.
- **Missing folders.**
  - COV-001: DEL-02-08, Work-graph parser (`Deliverables.csv` line 18).
  - COV-002: DEL-02-09, MEMORY run-index parser (line 19).
  - No `PKG-02_*/1_Working/DEL-02-0{8,9}_*` folder exists.
- **Reverse coverage.** No undeclared folder exists.
- **Register parity.** The §5 compact view matches `Deliverables.csv` for
  66/66 rows. `ContextBudgetQA.csv` matches for 66/66.
- **Context fidelity.** Every present `_CONTEXT.md` agrees with its register
  row on every compared field.

## Retired-row representation (plan C4 requirement)

The plan asked this audit to confirm that the retired-row representation
raises no blocker. That is confirmed on the real files: the four retired
deliverables (DEL-06-04, DEL-07-02, DEL-07-04, DEL-07-05) raise no `BLOCKER`
and no `WARNING`.

**How they are represented:**

- Their register rows stay in place with the `[RETIRED — SCA-005]`
  description prefix and blank coverage and objective cells.
- §5 marks them `— [RETIRED — SCA-005] (was SOW-0xx)`.
- `ContextBudgetQA.csv` marks them in RecommendedAction.
- Their `_CONTEXT.md` renders `(none — retired under SCA-005)`.
- Their `_STATUS.md` reads `RETIRED`, at the planned A3 postimage hashes.
- Their folders and all files are retained.

**How each check treats them:**

| Check | Result for the retired rows |
|---|---|
| 3 | No warning, because they are declared |
| 4 | PASS |
| 5 | MATCH, per D-7 |
| 6 | INFO, carried from PRECHANGE with the reason changed and not escalated (D-8) |
| 7 | INFO (COV-064..067). The `RETIRED`-only `BLOCKER` cannot fire, because no objective lists a retired supporter |
| 8 | No `IN` row references a retired deliverable. The four scope items (SOW-029, 035, 037, 087) are OUT with no mapping |
| 11 | `RETIRED` is a recognized state |

**Closure tool.** The plan's expected "isolated-node warnings for the four
retired DELs from the closure tool" do not appear yet. The retired registers
still hold ACTIVE edges because B3 is not opened (COV-080). They are a
post-B3 expectation.

## Objective evidence (Check 7)

Objectives resolve from the `ScopeLedger.csv` `ObjectiveIDs` column. There
are six: OBJ-001..OBJ-006.

| Objective | IN scope items (ledger) | Supporting deliverables | Folder-backed |
|---|---|---|---|
| OBJ-001 | 27 | 25 | 23 |
| OBJ-002 | 14 | 14 | 12 |
| OBJ-003 | 16 | 14 | 14 |
| OBJ-004 | 13 | 11 | 11 |
| OBJ-005 | 9 | 7 | 7 |
| OBJ-006 | 9 | 9 | 9 |

For every objective, the ledger scope-item set, the `SupportsObjectives`
set, the ledger-reached deliverable set and the §3 objective-side view (lines
335–340, with ranges and instruments expanded) are equal.

The residue from revision 1.4 is fully closed. Its 11 unmapped `IN` rows and
9 unmapped deliverables are now 0 and 0, matching §7 "IN items without
objective mapping 0". The owner's TM-PEC-023 selections and amendment 2 are
reflected exactly. No objective depends only on retired units.

OBJ-001 and OBJ-002 each have two declared supporters without folders,
DEL-02-08 and DEL-02-09 (COV-068, COV-069, `INFO`). The zero-support warning
does not fire.

## Artifact and lifecycle evidence (Checks 6 and 11)

Deliverable-local matching found three anticipated sets, unchanged from
PRECHANGE: DEL-00-01 (ADRs), DEL-00-03 (SPEC) and DEL-10-01 (baseline
method and baseline).

Three absences are warnings. They are unchanged from PRECHANGE and
`PRE-EXISTING`:

| Issue | DEL | State | Artifact location |
|---|---|---|---|
| COV-006 | DEL-01-03 | `IN_PROGRESS` | D-PEC-85 candidate bytes under `projects/pec/v2/` |
| COV-008 | DEL-01-05 | `IN_PROGRESS` | bytes under `projects/pec/v2/` |
| COV-042 | DEL-08-02 | `CHECKING` | unchanged since SCA-004 |

The other 58 absences are `INFO`: 54 at `OPEN`/`INITIALIZED` and 4 at
`RETIRED`.

Lifecycle moved from PRECHANGE only through the four A3 retirements (`OPEN`
32 → 28, `RETIRED` 0 → 4). No other `_STATUS.md` changed.

## Active snapshot and handoff evidence (Check 10)

`_ScopeChange/_LATEST.md` (`721a14dc…6280`) still resolves uniquely to
`SCA-004_2026-08-02_2325/`. That snapshot is byte-unchanged and complete, and
it claims no more than its evidence (`ReadyForNextPhase = NO`). Check 10
therefore passes on the active snapshot. The warning and the informational
findings are:

- **COV-072 (`WARNING`, `DEFECT`).** The accepted `Propagation_Plan.md` (L45,
  L802 B1, L904) and this run's brief say "40 other `_CONTEXT.md`". The real
  stale population is **42**: 64 folders minus the 22 A2 mirrors, confirmed
  by census. The likely slip is 62 active rows minus 22, but the 22 include
  the four retired folders and the 62 include the two folderless rows. B1's
  rule, "not written in A2", still selects all 42. Correct the count in the
  SCA-005 `Handoff_State.md`/`RUN_SUMMARY.md` and in any count-based B1
  acceptance check.
- **COV-073 (`INFO`, `EXPECTED_CONSEQUENCE`).** The pointers still name
  revision 1.4 and SCA-004. The hashes they and SCA-004 cite no longer equal
  the working-tree bytes. Those hashes are exactly recoverable at
  `2b0572fe0`. A6 moves the pointers only after acceptance.
- **COV-074 (`INFO`, `PRE-EXISTING`).** This is PRECHANGE's COV-071,
  unchanged: the pointer metadata fields understate the repairs made on
  2026-08-03 and 2026-08-09.
- **COV-075 (`INFO`, `EXPECTED_CONSEQUENCE`).** The SCA-005 snapshot is
  mid-A5:
  - `Supersession_Map.csv` is present (29 rows).
  - `Post_Change_Coverage.json` and `RUN_SUMMARY.md` are absent until this
    audit returns.
  - The `Handoff_State.md` heading still reads "Checkpoint-group-1".
  - It is not active and claims nothing cleaner than the evidence.
- **COV-076 (`INFO`, `EXPECTED_CONSEQUENCE`, flagged).** The 22 A2 mirrors
  already say "revision 1.5 (`current_basis`, SCA-005 successor)" before
  checkpoint 3 is accepted. These are the accepted exact postimages, but the
  claim is anticipatory. If checkpoint 3 is refused, the rollback must revert
  these lines too (D-12).
- **COV-077 / COV-078 / COV-082 (`INFO`, `EXPECTED_CONSEQUENCE`).** B1 and B4
  are open, so the following are unchanged:
  - 42 contexts and 64 reference packets still name revision 1.4.
  - 32 SOWs are byte-unchanged.
- **COV-079 / COV-080 / COV-081 (`INFO`, `EXPECTED_CONSEQUENCE`).** B3 is
  unopened, so the pre-B3 dependency state persists:
  - `DEP-09-05-005` still runs from active DEL-09-05 to retired DEL-06-04.
  - The retired registers still hold 18 ACTIVE rows.
  - 119 execution edges, 0 SCCs, isolated DEL-00-03 and DEL-01-05.
  - The validator reports 0 errors and the 2 DRB-008 warnings.

## Package shape (Check 9b)

The main document carries a `Companion Inventory` section, mirrored exactly
by `Companion_Inventory.csv` (six files). Authoritative and derived roles are
labelled. The §2/§5 duplication of register fields is declared and justified
(DL-15), and §7 states register counts that agree with the registers. No
derived publication artifact is treated as authoritative.

## Comparison with `COV_SCA005_PRECHANGE_2026-09-23_2139`

The full comparison is in `PrePost_Comparison.md`. Headlines:

- **Topology.** 94 → 96 scope items; 64 → 66 deliverable rows (62 active /
  4 retired); 11 packages and 6 objectives unchanged.
- **Forward deliverable coverage.** 100 → 96.97%.
- **Unmapped residue.** Unmapped `IN` rows 11 → 0. Unmapped active
  deliverables 9 → 0.
- **Issues.** 0/3/69 → 2/6/74.
- **Per-finding delta.** 62 carried, 6 resolved, 4 changed, 16 new. Of the
  new findings, 15 are expected consequences and 1 is a defect.

No regression is attributable to a defect in the amendment's decomposition
truth.

## What to fix for a cleaner rerun

1. **A4 and B3** (PROJECT_SETUP and dependency-extract, under their own
   packets). Creating the DEL-02-08/09 folders clears COV-001, COV-002,
   COV-068..071 and COV-081. B3 clears COV-079/080 and produces the planned
   isolated-node result for the retired DELs.
2. **B1 re-pin.** Clears COV-077 and COV-078. Before that, correct the "40"
   count to 42 (COV-072).
3. **A6 after the owner's checkpoint-3 acceptance.** Clears COV-073 and
   COV-074, and makes COV-076's claim true.
4. **A5 completion.** Clears COV-075.
5. **The three Check-6 warnings.** These clear only if artifact-location
   practice or lifecycle changes. They are unrelated to SCA-005.

## Findings and next action

The SCA-005 decomposition truth passes every structural check the method owns:

- declared packages and folders
- ID consistency
- context fidelity (64/64)
- objective evidence, internally consistent, with 0 unmapped `IN` rows and 0
  unmapped active deliverables
- ledger reciprocity and the union rule
- §7 telemetry parity
- package shape
- lifecycle

The two blockers and two Check-8 warnings stem only from the owner-deferred
A4 folders. The one defect is a documentary count in the accepted plan and
brief.

SCOPE_CHANGE may copy this `coverage_summary.json` into
`Post_Change_Coverage.json` (A5) and present the audited poststate at
checkpoint 3. Every finding and its classification should be stated as
recorded here. This derivative evidence accepts nothing and authorizes
nothing. The audit `_LATEST.md` pointer is unchanged.
