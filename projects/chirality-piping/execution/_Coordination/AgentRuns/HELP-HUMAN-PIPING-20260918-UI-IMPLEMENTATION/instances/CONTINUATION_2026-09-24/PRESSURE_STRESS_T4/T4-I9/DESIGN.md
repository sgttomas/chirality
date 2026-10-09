# T4-U1b: the certificate for load vectors on arcs (design for T3's agreement)

**Who and when:** T4-I9, TASK (Type 2), for T4's WORKING_ITEMS, to be agreed with T3's WORKING_ITEMS and its reviewer. 2026-10-09 UTC.

**Brief:** `R4/BRIEFS/T4-I9_U1B_CERTIFICATE_DESIGN.md` (`6a15cd3c…`) and `R4/BRIEFS/T4_WI_COMMON.md` (`7d44afd0…`), plus T3's five added constraints, relayed by T4's WORKING_ITEMS during the work. Status: a design. No product code was written or built.

**Basis:**
- **Code:** T3's U3 head `ed012c7ccf`. Citations are `path:line@ed012c7ccf` unless marked otherwise.
- **T4-U1:** its objective element (plan §3.1; I2 §1.6), which is not yet written. §2 states what T4-U1b needs from it.
- **T3's records:** RR and `S11G_GUARD.md` (revision 2.2, sha256 `afe5f256…`), read from T3's branch at `3743b79291`. Its S11-G and K-D5 entries are as at `70aa51b076`.

**Evidence:** an emulation in standard-library Python, `_run_records/arc_cert_probe.py`, with its stdout. It is evidence about arithmetic only, not about what the product publishes (RR, "K2a product reach: correction", lesson 3).

**Facts and inference:** facts carry citations. Inferences and proposals are marked.

## 0. Summary

1. **The method.** For each uniform load on a realized arc, the product's binary64 consistent vector `v` is compared exactly with a re-formation of T4-U1's objective element.
   - The re-formation runs in midpoint–radius ("ball") arithmetic: `Wide<2>` midpoints at p = 128, which is K-D5's precision (FC:38-39), and binary64 radii rounded upward.
   - Each component has a midpoint `m` and a proved radius `r`, with |f − m| ≤ r, where f is the exact formula of the held operands (§3, Theorem 1).
   - The record puts `v − m` into S11-G's net accumulator, exactly, and `r` into the bound B.
   - So the bound on |v − f| is the exact difference plus the re-formation's own proved error, which is what RV1's addendum (check 1) asked for.
2. **SF-2.**
   - **cond(F):** a residual-verified inverse. The certificate fails unless ‖I − F·X̃‖∞ < 1/2.
   - **Cancellation:** ball radii are absolute. The product's own cancellation is measured exactly in `v − m`.
   - **libm:** the certificate calls no libm. Whatever libm does to `v` is measured, never assumed.
   - **Failure:** any failed precondition keeps today's `CannotBound`.
3. **The interface.** A new ledger formation, `Formation::Certified { intended, radius }`, handled exactly as `Exact` plus `Bounded`. One new FK module. One call-site hunk in PP's `add_uniform_element_loads`.
   - These stay byte-identical: no priced layout, `Cargo.lock`, `LIMITATIONS`, reviewed input, `retained_product.rs` or `tests/s11f_site_test.rs` changes.
4. **Probe.**
   - Every one of the 84 certified arc cases is enclosed. The 3 cases at k = 1e40 are refused, as designed.
   - Radii are ≤ 4.4e-29 relative for φ ≥ 1°.
   - The guard statistic with T4-U1's objective binary64 element is at most 0.30 of the threshold for φ ≥ 1°. That maximum is a bend-dominated body at UTM 7.3e6; the L line reaches 2.3e-2. For φ ≥ 5° it is at most 3e-3, at ordinary and UTM coordinates.
   - At φ = 0.1° the binary64 element itself loses about 4 to 5 digits, and the guard fires. That is a true catch (§7).
5. **For T3 and ROOT.** T15 changes meaning (§5). Replacing S11-G's selected "CannotBound for curved consistent vectors" for certified terms is marked for ROOT (RETURN, R-1).

## 1. The SF-2 reading applied (T3's constraint 1)

**Source.** SF-2 is defined in RR, "S11-G after V1's S11G_CHECK (ROOT, 2026-09-27, on `30233f93a`)", item 3: fallback bounds must be "genuinely conservative", with "the curved bound including cond(F), cancellation and libm". Otherwise the contributions are routed to "cannot bound", which demotes.

**Related entries:**
- RR, "S11-G note: rulings, conditional on V1's check", (a): the exact defect has no binary64 intermediate.
- RR, "S11-G revision 2 after V1's delta check", 1 (DB-1): a net formation defect is never floored.
- RR, "S11-G note revision 2: rulings…", 3: CannotBound is accepted because realized bends are opt-in, and "W1c with T4 removes it".
- RR, "Selection: the S11-G design": CannotBound for curved consistent vectors is a condition of selection.

**The reading applied here (R-SF2).** A formed term may carry a record other than `CannotBound` only if all of the following hold:
- **(a) The bound is rigorous.** The record gives a rigorous upper bound on |value − f(z)| for that input. Here z are the held binary64 operands, f is the documented formula evaluated in exact real arithmetic, and "rigorous" means proved, never estimated.
- **(b) Nothing is assumed.** The derivation accounts for the conditioning of the flexibility inversion, for cancellation anywhere in the evaluation, and for the accuracy of every transcendental used. None of them is assumed.
- **(c) Failure is fail-closed.** If a precondition of the derivation fails for that input at run time, the term stays `CannotBound`.
- **(d) The defect side is exact.** It reaches the decision with no binary64 intermediate.
- **(e) Arc terms are net.** Certified uniform-load and cap terms are not self-equilibrated, so the SF-4 floor never applies to them.

**libm under this reading.** The product's libm (`sin`, `cos`, `atan2`; for example CB:166, :247-248, :302-303, :316-317, :564-565, :641-642, :692-695, :766-768) is not part of the certificate. Its effect on `v` is inside the exactly computed `v − m`. T3's reviewer should confirm that this meets "including … libm".

## 2. Scope and the element re-formed (brief items 1 and 2)

| Term family | Today | T4-U1b record | Self-equilibrated |
|---|---|---|---|
| Curved uniform consistent vector: every `distributed_force` on a realized arc, including self-weight and generated equivalent-static loads (PP lib.rs:10539-10619) | `CannotBound` (lib.rs:10584-10591) | `Certified`. The generated-load operand bound is γ₅·(\|m\|↑ + r). This is the straight precedent's γ₄ of intensity formation (lib.rs:10639-10641), divided by (1 − γ₄), since f is linear in the single intensity component | no |
| T4-U2's bend pressure identity K̃_b·u_free(ε_p) | — | As the thermal identity: `push_formed_product(K̃_rc, fl(ε̃_p·chord_c))` with `RoundedProduct { k: K̃_rc, a: ε̃_p, b: chord_c }`, plus `operand_bound = (\|ε̃_p − m_ε\| + r_ε)·\|K̃_rc\|·\|chord_c\|`↑. ε_p = (1−2ν)·p·π(od/2 − wall)²/(E·A) is enclosed by the same balls. This is RV1 N-3's "rounding enters the bound" | yes (the operand bound still enters B, unfloored) |
| T4-U2's caps c_b = [−P t_i, +P t_j], and the same machinery for T4-U2's terminal caps on arc tangents and interior remainders | — | `Certified`: P (T4-U2's pAi formula, the straight path's) and the tangents t_i = c_h d̂ + s n̂, t_j = c_h d̂ − s n̂ (§2.2), enclosed from held operands. π is a pinned 128-bit ball constant | no |
| Curved thermal identity | `RoundedProduct`, with K̃ and the chord held (lib.rs:10775-10805; S11G §3.2) | unchanged | yes |

**How the thermal identity relates (fact, then inference).**
- **Fact.** The identity's formula is K̃·fl(ε·chord), with the product's binary64 matrix K̃ and chord held (lib.rs:10786-10799). So S11-G sees only lo(ε·chord).
- **Fact.** K̃'s own formation error belongs to K-D5, whose residual ρ = f − K_int·u is formed from the ledger terms themselves (FC:209-226).
- **Inference.** T4-U1b keeps that convention for the pressure identity, unchanged. The caps are certified instead of held, because the tangents are derived quantities. That is stricter than the old held-tangent caps family (S11G §3.2).

**Out of scope:**
- partial extents, which stay blocked (lib.rs:10544-10565);
- arc recovery rows, which S11-G does not cover (S11G §4); RETURN O-13 records an observation.

### 2.1 Held operands (what T4-U1 must hold)

| Group | Held operands |
|---|---|
| Geometry | x_i and x_j, binary64 node coordinates; R, the user radius; y, the plane reference |
| Section and material | E, G, A, I, J |
| Flexibility | k_in and k_out |
| Load | the intensity w, with one nonzero global component |

**Proposal.** After T4-U1, K-D5's `CurvedFormation` (FC:47-61, which today holds PP's rounded `center`) carries exactly these. T4-U1b takes `&CurvedFormation` as its input, so K-D5 and S11-G re-form one intended element.

### 2.2 The formula f (exact real arithmetic)

**(F1) Chord and angle.**
- d = x_j − x_i, L = |d|, s = L/(2R).
- c_h = √(1 − s²), φ = 2·atan(s/c_h).

**(F2) Trigonometric values.**
- S = 2s·c_h, C = 1 − 2s².
- S₂ = 2SC, C₂ = 1 − 2S².

**(F3) Axes.**
- d̂ = d/L; n = y − (y·d̂)d̂; n̂ = n/|n|.
- e_x = −s·d̂ + c_h·n̂; e_z = n̂ × d̂; e_y = e_z × e_x.

**(F4) Local quantities.**
- The local chord is c = (e_x·d, e_y·d, e_z·d), and the local intensity is w_ℓ = (e_a·w).

**(F5)–(F7) CB's `consistent_uniform_nodal_loads` (CB:277-344), with H built from c.**
- F_ab = R[k_in·Q(g, m^in_a, m^in_b) + k_out·Q(g, m^out_a, m^out_b)]/(EI) + R·Q(g, m^t_a, m^t_b)/(GJ) + R·Q(g, m^ax_a, m^ax_b)/(EA).
  - The unit-load series m are at CB:563-612, and the trigonometric Gram g, in (φ, S, C, S₂), at CB:765-782.
- δ_a is formed likewise, with the extended Gram ĝ (CB:690-732) and the load series of w_ℓ (CB:636-685).
- X = −F⁻¹δ, and W = (Rφ·w_ℓ, R²(S − φ, 1 − C, 0) × w_ℓ).
- p_i = H(c)·X + W and p_j = −X. Each 3-block is rotated to global by the rows (e_x, e_y, e_z).

**Admissibility:** 0 < L < 2R and n ≠ 0. PP already refuses the others (lib.rs:7783-7794, :7830-7837).

**The identities used.** Each holds exactly in real arithmetic, for 0 < s < 1.
- **(I1)** φ = 2·asin(s) = 2·atan(s/c_h).
- **(I2)** S = sin φ, C = cos φ, S₂ = sin 2φ, C₂ = cos 2φ.
- **(I3)** The centre x_c = x_i + d/2 − R·c_h·n̂ is PP's convention: the arc bows toward +n̂ (lib.rs:7762-7765, :7838-7846). From it:
  - r_i = R(−s·d̂ + c_h·n̂) and r_j = R(s·d̂ + c_h·n̂);
  - r_i × r_j = −R²·S·(d̂ × n̂), so e_x = r̂_i and e_z = (r_i × r_j)/|r_i × r_j|, as in CB:150-179;
  - e_y = c_h·d̂ + s·n̂ = t_i.
- **(I4)** c = (−2R·s², 2R·s·c_h, 0) = R(C − 1, S, 0).

So H built from the actual chord equals CB's formula-chord H (CB:315-319) in exact arithmetic. The certificate may evaluate any expression equal to f in real arithmetic. If T4-U1 defines the element differently, T4-U1b re-proves (I1)–(I4) for that definition, and the review checks them.

## 3. The method and its proof (brief item 3)

### 3.1 Ball arithmetic

**Representation.**
- A ball (m, r) has m a `Wide2` value and r ≥ 0 a binary64 value. It represents every real x with |x − m| ≤ r.
- Let u = 2⁻¹²⁸.

**Facts the proof uses.**
- **The `Wide` operations.** `add`, `sub`, `mul`, `div` and `sqrt` each return the exact result of the operation on exact operands, rounded once to p bits, to nearest. There are no subnormals. An exponent out of range is an error, never a wrapped value (wide.rs:18-33).
- **Rounding at p = 128.** For a nonzero exact result z, |rnd(z) − z| ≤ ½ulp(rnd z) ≤ u·|rnd z|.
- **Radius arithmetic.** Radii are computed with upward-rounded binary64 operations:
  - `product_upward` (load_ledger.rs:464-474);
  - `sum_upward` and `quotient_upward`, which are new and use the same `fma` pattern;
  - |m|↑ = next_up(|t₀|) from m's exact split (wide.rs:108-120), plus 2⁻¹⁰⁷⁴ if the split is truncated.
- **Range.** An upward radius that is not finite fails the certificate. Underflow rounds up to 2⁻¹⁰⁷⁴.

**Lemmas.** Each assumes that the operands' exact values lie in their input balls.

- **L0, lift.** `from_f64` is exact (wide.rs:314-334), so r = 0.
- **L1, add and sub.** m = rnd(m_a ± m_b) and r = r_a + r_b + u|m|.
  - Proof: |x ± y − m| ≤ |x − m_a| + |y − m_b| + |m_a ± m_b − m|.
- **L2, mul.** m = rnd(m_a·m_b) and r = |m_a|·r_b + |m_b|·r_a + r_a·r_b + u|m|.
  - Proof: xy − m_a·m_b = (x − m_a)·m_b + m_a·(y − m_b) + (x − m_a)(y − m_b).
- **L3, div.** Precondition: |m_b| > r_b. Then m = rnd(m_a/m_b) and r = (r_a + |m_a/m_b|↑·r_b)/(|m_b| − r_b) + u|m|.
  - Proof: x/y − m_a/m_b = [(x − m_a)·m_b − m_a·(y − m_b)]/(y·m_b), and |y| ≥ |m_b| − r_b.
- **L4, sqrt.** Precondition: m_a − r_a > 0. Then m = rnd(√m_a) and r = r_a(1 + u)/m + u·m.
  - Proof: |√x − √m_a| = |x − m_a|/(√x + √m_a) ≤ r_a/√m_a, and √m_a ≥ m/(1 + u).
- **L5, atan.** Precondition: m_t − r_t > 0. Then m = `atan_positive`(m_t) and r = r_t + 21.55·u·m.
  - Proof: |atan′| ≤ 1. K3a's proved contract for an exact input gives |m − atan m_t| ≤ 21.54·u·atan(m_t) (wide.rs:54-60), and atan(m_t) ≤ m/(1 − 21.54u).
- **L6, scaling.** Negation and multiplication by 2^j are exact (`mul_pow2`); the radius scales upward.
- **L7, verified inverse (cond(F)).** Take a ball matrix (F̃, Δ) and any finite `Wide2` matrix X̃; X̃ is computed by Gauss–Jordan at p, but soundness does not depend on how.
  - Form R = I − F·X̃ in balls, by L1 and L2, with X̃ exact.
  - Set ρ = max_r Σ_k (|R̃_rk|↑ + r(R_rk)), rounded upward.
  - **Precondition:** ρ < 1/2.
  - **Claim:** every F with |F − F̃| ≤ Δ entrywise is nonsingular, and |(F⁻¹ − X̃)_rk| ≤ ‖X̃‖∞↑·ρ/(1 − ρ).
  - **Proof.** F·X̃ = I − R_F with ‖R_F‖∞ ≤ ρ < 1, so F is invertible and F⁻¹ = X̃(I − R_F)⁻¹. Then F⁻¹ − X̃ = X̃·R_F·(I − R_F)⁻¹, whose norm is at most ‖X̃‖∞·ρ/(1 − ρ). An entry is bounded by the ∞-norm.
  - **The condition number made explicit.** ρ ≈ cond∞(F)·(c·u + max_rk Δ_rk/‖F‖). The certificate fails only when cond(F) times F's relative enclosure width reaches 1/2.

**Theorem 1 (enclosure).**
- **Statement.** Evaluate (F1)–(F7) on balls by L0–L7. If every precondition holds, every WideError is absent and every radius is finite, then each output component satisfies |f_i(z) − m_i| ≤ r_i.
- **Proof.** By induction over the evaluation. The invariant is that the exact real value of each intermediate, as the same expression evaluated exactly at z, lies in its ball. Lifts start it (L0), and each lemma preserves it for every real input within its balls. By (I1)–(I4), the exact evaluation of this expression is f(z). ∎

**Output.** Each m_i is split exactly into at most 3 binary64 terms (wide.rs:409-452). A truncated split adds 2⁻¹⁰⁷⁴ to r_i, and a split overflow fails.

### 3.2 The term's bound, in S11-G

**Theorem 2 (per term).** For a certified term with binary64 value v: |v − f| ≤ |v − m| + r.
- In the ledger, 12(v − m) enters A_net exactly. It is `add_product(12, v)` minus `add_product(12, t_k)` over the split terms, with no binary64 intermediate (SF-1).
- r enters B, rounded upward (load_ledger.rs:729).
- **The decision is S11-G's, unchanged** (formation_guard.rs:240-242):
  - B > 0 and B ≥ T0;
  - |A_net| + 12B − 12T0 > 0, decided exactly;
  - and the SE clause, which certified terms do not enter.
- Therefore a row that does not fire satisfies |Σ_{t net} (v_t − f_t)| ≤ |A_net|/12 + B ≤ T0. Certified terms are net terms.

**Lemma 3 (the intended-net convention, applying to `Bounded` and `Certified` alike).**
- **Fact.** S11-G forms n′ and S\* from the intended values: the term's value for `Bounded`, and m for `Certified` (load_ledger.rs:640-649, :731-734).
- **Claim.** If no row of the case fires, then for every row, max(|n′|, S\*′) ≤ max(|n|, S\*)/(1 − c), with c = RD(1e-9). The effective criterion is therefore c/(1 − c) ≈ 10⁻⁹(1 + 10⁻⁹) of the exact-formula scales.
- **Proof.** Each row's |n′ − n| is at most its B. No-fire gives B < c·max(|n′|, S\*′). The coupling identity is L_b·fo′ = mo′.
  - So fo′ ≤ fo + c·fo′ and mo′ ≤ mo + c·mo′.
  - By the same argument, max(|n′_d|, S\*′_d) ≤ max(|n_d|, S\*_d) + c·max(|n′_d|, S\*′_d). ∎
- This 10⁻¹⁸-relative excess is pre-existing for `Bounded` (the exact-pressure operands). RETURN O-3 proposes closing it with one constant; T4-U1b does not depend on that.

### 3.3 SF-2's three conditions, item by item

- **cond(F).** L7 makes it explicit.
  - In the probe, ρ ≤ 3.9e-32 for φ ≥ 1° and 3.8e-29 at 0.1°.
  - At k = 10⁴⁰, ρ = 275 to 1476, and the certificate is refused.
  - S11G §3.2 quotes cond₁(F) up to 1.7e4 for realistic bends. By estimate, the certificate fails only when cond(F) reaches the order of 10³⁷.
- **Cancellation.** It appears in the Gram entries for small φ, in p_i = H·X + W_i, and in the rotation.
  - L1–L2 carry absolute radii, so cancellation cannot shrink r below the rounding scale of the operands.
  - The product's own cancellation is measured, not bounded, in v − m.
  - In the probe, r/max|p| ≤ 4.4e-29 for φ ≥ 1°.
- **libm.** None in the certificate. The arctangent is K3a's integer-only `Wide` routine, with its proved bound (L5).
  - T4-U1 may make the binary64 element libm-free: sin and cos from s and c_h, and only φ needs an arctangent (I2 §1.6). The certificate does not need that.
  - It is recommended for platform-independent published bytes (RR, "I109: a correctly rounded norm…", which leaves sin, cos and atan2 to a later round).
  - The probe's libm and libm-free variants give defects of the same order.

### 3.4 Inputs that defeat it: what then happens

**What fails the certificate:**
- any `WideError` (`ExponentRange`, `DivisionByZero`, `NegativeSqrt`, `AngleDomain`, `SplitOverflow`);
- a failed precondition of L3, L4, L5 or L7: a divisor or square-root ball reaching 0, s at or beyond 1 or n near 0 inside a ball, or ρ ≥ 1/2;
- a radius that is not finite.

**What then happens:**
- All 12 terms of that load are pushed as `Formation::CannotBound`, as today, with today's reason text (formation_guard.rs:233-237). The case demotes. Nothing passes silently.
- A non-finite `v` is a ledger range failure, and the row fires (load_ledger.rs:592-594).

## 4. Where it plugs in (brief item 4)

**FK `load_ledger.rs`.** A new variant, and an `add_defect` arm (load_ledger.rs:565-652) equal to `Exact { scale: 1 }` plus `Bounded`:
```rust
/// `intended`: binary64 terms whose exact sum m satisfies |m - formula| <= radius (T4-U1b).
Certified { intended: Vec<f64>, radius: f64 },
// add_defect: the Term value only (a Product is an error); for each t in intended:
//   target.add_product(-12.0, t); intended_net.add_product(12.0, t);
// after target.add_product(12.0, value); then bounds.add(*radius) (a non-finite radius is a range failure).
```
- `Formation`'s size does not grow, because `Exact` already holds a `Vec`.
- `formation_guard.rs` is unchanged: `decide_row` reads `net_defect`, `bound` and `intended_net_lower` as today.
- **The equivalent alternative,** with no FK type change: `Exact { scale: 1.0, scaled_intended: split(m) }` with `operand_bound = r`. RETURN O-2.

**FK `structural/arc_certificate.rs` (new).**
- It needs `Wide2`, which is `pub(crate)` under `structural`'s private `mod retained` (structural.rs:4-5; retained/mod.rs:24).
- structural.rs gets two lines: `mod arc_certificate;` and a `pub use`.
- **The API:**
  - `certify_curved_uniform_load(&CurvedFormation, [f64; 3]) -> Result<CertifiedVector12, ArcCertificateFailure>`;
  - for T4-U2, `certify_bend_caps(…)` and `pressure_strain_error_bound(…)`.
- It has its own ball type, its own point Gauss–Jordan for X̃, and no edits to `formation_check.rs`.
- It allocates no ledger term.

**PP `lib.rs`, in `add_uniform_element_loads`' curved branch (lib.rs:10576-10593).**
- Build `CurvedFormation` from `bend`'s held fields and call the certificate.
- On `Ok`, `ledger.push_formed(.., v[k], Formation::Certified { .. }, operand_bound, false)`.
- On `Err`, push today's `Formation::CannotBound` call unchanged.
- The pushes stay inline in that function. Then:
  - T8's required tokens (`Formation::CannotBound` is still present), its flag set {false}, its formed-site list, rule 5's producer list (s11f_site_test.rs:215-223, :1343-1383, :1429-1481) and the S11-F count for this function (`0`, :534) all hold unedited;
  - `tests/s11f_site_test.rs` is not touched.

**Unchanged** (T3's constraints 3 and 4):
- `preview_physics::LIMITATIONS` (preview_physics.rs:73-81), whose text never mentions this;
- every reviewed input;
- PP's `Cargo.lock`, because FK is already a path dependency and no new crate is added;
- `formation_guard::RecoveryRecord`, `preview_physics::MemberRecord` and the `Preview*` inputs, because the certificate reads held fields already built;
- `retained_product.rs`;
- SA, CB and `formation_check.rs`.

**W1 and retained.** W1 still refuses curved bends and element uniform loads (retained_product.rs:1557-1571). T4-U1b adds code only on the ordinary ledger builder, none in retained or source-recovery paths.

**FK `tests/s11_site_table.rs`.** Add the new file to `SOURCES` with count-0 rows, declared as an additive extension with a killed binary64-fold mutant, on K1's precedent (RR, "K1: the S11 site table for sparse.rs and formation_check.rs"). Radius sums go through helpers, so no `+=` shape is added.

**Cost.**
- **Operations.** One certificate is 4,666 ball operations (2,887 mul, 1,659 add, 116 div, 3 sqrt, 1 atan) plus about 360 point operations for X̃ (`_run_records/opcount.stdout.txt`; the emulation skips no zero terms).
  - That is about one K-D5 `curved_matrix` re-formation (FC:665-762), which K-D5 already runs per curved element per checked case.
  - F, X̃ and the K⁻¹ ball do not depend on the load (about two-thirds of the work) and may be cached per arc and solve.
- **Memory.**
  - The transient memory is under 20 KB per call (about ten 6×6 ball matrices at about 40 B per entry), freed on return.
  - Each certified term keeps at most 3 f64 in its record, about 0.5 KB per arc, load and live case. For example, 10,000 loaded arcs come to about 5 MB per live case, about 0.04 % of the 12 GiB ceiling (RR, "Owner decision: M's practical limit is 12 GiB").
- **Timing** is not claimed here. It is measured at implementation with interleaved runs of fresh archive builds (RR, "S11-G performance finding withdrawn; the method for performance claims").

## 5. T15's new meaning, and the T3-owned tests and tables it changes (brief item 5)

| Item | Change |
|---|---|
| `s11g_tests.rs:1743-1774`, T15 | **New meaning:** a realized arc carrying a uniform load (the same `curved_body` model, at ordinary coordinates) is certified and publishes `CHECKS_PASSED` on both entries and in both modes. **Precondition (paths differ):** every arc row carries `Certified` records and no `cannot_bound_sources`, and today's rule (`CannotBound`) would demote. The test also asserts the exact row statistic < 1, computed in the test. Renamed `t15_curved_uniform_load_is_certified` |
| New T15b | The same at UTM (X 5e6, Y 3.5e6; and X 7.3e6) and for 45°, 15° and 5° bends, k = 1 and 2, out-of-plane and in-plane loads. Runs after T4-U1 |
| New T15c | **A natural certificate failure** (for example k = 1e40, which makes ρ ≥ 1/2 in the probe) on a model whose ordinary report is Passed. It must demote, with the `CannotBound` reason. If no such Passed model is constructible, the test goes through a `#[cfg(test)]` failure seam, and RETURN R-2 marks that for ROOT. **It keeps M16** ("CannotBound as a zero defect") killed |
| New T15d | A true catch: a 0.1° bend whose binary64 element defect exceeds the criterion (probe: 1.7–37×) demotes, with the formation-defect reason |
| `s11g_tests.rs:1776-1806` (`ruling1_both_guards…`) | Its load-row trigger is a curved uniform load, which no longer fires. Rebuilt with a straight UDL-W1e8-type body as the load-row trigger; its assertions are unchanged |
| M16 | Its killer moves from T15 to T15c (natural, or the seam), plus a load_ledger unit test |
| `s11f_tests.rs` F8 `f8_curved_*` | They compare values only (`value_bits`, s11f_tests.rs:141-145), and the values are unchanged. At G = 1e80 the request becomes Sensitive by B (two radii add) while its net-load twin is Passed; that is not asserted. Rerun |
| T8, PRODUCERS and the S11-F counts (`tests/s11f_site_test.rs`) | Pass unedited (§4). T8's class text ("curved CannotBound") goes stale. Updating it is deferred to T4-U2's T8 row or B7, as T3 chooses (RETURN O-9) |
| FK `tests/s11_site_table.rs` | The `SOURCES` extension of §4 |
| load_ledger unit tests | `Certified` arm: the exact defect into A_net; the radius into B; the intended contribution as m; a non-finite radius or component is a range failure |
| S11-G CHANGE_RECORD's disclosed availability loss | Superseded for certified terms. Recorded in T4-U1b's change record; T3's record is not edited |
| Gates | Pass B (the G7 script on the final basis), T9 (zero committed-byte diff forecast: no committed envelope or model loads a realized arc; S11G §6.3) and the both-entry gate (no frozen reference loads one) all apply. Each forecast is confirmed by run |

## 6. Validation and mutants (brief item 6; plan §5)

**Required tests:**
- **V1. Passed.** Self-weight (−Z), in-plane (−Y) and a skew uniform load on arcs of 90°, 45°, 15° and 5°, with k = 1 and 2, at ordinary coordinates and at UTM (X 5e6, Y 3.5e6; X 7.3e6). Each publishes `CHECKS_PASSED`, both entries, both modes, with the certified rows' statistic computed in the test and below 1.
  - After T4-U2: the first usable path, with pressure, weight and temperature on the anchored L line.
- **V2. Enclosure (FK).** A frozen set of arc vectors, computed by an independent TASK at ≥ 60 digits, must lie inside every ball. It covers φ = 0.1°, 1°, 90° and π − 1e-6; k = 1e-3 and 1e6; extreme R/r; and UTM offsets, on the pattern of K3a's 3,307 referenced vectors.
  - Unit tests of L1–L7 against exact rationals, with adversarial balls, including RV2's atan input (wide.rs:96-101).
  - Refusals: a divisor ball containing 0, a square-root ball reaching 0, and ρ ≥ 1/2.
- **V3. Demotion.**
  - Natural: T15d.
  - Exact controls, at unit level: moving one certified component by +2·T0 fires, and by +T0/2 stays silent (when the base statistic is < 1/2). The probe holds both: +2·T0 fires in 84 of 84 cases, and +T0/2 stays silent in 73 of 73 applicable cases.
- **V4. Without a certificate.** T15c. The `CannotBound` fallback is pushed from the same function (T8 token).

**Mutants, each to be killed:**

| ID | Mutation | Killed by |
|---|---|---|
| MU1 | Radius dropped (B += 0) | V2 enclosure (ill-conditioned arcs); a unit row with zero defect and r ≥ T0 |
| MU2 | Intended := v (defect 0) | T15d; V3 +2·T0 |
| MU3 | Residual test skipped (rad(K⁻¹) = 0) | V2 (φ = 0.1°, k = 1e6); T15c |
| MU4 | ρ threshold removed or raised to 1 | T15c |
| MU5 | Atan radius without the 21.55u term | L5 unit test on RV2's input |
| MU6 | L1 without u·\|m\|; L2 without r_a·r_b; L3 with \|m_b\| for \|m_b\| − r_b | L1–L3 adversarial unit tests |
| MU7 | Certified pushed self-equilibrated (floored) | T8 flag set {false} |
| MU8 | Fallback removed (skip, plain push or garbage record) | T15c; T8 (M2) |
| MU9 | Generated-load γ₅ operand bound dropped | A unit pin of the operand bound |
| MU10 | Axes transposed in the rotation to global | V2 |
| MU11 (T4-U2) | ε_p operand bound dropped; caps as held-tangent `RoundedProduct` | Unit pins; T4-U2's T8 row requires `Formation::Certified` at the caps site |

**Not listed as a required kill:** building H from (I4)'s formula chord instead of the actual chord. Both are the same real number, so soundness is unaffected. Claiming that mutant equivalent would need an independent check (T4_RULINGS, item 1).

## 7. SP-2: can a pressurized bend with weight at ordinary coordinates still miss Passed?

**The certificate itself:** no reason found. The radius is ≤ 4.4e-29 relative and ρ ≤ 3.9e-32 for φ ≥ 1°. By estimate, it fails only when cond(F) reaches the order of 10³⁷.

**Residual reasons, stated plainly:**
1. **Small-angle arcs.**
   - At φ = 0.1°, CB's binary64 closed form loses about 4 to 5 digits (defect 1.6e-5 to 3.7e-4 of the bend's own vector), and the guard fires at 1.7–37×. That is a true catch.
   - At 1°: up to 2.3e-2 of the threshold in the 3 m / 4 m L line, and 0.30 in a bend-dominated body (0.3 m straights, UTM 7.3e6).
   - At ≥ 5°: ≤ 3e-3.
   - If T4-U2 admits arcs below about 0.5°, they may stay Sensitive unless T4-U1 adds a small-angle binary64 form.
2. **The checks outside T4-U1b.** K-D5 on the objective element (T4-U1's acceptance, `CSKEW_8_5`, the M31b kill) and the solve's own rcond.
3. **T4-U2's pressure terms** are forecast by magnitude only (not probed).
   - The ε_p operand bound (about γ·κ·pAi) is on the unfloored side. It is safe while the body's S\* is O(pAi), which a bend's own free-row nets supply.
   - T4-U2's reference runs confirm this.
4. **Process.** If T3 or ROOT does not accept R-1, SP-2 fires by construction (RV1 B-1).

At UTM, today's absolute-centre element is refused at 45° by the radius check in every UTM case of the probe (CB:160-162). T4-U1 is a prerequisite there, as the plan says.

## 8. Evidence

**The probe** (`_run_records/arc_cert_probe.py`; Python 3.13, run with `-I`). It covers 87 arc cases: 72 in the L-line sweep, 12 bend-dominated, and 3 at k = 1e40. Maxima over loads, k and offsets:

| φ | ρ | r/max\|p\| | Objective (libm-free): defect / guard | Today: defect / guard |
|---|---|---|---|---|
| 90° | 6.7e-35 | 1.0e-32 | 6.4e-15 / 5.7e-7 | 6.3e-11 / 5.6e-3 (UTM) |
| 45° | 5.1e-35 | 3.6e-33 | 3.5e-14 / 1.5e-6 | refused at UTM (8/8) |
| 15° | 1.9e-34 | 1.7e-32 | 7.0e-13 / 1.0e-5 | 1.3e-9 / 2.1e-2 |
| 5° | 1.6e-33 | 3.5e-31 | 3.7e-11 / 1.8e-4 | 1.8e-9 / 9.6e-3 |
| 1° | 3.9e-32 | 4.4e-29 | 2.3e-8 / 2.3e-2 | 4.6e-8 / 4.6e-2 |
| 0.1° | 3.8e-29 | 4.2e-25 | 3.7e-4 / 37 (fires) | 3.7e-4 / 37 |

**Notes on the probe:**
- Every reference component lies inside its ball, in 84 of 84 cases.
- At k = 1e40 all three cases are refused: `CannotBound`, ρ = 275 to 1476.
- "Defect" is max\|v − m\|/max\|p\|. "Guard" is the S11-G load-row statistic over threshold at the free rows, with straights taken as exact.
- Its limits: binary64 Gaussian elimination stands in for `solve_dense`; radii are exact rationals rounded up once per operation; the atan midpoint is accurate rather than K3a's own; no product code ran.

**Read:**
- plan §2, §3.1, §3.3 and §5 (`8d0635fa…`);
- `T4_RULINGS.md` (`cbec7434…`);
- RV1 `REVIEW.md` (`3d38f6cb…`) and `ADDENDUM_01.md` (`3c5d7598…`);
- I2 `RETURN.md` (`7111e843…`);
- `S11G_GUARD.md` (`afe5f256…`);
- the RR entries named in §1, and "R5-4", "K3a arctangent", the K-D5 M31b entries and the K1 site-table entries;
- the code cited above.

**Wider consultation:** none.
