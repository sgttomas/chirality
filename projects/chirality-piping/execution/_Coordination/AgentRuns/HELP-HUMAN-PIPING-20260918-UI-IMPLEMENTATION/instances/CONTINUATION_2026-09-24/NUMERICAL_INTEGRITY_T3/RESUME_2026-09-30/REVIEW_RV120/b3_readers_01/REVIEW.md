# RV120 (RV-R2): B3's three readers and lane T's carriers — CONFIRMED, with two repairs before the merge

TASK (Type 2), RV120, for ROOT (HELP_HUMAN, Agent 0), the return path. No delegation; I wrote none of the change. 2026-10-08 UTC.

## Verdict

**The shipped reader code admits nothing it should refuse and refuses nothing it should admit, in all three languages, on every input I built or replayed.** Lane T's carriers admit the producer-derived exact documents and refuse their downgrades. Two repairs before `b2-p`, `b2-r` and `b2-t` merge:

- **F1 (PY, low).** A first-failure order difference at G5b (the code, not the gate). It is a one-call move.
- **F2 (tests, medium).** I101's argued-equivalent mutants B28 and B29 are not equivalent. With either one applied, RS and TS read a forged statement as eligible, and no suite notices. The shipped readers refuse it. Pins are needed in all three languages.

## Basis

- **Brief:** ROOT's RV-R2 message and `R/BRIEFS/B3_READERS.md`.
- **Specification:**
  - I93 PLAN §1.3–1.4, with REVISION_01;
  - B3-D `R/I96/b3_d_01/DESIGN.md` (`ad7942f6…`) and `REVISION_01.md` (`6f5b1a6d…`);
  - RV116's rulings (S-1; B3D-10 with N-4; B3D-11; B3D-12);
  - RR "The G8 sourced-case rule aligned …" and "I101 returns B3's RS and TS readers …", including its fresh-set ruling: the panels stay closed to the exact successor.
- **Candidates:**
  - PY `b2-p` `b7721d27e9`;
  - RS `b2-r` `c845e899da`;
  - TS and lane T `b2-t` `77aaaa61d1`, which contains `b2-r`;
  - base `b2` `e67c364680`.
- **How the copies relate:**
  - RE's `src/` is byte-equal at `c845e899da` and `77aaaa61d1`. Of RE's tests, only `retained_precision_derivative_golden.rs` differs, so RS ran in the TS-head copy.
  - Lane P's `56e44fa081`, which all three heads contain, changes only `core/product_physics` and the two m3x fixtures. So the reader suites compare against `e67c364680`.
- **Copies:**
  - `git archive` into `WT/rv120b3/{base,py,rs,ts,probe,mut}`. `probe` and `mut` are `77aaaa61d1` plus my raw runners.
  - NMS is linked after a lock cmp. Each copy has its own `apps/desktop/node_modules` and the eight wasm assets.
  - PY's authority binaries are rebuilt in `WT/targets/rv120b3-pybins`; serialization and units are unchanged since I4.
- **Order:** I read the diffs and the code and ran my probes first. I read I100's RETURN (`e0956d64…`) and ADDENDUM_01 (`7a336bfd…`), and I101's RETURN (`68db75d1…`) and ADDENDUM_01 (`8492fc4d…`), all verified, after.

## Findings

| # | Severity | Finding |
|---|---|---|
| F1 | Low (PY; repair) | **The exact G5b evidence check runs in the wrong place in PY.** PY runs it inside the per-case loop of the shared G5b (`core/analysis_runs/retained_precision.py:1515`). That is before the case's row-scale checks and before every later case's shared checks. RS (`retained_precision.rs:4771`) and TS (`retainedPrecision.ts:1569`) run it after the shared G5b over all cases, as DESIGN §6.2's G5b row orders it ("…unchanged; then for each selected case…"). **Probe** (`evidence/readers/g5b_order_inputs.jsonl.gz`), on the exact `two_case_synthetic`: case 0's evidence `As_m2` +1 ulp, and case 1's `body_scales[0].force` +1 ulp. RS and TS give G5b `SCALE_MISMATCH`, bound and unbound; PY gives G5b `SECTION_MISMATCH`. Each fault alone gives the same reading in all three. Admission and standing are unaffected, and only a statement with two faults in at least two selected cases shows it. **Repair:** move the call into its own loop over `states`, after the shared loop and before `phase[0] = "G5c"`, and pin the probe in all three readers |
| F2 | Medium (tests; pins) | **B28 and B29 are not equivalent.** I101's argument rests on the native hashes, which the 07e test rule does not reseal; a producer can reseal them. N-6 plus G7's G binding plus S-C bind Ĝ only to within G7's 2-ulp tolerance. **Forgery** (`harness/forge_eg.py`; inputs `readers/forge_eg_inputs.jsonl.gz`), on the exact `ordinary_prepared_synthetic` and `m3x_sparse_interactive`, for E and for Ĝ in turn. The receipt's E (or Ĝ) moves by 1 ulp in all five copies: the material basis, the id-map member, `old_source`, and the old and new operational inputs. The recomputed operational stiffness moves with it in both section-term copies, and the evidence `G_pa` moves for Ĝ. The native hashes are resealed with PY's own encoding, with every copy of them, and then 07e's rehash is applied. **Results:** the shipped RS, TS and PY refuse all four at G8 `PREPARATION_MISMATCH` (step 4). With B28 applied, RS and TS read both E forgeries **bound and eligible**; with B29 applied, both Ĝ forgeries likewise. In I101's runs no suite kills either mutant. **Pins:** the four forgeries, refused at G8 `PREPARATION_MISMATCH`, in each reader's tests. They are the only witnesses that step 4's E and Ĝ bits anchor the receipt to the authored material |
| N1 | Note (PY) | `_preparation_payload(a, definition_hash=DEFINITION_HASH)` (`:398`) keeps DEF-O as a default. Both call sites pass the route's hash (`:1822` G8, `:1994` G1), but a future call site that omits it would hash with DEF-O silently. S-1 says "never a module constant", so I suggest dropping the default |

**Accepted equivalents:**
- **B06b:** XTABLE is hash-pinned at step 5, and on the exact route the reader constants are read only by step 6.
- **B30:** S-C's `poisson` requires unit `"1"` at the same gate with the same code; only the detail differs.

**The mutant tally is therefore:** RS 39 of 43 and TS 43 of 47, with B28 and B29 real survivors that my forgeries kill.

## Review items

| # | Item | Result |
|---|---|---|
| 1 | B3a: G8's namespace, type-strict (B3D-10, N-4) | **Holds in all three.** Code: RS `legacy_namespace`/`pressure_contract_is`, PY `_legacy_namespace`, TS `legacyNamespace`. Probes (48 on the preview route) on the 0.2.0 and 0.1.0 bases: `pressure_contract` `false`, `0`, `""`, `[]` and `{}` are each `INVOCATION_MISMATCH`, and explicit `null` passes. At 0.3.0 only exactly `{version "1.0.0", mode "legacy_pressure_v1"}` passes, keys in either order. Refused as `INVOCATION_MISMATCH`: a numeric or list version, an extra key, `null`, an absent contract, the exact contract, 0.2.0 with the legacy contract, a numeric or list `schema_version`, and 0.4.0 |
| 2 | B3b: the `<physics-retained>` branch | **Holds.** G0's steps 1–9 run in order in all three, with `FORMATION_MISMATCH` only at step 4. The preview identity with the exact profile, and an exact-id attempt on the preview route, are each G0. **S-1:** the route's H is used at every preparation-hash site: RS `:774` (`route.definition_hash`), PY `:1822` and `:1994`, TS `:280`, and PP `retained_wire.rs:1375` (`route_wire`). Cross-route probes: a preview statement hashed with DEF-E, an alternate H or PTABLE's sha, and an exact statement hashed with an alternate H, PTABLE's sha or XTABLE's sha, are all G1 `RECEIPT_MISMATCH` in all three. The ordinary id hashed with DEF-O's H on the exact route is G0. **The other gates:** G5b's section truth (seven fields, bit for bit); G7's projection to physics-1 and `exact_straight_pressure_v2` (transport uses physics-1's metadata check); G8's exact namespace; G8's step-3 base selector; G8's step-4 E, Ĝ = RN64(E/(2·RN64(1+ν))) and the derived shear origin; S-C; N-6; and `geometry.route == "exact"`. **S-C's exposure is minimal:** RS `pub(crate)`, PY imports `_actual_materials` and `_canonical_inputs`, TS exports `validateAuthoredCaseFacts`. **No new statement failure code.** RS's `SOURCE_PHYSICS_RETAINED_TABLE_*` verifies the packaged table (`.expect`), mirroring the preview's |
| 3 | The G8 sourced-case rule | **Holds in all three, on both routes.** **Preview:** `pressure_regions` `[]` and `null` pass; `{}`, `""`, `0`, `false` and one region are `PREPARATION_MISMATCH`. **Exact:** `[]` only. **Both routes:** `equivalent_static` `null` passes, while `false`, `{}`, `[]` and `0` are refused; any `analysis_state` (`null`, `{}`, `false`), including on the second case, is refused; a case-level `pressure` (or `null`) is not read and passes eligible |
| 4 | Lane T | **Holds.** The three carrier branches copy the preview successor's, with physics-1's evidence and result sets, the profile enums (`CARRIER_PROFILE_ENUMS`) and the seven producer limitations. The **real** exact goldens (both modes) validate against `results.v0.3`; with the preview profile or without the receipt, they are refused. PY's exact AnalysisRun, built from both m3x successors by PY's head and validated by it, validates against `analysis_run.v0.3`; without the receipt it is refused (`carriers/CARRIERS.txt`). `outputPolicy.ts` has `retained_physics` with its own reason; 19 surfaces are refused and 2 are `admitted_when_eligible`. The panels stay closed by RR's fresh-set ruling, so B3-D §7's exact panel tests are moot until B7/B8. The `SourceContract` union and every `isRetainedRoute` site were read (`tsc` rc 0). The T6S exact golden equals the live Rust derivative, and TS reproduces it byte for byte (RE and vitest, below) |
| 5a | Census, base vs heads | **0 changes and 0 expectation misses** in RS, TS and PY. That covers 07m (339 entries) and 07n (638 entries; sha256 `ea113e7b…`, through RV113's harnesses with only the corpus path from the environment: `harness/rv120_*env*`) |
| 5b | Suites against `e67c364680`, test by test | **RE:** 198 → **207 ok**. That is +9: 6 at the RS head plus lane T's 3 golden tests. 0 removed or changed. **vitest (whole suite):** 3,639 → **3,679 passed**. That is +41 added and 1 renamed (D31, B3D-10's declared rename); 0 failed or changed. **tsc:** rc 0 at both. **PY, at the PY head:** retained, carrier and schema files plus the B3 module: 1,318 → **1,693 passed**, +375 (the B3 module), 11 skipped at both. **PY, at the TS head:** lane T's schema files: 1,318 → **1,321**, +3. 0 removed or changed |
| 5c | Three-reader agreement on identical bytes (raw runners) | **I101's 165 shapes:** RS = TS = PY on bound, unbound and transport, except G7's per-language base codes (12 triples). **I100's 52 addendum shapes:** 0 differences. **I100's 318 B3 shapes** (re-materialized): 0 differences, and PY equals I100's `expected_python` on 318 of 318. **My 128 probes plus the 4 forgeries:** one difference (F1). Every stated want is met by all three, except F1 in PY (G7 codes compared per reader). My materializer reproduces RS's own dump byte for byte on 4 controls (rehash parity) |
| 6 | Platform | **No libm-dependent computation in B3's paths.** The new reader arithmetic is IEEE `+ − × ÷`, square root (correctly rounded in all three: `f64::sqrt`, `Math.sqrt`, `math.sqrt`), and exact powers of two. Unit conversion goes through the shared units crate (RS directly, TS through its wasm build, PY through its binary). TS's `Math.hypot` remains only in B1's preview-route `previewPhysicsEvidence`, inside the readers' guard (I109: the readers need no change) |

## Host

- **Jobs:**
  - Every cargo run went through `WT/tools/t3_cargo.sh --locked --offline` (targets `WT/targets/rv120b3-{base,ts,probe,mut,pybins}`).
  - Every other heavy job went through `WT/tools/t3_slot.sh`.
  - One heavy job of mine ran at a time, with one wait per chain.
  - No Git writes, no DEC-025, no installs and no measurements.
  - Light checks (the materializers, and the schema validation of the goldens and records) ran directly.
- **Disclosed:**
  - (a) The first PY schema-test run at the TS head ran before the authority binaries existed (`targets/rv120-*` had been cleared), and was rerun.
  - (b) The first forgery stopped at G5 because the call groups' native-hash copies had not been resealed. Its outputs were set aside (`*.v1`), and the forgery was completed.
  - (c) One of my own file-edit commands hung on stdin. I stopped it and removed its empty temporary file.
- **Record:** `evidence/host/job_stamps.txt` has every job's stamps. Placeholders: `WT`, `NUM`, `P`, `R`, `RR`, `NMS`, `VENV`. Junit host attributes were removed.
