# RV129: T3's review of T4-I9's arc load-vector certificate (T4-U1b)

**Who and when:** RV129, independent reviewer (Type 2), fresh instance, for T3's WORKING_ITEMS (Agent 1), the return path. 2026-10-09 UTC. No delegation.

**Brief:** `R/BRIEFS/RV129_T4_I9_CERTIFICATE.md`, sha256 `902dd36b…0079626` (verified; NUM `6784c7df12`), with `R/BRIEFS/B1_COMMON.md`'s host and records rules (WORKING_ITEMS in ROOT's place).

**Placeholders:** `WT`, `NUM` (= `WT/numerics`), `P` (= `projects/chirality-piping`), `T`, `R`, `RR` as in the brief. `R4` = `P/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/PRESSURE_STRESS_T4`. `FK` = `P/core/solver/frame_kernel`, `CB` = `P/core/solver/curved_bend`, `PP` = `P/core/product_physics`. Code citations are `path:line@ed012c7ccf` unless marked.

**What was reviewed (all hashes verified):**
- the design at `471ad93f48`: `R4/T4-I9/DESIGN.md` `8b90584f…dabdef9cb4`, `RETURN.md` `e032a78b…`, `_run_records/` (probe `2be57421…`, its stdout `2b37182f…`, `opcount.py` `ded4b61a…`, its stdout `668f0b5f…`); `SHA256SUMS` `b196aad2…` re-verifies 6/6;
- the code basis `ed012c7ccf` and `b2` `e582b61f9e` (read with `git show`/`git archive` into `WT/scratch/rv129/`);
- T3's authority: RR "S11-G after V1's S11G_CHECK" (item 3, SF-2), "S11-G note revision 2: rulings…", "S11-G revision 2 after V1's delta check", "Selection: the S11-G design", "K3a arctangent…", "K1: the S11 site table…", "T4 plan 01's annex A: T3's agreement recorded…", and `R/I115/t4_annex_check_01/RETURN.md`;
- T4's rulings: `R4/T4_RULINGS.md@1b682630e4`, sections "T4-U1b's certificate design (T4-I9)…" and "Very small realized bends…" (the latter is later than the design).

T4's worktree (`WT/t4`) was not touched. No Git write anywhere. No cargo.

## Verdict: PASS WITH AMENDMENTS

The enclosure proof holds, and so does the SF-2 reading. Every probe claim I re-ran reproduces, and an independent reference (different method, 55 new cases) finds every reference vector inside its ball. One BLOCKING finding concerns the interface, not the mathematics: the proposed `Formation::Certified` variant changes a priced layout. The design's own alternative (O-2) removes it. With amendments A-1 to A-6 below, R-1's three conditions are met.

| Condition (T4_RULINGS, R-1) | Finding |
|---|---|
| **(a)** the enclosure proof (L0–L7, Theorem 1) and the SF-2 reading | **Hold.** L0–L7, Theorems 1 and 2, Lemma 3 and (I1)–(I4) were re-derived line by line, with no gap in the real-number proof. Amendment A-2 is required before code: the binary64 evaluation of the radii must round the denominators down, which the design's "facts" do not provide. That is a specification omission, not a proof gap. R-SF2 is the right reading of SF-2 (§3). |
| **(b)** every failed precondition falls back to `CannotBound`, with a test | **Holds by construction, test plan incomplete.** Every precondition returns `Err`, and the PP hunk maps every `Err` to today's 12 `CannotBound` pushes. Only 3 of the 9 precondition classes have a planned test, and the natural candidate k = 1e40 probably never reaches the certificate. Amendments A-3 and A-4 (§4, §5). |
| **(c)** T15's new meaning | **Right,** with a non-vacuous precondition. T15c needs a different natural candidate (k ∈ [6e35, 1e39], not 1e40). Without an ordinary-Passed model, T15c can stay natural at guard level: no seam is needed for the mutant kills, and only the end-to-end envelope sentence is lost (R-2, for HELP_HUMAN). T15d's premise is overtaken by the later small-bend ruling (A-5). |

## Findings

### BLOCKING

**B-1. `Formation::Certified` changes a priced layout. The design's claim "Formation's size does not grow" (§4) is false. Resolved by A-1.**
- **Measured.** The variant set copied from `FK/src/load_ledger.rs:84-97`, compiled with the host's rustc 1.97.1 for aarch64-apple-darwin, which is the toolchain of `PINNED_RECORD_IDENTITY` (`PP/src/retained_memory_law_tests.rs:1196`) (`_run_records/tools/layout.rs`, `layout.stdout.txt`):
  - `Formation` is 32 B today and 40 B with `Certified { intended: Vec<f64>, radius: f64 }`;
  - `Option<FormationRecord>` grows from 48 B to 56 B.
  - **Why.** There are now two 32-byte dataful variants, so the tag can no longer sit in `Exact`'s `Vec` niche.
- **Priced.** `FORMATION = size_of::<Formation>()` is exported at `FK/src/structural/retained_resource.rs:78`. It feeds the atom `s(Option<FormationRecord>)` (`PP/src/retained_memory.rs:1760`, atom 131), which rises from 56 to 64 B.
  - The atom is used with coefficient 1,920 in `O_base_dense` and `O_base_sparse` (`:2140-2141`), and with 256 and 128 in `T25_S1` and `T25_S2` (`:2172-2173`).
  - So the phase bytes move, and `PINNED_RECORD` with them (`retained_memory_law_tests.rs:1192`). Pass B stops on the entry or law (exit 3).
  - This breaks T3's priced-layout constraint (T4_RULINGS, "T3 agrees annex A…", claims 2 and 3).
- **A-1.** Use the design's own alternative (O-2): `Formation::Exact { scale: 1.0, scaled_intended: split(m) }`, with `operand_bound` equal to r, plus γ₅·(|m|↑ + r) for generated loads, summed upward.
  - `add_defect` treats the two forms identically. Both add `operand_bound` to B first (`load_ledger.rs:573-575`), then 12·v − 12·Σt into A_net and 12·Σt into the intended net (`:577-602`).
  - No FK type changes, and `load_ledger.rs` needs at most a comment saying that a certified `scaled_intended` sums to the ball midpoint, with the radius in `operand_bound`.

### SHOULD-FIX

**S-1 (A-2). The radius arithmetic needs directed rounding on both sides.** The lemmas are stated over the reals, and they are correct. The design says only that the radii use upward operations and |m|↑ (§3.1). An implementation that follows that literally can under-bound.
- **Denominators need lower bounds:**
  - L3's |m_b| − r_b, which must be computed as |m_b|↓ minus r_b, rounded down;
  - L4's m;
  - L5's 1 − 21.54u;
  - L7's 1 − ρ.

  For example, `quotient_upward(num, abs_up(m_b) − r_b)` is unsound by up to one ulp. A lower bound is free: `split_binary64` truncates toward zero (`FK/src/structural/retained/wide.rs:409-452`), so |m|↓ = |t₀|.
- **Constants round up.** 21.55 is not a binary64 value. (1 + u) at u = 2⁻¹²⁸ rounds to 1 in binary64, so use next_up(1) or a separate u·term. |m_a/m_b|↑ can be `product_upward(|m|↑, 1 + 2⁻⁵²)`.
- **`sum_upward` cannot use "the same fma pattern"** (§3.1), because an fma gives a product's error, not a sum's. Use TwoSum, or an `ExactAccumulator` with `round_upward`, which S11-G already uses for B (`load_ledger.rs:729`).
- **The subnormal edge.** `product_upward` and the new `quotient_upward` decide by the sign of an fma remainder. In the subnormal range that remainder can round to 0, which leaves a result below the exact one by less than 2⁻¹⁰⁷⁴. Add 2⁻¹⁰⁷⁴ when |a·b| < 2⁻⁹⁶⁹ (`FMA_EXACT_PRODUCT_MIN`, `load_ledger.rs:558`), on the D21-2 precedent.
- **Tests.** Extend MU6 with downward-denominator mutants, killed by L3, L4 and L7 unit tests.

**S-2 (A-3). Condition (b)'s tests cover 3 of 9 precondition classes.** V2 lists three refusals: a divisor ball containing 0, a square-root ball reaching 0, and ρ ≥ 1/2. The table in §4 lists every class. These need tests:
- FK unit tests:
  - L5's atan domain;
  - a failed Gauss–Jordan for X̃ (`DivisionByZero` on a singular midpoint matrix);
  - a `WideError` mapped to `Err` (for example, a non-finite lift);
  - a non-finite radius;
  - `SplitOverflow` on an output, and the truncated split adding 2⁻¹⁰⁷⁴.
- **A ρ ∈ [1/2, 1) case,** to kill MU4's "threshold raised to 1" form. On the probe's L line, ρ ≈ 1.19e-36·k (measured: ρ = 0.118 at k = 1e35 and 1.19 at k = 1e36), so k ≈ 6e35 gives ρ ≈ 0.7. A case with ρ ≥ 1 does not kill that form.

**S-3 (A-4). T15c's natural candidate.**
- **k = 1e40 probably never reaches the certificate.** At k = 1e40, my binary64 Gaussian-elimination emulation of the flexibility inverse meets an exact zero pivot. The product's CB call (`invert_symmetric6` → `solve_dense`) then likely errs, which is today's blocking `LOAD_INPUT_INVALID` diagnostic, not the `CannotBound` path. Its actual behaviour must be checked; the emulation is not `solve_dense`.
- **The natural refusal window** on the L line is k ∈ [1e36, 1e39]: ρ = 1.19, 12.1 and 87.5 at k = 1e36, 1e37 and 1e38 (`rv129_ref_extra.stdout.txt`).
- **The product's element is meaningless there.** The binary64 inverse of F has a relative entry error of 1.0, and the vector's defect against my reference is 2.9e14 to 1.3e15 of max|f|.
- **So an ordinary report of `quality: Passed` there would itself be a K-D5 miss.** By construction the certificate (p = 128 with a verified inverse) fails only where binary64 is hopeless, so no natural model is expected to give an ordinary Passed report with a refused certificate.
- **The recommendation** is in §5.

**S-4 (A-5). T15d and MU2's natural kill are overtaken by the later small-bend ruling.**
- T4_RULINGS "Very small realized bends…" (`1b682630e4`, after the design) puts a stable small-angle binary64 form into T4-U1, or into T4-U1c before T4-U2.
- T15d's premise is that the binary64 element loses 4 to 5 digits at 0.1° (1.7–37×). That premise ends with the stable form.
- T15d and MU2's natural kill must be re-derived on T4-U1's element. Two candidates:
  - **Large k.** The binary64 inverse already loses digits at k = 1e11: an entry error of 1.8e-6 and a vector defect of 1.3e-5, while the certificate's radius is 5.7e-14. K-D5 may demote first, in which case the assertion is made at guard level.
  - **V3's unit control** (+2·T0) together with a guard-level natural catch.

**S-5 (A-6). L5's Lipschitz constant of 1 causes false demotions near π.** It is sound, but too loose for large t = s/c_h.
- **Measured** on skew-chord arcs whose 1 − s² is 7e-18 and 1e-19 (`rv129_near_pi.stdout.txt`):

  | Arc | rad/max\|f\| with the design's L5 | with a sharpened L5 |
  |---|---|---|
  | π − 5.3e-9 | 6.9e-9: B ≥ T0, so the row fires falsely | 1.9e-25 |
  | π − 6.5e-10 | 3.7e-6 | 1.6e-24 |

  The first arc is inside CB's window, which ends at π − 1e-9. Both forms enclose.
- **The fix is still rigorous:** r = r_t/(1 + (m_t − r_t)²)↓ + 21.55u·m. atan′ decreases on [0, ∞), and m_t − r_t > 0 is already L5's precondition. Alternatively, use φ = π − 2·atan(c_h/s) for t > 1, with π a pinned ball.
- **Why it matters:** it helps meet T4_RULINGS' acceptance ("the guard … met with margin … up to π − ε"). It costs availability only, never soundness.

### NOTE

- **N-1. The proof is verified** (§1). The subtle points:
  - |rnd z − z| ≤ u·min(|z|, |rnd z|) at p = 128; both forms are used, in L1–L3 and in L4;
  - L7's bound on entries from the ∞-norm;
  - L5 rests on K3a's atan_positive bound, (1.54 + 4k)u ≤ 21.54u relative. It is a corollary of the proof ROOT accepted ("K3a arctangent"), which I re-checked: Lemma A, the β₄ reduction step, and at most 5 reductions for every t > 0;
  - `split_binary64` truncates toward zero, so |m|↑ = next_up(|t₀|) is an upper bound.
- **N-2.** The 253 committed `atanpos` vectors are asserted only against the included angle's 23.6-ulp bound (`FK/tests/retained_wide/wide_tests.rs:1049`), while L5 cites 21.54u relative. Either add that assertion when atan_positive gains its first product caller, or cite a constant the tests assert.
- **N-3. f is T4-U1's objective element.** T4-U1 must implement exactly (F1)–(F7), or re-prove (I1)–(I4) for its definition. The proposed `CurvedFormation` change is an edit to K-D5's `formation_check.rs` inside T4-U1, covered by annex A's items 1 and 2. It is not part of T4-U1b, whose constraint leaves `formation_check.rs` unchanged.
- **N-4. Large k stays sound, but the radii grow.** L7's ∞-norm entry bound inflates the radii for a graded F:

  | k | rad/max\|f\| | Result |
  |---|---|---|
  | ≤ 1e4 (realistic) | ≤ 6e-28 | passes |
  | 1e8 | 5.7e-20 | passes |
  | 1e11 | 5.7e-14 | passes |
  | 1e15 | 5.7e-6 | fires, by B ≥ T0 |

  Where it fires, the binary64 element is itself wrong (defect 0.12 at k = 1e15). These are true catches, recorded as formation defects rather than as `CannotBound`.
- **N-5. Small φ.** rad/max|f| is:

  | φ | rad/max\|f\| |
  |---|---|
  | 1e-4 rad | 3.9e-20 |
  | 1e-6 rad | 3.9e-12 |
  | 1e-7 rad | 3.9e-8 |
  | 1.01e-9 rad (CB's floor) | 3.7 |

  Below about 1e-7 rad the certificate itself demotes, by B. This is outside T4's acceptance range, which starts at 1e-4 rad.
- **N-6. The mechanics transcription is confirmed by an independent derivation.** The probe's own 70-digit evaluation of (F1)–(F7) agrees with my Gauss–Legendre force method in global coordinates to 5e-33 to 8e-70 relative, over the 51 certified cases of the two sets.
- **N-6a. V2's frozen reference should not share the certificate's closed form.** Otherwise a transcription error common to both could pass. A quadrature force method in global coordinates, like `rv129_ref.py`, is one such method.
- **N-6b. The formula-chord mutant is equivalent for soundness.** The design (§6) leaves it unlisted: H built from (I4)'s formula chord R(C − 1, S, 0) instead of the actual chord. I re-derived (I4) independently, so both expressions are the same real number and the ball still encloses f; only the radius differs. This concerns the certificate only. It is not K-D5's M31b, which concerns the product's binary64 element.
- **N-7. T4-U2's terms** (O-5, O-6) are sketched, not specified. R-1 as reviewed here covers the uniform-load vector. The bend-pressure identity's ε_p ball and the caps' P and tangent formulas need their own statement and a T3 check at T4-U2's design.
- **N-8. An admissibility edge, which fails closed.** PP accepts a bend when the binary64 half-chord is below R (`PP/src/lib.rs:7783`). If the exact L/2 is at least R, the certificate's 1 − s² ball fails, giving `CannotBound`. After T4-U1, K-D5 holds the same operands and refuses as well. Nothing passes; this is noted for T4-U1's admissibility.

## 1. The proof (check 1)

All re-derived independently. "OK" means verified as stated.

- **Rounding facts.**
  - `Wide<2>` at p = 128 has a normalized 128-bit significand and rounds to nearest, ties to even, once per operation, with no subnormals; an exponent out of range is an error (`wide.rs:9-33`). K-D5 uses p = 128 (`FC:38-39`).
  - For z ≠ 0 with 2^e ≤ |z|: |rnd z − z| ≤ ½ulp(z) = 2^(e−128). That is at most u|z|, and also at most u|rnd z|, since |rnd z| ≥ 2^e by monotone rounding. OK.
- **L0** (`from_f64` is exact, `wide.rs:314-334`): OK.
- **L1:** OK.
- **L2:** OK; the identity is exact.
- **L3:** x/y − m_a/m_b = [(x − m_a)m_b − m_a(y − m_b)]/(y·m_b). Dividing by |m_b| gives (r_a + |m_a/m_b|r_b)/|y|, with |y| ≥ |m_b| − r_b > 0. OK; for the binary64 evaluation see A-2.
- **L4:** |√x − √m_a| ≤ r_a/√m_a, and √m_a ≥ m/(1 + u) because |m − √m_a| ≤ u√m_a. The precondition gives x > 0. OK.
- **L5:** |atan x − atan m_t| ≤ r_t, and |m − atan m_t| ≤ 21.54u·atan m_t ≤ 21.54u·m/(1 − 21.54u) < 21.55u·m. OK; see N-1 for the K3a bound and S-5 for sharpness.
- **L6:** OK (`mul_pow2`, `wide.rs:372-378`). The radius must round up on underflow.
- **L7:** R_F = I − F·X̃, and the ball residual encloses it for every F in the entrywise ball. So ‖R_F‖∞ ≤ ρ < 1/2 < 1, F is invertible, F⁻¹ = X̃(I − R_F)⁻¹, and F⁻¹ − X̃ = X̃R_F(I − R_F)⁻¹, whose norm is at most ‖X̃‖∞ρ/(1 − ρ). An entry is bounded by the ∞-norm. Soundness does not depend on how X̃ is computed. OK.
- **Theorem 1:** the induction invariant is preserved by each lemma for every real input in its balls. Two remarks:
  - The dependency between entries (the inverse used as independent balls) is valid, if pessimistic.
  - The evaluated expression equals (F1)–(F7) term by term.

  OK.
- **(I1)–(I4)** for 0 < s < 1, with φ/2 = asin s ∈ (0, π/2):
  - c_h = cos(φ/2) > 0, and atan(s/c_h) = φ/2;
  - S = sin φ, C = cos φ, S₂ = sin 2φ, C₂ = cos 2φ;
  - r_i = R(−s d̂ + c_h n̂) and r_j = R(s d̂ + c_h n̂);
  - r_i × r_j = −2s c_h R²(d̂ × n̂) = R²S(n̂ × d̂), so e_z = n̂ × d̂;
  - e_y = (n̂ × d̂) × e_x = c_h d̂ + s n̂ = t_i;
  - c = (−2Rs², 2Rs c_h, 0) = R(C − 1, S, 0). This matches PP's bow convention (`PP/src/lib.rs:7760-7846`) and CB's frame (`CB/src/lib.rs:150-179`).

  OK.
- **Output split:** the terms sum exactly, or a truncation below 2⁻¹⁰⁷⁴ is added to r. OK.
- **Theorem 2:** no fire means not (B > 0 and B ≥ T0) and |A_net| + 12B − 12T0 ≤ 0, decided exactly (`formation_guard.rs:182-201`, `:216-250`). So |Σ_net(v − f)| ≤ |A_net|/12 + B ≤ T0. OK.
- **Lemma 3.** For every row, |n′ − n| ≤ B: Exact and unscaled RoundedProduct are exact, while Bounded, Certified and the operand bounds are in B. No fire gives B ≤ c·max(|n′|, S\*′). For a free force row, |n′_i| ≤ |n_i| + c·fo′, so F′ ≤ F + c·fo′; likewise M′ ≤ M + c·mo′.
  - With mo′ = L_b·fo′ in exact arithmetic, fo′ ≤ fo + c·fo′ and mo′ ≤ mo + c·mo′.
  - The directed roundings in `coupled` only lower T0.
  - So the effective criterion is c/(1 − c). OK, and pre-existing for Bounded.
- **The generated-load bound γ₅(|m|↑ + r).** f is linear in the single intensity component and the intensity is w(1 + θ) with |θ| ≤ γ₄, so |f(w̃) − f(w)| ≤ |f(w̃)|γ₄/(1 − γ₄). Since 4u/(1 − 8u) ≤ γ₅ for 20u ≤ 1, the bound holds. OK.
- **Re-checked numerically** (`rv129_lemmas.stdout.txt`):
  - L1–L4 as the probe implements them: 156,000 exact-rational checks at ball endpoints and interior points, 0 outside;
  - L7: 4,320 entry checks on random members of 40 ill-scaled ball matrices, 0 outside.

## 2. The probe and the independent reference (check 2)

**Re-runs, standard-library Python 3.13.14 with `-I`:**
- `opcount.py`'s stdout is **byte-identical** to the recorded one (`opcount.rerun.stdout.txt`): 4,666 ball operations and 5,023 rounded midpoint operations.
- `arc_cert_probe.py` was queued under `WT/tools/t3_slot.sh` behind #1168's exclusive DEC-025. Its result is recorded in `probe.rerun.result.txt` and in §2.1.

**The independent reference** (`_run_records/tools/rv129_ref.py`).
- **Precision:** Decimal at 120 digits, cross-checked at 140 digits with more nodes; the cross-check difference is at most 4e-86 times the largest ball radius.
- **A different method from the probe's:**
  - its own π (Machin), sin and cos (quadrant reduction and Taylor) and half angle (Newton on sin or cos), not the probe's atan series;
  - the frame from CB's centre-based construction, not the (s, c_h, d̂, n̂) formulas;
  - unit loads along the six **global** axes, with internal actions formed from 3D vectors at each section;
  - the distributed load's section moment as an inner Gauss–Legendre integral;
  - flexibility and tip deflection by 56×56-node Gauss–Legendre quadrature, not closed-form Gram entries;
  - F⁻¹ by Decimal elimination, and the node-i share from global rigid equilibrium.
- **The certificate under test** is the design's own ball evaluation (`formula(BallCtx(), …)`), checked exactly with Fractions.

**Cases the probe did not choose (`rv129_ref.stdout.txt`, 39 cases):**
- φ = 30°, 60°, 120°, 150°, 170°, 179°, 179.9°, π − 1e-6 rad and π − 1e-8 rad (the last is coordinate-limited, so it is about π − 9e-8);
- φ = 0.5°, 0.05°, 1e-4 rad and 1e-6 rad;
- skew planes at UTM (7.3e6, 4.6e6, 312.8) at 45°, 7°, 0.2° and 178°, and at (5e5, 6e6, −12);
- k = 1e-3, 30, 1e4, 1e8, 1e15 and 1e20, and k_in = 3 with k_out = 0.5;
- R = 0.05 m with a 21.3 mm bar; R = 25 m with a 1,219 mm × 6.35 mm pipe, at 20° and at 0.3° at UTM;
- aluminium; G ≪ E; w = 1e9 and 1e-6; a three-component w;
- six random arcs with full-mantissa inputs.

**Results:**
- **Certified 39 of 39, enclosed 39 of 39.** The worst |ref − m|/r is 0.138 (R = 25 m, 0.3°, UTM); typical values are 1e-4 to 1e-20.
- **The extra set** (`rv129_ref_extra.stdout.txt`, 16 cases: k = 1e11 to 1e40, φ near π, φ down to 1.01e-9 rad):
  - every certified case is enclosed, 12 of 12;
  - k = 1e36, 1e37, 1e38 and 1e40 are refused (ρ = 1.19, 12.1, 87.5 and 762).
- **Near π** (`rv129_near_pi.stdout.txt`): 4 of 4 enclosed, with both L5 forms (S-5).
- **Total:** 55 new certified cases, 0 enclosure failures.

### 2.1 Probe re-run versus the recorded stdout

See `probe.rerun.result.txt`. The probe is deterministic (Fractions and Decimal), so a byte comparison is expected to match. If the slot did not start within this review's window, that file says so.

## 3. SF-2 (O-1)

**R-SF2 is the right reading of RR "S11-G after V1's S11G_CHECK", item 3, and a stricter one.**
- **What SF-2 demanded.** The curved fallback bound had to be "genuinely conservative", accounting for cond(F), cancellation and libm, or be routed to "cannot bound".
- **What it guarded against.** The stated-bound fallback it addressed would have been an a-priori bound, which is only conservative if it assumes nothing about conditioning, cancellation or libm accuracy.
- **Why the design meets it.** Its bound is a-posteriori: |v − m| is computed exactly, and r is a proved enclosure of the certificate's own error.
  - The product's libm, conditioning and cancellation are all inside |v − m|, measured with no assumption.
  - The certificate's own transcendental is K3a's integer-only atan, with a proved bound.
  - Its own conditioning is verified by the residual condition ρ < 1/2.
- **libm is acceptable** where its effect on v is measured exactly and nothing relies on its accuracy: that meets "including … libm" in the strongest sense.
- R-SF2's (c), (d) and (e) match RR's rulings: fail-closed, SF-1's exact defect, and DB-1 (a net defect is never floored).

## 4. Fail-closed (condition b)

Every row of this table is mapped to `Err(ArcCertificateFailure)`. At `PP/src/lib.rs:10576-10593`, the design's PP hunk turns any `Err` into today's 12 `Formation::CannotBound` pushes, with today's reason (`formation_guard.rs:233-237`). The certificate returns all 12 components or `Err`, so no partial record is possible.

| # | Precondition | Where it fails | Planned test | Needed |
|---|---|---|---|---|
| 1 | 0 < L < 2R and n ≠ 0 | PP refuses first (blocking, `lib.rs:7783-7794`, `:7830-7837`); the exact edge is in rows 2–3 (N-8) | existing PP diagnostics | — |
| 2 | L3: divisor ball excludes 0 (L/2R, d/L, n/\|n\|, s/c_h, /EI, /GJ, /EA) | FK → `Err` | V2 unit | — |
| 3 | L4: sqrt argument ball positive (d·d, 1 − s², n·n) | FK → `Err` | V2 unit | — |
| 4 | L5: atan argument ball positive | FK → `Err` | none | **unit (A-3)** |
| 5 | L7: ρ < 1/2 | FK → `Err` | V2 unit; T15c | natural k ∈ [1e36, 1e39]; **ρ ∈ [1/2, 1) case for MU4 (A-3)** |
| 6 | X̃ Gauss–Jordan completes (nonzero pivots) | `WideError::DivisionByZero` → `Err` | none | **unit (A-3)** |
| 7 | every Wide operation succeeds (`ExponentRange`, `NonFinite`, `AngleDomain`, `ArctangentLimit`, …) | `WideError` → `Err` | none | **one mapping test (A-3)** |
| 8 | every radius finite (including \|m\|↑ needing a split) | FK → `Err` | none | **unit (A-3)** |
| 9 | output split: `SplitOverflow` fails; truncation adds 2⁻¹⁰⁷⁴ | FK → `Err` / radius | none | **unit (A-3)** |
| 10 | PP: `Err` → the 12 `CannotBound` pushes | PP call site | T15c; MU8; T8 token | natural, per §5 |
| 11 | generated-load operand bound finite | ledger range failure, so the row fires (`load_ledger.rs:573-575`) | MU9 unit pin | — |
| 12 | v finite | ledger range failure (`load_ledger.rs:592-594`) | existing | — |

## 5. T15, T15c and M16 (condition c; O-7; R-2)

- **T15's new meaning is right.** Certified arc load terms publish `CHECKS_PASSED`, on both entries and in both modes. The test must also:
  - assert non-vacuity: every arc DOF row carries the certificate's record (per A-1, an `Exact` record with the arc load's id in `formed_sources`) and no `cannot_bound_sources`, and the certificate returned `Ok`;
  - compute the exact row statistic in the test and assert it is below 1.

  "Today's rule would demote" cannot be shown without a seam. The formed-source precondition is the non-vacuity that matters.
- **O-7: a natural certificate failure exists** (k ∈ [1e36, 1e39], S-3), but not one with an ordinary Passed report, unless K-D5 misses a meaningless element. Recommendation:
  1. At implementation, run T15c with k ∈ {6e35, 1e36, 1e37, 1e38}, and record the ordinary verdict and `solve_dense`'s behaviour at 1e40.
  2. **If any case gives an ordinary Passed report,** use it for the full envelope assertions. Report it to T3 as a possible K-D5 miss.
  3. **Otherwise, keep T15c natural at guard level, with no seam.** Build `guard_view` through the product's own ledger builder (`case_force_ledger` → `add_uniform_element_loads`; `s11g_tests.rs:220-279`), then assert that:
     - the arc rows carry `cannot_bound_sources` with the arc load's id;
     - `decide_row` fires with the `CannotBound` reason;
     - the envelope is Sensitive by whatever path.

     This kills M16 (`CannotBound` treated as a zero defect), MU8 (the fallback removed) and MU3/MU4 (with the 6e35 case).
  4. **What is lost:** only the end-to-end assertion that the envelope message carries the `CannotBound` sentence, because `demote` is a no-op on a report that is already Sensitive (`formation_guard.rs:481-489`). That loss is R-2's narrowing. It goes to HELP_HUMAN with this evidence, and a `#[cfg(test)]` seam is needed only if HELP_HUMAN wants that sentence end to end.
- **M16's kill:** T15c, plus the `load_ledger` unit test for the `CannotBound` arm.

## 6. T3's technical questions

| ID | Recommendation | Reason |
|---|---|---|
| O-1 | **Yes** | §3 |
| O-2 | **`Exact { scale: 1.0, scaled_intended: split(m) }` with `operand_bound` = r (⊕ γ₅ term), not a new variant** | B-1: the variant grows `Formation` and moves a priced atom. The alternative is decision-identical in `add_defect`, needs no type change, and leaves `load_ledger.rs` code unedited. T8's tokens (`Formation::CannotBound` present, flags {false}) still hold. For T4-U2, MU11's token becomes the certificate call (for example `certify_bend_caps(`), not `Formation::Certified` |
| O-3 | **Accept Lemma 3 as is; do not change `CRITERION` in T4-U1b** | `formation_guard.rs` is on T3's unchanged list. The excess is 1e-9 relative of the criterion, and it is pre-existing for `Bounded`. A global constant change re-thresholds every formed row and needs its own zero-diff evidence. If T3 wants it, it is a T3 item. T4-U1b discloses c/(1 − c) in its change record |
| O-4 | **atan_positive, as its first product caller**, with N-2's test assertion, plus S-5's sharpened L5 (or the reflection) | It is a single-input lemma with a Lipschitz bound. `included_angle(S, C)` needs a two-input ball lemma whose sensitivity grows like 1/(1 + C) near π. The bound is a corollary of the accepted K3a proof. No `wide.rs` edit is needed (`pub(crate)`, reachable from `structural`'s child) |
| O-5 | **Agree in principle** | The thermal identity's convention: K̃ and the chord held, K̃'s formation K-D5's, and ε_p's ball error as an operand bound that enters B unfloored (the operand bound is added to B for self-equilibrated terms too, `load_ledger.rs:573`). The ε_p enclosure needs its own statement and check at T4-U2 (N-7) |
| O-6 | **Agree in principle** | Certifying the tangents and P is stricter than a held tangent, and the caps are net (never floored). At T4-U2: state P's formula, prove π's 128-bit ball, and apply L0–L7 |
| O-7 | **Natural first, at guard level if needed; k ∈ [6e35, 1e39], not 1e40** | §5, S-3 |
| O-8 | **Yes**, on a separate body (offset like today's `curved_body` at 100 m) with a straight UDL-W1e8-type row that S11-G catches; assertions unchanged | Today's assertions (`s11g_tests.rs:1781-1806`) check the load-row phrase and that R-b′'s sentence is absent, not "CannotBound", so they carry over. Keep the precondition that the trigger body's own row fires |
| O-9 | **In T4-U2's T8 edit** (the first time T8 is touched), with T4-U1b's change record noting the stale class text meanwhile | No token is removed, and B7 is later than needed |
| O-10 | **No re-registration expected; Pass B on the candidate decides**, with a dry TEXT check before code | At G6's rule basis, `add_uniform_element_loads` is `fn_zero` (D1.7, uniform element loads outside W1), and curved loops are zero by regex rules (D1.4/D1.8) (`R/I65/u4_g6_01/_run_records/loop_bounds.g4.json`, `fn_zero[19]`, `loops[214]`, `loops[217]`). The certificate is called only beneath both, so FORMS should be unchanged. If TEXT reports the new loops as unmapped, the fix is zero-bound mapping rules (reviewed tooling), with the entry compared byte for byte. Any change to the entry or FORMS goes to HELP_HUMAN before code (T4_RULINGS, O-10). B-1's variant would itself force Pass B's exit 3, which A-1 avoids |
| O-11 | **Agree**, on K1's five conditions | Additive rows; the ball sites dispositioned like `formation_check.rs`'s re-formation exemptions (Wide midpoints, whose rounding is covered by the proved radius, and nothing published); radius folds through helpers; a killed binary64-fold mutant (for example a `+=` fold of the split terms). Declared in the change record |
| O-12 | **Done (§1): the proof holds** | Amendment A-2 is for the binary64 radius evaluation |
| O-13 | **Route to T3 as its own item, not T4-U1b's** | With D-2, arcs are the normal bend, and formed curved end actions (K̃_c·u) have no recovery guard (S11G §4). T3 should decide on an arc analogue of R-b′ before T4-U2 makes arcs the pressure path |

## 7. T3's constraints and the distance from `b2`

| Constraint | With A-1 | As designed |
|---|---|---|
| `preview_physics::LIMITATIONS` | unchanged; no string mentions this (`preview_physics.rs:73-81`) | same |
| Reviewed inputs (`build_identity.rs:148-163`) | none edited | same |
| PP `Cargo.lock` | unchanged (FK is already a path dependency; no new crate) | same |
| Priced layouts | `RecoveryRecord`, `MemberRecord` and `Preview*` untouched; **`Formation` byte-identical** | **broken** by `Formation::Certified` (B-1) |
| `retained_product.rs` | untouched | same |
| `tests/s11f_site_test.rs` | untouched; T8 (`:1343-1383`), PRODUCERS (`:215-223`) and rule 8's count 0 for the function hold, provided the hunk adds no `+=`, sum or fold | same |
| `formation_guard.rs` | untouched, **provided O-3 is not adopted** | same |
| K-D5's `formation_check.rs` | untouched by T4-U1b (the `CurvedFormation` change is T4-U1's, N-3) | same |
| SA, CB | untouched | same |

**Distance from `b2`** (`e582b61f9e` against its base, main `ec5d397359`):
- **PP `lib.rs`.** `b2`'s 13 hunks end at main line about 3,458. T4-U1b's hunk is the curved branch of `add_uniform_element_loads`, at main lines about 10,650–10,675 (`ed012c7ccf` 10,576–10,593). The distance is about 7,200 lines.
- **FK `structural.rs`.** `b2` edits lines 28–47, inside `retained_api`. T4-U1b's `mod arc_certificate;` beside lines 4–5 is 23 lines above that. A `pub use arc_certificate::…` beside `pub use formation_check::{` (line 62) is about 15 lines below. Keep both outside 28–47.
- **Untouched by `b2`:** FK `load_ledger.rs`, PP `s11g_tests.rs` and FK `tests/s11_site_table.rs`. `b2`'s edits to `retained_memory.rs` and `s11f_site_test.rs` are not in T4-U1b's set with A-1. As designed, B-1 would force a re-pin in `b2`'s memory files.

## 8. Evidence and host notes

`_run_records/`:
- `tools/rv129_ref.py`: the independent reference and the enclosure test. Modes: default, `--extra`, `--quick`.
- `tools/rv129_near_pi.py`: S-5's radius growth near π, with both L5 forms.
- `tools/rv129_lemmas.py`: the adversarial L1–L4 and L7 checks.
- `tools/layout.rs`: B-1's layout measurement.
- Outputs:
  - `rv129_ref.stdout.txt` and `rv129_ref_extra.stdout.txt`;
  - `rv129_near_pi.stdout.txt` and `rv129_lemmas.stdout.txt`;
  - `layout.stdout.txt`;
  - `opcount.rerun.stdout.txt`;
  - `probe.rerun.result.txt`, and `probe.rerun.stdout.txt` if the run completed.

**Commands** (from `WT/scratch/rv129/run/`; `D` = the extracted `R4/T4-I9/_run_records`):
- `WT/venv/bin/python -I tools/rv129_ref.py D/arc_cert_probe.py [--extra]`
- `… tools/rv129_near_pi.py D/arc_cert_probe.py tools/rv129_ref.py`
- `… tools/rv129_lemmas.py D/arc_cert_probe.py`
- `… D/opcount.py D/arc_cert_probe.py`
- `rustc --edition 2021 -O tools/layout.rs`, a standalone 30-line program in scratch with no crate, cargo or dependency, using `TMPDIR` in scratch
- the probe through `WT/tools/t3_slot.sh`

**Host notes.**
- My own scripts are light: about 30 s of CPU in total, single-threaded, a few MB of memory. They ran directly while #1168's DEC-025 held the exclusive slot. Only the probe was queued through the slot.
- No installs. No other job signalled.
- Scratch is `WT/scratch/rv129/`.
- No Git writes. WORKING_ITEMS commits these records.

**Wider consultation:** none beyond the brief's sources and the code cited.
