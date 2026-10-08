# I100 B1, the reader follow-up toward I4′, PY's lane: rulings 1, 2 and 5

TASK (Type 2), I100 (I-PY), for ROOT (HELP_HUMAN, Agent 0), the return path. I made no delegation. 2026-10-08 UTC.

## Basis

- **Instructions read:** `NUM/AGENTS.md` and `NUM/agents/AGENT_TASK.md`.
- **Briefs**, each verified by sha256 before use:
  - `R/BRIEFS/B1_I4P_PY.md` `fc603ee291a4eb59ab51bbb9fc25ca934a8fbbf02f73a07e7d23cac4e5d2e43b` (mine; its host rules govern);
  - `R/BRIEFS/B1_COMMON.md` `2d170307516b98c40e8aa2dcf352cf11a13dbdd29aeddd78a4c39f3f15eb2c75`;
  - `R/BRIEFS/B1_SR_PY.md` `2a902874278ed5890a9179f9faa1ba8b065baf1c7cabeb5c25ccd2ffb180322e`.
- **The specification:** RR "I4 made at `30f3d1b24a`; RV113's items for ROOT ruled; …", rulings 1, 2 and 5 (`T/ROOT_RULINGS_V1.md` at NUM `b9383b9b6e`, sha256 `77780a0c…`).
- **RV113's addenda:**
  - SR-PY addendum 01, `R/REVIEW_RV113/rvr_sr_py_01/ADDENDUM_01.md` `a61bbe1b5c81ffc88c988e4fcc04d4702dcc8873d8b06a2d151fc2a8dfd757e3`: §3, S-1, N-1, N-2 and "For ROOT";
  - SR-RS addendum 02, `rvr_sr_rs_01/ADDENDUM_02.md` `c43317f81d6eae653cc605629334194cd27791e25a6c6076bce8886c29ba682d`: §6.
- **Also read, for items it names only:** `R/BRIEFS/B1_SC.md` (`c6ddf8d6…`), items 7, 12, 13 and 14. Nothing for SC is done or committed.
- **The worktree:** `WT/b1-p`, branch `codex/piping-t3-b1-p-20261007`, clean at I4 = `30f3d1b24a` on arrival.

**Placeholders:** `WT`, `NUM`, `P`, `T`, `R`, `VENV` as in the dispatch; `S` = `WT/scratch/i100_b1_i4p_py`. Outputs are in `_run_records/`, covered by `SHA256SUMS`.

## 0. Summary

- **HEAD = `52d83da2755599ce554a673077a8409d30d8722b`**, two commits on I4, each ending with the agent trailer. Not pushed: ROOT pushes.
  - `8fa5aac15c`: rulings 1, 2 and 5, with three added tests;
  - `52d83da275`: one docstring (`compatibility._retained_transport`), no code. Its file's AST, docstrings removed, equals `8fa5aac15c`'s (`diff/ast_same.txt`).
- **The census over 07m** (RV113's harness, 339 entries × 3 verdicts):
  - at I4 against RV113's PY census at `2843a59a16` (PY's files are byte-identical): **0 changes**, detail included;
  - at HEAD against I4: **0 changes** on all 1,017 verdicts, detail included; **0 misses** against the corpus's PY expectations and 0 escapes, at both.
- **RV113's probes** (392, plus RS addendum 02's two `r2x` metadata probes):
  - **7 PY verdicts change, all on transport, and each moves onto RS's and TS's verdict at I4:** the six ruling-1 header probes and `t_withheld_duplicate_multiset`.
  - RV113's 430 stated expectations: **430 met** (426 at I4).
  - **PY = TS on 390 of 392 probes and PY = RS on 349;** on transport, PY = RS = TS on 390.
  - **Every remaining difference is either a declared raw G7 code (41 probes, bound and unbound only) or one of the two extrema shapes that I101's lane aligns** (rulings 2 and 3). No other difference.
- **pytest, I83's 27 files, against I4: 1,944 → 1,947 passed, 30 skipped, rc 0.** The three added tests are the only difference: 0 removed, 0 changed in outcome.
- **Mutants: 10 of 10 killed by an assertion,** one per new or moved check, plus the kept extrema demand. The control passes 613 of 613. PRE (the head's tests on I4's reader) fails exactly the ruling-1 and ruling-2 tests.
- **For ROOT** (§8): one further shape PY's schema typing refuses that RS and TS admit (more than 16,384 items in a `contract_evidence` array, on transport), and one PY admits that RS and TS refuse (an unsafe-integer `span_index`, on transport). Neither is changed.

## 1. Ruling 1: PY's transport header takes Rust's order and codes

**The change** (`compatibility.py`, `retained_precision.py`):
- `_source_contract` gains a keyword, `rust_header_order` (default `False`). **Only `retained_precision._transport_base` passes it** (`True`), on the reader's transport projection. With it:
  - **no carrier branch:** a `carrier_evidence` member passes the header and reaches the preview-physics transport metadata check, whose namespace demand refuses it (`…EVIDENCE_INVALID: unsupported source namespace`), which `_transport_base` reports at **G7**;
  - **`source_block_recovery` before `contract_evidence`:** the recovery member is refused before the preview evidence demand, as Rust's `for_source_metadata` orders them.
- **Every other caller passes nothing and reads exactly as before:** the raw reads (G7 runs `_source_contract(projected)`) and every non-retained dispatch, including a preview-physics-1 statement's own transport dispatch and the v0.3 packager's.
- **Docstrings corrected:** `validate_retained_precision_transport`, `_transport_base` and `compatibility._retained_transport` now say the order is Rust's.

**After the change, the retained transport header is Rust's, check for check:** producer, then recovery, then the evidence demand, then quality, cases and formulation. The metadata check follows at G7. TS already reads it so at I4 (RV113's SR-PY addendum 01, S-1).

**Evidence:**
- **RV113's six transport probes** (`probes/`), each now RS's and TS's gate and code at I4:

| Probe | PY transport at I4 | PY transport at HEAD | RS and TS at I4 |
|---|---|---|---|
| `h_carrier_present` | G2 `SOURCE_PRODUCER_CONTRACT_UNSUPPORTED` | **G7 `SOURCE_PREVIEW_PHYSICS_EVIDENCE_INVALID`** | G7 `SOURCE_PREVIEW_PHYSICS_EVIDENCE_INVALID` |
| `h_carrier_and_quality_defect` | G2 `SOURCE_PRODUCER_CONTRACT_UNSUPPORTED` | **G2 `SOURCE_NUMERICAL_QUALITY_INVALID`** | G2 `SOURCE_NUMERICAL_QUALITY_INVALID` |
| `h_carrier_and_recovery` | G2 `SOURCE_PRODUCER_CONTRACT_UNSUPPORTED` | **G2 `SOURCE_BLOCKS_LEGACY_DOWNGRADE_FORBIDDEN`** | G2 `SOURCE_BLOCKS_LEGACY_DOWNGRADE_FORBIDDEN` |
| `n6_carrier_evidence_with_case_defect` | G2 `SOURCE_PRODUCER_CONTRACT_UNSUPPORTED` | **G2 `SOURCE_NUMERICAL_CASE_INVALID`** | G2 `SOURCE_NUMERICAL_CASE_INVALID` |
| `h_recovery_and_evidence_null` | G2 `SOURCE_PREVIEW_PHYSICS_EVIDENCE_REQUIRED` | **G2 `SOURCE_BLOCKS_LEGACY_DOWNGRADE_FORBIDDEN`** | G2 `SOURCE_BLOCKS_LEGACY_DOWNGRADE_FORBIDDEN` |
| `n6_contract_evidence_null_and_source_block_recovery` | G2 `SOURCE_PREVIEW_PHYSICS_EVIDENCE_REQUIRED` | **G2 `SOURCE_BLOCKS_LEGACY_DOWNGRADE_FORBIDDEN`** | G2 `SOURCE_BLOCKS_LEGACY_DOWNGRADE_FORBIDDEN` |

  Their bound and unbound verdicts are unchanged: PY's own raw G7 codes, the declared class (B1_SC item 13).
- **The test** `test_i4p_ruling1_transport_header_takes_rusts_order_and_codes` (`tests/test_retained_precision_contract.py`) pins the six as rows, each built from RV113's base and edits: transport as RS and TS; raw at G7 with PY's code. It also pins:
  - the carrier member alone reaching the metadata check's namespace demand;
  - each member alone at its own gate and code, and the control admitted (`needs_recompute`);
  - the successor's transport dispatch (`_source_contract(…, check_receipt=False)`) giving the reader's text;
  - **the scope:** a preview-physics-1 statement's own transport dispatch keeps Python's order (`SOURCE_PRODUCER_CONTRACT_UNSUPPORTED` for the carrier, `…EVIDENCE_REQUIRED` for the pair).

## 2. Ruling 2, PY's side: withheld records compared as multisets

**The change** (`preview_physics_evidence.py`):
- `_cases` gains a keyword, `withheld_multiset` (default `False`). With it, each case's withheld records are compared across cases as a sorted tuple (a multiset), as Rust and TS compare sorted lists. **A record whose multiplicity differs between cases is refused** ("support attribution differs between cases"), which the retained reader reports at **G7 `SOURCE_PREVIEW_PHYSICS_EVIDENCE_INVALID`**.
- **`validate_transport_metadata` passes it.** The raw evidence check (`validate_preview_physics_evidence`) does not: raw reads keep sets there, and their support-action step already refuses any record repeated within a case. So raw verdicts and details are unchanged.
- **PY's extrema-number demand stays** (`global_upper_bound_pa` and `certified_gap_pa` must be numbers): it is the shared form. The docstring says so.
- **PY's schema typing is unchanged.** One further shape it refuses that RS and TS admit is reported in §8.

**The callers this reaches.** `preview_physics_evidence.validate_transport_metadata` also serves a non-retained path, and the change is identical there. It is called only by `compatibility._source_contract(…, check_receipt=False)` for a preview-physics-1 statement, which is reached by:
- the retained reader's transport step (`retained_precision._transport_base`, from `validate_retained_precision_transport`, and so from `compatibility._retained_transport` and the successor's transport dispatch);
- the v0.3 stress-neutral packager's validator, `package_v0_3.validate_stress_neutral_export_package_v0_3` → `_transport_contract`, for a preview-physics-1 package's transport statement;
- tests: `tests/test_preview_physics_consumer_contract.py` calls it directly.

**Evidence:**
- **`t_withheld_duplicate_multiset`** (case 0 withholds `s` twice, case 1 once): PY transport **admitted → G7 `…EVIDENCE_INVALID`**, RS's and TS's verdict. Bound and unbound unchanged: G7 `…EVIDENCE_INVALID` (PY's and TS's raw code; RS's is `…SUPPORT_LISTED_TWICE`, the declared raw class).
- **The two extrema shapes** (`t_extrema_global_upper_string`, `t_extrema_certified_gap_null`): PY refuses them at G7 bound, unbound and on transport, at I4 and at HEAD. RS and TS admit them on transport at I4; ruling 2 has them add the demand in I101's lane.
- **The test** `test_i4p_ruling2_transport_metadata_compares_withheld_records_as_multisets` pins:
  - transport: the probe and its mirror (the multiplicities the other way) refused, with the multiset detail; equal multisets with a duplicate in each, and equal multisets in another order, admitted; different sets refused;
  - raw: the probe's bound and unbound verdicts and details unchanged;
  - the non-retained path: `validate_transport_metadata` and the transport dispatch on the probe's preview-physics-1 projection both refuse it with the same text, while the raw dispatch keeps its own;
  - the extrema-number demand, kept: both shapes refused bound, unbound and on transport.

## 3. Ruling 5: C2's kernel branch, a whole-reader row

**The change:** test only. `test_i4p_ruling5_kernel_reason_without_a_run_is_g5_attempt_in_the_reader` builds RV113's `r2:cb_kernel_no_run`. That is `two_case_preparation_failure_synthetic`'s case 1 with a kernel reason (`kernel_refused`, phase `kernel`), no Run and no product attempt.
- It expects **G5 `ATTEMPT_MISMATCH`, bound and unbound, with no cause** (`__cause__ is None`, as D16's row does).
- **RV113's P31** (the kernel branch without its Run-present conjunct) now fails this row at its assertion: the fallback gives G5 `PRODUCT_ATTEMPT_MISMATCH` caused by a `TypeError` (my M8, §7).

## 4. The record's correction (I91's REPAIR_02_ITEM4 §2)

I91's `REPAIR_02_ITEM4.md` §2 calls the transport verdicts of `n6_carrier_evidence_with_case_defect` and `n6_contract_evidence_null_and_source_block_recovery` "the declared N6 classes".
- **That "declared" holds for raw reads only:** their bound and unbound G7 codes (RV108 N6; B1_SC item 13).
- **On transport, ruling 1 supersedes it.** PY now reads both as RS and TS do: G2 `SOURCE_NUMERICAL_CASE_INVALID` and G2 `SOURCE_BLOCKS_LEGACY_DOWNGRADE_FORBIDDEN` (§1).
- The sealed record is not edited.

## 5. The census and the probes

**The census over 07m** (`census/`). RV113's harness, as published (`rv113_py_harness.py`, sha256 `df4310a8…`, equal to RV113's sealed copy), ran on archive copies of I4 and HEAD (`P` without `execution/_Coordination`), with my builds, each as one slot job. Entries are matched by set, position and id.
- **I4 against RV113's PY census at `2843a59a16`** (`I4_VS_RV113_PY2.json`): **0 changes** on 1,017 verdicts, detail included; equal input hashes; 0 misses; 0 escapes.
  - PY's reader files, tests and the corpus at I4 are byte-identical to `2843a59a16`'s (`static/heads.txt`).
- **HEAD against I4** (`FINAL_VS_I4.json`; the first commit's run, `HEAD_VS_I4.json`, reads the same): **0 changes on all three verdicts**, detail included; equal input hashes; **0 misses** against the corpus's PY expectations; 0 escapes.
- **Against the other readers at I4** (short verdicts): PY = TS on all 1,017; PY = RS on all but `g7_maximum_off_enclosure`'s bound and unbound code, the corpus's declared entry. That holds at I4 and at HEAD.

**RS's and TS's verdicts at I4.** I did not run RS or TS. Their verdicts are RV113's recorded runs at RS `6e3e4fe219` and TS `6fa6a64658`, the heads merged into I4:
- RS: `rvr_sr_rs_01/addendum_02/census/rs2_head.jsonl.gz`, `rvr_sr_ts_01/addendum_01/probes/rs2_head_ts1.jsonl.gz`, and `rvr_sr_rs_01/addendum_02/mutants/runs/NONE/probes_r2x.jsonl.gz` (RS's control on the two `r2x` probes);
- TS: `rvr_sr_ts_01/addendum_01/census/census_ts1_head.jsonl.gz` and `…/probes/ts1_head.jsonl.gz`.

They are RS's and TS's verdicts at I4 because their readers are byte-identical there (`static/heads.txt`, `git diff --name-only` of each head against I4):
- **RS:** `core/reporting/result_export`, its two dependency crates (`core/serialization/canonical_json`, `core/units`), the corpus and the schemas are unchanged from `6e3e4fe219` to I4. The only `fixtures/` difference is the two new W-C2 successor files, which neither harness reads.
- **TS:** `apps/`, the corpus and the schemas are unchanged from `6fa6a64658` to I4.

**RV113's probes** (`probes/`; HEAD's comparison is `FINAL_PROBES_TS1.json`): `probes_ts1.json` (392; sha256 `e4a74e48…`, the decompressed sealed copy) and `probes_r2x.json` (2; `8d1c33d2…`), at I4 and at HEAD.
- **PY at I4 equals RV113's PY run at `2843a59a16`** on all 392 probes, detail included.
- **I4 → HEAD: 7 probes change, each on transport only,** and each onto RS's and TS's verdict: the six of §1 and `t_withheld_duplicate_multiset` (§2). No bound or unbound verdict changes.
- **RV113's stated expectations: 430 of 430 met at HEAD** (426 at I4; the four misses were header probes of §1).
- **Agreement at HEAD:**

| | All three verdicts equal | Transport equal |
|---|---|---|
| PY and TS | 390 of 392 (383 at I4) | 390 (383 at I4) |
| PY and RS | 349 of 392 (349 at I4) | 390 (383 at I4) |

- **Every remaining difference** (`FINAL_DIFF_CLASSES.json`, equal to the first commit's `HEAD_DIFF_CLASSES.json`):

| Probes | PY at HEAD | RS and TS at I4 | Class |
|---|---|---|---|
| 34 `r2:t_*` metadata-defect probes, bound and unbound | G7 `…EVIDENCE_INVALID` (= TS) | RS: its specific raw G7 codes (`…EXTREMA_BOUNDS`, `…STRESS_COVERAGE_PARTITION`, `…INTENSIFIED_RESULT_MISSING`, …) | **Declared raw G7 codes** (RV113's RS addendum 02 N-3; B1_SC item 13; ruling 3's declared raw class). Transport equal in all three |
| the six probes of §1 (four `h:` and two `n6_`), bound and unbound | PY's raw G7 code (= TS) | RS's raw G7 code | **Declared:** the compound N6 probes' raw G7 codes (RV108 N6; B1_SC item 13), and for `h_carrier_present` RS's specific raw code (`…FOREIGN_METHOD_EVIDENCE`; RS addendum 02 N-3). Transport now equal (§1) |
| `h_formulation_limitations_other`, bound and unbound | G7 `…EVIDENCE_INVALID` (= TS) | RS G7 `…FORMULATION_BASIS` | **Declared** (I83 §7 item 6; B1_SC item 12) |
| `t_extrema_global_upper_string`, `t_extrema_certified_gap_null` | G7 `…EVIDENCE_INVALID` bound, unbound and transport | RS: G7 `…NUMBER_INVALID` raw, admitted on transport. TS: admitted (eligible bound) | **Ruled, I101's lane:** ruling 2 (RS and TS add the demand on transport) and ruling 3 (TS's raw false accept). RS's raw code is the declared class |

  That is 34 + 6 + 1 = 41 probes in the declared raw class, and 2 ruled in I101's lane. **No other difference.** No `C`, `F`, `G`, `fg`, `rp` or `x` probe differs in any reader.
- **The two `r2x` probes** (a measure and a gate with an extra member): PY refuses both at G7 bound, unbound and on transport, at I4 and HEAD. RS's control gives the same transport verdict; its raw codes are its own (declared class). TS did not run them.

## 6. The tests

**I83's Python set** (the 27 files I91 ran: I69's set plus the retained files) ran at I4 and at HEAD, each as one slot job with my builds (`suites/`, the junit `hostname` attribute removed).
- **I4 (`30f3d1b24a`): 1,944 passed, 30 skipped, rc 0.** That is I91's count at `2843a59a16`.
- **HEAD (`52d83da275`): 1,947 passed, 30 skipped, rc 0.**
- **Against I4, test by test** (`SUITE_COMPARE_I4_FINAL.json`): **+3 added, 0 removed, 0 changed in outcome.** The three are `test_i4p_ruling1_transport_header_takes_rusts_order_and_codes`, `test_i4p_ruling2_transport_metadata_compares_withheld_records_as_multisets` and `test_i4p_ruling5_kernel_reason_without_a_run_is_g5_attempt_in_the_reader`, all passing. No existing test changed.
- **The first commit `8fa5aac15c` ran the same set:** 1,947 passed, 30 skipped, equal to HEAD's run test by test (`SUITE_COMPARE_HEAD_FINAL.json`: 0 added, 0 removed, 0 changed). Its census and probe outputs are byte-identical to HEAD's.

## 7. Mutants

`scripts/make_mutants.py` makes ten guarded edits to the HEAD copy's reader files. Each is active only when `I100_MUT` names it, and each replaced text is asserted unique. Each run is one slot job of the two retained test files and the preview-physics consumer contract, in full (`scripts/run_mutants.sh`). **A kill counts only for an assertion:** an `AssertionError`, or `pytest.raises`' own "DID NOT RAISE" (`scripts/mutant_table.py`).

**The control (NONE, the mutant copy with no mutant active) passes 613 of 613.** That is the contract file 421, the carriers 52 and the preview-physics consumer contract 140.

| Mutant | Edit | Result |
|---|---|---|
| M1 | ruling 1: the carrier branch restored on the retained transport header | **killed** by `…ruling1…` (`h_carrier_*` and `n6_carrier_*` rows) |
| M2 | ruling 1: recovery not moved before the evidence demand on transport | **killed** by `…ruling1…` (`h_recovery_and_evidence_null`, `n6_contract_evidence_null_and_source_block_recovery`) |
| M3 | ruling 1: the transport step does not ask for Rust's order (both moves undone) | **killed** by `…ruling1…` |
| M4 | ruling 1's scope: Rust's order for every caller (raw reads and the non-retained dispatch too) | **killed** by `…ruling1…` (raw codes and the preview-physics-1 dispatch rows) |
| M5 | ruling 2: the transport check compares withheld records as sets again | **killed** by `…ruling2…` (`t_withheld_duplicate_multiset` and its mirror admitted) |
| M6 | ruling 2: the multiset compared as an unsorted list | **killed** by `…ruling2…` ("equal multisets, in another order" refused) |
| M7 | ruling 2's scope: the raw evidence check compares multisets too | **killed** by `…ruling2…` (the raw detail changes) |
| M8 | ruling 5: C2's kernel branch without its Run-present conjunct (RV113's P31) | **killed** by `…ruling5…` (G5 `PRODUCT_ATTEMPT` with a `TypeError` cause, against G5 `ATTEMPT` with none). `…c2_cause_table_reader_logic` also fails, by a `TypeError`, as RV113 found |
| M9 | kept: the `_cases` extrema-number demand without `global_upper_bound_pa` and `certified_gap_pa` | **killed** by `…ruling2…` (the bound read admits the shape, eligible) |
| M10 | kept: both of PY's demands on those members gone on transport (M9, and the schema walk skipped) | **killed** by `…ruling2…` (transport admits) and by the existing `test_transport_metadata_checks_statement_without_rows` ("DID NOT RAISE") |

- **10 of 10 are killed by an assertion.** No kill is only an error, and nothing failed to load.
- **PRE** (a baseline, not a mutant: the head's tests on I4's three reader files) fails exactly two tests, at their assertions: `…ruling1…` and `…ruling2…`. The other 611 pass. `…ruling5…` passes on I4's reader, as a test-only row should.

## 8. For ROOT

1. **A further shape PY refuses that RS and TS admit (ruling 2: reported, not changed).**
   - **The shape:** on transport, a `contract_evidence` array with more than 16,384 items. That covers `preview_cases`, `combination_gates`, and each case's extrema, coverage lists, attribution lists and measures.
   - **The cause:** PY's transport check walks `contract_evidence` against the results schema with `source_blocks._shape`. That walk caps every array at `maxItems`, **defaulting to 16,384** when the schema names none (`source_blocks.py:73`). `PreviewPhysicsContractEvidence` names none.
   - **The other readers:** RS's `preview_physics_transport_metadata` and TS's `validatePreviewPhysicsTransportMetadata` have no such bound. This is by reading; I did not run them.
   - **My probe** `x100:t_gates_16385` (16,385 distinct, well-formed gates, set after rehash, since a transport read does not verify the publication): PY refuses at G7 `…EVIDENCE_INVALID: transport evidence shape`. `x100:t_gates_16384` is admitted.
   - **Raw reads** do not walk the schema, so they have no such bound.
   - **Every other schema demand** on `contract_evidence` I compared with RS's and TS's checks (closed keys, non-empty strings, enums, the fractions' range, `subdivisions`' range, positive `sif` and modulus, the gate reason's `oneOf`) is one that RS and TS make too, or the ruled extrema-number demand.
2. **A shape PY admits that RS and TS refuse (not asked; reported, not changed).**
   - **The shape:** on transport, an extremum's `span_index` that is integral but not a safe integer. RS's `safe_integer` (|n| ≤ 2⁵³ − 1) and TS's `Number.isSafeInteger` refuse it, by reading.
   - **PY's tests** (`_integer` in `_cases`, and the schema walk's `integer`) admit it. My probes `x100:t_span_index_2p53_plus_1` (9,007,199,254,740,993) and `x100:t_span_index_1e300` are admitted on transport (`needs_recompute`).
   - **Why only on transport:** a raw read cannot carry it, because the checked-JSON authority cannot hash the publication (RV113's RS addendum 02 §6 dropped a 1e300 probe for that reason). A transport read does not hash the publication, so the shape reaches the metadata check.
   - **Proposed:** PY could demand a safe integer there, as `subdivisions`' bound already implies. That needs ROOT's ruling, and an SC entry.
3. **Not in my lane, for context:** a preview-physics-1 statement's own transport dispatch (`_source_contract(…, check_receipt=False)`, as the v0.3 packager runs it) keeps Python's header order, as ruling 1 is scoped. Rust's `for_source_metadata` uses Rust's order for that identity too. No retained read reaches that path, and no ruling covers it.
4. **A tree note:** `WT/b1-p` at I4 still carries RV58's pre-#1109 fixture `.gitignore` as a symlink (mode 120000; `git status` warns "Too many levels of symbolic links"). NUM has #1109's repair. It comes to `b1` with NUM's next merge.

## 9. Host

- **The four-slot rule** (the brief's host rules, which govern here).
- **Cargo:** three builds of the CLI authorities through `WT/tools/t3_cargo.sh` (`--locked --offline --release`), from `WT/b1-p` at I4, into `WT/targets/i100-b1-i4p-py/` (`scripts/build_bins.sh`). They are byte-identical to I91's builds (`host/binaries.txt`). This round changes no CLI source.
- **Every Python job** set `OPENPIPESTRESS_CHECKED_JSON_BIN`, `OPENPIPESTRESS_BINARY64_JSON_BIN` and `OPENPIPESTRESS_UNITS_BIN` to those builds (`scripts/env.sh`), with `PYTHONDONTWRITEBYTECODE=1` and `TMPDIR` under `S/tmp/`.
- **Heavy jobs: 22, each through `WT/tools/t3_slot.sh` (or `t3_cargo.sh`), one of mine at a time** (`host/cargo_jobs_i100.log`: 22 starts and 22 ends, none overlapping):
  - the three builds;
  - the census and probes at I4, at `8fa5aac15c` and at HEAD;
  - I4's further probes;
  - the 27-file suite at I4, at `8fa5aac15c` and at HEAD;
  - the twelve mutant-lane runs: NONE, M1–M10 and PRE.
- **Light checks outside a slot, disclosed:**
  - eight named probes on the edited tree before committing (seconds, `scripts/quick_probes.py`);
  - the three new tests alone (3 tests, 2.5 s);
  - the four further probes, once, before their slot runs.
- **Waits:** two background chains (`scripts/chain_suites.sh`, `scripts/chain_final.sh`), each with one waiter, its completion notice. The first build and the I4 and `8fa5aac15c` verdict jobs were foreground calls that ended with their jobs. No monitor or poll loop ran. No process of mine remains.
- **I signalled or killed no job.** No DEC-025 and no install.
- **Git:** two commits on `codex/piping-t3-b1-p-20261007` in `WT/b1-p`; no push. Reads used `GIT_OPTIONAL_LOCKS=0`. `WT/b1-p` is clean at HEAD apart from the pre-existing symlink warning (§8.4).
- **Copies:** I4, `8fa5aac15c` and HEAD as `git archive` copies of `P` without `execution/_Coordination`, each file checked against `git show` (`static/copies.txt`). The mutant copy and PRE copy are made from HEAD's archive.
- **Records:**
  - every file copied through `scripts/sanitize.py`: placeholders, junit `hostname` attributes removed, and any machine path refused;
  - no symlink and no folder named `build`;
  - screened by `scripts/screen_dir.py`, which uses `WT/tools/t3_host_screen.py`'s own patterns (the strict path forms, the junit host attribute, the model form and the machine's names, read at run time and never printed), every file read whole and `.gz` decompressed: **0 hits** on every file of this folder, `RETURN.md` and `SHA256SUMS` included. A positive control on planted forms (a strict path, a junit host attribute, and the machine's name in a `.gz` file) hit all three;
  - `git status --ignored` on the records folder: the folder is untracked and nothing in it is ignored (`git status --ignored` shows no `!!` entry, and `git check-ignore` matches no file), so ROOT can add it without forcing anything.
- **Cleanup:**
  - deleted the five tree copies (`S/i4`, `S/head`, `S/final`, `S/mut`, `S/pre`) and `S/tmp/`;
  - kept the scripts and outputs in `S/`;
  - kept the three CLI builds in `WT/targets/i100-b1-i4p-py/` for SC, where I am I-PY.

## 10. Records

`RETURN.md`, and `SHA256SUMS` over `_run_records/`:
- `diff/`: `commits.txt`, `diffstat.txt`, `i4p_py.diff` (I4..`8fa5aac15c`), `docstring_followup.diff` (`8fa5aac15c`..HEAD), `ast_same.txt`.
- `static/`: `heads.txt` (the readers' files at I4 against RV113's heads), `copies.txt`.
- `census/`: `census_{i4,head,final}.jsonl.gz` (`head` = `8fa5aac15c`, `final` = HEAD), `I4_VS_RV113_PY2.json`, `HEAD_VS_I4.json`, `FINAL_VS_I4.json`.
- `probes/`:
  - `inputs.txt` (every RV113 input used, with its sealed sum);
  - `probes_i100x.json.gz`;
  - `{i4,head,final}_probes_{ts1,r2x,i100x}.jsonl.gz`;
  - `I4_PROBES_TS1.json`, `HEAD_PROBES_TS1.json`, `FINAL_PROBES_TS1.json`, `HEAD_PROBES_R2X.json`, `FINAL_PROBES_R2X.json`, `HEAD_DIFF_CLASSES.json`, `FINAL_DIFF_CLASSES.json`.
- `suites/`: `py_{i4,head,final}.xml.gz` and `.tail`, `SUITE_COMPARE_I4_HEAD.json`, `SUITE_COMPARE_I4_FINAL.json`, `SUITE_COMPARE_HEAD_FINAL.json`.
- `mutants/`: `MUTANTS.json`, `MUTANT_TABLE.json`, and `runs/<id>/` (`junit.xml.gz`, `pytest.tail`) for NONE, M1–M10 and PRE.
- `scripts/`: every script I ran. RV113's `rv113_py_harness.py` was used as published (sha256 in `probes/inputs.txt`) and is not copied.
- `host/`: `binaries.txt`, `cargo_jobs_i100.log` (my lines of the guard's job log), and `job_logs/` (each job's stamps and output).
