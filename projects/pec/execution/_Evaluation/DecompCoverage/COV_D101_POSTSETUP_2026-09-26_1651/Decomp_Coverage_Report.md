# Decomposition Coverage Report — D-PEC-101 post-setup re-audit (add-on V)

| Field | Value |
|---|---|
| Variant | `SOFTWARE` |
| Decomposition | revision **1.6**, `status: current_basis`, SHA-256 `9374c21fb87b02e5f842af9407caf65690d73f3067f86ce6c7dba0a3a7908eb1` |
| Audited tree | worktree `pec-d101-act`, HEAD `43b60687b` on `claude/pec-d101-act`; product bytes unchanged since the K4 commit `62230fa46` (only run-root files changed after it) |
| Scope | `ALL` |
| Status | **`WARNINGS`** (0 blockers / 3 warnings / 73 info; 2 expected consequences, counted separately) |
| Closure readiness | **`WARN`**, method-literal from the counts |
| Method edition | `audit-decomp` WORKFLOW `7ba6291c…246b`, contract `704929c7…4e75`, method `51a0c69b…8308827` |

**Expected source.** Revision 1.6 `current_basis` with SCA-006 closed for
scope change only (`_ScopeChange/_LATEST.md` names the active snapshot
`SCA-006_2026-09-25_1912/`), plus the D-PEC-101 poststate: Part K1 (two new
folders, 22 added rows, 2 refreshed quotes) and Part K4 with add-on C (63
context and 66 reference re-pins, two covers bullets), applied and verified
(run root `_Coordination/REV16_CURRENCY_SETUP_D101_2026-09-26/`,
`VERIFIER_VERDICT_01.md` PASS WITH NOTES). This run independently confirmed
that all 161 granted product paths equal the proposal's tabled postimages
(the add-on C column where it differs) (`QA_Report.md` command 14).

**Expected phase.** Post-setup re-audit before publication. The
`_Evaluation/DecompCoverage/_LATEST.md` decision belongs to the invoking
manager; this run did not touch it.

| # | Check | Verdict |
|---|---|---|
| 1 | Forward packages | `PASS`: 11/11. `INFO` ×2 from the structure tool (package SHOULD-subfolders; absent tool roots), pre-existing |
| 2 | Forward deliverables | `PASS`: **68/68** declared deliverables have folders (was 66/68). No finding |
| 3 | Reverse coverage | `PASS`: no undeclared package or deliverable folder |
| 4 | ID consistency | `PASS`: every folder ID and parent package equals the declared value, including the two new folders |
| 5 | Context fidelity | `PASS`: 68/68 `_CONTEXT.md` match `Deliverables.csv` on every compared field, including `ContextEnvelope`, the three A2 mirrors and the two new contexts |
| 6 | Artifact presence / contract shape | `WARNING` ×3 (pre-existing, unchanged) and `INFO` ×62. 3 anticipated sets found. 34 `SOW_V1`, 34 `NONE`, 0 ambiguous |
| 7 | Objective mapping | `PASS` for all six objectives; OBJ-001's 27 supporters are all folder-backed. `INFO` ×4: the retired rows by design |
| 8 | Ledger integrity | `PASS`: 100 rows (`74 IN / 18 OUT / 8 TBD`); all 74 IN rows resolve to packages and to declared, non-retired, folder-backed deliverables. `INFO` ×1: 26 XRG-013 (D-GOV-48 package home for OUT/TBD rows), newly measured, owner-deferred |
| 9 | Derivative parity | `SKIPPED`: not owned by the SOFTWARE variant. Other derivative-currency observations: `INFO` ×3, `EXPECTED_CONSEQUENCE` ×1 |
| 9b | Package-shape conformance | `PASS`: companion inventory present and mirrored by `Companion_Inventory.csv`; roles explicit; duplication justified (DL-15); §7 telemetry equals the registers |
| 10 | Active snapshot / handoff state | `PASS`: `_ScopeChange/_LATEST.md` names exactly one complete active snapshot (SCA-006); no handoff surface claims a later phase or cleaner closure than the evidence. `EXPECTED_CONSEQUENCE` ×1 (surfaces understate the D-PEC-101 poststate), `INFO` ×1 (edition drift) |
| 11 | Lifecycle distribution | `PASS`: 28 `INITIALIZED`, 30 `OPEN`, 4 `CHECKING`, 2 `IN_PROGRESS`, 4 `RETIRED` (68 folders); no unrecognized state |

## How to read the verdict

`overall_status = WARNINGS` and `closure_readiness = WARN` follow the count
rule: 0 blockers and 3 warnings. The three warnings are the pre-existing
Check-6 artifact-location findings (DEL-01-03 COV-006, DEL-01-05 COV-008,
DEL-08-02 COV-044), carried with identical text from the prior run's COV-008,
COV-010 and COV-046 and unrelated to D-PEC-101. The two
`EXPECTED_CONSEQUENCE` findings cite `D-PEC-101`; the contract excludes them
from the verdict. Without that classification each would be a WARNING and the
verdict would still be `WARNINGS` / `WARN`. `closure_readiness` is the
method's three-way verdict only; it is not a lifecycle, readiness,
acceptance or reliance judgement.

## The D-PEC-101 prediction, tested

| Prediction (brief) | Observed | Result |
|---|---|---|
| Prior COV-003/004/073/074 (two absent folders) resolved | Both folders exist with the six-file set (`_STATUS.md` `OPEN`, stamped `TASK+preparation`); structure tool 68/68 PASS; strict validator 0 DRB-008; SOW-099 and SOW-100 resolve to folders | Confirmed |
| COV-075/076 (two stale quotes) resolved | DEP-09-06-003 and DEP-10-03-003 carry the whole revision-1.6 DEL-08-01 cell, verbatim; 127/127 ACTIVE EXECUTION quotes verbatim | Confirmed |
| COV-080 (no register traced SOW-097..100) resolved | DEP-04-03-005, DEP-08-03-005, DEP-08-06-002 and DEP-10-13-002 trace SOW-097..100; 74/74 IN items are traced by an ACTIVE `TRACES_TO_REQUIREMENT` row in every deliverable they name; 138/138 ACTIVE anchor assertions true | Confirmed |
| With K4, COV-077/078 (revision 1.5 re-pin) resolved | 68/68 context provenance blocks end at revision 1.6 (`current_basis`, SCA-006 successor); 68/68 reference packets name revision 1.6 and PRD v2.4, none 1.5 or v2.3; every active covers bullet equals its register cell (add-on C) | Confirmed |
| Forward production-unit coverage 100 % (68/68) | 68/68 | Confirmed |
| Three pre-existing Check-6 warnings unchanged | Same three, identical text | Confirmed |
| 0 BLOCKER | 0 | Confirmed |

**Beyond the prediction.** The prior run's other expected consequences also
resolved, but not through D-PEC-101: COV-079 (anticipatory A2 tails) and
COV-084 (pre-acceptance pointers) through the SCA-006 checkpoint-3 acceptance
and its A6 pointer moves, COV-085 (mid-A5 snapshot) through A5 completion.
COV-086 (SCA-005 residual) is resolved because SCA-005 is now the historical
predecessor. Two new `EXPECTED_CONSEQUENCE` findings and two new INFO findings
appear (next sections).

## Expected consequences (`EXPECTED_CONSEQUENCE`)

| Issue | Check | Entity | Would otherwise be | Evidence | Decision |
|---|---|---|---|---|---|
| COV-076 | 9 | `_COORDINATION.md` Notes (human-owned) L225–227 | WARNING | Still "revision 1.5 is `current_basis` since SCA-005 …"; file `95ebe344…8a90c`, the ruling's preimage | `D-PEC-101` ruling question 4 (a): HELP_HUMAN replaces the lines with the with-K1 text in the act's PR after the verifier passes K1; not yet in the audited tree |
| COV-077 | 10 | `_Decomposition/_LATEST.md`, `_ScopeChange/_LATEST.md`, SCA-006 snapshot | WARNING | `_Decomposition/_LATEST.md:35` "no folders yet; SCA-006 Lane B1"; lines 53–55 list B1, B2, B3, B7 open; `_ScopeChange/_LATEST.md:15-19` Lane B open, B7 re-pin open, audit `COV_SCA006_POSTCHANGE`; SCA-006 `RUN_SUMMARY.md` §6–§7 the same | `D-PEC-101` Administrative grant: both pointers and the SCA-006 folder are "Records not opened"; the Lane B closeout goes to the run root's `HANDOFF_STATE.md`, which does not yet exist |

Both surfaces understate the evidence; neither claims a later phase or cleaner
closure. COV-077 is why Check 10 still passes.

## Findings about the D-PEC-101 bytes

No `DEFECT` was found in the D-PEC-101 bytes. Observed:

- **Byte identity.** All 161 granted paths equal the proposal's postimages
  (K4 129 with the add-on C values for DEL-04-03 and DEL-08-03 references; K1
  20 modified and 12 created). The branch's product diff against its merge base
  `f392294b5` is exactly those 161 paths (63 + 66 + 16 + 4 modified, 12
  created), plus the run root and the K14A brief copy.
- **Registers.** 68 registers, 285 rows (ANCHOR 146: 138 ACTIVE / 8 RETIRED;
  EXECUTION 139: 127 ACTIVE / 12 RETIRED). Strict validator: 0 ERROR, 26
  WARNING, all XRG-013, 0 DRB-008 (exit 1 by design of `--strict`). No
  duplicate `DependencyID`, `EdgeID` or source–target pair. E-P83 unused;
  E-P84..E-P99 each mentioned exactly twice.
- **Mirrors.** Every one of the 127 ACTIVE EXECUTION edges appears once as a
  `| … | E |` row in its source's `_DEPENDENCIES.md` and once as a `[E]`
  bullet in its target's. The two new `_DEPENDENCIES.md` use the D-GOV-46
  heading schema, as the ruling states; the 66 others keep legacy headings.
- **Closure.** 127 edges, 68 nodes, 0 SCCs, 0 bidirectional pairs, 0 orphans,
  0 declared disagreements, `declared_only_rows` 127, `declared_unread_count`
  136, isolated exactly the six named, hub DEL-03-01 only (25).
  `closure_summary.json` is byte-identical to the run root's.
- **New contexts.** Every compared field equals the revision-1.6
  `Deliverables.csv` row. The two new `_REFERENCES.md` name the absent
  `<package>/0_References/` staging path, as all 66 others do (COV-001).

## Coverage and context evidence

- **Packages.** All 11 declared packages (§4) have exact folders, each
  containing only `1_Working/`. §4 "Assigned (count)" equals the ledger's
  per-package IN counts for 11/11 (3/8/9/7/7/3/6/3/8/7/13).
- **Deliverables.** 68 declared rows (64 active, 4 retired); 68 folders. The
  §5 compact view and `ContextBudgetQA.csv` match `Deliverables.csv` for 68/68
  rows; the four retired rows are marked in both.
- **Reverse coverage.** No undeclared folder and no non-`DEL` entry exists.
- **Context fidelity.** 68/68 match on DeliverableID, name, package, type,
  `ContextEnvelope`, `PhaseHint`, covered items, objectives, responsible
  party, description, anticipated artifacts and envelope notes.

## Objective evidence (Check 7)

| Objective | IN scope items (ledger) | Supporting deliverables | Folder-backed |
|---|---|---|---|
| OBJ-001 | 31 | 27 | 27 |
| OBJ-002 | 15 | 14 | 14 |
| OBJ-003 | 16 | 14 | 14 |
| OBJ-004 | 13 | 11 | 11 |
| OBJ-005 | 9 | 7 | 7 |
| OBJ-006 | 9 | 9 | 9 |

For every objective, four sets are equal: the ledger IN set, the
`SupportsObjectives` set, the ledger-reached deliverables and the §3
objective-side view. No IN row lacks an objective; no active deliverable lacks
one. The union rule holds on all 64 active rows; reciprocity holds on 68/68.
The four retired deliverables support no objective by design (COV-068 to
COV-071, `INFO`).

## Check 6 (artifact presence and contract shape)

Only DEL-00-01 (`artifacts/v2/ADRs.md`), DEL-00-03 (`artifacts/v2/SPEC.md`)
and DEL-10-01 (two `STEP0_COST_BASELINE*` files) hold deliverable-local
artifacts. Of the 65 absences, three are WARNING because the deliverable is at
`IN_PROGRESS` or `CHECKING` (DEL-01-03, DEL-01-05, DEL-08-02; their bytes live
under `projects/pec/v2/`, outside this folder-local match); 62 are INFO. The
two new folders are INFO (`OPEN`, contract `NONE`). DEL-02-08 and DEL-02-09
are now `INITIALIZED` with `SOW_V1` contracts (D-PEC-98). DEL-01-06's INFO row
now notes the D-PEC-96 registry-v2 source bytes outside its folder. Contracts:
34 `SOW_V1` (all valid per `audit_structure.py`), 34 `NONE` (30 `OPEN` + 4
`RETIRED`), no legacy, dual or invalid contract.

## Check 8 (ledger integrity) and XRG-013

The method's Check 8 reads IN rows and passes. The current strict validator
(`869df1d5…57ee`, carrying Root D-GOV-48 since the prior run) also reports 26
XRG-013 warnings: every OUT and TBD ledger row has a blank `PackageID`. They
are the same 26 IDs at revision 1.5 and 1.6, revision 1.6 keeps the edition it
adopted, and the owner defers action (`NOTICE_2026-09-26_PACKAGE_HOME_D-GOV-48.md`;
D-PEC-101 Limits). Recorded as COV-072 `INFO`.

## Other derivative-currency observations (Check 9)

| Issue | Severity | Observation |
|---|---|---|
| COV-073 | INFO | 34 `SOW_V1` contracts: the prior run's 32 byte-unchanged, 2 new (D-PEC-98). SCA-005 and SCA-006 §B4 currency work remains open; SOW text not audited |
| COV-074 | INFO | Closure tool `isolated_units` WARNING: the same six isolated units at 127 edges / 68 nodes; no cycle possible from the 16 new edges |
| COV-075 | INFO | Revision 1.6 still says PEC's row "declares the `remaining-loop` profile now" and lists `remaining-loop` in §9. D-PEC-96 has since been ruled and applied; live `loops.json` declares `shared-dev-loop` live and two historical profiles. The owner carried the text knowingly at checkpoint 3 (Q-CP3-1 (a)) for a later scope change |
| COV-076 | EXPECTED_CONSEQUENCE | `_COORDINATION.md` Notes line (above) |

## Active snapshot and handoff state (Check 10)

`_ScopeChange/_LATEST.md` names exactly one active snapshot. SCA-006 is
present and complete for its bound contract edition; its
`Post_Change_Coverage.json` is byte-identical to the prior run's
`coverage_summary.json`. It omits `AdjustedAuditState`, a field the current
scope-change contract added after SCA-006 bound its edition (COV-078 `INFO`).
The pointers and the snapshot's state fields understate the D-PEC-101
poststate (COV-077 `EXPECTED_CONSEQUENCE`). The SCA-005 snapshot is now the
historical predecessor. It is complete, so the prior COV-086 is resolved.

## Comparison with the prior run

| Metric | `COV_SCA006_POSTCHANGE_2026-09-26_0051` | This run |
|---|---|---|
| Forward deliverable coverage | 97.06 % (66/68) | **100 % (68/68)** |
| Context fidelity | 100 % (66/66) | 100 % (68/68) |
| Context provenance at revision 1.6 | 3 | 68 |
| References at revision 1.6 / PRD v2.4 | 0 | 68 |
| Registers / rows | 66 / 263 | 68 / 285 |
| ACTIVE EXECUTION quotes verbatim | 109/111 | 127/127 |
| IN items fully traced | 70/74 | 74/74 |
| Strict validator | 0 ERROR; 2 DRB-008 (tool `a1544dc4…`) | 0 ERROR; 0 DRB-008; 26 XRG-013 (tool `869df1d5…`, D-GOV-48) |
| Closure edges / nodes / isolated | 111 / 66 / 6 | 127 / 68 / 6 (same six) |
| Lifecycle (folders) | 26 I / 30 O / 4 C / 2 IP / 4 R (66) | 28 I / 30 O / 4 C / 2 IP / 4 R (68) |
| Issues (B / W / I / EC) | 0 / 3 / 71 / 12 | 0 / 3 / 73 / 2 |

Per-finding delta (`PrePost_Comparison.md`): 64 carried, 8 changed, 14
resolved, 6 new. There is no new BLOCKER or WARNING. The methodology is the
same edition as the prior run. Two tools changed bytes (validator, closure),
which is disclosed in `Decision_Log.md` D-12.

## What to fix for a cleaner rerun

These are observations for the manager and owner, not authorizations.

- COV-076: apply the authorized `_COORDINATION.md` Notes-line replacement
  (D-PEC-101 question 4 (a)).
- COV-077: write the run root's `HANDOFF_STATE.md` recording the Lane B1, B2,
  B3 and B7 closeout (D-PEC-101 Administrative grant). The two `_LATEST.md`
  pointers can change only under a later packet that opens them.
- COV-075: the `remaining-loop` text awaits the later PEC scope change the
  owner routed it to.
- COV-072: the D-GOV-48 package homes await the owner's adoption decision.
- The three Check-6 warnings clear only when artifacts are recorded where this
  folder-local audit can see them, or when the method is given the v2 source
  locations. Neither is in scope here.

This snapshot is derivative evidence. It accepts nothing, authorizes nothing
and changes no governed state. It makes no lifecycle, CHECKING, ISSUED,
acceptance, readiness or reliance claim.
