# T4-RV4: refutation of T4-I8's rebuilt straight references (T4-U2)

- **Role:** independent reviewer, TASK (Type 2), for T4's WORKING_ITEMS. Brief `R4/BRIEFS/T4-RV_REFERENCE_REFUTATION.md` (sha256 `816c20ab…12db`); terms `R4/BRIEFS/T4_WI_COMMON.md` (sha256 `7d44afd0…02cb`).
- **Object:** `R4/T4-I8/` at `61b4e0b460`. SHA256SUMS digest `8246ea4e…2d6`; all seven entries verified OK before reading.
- **Basis:** plan revision 2 (§2 SP-1, §4.3 item 3, §5), `R4/T4_RULINGS.md`, I4 §2 and §5, code at `ed012c7ccf` (conventions), retired cases at `ec5d397359`, T1's package at `ed012c7ccf`. No product build, run or output was used.

## Disposition: PASS WITH FINDINGS

No BLOCKING finding. Every load-bearing value of cases 1–3 (all 690 rows) is reproduced **exactly** by a different method, and the conventions match the product at `ed012c7ccf`. The findings below are four SHOULD-FIX items (one transport defect, one missing re-freeze condition, one mis-aimed negative control, the twin's SP-1 record) and five NOTEs. None of them changes a frozen value. No stop rule (SP-1 to SP-4) or T3 condition is touched. S-2 interacts with SP-3 later, at T4-U8.

## 1. Checks performed (facts)

| Check | Method | Result |
|---|---|---|
| Reproduction | T4-I8's two scripts re-run (Python 3.13.14, `-I`) on the fixture extracted at `ed012c7ccf` (sha256 `7e51ecb3…1ab1`) | JSON and both stdouts byte-equal |
| Lamé, Nw, S, σz, extension (cases 1–3, all states) | Generalized plane strain in Lamé constants (u_r = Ar + B/r, uniform ε_z, thermal via (3λ+2μ)αΔT), boundary conditions solved by Cramer's rule in exact rationals. This replaces T4-I8's Hooke compliance with C = P/As | Exact equality, every station and member |
| Section | I = π(ro⁴ − ri⁴)/4 and As = π(ro² − ri²) directly | Exact |
| Case 2 transverse | Unit-load integrals ∫M·m/EI (exact piecewise polynomials) for uy and rz at B, C, D; V and M by load integration | uy(D) = −1701/(137560π), rz(D) = −351/(137560π); every station and end row exact |
| Reactions | Nodal free bodies with the cap ledger (−P at A, +P at the far terminal); whole-pipe equilibrium for Fy and Mz | Exact. Combined-case magnitudes within 1e-15 |
| Retired 009 witness | Same unit-load code at q = −2 N/m, EI = 2000 | −0.070875 m, −0.014625 rad (hand calculation reproduced) |
| Thin-wall comparison | Recomputed, plus the mean hoop from ∫σ_h dr/t of the Lamé field | −1/145, 23/121, 1/11, 23/121 exact |
| Twin fixture | 20 values plus the normal maximum, re-derived by a second route (unit-load cantilever; I from radii) from the binary64 inputs | All binary64-identical to the fixture |
| Rows both ways | Each T4-I8 row is recomputed from (kind, entity, component, location), and each independent row is looked up in T4-I8's set | 2139 checks, 0 failures; row sets identical (80/86/222/222/80) |
| Hygiene | grep for absolute, home, temp and machine paths | None; placeholders only |

## 2. Independence and formulation match

**Independence.** No value was taken from the product. The twin's values come from an independent frozen fixture whose method states "no product import or observed output as oracle". The straight physics is derived from 3D compliance, not from the product's Poisson-pair ledger, and my generalized-plane-strain solve confirms it from 3D elasticity. The conventions (section rule, stations, signs) were read from code, which the brief permits.

**Conventions at `ed012c7ccf`, verified against code:**

| Row family | Product | Reference |
|---|---|---|
| Section | t_eff = wall − mill tolerance; the exact annulus is built from OD and t_eff, with Ai from the reduced bore (`lib.rs:10213-10230, 7245-7258`) | Same |
| Nw, S, σz, Lamé (five stations) | From the negated i-side helper at s; 2νP added in recovery; caps never subtracted (`lib.rs:11518-11590`; `source_geometry.rs` `recover_wall_effective_membrane`) | Uniform values, tension-positive |
| `pipe_wall_endpoint_action_v2` | end_i = −Nw, end_j = +Nw (`lib.rs:5042-5043, 11512-11517`) | Same |
| Transverse end rows | Node-on-element K_e·u − f_eq (`lib.rs:5076, 11100-11180`) | end_i = −(V, M)(x_i); end_j = +(V, M)(x_j) |
| Transverse stations | The i-side sum, negated: the action of the j-side part on the i-side segment (`lib.rs:10321-10331`; `straight_pipe/src/lib.rs:1049-1090, 1501-1530`) | V(x) = ∫ₓᴸ q ds; M(x) = ∫ₓᴸ (s − x) q ds |
| Displacements and rotations | Global; translations ×1000 into mm; rotations in rad, right-hand (`lib.rs:11182-11260`) | Same; the reference is in m with `m_to_mm` |
| Reactions | Support-on-pipe, global; only restrained slots are filled, the rest are +0.0 (`lib.rs:4806-4849, 11400-11422`) | Same |

A correct product passes these references. Each reasonable wrong product I considered (by the discriminator values and by arithmetic, not by running code) fails at least one positive row by more than 1e6 criteria: arc recovery applied to straights; the Poisson term omitted or reversed; caps subtracted; caps at interior chain nodes; the mill slot ignored; the i-side station sign.

## 3. The five points I was asked to attack

1. **The 009 chain is sound and forced.** On forced: `PreviewPrimitiveLoad` and `LoadTargetInput` have no extent field (`lib.rs:687-703`), partial extents exist only for wind `exposed_spans` (`lib.rs:639`), and the exact route refuses `equivalent_static` (`pressure_runtime.rs:227`). On sound: the chain keeps the four things 009's pressure half tested:
   - one solve that combines caps, Poisson pairs, thermal pairs and a distributed load;
   - recovery on a member that carries all of them (B-C);
   - the mixed restraint (anchor plus UX stop);
   - the loaded interval [0.25 L, 0.75 L], exactly. The nodal values equal those of the one-member partial-span problem.

   What it gives up, a load boundary inside a member, belongs to the non-pressure half, which the crate fixture keeps. It adds interior chain nodes, which is a gain. N-1 applies.
2. **The MILLTOL fold is faithful.** The retired code fixes OD and takes id = OD − 2(t − c − m) (`stress/src/lib.rs:1630-1636@ec5d397359`), so c and m both enlarge the bore. Authored wall 0.008 with slot 0.00125 gives the identical annulus under today's rule. S-3 applies.
3. **Frames and signs are correct for every five-station and endpoint row** (§2 table).
4. **The zero-scale floors are adequate.** Every zero is exact by decoupling or restraint, or sits at residual level. The smallest margin, tolerance / (ε·largest same-unit value in the case), is 4.4e4: case 2 combined, transverse-force zeros (9e-7 N against ε·9.2e4 N). The other load cases have margins of at least 1.9e6. No floor hides an error of physical size; an error such as interior caps or an unpaired Poisson load gives a UX of order 1e-5 m against a 4.6e-13 m floor. The 1e-9 relative criterion absorbs the decimal-input rounding (ν = 0.3 and similar).
5. **The twin's "bit-equal" scope is right in kind, but needs repair.** The kind is right: per mode; f64 bits including the sign of zero; rows, row set, maxima, evidence and standing; contract strings, cross-mode and cross-schema excluded. The repairs are in S-4.

## 4. Findings

**S-1 (SHOULD-FIX, transport). Zero scales are not maintained quantities under T1's pattern.**
- **Claim affected:** the JSON is "shaped for the `exact_pressure_1` package on T1's `load_reference_1` pattern".
- **Evidence:** each `zero_scales` entry carries an extra `definition` key. T1's generator accepts only `{unit, exact, decimal, value}` (`validation/qualification/fixtures/load_reference/generate_reference_values.py:104-105@ed012c7ccf`). Several scales exist nowhere else in the file: case 2's `scale_stress` (P/As) and `scale_axial_length`, and the `scale_rotation` of cases 1 and 3. A T1-style selector therefore cannot reach them.
- **Related:** T1 converts the reference into the selector unit, using transform `identity` with an exact m→mm factor (`:51`, `UNIT_FACTORS`). T4-I8's `m_to_mm` is applied to the observation, with the tolerances precomputed in m. That is the inverse convention, so name or align it.
- **Repair:** move the definitions to a sibling map, or declare that the package generator accepts them. The values are unchanged.

**S-2 (SHOULD-FIX, missing re-freeze condition). Case 2's deflections are Euler–Bernoulli.**
- **Claim affected:** "relative 1e-9" for the uy rows at B, C, D, and the twin's tip bending.
- **Evidence (inference):** if D-6 makes Timoshenko the default in T4-U8, a correct product moves uy(D) by about −1.2e-5 m, or 0.3% (κ ≈ 0.5, ∫V dx/κGA). SP-3 then forbids changing the reference.
- **Repair:** declare now, as for MILLTOL and D-5, that these rows are re-frozen in T4-U8 if D-6 changes the default. The cantilever's V, M, reactions and pressure rows are statically determinate or axial and stay. The rz rows stay if the published rotation is the section rotation.
- **Planning point for T4-U8:** how a changed default squares with SP-1's v2 byte-identity.

**S-3 (SHOULD-FIX, negative control). `cap_area_on_nominal_bore` targets an error the folded document cannot produce.**
- **Evidence:** it uses ri = 0.09, but the folded document never carries the 0.01 wall, so its "why" is wrong for the fold.
- **What is missing:** the producible wrong product applies the mill reduction to As but takes Ai from the authored bore (ri = 0.092). It gives σz(free) = 270848000/20871 = 12977.241148004408 Pa, which is not listed.
- **Repair:** replace the control or add this one. The positive rows already reject this error, so no value changes.

**S-4 (SHOULD-FIX, the twin's SP-1 record).**
- (a) **Invert the inclusion list.** Every numeric leaf of the envelope should compare bit-equal, except a closed exclusion list. The enumerated list omits numeric evidence that the exact route publishes:
  - the material evidence (E, ν, G, α), `eigenload_pair_local_n`, the cap pairs, the terminal cap forces and the assembly-term coefficients (`pressure_runtime.rs:642-647, 686-689, 880-883`);
  - `pipe_stress_extrema` (`lib.rs:5569`);
  - the 0.4.0 `load_reference_states` evidence (`lib.rs:2820`).

  Also align the diagnostics. The markdown says "the diagnostics" and the JSON says "blocking/failure diagnostics". Prefer all diagnostics by code, severity and refs, with message text that names the contract excluded.
- (b) **Anchor the v2 side.** As written, v3 is compared with v2 from the same candidate build, so a common-mode change below 1e-9 in shared straight code passes. State that the v2 run compared is itself byte-identical to the base output (SP-1's first clause).
- (c) **Attach the same scope to every v2/v3 pair, and restrict the inputs.** Cases 1–3 carry only a note. Restrict the claim to v2-admissible inputs (p ≥ 0): v3 admits signed pressure, and v2 refuses p < 0 after T4-U0.

**N-1.** The chain's interior nodes also exercise three-member region traversal. Product tests cover two spans (`PP/tests/pressure_runtime.rs:572-603`).

**N-2.** `allowance_not_folded` guards the document's authoring, not the product. The D-5 re-freeze inference ("Nw, S stay") holds only if ε_p's As equals the stiffness As (RV1 N-5), as D-5 recommends.

**N-3. Product rows not frozen, beyond the brief.**
- The support force and moment magnitude rows for cases 1 and 3. They are published for every support (`lib.rs:11425-11435`); case 2 has them only as a side block.
- The station and end bending-normal and torsional-shear stress rows.
- `pipe_elastic_normal_stress_maximum_v2`. On straights it already uses the wall membrane Nw/As (`lib.rs:10340-10420`), so it is pressure-coupled today. The JSON's attribution of the maximum to T4-U4 is inaccurate: T4-U4 is the arc maximum.

Case 2's maximum is a cheap closed form, |Nw/As| + |M(0)|/Z.

**N-4. SP-1 sample breadth.** No v2/v3 pair exercises separately supported closures, reversed member or terminal order, or unequal-wall chains. Running the bit-equality over the existing v2 exact documents in PP's tests would cover these mechanically. Straights next to bends in a v3 document have no v2 twin; they belong to the L-bend references.

**N-5.** Using `weight` for the lateral load is mechanically identical to `distributed_force` (`lib.rs:13512-13513`) and avoids the mapping warning (`lib.rs:9106`). The product publishes displacement, end and station rows with `basis_ref: None` (`lib.rs:11253, 11355`). T1's selectors attach the case basis in the same way, so no change is needed.

## 5. Coverage, discrimination and transport

- **Coverage:** every case, quantity, document version (0.3.0, 0.4.0, and the provisional v3 patch), both modes and the negative controls required by the brief and plan §5 are present. The gaps are listed in N-3 and N-4.
- **Discrimination:** all 25 discriminator comparisons (24 discriminators) are separated by 1.2e6 to 2e9 criteria. The smallest is the retired thin-wall hoop in case 1.
- **Transport:** the 0.3.0 twin document equals `pressure_section_geometry.rs` `fixture()`. The 0.4.0 sketches match T1's `preview_request` shape. Provisional fields are marked. S-1 is the one transport defect.

## Run records (`R4/T4-RV4/_run_records/`)

- `reproduce_i8.py` and `reproduce_i8.stdout.txt`: SHA256SUMS verification and the byte-for-byte re-run.
- `refute_values.py` and `refute_values.stdout.txt`: the independent re-derivation, discriminator separations and zero-floor audit.

Reproduce from `_run_records/`, with the fixture extracted at `ed012c7ccf` into scratch:

```
WT/venv/bin/python -I reproduce_i8.py ../../T4-I8 <fixture> <empty scratch dir>
WT/venv/bin/python -I refute_values.py ../../T4-I8/rebuilt_reference_cases.json <fixture>
```
