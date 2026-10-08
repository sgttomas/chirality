# RV126 (RV-N): the fresh independent review of PR-N (the correctly rounded norm)

**Who:** RV126, TASK (Type 2), independent reviewer dispatched by WORKING_ITEMS for T3 (Agent 1), 2026-10-08 UTC. I wrote none of this code and did not delegate.
**Brief:** `R/BRIEFS/RV126_RVN_PRN.md` (sha256 `70321724…0aec5f9`, verified) with `R/BRIEFS/B1_COMMON.md` (`2d170307…2eb2c75`, read), NUM's `AGENTS.md` and `agents/AGENT_TASK.md`. Mid-task, WORKING_ITEMS sent PR #1163's head `dab19291a8` (the code commit plus the package `T/IMPLEMENTATION/PR_N/`) and asked that the package be in item 4.
**Basis:** RR "I109: a correctly rounded norm replaces libm `hypot` on published paths; …" and RR "RV125 confirms PR-B1's platform test repair; …" (A1-N1); the implementer's `R/I109/platform_norm_01/RETURN.md`, `R/I109/pr_n_01/RETURN.md` and `R/I109/pr_n_package_01/_run_records/`.

| Head | Base | What | Status |
|---|---|---|---|
| `8dd64c1835698da87e5f0fd303c1b886daee956f` | main `7eae707bb7` | the code commit, 21 maintained files | reviewed (items 1–5) |
| **`dab19291a86f28ee2d26c6ddace5c10e359c68ef`** (#1163's head) | the same | + the package (CHANGE_RECORD.md, PR_BODY.md, citations.json, SHA256SUMS) | reviewed for item 4; #1163's body equals `PR_BODY.md` |

**Placeholders:** `WT`, `NUM`, `P`, `PP`, `FK`, `RE`, `T`, `R`, `RR` as in the brief. `S` = my scratch `WT/scratch/rv126_n/`. `A` = my archive copy `WT/rv126/` (`git archive 8dd64c1835`, `P/execution` excluded). `E` = this folder's `_run_records/`. Line numbers are at `8dd64c1835`.

## Verdict: **FAIL** at `dab19291a8`, on B-1 only: 1 BLOCKING, 1 SHOULD-FIX, 8 NOTE

- **The norm is correct.** I read the algorithm, its proof sketch and every special case against `hypot`'s contract and found no defect (§1). **My own exact oracle finds 0 misrounded in 2,801,296 results**, with 201,256 exact ties among them (including 3-D ties, power-of-two ties and the exact overflow-threshold tie), checked two independent ways. Debug equals release, and a wasm32 build (software `fma`) equals aarch64 bit for bit.
- **Every call site is right** in arity and semantics, and no published-path `hypot` is left (§2).
- **The re-pins are right** (§3): every moved value is the correctly rounded norm of its own components, each hash follows from it, B1's glibc variants are gone with no pin weakened, u1 is unconditional, m08 uses `norm2`, and the ring check is tightened exactly as RV125 A1-N1 asked. glibc dispatch 37820998162 on the identical 21 files has since succeeded.
- **B-1 is the only blocking item, and it is a ruling, not a repair.** Under the brief's admission view ("a changed decision would be a defect"), the rank screen's decisions do change on synthetic bodies: the Restrained screen in both directions, but only within ~0.15 % of its threshold, where the parent's own decision is non-monotone and already platform-dependent; and one witness class at 10²⁰⁰ scale. No committed input changes and no true mechanism can be admitted. ROOT either accepts this or drops `d538f469af` (§2a).
- **S-1:** the scope sentence "a published 3-component magnitude is the correctly rounded 3-norm" (and `PP/src/lib.rs:38`) is broader than the change: the selected-source `scaled_norm` and the displacement magnitude are not the norm.
- **My spot checks pass:** PP 743/0, RE 199/0, FK 499/0, PY 1,079/0 and TS (all four files that read the corpus) 1,314/0.

## Findings

| ID | Class | Where | Evidence | Remedy |
|---|---|---|---|---|
| B-1 | **BLOCKING by the brief's admission-view rule**; no code defect; discharged by a ROOT ruling | `FK/src/rigid_body.rs:53`, `:109` (`d538f469af`'s two calls), deciding at `:154-157` (Restrained) and `:158-191` (the witness) | §2a. On synthetic bodies the head changes decisions that the parent made on this Mac: (a) the Restrained screen, **both ways** (59,600 newly Restrained and 66,967 newly not, in 1,045,305 near-transition probes), only within 1.5·10⁻³ relative of the threshold, where the parent's own decision is non-monotone; (b) one witness class in 300,000 random bodies, MechanismWitnessed → NumericallyUnresolved at 10²⁰⁰ scale, which changes the refusal's integrity code. No committed input changes; both directions are sound (no true mechanism is admitted); the parent's band decisions already differed by platform | **ROOT rules** under the admission view: (i) accept decision changes confined to the screen's noise band, and the witness-class change, as the cost of a platform-independent screen (B-1 then closes; the package states it, with N-5's bytes), or (ii) drop `d538f469af` from PR-N (the screen keeps libm `hypot`, its macOS/glibc disagreement in the same band, and its T3-close item). No repair to the norm or the other call sites is indicated |
| S-1 | SHOULD-FIX (scope) | `PP/src/lib.rs:38` ("published norms are correctly rounded"); the commit message ¶1, CHANGE_RECORD.md:23 and PR_BODY.md ("A [published] 3-component magnitude is the correctly rounded 3-norm") | Two published magnitude paths are not the norm and are not correctly rounded: the selected-source support magnitude `source_receipt::scaled_norm` (`PP/src/lib.rs:4926-4927`; `PP/src/source_receipt.rs:46-53`, m·√((a²+b²)+c²)), and the nodal displacement magnitude `displacement_magnitude` (`PP/src/lib.rs:13916-13921`, √(Σ powi(2))). I109 round 1's own audit found 4 committed `fields` magnitudes that are not RN3 from the first. Both are deterministic IEEE, so this is not a platform claim, but the sentences say every published 3-component magnitude is RN3 | Reword `lib.rs:38` (e.g. "magnitudes formerly formed with libm `hypot` are correctly rounded norms; `scaled_norm` and `displacement_magnitude` are deterministic but not correctly rounded") and qualify the CHANGE_RECORD and PR body sentences ("every magnitude formerly formed with a libm `hypot` chain"). The commit message would need a recut; WORKING_ITEMS' call whether the package's correction suffices |
| N-1 | NOTE | `PP/tests/preview_physics_runtime.rs:1-8` vs `:9`, `:281` | The header says "nothing here derives an expectation from product code"; m08's expectation now imports FK's `norm2`. It is exact and independently verified (§1), so the check is sound, but the header is no longer literally true | Add one header line: the intensified identity uses FK's `correct_norm::norm2`, verified against an exact oracle |
| N-2 | NOTE | `FK/src/rigid_body.rs:466`, `:542-543` | K5's comments still contrast its screen with `assess_rigid_body`'s `hypot` ("`sqrt` forms in place of `hypot`"; "as `assess_rigid_body` (:88-131), with `root_one_plus_square` in place of `hypot(ζ, 1)`"). That function now uses `norm2(ζ, 1)`, and its Jacobi is at `:89-132` | Update the two comments (e.g. "in place of `assess_rigid_body`'s `norm2(ζ, 1)`", `:89-132`) |
| N-3 | NOTE (scope wording) | CHANGE_RECORD.md:25 and its table rows `:37-38` | "Every product `hypot` whose result reaches published bytes, a receipt or diagnostic text now calls the norm: 30 of the 32". The 30 include `elastic_section` (no caller; the table says so) and the rank screen's 3 (an admission decision). The sentence is true as a universal; the count reads as 30 published sites | "30 of the 32 product `hypot` calls now call the norm: every one that reaches published bytes, a receipt or diagnostic text, plus the rank screen (admission) and `elastic_section` (no caller)" |
| N-4 | NOTE | `FK/src/correct_norm.rs:6-8`; CHANGE_RECORD §1 "Every platform gives the same bits"; commit message "no longer depend on the platform's libm" | On a target without hardware FMA, `f64::mul_add` is a call to `fma`: libm's on x86_64 baseline (the hosted CI builds with no `target-cpu`), compiler-builtins' on wasm32 (the browser engine links PP). Rust's `mul_add` contract and IEEE 754 require it correctly rounded, so the claim holds given a conforming `fma`. I measured wasm32 (software `fma`) bit-identical to aarch64 (hardware) on 2,721,296 results; x86_64 is evidenced by the glibc dispatches' pins only | Optional: say "IEEE operations, `sqrt` and a correctly rounded `fma` (hardware, or the platform's `fma` where there is none)" |
| N-5 | NOTE (scope) | `FK/src/rigid_body.rs:213` (node motion = L·t + θ × Δ); `FK/src/structural.rs:298-300` (`Display` is `Debug`); `PP/src/lib.rs:1329`; `PP/src/retained_wire.rs:720-721` | The rank screen is described as "an admission decision" only. Its L also scales a witnessed mechanism's translations, which are published: in the blocking diagnostic text (`{error}`) and bit-encoded in the retained wire. On this Mac, 22,966 of 246,587 synthetic witnessed mechanisms change node-motion bits. No committed pin carries one that moved | Add to CHANGE_RECORD §1's rank-screen row and §2: published mechanism directions move by an ulp wherever the libm L did |
| N-6 | NOTE | PR_BODY.md, Evidence ("the PY and TS readers that read the corpus: all pass"); CHANGE_RECORD §3 | I109 ran the two PY files and one of the four TS files that read the corpus (`retainedPrecision.test.ts`). RV126 ran all of them at the head: PY 1,079 passed, TS 4 files and 1,314 tests passed, 0 failed (§5). So the claim is now true, but on my evidence, not the package's | Cite the four TS files (or this review) for "all pass", or say "`retainedPrecision.test.ts`" |
| N-7 | NOTE | CHANGE_RECORD.md §3 ("Result: pending") and §4's row; PR_BODY.md ("glibc dispatches 37808190331 (success) and 37820998162") | 37820998162 on `7bd84e0526` (21 files equal to `8dd64c1835`'s) completed with **success**, numerical cargo suite included: the first glibc run of u1's unconditional pin and the single W-C2 and SF-2 pins. Until it is cited, "On glibc every committed pin holds" rested on 37808190331, which did not assert u1's ordinary pin | Record the success in the CHANGE_RECORD and the PR body |
| N-8 | NOTE | `FK/tests/retained_k4/product_final_case_tests.rs:342`; `PP/tests/support_reactions_runtime.rs:130`, `:135` | Expectations still formed with libm `hypot` chains: the first asserts **bitwise** equality between `support_hypot` (now `norm3`) and a libm chain on (3, 4, 12), zeros and subnormals (1, 2, 3)·2⁻¹⁰⁷⁴, which any faithful libm gets exactly; the others are toleranced | Optional: exact constants (13, 0, 4·2⁻¹⁰⁷⁴), or `norm3` |

## 1. The norm (`FK/src/correct_norm.rs`)

**Read against `hypot`'s contract (C Annex F, IEEE 754 RN-even):**
- **Special values** (`:40-45`, `:56-58`): ±∞ anywhere gives +∞ before the NaN test (so `hypot(∞, NaN) = +∞`); otherwise NaN gives NaN; all zeros give +0 (`x0` is an `abs`); `norm2(x, ±0)` = |x| through the `y1 < 2⁻⁶⁰` path. Correct.
- **Sorting** (`:47-55`): three compare-swaps give x0 ≥ x1 ≥ x2. Correct.
- **Scaling** (`exponent`, `scale`, `pow2`): `exponent` is floor(log2) including subnormals; `scale` is exact whenever the result is normal or x is scaled up (when k < −1000 and the result is normal, the intermediate x·2⁻¹⁰⁰⁰ ≥ the result is normal too). y0 ∈ [1, 2) exactly; y1, and y2 when kept, are exact. `pow2`'s argument stays in [−1022, 1023]: k = ulp_exponent(r) − 1 − e lies in {−54 … −52} for normal results and in [−52, −1] for subnormal ones, and r = MAX only when e = 1023 (k = −53). My debug driver ran every input with debug assertions and overflow checks on and never tripped `pow2`'s assertion.
- **Step 1** (`:62-64`): with y1 < 2⁻⁶⁰ the exact norm is < x0 + 2^(e−120), below the half-gap 2^(e−53) (wider for subnormal x0; at x0 = MAX it is below the overflow threshold). Correct.
- **Step 2, the sticky bit** (`:65-70`): when y2 < 2⁻¹²⁰ is dropped, S = y0² + y1² is a multiple of 2⁻²²⁴ (y0 a multiple of 2⁻⁵², y1 ≥ 2⁻⁶⁰ a multiple of 2⁻¹¹²), and every midpoint m (rs ≥ ~1, half-gap ≥ 2⁻⁵⁴) has m² a multiple of 2⁻¹⁰⁸. So S − m² is 0 or ≥ 2⁻²²⁴ > y2² in magnitude: y2 can only break an exact tie, upward. Correct. A kept y2 ≥ 2⁻¹²⁰ squares exactly (its `mul_add` error term is ≥ 2⁻³⁴⁴, normal).
- **Step 3, the correction loop** (`:84-108`): the up test (`above > 0`, or a tie with sticky or odd r) and the down test (`below < 0`, or a tie with no sticky and odd r) implement RN-even exactly; the gap below a normal power of two is halved, and not below MIN_POSITIVE (`bits >> 52 > 1`), which is right; MAX's upper midpoint is the overflow threshold 2¹⁰²⁴ − 2⁹⁷⁰, and MAX is odd, so an exact tie goes to +∞, as IEEE requires. Once it moves up it never moves down (the new lower midpoint is the old upper one), and vice versa, so it terminates.
- **`midpoint_sign` / `exact_sign`:** rs² = rr + rq exactly, 2·rs·h and h² are exact (h a power of two), the ten terms are bounded (no overflow in TwoSum), and Shewchuk's grow-expansion with zero elimination leaves a nonoverlapping expansion whose largest component has the sign of the sum. Correct.
- **The loop count** (CHANGE_RECORD §5 "at most two iterations"): an instrumented scratch copy (`E/tools/iter/`) counted loop passes over my 1,360,648 triples (2,721,296 calls): 2,045,660 calls entered the loop, 119,616 of them took a second pass, **none a third** (`E/results/loop_passes.txt`). That supports the argument; it is not a proof.
- **The proof sketch in the module doc** matches the code.

**My own exact oracle** (`E/tools/`, written without I109's harness):
- **Generator** `gen.py` (seed 126; Python 3.13.14; reproducible: the regenerated file has the same sha256 `983d3a10…`): **1,360,648 triples** in 11 classes:
  - every ordered triple of 22 special values (10,648);
  - random bit patterns (150,000) and comparable magnitudes over the whole exponent range (250,000);
  - dynamic ranges straddling the 2⁻⁶⁰ shortcut and the 2⁻¹²⁰ sticky threshold, including both thresholds' exact neighbours (150,000);
  - **exact 2-D midpoints** from Euclid's formula (h odd in [2⁵³, 2⁵⁴)), scaled over the range, with no, sticky or kept third components and 1–3-ulp perturbations (200,000);
  - **exact 3-D midpoints** from the quaternion form of Pythagorean quadruples (100,000), which I109's adversarial set did not include;
  - 2-D near-midpoints with a small second component (100,000) and 3-D near-midpoints with the third component solved exactly toward a midpoint, including those beside powers of two (200,000);
  - subnormal results, subnormal-grid near-ties and the MIN_POSITIVE boundary (100,000);
  - the overflow threshold and near-MAX triples (50,000); small integers (50,000).
- **Oracle** `check.py`, two independent exact checks on every result:
  - **A** computes RN(√S) from an integer square root of S = N·4^E0 (all components as integers times 2^E0), on the destination's quantum (subnormal grid; overflow at 2¹⁰²⁴ − 2⁹⁷⁰) with ties to even;
  - **B** verifies the implementation's r directly: D² ≤ S ≤ U² at r's own lower and upper midpoints, with the tie rule, without computing RN.
  - **Self-test** `selftest.py`: on 29,681 sampled triples (59,362 results, 3,655 exact ties), A agrees with a third, decimal-based rounding (1,600 digits) everywhere, and B accepts every RN result and **rejects both binary64 neighbours of every one** (`E/results/selftest_30000.txt`).
- **Result: 0 misrounded in 2,721,296 results** (norm3 and norm2 per triple), by A and by B, with A and B never disagreeing (`E/results/oracle_report.json`).
  - **Closeness:** 167,233 results are exact ties (120,727 norm3, 46,506 norm2), 87,800 more are within 2⁻⁶⁰ ulp of a midpoint (sticky-broken ties) and 235,965 within 2⁻⁴⁰ ulp.
  - For scale, this Mac's libm `hypot` is not correctly rounded on 148,977 of the 1,360,648 norm2 inputs, and its chain differs from RN3 on 387,092 norm3 inputs.
- **A targeted family** (`tie_pow2.py`): 40,000 triples on exact 3-D ties at h = 2⁵⁴ − 1, the lower midpoint of a power of two, scaled over the range **including h·2⁹⁷⁰, which is exactly the overflow threshold** (the exact tie must give +∞). 34,023 exact ties, 26,371 power-of-two results and 10,589 +∞ results: **0 misrounded in 80,000 results** (`E/results/oracle_tiepow2.json`).
- **Debug equals release:** the driver built with `-C opt-level=0 -C debug-assertions=on -C overflow-checks=on` and with `-C opt-level=3` gives byte-identical outputs (`c50bcb73…`).
- **A second target:** the same module built for `wasm32-unknown-unknown` (the browser operation engine links PP, so it ships the norm; there `mul_add` is software `fma`) and run under node gives **bit-identical results to aarch64's hardware FMA on all 2,721,296 results** (`E/results/wasm32_vs_native.txt`).
- **Cross-check with I109:** my oracle agrees with all 2,400 expected results of the committed `correct_norm_vectors.txt` (180 of them exact ties), and my driver reproduces them.
- **Total: 0 misrounded in 2,801,296 results.**

## 2. The call sites

All 30 product replacements (I109's inventory, `R/I109/platform_norm_01/_run_records/inventory/inventory.tsv`, 32 product `hypot` calls) were read at the head:

| Site | Arity and semantics |
|---|---|
| `PP/src/lib.rs:4928` | ordinary support force magnitude: `norm3(F)` for the former chain; the selected-source path keeps `source_receipt::scaled_norm` (unchanged) |
| `PP/src/lib.rs:5124` | formation guard q = `norm2(My, Mz)` |
| `PP/src/lib.rs:11876`, `:11882` | support-action force and moment magnitudes, `norm3` |
| `PP/src/lib.rs:13511` | combined vector magnitude, `norm3` |
| `PP/src/preview_physics.rs:465`, `:634`, `:966`, `:967` | tangent \|cross\| (`atan2` stays libm), i·`norm2(My, Mz)`/Z, combination magnitudes |
| `PP/src/pressure_runtime.rs:1082`, `:1100` | chord length and collinearity residual, `norm3` |
| `PP/src/retained_product.rs:2446` | the retained support guard against the published magnitude: now an exact identity |
| `PP/src/case_state/resolve.rs:899` | `reference_length_m` = `norm3(to − from)` |
| `FK/.../product_certificate/final_case.rs:1851` | `support_hypot`: one `norm3`, still charged two scalar operations (the charges are unchanged in order and count; the test at `FK/tests/retained_k4/product_final_case_tests.rs:339-350` passes) |
| `FK/src/rigid_body.rs:53`, `:109` | the rank screen: L = max `norm3(r)`; Jacobi √(ζ² + 1) = `norm2(ζ, 1)` (an infinite ζ still gives t = 0) |
| `P/core/loads/stress_recovery/src/elastic_section.rs:106` | `norm2(by, bz)`; by `#[path]` (`stress_recovery/src/lib.rs:9-12`). The function has no product caller (PP uses `elastic_extrema` only): outside the published paths, with I109's stated reason |

- **Arity and order:** every former two-`hypot` chain became one `norm3` with the same three components; every single `hypot` became `norm2`. The ordinary magnitude and the retained certificate's projection both use `norm3` of the same components, so their agreement is unchanged (and now order-independent).
- **Nothing left out:** at the head the only product `hypot` calls are `performance_harness/src/lib.rs:1078`, `:1080` (a dependency only of `validation/benchmarks/numerical_robustness`). The readers' `hypot` (RS, PY, TS) stays inside their 64ε guards. The desktop's viewport `Math.hypot` (measurements, picking) is UI, not a published result.
- **Nothing else changed without reason:** the other hunks are tests, fixtures, the reader corpus and comments.
- **Other published magnitudes that are not the norm:** see S-1.
- **The rank screen under the admission view:** see §2a and B-1.

### 2a. The rank screen (`d538f469af`'s two calls): the admission view

I built a differential harness (`E/tools/rank/`, through `t3_cargo.sh`): the head's `assess_rigid_body` against the parent's (FK at `7eae707bb7`'s `rigid_body.rs`, libm `hypot`), on this Mac.

- **Random bodies** (300,000: six classes of 1–5 nodes, at scales 10⁻²⁰⁰ to 10²⁰⁰, random, nearly collinear, nearly coplanar, integer and oblique-integer geometry, random or translation-only ground sets; `E/results/rank_random.txt`):
  - **The Restrained decision never changed.** Statuses at the head: 21,223 Restrained, 246,587 MechanismWitnessed, 32,190 NumericallyUnresolved.
  - **One witness class changed:** MechanismWitnessed (parent) → NumericallyUnresolved (head), on coordinates `[[3e200, −1e200, −1e200], [3e200, 6e200, 3e200]]`, ground dofs `[0, 2, 1, 8, 6]`. L = ‖(0, 7e200, 4e200)‖ is `8.062257748298551e200` from this Mac's chain and the correctly rounded `8.06225774829855e200` from `norm3`. The smallest singular value is 0 in both, so both refuse; but the parent found an exact witness through a rounded candidate that depends on L's last bit, and the head does not (the exact unnormalized candidate overflows the `Expansion` at this scale). The refusal's integrity code changes from `NUMERICAL_INTEGRITY_PHYSICAL_MECHANISM` to `NUMERICAL_INTEGRITY_UNRESOLVED` (`PP/src/lib.rs:1306-1320`), with different published refusal content.
  - L's bits changed in 33,653 bodies and the published node motions of 22,966 witnessed mechanisms changed (N-5).
- **The threshold hunt** (`E/results/rank_hunt.txt`): 2,000 nearly collinear bodies (2–4 nodes, translation grounds), whose rotation about the line is held only through offsets c_k·δ. For each, δ* is the parent's Restrained transition (bisection); 1,305 transitions were found.
  - **At the 801 consecutive doubles around each δ*:** 126,567 of 1,045,305 decisions differ, **in both directions**: 59,600 are Restrained only at the head (newly admitted by the screen), 66,967 only in the parent. The parent flips once per transition there; the head's transition is displaced by ~97 ulps of δ on average.
  - **Over δ*·(1 + j·10⁻⁶), |j| ≤ 2,000:** 56,833 of 5,221,305 decisions differ, all within |j| ≤ 1,482 (1.5·10⁻³ relative of the transition; for 495 of the 498 transitions with a difference, all of it lies within 10⁻³). In the same band **the parent's own decision is not monotone in δ** (4,041 flips over the 1,305 transitions, where a monotone decision would flip 1,305 times; out to 1.7·10⁻³).
- **Reading.**
  - The changes are confined to the screen's rounding-noise band: σ_min within about 0.15 % of τ = 64·γ·σ_max, where τ is a few hundred ε·σ_max and σ_min carries an error of order ε·σ_max. There the parent's decision already depended on the last bits of its inputs, and so on the platform's `hypot` (macOS and glibc differ there today).
  - **Both directions are sound:** a true mechanism has σ_min = 0 and a computed σ_min far below τ in both versions (none of the 246,587 + 32,190 non-Restrained random bodies changed to Restrained; the hunt's δ → 0 end is non-Restrained in both). A body newly admitted in the band has σ_min ≈ 10⁻¹³·σ_max ≠ 0.
  - **No committed input lies in the band:** every suite passes on the Mac (mine, I109's 40 manifests) and on glibc (37820998162).
  - **But by the brief's rule** ("a changed decision would be a defect"), these are changed decisions, of both the Restrained screen and the witness class. They cannot be removed by any correct change to L or to √(ζ² + 1): any change of last bits moves the band's decisions. Hence B-1, for ROOT.

## 3. The re-pins

- **Every moved value is the correctly rounded norm of its own components.**
  - My `magnitudes.py` checks every support magnitude row against RN3 of its own `Fx/Fy/Fz` (or `Mx/My/Mz`) rows with oracle A: the W-C2 dense fixture, 30 of 30; the reader corpus's producer-solved cases 15–25, all. The only non-RN3 magnitudes in the corpus are in the synthetic cases 0–14 and in mutations and must-pass edits built on them, as I109 round 1 reported (17 in cases 0–14).
  - Each of the 7 moved values in `R/I109/pr_n_package_01/_run_records/moved_values.json` (and CHANGE_RECORD §1's table): "after" equals my oracle's RN3 and the head's `norm3`, and "before" equals this Mac's libm chain (`f64::hypot` from Rust, not Python's `math.hypot`, which is CPython's own); each move is one ulp (`E/results/moved_values_check.txt`). The fixture's `rigid:N0` components equal the record's hex.
- **Each hash follows from the moved value.**
  - The fixture differs from its parent in exactly three lines: the value, `publication_sha256` and `receipt_sha256`. Its sha256 is `c11f7566…`, as `W_C2_PINNED`, the corpus's `provenance.fixture_sha256` and `N07_W_C2` say; the corpus case's `source` equals the fixture's `source`.
  - The corpus moves 11 lines: case 18 (5), case 23 (5: the value, both hashes, `successor_bytes_sha256` and `receipt_sha256` in provenance) and the one mutation value.
  - In my PP run, `b1_sp_w_c2_fixtures_are_the_live_successors`, `b1_sp_w_c2_direct_entry_publishes_the_pinned_successor`, `b1_sp_sf2_selected_not_first_and_two_selected_pins` and `u1_ordinary_bytes_unchanged_under_capture` pass: the live product produces the re-pinned bytes and hashes. **Independently:** starting from the parent's (`7eae707bb7`) W-C2 dense fixture and the parent's corpus cases 18 and 23, I replaced only the one value and recomputed `publication_sha256` and `receipt_sha256` with the PY reader's own recipe (`retained_precision.py:1783-1784`, `_hash` over the checked JCS, with the binary built from `A`). Each result equals the committed source exactly, and every other corpus case is unchanged (`E/results/rehash_check.txt`). The PY reader suite also verifies these hashes (§5).
- **B1's glibc variants are gone, with no pin weakened:** `GLIBC`, `W_C2_DENSE_GLIBC(_RECEIPT)`, `w_c2_on_this_platform` and `CBA_DENSE_GLIBC` are removed; the fixtures test compares the live document with the fixture on every platform; SF-2 has one pin. No `target_env`/`target_os` condition remains in PP, FK or RE.
- **u1 is unconditional:** `ORDINARY_PINNED_TARGET` is removed and the assertion runs on every target (`PP/src/retained_wire_tests.rs:69`).
- **m08 uses `norm2`** (`PP/tests/preview_physics_runtime.rs:281`), still asserted exactly equal (see N-1 on the file's header).
- **The ring check is tightened as RV125 A1-N1 asked** (`PP/src/retained_memory_law_tests.rs:136-155`): the absolute 1e-14 escape now applies only to nonzero coordinates below 1e-14, which must be exactly three (N8's x, N16's y, N24's x); every other coordinate, N0's exact 0 included, must be within one ulp. `tests/common/b1_sq_inputs.rs`'s transcribed table is identical to `law_tests`'.
- **glibc:** dispatch 37820998162 on `7bd84e0526`, whose 21 files equal `8dd64c1835`'s (I diffed each), **completed with success**, including the numerical cargo suite (read with `gh run view`). That is the first glibc run of u1's unconditional pin, the single W-C2 fixture, the single SF-2 pin, m08 with `norm2` and the tightened ring.

## 4. Scope truthfulness (the commit message, the comments and the package)

- **True and supported:** the norm's operations, the oracle counts, "one value moves by one ulp" among committed pins, the re-pin list, the retired variants, the Mac-side passes of `t13` and the runner's `load_reference` tests (CHANGE_RECORD §1 lists their outputs as moves to the committed Linux bytes; I confirm each "after" is RN3 and each "before" is this Mac's libm), the D1 site list, and the "not in scope" libm list (sin, cos, atan2, asin, exp, exp_m1) with CHANGE_RECORD §2's "still platform-dependent" table.
- **Overclaims:** S-1 (every published 3-component magnitude), N-3 (the 30 counted as reaching published bytes), N-5 (the rank screen as only an admission decision), N-6 (the readers).
- **Stale evidence status:** N-7 (37820998162 is now a success).
- **Citations:** I did not re-run `check_citations.py`/`source_equality.py`; WORKING_ITEMS reports both pass on the PR head. The package's cited records (`R/I109/pr_n_package_01/`) are present at NUM `bfeebe520c`.

## 5. My spot checks (archive copy `A`, fresh targets `WT/targets/rv126-*`, every cargo through `t3_cargo.sh`)

| Check | Result |
|---|---|
| PP suite (`cargo test`, all targets) | **743 passed, 0 failed, 79 ignored** (as I109's) |
| RE suite | **199 passed, 0 failed** |
| FK: lib, `correct_norm_oracle`, `k5_constrained_bodies` | **499 passed, 0 failed, 2 ignored** (the oracle dump, and KF2's release-only cost test) |
| PY readers that read the corpus (`test_retained_precision_contract.py`, `test_retained_precision_schema.py`) | **1,079 passed, 0 failed** (with binaries built from `A`) |
| TS readers that read the corpus (`retainedPrecision.test.ts`, `retainedPrecisionIntegration.test.tsx`, `retainedPrecisionResultExport.test.tsx`, `retainedPrecisionStressNeutral.test.tsx`) | **4 files, 1,314 passed, 0 failed** (wasm engine built from `A`) |

`E/results/crates_summary.txt` and `E/results/readers_summary.txt` hold the result lines. The PY binaries were built from `A` (`checked-cli`, `cli`); the wasm engine was built as `scripts/build-wasm-engine.mjs` builds it (cargo through `t3_cargo.sh`, then `wasm-bindgen`); `node_modules` are APFS clones of an existing T3 install whose `package-lock.json` is byte-identical (nothing installed).

## 6. Host and records

- Every cargo went through `WT/tools/t3_cargo.sh` (`--locked --offline`): the three crate suites, the PY binaries, the wasm engine and the rank harness (a scratch package with a hand-written `Cargo.lock`: no registry dependencies). The single-file `rustc` builds of my norm driver (aarch64, debug and release, and wasm32) took under a second each and ran directly, not through a slot; an identical release `rustc` I had queued through `t3_slot.sh` ran later, and its outputs equal the direct build's. My Python oracle ran directly under `nice` with 4 workers (under 2 GB). Nothing was installed; no Git writes; no DEC-025, RSS or solver-at-scale job; no other job was signalled.
- The 32 MB input file is not committed: `E/results/data_sha256.txt` gives its sha256 and those of the outputs; `gen.py 1000 126` regenerates it.
- `E/tools/` holds every script and harness, with machine paths replaced by `WT`. The copies under `S` and `A` and the targets `WT/targets/rv126*` were deleted at the end of this review; `E/tools/` and `gen.py 1000 126` rebuild them for a confirmation round.

## 7. For ROOT (through WORKING_ITEMS)

1. **B-1's ruling.** Under the admission view, does a decision change confined to the rank screen's rounding-noise band (both directions, sound, already platform-dependent before PR-N), plus a witness-class change at extreme scale, count as a defect? (i) If ROOT accepts it, B-1 closes, and the package should say so with N-5; the verdict then becomes PASS with S-1 and the NOTEs, which I can confirm on the repaired text. (ii) If not, drop `d538f469af` (FK `rigid_body.rs:53`, `:109` back to `hypot`, `k5_constrained_bodies.rs`'s B10 scan back to excluding the two functions). The rest of PR-N stands either way.
2. **S-1's commit message:** whether a recut is wanted for one sentence, or the package's correction suffices.
3. **Forward (not PR-N):** the rank screen's band is wide in absolute terms (σ_min within ~0.15 % of τ). If a deterministic decision at the band's edge matters for admission, that is a property of the screen's design (K5's screen uses a power-of-two L and the same τ), not of the norm.
