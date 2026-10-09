# T4-I2 return: the curved element and stress recovery (after U3)

TASK T4-I2 (Type 2, research only), for T4's HELPS_HUMANS. Brief: `R4/BRIEFS/T4-I2_CURVED_ELEMENT_STRESS.md`.

- **Basis.** Main `ec5d397359` plus U3 `70e7f49ced`. U3 is the basis where they differ. Main's only later changes in these files are I109's correctly rounded norm (`hypot` → `norm2`/`norm3`) and two import lines.
- **Commit labels.** `@U3` means `@70e7f49ced`; `@main` means `@ec5d397359`. A file cited `@U3` that U3 did not touch is byte-identical at `@main`.
- **Path labels.**
  - `CB` = `P/core/solver/curved_bend/src/lib.rs`
  - `PPL` = `PP/src/lib.rs`
  - `PPP` = `PP/src/preview_physics.rs`
  - `PRT` = `PP/src/pressure_runtime.rs`
  - `SA` = `P/core/solver/nonlinear_integration/src/structural_adapter.rs`
  - `FC` = `FK/src/structural/formation_check.rs`
  - `SR` = `P/core/loads/stress_recovery/src/`
  - T3's rulings: `I/NUMERICAL_INTEGRITY_T3/ROOT_RULINGS_V1.md`, read at `WT/numerics` HEAD `db763ed75c`.
- **Method.** Reading only, with no cargo. One standard-library Python emulation of PP's arc centre (`_run_records/centre_probe.py`, sha256 `d3ec681d…`; output `centre_probe.stdout.txt`, `c709a1ed…`; Python 3.13). It is an emulation, not a product run.
- **Fact and inference.** Unmarked statements are facts read from code or records. Inferences are marked **(inference)**.

## 0. Findings most likely to change T4's plan

1. **No curved bend can reach the exact contract or retained precision today, and the desktop cannot author one.**
   - The exact route refuses every component (`PRT:174-177@U3`).
   - The source and retained routes refuse curved and component families (`PP/src/source_recovery.rs:579-585@U3`, `PP/src/retained_product.rs:1557-1560@U3`).
   - Realizing a curved bend needs `mechanics_interface.solver_consumption = "curved_bend_macro_element"`. No app or operation path writes that field (§2).
   - So "pressure on one curved bend" needs, as one connected unit:
     - M02 authoring;
     - the exact contract admitting a curved component;
     - a new curved pressure load. U3 deleted the old one.
     - arc stress recovery.
2. **The objectivity and rotation defects have one root.** The product builds the equilibrium transfer H from a *formula* chord, R(cos φ − 1, sin φ, 0) (`CB:246-250`, `:315-319@U3`), not from the node chord. PP forms the arc centre in absolute binary64 coordinates (`PPL:7836-7845@U3`).
   - In my emulation, at |X| = 5e6 m with R = 0.3 m:
     - 16% of random elbows are refused outright by the 1e-9 radius check (`CB:160-162`);
     - the admitted ones carry a chord mismatch of up to 9.6e-10·R.
   - A node-relative centre keeps both at about 5e-16 at any |X| (§1.4).
   - The fix has two parts: H from the actual chord, as K-D5 already does (`FC:735-751@U3`), and geometry formed from node differences, never from an absolute centre.
3. **S11-G's guard demotes any realized curved bend that carries a uniform load** to Sensitive with `CannotBound` (`PP/src/formation_guard.rs:21`, `:233-236@U3`; test `PP/src/s11g_tests.rs:1743-1774@U3`).
   - Every realistic elbow carries self-weight. T4's curved pressure load will meet the same guard unless it ships with an exact formation or a conservative formation bound (**inference**).
4. **T4's repair breaks T3-owned tests that pin today's defect.**
   - Among them: `kd5_very_large_coordinate_pp_route_elbow_demotes_on_both_entries`. Its precondition `actual > 1.0` will fail, as intended (`PP/tests/formation_check_runtime.rs:379-399@U3`).
   - SA's K-D5 tests at `kd5_tests.rs:400`, `:447` and the M31b mutation kills are also affected.
   - The constructor signature is used at 19 call sites in 8 files.
   - This is a T3 interface, and T3 has said its W1c will re-form whatever element T4 defines (R5-4).
5. **Arcs publish no stress maximum, no SIF and no intensified measure.**
   - The certified maximum (`SR/elastic_extrema.rs:76@U3`) takes only quadratic polynomial fields. Arc resultants live in the {1, cos θ, sin θ, θ, θ cos θ, θ sin θ} basis (`CB:614-685@U3`).
   - So M14 for bends needs a new enclosure, not a reuse.
6. **The VP-STATIC Q1 outputs do not exist.** Transverse-shear stress and signed circumferential extrema and fibres have no producer and no schema vocabulary (§3.7).
7. **M30 is untouched.** One section basis, OD with wall − mill tolerance, drives stiffness, the curved element, stress, the exact pressure annulus and mass. PP has no corrosion-allowance input at all (§3.2).
8. **The SIF and flexibility are single scalars.** The curved crate already takes separate in-plane and out-of-plane flexibility factors, but PP passes one value twice (`PPL:7862-7863@U3`). There is no in-plane or out-of-plane SIF field (§3.5).

## 1. The curved element

### 1.1 Formulation (`CB@U3`)

- **The element.** A two-node, 12-DOF arc macro-element. Each node has [ux, uy, uz, rx, ry, rz] (`CB:21-22`, `:83-98`).
  - Its geometry comes from the two end nodes and an absolute `center` (`CB:87`).
  - `geometry()` forms r_i = x_i − c and r_j = x_j − c, and R as the **mean** of |r_i| and |r_j| (`CB:150-163`).
  - It refuses a radius mismatch above 1e-9 relative (`CB:26`, `:160-162`), and requires φ = atan2(|r_i × r_j|, r_i·r_j) in [1e-9, π − 1e-9] (`CB:165-169`).
- **The local frame.** x is radial at i, z = r_i × r_j normalized, and y = z × x (`CB:171-177`, `:194-198`).
- **The flexibility.** A Castigliano closed-form 6×6 tip flexibility with i fixed (`CB:206-239`):
  - unit-load actions in {1, cos θ, sin θ} (`CB:563-612`);
  - an exact trigonometric Gram (`CB:765-782`);
  - the user factors k_in and k_out scale only the in-plane and out-of-plane bending-energy terms;
  - torsion and axial energy are included; shear deformation is excluded (`CB:80-82`).
- **The stiffness.** K_jj = F⁻¹ by FK `solve_dense`, one column at a time, then symmetrized (`CB:796-817`). The full matrix is K = [[H K Hᵀ, −H K], [−K Hᵀ, K]] with H = [[I, 0], [skew(c), I]] (`CB:821-850`).
  - **c is the formula chord R(cos φ − 1, R sin φ, 0)** (`CB:246-250`).
  - The matrix is rotated to global with FK `transform_global_stiffness` (`CB:255-259`).
- **Loads and recovery that remain.**
  - Consistent uniform-load equivalents, by the force method in the extended basis (`CB:277-344`). These use the formula chord again (`CB:315-319`).
  - Arc section resultants by segment equilibrium. The section frame has x tangent, y inward and z normal (`CB:360-450`).
  - Exact-sum E11 terms (`CB:476-510`).
  - `end_tangents` (`CB:457-469`), now used only by the tangency warning (`PPP:503-546@U3`).
- **libm dependence.** `sin`, `cos`, `atan2` and `sqrt` appear throughout in binary64. Their accuracy is not specified by the product (R5_4 §2).

### 1.2 How PP forms and places it (`PPL@U3`)

1. **Selection.** A component of kind `bend` or `elbow` with `mechanics_interface.solver_consumption == "curved_bend_macro_element"` (`PPL:7593-7606`, `:12233-12235`). Its `geometry.bend_pipe_ref` span is replaced: the arc's ends are that span's two nodes (`PPL:7613-7626`).
2. **Required inputs.** Any missing one blocks; there is no straight fallback (`PPL:7628-7760`).
   - `bend_pipe_ref`;
   - `bend_radius`;
   - `modifiers.flexibility_factor_user_value`;
   - the pipe's `y_reference`.
3. **The angle and plane.**
   - The implied angle is 2·asin(L/2R) (`PPL:7793`). An optional `bend_angle` must agree to 1e-6 relative (`PPL:7794-7811`; constant `PPL:163`).
   - The plane is spanned by the chord and the pipe `y_reference`, projected normal to the chord (`PPL:7812-7835`). The arc bows toward +y_reference (review row, `PPL:12028`).
   - **`bend_plane_orientation` is required for completeness** (`PP/src/validation.rs:1559-1575@U3`), **but the solver never reads it.**
4. **The centre** is computed in absolute coordinates: c = ½(x_i + x_j) − s·n̂, with s = √(R² − L²/4) (`PPL:7836-7845`).
5. **Formation.** The element is formed with the single user factor passed as both k_in and k_out (`PPL:7849-7863`). It is stored with the chord x_j − x_i, its global K and the element (`PPL:2090-2109`, `:7893-7911`). It enters every solve path as an explicit global matrix:
   - linear: `CurvedBendStiffnessElement::from_macro_element`, `P/core/solver/nonlinear_integration/src/lib.rs:214-232@U3`;
   - nonlinear (`PPL:5729-5740`);
   - K-D5/K5 `curved_sources` (`PPL:1431-1457`, `:6086-6128`).
6. **Recovery.**
   - **End forces** are one exact sum of K_e·u minus the thermal free expansion and the uniform equivalents (`PPL:10877-10944`). They are then rotated into the **straight chord frame** of the span (`PPL:10946-10957`).
   - **Station resultants** rotate those chord-frame forces back to global, then evaluate the arc section function (`PPL:11013-11055`). That is a binary64 round trip through the rotation (**inference**: avoidable).
   - **Thermal** is the exact free-expansion identity about node i (`PPL:10809-10818`).

### 1.3 What U3 removed and what remains

- **Removed from CB** (`git diff ec5d397359...70e7f49ced -- CB`):
  - `consistent_radial_pressure_nodal_loads`;
  - `arc_section_resultants_with_radial_pressure`;
  - `tip_deflection_under_radial_pressure`;
  - `radial_pressure_load_actions`;
  - six radial-pressure tests.
- **Removed from PP:**
  - `build_pressure_thrust_loads`;
  - `add_pressure_thrust_loads`;
  - `add_curved_bend_pressure_thrust_load`, which made the arc end-cap tangent pair {−pA t_i, +pA t_j} from `end_tangents` plus the consistent radial wall load;
  - the expansion-joint thrust plumbing.
- **The review row now states the truth:** `pressure_thrust_treatment=none_pressure_refused_outside_the_exact_straight_contract` (`PPL:12028@U3`).
- **Stale code comments still describe the deleted radial treatment:** `PPL:10899-10904`, `:11004-11012` and `:11045-11047@U3`. They are not published text, so they fall outside ruling 4 of the U3 Stage 2 rulings.
- **What remains:** stiffness, uniform loads, thermal, stations and tangents. No pressure path exists for arcs.

### 1.4 T3's findings: cause and location

- **The rigid-motion null space and rotation consistency.** A rigid rotation is in K's null space only if c = x_j − x_i in the local frame (`I/NUMERICAL_INTEGRITY_T3/DESIGN_NUMERICS/R5_4_CURVED.md` §2).
  - The product's c comes from R and the trigonometric values, so the binary64 element carries a rigid-mode stiffness of O(u).
  - This mismatch is the main formation defect. It drives the four Passed breaches, up to 1.48× the criterion (R5_4 §3; ROOT ruling R5-4).
  - A check that reused the product's own matrix missed 2 of the 4, which is why K-D5 re-forms the element.
- **Non-objectivity at large coordinates.** PP's absolute centre rounds at ulp(|X|) (about 9.3e-10 m at 5e6 m), which unbalances |r_i| and |r_j|, and so the formula chord drifts from the actual chord. The emulation (`_run_records/centre_probe.stdout.txt`; R = 0.3 m; 2,000 random elbows per row):

  | \|X\| | PP centre: max \|r_i−r_j\|/R | Refused (> 1e-9) | Formula−actual chord / R (admitted) | Node-relative centre: same two |
  |---|---|---|---|---|
  | 0 | 9.3e-15 | 0 | 6.7e-15 | 3.7e-16 / 5.9e-16 |
  | 5e5 | 2.7e-10 | 0 | 2.1e-10 | 3.7e-16 / 6.7e-16 |
  | 2e6 | 1.1e-9 | 21 | 7.8e-10 | 3.7e-16 / 5.9e-16 |
  | 5e6 | 4.6e-9 | 321 | 9.6e-10 | 3.7e-16 / 6.7e-16 |

  - These agree with T3's product numbers: 1.13× the criterion at X = 5e6 m, φ = 5°; Sensitive by K-D5 (WORK_GRAPH T4 row; ROOT, "K-D5 mutation M31b: equivalence withdrawn").
  - The **refusal column is a hidden availability loss.** K5's ruling notes it: "non-dyadic bends at 5e6 m are refused earlier by the curved-bend radius check".
- **W4 and K5.** W4 already treats a matched curved slot as an objective link whose null space is the six rigid motions (`SA:1446-1470@U3`; FK `rigid_body.rs:250-260@U3`). T4's confirmation is not a prerequisite (K5 ruling Q3), but T4's formation is what makes that assumption true.
- **SA keeps a second copy of the formula chord** in its symmetry trace `curved_formation` (`SA:2025-2045@U3`).

### 1.5 Where K-D5 and its wide-precision re-formation live

- **The intended element.** `FC:1-35` (doctrine) and `FC:47-60`: `CurvedFormation` carries the nodes, coordinates, **PP's binary64 centre**, E, G, A, I, J, k_in and k_out.
  - `curved_matrix` (`FC:663-764`) re-forms the element in `Wide<2>` at p = 128.
  - It takes cos φ and sin φ from square roots, φ by the K3a `included_angle` (FK `structural/retained/wide.rs:924-936@U3`), and the closed-form flexibility and its inverse.
  - **H comes from the actual chord** (`FC:735-751`).
- **The check.** The rule is 2|w| > 1e-9·scale (`FC:155-180`). A source family the check cannot form demotes (`FC:69-74`).
- **Plumbing.** SA matches each slot to its macro element by node indices and the bits of its global matrix (`SA:1546-1595`), and K5 matches the same way (`SA:1505-1529`).
- **Reserved API.** `atan_positive` is labelled "later-slice API (W1c; K3 Q6)" (FK `wide.rs:938-939@U3`).

### 1.6 What an objective, rotation-consistent formation changes

This section is a design sketch for T4 (**inference**, grounded in §1.4).

- **Inputs.** Form the element from node *differences* and user data: d = x_j − x_i, the user R, the plane normal n̂ from `y_reference`, the section, the material and the factors. Never form an absolute centre.
  - φ = 2·asin(|d|/2R) and R come straight from the inputs, so the 1e-9 radius refusal becomes unnecessary for PP-built bends.
  - The local axes come from d̂ and n̂: x_r = −sin(φ/2)·d̂ + cos(φ/2)·n̂, then z and y.
  - If a centre is kept, keep it as an offset from node i. The emulation's node-relative column shows the effect.
- **H from the actual chord**, axes·d, in the product (`CB:246-250`, `:315-319`), and the same in SA's trace (`SA:2036-2041`). The null space is then exactly the rigid motions of the actual nodes, for any K_t.
- **A mathematical definition of the intended element** (inputs, then exact formulas), so that W1c can re-form it at precision p. Today K-D5 takes PP's *rounded* centre as an input (`FC:668`). That input changes, and `CurvedFormation` (`FC:47-60`) and SA (`SA:1576-1589`, `:1731-1744`) change with it.
- **Optional removal of libm.** Taking sin φ and cos φ from |d| and R (square roots only), as K-D5 does, would make the binary64 element platform-independent. Only φ itself needs an arctangent.
- **Compatibility.** The `CurvedBendMacroElement::new(…, center, …)` signature has 19 call sites in 8 files:
  - 2 in PPL;
  - 10 in CB and its S11-K tests;
  - 7 in the nonlinear_integration crate: its `lib.rs` and the `k1`, `k2b`, `k5` and `kd5` test modules.

### 1.7 Tests that pin today's behaviour (`@U3`)

| Location | Tests | What changes with an objective formation |
|---|---|---|
| CB | `rigid_body_modes_produce_zero_force` (`:1233`), `rotated_geometry_transforms_stiffness_congruently` (`:1319`); both at the origin, 1e-9·max\|K\| | They still pass. They do not detect the defect, so a large-coordinate and ill-conditioned control should be added (**inference**). |
| PP tests | `kd5_large_coordinate_pp_route_elbow_is_published_accurately_and_not_demoted` (`PP/tests/formation_check_runtime.rs:358`) and `kd5_very_large_coordinate_…_demotes_on_both_entries` (`:379`; precondition `actual > 1.0`) | The second fails by design. T3 must agree its replacement. |
| SA `kd5_tests.rs` | `:378` (E1/E6 no demotion), `:400` (k_X = 8.5 demotes), `:419` (actual chord), `:447` (centre mismatch demotes), `:484`; the M31b/M31b0 kills (ruling "M31b equivalence withdrawn") | `:400` and `:447` may stop demoting. Once the product itself uses the actual chord, the M31b mutant becomes a *false* demotion rather than a miss, so the kills must be re-derived. |
| PP tests | `k5_curved_mechanism_runtime.rs:148-250`; `preview_physics_runtime.rs:854` (b1 arc rows, frames, withheld maximum) and `:913` (b2) | Values move by about u; the frozen references hold at their scales (**inference**). |
| PPL | `curved_bend_macro_element_*` (`:21962-22445`); `curved_bend_macro_element_multiplier_applies_sif_only` (`:22083`), which pins "SIF not applied until T4" | They change deliberately when arc SIF lands. |
| PP S11 tests | `s11g_tests.rs:1747` (curved CannotBound), `s11f_tests.rs` `f8_curved_*` | They change only if T4 supplies a curved formation bound. |

## 2. M02: how a bend is authored today

- **The model of a bend.** A bend is a **component** at a node (`kind: bend|elbow`, `node`, `geometry`, `modifiers`, `mechanics_interface`) in the product preview document (`PPL:359-420@U3`). There is no explicit element kind, and no "implied bend at a corner node with a radius".
  - The arc *is* the named span `bend_pipe_ref`. The user must create the tangent-point nodes and that span themselves.
  - Tangency with the neighbouring pipes is only warned about, above 1e-6 rad (`CURVED_BEND_TANGENT_DISCONTINUITY`, `PPP:503-546@U3`).
- **Modes.**
  - The default, `mechanics_geometry_only` (`PPL:7604`), is a **straight chord** element. The user SIF becomes an intensified measure at the adjacent straight member ends (`PPP:403-432`, `:693-760@U3`), and the flexibility factor is unused.
  - `curved_bend_macro_element` is the arc of §1.
- **Schema.**
  - No JSON schema for `openpipestress.product_preview.model` exists in `P/schemas`; PP's serde structs are the operative contract.
  - `P/schemas/model.schema.yaml:290-330@U3` defines a different canonical `Component`: a `component_type`, a map of geometry quantities and `mechanics_modifiers`.
  - `P/schemas/component.schema.yaml:498-507@U3` (the library-record schema) lists `curved_bend_macro_element` as a `solver_consumption` value.
- **The desktop.**
  - Creation writes geometry only: `bend_pipe_ref` (the first incident pipe), `bend_radius`, `bend_angle`, a free-text `bend_plane_orientation` and a source (`apps/desktop/src/features/component-creation/componentIntent.ts:320-327@U3`). It writes no modifiers and no `mechanics_interface`.
  - The applier canonicalizes the same five fields (`P/core/model_operations/operation_applier/src/lib.rs:2520-2585@U3`).
  - Its editable paths include the bend geometry and `modifiers.sif_user_value` / `flexibility_factor_user_value` (`:513-533`, `:652`, `:673`), but **not `mechanics_interface`**.
  - The model view only *displays* the mode (`apps/desktop/src/features/model-workspace/modelView.ts:142-165@U3`).
  - So a realized arc reaches a solve only from an imported or hand-authored document. No committed model uses one (R5_4 §1).
- **What explicit authoring would need** (**inference**):
  - an authorable realization mode, or a distinct bend element;
  - geometry that is explicit and consumed. The plane and side should come from the tangents of the adjacent pipes or from an explicit corner point. Today they come from `y_reference`, while `bend_plane_orientation` is required but ignored.
  - optionally, an operation that inserts tangent points at a corner node from a radius, with tangency enforced rather than warned;
  - separate in-plane and out-of-plane flexibility and SIF fields, with their source;
  - one radius/angle authority (today the angle is redundant and checked to 1e-6);
  - a JSON schema for the document's component block;
  - UI in the component panel and the property inspector.

## 3. Stress recovery (after U3)

### 3.1 Quantities

- **`SR/lib.rs@U3`** computes:
  - axial N/A;
  - bending My/Z_y and Mz/Z_z;
  - torsion T·r/J (`SR/lib.rs:428-470`, `:789-810`).
- **U3 removed** the thin-wall membrane (`PressureBasis`, `pressure_hoop`, `pressure_longitudinal` and their ranges; `SR/README.md@U3`).
- **The legacy summary** is still the absolute sum N/A ± (|σ_y| + |σ_z|) (`SR/lib.rs:898-912`). PP's `open_formula_summary_mpa` (`PPL:11608-11630`) repeats it.
- **PP's calls.** PP calls `recover_section_stress` (`PPL:11586-11606`) at the ends (j-side section actions at fractions 0 and 1) and at the quarter_1, midspan and quarter_3 stations (`PPL:5135-5350`).
- **Not produced on any route:** transverse-shear stress, hoop or radial stress (outside the exact pressure route), and equivalent stress (`PPP:76@U3`; `SR/elastic_section.rs:6-9@U3`).

### 3.2 Section bases (M30)

- **`SR/elastic_section.rs` is unused by any product code.** Its only caller is its own tests (a search of `P/core` and `P/apps`).
  - It has no nominal, corroded or mill-tolerance bases. The caller owns the basis (`:11-22`).
  - Main changed only its norm (`elastic_section.rs:106@main`).
- **PP uses one `DerivedSection` from OD and wall − mill tolerance** (`PPL:10192-10241@U3`) for every purpose:
  - straight stiffness (`PPL:7288-7296`);
  - the curved element (`PPL:7849-7863`);
  - stresses (`PPL:11586-11606`);
  - maxima (`PPL:10338-10421`);
  - the exact pressure annulus, built from `derived.wall_thickness` (`PPL:7239-7259`);
  - mass (`PPL:9185-9250`; `PP/src/self_weight.rs:460-465`, method `source_od_effective_wall_areas/v1`).
- **Corrosion allowance.** `PipeSectionInput` has no such field (`PPL:318-340`). The Python calculator subtracts both corrosion and mill tolerance from one wall (`P/core/section_properties/calculator.py:154-157@U3`).
- **So M30's physical, mass and stress separation does not exist.** Stiffness and mass are reduced by the mill tolerance.

### 3.3 Extrema (M14)

- **The certified maximum.** `bound_piecewise_elastic_maximum` (`SR/elastic_extrema.rs:76@U3`) encloses max |a| + √(b² + c²) over piecewise **quadratic** Bernstein fields, with a gap of 1e-12 relative plus 1e-12 Pa (`:66-69`).
  - PP builds the fields from straight statics (`PPL:10338-10421`).
  - It publishes `pipe_elastic_normal_stress_maximum_v2` = |N/A| (or |Nw/As|) + hypot(My, Mz)/Z, with torsion kept separate:
    - on the exact route at `PPL:5397-5440`;
    - on preview-physics-1 through `PPP:335-362` and `:593-700`.
- **Arcs** get no maximum and no stress headline (`PPP:77`, `:693`, `:799`).
- **The abs-sum `open_formula_stress_summary`** is still computed for every member (`PPL:5345-5372`) and is retired only by the preview render (`PPP:14-18`).
  - **Inference to verify:** on non-exact source-selected envelopes (source-blocks-1), where no render runs, the abs-sum row is still published (`PPL:5451-5476`).
- **Naming.** The headline still travels in `summary.max_open_formula_stress` (`PPL:2845`).

### 3.4 Frames and signs (M37)

- **End force rows** are node-on-element in the element-local frame, with the sign of the local DOF (`PPL:11154-11178@U3`). On arcs the frame is the **chord frame**, relabelled `arc_chord_frame` (`PPP:667-680`).
- **Station rows and endpoint stress rows** are the **j-side cut action**:
  - straight: `STRAIGHT_ENDPOINT_SECTION_SIGN_CONVENTION`, `PPL:10961`;
  - arcs: in the **tangent frame**, x tangent, y inward, z the bend normal (`PPL:10962`, `:5200-5212`). Their `coordinate_system` is still "element_local".
- **So at one arc end, force rows and stress rows use different frames and sign senses.** Both are disclosed in their metadata.
- **Bending stress rows are resultant/Z**, signed with the moment, not a fibre stress. For example, at the +y fibre the stress is −Mz/Z (STRESS_REFERENCE §1: σ = N/A + My z/I − Mz y/I). No fibre is named.
- **Support rows** are support-on-pipe, global (`PPL:11398-11412`).

### 3.5 Directional recovery after signed algebra (M08) and SIF

- **Combinations.** On preview-physics-1 only the 20 linear kinds combine, including the four signed stress components (`PPP:34-55`, `:968`).
  - Maxima and intensified measures are **never combined** ("No combination maxima", `PPP:80`).
  - Exact-route combinations are refused (`PRT:204-206@U3`).
  - **So no directional quantity is recovered after signed algebra.** M08's "recover after algebra" is unimplemented, but no longer wrong.
- **The SIF measure** is i·hypot(My, Mz)/Z with a single scalar user SIF, at straight member ends next to a geometry-only bend or branch marker (`PPP:693-760`; `hypot` at `PPP:699@U3`, `norm2` on main).
  - On realized arcs it is not applied: `COMPONENT_STRESS_INTENSIFICATION_NOT_APPLIED` (`PPP:434-447`).
- **No directional SIF.** There are no i_ip or i_op fields, against STRESS_REFERENCE §4.
  - The arc's tangent-frame resultants already split cleanly: Mz is in-plane (about the bend normal), My is out-of-plane (about the inward radial), Mx is torsion (`CB:438-449`).

### 3.6 Shear deformation (M31)

- **No shear deformation anywhere:** FK frames are Euler–Bernoulli, and so is the arc (`CB:80-82`, `P/core/solver/curved_bend/README.md:40`).
- **`I/CORRECTNESS_DESIGN/SHEAR_REFERENCE/CONTRACT.md` §1** selects an energy-normalized annular Timoshenko formulation with K_s = 3EA(1+ν)(1+m²)²/D:
  - it needs **E/ν**, so the exact-route materials qualify and the ordinary route's independent E/G does not;
  - stiffness, load equivalents and recovery must change together.
- **It is straight-only.** Curved-pipe flexibility is explicitly out of its scope (SHEAR_REFERENCE `RETURN.md`). An arc with shear has no reference yet.

### 3.7 The VP-STATIC Q1 outputs

- **They do not exist.** `VALIDATION_FOUNDATION/_run_records/FIRST_STATIC_BINDINGS/OUTPUT_OBLIGATIONS.json:5-42` lists two:
  - `transverse_shear_stress_distribution`: "unsupported_observation_in_current_producer";
  - `signed_circumferential_normal_extrema_and_fibers`: "no_direct_producer_rows".
- **No producer and no schema vocabulary.**
  - The component enums in `P/schemas/results.v0.3.schema.yaml:626-675` (ResultMetadata) and `:3860-3905` (PreviewPhysicsResultMetadata) have neither.
  - Their only mentions are the limitation text "No transverse shear" (`:1457`, `:1680`).
  - `evaluate_elastic_section` computes σ⁺ and σ⁻ (`elastic_section.rs:69-120`) but is unused.

## 4. Publication and precision

| Identity, route | Where | Stress rows | Arcs |
|---|---|---|---|
| `preview-physics-1`: ordinary 0.1.0/0.2.0, pressure-free, the desktop default (`PPL:2685`, `:2852-2856`; `PPP:13`) | §3.1 rows; `pipe_elastic_normal_stress_maximum_v2` (Pa; evidence in `contract_evidence.preview_cases[].pipe_stress_extrema`); `component_equal_factor_intensified_bending_stress_v1` (`PPP:23`) | Station rows plus endpoint stress rows with basis `nominal_straight_beam_formula_on_arc_resultants` (`PPP:24-25`, `:56-63`) | Admitted |
| `physics-1`: exact 0.3.0 (`PPL:989-997`, `:911`) and `load-reference-1` (0.4.0, same route, `PRT:77-78`) | Component rows, except that the axial force and axial stress rows of pressurized members are replaced by `pipe_wall_endpoint_action_v2`, `pipe_wall_axial_force_v2`, `pipe_effective_axial_force_v2`, `pipe_axial_membrane_stress_v2`, and `pipe_lame_radial_stress_v2` / `pipe_lame_hoop_stress_v2` (inner and outer) at five stations (`PPL:11436-11585`); the v2 maximum | Refused (`PRT:174-177`) | Refused |
| `source-blocks-1`, `physics-source-1`, `load-reference-source-1` | Straight only. Exact plus source gives the maximum with basis `retained_source_endpoint_normal_max_v1` (unloaded spans; `PPL:5374-5396`) | Refused (`source_recovery.rs:579-585`) | Refused |
| `preview-physics-retained-1`: private, behind the capture permit and the registered build (`PP/src/retained_wire.rs:1-28`) | FK product certificate: `Stress{Axial, BendingY, BendingZ, Torsion}` per site and `CircularMaximum` per member (FK `structural/retained/product_certificate/final_case.rs:91-110@U3`) | Refused | Refused |

- **Schema fields.** Rows carry `kind`, `value`, `unit` and `entity_ref`, plus metadata with `component`, `coordinate_system`, `location`, `basis` and `sign_convention`. The enums are in `results.v0.3.schema.yaml:613-700` and `:3850-3950`.
- **Dead kinds.** After U3, `pipe_section_pressure_hoop_stress` and `_longitudinal_stress` have no producer. They remain in:
  - `PPP:51-52` and `:61-62`;
  - `P/core/reporting/result_export/src/retained_precision.rs:2496`;
  - the Python and TypeScript readers;
  - the schema enums.

  ROOT deferred the `PPP:75` wording to the next corpus generation (T3 rulings, "U3, I110's round-4 stop").
- **Retained precision covers** straight-frame component stress rows and the circular maximum only, on a pre-public path.
  - **Not covered:** arcs (W1c), pressure (pressure regions must be empty: `source_recovery.rs:589-608`; `retained_product.rs:1563-1566`), intensified measures and uniform loads on the source routes (`source_recovery.rs:609-610`).
  - `physics-retained-1`, for the exact routes, is T3's B3 and is in phase 0 (WORK_GRAPH T3-B2/B3/B4).
  - So **the stress-recovery precision interface T4 inherits is:** T3 certifies the straight stress functionals that T4 does not change. Every new T4 quantity (arc stresses, maxima, SIF, Lamé on bends, shear) starts outside retained precision. **Inference:** each needs T3's F2b/W1c family work before it can publish under a retained identity.

## 5. Open points for the plan

- Whether the objective formation keeps a `center` field or moves to (d, R, n̂). This is a T3 interface: K-D5, K5 and W1c consume it.
- Whether the curved pressure load is formed exactly, or with a bound that S11-G accepts. Either way it is needed, or curved pressure cases publish Sensitive.
- The arc-maximum method: a trigonometric-basis enclosure, or interval subdivision over θ.
- The section-basis contract (M30): which basis stiffness, mass, stress and pressure each take. Corrosion allowance is the owner's to define as an input.
