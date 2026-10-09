# T4-I12 round 01: the 0.4.0 form, the eigenstrain refusal, the replaced-span controls, K-D5 at UTM scale

- **Asked by:** T4's WORKING_ITEMS, after the round-0 commit `a744c09021` (SHA256SUMS `9925375b…`), while T4-RV5 refutes round 0.
- **WI ruling applied:** under load-reference-1 the connector does not use the replaced span's resolved element state (E/ν and eigenstrain). Three things refuse with `JOINT_REPLACED_SPAN_LOAD_UNOWNED` (SLOT_TABLE S20 applied to 0.4.0): a nonzero resolved eigenstrain on the replaced span, self-weight on it, or any load it owns.
- **WI's follow-up rulings, folded in:**
  - a state that resolves to exactly zero eigenstrain has no effect on the connector and is admitted;
  - refusal is decided per case, by what that case applies. A case listing a load on the replaced span in `load_sources` is refused; a load stored but applied by no case is not refused and has no effect.
- **Also asked (after WI committed round 01 at `2e79cf469e`):** T3's slot-table review RV130, S-3, which K-D5's undemoted connector case serves. Addition 5 below.
- **Status:** appended and frozen; no product run; no Git write.

## What changed

- **`u3_reference_cases.json`:** five cases appended at indices 18–22, and a top-level `round_01` note.
  - Against round 0 (`a744c09021`) the git diff is 9560 insertions and 0 deletions; the round-0 text is a byte prefix of the new file.
  - Against the round-01 commit `2e79cf469e`, cases 0–21 are unchanged. The only other change is the `round_01` note, which gains the new case id and an `rv130_s3` line.
- **`_run_records/u3_reference.py`:** blocks inserted before the document is assembled (499 lines added against round 0, 0 removed); 861 of 861 checks pass, the first 761 as in round 0.
- **`_run_records/check_round01.py` (new):** 130 of 130 pass. It also proves the four round-01 cases committed at `2e79cf469e` unchanged, by canonical hash. It shows the 18 frozen cases unchanged:
  - their order (indices 0–17);
  - each case's canonical SHA-256, against constants taken from the round-0 file (sha256 `46816c84…`);
  - every round-0 top-level key.

  A direct comparison with the round-0 file, via the optional second argument, also passed during preparation.
- **Unchanged:** `check_reference_json.py` (508 pass) and `probe_binary64.py`, rerun with identical stdout. `U3_REFERENCE.md` and `RETURN.md` are not edited. U3_REFERENCE §7's "not frozen: a 0.4.0 form" is superseded by addition 1.

## Additions

1. **`U3-SYS-DEMO-CONNECTOR-002-LR1`: the 0.4.0 form of the system case.**
   - The model: schema 0.4.0 and one `direct_strain_reference` configuration (fit none for every pipe, P-130 included).
   - Each case carries an `analysis_state`:
     - one element state per pipe, `explicit_base_properties` naming the pipe's own material;
     - every support `active_model_device`;
     - every stored primitive in `load_sources` with factor 1.
   - L-100's thermal becomes P-120's `constant_alpha_interval` (1.2e-5 /°C × 12.5 °C; eigenstrain 3/20000); there is no thermal primitive.
   - **The replaced span stays cold:** `unchanged_reference`, fit none, resolved eigenstrain exactly 0, while P-120 is strained. Element states are per pipe and per case, so no nearer variant was needed.
   - Every displacement, reaction and connector value equals U3-SYS-DEMO-CONNECTOR-001's, string for string. A document-driven solver checks this; it first reproduces the frozen 0.3.0 case from its own document.
2. **`U3-SYS-LR1-REPLACED-SPAN-EIGENSTRAIN-REFUSAL`.** Each variant gives `MODEL_INCOMPLETE`, no results, and `JOINT_REPLACED_SPAN_LOAD_UNOWNED` with refs including `component:C-150` and `pipe:P-130`:
   - (a) P-130's thermal state in L-100 is `constant_alpha_interval` (eigenstrain 3/20000): L-100 refused;
   - (b) P-130's fit is `fit_strain` 1e-4 (eigenstrain 1/10000 in every case): all cases refused;
   - (c) a weight primitive on P-130 is listed in `load_sources`: L-100 refused.

   **Boundary (admitted, by WI's ruling):** P-130 with an `explicit_interval_strain` of 0 resolves to exactly zero eigenstrain. It is not refused, and every expected value equals the cold case 002-LR1 (string for string; the values are recorded).
3. **`U3-SYS-REPLACED-SPAN-MATERIAL-CONTROL`.** P-130 names a different material (E 1e11 Pa, ν 0.25); in 0.4.0 its element state selects that material too. Every value is identical to 001 (0.3.0) and to 002-LR1 (0.4.0); in each mode the product's rows must be bitwise equal to its run of the unmodified document.
   **Discriminating:** with P-130 kept in parallel, its E/ν moves S-100 Fz, Mx and My, S-120 Fz and SH-140 Fz in every case (both E/ν sets are recorded).
4. **`U3-SYS-LR1-REPLACED-SPAN-STORED-UNAPPLIED-CONTROL` (index 21; admitted).** L-100 stores a weight primitive on P-130 (`load:L-100-Z-130-STORED`, −150 N/m in global x) that no case lists in `load_sources`.
   - Nothing is refused.
   - Every displacement, reaction and connector value equals 002-LR1, string for string.
   - The document differs from 002-LR1's only by that stored primitive.
   - Listing the same primitive in L-100's `load_sources` is refusal variant (c).

5. **`U3-KD5-UTM-SKEW-OFFSET-COUPLED` (index 22; RV130 S-3).** No frozen case met S-3: U3-GENERIC has offsets, a skew Q and a coupled K, but only at ordinary coordinates and with decimal (not binary64-exact) inputs.
   - **Inputs (all exact binary64, given as round-trip strings, hex and rationals):**
     - Q is the binary64 rounding of the rational rotation with columns (1,2,2)/3, (2,1,−2)/3, (−2,2,−1)/3, used exactly as given;
     - K is U3-GENERIC's coupled PD K, with Ls = 0.25;
     - aᵢ = (0.2, 0.4, −0.2), aⱼ = (−0.1, 0.3625, 0.44999999999999996);
     - q_ref and d are dyadic.
   - **Locations:** xᵢ = (X0 + 0.5, −1.25, 2) and xⱼ = (X0 + 1.8125, 0.8125, 3.375), for X0 = 0, 5e6 and 7.3e6 m.
   - **Geometry:** xⱼ,ₓ − xᵢ,ₓ = 1.3125 exactly. aⱼ was solved for so that the exact r = (xⱼ − xᵢ) + (aⱼ − aᵢ) is exactly parallel to (1, 2, 2) = Q.x. The x offsets carry binary64 tails finer than the 2⁻³⁰ m grid at 5e6–7.3e6 m, so the absolute-position form must round there.
   - **Reference:** B, Ke, q, g, energy, end actions and BᵀKq_ref, exact for those binary64 values and identical at all three locations. The six rigid motions about the origin and about xᵢ lie in null(B) and null(Ke) exactly. The end actions balance at each location.
   - **Illustration (a naive binary64 formation in this script, not the product):**

     | Form | Relative error in r | Relative error in Ke |
     |---|---|---|
     | Difference, all locations | 1.8e-17 | 9.4e-17 |
     | Absolute-position, at UTM | 6.1e-11 | 5.3e-11 |

     T3 reports 1.39× and 6.5e-7× of K-D5's criterion for the two forms at UTM. K-D5's own criterion decides demotion.
   - **Perturbed variant:** Ke′ = Ke_formed + δ e₃e₃ᵀ on the largest diagonal entry (DOF index 3), with δ = 2⁻²⁰ max|Ke|. It is applied to the formed matrix only, never to K-D5's re-formation. δ is about 18000× the absolute-form defect. Expected: demoted at all three locations, while the unperturbed difference-form case is not demoted.

## Admission (inferred from code at `ed012c7ccf`, not run)

The 0.4.0 document follows `case_state/input.rs` and `resolve.rs`:
- an element state and a reference member for every pipe;
- a support state for every support, with no spring device reference;
- no thermal primitive;
- `material_ref` equal to the pipe's material;
- an empty request `materials`.

The `"1"` unit for a dimensionless strain (variant b and the boundary) is the catalogue's dimensionless symbol (`P/core/units/src/lib.rs:417`).

## SHA256SUMS

Regenerated over every file under `R4/T4-I12/`.
