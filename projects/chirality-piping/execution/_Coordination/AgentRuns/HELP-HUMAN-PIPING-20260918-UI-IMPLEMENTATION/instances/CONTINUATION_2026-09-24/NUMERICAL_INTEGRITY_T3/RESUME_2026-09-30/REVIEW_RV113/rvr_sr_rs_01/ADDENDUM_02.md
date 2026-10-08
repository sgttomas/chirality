# RV113 (RV-R), addendum 02: confirmation of SR-RS's repair round 2 (the three-reader alignment set)

TASK (Type 2), RV113, for ROOT (HELP_HUMAN, Agent 0), who is the return path. I made no delegation and wrote none of the change. 2026-10-08 UTC.

## Basis

- **The request:** the coordinator's message. Confirm I90's SR-RS repair round 2, which applies RR "RV113's three returns verified; I3 made at `2ba2f81863`; the three-reader alignment set ruled", items 1–4, to RS. Confirm independently:
  1. each item's gate and code, bound and unbound;
  2. the C2 table's branches, including the cross-code precondition rows;
  3. the census;
  4. the two changed tests;
  5. my own mutants;
  6. the metadata check against TS's and PY's.
- **I90's brief:** `R/BRIEFS/B1_SR_RS_REPAIR_02.md`, sha256 `50b2ec70…0f94` (verified).
- **I90's record:** `R/I90/b1_sr_rs_01/REPAIR_02.md`, sha256 `a315bc7f954811a228dad850a279d5a6312bc4e140767d560cfe9038f47b115a` (verified), with SHA256SUMS.repair_02 (75 of 75 OK), committed on NUM at `d914194721`.
- **The candidate:** `codex/piping-t3-b1-r-20261007` at `6e3e4fe219733652e38c3878f6c63de8acbd9a40`, the branch tip in `WT/b1-r`. It is one commit over `b5cb7faaeb` and touches exactly two files:
  - RS, +390/−13;
  - `RE/tests/retained_precision_contract.rs`, +1,007/−35.

  `RE/src/source_blocks.rs` is unchanged. My archive copy's two files equal `git show` at the commit (`addendum_02/static/copies.txt`).
- **Order of reading.** I read the ruling, the diff and the candidate's tests first. Then I built and ran my own probes, the census, the suite and my mutant schema. Only after that did I read REPAIR_02.

**Placeholders:** WT, NUM, P, PP, RE, RS, R, RR as in my earlier records. TS is `P/apps/desktop/src/features/results/retainedPrecision.ts` (and `previewPhysicsEvidence.ts`); PY is `P/core/analysis_runs/retained_precision.py` (and `preview_physics_evidence.py`).

**My copies.** These are `git archive` copies of P without `execution/`:
- `WT/rv113/rs2-head` and `WT/rv113/rs2-mut` (`6e3e4fe219`);
- for comparison, `WT/rv113/ts-cmp` (TS at `7e47e51b5d`, SR-TS's reviewed head, with NMS linked and I71's eight wasm assets copied, sha256 verified) and `WT/rv113/py-cmp` (PY at `11cc14e3e6`, SR-PY's reviewed head, whose `preview_physics_evidence.py` is unchanged on `b1-p` since).

## CONFIRMED

**Every item reads as ruled, through `validate` and the transport entry, bound and unbound:**
- the census is unchanged;
- the suite's only changes are the six added tests;
- the two changed tests are faithful to the ruling;
- RS's metadata check is TS's, check for check.

The findings concern pins and records, not behaviour:
- S-1: twelve of the new checks are pinned by no RS test;
- N-1: the metadata check does not match PY's;
- N-2 and N-3: I90's "16 cross-code rows", and a pre-existing raw G7 code difference to note for SC.

| # | Confirm | Result | Evidence |
|---|---|---|---|
| 1 | Each item's gate and code, bound and unbound | **Yes.** 225 new probes read exactly as I expected, on all 401 stated verdicts. Of my earlier 135, 33 verdicts moved, each as ruled; nothing else changed | §1; `probes/RS2_PROBE_TABLE.json` |
| 2 | The C2 table's branches, including the cross-code precondition rows | **Yes.** Every branch, satisfied and broken, through `validate`. All 15 distinct cross-code pairs are refused in both admitted phases, and every pair in the three other phases. The ten keyed pairs are admitted | §2 |
| 3 | The census, 0 changes over 07m | **Yes.** 339 entries: 0 changes on input, bound, unbound, transport or standing; 0 misses | §3; `census/RS2_CENSUS_07M.json` |
| 4 | The two changed tests are faithful | **Yes** | §4 |
| 5 | My own mutants | **61 mutants: 46 killed by the candidate's tests, 3 equivalent, and 12 that only my probes kill** (S-1) | §5; `mutants/MUTANT_TABLE_R2.json` |
| 6 | The metadata check against TS's and PY's | **Equal to TS's, check for check, by reading and on all 41 metadata probes. PY differs on three** (N-1) | §6 |

## 1. Each item's gate and code, bound and unbound (my probes)

**My probe set** (`addendum_02/probes/`), 360 probes in all:
- my earlier 135: SR-TS's v5 (103), the (f)/(g) table (15) and the repair-01 table (17);
- 225 new ones (`gen_probes_r2.py`), written from the ruling, not from I90's tests. Each states my expected RS verdict per entry point (bound, unbound, transport).

RS at the head (`rs2_head_all.jsonl`) is compared with that expectation and, for the earlier 135, with RS at `b5cb7faaeb` (my published SR-TS and SR-PY outputs; RS there is byte-identical to `cc81e78801`). **All 225 new probes read exactly as I expected, on 401 stated verdicts. Every one of the earlier 135 either reads as before or moved as the ruling says.**

| Item | Probes | RS at `6e3e4fe219` |
|---|---|---|
| **1 (f) family at G3** | 9 new + the (f) table's 7: a wrong `material_bases[].index` (one basis; two swapped); a wrong `sources[].index` (one; two swapped); `case_indices` with a duplicate or out of range; a source owner naming another case's id, an unknown id, or an index out of range | **G3 COVERAGE bound and unbound,** all 16. At `b5cb7faaeb` they were G8 PREPARATION bound and admitted unbound, and the owner-id probe was G5 ATTEMPT |
| 1, an owner consistent but not the source's case | `f_src_owner_other_case_consistent` (source 1's owner is case 0, consistently) | G3 passes; **G5 ATTEMPT** bound and unbound (the Call position's binding, kept at G5) |
| **1, the ordinary basis at G5** | a dangling `material_basis_ref`; a basis listing no case; repair 01's three inputs (`r_b_basis_ref_7`, `r_c_basis_omits_case_1`, `r_c_missing_sourceless_basis`) | **G5 ATTEMPT bound and unbound.** The invocation-derived controls (cases out of order; an extra empty basis; (b) beside a second basis; the (e) materials) stay **G8 PREPARATION** bound and admitted unbound. 07j unedited is admitted |
| **2 (g) at G8 INVOCATION** | 23 model edits plus the (g) table's 8: `combinations`/`components` absent, `[]`, null, `{}`, an object, a string, 0, false, non-empty; `reference_configurations` null, `[]`, `{}`; `pressure_contract` null, `{}`, false, 0, `""`, `[]` | **Absent or `[]` admitted; every other value G8 INVOCATION;** `pressure_contract` null admitted. Unbound, all admitted (G8 is bound only) |
| 2, order | `combinations` null beside a P1 mode code 3 | **G8 INVOCATION** (the model-scope check precedes PREPARATION); the P1 defect alone is G8 PREPARATION |
| **3 C2 table** | §2 | as ruled, every branch |
| **4 transport** | 41 metadata probes (§6), and the eight N6 header probes | metadata defects: **G7 `SOURCE_PREVIEW_PHYSICS_EVIDENCE_INVALID`** on transport; header defects stay **G2** with the base code |

**Earlier probes that moved** (`RS2_PROBE_TABLE.json`, `earlier_sets_changed`). There are 33 verdict changes, each one the ruling's:
- the five C2 probes and `x_reason_cause_receipt_failure`: G5 ATTEMPT;
- the (f) table's seven: G3 COVERAGE bound and unbound;
- three (g) probes: G8 INVOCATION;
- repair 01's three (b)/(c) inputs: G5 ATTEMPT bound and unbound.

Nothing else in the 135 changed on any verdict.

**Against TS's present results** (`CROSS_TABLE.json`; TS at `7e47e51b5d`), on the earlier 135: **RS equals TS on all three verdicts for 120.** The 15 others are the same 15 that REPAIR_02 §3 lists, all on TS's side of the set:
- eight N6 header probes on transport;
- the two compound N6 probes;
- five (g) probes.

## 2. The C2 cause table, branch by branch

The ruling's table is item 3. RS (`g5_ordinary`, after O5) carries it as one `match`, for every unavailable case whose cause is not `prepared_product_failure`. By reading, each conjunct is the ruling's. By run, through `validate` (the full reader), I used four constructions:

| Construction | What it reaches |
|---|---|
| **C-a:** `two_case_synthetic`'s case 1 unavailable beside its Ready attempt and selected Run (21 probes) | `receipt_failure` with each of the three codes: **admitted** (D19 lets a Ready attempt carry `receipt_failure`). Phase routing, preparation, kernel or facade, or the codes `source_unavailable`, `facade_certificate`, `kernel_selected` or `caller_not_qualified`: **G5 ATTEMPT**. `facade_failure` satisfied: **G5 PRODUCT_ATTEMPT** (the table passes, then D19). Its phase routing, preparation, kernel or receipt, the code `receipt_encoding`, an owner naming case 0, or a combination owner: **G5 ATTEMPT**. A precondition, or a kernel reason, beside the selected Run: **G5 ATTEMPT** |
| **C-b:** `two_case_preparation_failure_synthetic`'s case 1 unavailable with no product attempt, source or Run (112 probes) | **Every `unavailable_precondition` pair:** 5 preconditions × 4 codes × 5 phases = 100 probes. Exactly the ten keyed pairs in phase routing or preparation are **admitted** (`needs_recompute`). The other 90 are **G5 ATTEMPT**: the **15 cross-code pairs** in both admitted phases, and every pair in phase kernel, facade or receipt. `source_error` with an equal decline: **admitted**; with no decline, a different error, phase routing, or code `caller_not_qualified`: **G5 ATTEMPT**. `receipt_failure` with its three codes: **admitted** (no Run needed); phase preparation: G5 ATTEMPT. `facade_failure` or a kernel reason with no Run: **G5 ATTEMPT** |
| **C-c:** the same base with its unavailable product attempt (6 probes) | each precondition with its keyed code: **G5 PRODUCT_ATTEMPT** (the table passes, then D19); a cross code: **G5 ATTEMPT** |
| **C-d:** F_BASE's case 1 with its own idle, refused Run (5 probes) | the kernel reason (`kernel_refused`, `kernel`, the terminal's reason): **G5 PRODUCT_ATTEMPT** (D19 next); code `kernel_unresolved`, phase facade, or another cause: **G5 ATTEMPT** |

**On the "16 cross-code precondition rows."** In `b1_r2_c2_cause_table_source_precondition_kernel`, I count 18 rows of "another precondition's code", all in phase `preparation`. They cover the 15 distinct (precondition, code) cross pairs: `source_unavailable` is repeated for `caller`, `resource_admission` and `upstream_no_wrap`. That test, and its `source_error`, precondition and kernel rows, read the ordinary class alone (`reader_logic::ordinary`). My C-b to C-d probes run the same branches through `validate`, in all five phases, with the same results. See N-2.

**Against TS** (`7e47e51b5d`), where TS's table is still the set form, RS differs only by the keying:
- TS admits the 15 cross-code pairs (60 verdicts, C-b);
- TS gives G5 PRODUCT_ATTEMPT on C-c's cross code.

Every other C2 probe reads the same in RS and TS. This is I92's item 3.

## 3. The census over 07m

My harness (`rv113_census.rs`, `c0dadef9…`, as published) ran in my copy of the head. It was compared with my RS census at `cc81e78801`, whose RS and `source_blocks.rs` are byte-identical to `b5cb7faaeb`'s (ADDENDUM_01). The result (`RS2_CENSUS_07M.json`):
- **339 entries** (17 bases, 294 mutations, 28 must-pass);
- **0 changes** in input, bound, unbound, transport or standing;
- **0 misses** against the corpus's Rust expectations (`expected_by_reader.rust`, else `expected`), the must-pass eligibilities and standings, and the bases.

The 07m mutations that carry non-`prepared_product_failure` causes (`unavailable_attempt_under_facade_failure_cause`, `…source_error_cause`, `preparation_error_selected_run_under_receipt_cause`, `ready_attempt_under_facade_failure_cause`) still read as before. Each carries its cause's C2 phase and code.

## 4. The suite, and the two changed tests

RE's whole suite, at the head (one cargo job), compared test by test with my run at `b5cb7faaeb` (ADDENDUM_01's `rsr_re_head.log`):
- **187 → 193 ok** for the candidate's tests, plus my two harness tests, which were absent from that pristine copy;
- **+6 added:** `b1_r2_f_family_at_g3_bound_and_unbound`, `b1_r2_ordinary_basis_reference_at_g5_attempt`, `b1_r2_g_model_scope_at_g8_invocation`, `b1_r2_c2_cause_table_receipt_and_facade`, `b1_r2_c2_cause_table_source_precondition_kernel`, `b1_r2_transport_metadata_at_g7`;
- **0 removed, 0 changed outcomes.**

**The two changed tests are faithful to the ruling.**
- **`d19_converse_cause_binding`.** The test is about D19, so each row must reach the product class. Now that C2's table runs first, each probe states its cause with a C2-consistent phase and code. Its intent is kept, with one honest exception:
  - The two `receipt_failure` rows now carry (`receipt_encoding`, `receipt`) and still reach D19 (G5 PRODUCT_ATTEMPT).
  - "A precondition beside the case's Run" now expects G5 ATTEMPT. No precondition can sit beside a Run, so no C2-consistent form reaches D19 there. D19 for a precondition cause stays pinned by the P′ row, which has no Run and still expects G5 PRODUCT_ATTEMPT.
  - The Ready-attempt row's cause became a satisfied `facade_failure` naming the case, and still reaches D19.
  - The last row's full `receipt_failure` reason still reaches G6.
- **`b1_d38_capture_before_any_run_beside_a_selected_case`.** Only its "cause not a prepared product failure" row changed. A `receipt_failure` cause with phase `preparation` breaks C2's receipt branch, so it is G5 ATTEMPT, as TS gives (RR's ruling 2 on I92's variant). The other 15 rows are unchanged.

My probes reproduce both changed expectations through `validate` (`x_reason_cause_receipt_failure`; C-a's `ca_precondition_beside_run`).

## 5. My mutants

**Method** (`harness/make_mutants_r2.py`):
- 61 edits in my copy of the head, each guarded by `mx("Nnn")` (`RV113_MUT`);
- one cargo build;
- each mutant as one slot job running RE's lib binary (26 tests) and its contract binary (76);
- then my 360 probes, for the control and for every mutant that survived the tests.

The control passes 102 of 102, and its probe verdicts equal the head's on all 360 probes × 3 entry points. A kill counts when a test fails at an assertion. Every failing test panics at an `assert!`/`assert_eq!` line, except one of N33's 27 failures: a test helper's `panic!` on a base that must pass.

| Id | Item | Mutant | Candidate's tests | My probes |
|---|---|---|---|---|
| N01 | 1 (f) | G3: a source's index at its position dropped | killed: f-family | — |
| N03 | 1 (f) | G3: the owner's case binding dropped (index range and id) | killed: f-family | — |
| N04 | 1 (f) | G3: the owner's case id against the case at its index dropped (index range kept) | killed: f-family | — |
| N05 | 1 (f) | G3: a material basis's index at its position dropped | killed: f-family | — |
| N06 | 1 (f) | G3: case_indices in range dropped | killed: f-family | — |
| N07 | 1 (f) | G3: case_indices unique dropped | killed: f-family | — |
| N08 | 1 G5 | G5 ordinary: the ordinary attempt's basis reference dropped | killed: ordinary basis | — |
| N09 | 1 G5 | G5 ordinary: the basis need only resolve (not list the case) | killed: ordinary basis | — |
| N10 | 2 (g) | G8: combinations back to the old list(..).is_empty() (null and non-arrays admitted) | killed: (g) | — |
| N11 | 2 (g) | G8: components back to the old list(..).is_empty() | killed: (g) | — |
| N12 | 2 (g) | G8: combinations and components may be null | killed: (g) | — |
| N13 | 2 (g) | G8: reference_configurations check dropped | killed: (g) | — |
| N14 | 2 (g) | G8: pressure_contract false admitted | killed: (g) | — |
| N15 | 3 C2 | the whole C2 table dropped | killed: 4 tests | — |
| N16 | 3 C2 | source_error: phase dropped | killed: C2 source/precondition/kernel | — |
| N17 | 3 C2 | source_error: code dropped | killed: C2 source/precondition/kernel | — |
| N18 | 3 C2 | source_error: no Run dropped | **survives** | equivalent: O5 refuses a source_decline beside a Run first (G5 ATTEMPT) |
| N19 | 3 C2 | source_error: the decline's error equality dropped | killed: C2 source/precondition/kernel | — |
| N20 | 3 C2 | unavailable_precondition: phase dropped | killed: C2 source/precondition/kernel | — |
| N21 | 3 C2 | unavailable_precondition: no Run dropped | **survives** | killed: ca_precondition_beside_run |
| N22 | 3 C2 | unavailable_precondition: keying replaced by TS's present set (any of the four codes) | killed: C2 source/precondition/kernel | — |
| N23 | 3 C2 | unavailable_precondition: source_family's keyed code refused | killed: C2 source/precondition/kernel | — |
| N24 | 3 C2 | unavailable_precondition: an unknown precondition admitted | **survives** | equivalent: the schema's precondition enum refuses an unknown precondition first (G1) |
| N25 | 3 C2 | receipt_failure: phase dropped | **survives** | killed: ca_receipt_phase_facade, ca_receipt_phase_kernel, ca_receipt_phase_preparation, ca_receipt_phase_routing, cb_receipt_phase_preparation |
| N26 | 3 C2 | receipt_failure: code set dropped | killed: C2 receipt/facade | — |
| N27 | 3 C2 | receipt_failure: invocation_not_representable removed from the set | killed: C2 receipt/facade | — |
| N28 | 3 C2 | facade_failure: phase dropped | killed: C2 receipt/facade | — |
| N29 | 3 C2 | facade_failure: code dropped | killed: C2 receipt/facade | — |
| N30 | 3 C2 | facade_failure: selected Run dropped | **survives** | killed: cb_facade_no_run |
| N31 | 3 C2 | facade_failure: owner_ref dropped | killed: C2 receipt/facade | — |
| N32 | 3 C2 | kernel: phase dropped | killed: C2 source/precondition/kernel | — |
| N33 | 3 C2 | the table also applied to prepared_product_failure causes | killed: 27 tests | — |
| N34 | 3 C2 | kernel: a Run present dropped | **survives** | equivalent: with no Run, the code and cause conjuncts cannot hold |
| N35 | 3 C2 | kernel: code dropped | killed: C2 source/precondition/kernel | — |
| N36 | 3 C2 | kernel: cause equal to the terminal's reason dropped | killed: C2 source/precondition/kernel | — |
| N40 | 4 T | the metadata check not run | killed: transport | — |
| N41 | 4 T | the metadata check reported at G2 instead of G7 | killed: transport | — |
| N42 | 4 T | metadata: the namespace demand dropped | killed: transport | — |
| N43 | 4 T | metadata: the demand 'formulation profile or limitations' dropped | killed: transport | — |
| N44 | 4 T | metadata: the demand 'transport evidence shape (both demands)' dropped | killed: transport | — |
| N45 | 4 T | metadata: the demand 'preview case shape' dropped | **survives** | killed: t_case_extra_member |
| N46 | 4 T | metadata: the demand 'preview case identity' dropped | killed: transport | — |
| N47 | 4 T | metadata: the demand 'maximum coverage values' dropped | **survives** | killed: t_coverage_duplicate_ids |
| N48 | 4 T | metadata: the demand 'maximum coverage overlap' dropped | **survives** | killed: t_coverage_overlap |
| N49 | 4 T | metadata: the demand 'maximum coverage completeness' dropped | killed: transport | — |
| N50 | 4 T | metadata: the demand 'support both attributed and withheld' dropped | killed: transport | — |
| N51 | 4 T | metadata: the demand 'withheld support values' dropped | killed: transport | — |
| N52 | 4 T | metadata: the demand 'extrema identity or basis' dropped | killed: transport | — |
| N53 | 4 T | metadata: the demand 'extrema fractions' dropped | killed: transport | — |
| N54 | 4 T | metadata: the demand 'extrema integers' dropped | killed: transport | — |
| N55 | 4 T | metadata: the demand 'extrema bounds' dropped | killed: transport | — |
| N56 | 4 T | metadata: the demand 'extrema member partition' dropped | **survives** | killed: t_extrema_pipe_duplicate, t_extrema_pipe_in_unavailable |
| N57 | 4 T | metadata: the demand 'intensified measure identity' dropped | killed: transport | — |
| N58 | 4 T | metadata: the demand 'intensified measure inputs' dropped | **survives** | killed: t_measure_moment_string, t_measure_sif_zero |
| N59 | 4 T | metadata: the demand 'attribution sets differ between cases' dropped | killed: transport | — |
| N60 | 4 T | metadata: the demand 'duplicate evidence result binding' dropped | **survives** | killed: t_measure_duplicate_result |
| N61 | 4 T | metadata: the demand 'combination gate reason' dropped | killed: transport | — |
| N62 | 4 T | metadata: the demand 'combination gate identity' dropped | killed: transport | — |
| N63 | 4 T | metadata: the demand 'extrema shape' dropped | **survives** | killed: t_extrema_extra_member |
| N64 | 4 T | metadata: the demand 'intensified measure shape' dropped | **survives** | killed: t_measure_extra_member (`probes_r2x.json`) |
| N65 | 4 T | metadata: the demand 'combination gate shape' dropped | **survives** | killed: t_gate_extra_member (`probes_r2x.json`) |

**Totals: 61 mutants.**
- **46 are killed by the candidate's tests.**
- **3 are equivalent at the reader:** N18, N24 and N34.
- **12 survive every RS test but change a verdict** (S-1):
  - **C2:** N21 (the precondition's no-Run conjunct), N25 (the receipt branch's phase) and N30 (the facade branch's selected Run). Each is killed by my probes.
  - **The metadata check:** nine demands. N45, N47, N48, N56, N58, N60 and N63 are killed by my probes. N64 (a measure's shape) and N65 (a gate's shape) are killed by two extra probes, a measure and a gate each with an extra member (`probes/probes_r2x.json`, run on the control, N64 and N65; the control refuses both at G7 `…EVIDENCE_INVALID`).

**Why the tests miss them:**
- I90's C2 test breaks a branch by changing phase and code together. For example, "receipt_failure with phase kernel" carries the code `kernel_unresolved`, so the code conjunct refuses it whatever the phase.
- Its precondition rows never put a precondition beside a Run with a keyed code and an admitted phase.
- No row puts a `facade_failure` on a case without a Run.
- `b1_r2_transport_metadata_at_g7` has no row for those nine demands.

PY's repair-02 test does break each conjunct alone.

## 6. The metadata check, against TS's and PY's

**By reading.** RS's `preview_physics_transport_metadata` is TS's `validatePreviewPhysicsTransportMetadata`, check for check, in TS's order:
- the namespace;
- the formulation basis's shape, then its profile and limitations;
- `contract_evidence`'s shape and lists;
- `readCases`: each case's shape, identity, lists, coverage, attribution and withheld records, extrema, partition and measures; then the cross-case attribution sets and duplicate result ids;
- `readGates`.

Every detail string is TS's.

Two differences are not behavioural:
- TS's finite-tree walk has nothing to refuse in Rust, because serde_json has no non-finite number;
- TS's `strings`/`text` and RS's `nonempty`/`strings` agree on every JSON type.

**By run** (§1, item 4). Each reader ran as its own locked job on my 41 metadata probes:
- **RS equals TS on all 41** transport verdicts. Across all 360 probes, RS equals TS on transport except the ten header-defect probes, which RS refuses at G2 and TS will check in I92's round.
- **PY differs from both on three** (N-1):

| Probe | RS | TS | PY |
|---|---|---|---|
| `t_extrema_global_upper_string` (`global_upper_bound_pa` a string) | admitted | admitted | G7 `…EVIDENCE_INVALID` |
| `t_extrema_certified_gap_null` (`certified_gap_pa` null) | admitted | admitted | G7 `…EVIDENCE_INVALID` |
| `t_withheld_duplicate_multiset` (case 0 withholds `s` twice, case 1 once) | G7 `…EVIDENCE_INVALID` | G7 `…EVIDENCE_INVALID` | admitted |

PY's check is not TS's in three ways:
- it validates `contract_evidence` against the results schema's `PreviewPhysicsContractEvidence` (types throughout);
- it has an "extrema numbers" demand on `global_upper_bound_pa` and `certified_gap_pa`;
- it compares the attribution dispositions as sets, not as sorted lists.

So RS's doc comment, and REPAIR_02 §1 item 4, overstate the match: "and PY's … check for check" holds for TS only.

One shape I first built could not be a probe: a `span_index` of 1e300, which TS and RS would refuse as unsafe and PY's integer test would admit. A statement carrying it cannot be hashed under checked JSON (`CHECKED-JSON-UNSAFE-INTEGRAL-FLOAT`), so no receipt can carry it, and I dropped it.

## Findings

| # | Severity | Where | Finding | Recommendation |
|---|---|---|---|---|
| S-1 | SHOULD-FIX | `RE/tests/retained_precision_contract.rs` (`b1_r2_c2_cause_table_*`, `b1_r2_transport_metadata_at_g7`) | **Twelve of the new checks are pinned by no RS test** (§5). <br>• C2: the precondition's no-Run conjunct (N21), the receipt branch's phase alone (N25) and the facade branch's Run (N30). <br>• The metadata check: the case shape (N45), the coverage values (N47), the coverage overlap (N48), the extrema partition (N56), the measure inputs (N58), duplicate result ids (N60), and the extrema, measure and gate shapes (N63–N65). <br>Each mutant changes RS's verdict on my probes, and each check is right at the head. This is the same class as round 1's S-1 | Add one row per check, breaking that conjunct alone: <br>• `ca_precondition_beside_run`; <br>• `ca_receipt_phase_*` with `receipt_encoding`; <br>• `cb_facade_no_run`; <br>• the nine T probes. <br>This is test-only; I can confirm it as I did round 1. 07n's C2 rows (by the ruling) will also pin the three C2 ones in every reader |
| N-1 | NOTE | RS `preview_physics_transport_metadata`'s doc comment; REPAIR_02 §1 item 4 | **The metadata check is TS's, check for check, but not PY's.** PY refuses `global_upper_bound_pa` or `certified_gap_pa` when not a number (its "extrema numbers" demand and its schema shape), and admits withheld records that differ between cases only in multiplicity (it compares sets). RS and TS do the opposite on those three probes (§6). Item 4 says PY and TS "keep" their checks, so this is a three-reader difference on transport, not a defect in RS | Correct the comment. ROOT rules which form the three readers share (TS's and RS's, or PY's), in I91's or a later round |
| N-2 | NOTE | REPAIR_02 §1 item 3 | **"16 rows" is 18 rows over 15 distinct cross pairs, in phase `preparation` only, and they read `reader_logic::ordinary`, not `validate`.** The behaviour is right: my full-reader probes cover all 15 pairs in all five phases | Record only |
| N-3 | NOTE | RS and TS raw G7 (pre-existing; not this round) | **On a statement whose preview-physics evidence is defective, the raw (bound and unbound) G7 codes differ.** RS's raw evidence reader gives specific codes (`…EXTREMA_SUBDIVISIONS`, `…STRESS_COVERAGE_PARTITION`, `…INTENSIFIED_RESULT_MISSING`, …); TS gives `…EVIDENCE_INVALID`. My 41 T probes show it bound and unbound. 07m declares one such split (`g7_maximum_off_enclosure`) | For SC: 07n entries with evidence defects need per-reader expectations, or none of them |

## For ROOT

1. **CONFIRMED.** RS at `6e3e4fe219` implements items 1–4 as ruled. ROOT may merge it for I4.
2. **S-1** is a test-only follow-up. Twelve rows would pin checks that no RS test reads today. Take it before I4 or with SC's 07n, as ROOT prefers.
3. **N-1:** rule the shared form of the transport metadata check. RS and TS now agree on all 41 of my metadata probes; PY differs on three.
4. **For I92's round** (now at `6fa6a64658`, my next item): `f_src_owner_other_case_consistent` and the (g) ordering probes are in my set.

## Host

- **Cargo:** three cargo jobs through `WT/tools/t3_cargo.sh` (`--locked --offline`):
  - the head's test build (target `WT/targets/rv113-rs2`);
  - the mutant copy's test build (`WT/targets/rv113-rs2mut`);
  - the head's whole RE suite.

  Two more built the PY authorities (`WT/targets/rv113-pybins2`; sha256 equal to my SR-PY builds and I91's).
- **Slot jobs** through `WT/tools/t3_slot.sh`, one at a time, each the only heavy job of mine:
  - the harness binary (census, then probes; the first probe run stopped at a probe that cannot be hashed (§6), and the second ran the 360);
  - the TS vitest probe run and the PY probe run;
  - the control's and 61 mutants' test binaries;
  - the control's and the 15 survivors' probe runs;
  - the two extra probes on the control, N64 and N65.

  No test binary, pytest or vitest ran outside a slot. My lines in `WT/guard/cargo_jobs.log` are in `addendum_02/host/`.
- **Waits: slips, disclosed.** Each job had its own waiter (its background completion, or one foreground loop), and each waiter ended with its job. But I also watched three jobs twice:
  - the mutant chain, whose waiter outlived the tool's 10-minute limit and continued in the background: I also polled its progress with two short loops;
  - the survivors' probe chain: a blocking loop beside its background waiter;
  - one accidental second background waiter on that chain, which I stopped at once (my own task).

  These were extra watchers, not extra jobs, and none outlived its job. None of mine remain. I killed no job.
- **Records:**
  - no symlink, and no folder named `build`;
  - no junit output;
  - placeholder paths only;
  - screened, `.gz` files decompressed, with the strict pattern and the host name.
- **Not done:** no DEC-025, installs or Git writes (`git archive` and reads only, with `GIT_OPTIONAL_LOCKS=0`). I did not rerun PP's suite or the c = 1 pins. RS's production change reaches PP's precommit through `validate`, and my census shows `validate` reading all 339 entries, including the u8 L = 0 successor bases, exactly as before.
- **Cleanup:**
  - I deleted my copies (`WT/rv113/{rs2-head,rs2-mut,ts-cmp,py-cmp}`), including the NMS link and the wasm assets;
  - I deleted the targets (`WT/targets/rv113-{rs2,rs2mut,pybins2}`);
  - scratch is kept in `WT/scratch/rv113_rvr_01/rsr2/`.

## Records (`addendum_02/`)

- `static/`: `copies.txt` (file hashes against `git show`), `wasm_assets.sha256`.
- `harness/`:
  - `gen_probes_r2.py`, `compare_r2.py`, `make_mutants_r2.py`, `mutant_table_r2.py`;
  - `rsr2_job.sh`, `run_mutants_r2.sh`, `run_mutants_r2_all.sh`, `make_rsr2_copies.sh`.
- `probes/`:
  - `probes_r2.json`, `probes_all.json`;
  - RS's, TS's and PY's outputs (`rs2_head_all.jsonl`, `ts_cmp_all.jsonl`, `py_cmp_all.jsonl`);
  - `RS2_PROBE_TABLE.json`, `CROSS_TABLE.json`.
- `census/`: `rs2_head.jsonl`, `RS2_CENSUS_07M.json`.
- `suites/`: `SUITE_RE_R2.json`, `rs2_suite.log`.
- `mutants/`: `MUTANTS_R2.json`, `MUTANT_TABLE_R2.json`, and `runs/<id>/` (run stamps; the lib and contract logs, gzipped; the probe runs).
- `host/`: `cargo_jobs_rv113_r2.log`, `job_stamps.txt`.
