# RV122 (RV-Q2), round 1, addendum 01: I103's repair round 01 on lane A

**Repair round 01 on lane A: CONFIRMED.** RV122, for ROOT, 2026-10-08 UTC. SF-1, SF-2 and N-1 are repaired.

**Candidate:** `codex/piping-t3-b2-a-20261008` at `ea5625ad04`, which is also origin's head. It adds three commits over `e96355ef8f`:
- `c2c725347d`: SF-1, test only;
- `70cb600519`: SF-2;
- `ea5625ad04`: N-1, comments in `retained_memory.rs`, `build_identity.rs` and `build.rs`.

I read I103's `REPAIR_01.md` (`a6617dba…`, SHA256SUMS.repair_01 OK) after my own runs.

**Method:**
- a `git archive` copy of P at `ea5625ad04`;
- every cargo through `t3_cargo.sh --locked --offline`, in fresh per-tree targets (`WT/targets/rv122-r1-*`, `rv122-r1mut-pp`), one job at a time;
- the mutants in a `cp -R` copy;
- no Git write.

Every run was a Registered build: `the_registered_profile_is_the_only_permit_source` and `reviewed_inputs_bind…` pass in each.

## Findings

| ID | Status | Evidence |
|---|---|---|
| SF-1 | **Repaired** | In both modes, `b3a_direct_entry_oracles` now pins `Precommit{G8, RETAINED_PRECISION_INVOCATION_MISMATCH}`. It also pins the one publication (`into_publication`) as the plain bytes plus exactly one notice: its `with_one_notice` has the same text as B1's `with_notice(…, None)`, which my probe A matched. The `Ok` arm is gone. My mutant A1-SF1-a (the G8 fallback publishes without its notice) is killed by it, and by B1's two fallback tests. |
| SF-2 | **Repaired** | The exact D1.5 clause refuses an empty `pressure_regions` list with spare capacity. It refuses with `Cap{PressureRegionsCapacity, observed, cap: 0}`: `clause()` = Caps, precondition `resource_admission`, the same shape as `SectionsCapacity`. `CAP_ROWS` stays 53 and no row changes. `b3b_exact_regions_capacity_is_read` refuses probe B's 65,536 and capacity 1 on the first and the last case, and admits capacity 0. My three mutants are each killed by it: the check removed (A1-SF2-a), only capacity > 1 refuses (A1-SF2-b), and the first case only (A1-SF2-c). The repair only adds a refusal for a capacity no parsed request has, so nothing admits more than before. |
| N-1 | **Repaired** | The three comments now name all 17 inputs. `build.rs` changed only in comments. |
| N-2, N-3 | Open, as ruled | N-2 goes to the readers' lanes. N-3 goes to lane P (I105). |

**Nothing priced moves.** The generated profile block is still `a3c627216102bdfc`.

**Suites against `e96355ef8f`, test by test** (`addendum_01/compare_r1_vs_e96355ef8f.json`):
- **PP**, lib plus all 22 integration tests: 749 ok, 1 failed, 11 ignored, against 748, 1 and 11. 0 tests changed. The only addition is `b3b_exact_regions_capacity_is_read`, and the modified `b3a_direct_entry_oracles` passes.
- **Runner:** 85 ok, 2 failed, identical.

The failures are I4′'s own three. RE, PY and TS read no changed file.

**Evidence** (`addendum_01/`):
- `repair_checks.out.txt`;
- `compare_r1_vs_e96355ef8f.json`;
- `r1_mutants_def.py` and `r1_mutants.sh`, with placeholder paths;
- `meta_r1*.txt`.

**For ROOT:** nothing to rule. Lane P's change to `b3b_direct_entry_keeps_the_exact_ordinary_bytes` on `b2` is outside this candidate.
