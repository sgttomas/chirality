# RV124 (RV-Q): B1's SQ, Pass A — G5, M, G6 and the registration, the re-pins, the witnesses, the challenge, RSS_TIME, QUAL §11, DEF-O

TASK (Type 2), RV124, for ROOT (HELP_HUMAN, Agent 0), who is the return path. I hold RV-Q for B1 after RV112. I am a fresh instance, wrote none of this change, and made no delegation. 2026-10-08 UTC. I read NUM's `AGENTS.md` and `agents/AGENT_TASK.md` first.

**The brief:** ROOT's dispatch message to RV124 (no brief file). **The specification:** `R/BRIEFS/B1_SQ.md` (`f6eaa6cc…50cb8`, items 1–10), `B1_COMMON.md` (`2d170307…2eb2c75`), PLAN_v2 §3.1–3.7 (`c85786b7…19be0`) with RV107's A1 amendments, and RR (`f514697a…05c73`): "R6a: …", SF-1 of "RV112 passes SA; …", E-12 of "RV109 passes SP in RV-P round 2; …", I89's value pins, I86's inputs, "I90's SR-RS repair round 2 …" item 2 and "RV115 confirms S-4 (a)'s soundness …" NC-1.

**The candidate:** b1-q `b075c5c59f` (G5) and `69002bc862` (G6) over `57c92a7b33`, plus `R/I104/b1_sq_01/registration.diff` (`d85101ea…7d6526`). **The returns,** read after I had formed my view: RETURN.md `1712ba86…2df330` and RETURN_ADDENDUM_01.md `5cb3c461…66dfc` (full hashes in §11). SHA256SUMS 116/116 and SHA256SUMS.addendum_01 465/465 OK.

**Placeholders:** WT, NUM, P, PP (= `P/core/product_physics`), T, R, RR, VENV as in the dispatch. `S` = my scratch `WT/scratch/rv124_rvq` (kept for SB's Pass B); `E` = this folder's `evidence/`. My copies are `git archive`s in `S`: `base` (`57c92a7b33`), `g5` (`b075c5c59f`), `cand` (`69002bc862`), `reg` (`cand` + `registration.diff`, applied with `patch -p1`, one hunk, clean) and `mut` (`reg` without `execution/`). Targets: `WT/targets/rv124-reg` (fresh) and `WT/targets/rv124-mut`.

**Limits kept.** Every cargo job through `WT/tools/t3_cargo.sh` (`--locked --offline`); every other heavy command (the Python chain points, every test-binary run) through `WT/tools/t3_slot.sh`; the RSS/time runs only through `WT/tools/t3_exclusive.sh`. One heavy job of mine at a time (my chains were serialized, each waiting on the previous one's process); no other job signalled. No Git write, DEC-025 or install; nothing read or written in `WT/b1` or `WT/b1-q`; TMPDIR in `S`.

## Verdict: **PASS** — 0 BLOCKING, 0 SHOULD-FIX, 5 NOTE. **M = 10.5 GiB: confirmed.**

G5 reproduces byte for byte from I104's recorded tools, and its new rules hold up under an independent audit; G6, the registration, the re-pins, SF-1, RV112's N-1/N-2/N-5 and E-12 are right and are pinned (20 of my 21 mutants die at assertions; the survivor is equivalent on today's inputs, Q-N4); all 28 witnesses and all 27 challenge entries pass as one process each; RSS_TIME's numbers trace to its raw files, and the ones I re-measured agree.

## Findings

| ID | Sev. | Where | Finding | Proposed |
|---|---|---|---|---|
| Q-N1 | NOTE | PP `retained_product.rs` `prepare_cases`; RS `retained_precision.rs`; the profile | **B1 added heap owners that no profile row prices.** `prepare_cases` builds `Vec::with_capacity(attempted.len())` of `CaseAttempt`, and **`size_of::<CaseAttempt>()` is 9,400 B in this build** (`AttemptEnd` 8,704, holding a `RefusedCase` 8,704 or a `FrozenCase` 4,392 inline; `PreparedTrace` 520). That is **28,200 B at |A| = 3** (9,400 at c = 1), live from T-7 through staging and the serializer. On `main` the one case's `PreparedCase`/`FrozenCandidate` were stack values, under R. There is no `s(CaseAttempt)` atom, and N-5's patch prices only the adapter reservations. B1's small O(c) heap locals are unpriced as well: in the serializer (`attempt_of`, `diagnostic_ids`, `diagnostic_refs`' outer vector, …), and the RS reader's new id sets and vectors in `g3` and `preview_physics_transport_metadata` (at most a few KB). This is RV112 N-5's class: about 30 KB against 287,052,726 B of dense margin. **M and every 0.9 M margin are unaffected**, and no measured peak comes near (§6). | ROOT rules, as for N-5. Either price `s(CaseAttempt)·a`, with one `sq_n5_chain.py`-style row and a regenerated block (PINNED_RECORD and the challenge constants then move by about 28 KB), and record a census of B1's non-adapter allocation sites before R6b; or carry both to SB with a stated bound. |
| Q-N2 | NOTE | RSS_TIME §6; ADDENDUM "For ROOT" 3 | **DEF-O's "other" class hides a third projection with NC-1's property.** Of b2_k1e3's 79 "other" failing rows (each mode), **52 are `MPa` stress rows** (30 torsional shear, 18 bending z, 4 bending y), which DEF-O projects by `y × 1e6` after RN64 (`ProductUnit::Megapascal`, `final_case.rs` `normalize`): a second rounding, like mm→SI's `/1000`. The other **27 are unprojected** (`Pa` stress maxima 12, `N` forces 15). The conclusion stands on those 27: neither named property, nor all three projections together, is the sole cause of either fallback. | Amend §6's table to split "other" into MPa-projected and unprojected rows, so that ROOT's DEF-O decision sees that the ×1e6 projection shares NC-1's availability limit. |
| Q-N3 | NOTE | QUAL_B1.md | **Not wholly in QUAL's form.** It has no §7 (the identifier-class audit; G5's 12/12 controls are only in RETURN.md) and no §9 (controls: unregistered fixture sweep, the other crates' suites, the mutant set). Some of §9 belongs to SG, ROOT's §3.9 suite and SB. My 6 controls on B1's new identifier sites all fire (§1.6). | Add a short §7 citing G5's audit and the B1-site controls, and a §9 line saying which controls moved to SG/§3.9/SB. |
| Q-N4 | NOTE | `tests/retained_memory_challenge.rs` `measure` | **A1-S-1's bound choice is unpinned.** Mutant M17 (W1 work read from the successor only, ignoring the N1 notice) survives: `b2_k1e3`'s peak (13.2 MB) is under either bound. Equivalent on today's inputs, whose peaks are ≤ 1.22 % of E_mov,max. | Optional: factor the bound choice into a function with a unit test (notice ⇒ E_mov,max), or accept as equivalent-by-data. |
| Q-N5 | NOTE | ADDENDUM "For ROOT" 5 | **Agreed:** `noncand_compare.py` keys on the multiplicity, so at C = 3 it reports 288 "new" rows (I reproduce: exit 1, 288 new, 286 absent). The multiplicity-free comparison gives 408 matched, 4 new, 2 gone, identical to I104's. | SB's Pass B gate should take `noncand_compare_nomult.py` (or a c = 1 sweep), as I104 says. |

## 1. G5

### 1.1 The chain reproduces byte for byte (`E/chain/`)

I rebuilt I104's chain from the records alone (`R/I104/b1_sq_01/_run_records/tools/`, I65's `u4_g7_06` chain, my copies of `text_base.sh` and `run_point.sh` retargeted to `S` only):
- the line map Pass A `ba1faa1c85` → `57c92a7b33` equals I104's (439 remapped, 7 unmapped; the tool exits 1 on the 7, as recorded);
- `b1q_chain.py` (41 patches, no emulated rebinds or edges), `i104_rules.py` (89 new headers over 97 inventory indices, 2 FIRST, 21 REBIND, 9 KEEP, 1 edge, 3 call-graph rules dropped and 3 added, 18 text-args actions, 7 scaled totals) and `sq_n5_chain.py` give chains **byte-identical** to `chain/` and `g6/n5/SQ_N5_PATCHES.json` (all 23 files);
- the profile trees at c = 3 (G5 and N-5) and c = 1 are **byte-identical** to I104's;
- `g5_profile.py` on those trees regenerates **both GENERATED PROFILE blocks byte for byte**: `b075c5c59f`'s (1,250 lines) and `69002bc862`'s (1,262 lines);
- outside the block, `69002bc862`'s `retained_memory.rs` differs from `57c92a7b33` only in `phase_caps`' late bound and its doc.

| Point (C = 3 unless stated) | TEXT complete | Unmapped / unclassified | D (converged) | D_env | TAV_W |
|---|---|---|---|---|---|
| c = 1 (N-5 chain) | yes | 0 / 0 | 14,781 | 9,361 | 1,640,333,910 |
| c = 2 | yes | 0 / 0 | 27,712 | 16,008 | 2,953,217,280 |
| c = 3 | yes | 0 / 0 | **41,769** | **22,911** | **4,301,774,658** |

No SCC finding (an SCC is reported as an unclassified argument, as I65's control c9 shows); the self-recursion list is the reviewed 11. The deepest chain from the Direct root is **40** at c = 1, 2 and 3 (`cg.out.json` `root_depths`).

### 1.2 In-build E_mov,max + R (my registered build, `E/law/law_registered_nocapture.log`)

**9,800,676,166 B sparse, 9,859,807,510 B dense (W3)**; no `I65_G6_RECORD_SKIP`, so `PINNED_RECORD` is asserted in this build. My 265 `I65_G5_ATOM/PHASE/PROFILE` lines are identical to I104's registered dev/test record, which is identical to its release record (`diff` exit 0 on both).

### 1.3 The new rules: real multiplicities against I82's emulation

- **By function** (`E/chain/fn_text_W_c3_i82_vs_b1.txt`, my computation from the c = 3 runs): TAV_W is +112,078,320 B over I82's. Every decrease is a B1 restructuring: `observation_fields` (−73.2 MB) becomes `observation_fields_of` (+26.1 MB) once the c² scan is gone; `bind_observations` (−4.1 MB) becomes `_by_case` and `_in` (+5.2 MB); `publish` 18 → 1 call (B1 has one call site with a loop over A, where `main` had six); RS's `unit_by_symbol` (−6.2 MB). The increases are the qualified-id call (+126.1 MB) and `stable_suffix` (+21.7 MB), `SupportFinding::new` (+8.2 MB), and small sites. This is I104's account.
- **I82's checklist.** 19 rebinds are applied on the real code; the 3 kept at 1 (material bases, calls, groups) hold: `material_basis` emits one basis whose `case_indices` name every case, and the serializer refuses `calls().len() != 1`. I82's 22 emulated edges are now real loops. At c = 3 each named callee's real multiplicity is at least I82's: `prepare_active_case` 3 (I82's `prepare_case` 3), `freeze_case` 3 (`freeze_candidate` 3), `selection` 3, `legacy_source` 3, `ordinary_entry` 3 (`ordinary_value` 3), `product_attempt` 9, `kernel_outcome`/`run_value`/`bind_preparation`/`case_source` 6, and `domain_hash` 11 (I82: 8). There are two exceptions, both because B1 has fewer call sites: `publish` is 1 (I82: 18, from main's 6 call sites × a), with its loop over A carrying a; and the c = 1-only `bind_rows` is 1 beside `bind_rows_scoped` at 3.
- **No rule under-counts, as audited.** From the c = 3 loop log I took every distinct loop priced at P (29), l (26) or 1 (41) (`E/chain/looplog_P_l_1.txt`). I read the code of each one in B1's changed functions, and checked the others by their call context:
  - the P loops all iterate one case's rows: the case scope (`case_rows`, `rows_of`), a per-case solve, `rows_for`, or a filter whose body runs only on in-case rows;
  - `bind_observations`' whole-envelope loop (P) runs only when `parked` is empty, that is at c = 1;
  - `bind_case_rows` refuses any row outside the case blocks, so no invocation-level row escapes the c·P bound;
  - the l loops are per case (`old.loads()` is the case's own captured source);
  - the loops priced at 1 that are not single-shot `Option`/`Result` adapters are the three KEEPs and two `windows(2)`.
- **The c = 1 control.** TAV_W is 1,640,333,910 against Pass A's 1,570,041,862: **+70,292,048**, equal to I104's in-build E+R difference (3,646,070,334 − 3,575,778,286 sparse). By function: the qualified-id call +56.7 MB, `stable_suffix` +9.7 MB, `observation_fields_of`/`observation_fields` +1.7 MB, the c ≥ 2 binders +1.0 MB, the rest under 0.7 MB. All named B1 code.
- **c².** TAV_W's second difference over c = 1, 2, 3 is 35,674,008 B, as I104 states.

### 1.4 The three `freeze` rules

There are two `fn freeze` (`PreparedCases::freeze`, `PreparedTrace::freeze`). The three adjudicated callers bind correctly: `w1_transaction`'s `prepared` is the `PreparedCases` from `prepare_cases`; `native`'s `attempt.trace` and `prepare_attempt`'s local `trace` are `trace::PreparedTrace`. Every other caller already binds one target. `prepare_owned_case` still fans out to both, which can only over-count, and it is unreached at c = 3.

### 1.5 SF-1's premise

At c = 3 the late-capture and ordinary-seed forms are exactly 3 × their c = 1 forms (chain), and in-build `T11 = 443,136`, one case's late capture `38,016`, **G-B's bound `405,120`** (`I104_SQ_G_B_BOUND`).

### 1.6 The identifier audit on B1's new sites (`E/chain/audit_b1.txt`)

On my c = 3 point, removing each of I104's five new `id_audit` entries (`retained_wire.rs:1634`, `:1946`, `lib.rs:3078`, `retained_product.rs:4492`, RS `retained_precision.rs:4371`) makes TEXT incomplete with `id-unaudited` at that site. Removing the new static rule for the terminal kind makes it incomplete on that expression, with a finding labelled `to_owned`; my script expected a different label, so it prints `pass=False`. The unmodified run is complete.

## 2. M (D-7)

From the in-build E+R and TAV_W 4,301,774,658:

| M | Sparse: fraction, margin, budget | Dense: fraction, margin, budget |
|---|---|---|
| 10.25 GiB | 0.8905, 104,592,160, 2.43 % | 0.8959, 45,460,816, **1.06 %** (fails 5 %) |
| **10.5 GiB** | **0.8693, 346,184,070, 8.05 %** | **0.8745, 287,052,726, 6.67 %** |

**10.5 GiB (11,274,289,152 B) is the smallest 256 MiB step** with E+R ≤ ⌊0.9 M⌋ and a text-error budget of at least 5 % (margin / TAV_W, ADD §1's measure) in both modes. It is within ROOT's 12 GiB. Q-N1's ~30 KB would not move it: at 10.25 GiB dense still fails by about 170 MB of budget. **Confirmed.**

## 3. G6 and the registration

- **`registration.diff`** applies cleanly as one hunk. **PP's whole suite in the registered copy (fresh target): 741 passed, 1 failed (`s11g_tests::t13_committed_fallback_uz_is_byte_identical`, the known Mac t13), 79 ignored**, as I104 reports (`E/suite/`). Law tests 47/47 at `M − R − 1`, `M − R`, `M − R + 1` (`admission_bound_adds_r_…`, `bound_admits`) and `maximum_takes_every_phase` (each of the 7 phases largest, by requested and by moving part).
- **The 0.9 M rule:** pinned in both modes (`MARGIN` = 10,146,860,236, asserted in `profile_laws_hold_in_this_build`).
- **The release record** equals dev/test (I104's records; `diff` of the 265 lines, exit 0). I did not rebuild release.

## 4. The re-pins, SF-1, RV112's N-1, N-2 and N-5, E-12

- **Every re-pin the brief lists is present and right:** `const M`; `threshold_bytes`; the three 0.9 M margins as `MARGIN`; `profile_in_build_record`'s denominator and `PINNED_RECORD` (asserted in-build); `challenge_bounds_are_the_profile` (W1, E_mov,max, `CAP_BYTES` = 16 GiB, the N1 text); I89's value pins (Text(diag_env) 175,409,684; L_PUB 2,599,962; L_DIAGID 2,330; Text(err) 16,384; D_env 22,911; PushCap(D_env) 32,768; Text(row) 11,474, unchanged); A1-N-3's three tests; SA's expression test. No stale literal remains in P (`4_026_531_840`, `3_623_878_656`, `68_720_236`, the old phase values).
- **SF-1:** `phase_caps().late[9]` = T11 − `F_T11_LATE_CAPTURE` / C; exact because every coefficient is a multiple of C (pinned; M09 dies).
- **N-1:** the PP test reads the runner's one `C_PLUS_ONE` line and holds it to C + 1 (M18 dies).
- **N-2:** the C = 3 parked-slot test kills G04 (M19: 0 ≠ 101).
- **N-5:** T11.8 (2 × `s(CaseSlot)`, 1,336 B in-build), T11.9 (2c × 16 B) and T13.3 (a × 248 B) are priced (+3,512 B); removing either term, or binding `s(CaseSlot)` to 0, is killed by the pinned record and the challenge bounds (M10–M12).
- **E-12:** `retained_product.rs` is in `RULE8_FILES` with its two integer sites (`check_support_maps`, `selected_attempts`). Dropping it fails with "unknown file" (M20); a new float accumulation there fails as unlisted (M21).
- **Q-N1's size** (`E/probes/size_probe_run.log`, a test-only probe in `mut`):
  - `CaseAttempt` 9,400 B, `AttemptEnd` 8,704, `RefusedCase` 8,704, `FrozenCase` 4,392, `PreparedTrace` 520, `AttemptParts` 128;
  - `CaseSlot` 1,336 (N-5's in-build value, confirmed), `PrimitiveSource` 248;
  - `PreparedCases` 2,936 and `ProductCapture` 2,176, both on the stack.

## 5. The witnesses (`E/witnesses/`, registered dev/test build, R/16 = 4 MiB)

All 51 lib entry points ran as their own processes (`<lib binary> <name> --exact --ignored --test-threads=1 --nocapture`), each through `t3_slot.sh`: **28 witnesses, 12 ordinary controls, the floor and 10 DEF-O reports, all exit 0**, with no overflow, abort or panic. The outcomes are asserted and match QUAL_B1 §4:
- W1, W2-deep, headroom, W-C2 (at 4 MiB and 1 MiB), W-C2's (A, C), c1 and the three-case input publish;
- W2 and W4 end at Preparation; `b2_k1e3` at Candidate; W6 (case C) at Native; W2b and PHYS-R4 at `NoTriggeredCase` with exact bytes;
- W3 is ExactSelected; W7 gives its five fallbacks.

The three-case witness asserts, through `assess`, that the input is inside D1 with raw depth 16, three cases and Σ l_i = 384, and checks the input's hash. `stressed()` escapes every provenance. I ran the dev/test build only. I104's release logs show the same outcomes.

## 6. The challenge (`E/challenge/`)

All 27 ignored entries (one input, mode and route per process) and the default test pass. **Every peak is within its A1-S-1 bound:**
- a run with W1 work (a successor, or one N1 notice for `b2_k1e3`) is bounded by E_mov,max;
- no-W1-work runs (W2 through Direct) and the ordinary route by the W1 phase.

The largest is the three-case input, dense Direct: 118,781,785 B against 9,792,698,646 (1.21 %). The requested-heap peaks equal I104's to the byte (deterministic). `CAP_BYTES` is 16 GiB, held by `challenge_bounds_are_the_profile` (M13). The furthest phase per input is the witnesses' (§5): W5 for publishers, W2 for `b2_k1e3`.

## 7. RSS_TIME.md

- **Method:** `rss_batch.sh` under `t3_exclusive.sh`, four batches, 159 runs, all rc 0. The guard log shows each batch as START-/END-EXCLUSIVE, with no slot job between them. One process per run and mode, binaries run directly, 3 repetitions.
- **The headline values trace to the raw `time -l` files,** median and maximum: dev three-case dense Direct 161.0/161.0 MiB RSS, 112.3/112.3 MiB footprint, 51.56/51.72 s; release 206.3/206.5 MiB, 134.3/134.4 MiB, 1.74/1.76 s.
- **My reproduction** (`E/rss/`, one `t3_exclusive.sh` batch on my registered build, one process per run). It agrees within run-to-run noise, and the requested-heap peaks match to the byte:

  | Run | Reps | RSS median / max, MiB | Footprint median / max, MiB | Real median / max, s | I104 |
  |---|---|---|---|---|---|
  | Three-case, dense, Direct | 3 | 160.9 / 160.9 | 116.9 / 117.6 | 50.93 / 51.20 | 161.0 / 161.0; 112.3 / 112.3; 51.56 / 51.72 |
  | c1, sparse, Direct | 3 | 69.6 / 69.6 | 51.7 / 51.7 | 16.75 / 16.80 | 69.8 / 71.8; 51.8 / 52.2; 17.23 / 17.29 |
  | Milestone, dense, Direct | 1 | 19.9 | 7.4 | 0.66 | 20.5; 7.8; 0.65 |
  | Process floor | 1 | 2.7 | 1.6 | 0.00 | 2.7; 1.6 |
- **Phase coverage, the census of what the inputs leave below the caps, and the non-claims** (16 GB behaviour not observed, no swap, debug timings pessimistic, RSS includes shared pages, no supported-machine claim) are stated as PLAN_v2 §3.6 and RR ruling 3 of I86 require.
- RR's "springs at most 31/192" was I86's bound; RSS_TIME's count is 21 (7 copies × 3). The census's `string_bytes`/`key_bytes` have no cap in the JSON, but the prose gives 65,536.

## 8. QUAL §11's carry (`E/noncand/`)

On my own c = 3 point, the non-candidate rows are identical to I104's `noncand.json`. With the multiplicity dropped from the key: 408 of RV87's 410 match, 2 are gone (`freeze_candidate`'s and `one_case`'s, replaced), and 4 are new. I read the 4 by type:
- `serialize_attempt` `terminal["kind"]`: a kernel terminal token (`selected`/`refused`/`unresolved`);
- `format!("kernel_{other}")`: the same token;
- `native`'s `error.clone()`: a `CaptureError`;
- `freeze_case`'s `failure.failure()`: a `ProductFailure`, the moved row.

None is an identifier alias. Agreed.

## 9. DEF-O's shares (item 9)

**Reproduced:** `b2_k1e3` fails 81 rows in each mode, all `SharperExact` (predicates F, F, T, T), with the first failing row a `displacement_magnitude`. c1 and the three-case input fail none; W-C2's case C ends Native.

The kinds come from my probe in `def_o_report` and, independently, from `freeze_case`'s own `I51_FROZEN_REFUSAL` rows (`E/probes/`):

| Failing rows (each mode) | Unit and DEF-O projection | Count |
|---|---|---|
| `displacement_magnitude` | mm, `/1000` (NC-1's mm→SI) | 2 |
| element torsional / bending z / bending y stress | MPa, `× 1e6` (the same second-rounding property, not named in NC-1) | 30 + 18 + 4 = 52 |
| `pipe_elastic_normal_stress_maximum_v2` | Pa, none | 12 |
| element axial / shear z force | N, none | 10 + 5 = 15 |
| support magnitudes (nested hypot) | — | 0 |

**The claim holds:** neither DEF-O property is the sole cause of either fallback, because the 27 unprojected rows fail too. See Q-N2 for the MPa rows.

## 10. My mutants (`E/mutants/`; registered copy; each built and run through `t3_cargo.sh`)

| ID | Mutant | Killed by |
|---|---|---|
| M01 | G-B bound back to `T11 − T11_late_capture` | `b1_sa_gate_bounds_…`, `b1_sq_late_capture_…` |
| M02 | `/ 2` for `/ C` | the same |
| M03 | no late subtraction | the same, and `every_phase_fact_…` |
| M04 / M05 | `threshold_bytes` − 1 / 12 GiB | `the_registered_profile_is_the_only_permit_source` |
| M06 / M07 / M08 | Text(diag_env) + 1 / D_env − 1 / L_DIAGID + 1 | `every_phase_fact_…` (M07 also `profile_laws_…`) |
| M09 | a late coefficient not a multiple of C | `b1_sq_late_capture_form_is_c_times_one_case` |
| M10 / M12 | N-5's T11 / T13 term removed | `challenge_bounds_…`, `profile_in_build_record`, `profile_transcribes_…` |
| M11 | `s(CaseSlot)` = 0 in-build | `challenge_bounds_…`, `profile_in_build_record` |
| M13–M16 | challenge `CAP_BYTES`, `MAX_PHASE_BYTES`, `W1_PHASE_BYTES`, N1 text | `challenge_bounds_are_the_profile` |
| M17 | the challenge ignores the N1 notice | **survives** (Q-N4) |
| M18 | runner `C_PLUS_ONE` = 5 | `b1_sa_runner_oracle_literal_…` |
| M19 | G04 | `b1_sq_retained_error_text_reads_every_parked_slot_at_c` |
| M20 / M21 | E-12 reverted / a new float accumulation | s11f rule 8 |

The baseline (M00, probe only) passes 47/47 law and 11/11 s11f. The copy was restored and `diff -rq` checked clean after each chain.

## 11. For ROOT

1. **R6b:** M = 10.5 GiB is confirmed; `registration.diff` is ready to apply as it stands.
2. **Q-N1:** rule whether `s(CaseAttempt)·a` is priced before R6b (as N-5 was) or carried to SB.
3. **Q-N2:** the MPa projection's second rounding belongs in any DEF-O revision ROOT considers beside NC-1's mm→SI.
4. Q-N3 to Q-N5 are records-only.

**Hashes:** RETURN.md `1712ba8653eec055626d60ee10d58a6c8fd31b9112221e386456244b892df330`; RETURN_ADDENDUM_01.md `5cb3c4612244c1ec042713f6bb6c519712e6a12236604102ce87b6d62449fae1`; QUAL_B1.md `eb6541fce58be0c7dac4720f0a9b8a8cdd6f0ad5d07c674e8f8f21bd48166dfc`; RSS_TIME.md `f230c7ecea8298e93d8eaf7c87ae3c1ec8f6a9178f2378799593c103e0cfef90`; registration.diff `d85101ea1bca112aa742ab430c5538a548a9fa345e05ea1410d96d91f37d6526`.

**Records:** this file, `evidence/` (sanitized logs, my tools, the tables), `SHA256SUMS`. Placeholder paths only; no symlink; no folder named `build`; the host screen's patterns find 0 hits (`E/screen.txt`).
