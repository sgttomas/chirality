# Pre/Post Comparison — COV_SCA005_POSTSETUP_2026-09-25_1606 → COV_SCA006_POSTCHANGE_2026-09-26_0051

This is the formal comparison mode of method Step 12, required by SCA-006
`Propagation_Plan.md` §C4 item 2. The baseline `coverage_summary.json` hashes
to `b7b432a2b9e9ae13a911c7193b02776e64cd07e247135b3c98caf77882f4128d`
(verified), byte-identical to `SCA-006_2026-09-25_1912/Pre_Change_Coverage.json`.

## Basis

| | Baseline (POSTSETUP) | This run (SCA-006 POSTCHANGE) |
|---|---|---|
| Decomposition | revision 1.5 `current_basis` `dc2b8479…9660` | revision 1.6 pre-acceptance `3ef0412a…9b29` (differs from the accepted CP2 candidate only in the pre-acceptance front-matter lines and date slots) |
| Registers | ScopeLedger `83152a94…fd9df`, Deliverables `b8628fc4…3d65a`, ContextBudgetQA `2a194105…eb0df`, Companion_Inventory `7c8a24a8…6ef8` | `1d24a4b8…e916e`, `94ee5d18…9805`, `93b0bb07…c7c`, `1597ceec…8662` (each equal to its CP2 candidate) |
| PRD | v2.3 `fff27a66…fdc32` | v2.4 `ae49b806…7fbe` (equal to the CP2 candidate) |
| Pointers | revision 1.5 / SCA-005 (pre-D-PEC-95 text) | revision 1.5 / SCA-005 (D-PEC-95 text; unmoved by design until A6) |
| Active SCA snapshot | SCA-005, complete | SCA-005, complete, byte-identical; SCA-006 candidate mid-A5 |
| Intervening acts | — | `D-PEC-95` (PR #924, `abfd0897b`): 119 derivative paths (42 contexts, 64 references, 10 registers, 2 pointers, `_COORDINATION.md`); then SCA-006 Lane A1, A2, A4 and part of A5 |
| Git basis | `995af4f36` | `5e0169f5e` |
| Method edition | audit-decomp contract `70a5abeb…401a0c`, method `97df8402…d79c2` | contract `704929c7…4e75`, method `51a0c69b…8308827` (Root wave-2A; `EXPECTED_CONSEQUENCE` severity) |

Deliverable-tree changes between the two audited commits: the `D-PEC-95`
paths (contexts, references, registers) and the three SCA-006 A2 `_CONTEXT.md`
mirrors. No `_STATUS.md`, `ScopeOfWork.md` or `artifacts/` file changed.

## Topology

| Metric | Baseline | This run | Delta |
|---|---|---|---|
| Packages | 11 | 11 | 0 |
| Deliverable rows | 66 (62 active / 4 retired) | 68 (64 / 4) | +2 (DEL-08-06, DEL-10-13) |
| Deliverable folders | 66 | 66 | 0 (the two new rows have no folder: plan §B1) |
| Objectives | 6 | 6 | 0 (statements unchanged) |
| Scope items / ledger rows | 96 (70 / 18 / 8) | 100 (74 / 18 / 8) | +4 IN (SOW-097..100) |
| Per-package IN (PKG-00..10) | 3/8/9/7/6/3/6/3/6/7/12 | 3/8/9/7/7/3/6/3/8/7/13 | PKG-04 +1, PKG-08 +2, PKG-10 +1 |
| Active envelopes S/M/L/XL | 28/32/2/0 | 28/34/2/0 | M +2 (DEL-08-03 S→M; DEL-08-06 M; DEL-10-13 S) |
| Open / resolved issues | 10 / 3 | 10 / 3 | 0 |
| Vocabulary terms | 26 | 29 | +3 |
| Register validator (strict) | 66 registers / 263 rows / 0 errors / 0 warnings (exit 0) | 66 / 263 / 0 / 2 DRB-008 (exit 1) | +2 DRB-008 (DEL-08-06, DEL-10-13; plan §C2) |
| Dependency rows ANCHOR / EXECUTION | 140 / 123 (ACTIVE 132 / 111; RETIRED 8 / 12) | same | 0 (SCA-006 Lane A wrote no register) |
| Dependency closure | 111 edges / 66 nodes / 0 SCC / 0 bidirectional / 6 isolated / hub DEL-03-01 (25) | same; `closure_summary.json` byte-identical (`bd73806c…187a`) | 0 |
| Non-verbatim ACTIVE EXECUTION quotes | 19 | 2 | −19 by `D-PEC-95` N3; +2 by SCA-006 (B3) |
| Context provenance (last revision) | 1.5: 24 / 1.4: 42 | 1.5: 63 / 1.6: 3 | 1.4 → 1.5 ×42 by `D-PEC-95` N2; 1.5 → 1.6 ×3 by SCA-006 A2 |
| Reference packets (revision / PRD) | 1.4: 64 / 1.5: 2 | 1.5: 66 (all PRD v2.3) | 1.4 → 1.5 ×64 by `D-PEC-95` N2 |
| Lifecycle | 26 INITIALIZED / 30 OPEN / 4 CHECKING / 2 IN_PROGRESS / 4 RETIRED | same | 0 |
| Contracts | 32 SOW_V1 / 34 NONE | same (+2 declared without folder) | 0 |

## Coverage percentages

| Metric | Baseline | This run |
|---|---|---|
| Forward packages | 100 % (11/11) | 100 % (11/11) |
| Forward deliverables | 100 % (66/66) | 97.0588 % (66/68) |
| Reverse coverage | 100 % | 100 % |
| Context fidelity | 100 % (66/66) | 100 % (66/66 matched folders) |
| Artifact presence | 4.5455 % (3/66) | 4.4118 % (3/68) |
| Objective coverage | 100 % | 100 % (OBJ-001 25/27 supporters folder-backed) |
| IN rows / active deliverables without objective | 0 / 0 | 0 / 0 |

## Check verdicts

| Check | Baseline | This run | Note |
|---|---|---|---|
| 1 | PASS | PASS | +2 INFO from the structure tool (new to this edition) |
| 2 | PASS | PASS | 2 missing folders, `EXPECTED_CONSEQUENCE` (would be BLOCKER) |
| 3, 4, 5 | PASS | PASS | — |
| 6 | WARNING | WARNING | same three warnings |
| 7 | PASS | PASS | +1 INFO (OBJ-001) |
| 8 | PASS | PASS | 2 `EXPECTED_CONSEQUENCE` (would be WARNING) |
| 9 | SKIPPED | SKIPPED | derivative-currency observations now recorded here (method change) |
| 9b | PASS | PASS | — |
| 10 | PASS | PASS | — |
| 11 | PASS | PASS | — |

## Issue counts

| Severity | Baseline | This run |
|---|---|---|
| BLOCKER | 0 | 0 |
| WARNING | 3 | 3 |
| INFO | 70 | 71 |
| EXPECTED_CONSEQUENCE | — (not a severity in the baseline edition; 11 INFO rows carried an `[EXPECTED_CONSEQUENCE]` description tag) | 12 |
| `overall_status` / `closure_readiness` | WARNINGS / WARN | WARNINGS / WARN |

## Methodology changes that affect the comparison

1. **Severity model.** The baseline tagged classifications
   (`PRE-EXISTING`, `EXPECTED_CONSEQUENCE`) inside INFO/WARNING descriptions.
   The current edition makes `EXPECTED_CONSEQUENCE` a severity with a
   `DecisionRef`, for conditions that would otherwise be BLOCKER or WARNING.
   Baseline INFO rows tagged `[EXPECTED_CONSEQUENCE]` that are carried
   (DEL-02-08/09 artifacts, retired Check-7 rows, isolated units) therefore
   stay INFO (`Decision_Log.md` D-6).
2. **Check placement.** Derivative-currency observations moved from Check 10
   (baseline D-9) to Check 9, as the current method directs. The carried
   baseline COV-070 and COV-071 changed check number for this reason only.
3. **Structure tool.** `audit_structure.py` is now required. Its two
   workspace-level observations (COV-001, COV-002) are pre-existing conditions
   measured for the first time, not regressions.
4. **Tool bytes.** The register validator and closure tool changed bytes since
   the baseline; their outputs remain comparable (`Decision_Log.md` D-22).

## Attribution of the four baseline findings the plan names (§C4 item 2)

| Baseline | Disposition | Attributed to | Not an SCA-006 effect because |
|---|---|---|---|
| COV-068 (42 contexts at 1.4) | RESOLVED | `D-PEC-95` N2 | the 42 files changed in `abfd0897b`; SCA-006 later touched only 3 contexts (A2) |
| COV-069 (64 references at 1.4) | RESOLVED | `D-PEC-95` N2 | the 64 files changed in `abfd0897b`; SCA-006 wrote no `_REFERENCES.md` |
| COV-072 (19 non-verbatim quotes) | RESOLVED | `D-PEC-95` N3 | the 10 registers changed in `abfd0897b`; SCA-006 wrote no `Dependencies.csv` |
| COV-073 (stale SCA-005 handoff surfaces and pointers) | PARTIALLY RESOLVED; residual carried as COV-086 `INFO` | `D-PEC-95` N1 (pointers); option P kept the two SCA-005 snapshot files byte-identical | the pointers changed in `abfd0897b` and SCA-006 has not moved them (A6 pending) |

The SCA-006 consequences that resemble them (COV-077, COV-078: lag against
revision 1.6 / PRD v2.4; COV-075, COV-076: two different stale quotes) are new
conditions introduced by SCA-006 Lane A1. They are mapped as NEW below, not as
continuations of the baseline IDs.

## Regressions and improvements

- **Regressions (new BLOCKER or WARNING):** none. Every new condition that
  would be BLOCKER or WARNING is an `EXPECTED_CONSEQUENCE` under `D-PEC-97`.
- **Improvements:** COV-068, COV-069 and COV-072 resolved, and the pointer
  part of COV-073, all by `D-PEC-95`.

## Per-finding delta

Prior IDs are the baseline's; new IDs are this run's. Mapping rules are in
`Decision_Log.md` D-4 and the table's notes.

| Prior ID | Check | Prior severity | Entity | Disposition | New ID | New severity | Attribution / note |
|---|---|---|---|---|---|---|---|
| COV-001 | 6 | INFO | DEL-00-02 | CARRIED | COV-005 | INFO | unchanged condition |
| COV-002 | 6 | INFO | DEL-01-01 | CARRIED | COV-006 | INFO | unchanged condition |
| COV-003 | 6 | INFO | DEL-01-02 | CARRIED | COV-007 | INFO | unchanged condition |
| COV-004 | 6 | WARNING | DEL-01-03 | CARRIED | COV-008 | WARNING | unchanged condition |
| COV-005 | 6 | INFO | DEL-01-04 | CARRIED | COV-009 | INFO | unchanged condition |
| COV-006 | 6 | WARNING | DEL-01-05 | CARRIED | COV-010 | WARNING | unchanged condition |
| COV-007 | 6 | INFO | DEL-01-06 | CARRIED | COV-011 | INFO | unchanged condition |
| COV-008 | 6 | INFO | DEL-02-01 | CARRIED | COV-012 | INFO | unchanged condition |
| COV-009 | 6 | INFO | DEL-02-02 | CARRIED | COV-013 | INFO | unchanged condition |
| COV-010 | 6 | INFO | DEL-02-03 | CARRIED | COV-014 | INFO | unchanged condition |
| COV-011 | 6 | INFO | DEL-02-04 | CARRIED | COV-015 | INFO | unchanged condition |
| COV-012 | 6 | INFO | DEL-02-05 | CARRIED | COV-016 | INFO | unchanged condition |
| COV-013 | 6 | INFO | DEL-02-06 | CARRIED | COV-017 | INFO | unchanged condition |
| COV-014 | 6 | INFO | DEL-02-07 | CARRIED | COV-018 | INFO | unchanged condition |
| COV-015 | 6 | INFO | DEL-02-08 | CARRIED | COV-019 | INFO | unchanged condition |
| COV-016 | 6 | INFO | DEL-02-09 | CARRIED | COV-020 | INFO | unchanged condition |
| COV-017 | 6 | INFO | DEL-03-01 | CARRIED | COV-021 | INFO | unchanged condition |
| COV-018 | 6 | INFO | DEL-03-02 | CARRIED | COV-022 | INFO | unchanged condition |
| COV-019 | 6 | INFO | DEL-03-03 | CARRIED | COV-023 | INFO | unchanged condition |
| COV-020 | 6 | INFO | DEL-03-04 | CARRIED | COV-024 | INFO | unchanged condition |
| COV-021 | 6 | INFO | DEL-03-05 | CARRIED | COV-025 | INFO | unchanged condition |
| COV-022 | 6 | INFO | DEL-03-06 | CARRIED | COV-026 | INFO | unchanged condition |
| COV-023 | 6 | INFO | DEL-04-01 | CARRIED | COV-027 | INFO | unchanged condition |
| COV-024 | 6 | INFO | DEL-04-02 | CARRIED | COV-028 | INFO | unchanged condition |
| COV-025 | 6 | INFO | DEL-04-03 | CARRIED | COV-029 | INFO | unchanged condition |
| COV-026 | 6 | INFO | DEL-04-04 | CARRIED | COV-030 | INFO | unchanged condition |
| COV-027 | 6 | INFO | DEL-04-05 | CARRIED | COV-031 | INFO | unchanged condition |
| COV-028 | 6 | INFO | DEL-05-01 | CARRIED | COV-032 | INFO | unchanged condition |
| COV-029 | 6 | INFO | DEL-05-02 | CARRIED | COV-033 | INFO | unchanged condition |
| COV-030 | 6 | INFO | DEL-06-01 | CARRIED | COV-034 | INFO | unchanged condition |
| COV-031 | 6 | INFO | DEL-06-02 | CARRIED | COV-035 | INFO | unchanged condition |
| COV-032 | 6 | INFO | DEL-06-03 | CARRIED | COV-036 | INFO | unchanged condition |
| COV-033 | 6 | INFO | DEL-06-04 | CARRIED | COV-037 | INFO | unchanged condition |
| COV-034 | 6 | INFO | DEL-06-05 | CARRIED | COV-038 | INFO | unchanged condition |
| COV-035 | 6 | INFO | DEL-06-06 | CARRIED | COV-039 | INFO | unchanged condition |
| COV-036 | 6 | INFO | DEL-07-01 | CARRIED | COV-040 | INFO | unchanged condition |
| COV-037 | 6 | INFO | DEL-07-02 | CARRIED | COV-041 | INFO | unchanged condition |
| COV-038 | 6 | INFO | DEL-07-03 | CARRIED | COV-042 | INFO | unchanged condition |
| COV-039 | 6 | INFO | DEL-07-04 | CARRIED | COV-043 | INFO | unchanged condition |
| COV-040 | 6 | INFO | DEL-07-05 | CARRIED | COV-044 | INFO | unchanged condition |
| COV-041 | 6 | INFO | DEL-08-01 | CARRIED | COV-045 | INFO | unchanged condition |
| COV-042 | 6 | WARNING | DEL-08-02 | CARRIED | COV-046 | WARNING | unchanged condition |
| COV-043 | 6 | INFO | DEL-08-03 | CARRIED | COV-047 | INFO | unchanged condition |
| COV-044 | 6 | INFO | DEL-08-04 | CARRIED | COV-048 | INFO | unchanged condition |
| COV-045 | 6 | INFO | DEL-08-05 | CARRIED | COV-049 | INFO | unchanged condition |
| COV-046 | 6 | INFO | DEL-09-01 | CARRIED | COV-050 | INFO | unchanged condition |
| COV-047 | 6 | INFO | DEL-09-02 | CARRIED | COV-051 | INFO | unchanged condition |
| COV-048 | 6 | INFO | DEL-09-03 | CARRIED | COV-052 | INFO | unchanged condition |
| COV-049 | 6 | INFO | DEL-09-04 | CARRIED | COV-053 | INFO | unchanged condition |
| COV-050 | 6 | INFO | DEL-09-05 | CARRIED | COV-054 | INFO | unchanged condition |
| COV-051 | 6 | INFO | DEL-09-06 | CARRIED | COV-055 | INFO | unchanged condition |
| COV-052 | 6 | INFO | DEL-09-07 | CARRIED | COV-056 | INFO | unchanged condition |
| COV-053 | 6 | INFO | DEL-10-02 | CARRIED | COV-057 | INFO | unchanged condition |
| COV-054 | 6 | INFO | DEL-10-03 | CARRIED | COV-058 | INFO | unchanged condition |
| COV-055 | 6 | INFO | DEL-10-04 | CARRIED | COV-059 | INFO | unchanged condition |
| COV-056 | 6 | INFO | DEL-10-05 | CARRIED | COV-060 | INFO | unchanged condition |
| COV-057 | 6 | INFO | DEL-10-06 | CARRIED | COV-061 | INFO | unchanged condition |
| COV-058 | 6 | INFO | DEL-10-07 | CARRIED | COV-062 | INFO | unchanged condition |
| COV-059 | 6 | INFO | DEL-10-08 | CARRIED | COV-063 | INFO | unchanged condition |
| COV-060 | 6 | INFO | DEL-10-09 | CARRIED | COV-064 | INFO | unchanged condition |
| COV-061 | 6 | INFO | DEL-10-10 | CARRIED | COV-065 | INFO | unchanged condition |
| COV-062 | 6 | INFO | DEL-10-11 | CARRIED | COV-066 | INFO | unchanged condition |
| COV-063 | 6 | INFO | DEL-10-12 | CARRIED | COV-067 | INFO | unchanged condition |
| COV-064 | 7 | INFO | DEL-06-04 | CARRIED | COV-069 | INFO | unchanged condition |
| COV-065 | 7 | INFO | DEL-07-02 | CARRIED | COV-070 | INFO | unchanged condition |
| COV-066 | 7 | INFO | DEL-07-04 | CARRIED | COV-071 | INFO | unchanged condition |
| COV-067 | 7 | INFO | DEL-07-05 | CARRIED | COV-072 | INFO | unchanged condition |
| COV-068 | 10 | INFO | DEL-* (42 not in A2) | RESOLVED | — | — | D-PEC-95 N2 re-pinned the 42 contexts to revision 1.5 (0 contexts end at 1.4). The new version-only lag against revision 1.6 is a separate SCA-006 consequence, COV-077 |
| COV-069 | 10 | INFO | DEL-* (64 of 66) | RESOLVED | — | — | D-PEC-95 N2 re-pinned the 64 reference packets to revision 1.5 (0 at 1.4). The new lag against revision 1.6 / PRD v2.4 is a separate SCA-006 consequence, COV-078 |
| COV-070 | 10 | INFO | 32 SOW_V1 contracts | CHANGED | COV-081 | INFO | Check 10 → 9 (current method: derivative-currency observations); SCA-006 §B4 nine-contract set added; SOW bytes unchanged |
| COV-071 | 10 | INFO | DEL-00-03; DEL-01-05; DEL-06-04; DEL-07-02; DEL-07-04; DEL-07-05 | CARRIED | COV-082 | INFO | Check 10 → 9 (current method); closure output byte-identical |
| COV-072 | 10 | INFO | 19 ACTIVE EXECUTION rows (10 registers) | RESOLVED | — | — | D-PEC-95 N3 refreshed the 19 quotes; all 19 now verbatim and note D-PEC-95. The two stale quotes now open are different rows and an SCA-006 consequence, COV-075/076 |
| COV-073 | 10 | INFO | SCA-005 | CHANGED | COV-086 | INFO | Narrowed: pointer part resolved by D-PEC-95 N1; SCA-005 Handoff_State.md and RUN_SUMMARY.md kept byte-identical by D-PEC-95 option P, carried as INFO |
| — | 1 | — | PKG-00..PKG-10 (11) | NEW | COV-001 | INFO | PRE-EXISTING (newly measured) |
| — | 1 | — | _Aggregation, _Estimates, _Sources | NEW | COV-002 | INFO | PRE-EXISTING (newly measured) |
| — | 2 | — | DEL-08-06 | NEW | COV-003 | EXPECTED_CONSEQUENCE | SCA-006 |
| — | 2 | — | DEL-10-13 | NEW | COV-004 | EXPECTED_CONSEQUENCE | SCA-006 |
| — | 7 | — | OBJ-001 | NEW | COV-068 | INFO | SCA-006 |
| — | 8 | — | SOW-099 | NEW | COV-073 | EXPECTED_CONSEQUENCE | SCA-006 |
| — | 8 | — | SOW-100 | NEW | COV-074 | EXPECTED_CONSEQUENCE | SCA-006 |
| — | 9 | — | DEP-09-06-003 | NEW | COV-075 | EXPECTED_CONSEQUENCE | SCA-006 |
| — | 9 | — | DEP-10-03-003 | NEW | COV-076 | EXPECTED_CONSEQUENCE | SCA-006 |
| — | 9 | — | DEL-* (63 of 66 _CONTEXT.md) | NEW | COV-077 | EXPECTED_CONSEQUENCE | SCA-006 |
| — | 9 | — | DEL-* (66 of 66 _REFERENCES.md) | NEW | COV-078 | EXPECTED_CONSEQUENCE | SCA-006 |
| — | 9 | — | DEL-04-03; DEL-08-01; DEL-08-03 | NEW | COV-079 | EXPECTED_CONSEQUENCE | SCA-006 |
| — | 9 | — | DEL-04-03; DEL-08-03 | NEW | COV-080 | EXPECTED_CONSEQUENCE | SCA-006 |
| — | 9 | — | SOW-094; DEL-01-06; vocabulary 'feed profile' | NEW | COV-083 | INFO | PRE-EXISTING text; new owner direction (unforeseen) |
| — | 10 | — | SCA-005 (accepted predecessor); revision 1.5 pointer | NEW | COV-084 | EXPECTED_CONSEQUENCE | SCA-006 (designed) |
| — | 10 | — | SCA-006 (candidate) | NEW | COV-085 | EXPECTED_CONSEQUENCE | SCA-006 (designed) |

Counts: CARRIED 68, CHANGED 2, RESOLVED 3, NEW 16; prior rows 73, new rows 86
