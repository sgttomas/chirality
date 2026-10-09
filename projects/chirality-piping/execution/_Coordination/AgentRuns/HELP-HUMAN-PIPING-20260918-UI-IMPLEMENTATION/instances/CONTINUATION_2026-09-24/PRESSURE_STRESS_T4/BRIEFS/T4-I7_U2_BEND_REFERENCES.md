# T4-I7: independent references for T4-U2, pressure through realized bends (freeze)

**Terms:** `R4/BRIEFS/T4_WI_COMMON.md`. Your ID is T4-I7.

**Purpose.** T4-U2 is the first usable path: an L line (straight, realized bend, straight) under pressure, weight and temperature, published under `3.0.0/exact_pressure_v3` (H-1). You freeze its independent VP-STATIC references, before any code exists; a second TASK will refute them. Read plan §2, §3.1 "T4-U2 in detail", §4.2 H-2, §5 (the T4-U2 row, "T4-U2's cases", new closed forms, negative controls, the CBPT row of the rebuilt cases), D-3; I1 §1 and §5; I4 §2.1, §4 and §5; RV1 §1; `I/CORRECTNESS_DESIGN/PRESSURE_REFERENCE_QUALIFICATION.md` §1–3.

**Independence (plan §5, RV1 S-3).** The references must not presuppose the equivalence under test.
- The reference values come from a direct method: the flexibility (unit-load) method over the whole line, with the arc's wetted-wall load pAi/R along the outward normal, the terminal caps, the Poisson eigenstrain −2νpAi/(E·As), thermal strain and self-weight integrated directly, and redundants solved for the anchored cases. No stiffness matrix of the curved element and no K·u_free.
- A polygon-limit control at k = 1: the bend replaced by n straight segments with kink forces, converging to the reference (report n and the convergence).
- Σ K_m·u_free(ε_p) and the thermal analogue are cross-checks only. `WT/scratch/t4_RV1/h2_check.py` may seed your work; it is not a reference.
- You may read the product to learn conventions (DOF order, frames, station names, how a document states self-weight, gravity's direction, the section rule from OD and wall − mill tolerance), but not to obtain values.

**Formulation to match.** Euler–Bernoulli straights; the arc with axial and torsion energy and in-plane and out-of-plane bending energy scaled by the user's k (no shear); small strain; static internal pressure only (D-3's exclusions: no flow momentum, no Bourdon opening, no pressure stiffening, no ovalization). On arcs N_w = N_el + pAi and S = N_el along the tangent; M and V elastic. Straight members keep today's recovery (N_w = N_mech + 2νpAi, S = N_mech + (2ν−1)pAi; membrane N_w/As; Lamé surface values).

**Cases** (each with complete inputs: geometry, OD, wall, mill tolerance, E, ν, α, temperatures, density or w, gravity, p, k, supports, terminal closures):
1. Free closed L (one end anchored, the other free, both terminals `transfers_to_wall`): zero reactions; N_w = pAi, S = 0, M = 0 everywhere; growth by ε_p.
2. Anchored L (both ends anchored), and a U-loop.
3. Each of 1–2 with: a `separately_supported_or_compensated` closure at one end; added thermal strain; added self-weight; all three together in one case; k = 1 and k = 2.
4. The rebuilt CBPT (`MECH-CURVED-BEND-PRESSURE-THRUST-ARC`): an anchored–free quarter bend under E/ν, k = 1 and 2, with a new case id that records the retired id. Give its old and new tip values.
5. Each core case rotated to a skew orientation and translated to X = 5e6 and 7.3e6 m; and in mm/MPa units.

**Quantities.** Node displacements and rotations; six-component reactions at every support; at arc ends and at arc stations (fractions 0, 1/4, 1/2, 3/4, 1 of the included angle, and the product's own station names) N_w, S, V, M in the tangent frame (x tangent, y inward, z normal), membrane stress N_w/As; on straights the product's five stations with today's rows. State frames and signs exactly (end rows as node-on-element; station rows as the j-side cut action; check today's conventions in I2 §3.4).

**Negative controls.** For each, the discriminating values a test asserts the product does not produce: the bend term omitted (residual −pAi(t_in − t_out)); c_b added instead of subtracted; caps subtracted in recovery; the Poisson term missing on the arc; the wall load counted both in station statics and in the +pAi membrane; and a slightly non-tangent bend (for example 1e-3 rad), which must stay balanced with the interior remainder.

**Criteria.** Relative 1e-9 in both solver modes, with an explicit absolute zero-scale floor per quantity derived from the case's scale (I4 §5).

**Transport.** Values go in `u2_reference_cases.json` (decimal strings, at least 17 significant digits), shaped so a later `exact_pressure_1` package on T1's `load_reference_1` pattern can consume them (`P/validation/qualification/fixtures/load_reference/`, `PP/tests/fixtures/load_reference_states/reference_cases.json`). Add 0.3.0 and 0.4.0 document sketches per case, marked provisional where they depend on v3 fields T4-U2a defines.

Write `U2_REFERENCE.md` (derivations, conventions, cases, limits; at most about eight pages) and a one-page `RETURN.md`.
