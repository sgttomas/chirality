# RV123 (RV-P2, round 2): B2-P, combinations (lane P, Part 2)

TASK (Type 2), RV123, independent reviewer for ROOT (HELP_HUMAN, Agent 0), the return path. I wrote none of this change and delegated nothing. 2026-10-08 UTC.

**Candidate:** `codex/piping-t3-b2-20261008` at `72b3e5d9ea`. Byte and suite base: `a09e24b44c`. Reviewed commits: `794cb36e85`, `1032fc8357`, `384c9a1ed8`, `638214d8d8` and `72b3e5d9ea`, plus the effect of lane A's merge `583fc758ee`. Every copy is a `git archive` under `WT/rv123/` (`cand`, `base`, `chk`, `chkb`, `mut`). I did not touch `WT/b2`.

**Basis** (sha256 prefixes):
- `R/BRIEFS/B2_P_LANE.md` `525e5cd8`, Part 2;
- B2-C `R/I97/b2_c_01/`: CONTRACT `165cd4b1`, REVISION_01 `6f6a583f`, REVISION_02 `79007dcd`;
- `R/I102/b2_k_01/RETURN.md` `0d538ca1`;
- the three RR B2-C entries named in the dispatch.

I read I105's RETURN (`cd33b9b9`; its SHA256SUMS all verify OK) after forming my view.

**Host:** every cargo job went through `WT/tools/t3_cargo.sh` (`--locked --offline`), with targets under `WT/targets/rv123-r2-*`. One heavy job ran at a time. No Git writes, no DEC-025, no measurements.

**Placeholders:** WT, NUM, P, PP, FK and R are as dispatched. S is `WT/scratch/rv123_rvp2/r2`. E is this folder's `evidence/`.

## Verdict

**PASS, with 0 BLOCKING, 1 SHOULD-FIX and 4 NOTE.**

I found no correctness defect in the shipped producer:
- By reading, every B2-C item in the dispatch is implemented as specified (§2).
- On each of the 22 successors I dumped, an independent check outside PP recomputes all hashes and verifies identities and orders (§3). The 22 are the 16 witness documents plus 3 probes in both modes.
- Byte identity holds.

## 1. Round-1 items: closed

**S-1, S-2 and N-2 are closed.**
- Their four pins are present and pass:
  - `b3b_rv123_s1_two_member_exact_overlays_each_member`;
  - `b3b_rv123_s2_unavailable_exact_case_binds_def_e`;
  - `b3b_rv123_s2_one_case_unavailable_exact_serializer`;
  - `b3b_rv123_n2_unused_exact_material_is_not_checked`.
- They pass both in the registered candidate run and in the mutant control.
- My round-1 mutants R-01, R-02, R-03, R-06 and R-11 are each killed by one of them (`E/results/mutants.out`).
- `fail_freeze_of_case` is `cfg(test)` only.

## 2. B2-P against B2-C (reading `PP/src/{lib,retained_product,retained_wire}.rs`)

**Domain and gates:**
- **T-2′ and T-4:** `capture_combinations` records ids, the mechanics flag and term indices. `w1_combinations_admitted` re-checks D1.4: z ≤ 2, C_eq ≤ 3, h ≤ 3, range operands ≤ 3, and disjoint ids.
- **T-6′:** case blocks end at the first combination row, at c = 1 too. Mechanics runs are contiguous. Subtraction and range rows bind by id (REVISION_01 S-2).
- **T-8′:** the capacity is `for_invocation(&[n], h…, p)` over open, distinct mechanics combinations with a term in the batch. Retained combinations are a subset of that set, so these maxima bound the actual Calls and registrations.
- **T-9′:** only the gate shape and consistency are checked; a withheld entry is not a freeze failure.

**T-9b and T-9c (B2-C's T-10a and T-10b):**
- **Dispositions:** withheld gives `base_withheld`. Mechanics with distinct terms and a frozen term gives retained. Everything else is ordinary.
- **Operand sources:**
  - frozen gives `Selected`;
  - no CaseSource, or a Run refused `ledger_unavailable`, gives `operand_source_unavailable`;
  - any other unavailable case is rebuilt once at its batch source id;
  - a case outside A gets an operand preparation.
- **C3a operand preparations:** the owners are taken in first-need order, and `requested_by` lists the retained combinations naming each owner. A refusal is kept as a record with no source.
- **Calls:**
  - a pre-source refusal gives `retained_unavailable` with its Call;
  - an origin refusal or error abandons the successor (`CombinationCustody`, N-5);
  - an unselected Run gives `combination_unresolved` with phase `kernel`;
  - a selected Run is frozen on operand 0's slot with the results swapped (REVISION_01 N-9).
- **The freeze:** proof, then B2-K's projection (option (ii)), empty maxima and aliases, the certificate, the observables stage (the gate entry, no maximum or intensified row, supports, and the 64ε displacement guard), then G5a.

**Staging and receipt:**
- **Staging:** there is one overlay per frozen combination on its own block. Headlines come from load-case rows only.
- **R-COMB-1 (producer side):** unavailable and ordinary combination rows keep their ordinary values, with no `recovery_method`.
- **The wire:**
  - `combinations[]`;
  - `operand_preparations[]`, absent when empty (C-6);
  - the operand-prepared CaseSource hash, with purpose `combination_operand`;
  - `CombinationSource`: K4CMB, ledger, stiffness, representative operand 0, and operand identities;
  - the mechanics Call, with Group imports from selected operands only;
  - `execution_order` and `owner_refs` through `OwnerMap`, with batch ordinal → request and `Combination(k)` → authored index;
  - the meter chain;
  - the reason mapping.
- **NA4-5:** I105's statement is accurate.
  - Retained combination displacement magnitudes are RN64 of the exact 3-norm.
  - Ordinary ones are nested `hypot`.
  - Example: on my probe, `-3·case` is unavailable, so its rows keep their ordinary values. Its N1 ordinary magnitude is 1 ulp from the exact-norm value.

## 3. Evidence

**Byte identity** (`E/results/bytes_compare.txt`), over 37 inputs × 2 modes:
- Plain bytes: base equals candidate for every input.
- Direct bytes: base equals candidate for all 33 non-combination inputs. These include the c = 1 successors, the B1 multi-case cases and coexistence (`ps_*`).
- The 4 combination inputs (I98's R-7) now publish the plain bytes plus T-12's notices exactly. Today that is a G0 refusal, as designed.

**Suites** (`E/results/suite_*.txt`):
- **PP registered:** base 776 tests, candidate 800 (788 ok, 11 ignored).
  - The +25 are the added `b2p_*` and RV123 pins.
  - One removal is lane A's interim test, re-pinned per ROOT's ruling.
- **PP stale:** 613 → 637.
- **Runner:** identical (85 ok and the same 2 load-reference failures on both sides).
- **FK dependents:** compile.
- **The only failure:** the pre-existing `t13_committed_fallback_uz_is_byte_identical`, on both sides.

**Pins and fixtures:**
- The W-CB inputs equal I98's `r7_cb1_halfb`, `r7_cb1`, `r7_cb2` and `r7_cb3_v1`.
- The two new fixtures equal my dumped W-CB3 successors: both `source` and `invocation`.
- Dumps are reproducible: two independent dump runs gave identical bytes for every common witness.

**Independent checks** (`E/tools/b2p_checks.py`, outside PP; `E/results/b2p_checks_dump2.txt`): **0 failures** on 22 successors. The checks:
- SCHEMA;
- the receipt and publication hashes (RFC 8785);
- the DEF-O case-preparation hash;
- the operand-preparation hash and its source binding;
- source identities and `CombinationSource` operand identities;
- representative, ledger, stiffness and run owner;
- call ids and kinds, the meter chain, `charged` and `execution_order`;
- the attempt order, and the source order: batch, then operand-prepared, then combination;
- `requested_by`;
- C-6;
- the diagnostics order;
- R-COMB-1 values and `recovery_method`;
- headlines;
- exact-norm magnitudes;
- linear consistency of selected combinations (worst 0);
- W-CB1z's exact zeros.

**My probes** (scratch tests in `E/results/scratch_tests.diff`):
- **W-CB3 with its terms reversed (B + A, and B + 0.5·A):** operand 0 is the operand-prepared `not_required` case, and both select. This is the freeze on a prepared slot, which no pin covers.
- **c = 1 with `[2·case, −3·case]`:** an in-domain shape per REVISION_02 A-6, not pinned.
  - It makes three Calls with the meter chained 0 → 2377759 → 3947390 → 5516353, and `execution_order` is case, combination 0, combination 1.
  - `−3·case` refuses its own certificate (`sharper_exact`, row 7) with no hook. It is recorded `facade_certificate` and its rows keep their ordinary values.

All pass every check.

**Probe disclosure.** My first dump compiled before I added `provenance` to the last probe. That probe then fell back at custody with `Preparation`: the ordinary run emits `PROVENANCE_INPUT_MISSING`, which is B1's existing behaviour (`probe6`). The second dump has the corrected probe.

**Mutants:**
- I105's P2-22 and P2-36 are equivalent (N-2).
- My own 6 B2-P mutants: 5 killed, and M2-03 survived (S-1).
- The full mutant results are in `E/results/mutants.out`.

## 4. Findings

**S-1 (SHOULD-FIX): the `ledger_unavailable` operand branch is unpinned.**
- The rule: B2-C §2.4 (i), row 2, and the G5 rule keyed on `ledger_unavailable`. A term whose batch Run refused `ledger_unavailable` makes the combination `operand_source_unavailable`, with no rebuild, no preparation and no Call.
- The code at `retained_product.rs` `combine_on` is correct by reading.
- Mutant M2-03 replaces that test with `if false`. It survives the whole PP lib suite: 626 passed, and only the pre-existing t13 failed (`E/logs/m203_full.txt`).
- Without the branch, the operand would be rebuilt from a prep the kernel already refused. The result would be an abandonment or a different reason, not the contract's record.
- **Fix:** add a test-only hook that makes an attempted case's batch Run refuse `ledger_unavailable` (for example, by replacing its outcome after the Call). Assert the record and that there is no Call, as `b2p_hooks_and_failure_set` does for the no-CaseSource case.

**N-1 (NOTE, platform): libm-formed values in the new pins.**
- **The libm call sites:**
  - Retained support force and moment magnitudes come from FK's `support_hypot`, which calls `f64::hypot` (`final_case.rs` 1875, 1878).
  - Ordinary combination support magnitudes use `hypot` at `preview_physics.rs` 966–967.
  - Ordinary combination displacement magnitudes use it at `lib.rs` 13620.
  - Case support magnitudes use it at `lib.rs` 11985 and 11991.
- **What the new artifacts carry:** the W-CB pins and both fixtures are Mac bytes and carry all of these values.
- **Margins** (`E/results/libm_split_dump2.txt`):
  - Every retained support magnitude equals the correctly rounded nested hypot, each step at least 0.316 ulp from a rounding midpoint. Any hypot with error below 0.8 ulp agrees.
  - Ordinary combination rows are as close as 0.030 ulp to a midpoint, and three are not the CR value. These formations are pre-existing, but the new pins now capture them.
- **Platform-independent:** combination displacement magnitudes (exact norm).
- **Not reached by B2-P's tests:** `cap_maximal`'s `cos`/`sin`. `b2` lacks NUM's CAP_MAXIMAL_RING fix (J0).
- **Recommendation:** treat the required Linux CI run as the check. If a W-CB pin differs there, look at `hypot` before anything else.

**N-2 (NOTE): P2-22 and P2-36 are equivalent, as I105 argues.**
- **P2-22:** terms are captured only for mechanics combinations, so the conjunct is implied.
- **P2-36:** `OwnerMap::case`'s prepared-ordinal branch is unreachable. `owner()` is applied only to Call owners and Run owners, and a prepared registration adds a source, never a Call or Run. Without the branch, an unknown owner still fails closed (Association). Keep it as defensive or drop it; either is harmless.

**N-3 (NOTE): two in-domain shapes are unpinned.**
- A `not_required` representative (operand 0 operand-prepared), and c = 1 with two mechanics combinations (three Calls).
- Both behave correctly on my probes.
- `[2·case, −3·case]` also gives a natural, unhooked `facade_certificate` witness. Optional pins.

**N-4 (NOTE): SQ2.** I105's "For SQ2" list matches the code as I read it.
- One item to price explicitly: `combination_observables` is quadratic.
  - For each node it filters the whole block four times (x, y, z and the magnitude).
  - That is about 4 × nodes × block rows adapter events per selected combination.
  - S1's stack witnesses do not cover the combination freeze on the reserved stack.

## 5. For ROOT

- **S-1:** route a test-only pin to lane P. It is not merge-blocking under my verdict, but the brief's "one mutant per new check, each killed" is not met for this branch.
- **N-1:** confirm that the Linux CI run of the `b2p_*` pins is the platform check, or schedule one before relying on the Mac pin bytes.
- **N-4:** carry the observables stage's quadratic cost to SQ2's brief.
- **Nothing else needs a ruling.**
