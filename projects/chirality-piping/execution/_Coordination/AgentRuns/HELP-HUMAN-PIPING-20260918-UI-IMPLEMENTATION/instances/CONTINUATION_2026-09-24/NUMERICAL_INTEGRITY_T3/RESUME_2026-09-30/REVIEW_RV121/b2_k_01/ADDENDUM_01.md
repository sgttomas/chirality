# RV121 (RV-K) ADDENDUM_01: I102's repair 01 of lane K, against RK-1 to RK-4

TASK (Type 2), RV121, for ROOT (HELP_HUMAN, Agent 0), on ROOT's message of 2026-10-08 UTC. I made no delegation. REVIEW.md (`7bc01d1c…`) and its SHA256SUMS are unchanged.

**Candidate:** `WT/b2-k` at `e22fd799bc`, one commit over `ef51a2d295`. It changes 3 files under `FK/tests/retained_k4/` (+97/−5). I archived it into `WT/scratch/rv121_rvk/rep1/`, and read `R/I102/b2_k_01/REPAIR_01.md` (`0dedfbf2…`) only after the runs below.

## Verdict: CONFIRMED (0 BLOCKING, 0 SHOULD-FIX, 0 NOTE remaining)

| Finding | The repair | Mutant at `e22fd799bc` |
|---|---|---|
| RK-1 | `B2K_NORM3` gains the exact overflow tie and z one ulp below and above, expected as refused, MAX and refused. The oracle's `NORM3` gains my three ties with their neighbours (9 lines). The generator asserts S = (MAX + 2^970)^2 exactly and checks the three outcomes. All 9 expectations equal my independent oracle's. | I102's p2m29 is **killed** by `b2k_rn64_norm3_vectors_signed_zeros_refusal_and_work` and `b2k_rn64_norm3_agrees_with_the_oracle_vectors` (`left: Ok(1.797…e308)`, refusal expected). |
| RK-2 | A new test, `b2k_k13_a_case_owner_keeps_its_hull_projected_displacement_magnitude`. For the net cases of C7 and C9, the frozen magnitude must equal the hull projection of both lanes, formed in the test. The tip bits are pinned (`…f8`), and (ii) must be one ulp above. These match my probe. | m36 is **killed** by the new test ("C7 m1: the hull projection"). |
| RK-3 | C05's case control begins four row sets: the complete set is admitted; the maximum alone missing, the mode record alone missing, and both missing are each refused. | m18 is **killed** by C05 ("the maximum alone missing (slot 20)"). |
| RK-4 | K-09 pins C1–C9's failing rows, exactly as I reported. Each failing row must be a relative MPa bending row with predicates [F, F, T, T], and the proof must certify exactly when no row fails. | My mutant rk4 gates a combination's displacement magnitude as InputDerived. It is **killed** by K-09's per-row assertion ("C1 DisplacementMagnitude(1)"). The same mutant **survives** at `ef51a2d295`. I102's own mrk4 is a different mutant, also reported killed. |

**Also checked:**
- **FK's `src`:** byte-identical to `ef51a2d295` (`diff -r` of the archives).
- **Generator (`7fdfccdd…`):** verify mode reproduces both fixtures, and `--write` from the generator alone writes the same bytes. J2k's fixture is unchanged (`467f8811…`). The combination fixture is now `8516b06d…`: 9 lines added, 0 removed.
- **FK suite** (fresh target): lib 509 passed, 1 ignored; the integration and doc tests are unchanged. Against `ef51a2d295`, test for test, the only difference is the added RK-2 test.
- **PP and the dependents:** not re-run. Their builds use FK's library, which is unchanged.

**Records:** I102 edited `MUTANTS.md` and its line in the original `SHA256SUMS` in place. This does not matter, because the as-returned `MUTANTS.md` (`a3f84dee…`, which REVIEW.md cites) is in NUM's history at `996fa8cb90`.

**Execution:** one heavy job (`addendum_01/batch_repair.sh`), through the wrapper:
- FK's suite at `e22fd799bc`;
- `addendum_01/rv121_mutants_repair.py`, which ran the four mutants at `e22fd799bc` and rk4 at `ef51a2d295`, with the `b2k_`, `b3k_` and K-11 filters.

The generator ran with VENV in scratch copies. The outputs are in `addendum_01/`, with paths shown as placeholders. My scratch is kept.
