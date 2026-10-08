# RV123 (RV-P2, round 1): B3b-P, the exact route under `physics-retained-1`

TASK (Type 2), RV123, an independent reviewer for ROOT (HELP_HUMAN, Agent 0), who is the return path. I am a fresh instance, wrote none of this change and made no delegation. 2026-10-08 UTC.

**The candidate:** `e67c364680..22e9d00062` on `codex/piping-t3-b2-20261008`.
- I105's commits: `8d3419b542`, `cc24cd955c`, `22e9d00062`.
- 9 files: 7 in PP, and two new fixtures `P/fixtures/results/retained_precision_exact_successor_{sparse_interactive,dense_scrutiny}.json`.
- I built every copy with `git archive` from NUM's objects into S. I did not read `WT/b2`'s working tree.

**Basis** (sha256 checked when I read each file):
- the brief `R/BRIEFS/B2_P_LANE.md` `525e5cd8…`, Part 1;
- PLAN `R/I93/b2b3_plan_01/PLAN.md` `e1147dbd…`, §1.2.7 and §1.4;
- B3-D `R/I96/b3_d_01/DESIGN.md` `ad7942f6…` with `REVISION_01.md` `6f5b1a6d…` and `statics/r1/`;
- `R/I99/b3_w_probe_01/PROBE.md` `1628a8e3…`;
- RR (`T/ROOT_RULINGS_V1.md` `3ecfc423…`): "RV115's addendum accepts B3-K …", "RV116 (RV-D) accepts B3-D …", "RV116 confirms B3-D's revision 01; …", "I99's B3-W verified; …" and "Lane A returned; `b2` built …".

I read I105's RETURN (`bb81c54a…`; its SHA256SUMS verify, all OK) only after forming my view.

**Placeholders:** WT, NUM, P, PP, RE, FK, T, R, RR and VENV as in the dispatch. **S** is `WT/scratch/rv123_rvp2`; **E** is this folder's `evidence/`.

## Verdict

**PASS, with 0 BLOCKING, 2 SHOULD-FIX and 6 NOTE.**

Nothing the exact route publishes was found outside its certified enclosure or at odds with its definition:
- **The rows.** m3x's exact successor publishes the same certified values as the reviewed preview successor of the same physics, bit for bit.
- **The sections.** Its sections are the correctly rounded annulus.
- **The hashes.** Its hashes, recomputed independently, match, including S-1's route H.
- **The reader gates.** Today's RS gates, with only the route identity switched, accept it through G0–G7.
- **Coexistence and byte identity.** Coexistence keeps the exact ordinary bytes. Every byte comparison between the base and the candidate is identical, except the intended exact W1 fallbacks.

The two SHOULD-FIX findings are pins that are missing for behaviour I verified is correct. Neither can publish a misstatement today, because the readers' G0 refuses every exact successor.

## Findings

| # | Class | Finding |
|---|---|---|
| S-1 | SHOULD-FIX | **No multi-member exact pin.** Every exact test input has one member, so P-8's per-member section overlay is pinned only for member 0. My mutant R-11 (only the first section patch applied) survives the candidate's tests. The behaviour itself is correct: my two-member variant, in both authored orders and both modes, regenerates each member's own prepared A, I, J and Z, passes I105's `assert_exact_successor` and the patched RS (G0–G7), and is bit-equal to its preview twin (`E/results/explore.txt`). **Fix:** pin a two-member exact input, for example m3x plus a collinear M2 with OD 0.15 m and wall 0.008 m, in both orders. |
| S-2 | SHOULD-FIX | **No exact successor with an `unavailable` prepared case,** so S-1's route H is unpinned at a production site. The site is the n-case serializer's unavailable branch, `retained_wire.rs` `serialize_attempt`, `bind_preparation(…, pc.route())`. My mutant R-01 (DEF-O's H there) survives, and so do R-02 and R-03 in the test-only c = 1 serializer. The existing hooks cannot reach this branch: `fault_next_candidate` at G-C failed both cases of the two-case exact input (`Candidate` fallback, no successor), and on the private driver it is never consumed (`E/results/followup.txt`). By reading, the code is right. **Fix:** add a case-specific fault, or a natural exact input with one unavailable case (as W-C2 is for the preview route), and pin DEF-E's id and H on the unavailable attempt's source. If this site were wrong, the readers' G1 would refuse and the invocation would fall back; it would not publish a misstatement. |
| N-1 | NOTE | **Lane A's oracle.** At `22e9d00062`, PP's registered suite fails lane A's `retained_memory::law_tests::b3b_direct_entry_keeps_the_exact_ordinary_bytes`. This is I105's disclosed stop: its "no producer change yet" premise no longer holds, and nothing else changed. I105's first proposal was correct but checked only m3x's notice count. The strengthened form on the branch, `a09e24b44c` (renamed `b3b_direct_entry_coexistence_keeps_the_exact_bytes_and_m3x_falls_back_at_g0`), pins m3x's G0 fallback as the plain bytes plus exactly one notice, byte for byte, built independently of the product constant. **By reading it answers my note; I did not run it.** B3b-P should merge together with it. |
| N-2 | NOTE | **No test with an unused material on the exact route.** My mutant R-06 (every material treated as used) survives. Behaviour checked: an unused second material with no ν and no basis is selected, and only the used material appears in `material_bases`. The mutation would only cause a conservative refusal and fallback. |
| N-3 | NOTE | **P1-02 is equivalent,** as I105 says. `is_load_state` is `schema_version == "0.4.0"`, for which `namespace_branch` returns `Err(SchemaVersion)`, so `w1_route` already gives `None`. My R-00 survives, as expected. |
| N-4 | NOTE | **The tests accept either outcome.** They accept today's precommit refusal, which is exactly G0 `SOURCE_PRODUCER_CONTRACT_UNSUPPORTED` with the plain bytes plus one notice per case in A, or a validated successor. The successor bytes are pinned either way. When B3's readers land, the tests switch to the successor branch without failing; that is intended. |
| N-5 | NOTE | **For SQ2's per-route pricing:** the exact route adds work that B3-S priced before the code existed. It adds loops: `capture_exact_materials` (materials × pipes), the m² section and material lookups in `exact_case_evidence`, and `prepared_sections`. It also adds allocations: `material_nu`, and one `Vec<PreparedSectionPatch>` per selected case. W1 now runs exact inputs on the reserved stack, so S1's stack witnesses, which exercise only the preview route, do not cover the exact frames. |
| N-6 | NOTE | **With an inexact Ĝ (ν = 0.3, a variant of m3x) the route still selects.** Ĝ is `4231e8f9013b13b1` = RN64(2e11/2.6); B3-D's checks and the patched RS (G0–G7) pass. Against its preview twin (G authored as Ĝ, so the source lanes differ by G versus Ĝ), 52 of 98 rows are bit-equal. The other 46 are null-response rows with \|Δ\| ≤ 3.2e-92, far below the receipt's absolute bounds (about 5e-24 to 8e-22). This is consistent with certification against the exact G (`E/results/followup.txt`). |

## 1. What the exact route publishes, and its definition

**Code reading** (PP `lib.rs`, `retained_product.rs`, `retained_wire.rs`, and `grant2.rs` against B3-D P-1 to P-13):
- **P-1:**
  - `w1_route` decides the route once, from lane A's `namespace_branch`;
  - the observer is built on that route (`permitted_probe_on`);
  - the private driver uses the same decision.
- **P-3:**
  - Ĝ is checked as `E / (2.0 * (1.0 + nu))`, which is RN64(E/(2·RN64(1+ν))) because doubling is exact, and it must be positive and normal;
  - the basis must be `homogeneous_isotropic_E_nu_v1`;
  - ν comes from the resolved material after `resolve_base`. I confirmed the order in `run_linear_static_preview_observed`: `resolve_base` runs before `normalized`.
- **P-5:** the members carry `BaseENu { e, nu }`, and FK maps it to `ExactENu`.
- **P-6:** checks every listed item. D1.5-exact holds by two means: the ordinary exact route blocks a case without `pressure_regions` (`EXACT_PRESSURE_REGIONS_REQUIRED`), and the capture refuses a non-empty list.
- **P-7, P-8:**
  - the extrema and the four section values are regenerated in the owner case's `exact_cases` entry only;
  - the section values are taken from the facts after preparation;
  - the moves are pre-charged.
- **P-9 and S-1:** one route descriptor supplies the identity, the profile, the definition id, DEF-E's H in the preparation payload and `geometry.route`.
- **P-11:** the legacy disclosure is omitted on a selected case.
- **P-4:** the only pressure-runtime call in W1 is `is_exact`.
- No other preview constant remains in W1 (grep in `retained_wire.rs`, `retained_receipt.rs` and `retained_product.rs`).

**Independent checks** (my own scripts and harnesses, outside I105's tests):

| Check | Result | Evidence |
|---|---|---|
| m3x exact successor against the preview milestone successor (same E, G = 8e10, OD and wall) | All 98 (sparse) and 99 (dense) rows have identical kinds. Every value is bit-equal except dense's parity observation, which is an ordinary observation. All 69 `absolute_verified` bounds, the extrema's eight fields and both headlines are equal | `E/results/cmp_routes.txt` |
| Sections against the correctly rounded annulus (π to 300 digits, exact OD and wall) | A `3f7872fa3a37ac13`; I, J and Z `…210a`, `…210a` and `…954a6`, equal to the published values. The ordinary SourceAnnulus values are `…210b`, `…210b` and `…954a7` (one ulp above), with A equal, as B3-D's table states | `E/results/annulus_check.txt` |
| Hashes (Python, and RE's own `domain_hash`) | The receipt, publication and source-identity hashes match. The preparation hash matches with DEF-E's H `5a3bac43…` and differs from DEF-O's `a7ed7ca0…` | `E/results/hash_check.txt`, `re_check.txt` |
| In-tree statics | DEF-E `71f63d39…` and XTABLE `c4987e87…` equal B3-D's `statics/r1` | — |
| SCHEMA (jsonschema 2020-12) | Both receipts and every raw row: 0 errors. Control: an unknown `definition_id` gives 1 error | `E/results/schema_check.txt` |
| G7: physics-1's base validator on the projected successor | RS `for_source` passes (standing `needs_recompute`); PY `_source_contract` passes | `re_check.txt`, `py_checks.txt` |
| Today's RS gates with only the identity, table, definition and G7 projection switched (scratch copy; `E/results/patched_reader.diff`) | **G0–G7 pass** on both fixtures (98 and 99 rows classified), on the mixed base, two selected cases, two members (both orders), ν = 0.3, a redundant authored G and an unused material. With the invocation, G8 refuses `INVOCATION_MISMATCH`, which is expected: its predicates are preview-only (the exact branch is lane R's) | `re_check.txt`, `explore.txt` |
| Wire identity | `physics-retained-1`, `exact_straight_retained_w1a_v2`, `RP-PREPARED-EXACT-DUAL-v1`, Ĝ `4232a05f20000000`, `derived_e_nu` with ν `3fd0…`, `geometry.route` exact, `legacy_source_work[0].limit` 8,000,000 | fixtures |

**Variants on the private driver** (scratch; `E/results/pp_scratch_tests.diff`, `explore.txt`). Each is selected, passes `assert_exact_successor` and is accepted by the patched RS:
- ν = 0.3, with E in Pa and in GPa (the same receipt bits);
- two members, in both orders;
- a redundant authored G of 8.1e10 (ignored: Ĝ is 8e10);
- an unused material.

## 2. Coexistence and byte identity

A public-API harness ran unchanged on the base and the candidate, over 19 inputs in both modes: B3-W's 11 inputs, the 7 committed physics-source requests and the milestone (`E/results/bytes_compare.txt`, `bytes_sha256.txt`).
- **Plain ordinary bytes:** base = candidate for all 38 pairs.
- **The Direct entry's one publication:**
  - **Unchanged:** base = candidate for every input except the exact W1 inputs. These include n05, n06 and `fields` (coexistence), n05_units and n05_unicode (for all five the Direct publication equals the plain bytes, which equal the committed raw fixture's value), mixed and mixed_units (one case carries a region; the Direct publication equals the plain bytes), m3l, the m1 twins and the milestone successor.
  - **The intended change:** for m3x and m3x_mix_anchor/axial/lateral, the base published the plain bytes (`Domain`). The candidate publishes the plain bytes plus T-12's notice for each case in A, matching T-12's text exactly (independently rebuilt): `case`, or `case` and `case:b` for axial and lateral in sparse.
- **No c = 1 or B1 multi-case successor byte changed:** every existing pin test passes unchanged (§7), and no committed fixture changed apart from the two new ones.

## 3. P-2 and P-4

- **P-2 holds and is pinned:**
  - the unit assertion on `w1_budget`;
  - `fields` selects only at 8M, and its W1 ordinary run equals the ordinary route's bytes;
  - the receipt's `legacy_source_work[].limit` is 8,000,000;
  - n05, n06 and `fields` keep their bytes through the Direct entry.

  Mutants P1-04 and P1-05 are I105's.
- **P-4 holds by reading and is pinned by a static text guard** (`b3b_p4_…`).

## 4. The m3x successors, SCHEMA and the inputs; m3l

- **Fixtures:** both are the live documents, byte for byte (I105's test, which passed in my runs).
  - Document sha256s: `02465c6c…` and `31f10f04…`.
  - Their invocations equal I99's `m3x.json` (file `0ffbea35…`).
- **SCHEMA:** §1.
- **Inputs:** I99's input files verify against `inputs.sha256` (11 of 11). The tests pin the Value sha256s of m3x, m3x_mix_anchor and m3l as I99's: `c920a96d…`, `6ca777a6…`, `2f5ff465…`.
- **m3l needs no producer change,** and its Direct bytes are identical between the base and the candidate.

## 5. Today's fallback

- **The fallback is pinned exactly:** RS refuses at G0 `SOURCE_PRODUCER_CONTRACT_UNSUPPORTED`, and the publication is the plain physics-1 bytes plus one notice per case in A (`exact_outcome`; the Direct test; my byte comparison).
- **N-11 acceptance:** physics-1's base readers accept the noticed envelopes with the same contract and standing.
  - RS: I105's test.
  - PY: my check on m3x and m3x_mix_anchor, both modes (`py_checks.txt`).
  - TS: I105's vitest record only; I did not rerun it.

## 6. Mutants

**I105's 59:** I reviewed the list. P1-02 is equivalent (N-3).

**Mine: 12**, each one exact edit of a scratch copy of the candidate, run with PP `--lib` filtered to `b3b_`, `b3a_`, `b1_sp_`, `u3_permitted_path`, `u3g2_` and `u1_constants` (registered build; 45 tests; the pristine control passes 45 of 45; the source was restored and checked after each). Results: `E/results/mutant_results.json`.

| Mutant | Result |
|---|---|
| R-04: I and J swapped | killed (4 tests) |
| R-05: Z replaced by the radius | killed (4) |
| R-07: Ĝ formula wrong | killed (many) |
| R-08: the derived origin's basis literal | killed (4) |
| R-09: the c ≥ 2 case scope loses the route | killed (2) |
| R-10: the c ≥ 2 evidence entry is always 0 | killed (1) |
| R-00: P1-02 | survives (equivalent) |
| R-01, R-02, R-03: the unavailable exact branch | survive (S-2) |
| R-06: an unused material treated as used | survives (N-2) |
| R-11: only the first section patch applied | survives (S-1) |

## 7. Suites against `e67c364680`, test by test

All of these ran on pristine archives (`E/results/suite_*.txt`, `deps_check.txt`).

| Suite | Base | Candidate | Difference |
|---|---|---|---|
| PP registered, all targets | 748 ok, 1 failed (`t13`), 11 ignored | 763 ok, 2 failed, 11 ignored | **16 added, all ok; 1 changed: lane A's oracle, ok → FAILED (N-1)** |
| PP Stale `--lib` (`--cfg=rv123_stale`) | 585 / 1 (`t13`) / 11 | 601 / 1 (`t13`) / 11 | the same 16 added; nothing else |
| Runner (headless) | 85 ok, 2 failed (load-reference) | the same | none |
| PP's dependents: `cargo check --all-targets` of operation_applier, self_weight_wasm, physics_audit_regression, numerical_integrity and src-tauri | — | all compile, 0 errors | — |

FK is untouched by the candidate, and every FK dependent that depends on PP compiles.

## For ROOT

1. **N-1:** merge B3b-P only together with lane A's strengthened oracle (`a09e24b44c`). At `22e9d00062` alone, PP's registered suite fails.
2. **S-1 and S-2:** I105 should add the two pins, the multi-member exact pin and the unavailable exact case. ROOT may decide they land in B2-P's round instead. Each is test-only; S-2 may need a case-specific fault hook.
3. **N-5:** carry it to SQ2's brief, for per-route pricing and S1 stack coverage of the exact frames.

## Host, execution and records

- **Cargo:** every cargo job went through `WT/tools/t3_cargo.sh --locked --offline`, with fresh targets `WT/targets/rv123-*` per lockfile.
  - There were 29 jobs, one at a time, in four chained phases (`E/tools/phase*.sh`, `E/cargo_jobs_rv123.txt`).
  - They waited for I104's exclusive measurement.
  - There was no RSS or timing measurement, no DEC-025, no install and no Git write.
- **Python and TMPDIR:** Python came from VENV and ran on JSON only; `TMPDIR` was `S/tmp`.
- **Slips, disclosed:**
  - I briefly started two redundant waiters of my own beside my monitor, and stopped them.
  - My turn ended once mid-chain with an interim hand-back (ROOT then authorized lane A's edit).
  - No other agent's job was signalled.
- **Scratch tests** (`E/results/pp_scratch_tests.diff`, `re_rv123_exact_check.rs`, `re_lib_module.diff`, `patched_reader.diff`, `E/tools/rv123_*.rs`) exist only in S's check copies. A recursive diff shows those copies differ from the candidate and base archives only by these additions.
- **Records:**
  - Placeholder paths only; logs are filtered to outcome lines and sanitized (`E/tools/logfilter.py`, `sanitize.py`); 0 screen hits.
  - No symlink and no folder named `build`. The byte outputs (17 MB) stay in S; their sha256s are in `bytes_sha256.txt`.
  - `SHA256SUMS` covers every file here except itself.
