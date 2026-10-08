# RV113 (RV-R), addendum 01 to the SR-PY review: confirmation of SR-PY repair 02 (the three-reader alignment set, PY's side, with item 4)

TASK (Type 2), RV113, for ROOT (HELP_HUMAN, Agent 0), who is the return path. I made no delegation and wrote none of the change. 2026-10-08 UTC.

## Basis

- **The request:** the coordinator's message. Confirm I91's SR-PY repair 02, including item 4, against the alignment set (RR "RV113's three returns verified; …", items 1–4) and RR "I91's and I92's rounds verified; the header move's nine transport changes ruled in; …". Confirm:
  1. each item's change against the ruling:
     - (f) at G3, with the basis reference at G5;
     - (g) at G8;
     - the C2 table, with the `precondition` keying, at G5;
     - the header at G2, with the metadata at G7;
     - also S-4 (Q17's row), N-1, N-2, and S-2's correction in REPAIR_02 §6;
  2. the census over 07m against R01 on my own harness: exactly the nine ruled transport changes, 0 others on any verdict, 0 misses;
  3. my probes: PY against TS's and RS's present heads (TS `6fa6a64658`, RS `6e3e4fe219`), with any remaining difference named and checked against the declared ones;
  4. the mutants, including the F-src-kind survivor. I91 says it is unreachable, because the schema fixes `CaseSource.owner.kind` to `"case"` and G1 refuses first. Confirm or refute.
- **I91's records** (`R/I91/b1_sr_py_01/`), each verified with its sums:
  - `REPAIR_02.md`, sha256 `f7e503483f4283f91ed092317829e4c934dcc45622b3caaaf5dffbafddb87506` (SHA256SUMS.repair_02, 56 of 56 OK);
  - `REPAIR_02_ITEM4.md`, `06a724946c3b181e4afb06c72f31a4a10ac7b41db6bcb24d33a9efd7aadcd95e` (SHA256SUMS.repair_02_item4, 41 of 41 OK).
- **The candidate:** `codex/piping-t3-b1-p-20261007` at `2843a59a16fabb76a8e55cabdb2133b0a3c0ec5f`, the branch tip in `WT/b1-p` (clean). It is four commits over R01 `11cc14e3e6`:
  - `a721e58483`: items 1–3, with the S-4 and N-2 tests;
  - `5f267db91d`: N-1, the transport docstring;
  - `70d4a68bd7`: a source owner out of range is G3's own refusal (D16);
  - `2843a59a16`: item 4, the header at G2.

  R01..HEAD touches exactly `retained_precision.py` (+58/−13) and the two retained test files (contract +247/−7, carriers +40/−5). **The diff `70d4a68bd7..2843a59a16` is byte-identical to the held patch** (`item4_held.diff`, sha256 `357098ba93dfe3a3972477f83ede8c20eab4ad634807f36e1347b121a4d54682`). My archive copies' files equal `git show` (`static/copies.txt`).
- **Order of reading.** I read the ruling and the diff, then ran my census, probes, tests and mutants. I read I91's two records only after that.

**Placeholders** as in my SR-PY review: `R`, `WT`, `P`, `S` (my scratch). R01 is `11cc14e3e6`, my SR-PY review's head. TS is at `6fa6a64658` (my `rvr_sr_ts_01/ADDENDUM_01.md`), RS at `6e3e4fe219` (my `rvr_sr_rs_01/ADDENDUM_02.md`).

## CONFIRMED

**SR-PY repair 02, with item 4, is confirmed.** Each commit does what the ruling says:
- (f) at G3, with the basis reference at G5;
- (g) at G8;
- the C2 table, keyed by `precondition`, at G5;
- the header at G2, with the metadata at G7;
- S-4, N-1, N-2 and S-2's correction.

The evidence:
- **The census over 07m moves exactly the nine ruled transport verdicts.** PY now equals TS on all 1,017 verdicts, and RS on all but the declared entry.
- **On my 392 probes, every one of PY's 322 changed verdicts but two moved onto RS's and TS's.**
- **The two retained files: +7 tests, 0 changed.**
- **37 of my 40 mutants are killed by an assertion.** F-src-kind is unreachable, as I91 says; P18 is equivalent; and P31 is caught only by an error and by my probe.

**Findings: 0 blocking, 1 should-fix, 2 notes.**
- **S-1:** PY's transport header keeps Python's order. Six probes off the corpus read differently from RS and TS, which agree. One of them is at another gate. No declaration covers this. It does not touch 07m, and it needs ROOT's ruling.
- **N-1:** the metadata check's three shapes, a three-reader difference already before ROOT.
- **N-2:** P31's conjunct is pinned by no assertion.

## 1. Each item against the ruling

**By reading** (R01..HEAD, `retained_precision.py`):

| Item | The ruling | PY at `2843a59a16` | Tests |
|---|---|---|---|
| 1 (f) | the receipt's own references at G3 COVERAGE, bound and unbound | `_validate_draft`'s G3, for every source: `index` at its position; `owner.kind` `"case"`; `owner.case_index` integral and in range; and `owner.case_id` equal to that case's id. For every material basis: `index` at its position, and `case_indices` unique and in range. G8 keeps only the invocation's facts (it no longer checks the index, the owner kind or the owner's id) | `test_b1_repair02_receipt_references_at_g3_and_the_ordinary_basis_at_g5`, with D16's no-cause assertion for the out-of-range owner (`70d4a68bd7`) |
| 1 G5 | the ordinary attempt's basis reference at G5 ATTEMPT | `_g5_ordinary`: the basis must resolve and list its case (TS's `ordinaryAttempts` rule) | the same test; the repair-01 rows that this placement moves (below) |
| 2 (g) | no `reference_configurations` member, null included; `pressure_contract` absent or null; `combinations` and `components` absent or `[]`; G8 INVOCATION | `_g8`: `pressure_contract is None`, `combinations` and `components` `== []` by default, and `"reference_configurations" not in model` | `test_b1_repair02_model_scope_at_g8_invocation` |
| 3 C2 | the cause table at G5 ATTEMPT for every unavailable case whose cause is not `prepared_product_failure` | `_g5_ordinary`: the five branches as ruled; `RECEIPT_FAILURE_CODES` as a set; `PRECONDITION_CODES` keyed one to one by `precondition`; any other kind takes the kernel branch | `test_b1_repair02_c2_cause_table_reader_logic` (every branch satisfied, then single breaks) and `…_in_the_reader` (my six `c2_*` probes through the whole reader) |
| 4 | the header at G2 in every reader; the metadata at G7 | `_transport_base`: `_source_contract` on the projection, then the gate by code (`…EVIDENCE_INVALID` and the no-code fallback at G7, every other code at G2). Raw reads are unchanged | `test_repair02_transport_reports_the_header_at_g2_and_the_metadata_at_g7` (both modes); the RV108 N1 test's transport row now expects G2 |

**The rows whose expectation changed** (0 tests changed outcome). Each now reads as RS and TS do on my probes:
- the D38 test's receipt-failure row: G5 PRODUCT_ATTEMPT → G5 ATTEMPT (C2's receipt branch needs phase `receipt`);
- repair 01's (b)/(c) rows: three move from G8 PREPARATION to G5 ATTEMPT (the ordinary basis reference). These are the basis 7, the basis omitting the case, and the swapped selectors;
- (c)'s count: its pin moves to an extra basis, G8 PREPARATION with no cause. The missing-basis input it used before now reads G5 ATTEMPT;
- the RV108 N1 retained-reader test's transport row: G7 → G2.

**S-4, N-1, N-2 and S-2:**
- **S-4:** `test_b1_g5_not_required_admits_a_w2_published_case` gains my `nr_product_attempt_ref_with_attempt` row. That is 07j's edits keeping attempt 1, with case 1 naming it, expected G5 ATTEMPT. My Q17 is killed there (P37, §5).
- **N-1:** the transport docstring now states the gates: the header at G2 "as Rust reports it", and the metadata at G7. The gate and the single-defect code hold. On compound and carrier inputs, PY's header order is not Rust's (S-1).
- **N-2:** `test_b1_d38_stage_rule_refuses_each_conjunct_held_elsewhere` runs `_g5_stages` as the reader does, breaking each (4b) conjunct that other checks also hold. My P38–P40 test it (§5).
- **S-2:** REPAIR_02 §6 corrects REPAIR_01's claim for the three inputs. Its table matches my RP table: PY at R01 and RS (`b5cb7faaeb`) read G8 PREPARATION bound and admitted unbound, and TS read G5 ATTEMPT both. **At the three present heads, all three readers read G5 ATTEMPT on those three, bound and unbound.** On the other three repair-01 inputs, all three read G8 PREPARATION bound and admitted unbound. So SC's item 8 can now use any of the six.

## 2. The census over 07m

My harness (`rv113_py_harness.py`, as in my SR-PY review) ran on my copy of the head, as one slot job, with my authority builds (sha256 equal to I91's). It was compared with my census at R01 (the SR-PY review's `py_head.jsonl`), entry by entry (`census/PY2_CENSUS_07M.json`):
- **339 entries; input 0, bound 0, unbound 0; transport 9; 0 misses** against the corpus's Python expectations, at R01 and at the head; 0 escapes.
- **The nine are exactly the ruled ones,** entries 277 and 286–293. Each moves G7 → G2 with the same code and detail:
  - five `SOURCE_NUMERICAL_CASE_INVALID`;
  - one `SOURCE_NUMERICAL_QUALITY_INVALID`;
  - one `SOURCE_FORMULATION_BASIS_UNSUPPORTED`;
  - one `SOURCE_PREVIEW_PHYSICS_EVIDENCE_REQUIRED`;
  - one `SOURCE_BLOCKS_LEGACY_DOWNGRADE_FORBIDDEN`.
- **Against the other heads, all 1,017 verdicts** (`census/CENSUS_HEADS.json`):
  - against TS at `6fa6a64658`: **equal on all 1,017**;
  - against RS at `6e3e4fe219`: **transport equal on all 339**, bound and unbound on 338. The one difference is `g7_maximum_off_enclosure`, the corpus's declared per-reader G7 code.

## 3. My probes against TS's and RS's present heads

The 392 probes of my SR-TS confirmation (`probes_ts1.json`) ran through PY at the head, as one slot job. They are compared verdict by verdict with PY at R01 (the 360 it ran), RS at `6e3e4fe219` and TS at `6fa6a64658` (`probes/CROSS_PY2.json`).

**PY changed from R01 on 322 verdicts (176 probes).** 320 moved onto RS's verdict, and so onto TS's:
- (f): 32 bound and unbound verdicts to G3 COVERAGE (r2 F, and the (f)/(g) table);
- the ordinary basis: 14 to G5 ATTEMPT (r2 F's basis probes, and the three repair-01 inputs);
- (g): 20 bound verdicts to G8 INVOCATION;
- C2: 246 bound and unbound verdicts to G5 ATTEMPT (C-a, C-b, C-c, C-d, and the v5 C2 and (4b) rows), from admitted or from G5 PRODUCT_ATTEMPT;
- the header: eight N6 transport verdicts, G7 → G2 with the same code.

The other two are the compound N6 probes' transport verdicts. They moved to G2, but with PY's own first header code (S-1).

**Stated expectations.** The r2 and header sets state 430 verdicts. PY meets 426. The four misses are header probes on transport (S-1). TS and RS meet all 430.

**PY against TS and RS, all three verdicts:**
- **PY = TS on 383 of 392 probes, and PY = RS on 349.** On transport, PY = RS on 383, and RS = TS on all 392.
- **The (f), (g), ordinary-basis and C2 sections, and the rp and fg sets: PY = RS = TS on every verdict.** That is 144 C probes, 16 F, 25 G, 15 fg and 17 rp.
- **The owner-kind probe** (`x:f_src_owner_kind_combination`): G1 RECEIPT_MISMATCH in all three, bound, unbound and transport.

**Every remaining difference, named and checked against the declared ones:**

| Probes | PY | RS and TS | Declared? |
|---|---|---|---|
| `h_carrier_present` (transport) | G2 `SOURCE_PRODUCER_CONTRACT_UNSUPPORTED` | G7 `…EVIDENCE_INVALID` (no carrier branch in Rust's header; the metadata check refuses it) | **Not yet.** B1_SC item 7 asks for "a per-reader `carrier_evidence` entry". RS and TS now agree, and PY alone differs, at another gate. A declaration needs ROOT's ruling (S-1) |
| `h_carrier_and_quality_defect`, `h_carrier_and_recovery`, `n6_carrier_evidence_with_case_defect` (transport) | G2 `SOURCE_PRODUCER_CONTRACT_UNSUPPORTED` (the carrier branch first) | G2 with the other defect's code (`QUALITY_INVALID`, `LEGACY_DOWNGRADE_FORBIDDEN`, `CASE_INVALID`) | **No** (S-1) |
| `h_recovery_and_evidence_null`, `n6_contract_evidence_null_and_source_block_recovery` (transport) | G2 `SOURCE_PREVIEW_PHYSICS_EVIDENCE_REQUIRED` (evidence before recovery) | G2 `SOURCE_BLOCKS_LEGACY_DOWNGRADE_FORBIDDEN` (recovery first) | **No** (S-1) |
| the same six (bound and unbound), with `h_formulation_limitations_other` | each reader's raw G7 base code (PY = TS) | RS's raw G7 code | **Yes,** for the five compounds: the compound N6 probes' raw G7 codes (RV108 N6; B1_SC item 13). `h_formulation_limitations_other` is I83 §7 item 6 (B1_SC item 12). `h_carrier_present` is RS's specific raw code, as below (RS addendum 02, N-3) |
| `t_withheld_duplicate_multiset` (transport) | admitted | G7 `…EVIDENCE_INVALID` | **No** (N-1) |
| `t_extrema_global_upper_string`, `t_extrema_certified_gap_null` (transport) | G7 `…EVIDENCE_INVALID` | admitted | **No** (N-1) |
| the same two (bound and unbound) | G7 `…EVIDENCE_INVALID` | RS G7 `…NUMBER_INVALID`; **TS admits, eligible bound** | No: TS's false accept (my SR-TS addendum 01, S-1); PY refuses, correctly |
| 34 other metadata-defect probes (bound and unbound) | G7 `…EVIDENCE_INVALID` (as TS) | RS's specific raw codes | Pre-existing (RS addendum 02, N-3) |

**I91's reading of the compound pair.** REPAIR_02_ITEM4 §2 calls the two v5 probes "the declared N6 classes", and cites I90's REPAIR_02 §2 as recording the same pair. That holds for their raw G7 codes. But I90's §2 says "the transport parts follow item 4", and TS (`1d9455c714`) now reads them on transport with Rust's order and code. On transport they are not declared.

## 4. The tests

- **The two retained test files at the head** (contract and carriers), one slot job: **470 passed, 0 failed** (`suites/py2_retained.xml.gz`, with the junit `hostname` attribute removed).
- **Against my R01 run** (the SR-PY review's suite, these two files): **463 → 470: +7, 0 removed, 0 changed in outcome** (`suites/SUITE_COMPARE_PY2.json`). The seven are:
  - REPAIR_02's five: the (f)/G5, (g), the two C2 tests, and N-2's stage-rule test;
  - item 4's transport test, in its two modes.
- **I did not rerun the full Python set.** I91 reports 1,944 passed, 30 skipped, against R01's 1,937 (+7, 0 changed). My count for the two files (418 + 52) equals I91's.

## 5. Mutants

Forty mutants (`make_py_mutants_r2.py`, `make_py_mutants_r2b.py`), each an edit to `retained_precision.py` guarded by `RV113_MUT`, in my mutant copy:
- P01–P36 cover the round's items;
- P37 is my Q17 (S-4);
- P38–P40 drop three (4b) conjuncts that other checks also hold (N-2).

Each ran the two retained test files in full (470 tests, `--maxfail=10`) as one slot job. **The control passes 470 of 470,** and its probe run equals the head's on all 392 probes. A kill counts only for an `AssertionError` in a test (`MUTANT_TABLE_PY2.json`).

| Mutants | Edit | Result |
|---|---|---|
| P01, P03–P07 | G3: a source's index; the owner's case-index range (D16: without it, an `IndexError` reaches the fallback); the owner's case id; a basis's index; `case_indices` unique; in range | **all killed**, by `…receipt_references_at_g3_and_the_ordinary_basis_at_g5` |
| **P02** | **G3: the source owner's kind (I91's F-src-kind)** | **survives the tests and my 392 probes (0 moved): equivalent** (below) |
| P08, P09 | G5: the ordinary basis reference dropped; the basis need only resolve | **killed**, by the same test and repair 01's (b)/(c) tests |
| P10–P14 | (g): `reference_configurations` dropped; `pressure_contract`, `combinations` or `components` back to falsiness; null allowed | **all killed**, by `…model_scope_at_g8_invocation` |
| P15, P34 | C2: the whole table dropped; the table also applied to `prepared_product_failure` | **killed** (P15 by both C2 tests and the D38 capture test; P34 by ten failing test runs, where `--maxfail` stopped it) |
| P16, P17, P19 | `source_error`: the phase; the code; the decline's equal error | **killed**, by `…c2_cause_table_reader_logic` |
| **P18** | **`source_error`: no Run dropped** | **survives the tests and my probes: equivalent** (below) |
| P20–P22 | `receipt_failure`: the phase; the code set; `invocation_not_representable` removed from the set | **killed** (P21 also by `…in_the_reader`) |
| P23–P26 | `facade_failure`: the phase; the code; the selected Run; the owner | **killed** (P23 also by `…in_the_reader`) |
| P27–P29 | `unavailable_precondition`: the phase; no Run; the keying replaced by the set of four codes | **killed**, by `…reader_logic` |
| P30, P32, P33 | kernel: the phase; the code; the cause equal to the terminal's reason | **killed**, by `…reader_logic` |
| **P31** | **kernel: a Run present dropped** | **the tests fail only by a `TypeError`, not an assertion; my probe `r2:cb_kernel_no_run` kills it** (below; N-2) |
| P35, P36 | item 4: every base failure at G7 (the old label); every base failure at G2 (the metadata's too) | **killed**, by the item-4 test (both modes) and the N1 row (P35), or by the item-4 test and the G7 metadata test (P36) |
| P37 | Q17: `not_required` without its `product_attempt_ref` null conjunct | **killed**, by S-4's row in `test_b1_g5_not_required_admits_a_w2_published_case`. My probe `nr_product_attempt_ref_with_attempt` moves G5 ATTEMPT → G5 PRODUCT_ATTEMPT |
| P38–P40 | (4b): the case's Run absent; its status unavailable; the cause naming this attempt | **all killed**, each by the predicate's unit test and by N-2's `…stage_rule_refuses_each_conjunct_held_elsewhere`. 0 probes move, as N-2 says (other checks hold them in the whole reader) |

**37 of 40 are killed by an assertion, with 0 load failures.** The other three:
- **P02, F-src-kind: I91's claim is confirmed. The conjunct is unreachable.**
  - The schema's `CaseSource.owner.kind` is `{"const": "case"}`.
  - G1's `_shape(receipt, schema)` checks `const`, and it runs before G3 on every entry point (bound, unbound and transport; transport stops at G2 or G7 anyway).
  - My owner-kind probe (`x:f_src_owner_kind_combination`) reads G1 `RECEIPT_MISMATCH` in PY, RS and TS. With P02, 0 of 392 probes move.

  So no input reaches G3 with another kind. The conjunct is defensive, as in RS and TS.
- **P18 is equivalent.** C2's `source_error` branch needs a non-null `source_decline`. The decline rule later in the same pass (`_g5_ordinary`, pre-existing) requires `run` null whenever a decline is present, at the same gate and code (G5 ATTEMPT).
  - My further probe `x:c2_source_error_beside_run` (a source error with its decline, beside a selected Run) reads G5 ATTEMPT bound and unbound, with and without P18 (`PROBES_PY2X.json`).
  - I91 has no mutant for this conjunct.
- **P31 is detected only by an error.** `…c2_cause_table_reader_logic` calls `_g5_ordinary` directly. Its "kernel reason without a Run" row then subscripts `None`, so the test fails with a `TypeError`, not at its assertion.
  - In the whole reader, that `TypeError` reaches the fail-closed fallback: G5 `PRODUCT_ATTEMPT` instead of G5 `ATTEMPT`.
  - My probe `r2:cb_kernel_no_run` kills it, bound and unbound.
  - So the conjunct holds, but no assertion pins it (N-2).

## 6. Against I91's records

My results agree with REPAIR_02 and REPAIR_02_ITEM4 on every count I can compare:
- the nine transport changes, each G7 → G2 with the same code and detail, each equal to RS;
- transport equal to RS on all 339 entries;
- the two retained files 470, +7 over R01, 0 changed;
- the held patch's identity;
- F-src-kind's unreachability (§5).

Two readings differ:
- **The compound N6 pair on transport** (§3): "declared" holds for raw only.
- **The docstring** says the header is reported "as Rust reports it". That holds for each single header defect, but not for PY's order (S-1).

**I91's mutant counts** agree with mine where they overlap:
- 30 mutants, 29 killed by an assertion, and F-src-kind not killable;
- item 4's three, all killed;
- N0 470 of 470.

My set adds conjunct-level mutants to each C2 branch: the phase and code of `source_error`, `facade_failure`, `unavailable_precondition` and kernel, a receipt code removed, and the two Run conjuncts. These turn up P18 (equivalent) and P31 (N-2).

## Findings

| # | Severity | Where | Finding | Proposed |
|---|---|---|---|---|
| S-1 | SHOULD-FIX (ROOT to rule) | PY `_transport_base` (`_source_contract`'s header on the projection), its docstrings, and I91 REPAIR_02_ITEM4 §2 | **PY's transport header is at G2, but in Python's order.** It has the carrier branch first, and it checks `contract_evidence` before `source_block_recovery`. TS (`1d9455c714`) took Rust's order and code, so RS and TS now agree on transport on all 392 of my probes. PY differs on six (§3):<br>• `carrier_evidence` alone: PY G2 `PRODUCER_CONTRACT_UNSUPPORTED`, against RS and TS G7 `…EVIDENCE_INVALID`. That is a different gate: PY treats the member as a header defect, and Rust as a metadata defect;<br>• three carrier compounds and two recovery-with-null-evidence compounds: G2 in all three readers, but PY's code is its own first header code.<br>None is declared. RV108 N6 and B1_SC item 13 declare only the compound probes' **raw** G7 codes. I90's REPAIR_02 §2 says "the transport parts follow item 4". B1_SC item 7's "per-reader `carrier_evidence` entry" could hold the single-member case once ROOT declares it, but not the compound order. So I91's "the declared N6 classes" (REPAIR_02_ITEM4 §2) holds for raw reads only. The docstrings' "as Rust reports it" holds per single defect, not for the order.<br>**07m is not affected:** PY's transport equals RS's on all 339 entries, so aligning the order cannot move a census verdict | ROOT rules on one of two ways:<br>• (a) align PY's transport header with Rust's order, as TS did: drop the carrier branch on transport, and check recovery before evidence. Pin it with the h probes' compound rows;<br>• (b) declare PY's transport order per reader, with SC entries and scope sentences.<br>Either way, correct the docstring and REPAIR_02_ITEM4's "declared" |
| N-1 | NOTE | PY `validate_transport_metadata` against RS's and TS's | **The metadata check differs on three shapes,** as my RS addendum 02 (N-1) and TS addendum 01 (N-1) record. On transport, PY admits a duplicate withheld record, which RS and TS refuse at G7, because PY compares the records as sets. PY refuses a non-number `global_upper_bound_pa` and a null `certified_gap_pa`, which RS and TS admit. On the raw path, PY refuses all three, correctly. There, TS's admission of the two extrema shapes is TS's false accept (TS addendum 01, S-1) | ROOT rules the shared form before SC pins these shapes |
| N-2 | NOTE | PY tests: `test_b1_repair02_c2_cause_table_reader_logic` | **C2's kernel branch's "a Run present" conjunct is pinned by no assertion.** Without it (P31), the reader-logic test fails only by a `TypeError`. In the whole reader, the input reads G5 `PRODUCT_ATTEMPT` (the fallback) instead of `ATTEMPT`. My `r2:cb_kernel_no_run` kills it | Add a whole-reader row, a kernel reason on a case with no Run, expecting G5 ATTEMPT with no cause (as D16 does). SC's C2 entries can carry it |

## For ROOT

1. **S-1:** rule PY's transport header order: align it with Rust's, as TS did, or declare it per reader. Either way, 07m does not move. If ROOT reads item 4's "as RS has it" as including the order, this is a small PY follow-up after or with I4.
2. **N-1:** the same ruling my RS and TS addenda ask for: the shared form of the transport metadata check (PY's, or RS's and TS's).
3. **Nothing else on PY's side stands in the way of I4.** S-2's six repair-01 inputs now read the same in all three readers, so SC's item 8 can use them as they are.

## Host

- **No cargo job in this confirmation.** The three authority binaries are my SR-RS round-2 builds (`WT/targets/rv113-pybins2`; sha256 equal to my SR-PY builds and to I91's). Every Python job set the three `OPENPIPESTRESS_*_BIN` variables to them.
- **Slot jobs** through `WT/tools/t3_slot.sh`, one at a time, each the only heavy job of mine (`host/job_stamps.txt`):
  - the census, the 392 probes, and the two retained test files at the head;
  - the mutant chain: the control and P01–P36, each a pytest run of the two files;
  - the four further mutants, P37–P40;
  - the probe runs of the control, of every mutant not killed by an assertion, and of P37–P40;
  - the further C2 probe on the control and P18 (a first version, whose two probes were malformed for the schema and read G1 everywhere, also ran on P31; its outputs are kept in `mutants/py2x_first/`).

  No pytest ran outside a slot.
- **A slip, disclosed.** My first launch of the mutant chain passed its ids as a single word: zsh does not split an unquoted variable. So it ran one pytest job only, of the two files, with `RV113_MUT` set to the whole list. That value matches no mutant, so it was a second control run: 470 passed. It was one slot job, and its waiter ended with it. I deleted its folder and relaunched the chain from a bash script that reads the ids from a file.
- **Waits:** each chain had one waiter, its background completion (for the last two short probe jobs, the foreground call), which ended with it. None of mine remain. I killed no job.
- **A correction to my SR-RS addendum 02.** Its host section says I deleted `WT/targets/rv113-pybins2`. I had not: I kept those binaries for this confirmation. I deleted them at the end of this work (below).
- **E-16 (the coordinator's notice: my SR-PY review's 42 junit files redacted in place).**
  - I checked the review folder: `SHA256SUMS` has sha256 `0a93a804e88fadf2811dd5b00d29c0941c63a899fd9c7ee0adfcb4e5b68d091f` and verifies 245 of 245; `REVIEW.md` is unchanged (`d8611e59…`).
  - The `hostname` attributes there were my slip in that review. I re-screened every file of my three review folders, `.gz` decompressed, under E-16's rule: 0 hits. The folders are `rvr_sr_rs_01` (with addendum 02), `rvr_sr_ts_01` (with addendum 01) and `rvr_sr_py_01`.
- **Records:**
  - the junit `hostname` attribute stripped from every junit file before sealing (the sanitizer now strips it, and refuses any left);
  - no symlink and no folder named `build`;
  - placeholder paths only;
  - screened, `.gz` files decompressed: the strict pattern, and, case-insensitive, the machine's network name, every laptop-model form of its name, and any `hostname` attribute.
- **Not done:** no DEC-025, installs or Git writes (`git archive` and reads only, with `GIT_OPTIONAL_LOCKS=0`).
- **Cleanup:**
  - I deleted my copies `WT/rv113/py2-head` and `WT/rv113/py2-mut`, and the target `WT/targets/rv113-pybins2`;
  - `WT/rv113/` holds nothing of mine;
  - scratch is kept in `WT/scratch/rv113_rvr_01/pyr2/`.

## Records (`addendum_01/`)

- `static/`: `copies.txt` (file hashes against `git show`, and the files R01..HEAD changes).
- `harness/`:
  - `rv113_py_harness.py`, `rv113_py_harness_lib.py`, `cross_heads.py`, `compare_py.py`, `compare_junit_retained.py`;
  - `make_pyr2_copies.sh`, `run_pyr2.sh`, `rsr2_job.sh`;
  - `make_py_mutants_r2.py`, `make_py_mutants_r2b.py`, `run_py_mutants_r2.sh`, `run_py_mutants_r2_all.sh`, `run_py_mutants_r2_extra.sh`, `py_mutant_table_r2.py`;
  - `gen_probes_py2x.py`, `run_py2x.sh`;
  - `sanitize_py.py`.
- `probes/`:
  - `probes_ts1.json.gz` (the 392, as in my SR-TS addendum 01), `probes_py2x.json` (the further C2 probe);
  - `py2_head.jsonl.gz`, and PY at R01 on the 360 (`py_cmp_all.jsonl.gz`);
  - `CROSS_PY2.json`.
- `census/`: `py2_head.jsonl.gz`, `PY2_CENSUS_07M.json`, `CENSUS_HEADS.json`.
- `suites/`: `py2_retained.xml.gz`, `py2_tests.log`, `SUITE_COMPARE_PY2.json`.
- `mutants/`: `MUTANTS_PY2.json` (40), `MUTANT_TABLE_PY2.json`, `PROBES_PY2X.json`, `py2x_first/`, and `runs/<id>/` (run stamps; the pytest log and junit report, gzipped; the probe runs).
- `host/`: `job_stamps.txt`.
