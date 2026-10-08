# I102 lane K: repair 01 (RV121's RK-1 to RK-4), tests only

I102 (TASK) did this for ROOT on 2026-10-08 UTC. It follows ROOT's rulings on RV121's REVIEW.md (`7bc01d1c…`).

- **Branch:** `codex/piping-t3-b2-k-20261008` in `WT/b2-k`.
- **New head:** `e22fd799bc`, one commit over `ef51a2d295`.
- **Changed files:** three test files under `FK/tests/retained_k4/`. FK's `src` is unchanged (`git diff --name-only ef51a2d295 e22fd799bc`).

## Changes

| Item | Test | Mutant it kills |
|---|---|---|
| RK-1 | `B2K_NORM3` gains the exact overflow tie (7fefffffffffffe5, 7e7443426b800000, 7e4d4ef94a000000) and z one ulp below and above, asserted as refused, MAX and refused. The oracle's `NORM3` gains that tie and RV121's other two, each with its neighbours (9 lines). The generator asserts each is an exact tie, S = (MAX + 2^970)^2, and checks the three outcomes with its own integer square root. | p2m29 (`let up=upper>0;`). Killed by `b2k_rn64_norm3_vectors_signed_zeros_refusal_and_work` and `b2k_rn64_norm3_agrees_with_the_oracle_vectors`: the kernel publishes MAX where `Binary64Range` is expected. |
| RK-2 | New `b2k_k13_a_case_owner_keeps_its_hull_projected_displacement_magnitude`. The net cases of C7 and C9 freeze magnitudes at nodes 0 and 1. Each frozen value equals the hull projection of both lanes, formed in the test. The tip bits are pinned (`3f4ecfb060a222f8` and `64cecfb060a222f8`), and (ii) of the frozen components is one ulp above them. | RV121's m36 (`let combination=true;` in `project`). It fails on "C7 m1: the hull projection" (…f9 against …f8). |
| RK-3 | In `b2k_c05_the_combination_coverage_rule`, the case control now begins four row sets. The complete set is admitted. Without the maximum alone, without the mode record alone, and without both, it is refused ("missing final coverage"). | RV121's m18 (`!(j % 21 == 20)`). It fails on "the maximum alone missing (slot 20)". |
| RK-4 | K-09 pins the pattern. C2, C3, C6, C7 and C9 certify every row. C1, C4 and C5 lose `z7.I.1` and `z7.17.1`, and C8 loses `z7.J.1`. Each failing row is a relative MPa bending row with predicates [false, false, true, true], and `outcome.is_ok()` is true exactly when no row fails. The printed rows are unchanged. | mrk4 (`tests.into_iter().skip(2)`: relative rows judged only on the decimal predicates). At ef51a2d295 it survives FK's whole lib (508 passed); at e22fd799bc K-09 fails. |

`_run_records/MUTANTS.md` is corrected:
- p2m29's row is marked "not equivalent".
- A Repair 01 section gives the reason and the four rows above.

RETURN.md's sentence on p2m29 ("y0 is never odd at a tie") is wrong for overflowing estimates. This correction supersedes it, and RETURN.md itself is left as returned. SHA256SUMS's line for MUTANTS.md was updated:

| File | Before | After |
|---|---|---|
| `MUTANTS.md` | `a3f84dee…` | see `SHA256SUMS` |
| `SHA256SUMS` | `f21f1ee3…` | its new hash is given in the hand-back |

## Results at e22fd799bc (fresh targets under `WT/targets/i102-b2-k/`)

- **FK suite:** lib 509 passed, 0 failed, 1 ignored. All 7 integration binaries pass, S11 included, as do the 6 doc tests.
- **FK against ef51a2d295, test for test:** 576 test lines against 575. The only difference is the added RK-2 test; every other outcome is equal (`repair_01/compare.txt`).
- **K-09's printed rows:** all 658 `B2K_` lines are byte-identical to ef51a2d295's.
- **Fixtures:**
  - The generator's verify mode reproduces both fixtures.
  - The J2k fixture is unchanged (`467f8811…`).
  - The combination fixture is now `8516b06d…` (was `1999a326…`); only `NORM3` changed, with 9 added lines.
  - The generator is now `7fdfccdd…`.
- **PP and the FK dependents** were not re-run. They build FK's library without `cfg(test)`, and that library is byte-unchanged.
- **Screens:** `t3_host_screen.py` found 3 files and 0 hits. `validate_private_terms.py` (from the host, plus the private list) found 0 findings.

## Open

Nothing new. ROOT has accepted K-09's DEF-O limit, K-01's ledger-refusal half and W05's `Refused`.

**Host slips, disclosed:**
- I ran two waits on the mutant runner, a monitor and a foreground until-loop, which both ended when the runner exited.
- One test text edit (the RK-4 insertion) was made with the host `python3`. Every oracle, mutant and record step used VENV.

Evidence is in `_run_records/repair_01/`, with paths shown as placeholders. Sums are in `SHA256SUMS.repair_01`.
