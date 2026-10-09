# T4-RV5: refutation of T4-I12's T4-U3 references (the objective connector)

- **Role:** independent reviewer, TASK (Type 2), for T4's WORKING_ITEMS. Brief `R4/BRIEFS/T4-RV_REFERENCE_REFUTATION.md` (sha256 `816c20ab…12db`); terms `R4/BRIEFS/T4_WI_COMMON.md` (sha256 `7d44afd0…02cb`). No delegation, no Git writes.
- **Object:** `R4/T4-I12/` as committed at `a744c09021`; SHA256SUMS digest `9925375b…0f1f`; all nine entries verified OK (from the working tree before it moved, and again from `git show a744c09021:…`).
- **Basis:** `R4/BRIEFS/T4-I12_U3_REFERENCES.md`; `R4/T4-I10/SLOT_TABLE.md`; JR `I/CORRECTNESS_DESIGN/JOINT_REFERENCE/CONTRACT.md` and `INDEPENDENT_REFUTATION.md`; `CONNECTOR_CONTRACT_V1.md`; plan §4.3, §5, §6; `R4/T4_RULINGS.md`; code at `ed012c7ccf` (conventions, admission and the NI loop only). No product build, run or output was used.
- **Out of scope:** T4-I12's round 01 (`2e79cf469e`, `d7945f2f81`), committed while this review ran. It adds five cases and leaves the 18 refuted cases byte-identical (checked).

## Disposition: BLOCKING (one finding; every value passes)

Every load-bearing value of all 18 cases has been re-derived by a different method, and each one agrees exactly. The system case agrees to 30 digits, which is the precision the JSON publishes. T4-I12's scripts reproduce the JSON and all three stdouts byte for byte. There is one **BLOCKING** finding, B-1: the frozen system document is refused by the product's existing input validation, so the case cannot be run as frozen. The repair restores four metadata fields and changes no value. There are also three SHOULD-FIX items and five NOTEs. No stop rule (SP-1 to SP-4) or T3 condition is touched.

## 1. Checks performed (facts)

| Check | Method (different from T4-I12's) | Result |
|---|---|---|
| Reproduction | T4-I12's three scripts re-run from the frozen bytes (Python 3.13.14, `-I`) | JSON and all stdouts byte-identical (`rv5_reproduce_i12`) |
| B, Ke | Chain B = N(L)·blockdiag(Qᵀ)·T_link(aᵢ, aⱼ). N(L) is the Euler–Bernoulli natural-mode matrix, anchored independently: NᵀKN equals the textbook 12×12 beam stiffness for three rational sections, and a sign-flipped N fails. T_link is the rigid end-offset map | All 72 B entries and all 144 Ke entries equal in all 18 unit evaluations (the 6 six-component sub-cases, the companion and the preload state included), plus the B oracle's B |
| End actions | Virtual work: f = ∂U/∂d by exact central differences of U(d), with q(d) evaluated on vectors and not from a stored B. Separately, a midpoint-cut free body | VW = free body = JSON Fᵢ, Mᵢ, Fⱼ, Mⱼ in every case; Ke·d − BᵀKq_ref = f |
| Rigid modes, rank | Exact row reduction; the 6 rigid modes about the case origin | rank B = 6; B·rigid = 0; rank Ke as stated; for PD K, null(Ke) = span(rigid) |
| Definiteness | Sylvester leading minors (determinants), not LDL | PD flags agree; pivots = minor ratios = JSON |
| q_ref | Bᵀ K q_ref formed and its self-equilibrium checked about two origins; reduced solves done independently | RHS, Kq_ref, the stress-free flag, every PRELOAD-RELIEF state and the omitted-RHS discriminator all agree |
| JR numbers | Typed from JR CONTRACT §6 and refutation §§1 and 6, then compared | J1, the common rotation, raw 240 N / 0.36 J, J2 and J2-held, refutation §1 (Fⱼ = −0.2, Mᵢ = −0.4, Mⱼ = 0.8, 0.004 J; 0.6 N·m, 0.003 J), the EB 4EI/L cross-check, the B-oracle blocks, q and 1567/170, coupled H 0.075 J, rescaling (1, 0.5, 9), preload [±0.25], [±1]: all exact |
| Finite rotation | Decimal Taylor series at 80 digits, using the true rotation (R − I)x | qt and uⱼ agree to 38 digits; JR's decimals agree to 13 digits only (|Δ| = 1.1e-16 and 6.6e-18), as T4-I12 states |
| System case | Decimal at 70 digits with π by Gauss–Legendre AGM; textbook EB element; Hermite-consistent loads; I = π(ro⁴ − ri⁴)/4 directly; partial-pivot elimination; inputs read from the JSON document itself | Worst normalized difference against the JSON is **3.3e-30** over u, θ, reactions, q, g, U, F, M and end actions, in all three cases; balance residual < 1e-65 |
| Discriminators | Raw-difference element and the P-130-in-parallel variant, both solved | JSON values reproduced to 1e-17. Minimum gap on the listed components: 2.5e-2 (raw) and 5.6e-4 (parallel) of the floor, i.e. 2.5e7× and 5.6e5× the 1e-9 criterion. Raw imbalance −770 / −275 N·m about X and +440 N·m about Y, which is 7.9e7 to 2.2e8× the balance allowance |
| NI | The loop modelled from my own reading of `NI/src/lib.rs@ed012c7ccf` and nonlinear_supports. The block is formed from the rotated 12×12 frame, not from eeᵀ | All 20 old pinned values reproduced; the replacement values equal T4-I12's (§2.7) |
| Admission | `run_linear_static_preview_observed` gates read in order (`PP/src/lib.rs:2365-2420`) | B-1 |
| Hygiene | grep for absolute, home, temporary and machine paths | None |

## 2. The attack points

1. **JR §2.**
   - B, Ke = BᵀKB, F = Q g_t, M = Q g_r and the four blocks agree with JR §2 by virtual work and by the free body, with node-on-element signs (f = ∂U/∂d).
   - The RHS +BᵀKq_ref and the d = 0 residual −BᵀKq_ref follow JR's sign.
   - Reversal (T, Q′ = QJ, K′ = TKTᵀ, H′ = THTᵀ) and covariance (q, g, U invariant; actions rotate with R) hold exactly.
2. **J1, J2 and the B oracle.** Every JR number agrees exactly, including the oracle's B column by column, q for d_k = (k − 4)/17 and the virtual work 1567/170.
3. **The W4 link rule.**
   - rank B = 6 holds for every geometry: the (uⱼ, θⱼ) 6×6 block is block-triangular with Qᵀ on its diagonal.
   - So a PD K gives null(Ke) = null(B) = the 6 rigid modes exactly.
   - The PSD 4/1/9 case gives rank 2 and nullity 10, and the stated non-rigid vector [0, 0, Q.y, 0] is in null(Ke).
   - The indefinite H has a leading-minor ratio of −9/4.
   - The decision is exact in rationals. N-2 covers stating its operand.
4. **Offsets, preload, coupled H, rescaling, reversal.** All exact, including:
   - a = Q_node·offset_local;
   - the offsets-ignored, Q-transposed and residual-omitted discriminators;
   - H read as K (29/200 J);
   - PRELOAD-RELIEF (q = q_ref and g = 0 with j free; g_tx = −7/36 with uⱼx held);
   - S8 exact 2^b scaling.
5. **Finite rotation.** The exact values are right, and the negative-assertion bound holds. The 1e-12·L criterion is generous for binary64 d.
6. **The system case.**
   - *Values:* right, under the product's conventions as read: As = πt(OD − t), I = As(ro² + ri²)/4, J = 2I (`source_geometry.rs:28-65`, `annulus_geometry.rs:34-38`); G = E/(2(1 + ν)) (`pressure_exact.rs:236-252`, `pressure_material.rs:60-95`); EB (`FK/src/lib.rs:712-815`); thermal ±EAαΔT·x̂ (`PP/src/lib.rs:10668-10773`); Hermite loads (`user_loads` test `:1751`).
   - *Discrimination:* the 770, 275 and 440 N·m are forced by N-140's statics: r × F with Fᵧ = 350 or 125 N, or Fₓ = 200 N. They are therefore mode-independent and discriminate by about 1e8 against the criterion.
   - *658.44 N·m:* unreachable, as T4-I12 says. The legacy figure came from the pressure-stripped 0.1.0 demo with NL-140, NL-130-FRIC, CE-120 and the parallel element (`PP/tests/preview_physics_runtime.rs:1036-1043`). The exact route refuses those supports (`pressure_runtime.rs:179-183`), and the connector is v3-only (D-4).
   - *Admission:* **not as frozen** (B-1).
7. **NI.** The re-derived values are identical to T4-I12's:
   - (10, −10): 4375/7404, 4350/617, −1305/617.
   - (−10, −10): −4375/9276, 9550/773, 2865/773.
   - (10, −1) retry: 12125/14808, 1143/1234 (= Rₓ), −1905/617.
   - (10, −1) final: 12875/18552, −1143/1546, −1905/773.
   - (−10, 1): the same values, sign-reversed.
   - μ = 0: 2 iterations, u = 625/834, no applied force.

   The structure is preserved. Test 1 converges in 2 iterations from both seeds, with identical values from each seed. Test 2 takes 3 iterations: in iteration 2 the derived branch is inadmissible and Sliding is retried, the applied force then flips sign, and the final iterate has f·u < 0 and |f| = 0.3|N|. With the cap at 2 the loop exits non-converged on the derived-normal cause; the classifier residual is 0, so `nonconverged_exit_diagnostic` names "derived-normal". EA/L = 20 and 12EI/L³ = 48/5, so the normal stays affine-coupled. The block is the same for y_reference (0, 0, 1). The tolerance stays 1e-12.

## 3. Findings

**B-1 (BLOCKING): the system document is refused before any connector code runs.**
- *Fact.* `document_v3_0.3.0`'s SH-140 hanger carries only `hanger_type`, `stiffness`, the two references and `mechanics_consumption`. `validate_spring_hangers` (`validation.rs:816`, called at `:22` from `validate_model_inputs`, which runs on every route at `PP/src/lib.rs:2367`) emits two blocking diagnostics:
  - `SPRING_HANGER_LOAD_MISSING`, unless installed, cold and hot loads are positive (`validation.rs:904-915`);
  - `SPRING_HANGER_TRAVEL_MISSING`, unless travel_range or movement_limit is given (`:916-927`).
  
  The envelope is blocked (`MODEL_INCOMPLETE`, no results). The demo carries these fields (installed 460 N, cold 430 N, hot 390 N, travel_range 0.045 m, plus `load_side_review_reference`). The re-authoring dropped them.
- *Consequences:*
  - A correct T4-U3 fails the frozen case.
  - The annotation refusal variant passes vacuously (S-3).
  - An implementer may be pushed to weaken hanger validation, or to drop the hanger, which changes every value.
  - T4-I12 §0.5 checked only the exact-profile gates. T4-I12's round-01 system documents carry the same hanger (`…-002-LR1`, `…-MATERIAL-CONTROL`).
- *Repair (values-neutral).* Restore the demo's hanger metadata verbatim in the document and every variant derived from it. These fields are review metadata only: the spring is built from `stiffness` alone (`PP/src/lib.rs:7388-7404`), and the loads appear only in review rows (`:12104-12120`). Re-check admission against all of `validate_model_inputs` and `validate_support_family_tokens`, not only `validate_profile`. *Optional:* a diagnostics-only probe of the v2 twin (connector removed, P-130 kept as a pipe) through the current PP would settle §0.5's remaining inferences.

**S-1 (SHOULD-FIX): the FK unit criteria lack zero-scale floors.**
- *Fact.* The unit cases specify "relative 1e-12". Only `U3-J1-COMMON-ROTATION` (q_t, g_t, U) and `U3-RAW-DIFFERENCE-NEGATIVE` state floors.
- *Exact zeros without a floor:*
  - entries of B with a skew Q, e.g. COVARIANCE and GENERIC `B[0][5]`;
  - J2-ROTATION's cancellation zeros: qt, g_t, F, Fᵢᵧ and Fⱼᵧ;
  - PRELOAD-RELIEF's g = 0 and its zero reactions;
  - COMMON-ROTATION's end moments, which have no moment floor.
- *Evidence.* A plain binary64 formation of JR §2 gives −1.665e-16 at COVARIANCE `B[0][5]`, against an exact 0 (`rv5_unit_criteria_probe`). A different association gives 1.7e-16 at GENERIC's. A correct product therefore fails a literal reading.
- *Repair.* One rule for all FK unit arrays: |obs − exp| ≤ 1e-12·max(|exp|, max|array|) per array or family, as the system case does. Add a moment floor to COMMON-ROTATION. No value changes.

**S-2 (SHOULD-FIX): the system case depends on Euler–Bernoulli frames (D-6).**
- *Fact.* If D-6 makes Timoshenko the default for new v3 documents, this case's values change. *Inference:* φ = 12EI/(κGAL²) is about 0.010–0.035 for these spans (κ ≈ 0.5), which is far above 1e-9.
- The record should state that the case requires an explicit EB selection, or that it is re-frozen under D-6. This parallels T4-RV4's S-2, which is not yet listed in HELP_HUMAN's D-6 note.

**S-3 (SHOULD-FIX): a refusal variant can pass for an unrelated reason.**
- `annotation_only_joint_on_exact_route` expects only `MODEL_INCOMPLETE` with no results. It must also require a blocking diagnostic whose refs include `component:C-150`, plus T4-U3's code once that code is chosen.
- Also give concrete document patches for `joint_case_with_pressure_region` (a well-formed region) and `series_or_parallel_topology` (the topology objects). Each should be refused for the joint reason, not for malformed input.

**NOTEs.**
- **N-1, plan §5 wording.** The T4-U3 row's "658.44 N·m now balancing" is met by the v3 analogue: imbalances of 770, 275 and 440 N·m that would arise without the connector, against a balance below the criterion with it. WI should record the substitution; no stop rule is involved.
- **N-2, the W4 operand.** The JSON gives pivots of K for the PD and PSD cases, and of H for the indefinite one. The inertia is the same (H = DKD), but the record should say the exact decision is taken on the authored binary64 H. A binary64-formed K is rounded when Ls is not dyadic; all Ls here are dyadic. The record should also say that a zero pivot with a nonzero remaining column is indefinite, not skipped.
- **N-3, coverage.** Two controls are not frozen: JR §6's "zero-length explicit Q works", and the CONNECTOR_CONTRACT §2 refusal of a Q.x not aligned with r. Under `replaces_span` only, r = 0 arises only through offsets. Add small unit cases, or record why they are omitted.
- **N-4, the B oracle.** `U3-B-ORACLE` supplies g, not K and d. A product test has to form Bᵀg from `b()`, and the case should say so.
- **N-5, independence.** No value was taken from the product. The system conventions and the NI loop were read from code, which the brief permits. T4-I12's NI model agrees with mine. I wrote mine without reading T4-I12's code.

## 4. Coverage, transport, hygiene

- *Coverage:* brief items 1–8 are all present, apart from N-3. The excluded items (J3, J4, series and parallel, the 0.4.0 form) are excluded by the brief and the rulings.
- *Transport:* inputs are complete and decimals have at least 17 digits, except B-1 and S-3's patches. The provisional wire fields are marked (§0.8).
- *Hygiene:* placeholders only.

**Files** (`R4/T4-RV5/`):
- `REVIEW.md`;
- `_run_records/{rv5_connector, rv5_system, rv5_ni, rv5_unit_criteria_probe, rv5_reproduce_i12}.py`, each with its `.stdout.txt`;
- `SHA256SUMS`.

Run each script as `WT/venv/bin/python -I <script> <frozen u3_reference_cases.json>`. `rv5_reproduce_i12` instead takes `<frozen dir> <empty scratch dir>`. The frozen bytes come from `git -C NUM4 show a744c09021:R4/T4-I12/<file>`.
