# T4-RV1: independent review of T4 plan 01

**Who and when:** T4-RV1, TASK (Type 2), independent reviewer, 2026-10-09 UTC. I did not write the plan or its research. Brief: `R4/BRIEFS/T4-RV1_PLAN_REVIEW.md`.

**Reviewed bytes:** `R4/PLAN_01/PLAN.md`, sha256 `d30abda9931a3b9b38bf05390db7ecf127ff6e3dc372991c84a905b6b0b7b863`. This is the draft `1198702d…` after HELPS_HUMANS renamed the units in place to T4-U0…T4-U9 and the T3 references to "T3's U3" (HELPS_HUMANS' message to me during the review). I checked that claim: the size grows by exactly 397 bytes, which is 119 `T4-` prefixes (357 bytes) plus the ten T3 rewordings (40 bytes). So no other content changed, but one rewording is wrong (S-1).

**Read:** the plan; its brief (`16c9fff5…`); `R4/T4-I1…I4/RETURN.md` (hashes as in the plan's Evidence table, re-verified); `I/CORRECTNESS_DESIGN/PRESSURE_REFERENCE_QUALIFICATION.md` (QUAL) §1 to §3; `JOINT_REFERENCE/CONTRACT.md` (JR) §4 and §5; the code at `70e7f49ced` (T3's U3 basis) and readers at `ec5d397359`; T3's rulings at `WT/numerics` HEAD `a31c14e4d3`.

**Method and limits:** reading, plus one standard-library Python check of H-2 (`WT/scratch/t4_RV1/h2_check.py`, sha256 `5e31dc084721729b6c99a91ec19f835b899cb751a158d8032e53a0818a6af620`; output `h2_check.stdout.txt`, `278bff18e17abcc952398ec1e887021a7b293829fc05bf1f4ee06bed94d913ac`; Python 3.13). No cargo, no tracked file changed, no commit.

## Disposition: BLOCKING (one finding), otherwise PASS WITH FINDINGS

The physics of H-2 is correct: every sign and term the plan states checks out on paper and to about 1e-13 in arithmetic (§1). One finding blocks sending the plan to the owner unchanged. **B-1:** the first usable path, and C2's promise of "Passed standing on bends", cannot be met, because self-weight on an arc is `CannotBound` and no unit removes that. The fix is small: plan text plus one scheduling choice. Eight SHOULD-FIX items should be repaired in the same revision. S-1 is a one-token cycle introduced by the rename.

## 1. The physics of ruling H-2 (item 2)

**Derivation.** Notation: a bend of radius R, end tangents t_i and t_j in i→j travel, and P = pAi.

1. **The wetted-wall load.** Fluid statics on a slice gives a wetted-wall load of (P/R)·n_out per unit centreline length. It acts at the centreline and carries no distributed moment (the face forces act at the face centroids). Its resultant is P(t_i − t_j), which is QUAL §3.4's P(t_in − t_out).
2. **The membrane state.** Cut the arc at angle φ and keep the free part toward j. The wall load on that part gives N = P(1 − cos(φ_j − φ)) and M = PR(cos(φ_j − φ) − 1). Adding the outward pair c_b = [−P t_i, +P t_j] gives exactly N = P, V = 0 and M = 0. So wall load plus c_b is self-equilibrated, and the arc is in a pure membrane state.
3. **The strain in that state.** The Castigliano element contains axial energy (`curved_bend/src/lib.rs:80-82@70e7f49ced`). The elastic part of the strain is therefore P/(E·As). QUAL §1's σz = E(εz − αT) + 2νP/As adds the Poisson eigenstrain −2νP/(E·As). The total is ε_p = (1−2ν)P/(E·As), with no change of curvature. The deformation is therefore u_free(ε_p).
4. **The consistent vector.** Hence the consistent vector f of wall load plus Poisson satisfies c_b = K_b·u_free(ε_p) − f. That gives f = **K_b·u_free(ε_p) − c_b**, which is H-2's bend term. It holds for any k: by the unit-load theorem, the response to a uniform eigenstrain with i clamped is u_free, whatever the bending flexibility.
5. **Summing the members.** The member cap pairs sum to Σ_m c_m = (terminal caps) + Σ_interior P(t_in − t_out). The ledger therefore equals Σ_m K_m·u_free(ε_p) − (caps at non-transferring terminals) exactly when the interior remainder is **+P(t_in − t_out)**. Here t_in is the arriving member's end tangent and t_out the departing member's start tangent. The remainder is the physical kink force, and it is zero for exact tangency. Each K_m·u_free is self-equilibrated provided K_m's null space is the rigid motions. That is why T4-U1 must come first, and with it global equilibrium holds for any supports.
6. **Recovery.** The element's end action is K·d − f = K(d − u_free) + c_b. Along the end tangents this gives N_w = N_el + P; at each station the wall force is N_el(s) + P along t(s), with M and V elastic only; and S = N_el. For a free closed L, d = ε_p(x − x₀) solves the system, giving N_el ≡ 0, N_w = P, S = 0, M = 0, zero reactions and self-similar growth. For an anchored L, the reactions equal those of the thermal problem with strain ε_p. On straights, N_el + P ≡ N_mech + 2νP algebraically, which is QUAL §1's N_w.
7. **Straight-only regions.** They contain no bend term and no remainder, so their ledger is unchanged.

**Arithmetic check** (in-plane L: 3 m straight, 90° bend with R = 0.229 m, 4 m straight; OD 168.3 mm, t = 7.11 mm; p = 5 MPa; ν = 0.3; k = 1 and 2). Four formulations were compared:
- F1, the plan's H-2 ledger;
- F2, Σ K_m·u_free(ε_p);
- F3, the explicit wall/cap free body, with the bend's wall load integrated by unit load and no K·u_free;
- F4, the bend replaced by n straight segments with kink forces (k = 1).

| Check | Result |
|---|---|
| H-2 bend term against the explicit consistent vector of wall load plus Poisson | 2e-15 (k = 1) and 5e-15 (k = 2) relative. With c_b *added* instead of subtracted the error is O(1). |
| Free L (one end anchored, both terminals transferring) | Zero reactions (≤ 1e-15 of P); tip = ε_p·x to 1e-12; rotation 0; N_el/P ≤ 4e-15, so N_w = P and S = 0. Holds in F1, F2 and F3, for k = 1 and k = 2. |
| Anchored L | F1, F2 and the thermal(ε_p) problem equal F3 to 6e-13. Polygon F4 converges to F3: 3.8e-4, 2.4e-5 and 2.2e-6 at n = 8, 32 and 96. |
| Non-tangent bend (1e-3 rad kink at C) | With the remainder: balanced (1e-16 of P) and equal to F2. Without it: residual P·1e-3, as stated. |
| Separately supported closure at D; pressure plus thermal | F1 = F2 = F3. |

**Verdict on item 2.** The ledger, ε_p, the terminal caps along the end tangents, the interior remainder and the recovery are all correct. Global equilibrium holds, straight-only regions are unchanged, and N_w = N_el + pAi, S = N_el and the +pAi station membrane all follow. What still needs fixing is listed below: S-3 (the references are not independent), S-4 (straight-member recovery bytes), S-5 (excluded effects) and N-1, N-3 and N-4.

## 2. Findings

### BLOCKING

**B-1. The first usable path and C2 cannot reach Passed: self-weight on an arc is `CannotBound`** (items 4 and 6).

- **Claim.** §1 defines "done" as Passed standing. C2 promises bends that "keep Passed standing". §2's unit "carries pressure, weight and temperature in one case". P-D notes that uniform loads on arcs are `CannotBound`, but only the pressure term is planned to be bounded.
- **Evidence.**
  - `PP/src/formation_guard.rs:21,233-236@70e7f49ced`: any `CannotBound` term ("curved-span consistent load vector") demotes the row.
  - `PP/src/s11g_tests.rs:1747` (T15): a realized curved span carrying a uniform load is pinned to demote on both entries and in both modes.
  - T3's rulings, "S11-G note revision 2" (ROOT, 2026-09-27), item 3, accepted this loss because "realized curved bends are opt-in, and no committed model uses one", and expects "W1c with T4 removes it".
- **Consequence.**
  - Every realistic bend carries self-weight, so the first path's case is Sensitive whatever T4-U1 does.
  - SP-2 fires on the first path by construction, and C2 cannot be met.
  - D-2 (a) makes realized bends mandatory for pressure, which removes the premise of T3's acceptance.
- **Repair.** Choose one, and say which:
  - **(a)** Add to T4-U1 or T4-U2 an exact or conservative formation bound for the arc's uniform-load consistent vector. It must meet SF-2's conditions (cond(F), cancellation and libm; T3's rulings, "S11-G after V1's S11G_CHECK", ROOT 2026-09-27) and be agreed with T3 under the T3-interface review.
  - **(b)** Restate C1, C2 and the first-path "done": weight-bearing bend cases stay Sensitive, with the `CannotBound` reason, until that bound lands, while the pressure-plus-thermal case must reach Passed. Then put the reopened availability loss to HELP_HUMAN as an H-5.

  I recommend (a), in T4-U2, designed now: it uses the same formation machinery as the pressure term's bound.

### SHOULD-FIX

**S-1. The rename created a dependency cycle** (item 4).
- **Claim and evidence.** §3.2's T3 row now ends "T4-U3 merged before T4-U0" (line 181). The draft's "U3" there meant T3's U3 (compare §3.1, §7 R8 and "Blocking"). §3.1 says T4-U3 merges after T4-U2, and T4-U2 depends on T4-U0.
- **Consequence.** As written, the dependencies form the cycle T4-U0 → T4-U3 → T4-U2 → T4-U0. HELPS_HUMANS' statement that every T3 reference now says "T3's U3" is not true for this line.
- **Fix.** "T3's U3 merged before T4-U0".

**S-2. The deletion PR is held hostage to the largest unit** (item 4).
- **Claim.** T4-U3 can merge only after T4-U2 (8–10 days), because it needs U2's admission seam and the v3 identity.
- **Evidence.** I3 §0.3: the connector has no container until the exact profile admits a component family (`pressure_runtime.rs:157-177@70e7f49ced`).
- **Consequence.** The owner's M07 deletion is gated on the riskiest unit, and both lanes edit `pressure_runtime.rs`, PP `lib.rs` and the readers at the same time.
- **Fix.** Land the family-dispatching admission seam (named refusals for every family) and the v3 contract identity skeleton in T4-U0, or in a small T4-U2a. T4-U2 and T4-U3 then both depend on that seam.

**S-3. H-2's references are not independent of the equivalence under test** (item 2).
- **Claim.** The named reference formulations are JR's (A) and Σ K_m·u_free(ε_p). The anchored closed form is "equal to a thermal problem with strain ε_p".
- **Consequence.** The second formulation and the closed form presuppose the equivalence. JR's (A) does too, if the bend's wall load is taken as K_b·u_free − c_b.
- **Fix.** Require at least one reference to integrate the arc's wetted-wall load pAi/R and the Poisson eigenstrain directly by unit load, as RV1's F3 does. Add a polygon-limit control at k = 1 (F4), which uses no curved element.

**S-4. SP-1 against the new recovery form** (items 2 and 6).
- **Claim.** H-2 and T4-U2 state recovery generally as N_w = N_el + pAi and S = N_el.
- **Evidence.** Today's straight recovery is N_mech + 2νpAi and N_mech + (2ν−1)pAi (I1 §1.3). The two forms are algebraically equal but not bitwise.
- **Consequence.** If straights switch to the new form, SP-1 fires.
- **Fix.** State that straight members keep today's formulas and that the new form applies to arcs only. Also say what SP-1's "straight-only exact case" covers: v2 cases byte-identical, and the numbers of straight-only regions under v3 bit-equal to v2's.

**S-5. Excluded effects are incomplete or misstated** (item 2).
- **Static pressure only.** Neither D-3 nor any bend limitation says that loads come from static pressure only: steady-flow momentum and transient loads at direction changes are not modelled. QUAL §3.6 and JR (§4, last paragraph) require this disclosure, and it matters exactly when bends are admitted. Today's profile limitations do not mention momentum (`lib.rs:1039-1052@70e7f49ced`).
- **The Poisson term on the arc.** The term uses the straight Lamé sum 2P/As, while U2 withholds the straight Lamé hoop on arcs as false. Say this. For a thin shell, the toroidal hoop weighted by area has a mean of exactly pr/t, so the uniform term is the right mean. The circumferential variation adds an in-plane eigencurvature, which belongs to the excluded bend-opening effect.
- **Fix.** Add both to D-3 and to the v3 approximation text.

**S-6. The legacy-joint recognition catches annotation joints** (item 1, the joint PR).
- **Claim.** §6 recognizes a legacy joint as an `expansion_joint` with no `objective_connector` that carries `expansion_joint_pipe_ref` and/or the rates. D-4 keeps an explicit `not_solver_consumed` annotation mode.
- **Consequence.** An annotation-mode joint with a pipe reference would be refused.
- **Fix.** Exempt an explicit `solver_consumption = not_solver_consumed`.

**S-7. The frame of bend end rows is left to T4-U4.**
- **Claim and evidence.** T4-U2 publishes N_w and S at bend ends. Arc end force rows are in the chord frame today, while station rows are in the tangent frame (I2 §3.4). I1 §5.3 #8 notes that chord-frame end rows are not wall actions.
- **Consequence.** N_w = N_el + pAi holds only along the end tangent, so this cannot wait for T4-U4's "one frame per row family".
- **Fix.** Fix the tangent frame for the pressure family's end rows in T4-U2.

**S-8. The effort figures are lower bounds** (item 6).
- **T4-U2** (8–10 days) bundles: a contract; admission; chain topology; a term family; arc recovery; three readers and a semantic table; M02 authoring; and a VP-STATIC transport and package whose gate tests run only in DEC-025 (I4 §0.8).
- **T4-U3** (8–12 days) is about 2,265 enclosing lines, including about 300 TS (I3 §1.2). It also covers 15 slots, connector authoring, three routes and the full T3 gate set.
- **The calendar.** "First usable path in about 3 weeks" excludes gates that took days each in T3's record.
- **Fix.** Give gate-inclusive ranges, or label the figures as lower bounds.

### NOTES

- **N-1. Signs and notation.**
  - Write c_b = [−pAi t_i, +pAi t_j] (outward) explicitly.
  - Define the remainder without reference to member orientation: the sum of the incident members' outward caps at the node, which is pAi(t_in − t_out) in traversal order. This is safe for reversed members.
  - The negative control "imbalance pAi(t_in − t_out)" uses the bend's own tangents, not a node's. The residual of the applied set is −pAi(t_in − t_out).
- **N-2. Tangency rule.** The remainder makes small kinks physically exact, so state the tangency admission rule as an engineering tolerance, with larger kinks refused as mitres until T4-U7. Today tangency is only warned about, above 1e-6 rad (I2 §2).
- **N-3. Forming ε_p.** Unlike the thermal input strain (`RoundedProduct{a: thermal_strain}`, `lib.rs:10766-10802@70e7f49ced`), ε_p is a derived composite. Its own rounding must enter the S11-G bound, or it must be formed in `Scaled` arithmetic as the straight path is. The element's A and the annulus' As must also be the same value.
- **N-4. Another negative control.** Add one where the wall load is included in the station statics as well as the +pAi membrane (a double count).
- **N-5. D-5.** Name the basis that drives the pressure load path (Ai for the caps, As for ε_p), separately from the published stress bases. "Pressure annulus on both" is ambiguous for the loads.
- **N-6. Route coverage.** State whether T4-U2 covers 0.4.0 and `load-reference-1` (I1 §3.1). Also state the exact-route admission of geometry-only bends outside regions.
- **N-7. Order.** T4-U0 → T4-U1 is a facade serialization, not a logical dependency. T4-U1 could start alongside T4-U0.
- **N-8. Small points.**
  - The v2 readers will accept p < 0, but v2's byte-identical limitations cannot carry the collapse disclosure.
  - Withholding radial rows on arcs is unnecessary, because the surface values −p and 0 are boundary tractions. It is harmless.
  - In H-4, "T3's U3 text T4" reads as the tranche T4.

## 3. Items 1, 3, 4, 5, 6 and 7 in brief

- **1. Coverage:** all seven brief items are covered, including the fourth retired case (I4 §0.1), the deletion, and the legacy refusal.
- **3. Facts:** all verified at the cited bytes:
  - the exact route refuses every component (`pressure_runtime.rs:171-177`);
  - `objective_connector` is accepted only in 0.3.0/0.4.0 (`:157-168`), so the joint has no container;
  - the `.expect` (`lib.rs:5483-5492`);
  - the exact maximum has no bend guard (`:5396-5398`, against `:5357`);
  - the readers' `long_straight_annulus_small_strain_v2` and `p_pa >= 0` pins (rs `:620-627`, py `:158`, ts `:138` at `ec5d397359`);
  - S11-G's `CannotBound` against the bounded thermal identity;
  - the bend reads the derived G on 0.3.0 (`pressure_material.rs:86-88`).

  The deletion extent matches I3 §1.2: about 1,955 lines in Rust plus about 300 in TS.
- **4. Order:** T4-U0 → T4-U1 → T4-U2, with T4-U3 in parallel, is feasible once S-1 and S-2 are repaired. The first path is truly end to end: authoring, save and reopen, both modes, the three readers, the Results panel, export and the native witness. It tests P-A to P-F, but it will trip B-1 rather than test it.
- **5. Decisions:** D-1 to D-6 are the right owner questions, few and concrete, and the recommendations are sound. Nothing within authority is put to the owner. B-1 may add a HELP_HUMAN H-5. H-1 to H-4 are properly HELP_HUMAN's:
  - H-2 reverses JR's selection of (A) (CONTRACT:69), which JR itself permits ("two equivalent… one selected implementation owner", :67);
  - H-3 settles I3 §0.7 conservatively.
- **6. Risks:** apart from S-8 and B-1's rewording of SP-2, add two risks: the latency of T3's agreement (the K-D5 and M31b re-derivations) and collisions with T3's reader lanes.
- **7. Hygiene:** PASS. Only placeholder paths are used, and "the owner's Mac" names a platform, not a machine.
