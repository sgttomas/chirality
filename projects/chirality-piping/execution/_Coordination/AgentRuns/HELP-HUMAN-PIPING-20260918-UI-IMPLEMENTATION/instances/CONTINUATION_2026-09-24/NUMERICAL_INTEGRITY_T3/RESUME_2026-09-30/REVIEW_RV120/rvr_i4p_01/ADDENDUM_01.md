# RV120 (RV-R), addendum 01: PY's follow-up confirmed; the three readers agree at I4′'s heads

TASK (Type 2), RV120, for ROOT (HELP_HUMAN, Agent 0). No delegation; I wrote none of the change. 2026-10-08 UTC.

## Basis

- **The request:** ROOT's message: confirm PY (brief items 2 and 6, and PY's part of 1, 3, 7, 8 and 9), then the three-reader agreement at RS `e879118348`, PY `52d83da275`, TS `819e44f63e`; probe I100's two PY-only notes if cheap. ROOT's rulings in that message: 07n pins gate and code for the two extrema shapes, with their details declared per reader (my N-1); N-2 goes to PR-B1's complete-diff reviewer.
- **The candidate:** `codex/piping-t3-b1-p-20261007` at `52d83da275` (`8fa5aac15c`; `52d83da275`, docstring only) over I4: `compatibility.py` +18/−6, `preview_physics_evidence.py` +15/−4, `retained_precision.py` +13/−10, `tests/test_retained_precision_contract.py` +143/−0.
- **Copies:** `git archive` copies of P without `execution/` (plus PKG-15's folder, which a retained test reads, as RV113 made them) at I4, at the head, and a mutant copy (`addendum_01/static/copies_py.txt`). The three authority binaries are my builds from I4 (`WT/targets/rv120-pybins`), byte-equal to RV113's and I91's (`static/py_binaries.sha256`).
- **Order:** the code and my runs first; I100's RETURN (`R/I100/b1_i4p_py_01/RETURN.md`, sha256 `c877ddd9…9239e`, verified) after my census, probes and agreement.
- **Placeholders** as in REVIEW.md; PY = `P/core/analysis_runs/` (`retained_precision.py`, `compatibility.py`, `preview_physics_evidence.py`).

## Verdict

**PY `52d83da275`: CONFIRMED.** With RS and TS (REVIEW.md), the three readers agree at I4′'s heads, except the declared raw G7 codes.

## Brief items, PY

| # | Item | Result |
|---|---|---|
| 1 | Census over 07m, I4 → head | 339 entries: **0 changes** on bound, unbound and transport, details included; 0 misses against `expected_by_reader.python` at I4 and head. PY at I4 is byte-equal to RV113's census at `2843a59a16` |
| 2 | Ruling 1 | RV113's six transport probes now give RS's and TS's gate and code (table below); their raw verdicts are unchanged (PY's raw G7 codes, the declared class). The order is Rust's only on the retained transport step (`_transport_base` passes `rust_header_order=True`); every other caller reads as before |
| 3 | Ruling 2 | On transport PY refuses `t_withheld_duplicate_multiset` (admitted at I4), and still refuses the two extrema shapes, each at G7 `…EVIDENCE_INVALID`. My multiplicity probes: case 1 twice against case 0 once, and 3 against 2, refused; equal multiplicities (2 and 2) and a single record admitted, as RS and TS. Raw verdicts unchanged |
| 3 | Callers | `validate_transport_metadata` is reached through `_source_contract(…, check_receipt=False)` for a preview-physics-1 statement: the retained transport step, and `core/handoff/stress_neutral/package_v0_3.py` (the v0.3 stress-neutral packager's transport statement). The multiset change reaches both identically. On producer-emittable inputs nothing changes: a withheld support repeated within a case is refused by every raw read, and the producer withholds each support once |
| 6 | Ruling 5 | `test_i4p_ruling5_…` exists and pins G5 `ATTEMPT_MISMATCH` with no cause, bound and unbound, on RV113's `r2:cb_kernel_no_run`; all three readers give G5 ATTEMPT there. **RV113's P31 is killed by it** at its assertion (the reader-logic test also fails, by a `TypeError`, as RV113 found) |
| 8 | pytest vs I4, test by test | The three retained files (contract, carriers, schema): 528 → 531 passed, **+3 added** (`test_i4p_ruling1_…`, `…ruling2_…`, `…ruling5_…`), 0 removed, 0 changed |
| 9 | Mutants | **My 5 killed at assertions:** the carrier branch kept on the retained transport (Q01), recovery not first (Q02), Rust's order on every caller (Q03), sets again on transport (Q04), multiplicity lost (Q05). Of RV113's PY schema, the three on the touched checks: P31 (above), P35 and P36 (the transport gate mapping) killed at assertions. Control 473 of 473. RV113's other 37 were killed at `2843a59a16` by tests unchanged at the head (+143/−0) |

**Ruling 1's six probes, transport:**

| Probe | PY at I4 | PY, RS and TS at the heads |
|---|---|---|
| `h_carrier_present` | G2 `SOURCE_PRODUCER_CONTRACT_UNSUPPORTED` | G7 `SOURCE_PREVIEW_PHYSICS_EVIDENCE_INVALID` |
| `h_carrier_and_quality_defect` | G2 `…PRODUCER_CONTRACT_UNSUPPORTED` | G2 `SOURCE_NUMERICAL_QUALITY_INVALID` |
| `h_carrier_and_recovery` | G2 `…PRODUCER_CONTRACT_UNSUPPORTED` | G2 `SOURCE_BLOCKS_LEGACY_DOWNGRADE_FORBIDDEN` |
| `n6_carrier_evidence_with_case_defect` | G2 `…PRODUCER_CONTRACT_UNSUPPORTED` | G2 `SOURCE_NUMERICAL_CASE_INVALID` |
| `h_recovery_and_evidence_null` | G2 `SOURCE_PREVIEW_PHYSICS_EVIDENCE_REQUIRED` | G2 `SOURCE_BLOCKS_LEGACY_DOWNGRADE_FORBIDDEN` |
| `n6_contract_evidence_null_and_source_block_recovery` | G2 `…EVIDENCE_REQUIRED` | G2 `SOURCE_BLOCKS_LEGACY_DOWNGRADE_FORBIDDEN` |

**PY's probe changes, I4 → head** (435 probes, every verdict in full): exactly 9, all on transport: the six above and three withheld-multiplicity probes (`t_withheld_duplicate_multiset` and my two). No raw verdict or detail changed. 471 stated expectations: 0 misses.

## Item 7: the three readers at I4′'s heads

| Pair | 435 probes × 3 verdicts | 07m, 339 × 3 |
|---|---|---|
| TS ~ PY | **equal on all 1,305** | equal on all 1,017 |
| RS ~ TS, RS ~ PY | equal on 1,149; **78 probes differ only by RS's raw G7 code** (both refusing at G7, bound and unbound); **0 other differences** | equal on 1,015; entry 139 `g7_maximum_off_enclosure`'s declared raw code |

So transport agrees in all three readers on every probe and entry. The only other differences are raw G7 codes, all of the declared class (B1_SC item 13 as ruling 3 states it): RS's specific raw codes against PY's and TS's `…EVIDENCE_INVALID`.

**Details, for SC.** Gate and code agree; transport detail texts do not, beyond the two extrema shapes ROOT has declared: on 54 transport refusals PY's detail differs from TS's (and RS's), because PY's schema walk of `contract_evidence` refuses first ("transport evidence shape", 49) or because PY words the multiset demand differently ("support attribution differs between cases", 5). If 07n pins transport details anywhere in the metadata check, they need per-reader details too.

## I100's two notes (quick probes)

| Probe (`ordinary_prepared_synthetic`) | RS | TS | PY |
|---|---|---|---|
| 16,384 combination gates (rehashed) | admitted every path | admitted every path | admitted every path |
| **16,385 gates** | admitted every path | admitted every path | **transport G7 `…EVIDENCE_INVALID`** ("transport evidence shape"); raw admitted |
| span_index 2⁵³−1, set after rehash | transport admitted; raw G1 | the same | the same |
| **span_index 2⁵³, 2⁵³+1, 2⁶⁰**, set after rehash | transport **G7** `…EVIDENCE_INVALID` "extrema integers"; raw G1 | transport **G1** `RETAINED_PRECISION_RECEIPT_MISMATCH`; raw G1 | **transport admitted**; raw G1 |

- **The array bound: confirmed** as I100 reads it.
- **The unsafe span_index: confirmed** that PY admits it on transport and RS and TS refuse it, **with one correction:** TS refuses it at **G1**, not by `Number.isSafeInteger` at G7. TS's `snapshot` runs `checkedJsonText` over the whole statement first, and an unsafe integral number fails it. So the three readers differ in gate as well (RS G7, TS G1, PY admitted). Reachable only by a statement whose publication hash no longer matches (checked JSON cannot hash it), and only on transport.

## Findings

| # | Severity | Finding |
|---|---|---|
| A-N1 | NOTE (for SC) | Transport detail texts differ PY against RS and TS on 54 metadata refusals (PY's schema walk first, and the multiset wording), beyond the two extrema shapes already declared. Gate and code agree on all |
| A-N2 | NOTE (ROOT has these as unpinned, no change now) | I100's two PY-only transport differences reproduce: PY refuses an array over 16,384 items; PY admits an unsafe integral `span_index`, which RS refuses at G7 and TS at **G1** (not G7, as I100 read it) |

No BLOCKING or SHOULD-FIX finding.

## Against I100's RETURN

Agrees on every count I can compare: 0 census changes; the 7 RV113-probe changes (my 9 add my 2 multiplicity probes); RV113's 430 stated expectations met; 0 other differences beyond the declared raw class and the two shapes I101 aligned (now aligned: my three-head comparison shows 0); +3 tests; P31 killed by the ruling-5 row; the two notes, with the TS gate correction above.

## Host

- **Cargo,** 2 jobs through `WT/tools/t3_cargo.sh` (`--locked --offline --release`): the authority binaries.
- **Slot jobs,** one at a time: PY census and probes at I4 and head; the three retained test files at I4 and head (junit, host attribute removed in the record); the note probes on RS (four files: RS's harness stops at an unhashable statement), TS and PY; the PY mutants.
- **Waits:** one chain, one waiter (its completion); single progress reads only. None of mine remain. No other job signalled.
- **Not done:** no DEC-025, installs or Git writes.
- **Kept for SC:** `WT/scratch/rv120_rvr/` and the targets `WT/targets/rv120-{rs-i4,rs-head,rs-mut,pybins}`.

## Records (`addendum_01/`)

Placeholder paths only; no symlink; no folder named `build`; junit host attributes removed; screened with `WT/tools/t3_host_screen.py`'s patterns, `.gz` decompressed. `SHA256SUMS.addendum_01` covers this file and `addendum_01/`.
- `harness/`, `static/`, `census/` (PY at I4 and head; `PY_CENSUS_07M.json`; `CROSS_3_CENSUS_HEADS.json`), `probes/` (PY at I4 and head; `PY_PROBES_I4_HEAD.json`; `CROSS_3_HEADS.json`; `x/`: the note probes and the three readers' outputs), `suites/` (junit at I4 and head; `PY_SUITE_COMPARE.json`), `mutants/` (manifests, `MUTANT_TABLE_PY.json`, `py_runs/`), `host/job_stamps.txt`.
