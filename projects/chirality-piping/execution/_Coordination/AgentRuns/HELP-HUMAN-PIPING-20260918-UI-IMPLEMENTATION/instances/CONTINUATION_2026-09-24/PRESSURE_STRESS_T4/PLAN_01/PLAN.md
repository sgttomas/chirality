# T4 plan 01: pressure, stress and section mechanics

**Status:** a proposal for the owner's approval. It is not accepted until the owner approves it through HELP_HUMAN.

**Who and when:** HELPS_HUMANS (Agent 1, the T4 design manager), for HELP_HUMAN (Agent 0), 2026-10-09 UTC.

**Revision:** 2. It folds in T4-RV1's review and T4-I5's account of the T3 side. The dispositions are in `PLAN_01/RV1_DISPOSITION.md`.

**Brief:** `R4/BRIEFS/HELPS_HUMANS_T4_PLAN.md` (sha256 `16c9fff5…`).

**Basis:**
- main `ec5d397359`;
- T3's U3 pressure retirement at `70e7f49ced` (`codex/piping-t3-pressure-retire-20261008`), which is not yet merged. Implementation starts after T3's U3 merges.

**Unit names:** T4's units are **T4-U0 to T4-U9**. "T3's U3" always means T3's pressure retirement.

**Evidence:** five research TASKs and one review, listed under "Evidence" at the end. Their facts carry `path:line@commit` citations; this plan cites them by section, for example "I1 §5.3".

## 0. Summary

**Where things stand.**
- Pressure can be analysed only on straight pipe with linear supports.
- The exact route refuses every component, and T3's U3 deleted the old bend pressure load.
- The desktop cannot author a curved (realized) bend.
- A realized bend carrying self-weight is published Sensitive, because T3's formation guard cannot bound a load vector on an arc.

**What T4 delivers.** The exact contract carries realistic piping, each step through to the desktop:
1. realized bends;
2. a corrected expansion joint;
3. bend and branch stresses;
4. reducers and tees.

**The first usable path** is an L-shaped pressurized line: straight, curved bend, straight.
- It is authored on the desktop, solved under a successor exact contract, and published at Passed standing.
- It is read by all three readers and validated against independent closed forms.
- Four small or medium PRs prepare it: exact-route hardening; the curved element's objective formation, which also removes T3's UTM-scale defect; a formation certificate for arc load vectors; and the exact route's admission seam with the successor identity.

**The corrected joint** runs in a parallel lane from the seam. The old element is deleted in the PR that lands it.

**Decisions.**
- **The owner (D-1 to D-4, §4.1):**
  - approve the order;
  - pressure on realized bends only;
  - leave bend opening, pressure stiffening and flow momentum out for now;
  - refuse every legacy joint.
- **Later:** D-5 and D-6 are needed only later.
- **HELP_HUMAN:** H-1 to H-4 (§4.2).
- **T3:** its agreement on §3.3 and annex A.

## 1. What the user gets, in order

"Done" means delivered app capability:
- merged on main;
- authored, solved, inspected, saved, reopened and exported on the native desktop path;
- independent references passing in both solver modes;
- the three readers agreeing;
- Passed standing at ordinary and at UTM-scale coordinates, for cases with weight, pressure and temperature, unless T3's checks legitimately demote a case;
- the native witness on the owner's Mac recorded, or recorded as outstanding.

| # | Capability (user's view) | Done means, in addition to the above | Unit |
|---|---|---|---|
| C1 | **Pressure through bends.** A pressurized line with realized bends (the user's flexibility factor k), anchors, guides and linear springs. Any number of load cases, each with weight, pressure and temperature: sustained, expansion and operating as separate cases. Model 0.3.0 and 0.4.0 (load-reference-1). | Displacements, six-component reactions, wall force, effective force, membrane stress and stress components on straights and bends. Lamé hoop and radial stress on straights. | T4-U0 to T4-U2 |
| C2 | **Bends that stay clean at real-world coordinates and under weight.** | T3's K-D5 no longer demotes the recorded cases (X = 5e6 m and 7.3e6 m). No bend is refused by the radius check at large coordinates. A realized bend carrying self-weight or another uniform load is no longer `CannotBound`. | T4-U1, T4-U1b |
| C3 | **Expansion joints in equilibrium.** An explicit connector with frame, attachment offsets, 6×6 stiffness and span replacement. | Connector forces and moments are published. Every legacy joint is refused with a re-author message. The old element is gone. | T4-U3 |
| C4 | **Bend and branch stresses an engineer can use.** | A certified maximum on arcs. A toroidal hoop on bends. Directional user-SIF intensified bending on bends and branches. Transverse-shear stress and signed fibre stresses (VP-STATIC Q1). One frame and sign convention per row family. | T4-U4 |
| C5 | **Pressure thrust on joints, with tie rods.** | Untied bellows thrust p·Ae and elastic tie rods, with each tie's force published. | T4-U5 |
| C6 | **Honest section bases.** | Stiffness, mass and stress use the bases decided in D-5, each named on the result. | T4-U6 |
| C7 | **Pressure through reducers, tees and mitres.** | Bore changes, branch caps and kink resultants, with T7. | T4-U7 |
| C8 | **Shear-deformable straight pipe.** | Timoshenko with the energy-matched annular factor (SHEAR_REFERENCE). | T4-U8 |

**What T4 alone does not give.** Each of these belongs to another tranche:
- combinations on the exact route (T6);
- nonlinear and constant-effort supports under pressure (T5);
- hydrostatic head and hydrotest states (T2);
- retained precision for pressure and bends (T3-F2b and W1c).

C1 already supports the standard sustained, expansion and operating checks for linear-support systems, as separate load cases.

## 2. The first usable path

**The unit.** An L line: straight pipe, a realized 90° bend, straight pipe. It has closed, wall-transferring terminals and both ends anchored, with a free-ended variant. It carries pressure, weight and temperature in one case.

It runs through the whole chain:
- authored on the desktop (M02 minimal authoring: realize the bend and enter k; the region accepts the bend);
- applied, then saved and reopened;
- solved through the native path in both modes, on 0.3.0 and 0.4.0 documents;
- published under the successor contract, at Passed standing;
- accepted by the Rust, Python and TypeScript readers;
- shown in the Results panel;
- exported.

**Why this unit.** It tests the premises most likely to invalidate later work:

| Premise | Why it matters later |
|---|---|
| P-A: a non-straight pressure family can carry its own contract identity, and the readers dispatch on it (I1 §3.2: every reader pins straight premises) | Joints, reducers and tees reuse the same dispatch |
| P-B: the exact route admits a component family, and refuses all the others by name (I1 §5.2: lifting the refusal alone panics) | The joint (T4-U3), T7's components |
| P-C: the member-wise pressure ledger holds across a change of direction (§4.2 H-2) | Joints, reducers, T2's head |
| P-D: every load term on an arc can be certified, so T3's S11-G and K-D5 publish the case Passed. Uniform loads on arcs are `CannotBound` today (I2 §0.3; RV1 B-1); the thermal identity is bounded | Every bend result |
| P-E: realized-bend authoring on the desktop (I2 §2) | All bend work |
| P-F: the re-pin cost of new kinds in T3's corpora and registered profiles (I3 §1.3; §3.3) | The cost of every later unit |

**What comes before it** (detail in §3.1):
- **T4-U0, exact-route hardening:**
  - pin the untested refusals;
  - replace the `.expect` hazard with a refusal;
  - v2 refuses negative pressure, as its readers already do.
- **T4-U1, the objective formation:** the bend term reuses the arc's thermal identity, which is exact only when the rigid motions lie in the null space (I2 §1.4).
- **T4-U1b, the arc load certificate:** without it a bend carrying weight cannot be Passed (RV1 B-1).
- **T4-U2a, the seam and the v3 identity:** this lets T4-U3 proceed in parallel.

T4-U0 and T4-U1 can start together (RV1 N-7). T4-U2's reference, design and authoring run alongside them.

**What the path does not yet show.**
- **Arc stress maximum:** until T4-U4 the case headline is withheld for cases with bends, as preview-physics-1 already does. Signed stress components at the arc stations are published.
- **Hoop on arcs:** the straight Lamé hoop is false on a torus (I1 P2), so T4-U2 withholds hoop and radial rows on arcs, with a named reason. T4-U4 publishes the toroidal value.

**Stop rules for the path.**
- **SP-1:** v2 cases must stay byte-identical, except T4-U0's declared refusal of p < 0, whose byte evidence follows T3's U3 form. Straight-only regions under v3 must give numbers bit-equal to v2's. Any other change stops the work. Straight members keep today's recovery formulas; the arc recovery form applies to arcs only (RV1 S-4).
- **SP-2:** if, after T4-U1 and T4-U1b, a pressurized bend case with weight at ordinary coordinates cannot reach Passed, stop. HELP_HUMAN then chooses between further certificate work with T3 and accepting Sensitive with disclosure.
- **SP-3:** a product–reference mismatch beyond 1e-9 relative in either mode goes back to the implementer. It never changes a reference, tolerance or scope.
- **SP-4:** if new kinds would re-pin T3's retained successor pins or the reader corpora, report the blast radius to HELP_HUMAN before re-pinning (T3's U3 rule).

## 3. Units, order and interfaces

### 3.1 Units

| Unit | Content | Depends on | Lane |
|---|---|---|---|
| **T4-U0** Exact-route hardening (small PR) | Pin the three untested refusals; replace the `.expect` in exact bend recovery with a refusal, and guard the straight-statics maximum against non-straight members; v2 refuses p < 0 by name (I1 §2); remove stale comments on the deleted radial treatment | T3's U3 merged | P |
| **T4-U1** Objective curved formation | See below | T3's U3 merged; T3's agreement (§3.3) | P |
| **T4-U1b** Formation certificate for load vectors on arcs | See below | T4-U1; T3's agreement (§3.3) | P |
| **T4-U2a** Admission seam and v3 identity (small PR) | Family-dispatching admission on the exact route, with a named refusal for every family not yet admitted. The v3 contract (H-1) and a `pressure-1` semantic table skeleton, added as a new file. The reviewed physics-1 table is not edited, because it is one of the `REVIEWED_INPUTS` and editing it would force re-registration (RV1 addendum). Reader dispatch on the new identity, with no new family yet | T4-U0; H-1 | P |
| **T4-U2** Pressure through realized bends (the first usable path) | See below | T4-U1, T4-U1b, T4-U2a | P |
| **T4-U3** Corrected joint, mechanical (the deletion PR, §6) | J-A and J-B on v3 documents: an FK connector primitive (`B`, `Ke = BᵀKB`, offsets, qref residual), span replacement, slot implementations, legacy refusal, connector authoring, deletion of the old element and its plumbing | T4-U2a; T3's agreement (§3.3) | J |
| **T4-U4** Bend and branch stress (M08, M14 bend part, M37, Q1) | See below | T4-U2 | P |
| **T4-U5** Joint pressure and tie rods (J-C, without an MPC) | `p(Ae−Ai)` at the joint attachments under the existing ledger; the connector as a region chain edge (`JointPressureParticipation`); elastic tie rods as elements; tie force rows | T4-U2, T4-U3 | J |
| **T4-U6** Section bases (M30) | Per D-5: a corrosion-allowance input; separate stiffness, mass, stress and pressure-load bases; MILLTOL re-frozen if its basis changes | T4-U2; D-5 | P |
| **T4-U7** Fittings and transitions | Reducers (the bore-change cap difference); tees (region trees and branch caps; `_INTERNAL_BRANCH` lifted); mitres and kinks beyond the tangency tolerance (the direction-change resultant). With T7 for component stiffness and SIF | T4-U2, T4-U5 | P/J |
| **T4-U8** Shear deformation (M31) | The straight Timoshenko mode to SHEAR_REFERENCE: stiffness, load equivalents, recovery and interior reconstruction changed together | T4-U4; D-6 | P |
| (T4-U9) | Bend opening and pressure-dependent k and i, only if the owner selects them (D-3) | — | — |

**T4-U1 in detail.**
- Form the arc from node differences d = xⱼ − xᵢ, the user's R and the plane normal. Take H from the actual chord, in the product and in the nonlinear-integration (SA) trace. Never form an absolute centre (I2 §1.6).
- Define the element mathematically, so that T3's K-D5 and W1c can re-form it.
- Remove the `bend_plane_orientation` requirement, which is never read, or make the solver consume it.
- For 0.4.0, give the bend its per-member E/ν and use the arc length for the fit (I1 §5.3 #12).
- T3 re-agrees its tests (§3.3). Ordinary-route arc values move at the rounding level; that change is declared.

**T4-U1b in detail.** Today any uniform load on a realized arc is `CannotBound` (`PP/src/formation_guard.rs:21,233-236`), which demotes the case. T4-U1b gives S11-G a certified defect for the arc's consistent load vectors. The recommended method re-forms the vector from its inputs in Wide precision, with the machinery K-D5 already uses for the arc's stiffness (`FK/src/structural/formation_check.rs:663-764`), and takes the exact difference. That difference becomes a bound only once the re-formation's own error is added. The certificate must meet SF-2's conditions (cond(F), cancellation, libm; T3's rulings, "S11-G after V1's S11G_CHECK"). The design is agreed with T3 before any code. This removes the availability loss that T3 accepted on the premise that realized bends are opt-in. D-2 makes them the normal bend under pressure.

**T4-U2 in detail.**
- **Contract and admission.** Realized curved bends are admitted through T4-U2a's seam. Geometry-only (chord) bends are refused anywhere on the exact route (D-2).
- **Chain topology.** Tangent-continuous chains. Small kinks within an engineering tangency tolerance are carried exactly by the remainder term (H-2); larger kinks are refused as mitres until T4-U7 (RV1 N-2).
- **Bend pressure.** The bend term and terminal caps along the end tangents (H-2). ε_p's own rounding enters the S11-G bound, or ε_p is formed in `Scaled` arithmetic as the straight path is. The element's A and the annulus' As are the same value (RV1 N-3).
- **Recovery.** On arcs, `N_w = N_el + pAi` and `S = N_el` at the ends and stations. The pressure family's end rows on arcs are published in the tangent frame, not the chord frame (RV1 S-7). Straight members keep today's formulas (SP-1).
- **Readers.** The three readers and the `pressure-1` semantic table.
- **Authoring (M02 minimal).** The applier and desktop write `mechanics_interface` and k. The region picker accepts a bend.
- **Validation.** The VP-STATIC `exact_pressure_1` transport and package, with the rebuilt cases (§5).

**T4-U4 in detail.**
- **Arc maximum:** a certified arc maximum, using an enclosure in the {1, cos θ, sin θ, θ cos θ, θ sin θ, θ} basis (I2 §3.3).
- **Toroidal hoop:** the toroidal membrane hoop at intrados, crown and extrados, plus the radial surface values.
- **Separate directions:** separate in-plane and out-of-plane fields for k and for the SIF; intensified bending on arcs and markers, never combined.
- **Q1 outputs:** transverse-shear stress (the Saint-Venant annulus) and signed fibre stresses.
- **Frames and signs:** one frame and sign convention for each remaining row family on arcs (I2 §3.4).
- **Algebra class:** each kind is marked with its algebra class for T6.

**Order.**
- **Lane P:**
  - T4-U0 and T4-U1 start together;
  - then T4-U1b and T4-U2a;
  - then T4-U2, the first usable path.
- **Lane J:** T4-U3 starts design and the slot table at once, and builds on T4-U2a. It no longer waits for T4-U2 (RV1 S-2).
- **Then:** T4-U4 and T4-U5 in parallel; then T4-U6, T4-U7 and T4-U8, as their decisions arrive.

### 3.2 Interfaces

| Tranche | What T4 gives | What T4 needs, or must not break |
|---|---|---|
| **T3** (retained precision; W1c; stress-recovery precision) | **T4-U1:** an objective, mathematically defined curved element that W1c and K-D5 can re-form. **T4-U1b:** a certified defect for arc load vectors. **Each pressure family:** term generation as a pure function from inputs to ledger terms, which W1 could call if T3 lifts P-4, plus a published per-member wall-force basis W1 can certify. **New stress quantities:** pure functions of section actions and section data, callable with retained inputs | Agreement on §3.3 before the owner sees the plan. The PP facade is serialized through main, and T4 rebases after each T3 merge. SP-4. T3's U3 merged before any T4 code |
| **T1** (load states) | Bend and joint terms take each member's resolved E/ν in 0.4.0 | Pressure stays per case, and per resolved state (I1 §4) |
| **T2** (hydrotest) | Pressure through bends and joints in exact and 0.4.0 cases. A member-wise ledger, so non-uniform (head) pressure can be added per member | T2 owns the head distribution, the contents mass state and the hydrotest state |
| **T5** (supports) | A ledger shared with the nonlinear loop. The connector's NI nonlinear slot stays fail-closed until T5 lifts the exact route's nonlinear refusal | — |
| **T6** (combinations, results) | The algebra class of every new kind. The pressure v2 and successor rows are linear in p; maxima and intensified measures are never combined. M08's combination-exclusion piece moves to T6 (T0's proposed split) | T6 implements exact-route combinations and the desktop comparison fix |
| **T7** (components) | The exact-route admission seam (T4-U2a) and the pressure ownership of reducers, tees and mitres (T4-U7) | T7 owns component stiffness, rigid and semi-rigid transfer, branch mechanics and SIF data |

### 3.3 What changes on T3's side, for T3's agreement

The exact list, with tests, lines and counts, is annex A, `PLAN_01/T3_AGREEMENT.md` (from T4-I5). It is ready for T3's WORKING_ITEMS.

**What does not change.** Neither T4-U1 nor T4-U3 changes:
- any output of the retained route or the source route;
- `REVIEWED_INPUTS`;
- `REGISTERED_PROFILES`, any priced atom, `PINNED_RECORD` or M, provided H-4 holds.

**`b2`.** There is no textual overlap with `b2` or its lanes.

**Pass B.** It still applies to both units.

**What T3 decides:**
- **T4-U1:**
  - the disposition of the M31b/M31b0 mutant, whose required kills (SA `kd5_tests.rs:419`, `:447`; PP `formation_check_runtime.rs:379`) stop being constructible or fail by design;
  - the outcome for `CSKEW_8_5`, which T4-U1 runs;
  - the regenerated `kd5_models` and model sets.

  No corpus pin moves if `preview_physics::LIMITATIONS` stays unchanged.
- **T4-U1b:** the certificate design. S11-G's T15 changes meaning.
- **T4-U3:**
  - whether T3's W4 tie reduction stays. The recommendation is to keep it and delete only the old element's tie producer. Deleting the reduction would regenerate most of FK's K5 vectors;
  - the deleted and rewritten tests.
- **H-4:** the wave for the renames (§4.2).

## 4. Design questions

### 4.1 The owner's decisions

**D-1. Approve this plan.**
- What is being approved: the order in §3.1, with the first usable path of §2, and the corrected joint (T4-U3) in a parallel lane.
- Recommendation: approve.

**D-2. Pressure through bends: realized bends only?**
- **Option (a):**
  - Only realized curved bends can carry pressure. Each carries the user's flexibility factor k; k = 1 means no extra flexibility.
  - Today's default geometry-only bend, which the solver treats as a straight chord, is refused on the exact route with a "realize this bend" message. It remains available on the pressure-free route.
- **Option (b):** also admit geometry-only chord bends under pressure, through kink resultants. This is quicker for users, but such a bend has no flexibility, so its thermal and pressure response is stiffer than the real bend.
- **Evidence:** I2 §2 (geometry-only is a chord, and k is unused); I1 §5.
- **Recommendation: (a).**
  - The exact route's claim stays physically honest.
  - k is user data, and agents do not populate it.
  - Mitres and real kinks come in T4-U7.
  - T4-U1b removes the Sensitive standing that realized bends carry today.

**D-3. Effects T4 leaves out for now.**
- **What T4 includes:**
  - static internal pressure;
  - pressure elongation with the Poisson term, on straights and bends;
  - closure caps;
  - the bend's membrane wall load.
- **What T4 leaves out, stated as limits on every bend result and in the v3 approximation text:**
  - steady-flow momentum and transient loads at changes of direction: only static pressure is modelled (RV1 S-5);
  - bend opening under pressure (rotational Bourdon). It includes the circumferential variation of hoop and Poisson strain. The Poisson term on the arc uses the straight Lamé mean, which is the correct area-weighted mean for a thin torus (RV1 S-5);
  - the pressure reduction of the bend's flexibility factor and SIF (pressure stiffening);
  - ovalization.
- **A workaround:** a user who needs pressure-corrected k or i enters corrected values.
- **Options:**
  - (a) leave them out now and offer T4-U9 later;
  - (b) include them in T4. That needs shell-level references, which the repository does not have (I4 §4), and pressure-dependent k changes the stiffness per case (I1 P5).
- **Recommendation: (a).**

**D-4. Legacy joints.**
- **The question:** refuse both legacy populations (I3 §5) with `LEGACY_FINITE_CONNECTOR_REAUTHOR_REQUIRED`? The two populations are:
  - (i) the flexibility joints already refused;
  - (ii) app-authored joints, which have no mechanics interface and today silently solve as ordinary pipe with only a warning.
- **Under this recommendation:**
  - an explicit "annotation only, analysed as pipe" choice (`not_solver_consumed`) stays, disclosed on every result;
  - the corrected joint exists only in exact-contract (E/ν) documents, because no other version can hold it (I3 §0.3);
  - nothing is converted automatically (§6).
- **Recommendation: yes.** It matches the owner's "don't maintain the flawed code or compatibility with it", and JR §3.

**D-5 (needed before T4-U6). Section bases (M30).**
- **Today:** one basis, wall minus mill tolerance, serves stiffness, mass, stress and the pressure load path. There is no corrosion-allowance input (I2 §3.2).
- **Recommendation:**
  - stiffness and mass on the nominal wall;
  - stresses published on both the nominal and the reduced section (minus mill tolerance and a new corrosion-allowance input), each labelled; the user's rule pack picks the basis;
  - the pressure load path named separately: Ai for the caps from the bore of the reduced wall (internal corrosion enlarges it), and As for ε_p from the same section as the stiffness (RV1 N-5).
- **Effect:** every exact number changes deliberately.

**D-6 (needed before T4-U8). Shear deformation default.**
- **Recommendation:** Timoshenko, with the energy-matched annular factor, as the exact route's default. Euler–Bernoulli stays available by explicit selection.
- **Effect:** results change for short, stubby members.

### 4.2 HELP_HUMAN's rulings, within delegated authority

**H-1. Contract identity.**
- A successor model contract, `3.0.0/exact_pressure_v3`, publishes under the reserved `pressure-1` result semantics. It grows family by family (bends in T4-U2, joints in T4-U5, fittings in T4-U7). Each admitted family is named in the result's formulation evidence.
- `2.0.0/exact_straight_pressure_v2` stays accepted and byte-identical, because it is straight-only and not flawed. The one exception is T4-U0's declared refusal of p < 0.
- New authoring writes v3.
- Extending v2 in place is rejected: its name, approximation text and the readers' pins all say "straight" (I1 §3.2).

**H-2. The pressure ledger for bends and joints.**
- **Keep** today's pre-cancelled ledger, unchanged: physical caps only at transferring terminals, Poisson pairs per straight member.
- **Add member-owned terms:**
  - a realized bend contributes `K_b·u_free(ε_p) − c_b`, where:
    - `ε_p = (1−2ν)pAi/(E·As)`;
    - `u_free` is the free-expansion field the arc's thermal path already uses;
    - `c_b = [−pAi·t_i, +pAi·t_j]` is the bend's own outward end-cap pair, with t in i→j travel;
  - at each interior node next to a bend, the remainder is the sum of the incident members' outward caps. That is `+pAi(t_in − t_out)` in traversal order, independent of member orientation. It is the physical kink force, and it is zero for exact tangency;
  - a joint contributes `p(Ae−Ai)` at its attachments (JR's representation B).
- **Recovery on arcs** is `N_w = N_el + pAi` and `S = N_el` along the end tangents. At each station the wall force is the elastic force plus `pAi`, and M and V are elastic only. Straights keep today's formulas.
- **This reverses JR's choice of representation A, which JR itself permits ("two equivalent… one selected implementation owner").** The reasons:
  - it keeps the verified straight path and its exact sums bit-for-bit (SP-1);
  - it keeps bend terms boundable;
  - it avoids re-pins of the corpora.
- **T4-RV1 derived the bend term independently and checked it in arithmetic** against three other formulations: an explicit wall-load integration, `Σ K_m·u_free(ε_p)`, and a polygon of straight segments with kink forces. Agreement was 1e-13 to 1e-15 (RV1 §1).

**H-3. Which PR lands the corrected joint.**
- T4-U3, the live mechanical connector (J-A and J-B), carries the deletion.
- Pressure thrust and tie rods follow in T4-U5.
- J-A alone has no production use, so it cannot "land the corrected joint" (I3 §0.7).

**H-4. Re-pins the deletion can avoid.**
- Keep the summary key `component_user_stiffness_macro_element_count`; it also counts curved bends. Keep the historical joint row kind for reading old results.
- **Rename or remove both in the corpus generation that carries T3's deferred wording of `preview_physics.rs:75`:** PR-B2's re-pin wave, if T3 judges it cheap there; otherwise B7. This keeps one wave, not two, and follows HELP_HUMAN's precedent for T3's U3 published text.
- **The renames do not depend on T4-U3** (I5 §0.7). The key also counts curved rows, and G11 already refuses every flexibility joint. So T4-U3 lands with no re-pin.
- **The radius once `b2` merges** is 92 files, including 10 successor pins and 07n, plus 10 reviewed semantic contracts. Removing the row kind therefore needs a registration, which SQ2 (before PR-B2) or B7 provides.
- **Any other change to `preview_physics::LIMITATIONS`** joins the same wave. An example is T4-U4's frame unification for arcs on preview-physics-1.
- **What this avoids:** an 88-file re-pin and a profile re-registration in T4-U3 (I3 §1.3).

### 4.3 Design choices made within authority (recorded)

1. **Hoop and radial stress on arcs.** They are withheld in T4-U2 with a named reason, then published in T4-U4 as a new toroidal-membrane kind with the radial surface values. `pipe_lame_hoop_stress_v2` is never published on an arc.
2. **Signed pressure.** v2 refuses p < 0 at the producer, as its readers already do; v2's byte-identical limitation text cannot carry a collapse disclosure (RV1 N-8). v3 admits signed pressure, with the stated limitation that external-pressure stability and collapse are not assessed.
3. **Rebuilt validation.**
   - Each rebuilt case gets a new id that records the retired id it rebuilds. Retired ids stay retired.
   - The rebuilt cases live on PP's public entry and in the VP-STATIC package. The pressure arithmetic is not re-added to the PP-free benchmark crates, which would fork it (I4 §0.3).
4. **Joint slots (I3 §1.4).**
   - Implement: dense, sparse and NI-linear assembly; the S11-G edge; K2b scaling; K-D5 Wide<2> re-formation of BᵀKB, so that joint cases are not demoted.
   - Fail closed: NI nonlinear and strict-gap (unreachable until T5); retained and source recovery (until T3-F2b).
   - Delete the old element's W4 tie producer (`user_element_tie`, `TieRefusal`, SA's `UserTie`). T3's tie reduction itself stays, unless T3 chooses to delete it (§3.3).
5. **Ties.** Elastic rods, as elements, come in T4-U5. Ideal ties need a multipoint constraint, which is a later unit only if users need it. No penalty stiffness is used.
6. **Negative controls for the deleted element** are analytical values in the references: JR's raw-difference numbers. No code re-implements the old element.
7. **NI's four friction tests** move to an ordinary frame coupling, with independently re-derived expectations (I3 D9).
8. **Code placement.** New PP modules for the admission seam, bend pressure and connectors, and an FK `connector` module. Edits to PP `lib.rs` are kept to call sites, to limit facade conflicts with T3.

## 5. Validation per unit

All VP-STATIC references are independent: derived and frozen by a TASK that did not write the code, refuted by a second TASK before the code is read, and run in both solver modes at relative 1e-9 with explicit zero-scale floors (I4 §5).

| Unit | VP-STATIC (independent) | VP-PUBLISHED / VP-SOURCES | Negative controls |
|---|---|---|---|
| T4-U0 | Pin the refusals | — | A bend in an exact model is refused, not a panic; negative pressure under v2 is refused by name |
| T4-U1 | Rigid-mode null space and rotation invariance at X = 0, 5e5, 2e6, 5e6 and 7.3e6 m; translation equality of K; T3's four recorded Passed breaches no longer breach; K-D5 re-formation within criterion; the radius-refusal column of I2 §1.4 reduced to zero | SSLL101 (Hovgaard, assembled bend system with k): formulation-matched only where reduced inertias and shear agree (I4 §4). Otherwise recorded as not matching | The formula-chord mutant demotes; a large-coordinate control added to the CB tests |
| T4-U1b | Self-weight and other uniform loads on arcs at ordinary and UTM coordinates publish Passed, with the certificate's defect within criterion; S11-G's T15 (`s11g_tests.rs:1747`) re-agreed with T3 | — | A perturbed vector is demoted; a vector without a certificate stays `CannotBound` |
| T4-U2a | Each not-yet-admitted family refused by name; v2 cases byte-identical, except T4-U0's declared p < 0 refusal; a straight-only v3 case bit-equal to its v2 twin | — | An unknown family; a v3 result read as v2 |
| T4-U2 | See the case list below | No formulation-matched published case exists for pressure on bends. SSLL106's pressure assertions have no closure ledger and carry a sign mismatch (I4 §0.6), so they are excluded with that reason. VP-SOURCES: the load-path sources already qualified (Abaqus and Ansys pressure end-load bookkeeping; AISI/STI) | See the case list below |
| T4-U3 | JR J1 and J2; the B oracle; the six rigid modes; offsets; preload; coupled H; reversal; the finite-rotation value; the formerly unbalanced invented demo joint (658.44 N·m) now balancing within criterion | JR SOURCE_QUALIFICATION | Raw-difference values (240 N, .36 J) as analytical expectations; legacy refusal on PP, the headless runner (both modes) and native; an annotation-mode joint not refused |
| T4-U4 | STRESS_REFERENCE S1, S2 and I1 (directional SIF); the arc maximum against an analytic trigonometric extremum and a dense-sampling bound; the toroidal membrane hoop (thin shell) in closed form; the Saint-Venant annular shear field (SHEAR_REFERENCE refutation :75-80); signed fibre stresses at declared fibres; end and cut sign consistency | SSLL106 subsets for axial, torsion and pure moments (straight stress) | The component abs-sum (9 MPa vs 7); k multiplying stress; a combined intensified row |
| T4-U5 | JR J3: five configurations, plus the thermal anchored relation | — | J4 double count, inspecting the tie force (`800+75π` vs `800−50π`), not only reactions |
| T4-U6 | The same model on each basis: stiffness, mass, stress, pressure-load areas; MILLTOL re-frozen | — | Mill tolerance leaking into stiffness |
| T4-U7 | The reducer cap difference `p(Ai₁−Ai₂)`; the tee branch cap; the kink resultant; equal-bore cancellation | — | A double-counted interface cap |
| T4-U8 | SHEAR_REFERENCE: cantilevers, the distal half-load control (53/384 vs 54/384), the interior spring, the slender limit | SSLL106 transverse cases, which are Timoshenko | Stale Euler–Bernoulli load equivalents |

**T4-U2's cases.** These are T4's new VP-STATIC transport `exact_pressure_1` and package, on T1's `load_reference_1` pattern. The gate's Python tests run only in DEC-025, so each run is recorded (I4 §0.8).

**The references must not presuppose the equivalence under test (RV1 S-3):**
- at least one reference integrates the arc's wetted-wall load `pAi/R` and the Poisson eigenstrain directly, by unit load;
- a polygon-limit control at k = 1 replaces the bend by straight segments with kink forces and uses no curved element;
- `Σ K_m·u_free(ε_p)` and the thermal analogue are cross-checks only.

T4-RV1's check script (`WT/scratch/t4_RV1/h2_check.py`) may seed the reference TASK. It is not a frozen reference.

**New closed forms:**
- **Free closed L-bend:**
  - zero reactions;
  - `N_w = pAi` and `S = 0` everywhere;
  - M = 0;
  - self-similar growth by ε_p.
- **Anchored L-bend and U-loop:** reactions and moments from the direct wall-load integration, with `N_w = S + pAi`. Equality to the thermal problem with strain ε_p is a cross-check.
- **The same with:**
  - a separately supported closure at one end;
  - added thermal strain and self-weight;
  - k = 1 and k = 2.
- **Rotation and translation to UTM scale;** mm/MPa normalization; 0.3.0 and 0.4.0 documents.

**Negative controls:**
- the bend term omitted, which leaves a residual of `−pAi(t_in − t_out)` from the bend's own tangents;
- c_b added instead of subtracted;
- caps subtracted in recovery;
- the Poisson term missing on the arc;
- the wall load counted both in the station statics and in the `+pAi` membrane;
- a slightly non-tangent bend, which must remain balanced.

**Rebuilt cases:**

| Retired case | Rebuilt as | What changes (I4 §2) |
|---|---|---|
| `MECH-CURVED-BEND-PRESSURE-THRUST-ARC` (removed) | An anchored–free quarter bend under E/ν | Tip ×(1−2ν). New rows S = 0 and σz. k-independent |
| `STRESS-TP-PMM-P3-MILLTOL-EFFECTIVE-WALL-STRESS`, membrane values | Exact-route Lamé surface values plus σz, free and restrained, on the current basis | Re-frozen in T4-U6 if D-5 changes the basis |
| MECH-TP-PHYS-008/009, pressure halves | A new annular exact case: pressure plus thermal plus a partial-span transverse load, with mixed restraint | The pressure term is wall tension 2νP, opposite in sign to thermal |
| `STRESS-PRESSURE-MEMBRANE-ORIGINAL` (also removed by T3's U3; I4 §0.1) | A Lamé case with a thin-wall-limit comparison | Thin-wall values become Lamé values |

## 6. The corrected-joint PR (T4-U3)

**Scope.** T4-U3 contains:
- an FK connector primitive (J-A);
- its live topology and authoring on v3 documents (J-B), including:
  - `replaces_span`, which removes the named span from every assembly and recovery path;
  - blocking of the replaced span's loads that have no owner;
  - a typed `ObjectiveConnectorV1`, with Q, offsets, H and Ls, and the calibration descriptor;
  - `JointPressureModel = unpressurized`;
  - hardware `untied` only.

A pressurized model containing a joint is refused with `JOINT_PRESSURE_INTERFACE_UNRESOLVED` until T4-U5.

**Deletion.** T4-U3 deletes, with no historical copy:
- FK `user_stiffness_local_matrix`, `UserStiffnessElement` and its assembler API;
- the census, scaling, formation-check, sparse, NI and SA plumbing;
- PP's builder, gate, validation and review rows;
- the element's W4 tie producer (the reduction itself stays, unless T3 chooses otherwise; §3.3);
- the tests that pin the old element.

The work is about 38 Rust files and roughly 1,950 enclosing lines, plus about 300 in TypeScript (I3 §1.2; RV1 §3). Each of the 15 solver slots is implemented or fails closed, per §4.3 item 4. The slot table is agreed with T3's WORKING_ITEMS before any code.

**The refusal design.**
- **Recognition.** A legacy joint is an `expansion_joint` with no `objective_connector`, carrying `expansion_joint_pipe_ref` and/or the four scalar rates. That covers both of D-4's populations. An explicit `solver_consumption = not_solver_consumed` is exempt (RV1 S-6).
- **The code.**
  - One blocking `LEGACY_FINITE_CONNECTOR_REAUTHOR_REQUIRED`, with refs `[component, pipe]`.
  - It replaces `JOINT_ELEMENT_STIFFNESS_INCOMPLETE`, `_MAPPING_UNRESOLVED`, `_EQUILIBRIUM_UNQUALIFIED` and `EXPANSION_JOINT_MACRO_ELEMENT_INPUT_INVALID` for legacy joints.
  - It is reported before `EXACT_PRESSURE_COMPOSITION_UNSUPPORTED`.
- **The message.** It names the component and the pipe, and states that a four-rate finite-span joint is neither solved nor converted. It lists what to author: the frame and attachments, a 6×6 work matrix with its basis, the topology, the hardware and the pressure model.
- **Where it applies.**
  - Every route, through PP's single gate.
  - The headless runner, in both modes, and native, each with tests.
  - Readers need no change, because codes are free strings.
- **Authoring.** Legacy joint creation is replaced by connector creation on v3 documents. On 0.1.0/0.2.0 documents only the annotation mode is offered.
- **Documents.** They stay readable, editable and saveable. Nothing is migrated.

**Evidence.**
- Byte evidence follows T3's U3 form: equal except the declared codes and texts. No admitted model's published output changes (I3 §1.1).
- Published texts that name the old element are corrected under the published-text rule: NI's assumption and limitation strings, and the joint validation text.
- Their blast radius is reported (SP-4).

**Gates.** T4-U3 needs the full T3 gate set, because it changes solver crates:
- independent review;
- hosted CI and the dual-viewport dispatch;
- DEC-025;
- T9 and the both-entry gate;
- the fixture stop rule.

**Reviewers.** Two reviewers:
- one for the connector mechanics against JR;
- one for the slot table and the T3 interfaces.

## 7. Reviews, effort and risks

**Reviews.** Each unit gets three independent reviews:
- a reference refutation, before code;
- a complete-diff review on the actual candidate;
- a T3-interface review where it touches formation, the ledger, the readers or the registered profiles (T4-U1, T4-U1b, T4-U2a, T4-U2, T4-U3, T4-U5).

T4-U2 also gets a three-reader parity review, built on a shared generated corpus case for each new shape. A reviewer confirms the repairs of its own findings.

Further gates:
- hosted CI, plus the dual-viewport dispatch wherever the desktop changes;
- DEC-025, scheduled with T3 through the exclusive lock;
- T9, the both-entry gate and Pass B where formation, the kernel or files on T3's D1 call graph change (T4-U1, T4-U1b, T4-U3);
- the native witness on the owner's Mac for T4-U2 and T4-U3.

Reviewer IDs continue from T4-RV2.

**Effort.** Implementer-days, without and with gates and review rounds. The figures for T4-U2 and T4-U3 are lower bounds (RV1 S-8).

| Unit | Days (work) | Days (with gates) | Unit | Days (work) | Days (with gates) |
|---|---|---|---|---|---|
| T4-U0 | 1 | 2–3 | T4-U4 | 6–8 | 10–14 |
| T4-U1 | 2–4 | 5–8 | T4-U5 | 3–5 | 6–9 |
| T4-U1b | 3–5 | 6–10 | T4-U6 | 3–4 | 5–7 |
| T4-U2a | 2–3 | 4–6 | T4-U7 | 4–6 | 7–10 |
| T4-U2 | 8–12 | 14–20 | T4-U8 | 3–5 | 6–8 |
| T4-U3 | 10–14 | 16–24 | | | |

- **Total:** about 45–65 work-days.
- **Calendar, with two lanes and gates:** the first usable path in about 4–6 weeks; T4 complete in about 10–14 weeks.
  - The 4–6 weeks assume that T4-U2's reference, design and authoring overlap T4-U1 and T4-U1b, as §2 describes.
  - Run in series, the critical path T4-U1 → T4-U1b → T4-U2 takes 25–38 working days.
- The calendar stretches if the shared host's gates or T3's agreements queue.

**Risks and stop rules.**

| Risk | Stop rule or mitigation |
|---|---|
| R1: PP facade and corpus collisions with T3 (lib.rs; `REGISTERED_PROFILES`) | New modules; serialization through main; SP-4 |
| R2: bend results demoted to Sensitive (S11-G, K-D5) | T4-U1 and T4-U1b first; the thermal-identity formulation; SP-2 |
| R3: contention for the host's DEC-025 and exclusive gate | If the gate queue holds a T4 PR for more than 2 days, raise it with HELP_HUMAN |
| R4: drift across three readers, and collisions with T3's reader lanes | A shared corpus case for each new shape, which every reader must pass before expansion. Reader edits rebased on T3's lanes as they merge |
| R5: T4-U3's size (15 slots, about 38 files) | Agree the slot table first; commits by slot family; two reviewers |
| R6: no published reference for pressure on bends | Direct wall-load integration and a polygon limit in the references; the gap stated, not filled by tuning |
| R7: later deliberate value changes (D-5, D-6) | Re-freeze the references deliberately; never loosen them |
| R8: T3's U3 not merged, or changed late | T4 code starts only from main after T3's U3 merges. Design, references and authoring prototypes may start now |
| R9: the latency of T3's agreements (K-D5 and M31b re-derivations, S11-G T15, W4) | The agreements are sought now (§3.3). If one is not given within 3 working days of a unit's design freeze, raise it with HELP_HUMAN |

**Blocking.** Three things block, and nothing else does:
- T3's U3 merge to main, before any T4 code;
- D-2 to D-4 and H-1 to H-3, before the design freeze of T4-U2a, T4-U2 and T4-U3;
- T3's agreement on §3.3.

## Evidence

| Record | sha256 |
|---|---|
| `R4/T4-I1/RETURN.md`: the exact pressure surface | `f3c200341970545ac4fb0c46fc2b29a346ede869dd19494476b10071d4fd9d63` |
| `R4/T4-I2/RETURN.md`: the curved element and stress recovery | `7111e8435dbc73a69ba6a4cba817c90f5eae814c7fa736f58df87c4c02febfe3` |
| `R4/T4-I2/_run_records/centre_probe.py` and `.stdout.txt`: the centre emulation | `d3ec681d…`, `c709a1ed…` |
| `R4/T4-I3/RETURN.md`: the joint and the deletion PR | `4a6699d33aa21ff848d215d2313aa5331d6ac4a0e9f386edc57b9c04aa87d0f7` |
| `R4/T4-I4/RETURN.md`: the validation inventory | `f14555a0ced9686ceaed60632f9475d8ed784b4f355082231d20e9a3ee931439` |
| `R4/T4-I5/RETURN.md`: the T3 side | `4bc9deb361840b500bcede17c082257ab610767a05fcc4c8a316d1688418320b` |
| `R4/T4-RV1/REVIEW.md`: the independent review of revision 1 (BLOCKING on B-1; physics of H-2 confirmed) | `3d38f6cba4e81b400fb887acbfae842313cd624018a9fb3c0eb706468ac930c3` |
| `R4/T4-RV1/ADDENDUM_01.md`: the delta check of revision 2 (CONFIRMED; OI-1 fixed in this revision) | `3c5d759842d961ef057f756b14ec37b63492b06c0ba79c51cac77c249c0248b2` |
| Briefs: `R4/BRIEFS/T4-I1…I5_*.md`, `T4-RV1_PLAN_REVIEW.md` | `d59f1249…`, `bfa43d8f…`, `2640d67a…`, `7e8808e9…`, `f6f77d1d…`, `aa943caf…` |

**This plan's annexes:** `PLAN_01/T3_AGREEMENT.md` (annex A, the T3 side, for T3's WORKING_ITEMS) and `PLAN_01/RV1_DISPOSITION.md` (the dispositions of T4-RV1's findings).

**Prior design read:**
- `I/CORRECTNESS_DESIGN/`: `PRESSURE_INTEGRATION.md`, `PRESSURE_REFERENCE_QUALIFICATION.md`, `STRESS_REFERENCE.md` §1–4 and §8–9, `RESULTS_AND_COMBINATIONS.md`, `JOINT_REFERENCE/{CONTRACT,RETURN}.md`, the head of `INDEPENDENT_REFUTATION`, `SHEAR_REFERENCE/RETURN.md` and `VERSION_RESERVATION_V2.md`;
- `I/T0_REASSESSMENT/RETURN.md`: M01, M08 and M14;
- `I/DEFAULT_ROUTE_DESIGN/ROOT_SELECTION.md`;
- `I/OWNER_SIF_DECISION_2026-09-26.md`;
- T3's rulings of 2026-10-08 and 2026-10-09, from the NUM branch.

**Wider consultation:** none beyond this role's brief.
