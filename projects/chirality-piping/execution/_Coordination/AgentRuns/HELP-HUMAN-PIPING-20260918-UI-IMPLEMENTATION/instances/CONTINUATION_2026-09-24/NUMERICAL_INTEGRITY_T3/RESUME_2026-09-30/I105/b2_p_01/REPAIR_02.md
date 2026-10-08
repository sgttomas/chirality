# I105 lane P: B2-P repair 02 (RV123's RV-P2 round 2)

TASK (Type 2), I105, for ROOT. 2026-10-08 UTC. Basis: RV123's round-2 review of B2-P, `R/REVIEW_RV123/b2_p_01/REVIEW.md` (`616828f7…`; it passed B2-P with 0 blocking, 1 should-fix and 4 notes), and ROOT's routing of it. This repair is test-only, plus one `cfg(test)` hook.

## Head (`WT/b2`, `codex/piping-t3-b2-20261008`; not pushed)

**`cf607a02cd`** is one commit on top of `72b3e5d9ea`. It changes `retained_facade_tests.rs`, plus the hook in `lib.rs`, `grant2.rs` and `retained_product.rs` (`cfg(test)` only).

## What changed

- **S-1 (required), the `ledger_unavailable` operand branch** (B2-C §2.4 (i), row 2):
  - **New hook `refuse_ledger_of_case(index)`** (`grant2.rs`, consumed in `native_call`; `cfg(test)`). After the batch Call, it replaces that case's Run outcome with `Refused { LedgerUnavailable(Accumulator(NonFinite)) }`. It keeps the Run's attempt records, so the Run's records and work still conserve.
  - **Why a hook is needed:** the real refusal cannot be reached through valid input. FK's `PrimitiveSource::new` rejects non-finite loads, and the exact accumulator refuses only non-finite terms.
  - **New test `b2p_ledger_unavailable_operand_has_no_source`** (both modes, `b2p_two_cases` with case 1 refused). It asserts:
    - case 1 is `unavailable` (`kernel_refused`), with its CaseSource, and its Run's terminal is `refused`, `ledger_unavailable`, `accumulator`, `non_finite`;
    - the combination is `retained_unavailable`, `combination_unresolved`, `preparation`, `operand_source_unavailable`, operand 1;
    - there is no Call, Run, source or attempt;
    - there is one Call (the batch) and two sources, so no rebuilt or prepared registration;
    - `operand_preparations` is absent.
- **N-3 (optional, taken): two in-domain shapes, pinned in both modes.** Both go through the witnesses' checks (`b2p_pin_witnesses`: B2-C's producer requirements, today's precommit G0, T-12's notices, the base readers) and the Direct entry (`b2p_direct`). The test is `b2p_rv123_n3_shapes_are_pinned`.
  - **`rv123_w_cb3_ba` (B + A):** operand 0, the representative, is the `not_required` case B, operand-prepared. The CombinationSource's representative is the preparation's source, and the preparation is owned by case 1.
  - **`rv123_c1_two_mechanics` ([2·case, −3·case]):**
    - there are three Calls, owned by the batch case, combination 0 and combination 1;
    - −3·case is `retained_unavailable` with `facade_certificate` (phase `facade`) after its own Run, with no hook involved.

## Pins (receipt; successor bytes)

| Shape | Sparse | Dense |
|---|---|---|
| `rv123_w_cb3_ba` | `86d0f1f8…`; `ec58bcab…` | `03a8eec6…`; `6149647c…` |
| `rv123_c1_two_mechanics` | `577b1fcb…`; `167eb711…` | `b2a8db32…`; `e5ad415d…` |

**Each successor's bytes equal RV123's own independent dump** (`R/REVIEW_RV123/b2_p_01/evidence/results/dump2_lines.txt`), all four. Every existing pin is unchanged.

## Mutant

M2-03 is RV123's own exact edit: the `ledger_unavailable` test becomes `if false`. On a scratch archive of `cf607a02cd`, **it is killed** by `b2p_ledger_unavailable_operand_has_no_source` (`_run_records/repair_02/mutants/`). RV123 reported M2-03 surviving the whole PP lib suite at `638214d8d8`.

## Suites, test by test against `72b3e5d9ea` (`_run_records/repair_02/suites/`)

| Suite | `72b3e5d9ea` | `cf607a02cd` |
|---|---|---|
| PP, all targets (registered) | 789 ok, 1 failed (t13), 11 ignored | 791 ok, 1 failed (t13), 11 ignored |
| Runner (all tests) | 85 ok, 2 failed (load-reference) | identical |

- **PP test by test:** 2 tests added, both ok (`b2p_ledger_unavailable_operand_has_no_source`, `b2p_rv123_n3_shapes_are_pinned`); 0 changed; 0 removed.
- **The failures are the base's own:** PP's `t13` and the runner's two load-reference tests.

## Platform (RV123 N-1, for the record)

The W-CB pins and both fixtures are Mac bytes, and they carry ordinary combination and case magnitudes formed by libm `hypot`. Per ROOT, the Linux CI run is the check, and `b2` re-pins at J0 once main carries B1 and PR-N.

## Host and records

- Cargo jobs ran through `t3_cargo.sh --locked --offline` on `i105-b2-p-*` targets. They queued behind ROOT's DEC-025, and I signalled nothing. One heavy job of mine ran at a time, with one wait each.
- Records use placeholder paths only, with no symlink and no folder named `build`. The host screen of `72b3e5d9ea..cf607a02cd` (4 files) and of these records found 0 hits.
