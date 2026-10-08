# I101 B1, the reader follow-up toward I4′: RS's and TS's lanes (rulings 2, 3 and 4)

TASK (Type 2), I101 (I-RS and I-TS), for ROOT (HELP_HUMAN, Agent 0), who is the return path. I made no delegation. 2026-10-08 UTC.

## The basis

- **The brief:** `R/BRIEFS/B1_I4P_RS_TS.md`, sha256 `e974b819b34181a1f5fc8fcf245255e56b113081b33af4b5c04bf42e716f1daf` (verified). Also read and verified: `B1_COMMON.md` (`2d170307…2c75`), `B1_SR_RS.md` (`9c0bb8ac…e0e2`), `B1_SR_TS.md` (`9698cd33…edbfe`), and `NUM/AGENTS.md` and `NUM/agents/AGENT_TASK.md`. Where they differ, the I4′ brief governs (the four-slot host rule; TS's fence widened to `previewPhysicsEvidence.ts` and its test).
- **The specification:** RR "I4 made at `30f3d1b24a`; RV113's items for ROOT ruled; …", rulings 2, 3 and 4.
- **Read:** RV113's SR-RS addendum 02 (`c43317f8…682d`, verified): §5, §6, S-1, N-1 and "For ROOT"; RV113's SR-TS addendum 01 (`5f86b3e7…97d6`, verified): S-1 and N-1. ROOT's I4 record `T/IMPLEMENTATION/B1_I4/RECORD.md` and its `_run_records/run_i4_ts.sh`, for the vitest method.
- **RV113's tools, used unchanged** (each hash equals RV113's own SHA256SUMS): `rv113_census.rs` `c0dadef9…5018`, `rv113Census.test.ts` `abcc6e36…2b45`, `make_mutants_r2.py` `5d2398e5…1ad3`, `probes_ts1.json.gz` `4fe5d584…dd29` (SR-TS addendum 01; its content equals `rvr_sr_py_01/addendum_01/probes/probes_ts1.json.gz`'s), `probes_r2x.json` `8d1c33d2…5c90`.

**Placeholders:** WT, NUM, P, RE, DT, T, R, RR and VENV as in the brief; RS is `RE/src/retained_precision.rs`, RT its contract test `RE/tests/retained_precision_contract.rs`; TS is `DT/features/results/retainedPrecision.ts`, PPE `DT/features/results/previewPhysicsEvidence.ts`; PY is `P/core/analysis_runs/preview_physics_evidence.py`. APPWT is the checkout whose `node_modules` was linked into my scratch copies.

**State: done.** Three commits, none pushed (ROOT pushes):

| Lane | Worktree and branch | Commits over I4 (`30f3d1b24a`) | Head |
|---|---|---|---|
| RS | `WT/b1-r`, `codex/piping-t3-b1-r-20261007` | `990339d94f` (ruling 2, RS's side; the N-1 doc comment), `e879118348` (ruling 4's rows) | **`e879118348`** |
| TS | `WT/b1-t`, `codex/piping-t3-b1-t-20261007` | `819e44f63e` (rulings 2, TS's side, and 3) | **`819e44f63e`** |

RS's commits touch RS (+18/−6) and RT (+342), and TS's commit touches PPE (+4/−1), its test (+33) and `retainedPrecision.test.ts` (+33). No other file, no PY file and no corpus file changed. No 07m verdict changed, so no stop fired.

## 0. First: the census over 07m at I4 (the stop check)

Before any change, in `git archive` copies of P at I4 (without `execution/`), RV113's harnesses ran 07m's 339 entries (17 bases, 294 mutations, 28 must-pass) and the 394 probes (§3) in RS (one cargo job) and in TS (one vitest job) (`census/`, `probes/`).
- **RS at I4 equals RV113's RS census at `6e3e4fe219`** (`rvr_sr_rs_01/addendum_02/census/rs2_head.jsonl.gz`) on every entry: input digests and every verdict in full (bound, unbound, transport and standing, details included). 0 misses against the corpus's Rust expectations.
- **TS at I4 equals RV113's TS census at `6fa6a64658`** (`rvr_sr_ts_01/addendum_01/census/census_ts1_head.jsonl.gz`) on every entry, in full. 0 misses against the corpus's TypeScript expectations.
- **On RV113's 392 probes,** RS and TS at I4 equal RV113's recorded outputs at those heads verdict for verdict (`rs2_head_ts1.jsonl.gz`, `ts1_head.jsonl.gz`).

RE and TS at I4 are byte-identical to the reviewed heads (`git diff` shows only the two W-C2 successor fixtures in those trees), so this was the expected result. No unexpected verdict change: the work went on.

## 1. The changes and their evidence, item by item

### Item 1: ruling 2, the extrema-number demand on transport

**RS (`990339d94f`).** `preview_physics_transport_metadata` gains one demand in its extrema loop, right after "extrema identity or basis" (PY's place):

```rust
demand(
    ["global_upper_bound_pa", "certified_gap_pa"]
        .iter()
        .all(|k| number(&x[*k]).is_some()),
    "extrema numbers",
)?;
```

`number` is the check's existing JSON-number reader, so a string, null, boolean, list or object is refused, and an integer is a number. The refusal is G7 `SOURCE_PREVIEW_PHYSICS_EVIDENCE_INVALID` with PY's detail text, "extrema numbers". Nothing else changed: the duplicate-withheld refusal (the sorted-list comparison of the attribution sets) is kept, as the ruling requires. RS's raw path is untouched: its base reader still refuses both shapes at G7 `SOURCE_PREVIEW_PHYSICS_NUMBER_INVALID`, the declared per-reader raw code.

**TS (`819e44f63e`).** The same demand, with the same detail, at the same place in PPE's `readCases` extrema loop:

```ts
demand(finite(x.global_upper_bound_pa) && finite(x.certified_gap_pa), "extrema numbers");
```

`readCases` is the one function that both `validatePreviewPhysicsTransportMetadata` (transport) and `validatePreviewPhysicsEvidence` (raw, through `validate`) call. So the transport check stays one function, shared with `StressNeutralExportPanel.tsx`, and the one demand serves ruling 2 on transport and ruling 3 on the raw path (§6 lists the callers). The comment above the next demand now says the two members are typed, never bounded (A2 1's "no certified-gap bound" stands).

**Tests.**
- RS, `b1_i4p_transport_extrema_numbers_at_g7` (new), on `ordinary_prepared_synthetic`, by the transport entry, asserting gate, code and detail:
  - refused at G7 "extrema numbers": `global_upper_bound_pa` a string, null or a boolean; `certified_gap_pa` null, a string or a list;
  - admitted (not eligible): the base, and both members written as JSON integers;
  - order: a string bound beside a fraction above 1 is "extrema numbers"; the fraction alone stays "extrema fractions";
  - raw, bound and unbound: RV113's two shapes stay G7 `SOURCE_PREVIEW_PHYSICS_NUMBER_INVALID`.
- TS, PPE's test (new `describe`, 7 tests): the same six shapes, each refused with `SOURCE_PREVIEW_PHYSICS_EVIDENCE_INVALID: extrema numbers` by both `validatePreviewPhysicsEvidence` and `validatePreviewPhysicsTransportMetadata`, on two producer fixtures (`preview_physics_connected_sparse`, and `preview_physics_invented_sparse` at its first and at its second case's fourth extremum); integers admitted by both; the order rows as in RS.
- TS, `retainedPrecision.test.ts` (new `describe`, 1 test): through the retained reader, RV113's two shapes and two more are G7 `SOURCE_PREVIEW_PHYSICS_EVIDENCE_INVALID`, detail "extrema numbers", bound, unbound and on transport; integers and the base read as before (bound eligible, unbound and transport admitted, not eligible).

### Item 2: ruling 3, TS's raw extrema typing

The demand above, in `readCases`, runs in `validatePreviewPhysicsEvidence`'s extrema loop (`validate` → `readCases`), after `header`'s finite-tree walk. RV113's SR-TS addendum 01 S-1 false accept is closed: `t_extrema_global_upper_string` and `t_extrema_certified_gap_null` were admitted (eligible bound) and are now refused at G7 with TS's raw base code, `SOURCE_PREVIEW_PHYSICS_EVIDENCE_INVALID`, bound and unbound (§3). RS's raw code for the same shapes stays `…NUMBER_INVALID` (B1_SC item 13's declared class). The tests are item 1's (both checks are asserted in every TS row).

### Item 3: ruling 4, RS's twelve unpinned checks (`e879118348`, test-only)

One row per check, each breaking that conjunct alone, in two new tests:
- **`b1_i4p_c2_conjuncts_alone`**, by `validate`, bound and unbound, each G5 ATTEMPT:
  - N21, the precondition's no-Run conjunct: RV113's `ca_precondition_beside_run` (07j's two-case base, case 1 unavailable beside its Ready attempt and selected Run; `unavailable_precondition` `capture` with its keyed code `source_unavailable`, phase `preparation`);
  - N25, the receipt branch's phase: `ca_receipt_phase_kernel` (`receipt_failure` with `receipt_encoding`, phase `kernel`), on the same construction;
  - N30, the facade branch's selected Run: `cb_facade_no_run` (the preparation-failure base, case 1 unavailable with no product attempt, source or Run; a `facade_failure` with phase `facade`, code `facade_certificate` and its own case as owner).
- **`b1_i4p_transport_metadata_demands_alone`**, by the transport entry, each refused by its own demand (gate, code and detail), beside two controls (a valid intensified measure; a valid withheld gate), both admitted:
  - N45 a preview case with another member ("preview case shape");
  - N47 an unavailable pipe listed twice ("maximum coverage values");
  - N48 a pipe both unavailable and outside the domain ("maximum coverage overlap");
  - N56 an extremum's pipe listed unavailable ("extrema member partition");
  - N58 a measure's moment written as a string ("intensified measure inputs");
  - N60 two measures with one result id ("duplicate evidence result binding");
  - N63 an extremum with another member ("extrema shape");
  - N64 a measure with another member ("intensified measure shape");
  - N65 a gate with another member ("combination gate shape").

RV113's twelve mutants are each killed by these rows (§5).

### Item 4: RS's doc comment (RV113 N-1; `990339d94f`)

`preview_physics_transport_metadata`'s doc comment now says: it is TS's `validatePreviewPhysicsTransportMetadata`, check for check, in TS's order and with TS's detail texts; since ruling 2, TS's check and this one share PY's extrema-number demand ("extrema numbers"); TS's check with that demand is the ruled shared form, and the comment claims no other agreement with PY's check. The old text's "(and PY's `preview_physics_evidence.validate_transport_metadata`) check for check" is gone.

## 2. The census over 07m: I4 against the heads

The same harnesses ran in copies of the heads: RS at `e879118348` (cargo job), TS at `819e44f63e` (vitest job). The corpus is byte-identical at I4 and at both heads. Compared entry by entry with my I4 census (`compare.py census`; `census/CENSUS_*.json`):

| Reader | Entries | Inputs differing | Verdict changes (bound, unbound, transport; RS also standing; in full, details included) | Misses against the corpus's expectations, I4 / head |
|---|---|---|---|---|
| RS | 339 | 0 | **0** | 0 / 0 (`expected_by_reader.rust`, else `expected`; must-pass eligibilities and standings; bases) |
| TS | 339 | 0 | **0** | 0 / 0 (`expected_by_reader.typescript`, else `expected`; the same) |

No 07m entry carries a non-number `global_upper_bound_pa` or `certified_gap_pa` (every base's members are numbers, and the only two entries that edit `contract_evidence`, `g7_maximum_off_enclosure` and `g7_contract_evidence_null`, touch neither), so the census could not move, and did not.

## 3. RV113's probes

**The set** (394): RV113's 392 in `probes_ts1.json` (its SR-RS round-2 360, which hold the 40 T-section metadata probes, plus 31 header probes and one owner-kind probe), and the two in `rvr_sr_rs_01/addendum_02/probes/probes_r2x.json` (a measure and a gate each with an extra member). RV113's addendum counts its metadata probes as 41; its files hold the 40 T-section probes and the 2 r2x probes, and I ran all 42 with the rest. `probes_i101.json` (sha256 `94f07f4f…fa9b`) is their concatenation, rebuilt by `harness/build_probes.txt`.

**Changes from I4** (`compare.py probes`, every verdict in full; `probes/PROBES_*_I4_VS_HEAD.json`): exactly these, and no other verdict or detail on any probe:

| Probe | Reader | Bound | Unbound | Transport |
|---|---|---|---|---|
| `t_extrema_global_upper_string` | RS | G7 `…NUMBER_INVALID` (unchanged) | G7 `…NUMBER_INVALID` (unchanged) | admitted → **G7 `…EVIDENCE_INVALID`**, "extrema numbers" |
| `t_extrema_certified_gap_null` | RS | G7 `…NUMBER_INVALID` (unchanged) | G7 `…NUMBER_INVALID` (unchanged) | admitted → **G7 `…EVIDENCE_INVALID`**, "extrema numbers" |
| `t_extrema_global_upper_string` | TS | admitted, eligible → **G7 `…EVIDENCE_INVALID`** | admitted → **G7 `…EVIDENCE_INVALID`** | admitted → **G7 `…EVIDENCE_INVALID`** |
| `t_extrema_certified_gap_null` | TS | admitted, eligible → **G7 `…EVIDENCE_INVALID`** | admitted → **G7 `…EVIDENCE_INVALID`** | admitted → **G7 `…EVIDENCE_INVALID`** |

(TS's detail is "extrema numbers" on all six.)

**RS against TS at the heads** (`probes/CROSS_HEAD.json`):
- **transport: equal on all 394**, and on every refusal the detail text after the code is the same;
- **both refuse the two extrema shapes at G7 `SOURCE_PREVIEW_PHYSICS_EVIDENCE_INVALID` on transport;**
- **TS refuses them bound and unbound at G7** (`…EVIDENCE_INVALID`); RS refuses them there with its declared raw code (`…NUMBER_INVALID`);
- raw (bound or unbound): 45 probes differ, the same 45 as at I4. They are RV113's 43 on the 392 (the declared raw-code class and the N6 class) and the 2 r2x probes (RS's specific raw codes against TS's `…EVIDENCE_INVALID`). The two extrema shapes stay in the set, now as a code difference (both refuse) instead of a refusal against an admission.

**PY, for context only** (RV113's recorded run of PY at `2843a59a16`, I4's PY, `rvr_sr_py_01/addendum_01/probes/py2_head.jsonl.gz`; not my run, and I100 is changing PY now): on transport PY refuses the two extrema shapes at G7 `…EVIDENCE_INVALID`, so all three readers now agree on their gate and code. PY's transport detail is "transport evidence shape" (its schema typing of `contract_evidence` refuses them first), where RS and TS say "extrema numbers"; see "For ROOT". PY differs from RS's head on transport on seven other probes, all rulings 1 and 2's PY side (I100's lane): the two compound N6 probes, four header-order probes (`h_recovery_and_evidence_null`, `h_carrier_present`, `h_carrier_and_quality_defect`, `h_carrier_and_recovery`) and `t_withheld_duplicate_multiset`.

## 4. Suites against I4

All in clean copies (no harness file), each one heavy job (`suites/`):

| Suite | I4 | Head | Per-test difference |
|---|---|---|---|
| RE, all targets (`cargo test --locked --offline`; RS's head) | 193 ok | **196 ok** | **+3 added (ok):** `b1_i4p_transport_extrema_numbers_at_g7`, `b1_i4p_c2_conjuncts_alone`, `b1_i4p_transport_metadata_demands_alone`. 0 removed, 0 changed outcomes; the carrier test (`retained_precision_carriers.rs`, 17) is unchanged and ok |
| Desktop vitest, whole suite (TS's head) | 141 files, 3,629 passed | **141 files, 3,637 passed** | **+8 added (passed):** PPE's test, 7 (six `it.each` shapes and "admits integers; the demand precedes …"); `retainedPrecision.test.ts`, 1 ("a non-number member is refused at G7 …"). 0 removed, 0 changed outcomes |
| `tsc --noEmit -p tsconfig.json` | rc 0, no output | **rc 0, no output** | none |
| PP's two source-text guards that read RE (`--lib -- --exact`: `retained_memory::law_tests::reviewed_inputs_bind_the_lock_and_the_reader_statics`, `…::bindings_need_witnesses_inputs_and_reader_layouts`; RS's head) | (I90: ok) | **2 ok** | none. RS's change adds and removes no `include_str!` input and changes no reader layout |

RE's compiler warnings are the same two lines at I4 and at the head (the existing `derived` never used). rustfmt (1.9.0, edition 2021) reports no block on any line this round added or changed: RS's file count is 31 and RT's 108, as in I90's record at `6e3e4fe219`.

RS's first commit, `990339d94f`, was also run on its own: its contract test passes, 77 of 77 (I4's 76 and `b1_i4p_transport_extrema_numbers_at_g7`).

## 5. Mutants

**Method.** Each mutant is a guarded edit in a scratch copy of a head, never committed (`harness/make_mutants_rs.py`, `make_mutants_ts.py`; the schema diffs are in `mutants/`).
- **RS** (copy of `e879118348`): RV113's own schema applied unchanged (`make_mutants_r2.py`, its 61 mutants N01–N65, guarded by `RV113_MUT`; every anchor still matched once), then my two (X01, X02) under the same guard. One cargo build; then, per mutant and for the control, RE's lib unit-test binary (26) and RT's binary (79) as one slot job.
- **TS** (copy of `819e44f63e`): my two (Y01, Y02), guarded by `I101_MUT`; per mutant and for the control, PPE's test and `retainedPrecision.test.ts` (551 tests) as one slot vitest job with a JSON report.
- A kill counts when a test fails at an assertion: in RS, the panic's location is an `assert!` line (`b1_table`'s); in TS, the failure is an `AssertionError`. `harness/mutant_table.py` reads every run (`mutants/MUTANT_TABLE.json`).

**Controls:** RS passes 105 of 105 (26 + 79) with `RV113_MUT` unset; TS passes 551 of 551 with `I101_MUT` unset.

**My mutants, one per new check (each conjunct of the new demand), all killed by assertions:**

| Id | Reader | Mutant | Killed by (rows that missed) |
|---|---|---|---|
| X01 | RS | transport "extrema numbers": the `global_upper_bound_pa` conjunct dropped | `b1_i4p_transport_extrema_numbers_at_g7`: the three `global_upper_bound_pa` rows and the order row |
| X02 | RS | transport "extrema numbers": the `certified_gap_pa` conjunct dropped | `b1_i4p_transport_extrema_numbers_at_g7`: the three `certified_gap_pa` rows |
| Y01 | TS | `readCases` "extrema numbers" (raw and transport): the `global_upper_bound_pa` conjunct dropped | 5 tests: PPE's three `global_upper_bound_pa` shapes and its order test; the retained-reader test |
| Y02 | TS | the same, the `certified_gap_pa` conjunct dropped | 5 tests: PPE's three `certified_gap_pa` shapes and its order test; the retained-reader test |

**RV113's twelve, now killed by my rows** (each by exactly the row that breaks its conjunct; no other test fails):

| Mutant | Conjunct dropped | Killed by (the one row that missed) |
|---|---|---|
| N21 | C2 `unavailable_precondition`: no Run | `b1_i4p_c2_conjuncts_alone`: "unavailable_precondition, keyed, phase preparation, beside the selected Run" |
| N25 | C2 `receipt_failure`: phase | the same test: "receipt_failure, receipt_encoding, phase kernel" |
| N30 | C2 `facade_failure`: selected Run | the same test: "facade_failure, facade_certificate, phase facade, naming its case, with no Run" |
| N45 | preview case shape | `b1_i4p_transport_metadata_demands_alone`: N45's row |
| N47 | maximum coverage values | the same test: N47's row |
| N48 | maximum coverage overlap | N48's row |
| N56 | extrema member partition | N56's row |
| N58 | intensified measure inputs | N58's row |
| N60 | duplicate evidence result binding | N60's row |
| N63 | extrema shape | N63's row |
| N64 | intensified measure shape | N64's row |
| N65 | combination gate shape | N65's row |

**RV113's other 49:**
- **46 are killed as RV113 found them,** by the same tests (`mutants/mutants_vs_rv113.out` compares the failing tests, mutant by mutant). Four of them are now also killed by my new tests: N15 (the whole C2 table), N40 and N41 (the metadata check not run, or at G2), and N53 ("extrema fractions", by my order row).
- **N18, N24 and N34 survive**, the three RV113 judged equivalent at the reader (O5 refuses a source decline beside a Run first; the schema's precondition enum refuses an unknown precondition first; with no Run, a kernel reason's code and cause cannot hold).
- **N33** (the table applied to `prepared_product_failure` causes) fails 27 tests: 26 at assertions, and one at the test helper's `panic!` on a base that must pass (`complete_synthetic_controls_carry_their_shared_eligibility`), as RV113 recorded.

**Totals:** RS 63 mutants: 60 killed by assertions, 3 equivalent, 0 surviving otherwise. TS 2 mutants: 2 killed by assertions.

## 6. The callers each changed check reaches

**RS's change** is in `preview_physics_transport_metadata`, a private function whose only caller is `retained_precision::validate_transport_metadata` (the transport entry). That entry's callers:
- `semantic_contract::for_source_metadata`, on a retained statement only (`is_retained`: the producer's contract id is the retained one). Its non-test caller is the headless runner, `core/runner/headless/src/lib.rs` (the 0.3.0 result-envelope check, which reports `HEADLESS_RUNNER_RESULT_CONTRACT_UNSUPPORTED` when the metadata check refuses). `semantic_contract::for_source` calls `for_source_metadata` only on non-retained sources (its retained branch returns first through `validate`), so it never reaches this check; nor does `validate`'s own G7, which reads the projection (a preview-physics-1 header).
- RE's tests: RT, `retained_precision_carriers.rs` and the other `for_source_metadata` users in `RE/tests/` (all pass; §4).

**It does not reach `validate`**, so PP's precommit (`retained_precision::validate` in `core/product_physics`) and the c = 1 successor bytes are untouched by construction. I ran no PP pin and no solve; PP's two source-text guards that read RE pass at RS's head (§4).

**TS's change** is in PPE's `readCases`, which both PPE entry points run:
- `validatePreviewPhysicsTransportMetadata` (transport):
  - `retainedPrecision.ts` `validateRetainedPrecisionTransport`, at G7, whose callers are `StressNeutralExportPanel.tsx` `validateNeutralTransportEvidence` (the retained route, in `validateStressNeutralExportPacket`) and `numericalResultQuality.ts` `sourceContractTransport` (the retained route; no non-test caller);
  - `StressNeutralExportPanel.tsx` `validateNeutralTransportEvidence`, directly, on the plain preview-physics-1 route.
- `validatePreviewPhysicsEvidence` (raw):
  - `retainedPrecision.ts` `validateRetainedPrecision`, at G7, whose callers are `HistoricalRunContext.tsx`, `retainedPrecisionStanding.ts`, `retainedPrecisionDisclosure.ts` and `services/analysisRunCompatibility.ts` (`buildAnalysisRecord`, `validateAnalysisRunV03`);
  - on the plain preview-physics-1 route: `resultExportAdapter.ts` (`deriveResultDocument`, `validateResultDocument`), `numericalResultQuality.ts` (`numericalResultStanding`), `services/analysisRunCompatibility.ts` (`buildAnalysisRecord`, `validateAnalysisRunV03`) and `services/previewService.ts` (`validateCapturedSource`);
  - a test, `loadReferenceEvidence.parity.test.ts`.

So ruling 3's demand reaches every TS reading of a preview-physics-1 statement, plain or retained, raw or transport. The producer writes both members as numbers (`core/product_physics/src/lib.rs` and `preview_physics.rs` write the certified maximum's `upper_bound` and `certified_gap`, both `f64`), and every producer fixture still passes (§4), so no producer output is refused. RS's and PY's raw readers already refused both shapes on the plain route.

## 7. For ROOT

1. **Rulings 2, 3 and 4 are in RS and TS as ruled,** with 0 changes on 07m in either reader, and RS equal to TS on every transport verdict of RV113's probes. RV120 can confirm both heads against RV113's addenda and the ruling.
2. **A detail-text difference on transport, for SC's item 14.** For the two extrema shapes, RS and TS report "extrema numbers"; PY at I4 reports "transport evidence shape", because its schema typing of `contract_evidence` refuses them before its own "extrema numbers" demand (RV113's recorded PY run). Gate and code agree in all three readers. If 07n pins only gate and code, there is nothing to declare; if it pins details, this is a per-reader detail unless I100's PY change moves it. On the raw path, RS keeps its declared raw code (`…NUMBER_INVALID`); TS and PY give `…EVIDENCE_INVALID`, both with the detail "extrema numbers".
3. **RS's production change is on the transport path only.** `validate` cannot reach it (§6), so PP's precommit and the c = 1 successor bytes cannot change, and I ran none of PP's pins: they run native solves, which my brief does not name. PP's two source-text guards that read RE ran instead (§4): they pass. Like I90's round, the change alters RS's text and rides in B1's one RS re-qualification.
4. **TS's change reaches the plain preview-physics-1 route as well as the retained one** (§6). It refuses only shapes the producer cannot write and RS's and PY's raw readers already refuse, and every producer fixture and the A2 shared tamper vector read as before (the vitest suite's only differences are the added tests).
5. **Next, by your message after SC writes 07n:** I-RS's and I-TS's harness pins and counts. These heads' counts are RE 196 (RT 79) and vitest 3,637 (PPE's test 50 → 57, `retainedPrecision.test.ts` 493 → 494).

## 8. Host

- **The four-slot rule.** Every cargo ran through `WT/tools/t3_cargo.sh` with `--locked --offline` (toolchain 1.97.1, `CARGO_INCREMENTAL=0`), each in its own target under `WT/targets/i101-b1-i4p-rs-ts/`. Every vitest, tsc and test-binary run went through `WT/tools/t3_slot.sh`. Each job was the only heavy job of mine, in four chains run one after another (`logs/chain_*.out`; my lines of `WT/guard/cargo_jobs.log` are `host/cargo_jobs_i101.log`):
  1. the I4 census and probes (RS, then TS), then I4's suites (RE, vitest, tsc);
  2. a development run of the new tests in an I4 copy with my working files laid over it (RE's filtered contract test, the two TS test files, tsc), before committing;
  3. the heads' census and probes, RE's suite at RS's head, vitest and tsc at TS's head, RT at `990339d94f`; then the mutants (one cargo build, then 64 RS runs and 3 TS runs);
  4. PP's two law tests at RS's head.
- **Waits:** each chain had one waiter, its background completion, which ended with the chain. Besides those, I read a chain's progress a few times with single non-blocking reads (a file listing or a log's tail), never in a loop and never as a second waiter. One slip, harmless: my first launch of the I4 chain ran nothing, because the chain scripts were written after my `chmod` and were not executable (`logs/chain_i4.out` was overwritten by the relaunch, which ran it). None of my waits remain. I signalled no job.
- **vitest, as I92 and ROOT's I4 check ran it:** in `git archive` copies of P without `execution/`, with `P/node_modules` linked to APPWT's (its `package-lock.json` byte-identical to I4's and to both heads', checked by `cmp` before each link), and the eight wasm assets copied, not built, from `WT/sweep-skewpin` (each copy's hashes equal I4's `ts_wasm_assets.sha256`; `host/wasm_*.sha256`). One addition: each copy had an empty `apps/desktop/node_modules`, so vite's temporary config and caches were written in the copy, not in APPWT's tree (APPWT's `.vite-temp` is untouched since ROOT's I4 run).
- **No link or asset was ever in `WT/b1-t`** (or `WT/b1-r`): the links lived only in my scratch copies, which I deleted with the targets at the end. `git status --ignored` in both worktrees shows nothing of mine (§9).
- **Not done:** no DEC-025, install, wasm build, PP pin or solve, push or merge; no PY or corpus file touched; no Git write in NUM (ROOT commits the records). Git reads used `GIT_OPTIONAL_LOCKS=0`.
- **Scratch:** `WT/scratch/i101_b1_i4p_rs_ts/` (`TMPDIR` inside it). Kept: harness, logs and outputs. Deleted: all ten copies (`copies/`, the development copy included) and every target.

## 9. Records (`_run_records/`)

Placeholder paths only (WT, APPWT, HOME, TMP replace machine paths, by `harness/sanitize.py`); no symlink; no folder named `build`; no junit output was produced (vitest wrote JSON reports, which carry no host attribute). Every file was screened, `.gz` files decompressed, with `WT/tools/t3_host_screen.py`'s own patterns (the strict path forms, the junit host attribute, and every name this machine answers to, read at run time), by `harness/screen_files.py`: **283 files (the whole folder, RETURN.md and SHA256SUMS included), 0 hits, 6 names screened.** A second grep for home, temp and worktree paths and for e-mail domains also found nothing. `git status --ignored` in NUM lists the folder as untracked, with no file of it ignored, so nothing needs force-adding.

- `commits.txt`; `diffs/` (RS's and TS's diffs over I4).
- `inputs.sha256`: RV113's tools and outputs used, and the probe set; `harness/build_probes.txt` rebuilds `probes_i101.json` (not copied, 8.9 MB).
- `harness/`: the job wrapper, the copy maker, the chains, `compare.py`, `probes_vs_rv113.py`, `suites.py`, the two mutant-schema makers, `mutant_table.py`, `screen_files.py`, `sanitize.py`, `assemble.py`.
- `census/`: RS's and TS's census at I4 and at the heads (gzipped JSON lines), and the four comparisons.
- `probes/`: RS's and TS's probe outputs at I4 and at the heads, the two I4-to-head comparisons, `CROSS_HEAD.json.gz` (RS and TS at I4 and the heads, and RV113's PY record), `probes_vs_rv113.out`.
- `suites/`: the two comparisons, and vitest's JSON reports at I4 and at TS's head.
- `logs/`: every job's own log (queued, start and end stamps, exit code) and the chain outputs.
- `mutants/`: the two manifests, the two schema diffs, `MUTANT_TABLE.json`, `mutants_vs_rv113.out` (each of RV113's 61, my failing tests against RV113's), and `runs/<id>/` (run stamps; logs and reports gzipped).
- `host/`: my lines of the job log (83 STARTs, 83 ENDs, never two of mine open at once), `job_stamps.txt`, `worktrees_status.txt` (`git status --short --ignored` and the heads of `WT/b1-r` and `WT/b1-t`: clean, with no `node_modules` and no `public/` assets), and the wasm assets' hashes per copy.
