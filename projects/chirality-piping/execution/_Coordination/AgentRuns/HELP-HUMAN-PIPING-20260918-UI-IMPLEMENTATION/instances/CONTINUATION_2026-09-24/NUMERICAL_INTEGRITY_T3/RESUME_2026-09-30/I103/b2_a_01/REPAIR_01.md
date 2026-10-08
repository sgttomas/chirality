# I103 lane A, repair 01: RV122's SF-1, SF-2 and N-1

TASK (Type 2), I103, for ROOT; no delegation. 2026-10-08 UTC. **Basis:** ROOT's repair instruction relaying RV122 (RV-Q2 round 1: PASS at `e96355ef8f`, 0/2/3; `R/REVIEW_RV122/b2_a_01/REVIEW.md` sha256 `c49591fd…`, verified) and its probes A and B (`evidence/probes.out.txt`, `probe_appended_*.rs.txt`). RETURN.md and SHA256SUMS are unchanged; this file and `_run_records/repair_01/` are covered by `SHA256SUMS.repair_01`.

## New heads (`WT/b2-a`, `codex/piping-t3-b2-a-20261008`, on `e96355ef8f`; not pushed)

| Repair | Commit | Change |
|---|---|---|
| SF-1 | `c2c725347d` | test only: `b3a_direct_entry_oracles` |
| SF-2 | `70cb600519` | B3b-A's D1.5 exact clause, and a new law test |
| N-1 | `ea5625ad04` | comments only: `retained_memory.rs`, `build_identity.rs`, `build.rs` |

`b3b_direct_entry_keeps_the_exact_ordinary_bytes` is untouched (lane P changed it on `b2`; ROOT resolves it at the merge). The host screen over `e96355ef8f..ea5625ad04`: 4 files, 0 hits.

## SF-1: m3l's interim outcome, pinned

- `b3a_direct_entry_oracles` no longer accepts `Some(Ok(_))` and no longer compares only `results`. In the registered build, in both modes, it pins:
  - the cause, `W1Fallback::Precommit { gate: "G8", code: "RETAINED_PRECISION_INVOCATION_MISMATCH" }`;
  - the one publication (`into_publication`), equal to the plain value-route bytes plus exactly one notice for `case`, as B1 pins a precommit fallback (`u3g2_direct_entry_w1_fallbacks_append_one_notice`).
- The expected bytes come from `with_one_notice`, the same text as the facade tests' `with_notice(plain, case, None)`, copied into the law tests so that lane A stays in its files.
- The comment says the pin changes at J5, when the readers' B3a admits the L3 contract.

## SF-2: the exact clause reads the empty list's capacity

- On branch E, D1.5's exact clause also requires each case's explicitly empty `pressure_regions` list to have `capacity() == 0`. Spare capacity refuses with the new `CapFact::PressureRegionsCapacity { observed, cap: 0 }`. That is a resource-admission reason, as an empty `sections` owner with spare capacity gets `SectionsCapacity` at D1.9.
- It is raised in D1.5's position, not as a D1.9 row: `CAP_ROWS` stays 53. Its `clause()` reads D1.9, as every capacity reason does.
- A parsed request's empty list has capacity 0, so no admitted input changes.
- **The test** is `b3b_exact_regions_capacity_is_read`, with RV122's probe B as the witness:
  - capacity 65,536 and capacity 1 are refused on the first and the last of C cases;
  - length 0 with capacity 0 is admitted;
  - a parsed request's lists have capacity 0;
  - the sections control refuses with `SectionsCapacity`.

## N-1

The three comments that said "the precommit reader's 13 `include_str!` inputs" now name all 17 inputs: the PP lock, the reader's 13 statics and J1's three appended statics. N-2 (restore `[1..]` when RS packages the three) and N-3 (lane P) are not done here, as ruled.

## Evidence

**The suites against `e96355ef8f`** (test by test, fresh targets `WT/targets/i103-b2-a-r1-*`; `_run_records/repair_01/compare_r1_vs_e96355ef8f.json`):
- **PP** (`--lib`, `retained_precision_admission`, `s11f_site_test`): 602 ok, 1 failed, 11 ignored against 601, 1, 11. 0 tests changed; +1 new test (`b3b_exact_regions_capacity_is_read`). The modified `b3a_direct_entry_oracles` passes.
- **Runner** (all tests): 85 ok, 2 failed, identical.
- The three failures are I4′'s own and are unchanged: `t13_committed_fallback_uz_is_byte_identical` and the two load-reference runner tests.
- RE, PY and TS are not rerun: no file they read changed.

**The repairs' mutants** (`_run_records/repair_01/repair_mutants.json`): one exact edit each, run in scratch archives. The SF-1 mutants are run on both trees, to show the gap RV122 found and that it is closed.

| Mutant | Repair | Edit | Old test at `e96355ef8f` | New test at `ea5625ad04` |
|---|---|---|---|---|
| R1-SF1-a | SF-1 | the precommit fallback publishes without its notice | **survives** | killed by `b3a_direct_entry_oracles` |
| R1-SF1-b | SF-1 | RS's G8 admits the L3 contract (m3l's successor passes precommit) | **survives** | killed by `b3a_direct_entry_oracles` |
| R1-SF2 | SF-2 | the exact D1.5 clause no longer reads the empty list's capacity | n/a (no such clause) | killed by `b3b_exact_regions_capacity_is_read` |

Every mutant compiled. The registered build is shown by the kills themselves: in another build `b3a_direct_entry_oracles` compares only plain bytes, so neither SF-1 mutant could fail it.

The raw logs are in `WT/scratch/i103_b2_a/runs/` (`r1`, `r1mut`); the archives were deleted after the runs.
