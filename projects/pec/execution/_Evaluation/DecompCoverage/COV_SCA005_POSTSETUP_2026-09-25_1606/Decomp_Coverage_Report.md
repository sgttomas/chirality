# Decomposition Coverage Report — D-PEC-93 post-setup re-audit

| Field | Value |
|---|---|
| Variant | `SOFTWARE` |
| Decomposition | revision **1.5**, `current_basis` (SHA-256 `dc2b84791454ac888e692bfa507221f5d4a588c63bb8ab5005cc00343b119660`) |
| Audited tree | commit `995af4f36` (D-PEC-93 option-A act on `origin/main` `04e04da00`) |
| Scope | `ALL` |
| Status | **`WARNINGS`** (0 blockers / 3 warnings / 70 info) |
| Closure readiness | **`WARN`**, method-literal from the counts |
| Defects | 0 |

**Expected source.** Decomposition revision 1.5 `current_basis`, SCA-005
closed for scope change only (`_ScopeChange/SCA-005_2026-09-23_2139/`,
`CLOSED_FOR_SCOPE_CHANGE_ONLY`), plus the D-PEC-93 poststate (commit
`995af4f368d0d8cc0b3134eef484b4b9618aa8ac`; run root
`_Coordination/PROJECT_SETUP_SCA005_A4_B3_2026-09-25/`). The live
decomposition and all four registers equal their accepted revision-1.5
values, and PRD v2.3 equals `fff27a66…fdc32`. All 31 D-PEC-93 product paths
equal the proposal's postimage table (option-A aggregate `c4525add…727a`
reproduced).

**Expected phase.** D-PEC-93 post-setup re-audit, after the product writes and
before publication. The `_Evaluation/DecompCoverage/_LATEST.md` decision
belongs to the WORKING_ITEMS manager; this run did not touch it.

| # | Check | Verdict |
|---|---|---|
| 1 | Forward packages | `PASS`: 11/11 |
| 2 | Forward deliverables | `PASS`: 66/66 folders found, including DEL-02-08 and DEL-02-09 |
| 3 | Reverse coverage | `PASS`: no reverse-only package or deliverable folder |
| 4 | ID consistency | `PASS`: every folder ID and parent package equals the declared value |
| 5 | Context fidelity | `PASS`: 66/66 `_CONTEXT.md` match `Deliverables.csv`, including `ContextEnvelope`, the retired-row rendering and the two new contexts |
| 6 | Artifact presence / contract shape | `WARNING` ×3 (`PRE-EXISTING`) and `INFO` ×60. 3 anticipated sets found. 32 `SOW_V1`, 34 `NONE`, 0 ambiguous |
| 7 | Objective mapping | `PASS` for all six objectives, every supporter folder-backed. `INFO` ×4: the retired rows, by design |
| 8 | Ledger integrity | `PASS`: 96 rows (`70 IN / 18 OUT / 8 TBD`); every `IN` reference resolves to a declared, folder-backed, non-retired unit |
| 9 | Derivative parity | `SKIPPED`: not owned by the SOFTWARE variant |
| 9b | Package-shape conformance | `PASS`: companion inventory present and consistent, roles explicit, duplication justified (DL-15) |
| 10 | Active snapshot / handoff state | `PASS` with `INFO` ×6. `_ScopeChange/_LATEST.md` names exactly one complete active snapshot, SCA-005; no handoff surface claims a cleaner state than the evidence |
| 11 | Lifecycle distribution | `PASS`: 26 `INITIALIZED`, 30 `OPEN`, 4 `CHECKING`, 2 `IN_PROGRESS`, 4 `RETIRED`. No unrecognized state |

## How to read the verdict

`overall_status = WARNINGS` and `closure_readiness = WARN` follow the
contract's count rule: 0 blockers and 3 warnings. The three warnings are the
`PRE-EXISTING` Check-6 artifact-location findings (DEL-01-03, DEL-01-05,
DEL-08-02), carried unchanged through PRECHANGE, POSTCHANGE and this run and
unrelated to SCA-005 and D-PEC-93. No finding is classified `DEFECT`.
`closure_readiness` is the method's three-way verdict only; it is not a
lifecycle, readiness or reliance judgement.

## Coverage and context evidence

- **Packages.** All 11 declared packages (§4) have exact folders, each
  containing only `1_Working/`.
- **Deliverables.** All 66 declared deliverables (§5 compact tables;
  `Deliverables.csv` rows 2–67) have exact folders: 62 active and 4 retired.
  The two new folders are
  `PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser/` and
  `…/DEL-02-09_MEMORY_run_index_parser/`, each with `_STATUS.md` (`OPEN`),
  `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md` (empty)
  and `Dependencies.csv`.
- **Reverse coverage.** No undeclared folder exists.
- **Register parity.** The §5 compact view and `ContextBudgetQA.csv` match
  `Deliverables.csv` for 66/66 rows.
- **Context fidelity.** Every `_CONTEXT.md` agrees with its register row on
  every compared field.

## Objective evidence (Check 7)

| Objective | IN scope items (ledger) | Supporting deliverables | Folder-backed |
|---|---|---|---|
| OBJ-001 | 27 | 25 | 25 |
| OBJ-002 | 14 | 14 | 14 |
| OBJ-003 | 16 | 14 | 14 |
| OBJ-004 | 13 | 11 | 11 |
| OBJ-005 | 9 | 7 | 7 |
| OBJ-006 | 9 | 9 | 9 |

For every objective the ledger scope-item set, the `SupportsObjectives` set,
the ledger-reached deliverable set and the §3 objective-side view are equal.
OBJ-001 and OBJ-002 now have every supporter folder-backed, so the prior
folderless-supporter INFO rows are cleared. The four retired deliverables
support no objective by design (COV-064..067, `INFO`,
`EXPECTED_CONSEQUENCE`: DL-20; CP2 Q-CP2-1 (a)).

## Ledger integrity (Check 8)

SOW-095 → DEL-02-08 and SOW-096 → DEL-02-09 now resolve to existing folders.
Every IN row resolves at both the declaration and the folder level, so the
prior Check-8 warnings are cleared.

## Artifact and lifecycle evidence (Checks 6 and 11)

The three deliverable-local anticipated sets are unchanged: DEL-00-01 (ADRs),
DEL-00-03 (SPEC) and DEL-10-01 (baseline method and baseline).

| Issue | DEL | State | Classification | Note |
|---|---|---|---|---|
| COV-004 | DEL-01-03 | `IN_PROGRESS` | `PRE-EXISTING` | D-PEC-85 candidate bytes under `projects/pec/v2/` |
| COV-006 | DEL-01-05 | `IN_PROGRESS` | `PRE-EXISTING` | bytes under `projects/pec/v2/` |
| COV-042 | DEL-08-02 | `CHECKING` | `PRE-EXISTING` | accepted source-tree bytes outside the folder |

The other 60 absences are `INFO`: 54 at `OPEN`/`INITIALIZED` (carried), 4 at
`RETIRED` (carried), and 2 new at `OPEN` for DEL-02-08 and DEL-02-09 (COV-015,
COV-016; `EXPECTED_CONSEQUENCE`: D-PEC-93 creates the folders at `OPEN` only
and grants no SOW or artifact write).

Lifecycle changed from the prior run only by the two new `OPEN` files
(`OPEN` 28 → 30). No other `_STATUS.md` changed; the diff since the prior
audited commit touches exactly the 31 D-PEC-93 product paths.

## Dependency evidence (supplementary; Check-10 derivative surfaces)

- **Strict register validator:** 66 registers, 263 rows (ANCHOR 140,
  EXECUTION 123), **0 errors / 0 warnings**, exit 0. The two DRB-008
  warnings are gone.
- **Closure tool:** 111 edges over 66 nodes, 0 SCCs, 0 bidirectional pairs,
  0 orphans. Isolated exactly DEL-00-03, DEL-01-05, DEL-06-04, DEL-07-02,
  DEL-07-04 and DEL-07-05 (COV-071, `INFO`, `EXPECTED_CONSEQUENCE`: plan §C4
  and the D-PEC-93 topology). Hub DEL-03-01 (degree 24 → 25; QA only).
- **Retirements:** 20 rows `RETIRED`; 0 ACTIVE rows remain in the retired
  registers; 0 ACTIVE rows target a retired deliverable (`DEP-09-05-005` is
  retired).
- **Mirrors:** every retired edge is struck wherever a mirror names it; no
  live edge is struck; E-P79..E-P82 are mirrored.
- **Evidence-quote currency (COV-072, `INFO`, `PRE-EXISTING`):** 19 ACTIVE
  EXECUTION rows in 10 registers cite a quote that is not verbatim in the
  cited file: `DEP-03-01-005`, `DEP-03-01-008`..`013`, `DEP-05-01-004`,
  `DEP-05-02-003`, `DEP-06-03-003`, `DEP-08-04-005`, `DEP-08-05-004`,
  `DEP-09-05-006`..`008`, `DEP-10-05-004`, `DEP-10-05-005`, `DEP-10-10-003`,
  `DEP-10-12-003`. This is exactly the set in D-PEC-93 finding 1. These rows
  and their evidence files are byte-identical to the prior audited state, so
  the condition predates the act and is not caused by it. The owner ruled it
  a carried residual (D-PEC-93 ruling, question 4). Every new or refreshed
  quote is verbatim. The 132 ACTIVE anchor rows use structured assertion
  quotes by convention and are all true against the registers.

## Active snapshot and handoff evidence (Check 10)

`_ScopeChange/_LATEST.md` (`a2b5b789…4268`) names exactly one snapshot,
`SCA-005_2026-09-23_2139/`, which exists and holds every C5 artifact.
`_Decomposition/_LATEST.md` names revision 1.5 `current_basis` with the live
hashes. Neither pointer, nor the snapshot's `RUN_SUMMARY.md` or
`Handoff_State.md`, claims a later phase or a cleaner closure state than the
evidence: all state `ReadyForNextPhase = NO`. Check 10 therefore passes. The
informational findings are:

- **COV-068 (`INFO`, `EXPECTED_CONSEQUENCE`).** 42 `_CONTEXT.md`
  provenance blocks still end at revision 1.4 (B1 not selected: D-PEC-93
  ruling, A without B1). Unchanged from the prior run.
- **COV-069 (`INFO`, `EXPECTED_CONSEQUENCE`).** 64 of 66 `_REFERENCES.md`
  still name revision 1.4; the two new packets name revision 1.5.
- **COV-070 (`INFO`, `EXPECTED_CONSEQUENCE`).** 32 SOWs byte-unchanged (B4
  not opened; D-PEC-93 Limits exclude SOW writes).
- **COV-071 (`INFO`, `EXPECTED_CONSEQUENCE`).** Closure-tool isolated units,
  above.
- **COV-072 (`INFO`, `PRE-EXISTING`).** Evidence-quote currency, above.
- **COV-073 (`INFO`, `EXPECTED_CONSEQUENCE`).** The SCA-005 snapshot's
  `Handoff_State.md` and `RUN_SUMMARY.md`, and both `_LATEST.md` pointers,
  predate D-PEC-93: they still say DEL-02-08/09 `NOT_CREATED`, dependency
  registers pre-B3, and `AuditState BLOCKED` by `COV_SCA005_POSTCHANGE`. They
  understate the observed state and claim no more closure than the evidence.
  D-PEC-93 did not open these records; its run root `HANDOFF_STATE.md`, not
  yet written, is where the proposal places the SCA-005 open-work closeout.

The prior run's count defect (its COV-072, "40, not 42") is resolved: every
current handoff surface carries 42, and the SCA-005 `RUN_SUMMARY.md` records
the evidence correction (`Decision_Log.md` D-13).

## Package shape (Check 9b)

Unchanged from the prior run. The main document carries a `Companion
Inventory` section mirrored exactly by `Companion_Inventory.csv` (six files);
authoritative and derived roles are labelled; the §2/§5 duplication of
register fields is declared and justified (DL-15); §7 register counts agree
with the registers. No derived publication artifact is treated as
authoritative.

## Comparison with `COV_SCA005_POSTCHANGE_2026-09-25_1344`

The full comparison is in `PrePost_Comparison.md`. Headlines:

- **Forward deliverable coverage.** 96.97 % → 100 % (64/66 → 66/66).
- **Issues.** 2 / 6 / 74 → 0 / 3 / 70.
- **Per-finding delta.** 67 carried, 1 changed, 14 resolved, 5 new. No new
  BLOCKER or WARNING. No regression.
- **Register validator.** 0 errors / 2 warnings (exit 1) → 0 / 0 (exit 0).
- **Closure.** 119 edges / 64 nodes, isolated 2 → 111 / 66, isolated 6.

### Against the briefed expectation

| Expectation | Observed | Match |
|---|---|---|
| Cleared: prior COV-001/002, 070/071, 068/069, 079/080/081 | All nine resolved | yes |
| Forward production-unit coverage 100 % | 100 % (66/66) | yes |
| Unchanged: prior COV-006/008/042 | Carried as COV-004/006/042 | yes |
| Unchanged: prior COV-077/078 (B1 open) | Carried as COV-068 (unchanged) and COV-069 (now "64 of 66": the 2 new packets are at revision 1.5) | yes, with the count note |
| New: six isolated units | COV-071, `INFO` | yes |
| Prior COV-072 carried or resolved | Resolved by the recorded evidence correction | yes |
| 0 blockers; overall status WARN | 0 blockers; `overall_status WARNINGS`, `closure_readiness WARN` | yes (method enum spelling) |
| 19 non-verbatim quotes, not caused by the act | COV-072, `INFO`, `PRE-EXISTING`; same 19 rows | yes |

**Beyond the briefed list** (all `INFO`, none a blocker or warning):

- COV-015 and COV-016: the two new `OPEN` folders have no anticipated
  artifact set yet (Check 6 lists every absence).
- COV-073: the SCA-005 snapshot and both pointers still describe the pre-act
  state.
- Prior COV-073, 074, 075 and 076 (pointer, SCA-004, A5 and anticipatory
  provenance rows) are resolved by checkpoint-3 acceptance and A6, which
  happened after the prior run. The brief did not list them.

## What to fix for a cleaner rerun

These are observations of what would clear the remaining findings, not
recommendations to act; each belongs to its own owner and gate.

1. **The three Check-6 warnings** clear only if artifact-location practice
   or lifecycle state changes. They are unrelated to SCA-005 and D-PEC-93.
2. **B1 re-pin** (separate packet) would clear COV-068 and COV-069.
3. **B4 SOW currency** would change COV-070.
4. **A later evidence-quote refresh** (owner-ruled residual) would clear
   COV-072.
5. **The D-PEC-93 run-root closeout** (`HANDOFF_STATE.md`) and any later
   pointer maintenance would address COV-073.
6. COV-071 is the planned topology for retired deliverables and stays while
   they are retired.

## Findings

The D-PEC-93 poststate passes every structural check the method owns: forward
and reverse coverage (11/11 packages, 66/66 deliverables), ID consistency,
context fidelity (66/66), objective evidence, ledger integrity with every IN
row folder-backed, package shape and lifecycle. The strict register validator
reads 0/0 and the closure tool reads the planned topology. The remaining
warnings are pre-existing and unrelated to this act.

This derivative evidence accepts nothing and authorizes nothing. The audit
`_LATEST.md` pointer is unchanged.
