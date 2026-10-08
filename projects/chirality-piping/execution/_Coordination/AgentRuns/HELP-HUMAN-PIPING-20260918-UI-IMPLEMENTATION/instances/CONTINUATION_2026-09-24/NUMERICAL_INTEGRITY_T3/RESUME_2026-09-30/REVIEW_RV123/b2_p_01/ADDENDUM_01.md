# RV123 (RV-P2, round 2), addendum 01: B2-P repair 02

TASK (Type 2), RV123. Return path: WORKING_ITEMS for T3 (Agent 1), by the owner's decision of 2026-10-08. 2026-10-08 UTC. This addendum extends `REVIEW.md` (`616828f7…`) and leaves it and its `SHA256SUMS` unchanged. Its own checksums are in `SHA256SUMS.addendum_01`.

**Repair:** `b2` at `cf607a02cd`, one commit on `72b3e5d9ea`. I read it from NUM's objects into a `git archive` copy (`WT/rv123/rep2`, with a mutant copy `WT/rv123/rep2m`), not from `WT/b2`. `REPAIR_02.md` says "not pushed", but the dispatch says pushed; the commit is the same either way.

**I105's record:** `R/I105/b2_p_01/REPAIR_02.md` (`0b81d363…`). Its SHA256SUMS verifies 227 of 227.

**Host:** cargo went through `WT/tools/t3_cargo.sh` (`--locked --offline`), with targets `WT/targets/rv123-r2-rep2*` and `rv123-r2-runner-rep2`, one heavy job at a time. I signalled nothing. No Git writes.

**Placeholders:** as in `REVIEW.md`. E is `evidence/addendum_01/`.

## Verdict

**S-1 and N-3 are closed. The repair adds 0 BLOCKING, 0 SHOULD-FIX and 2 NOTE. B2-P's verdict stays PASS.**

## Scope of the change

The diff `72b3e5d9ea..cf607a02cd` touches 4 files and nothing else differs between the copies. Every non-test line is inside `cfg(test)`:
- **`lib.rs`:** a field in the `cfg(test)` module `retained_tests_hooks`.
- **`grant2.rs`:** `refuse_ledger_of_case` and `after_batch_run`.
- **`retained_product.rs` `native_call`:** a `#[cfg(test)]` call to `after_batch_run` before each submitted case's Run is stored.
- **`retained_facade_tests.rs`:** the two new tests.

No existing pin changed. `B2P_PINNED` only gains 4 entries, and `b2p_attempted` and `b2p_dispositions` gain the new names.

## S-1: closed

- **The test passes:** `b2p_ledger_unavailable_operand_has_no_source` passes in both modes in the registered run.
- **It kills M2-03.** On `rep2m`, with my exact M2-03 edit, the test fails (`E/logs/rep2_m203.txt`).
  - It fails at its first mode (sparse) with the combination `retained_selected`, where it expects `retained_unavailable` / `operand_source_unavailable`.
  - The branch under test does not depend on the mode.
  - `b2p_hooks_and_failure_set` and the N-3 test still pass on the mutant.

**Is the hook a faithful stand-in?** For the decision under test, yes. `combine_on` reads only the refusal kind in the case's Run outcome, and the hook sets exactly that, through the same path a real refusal takes: `native()` makes the attempt `Native`, and the case becomes `unavailable` (`kernel_refused`). The test asserts only fields that follow from that decision:
- the combination record;
- no Call, Run, source or attempt;
- one Call and two sources;
- no `operand_preparations`;
- the case's status, CaseSource, reason and terminal.

Its Run is not a byte-faithful real refusal, though (A-N1).

**Is a real refusal reachable? I agree with I105 that it is not.** The checks:
- **NonFinite:** `PrimitiveSource::new` refuses non-finite load values (`FK/structural/retained/source.rs` 598) before any ledger exists.
- **The case ledger can raise nothing else in practice.** `RetainedLedger::from_source` uses only `ExactAccumulator::add`, which can raise:
  - `NonFinite` (excluded above);
  - `AccumulatorOverflow`, which needs a carry out of 68 limbs at quantum 2⁻²¹⁴⁸, about 2¹¹⁸⁰ maximal terms.
- **`NonRepresentable`** arises only when rounding to binary64, and `from_source` does not round.
- **The batch's only `LedgerUnavailable` source** is `CasePrep::new` (`FK/structural/retained/adaptive.rs` 5082–5087).

## N-3: closed

`b2p_rv123_n3_shapes_are_pinned` passes in both modes. It runs:
- `b2p_pin_witnesses` and `b2p_direct` over `rv123_w_cb3_ba` (B + A) and `rv123_c1_two_mechanics` ([2·case, −3·case]);
- the representative assertion and the three-Call / `facade_certificate` assertions.

The four new `B2P_PINNED` entries equal my independent dump (`R/REVIEW_RV123/b2_p_01/evidence/results/dump2_lines.txt`, my own harness at `72b3e5d9ea`):
- **Receipt sha256:** `86d0f1f8…`, `03a8eec6…`, `577b1fcb…`, `b2a8db32…`, recomputed from my dumped successors.
- **Successor-bytes sha256:** `ec58bcab…`, `6149647c…`, `167eb711…`, `e5ad415d…`.

## No other pin moved (`E/results/suite_rep2_*.txt`)

- **PP registered, test by test against `72b3e5d9ea`:** 2 tests added, both ok. 0 changed, 0 removed. The one failure is the pre-existing t13, on both sides.
  - My parser counts 788 → 790 ok per unique test. Summing the `test result` lines gives 789 → 791, as I105 reports.
- **Runner:** identical (85 ok, the same 2 load-reference failures).

## Findings (new)

**A-N1 (NOTE): the hook's Run is not a real refused Run.** A real `ledger_unavailable` Run is `CoreRun::idle`:
- no attempts, no solve charge;
- phase `SourcePreparation`;
- the group's geometry;
- no kernel prep to rebuild.

The hook keeps the selected Run's attempts and work, sets empty geometry, and leaves the invocation's records as they were. Under M2-03 this shows: the hooked case's prep rebuilds and the combination selects. A real refusal would make the rebuild refuse, which is a whole-successor abandonment (`CombinationCustody`, B2-C §2.6). So:
- the pin is right to assert only the decision, not the case record's bytes or work;
- nothing should be byte-pinned from this hooked successor;
- a real refusal is unreachable anyway.

**A-N2 (NOTE): one sentence in `REPAIR_02.md` is narrower than the argument.** It says the accumulator "refuses only non-finite terms". In fact `add` can also raise `AccumulatorOverflow`, though only past about 2¹¹⁸⁰ terms. The conclusion stands. No action needed.

## For the return path

- **Nothing needs a ruling.** S-1 and N-3 are closed.
- **Round 2's remaining notes are unchanged:**
  - N-1, platform: per ROOT, the Linux CI run is the check.
  - N-2: equivalent mutants.
  - N-4: SQ2 pricing of the quadratic observables stage.
