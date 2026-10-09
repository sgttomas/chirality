# RV130: T3's independent review of T4-I10's slot table (T4-U3)

**Reviewer.** RV130, Type 2, fresh instance. Dispatched by WORKING_ITEMS for T3 (Agent 1), the return path. No delegation. Brief `R/BRIEFS/RV130_T4_I10_SLOTS.md` (sha256 `025d7850…6df6a74b`, verified at NUM `6784c7df12`); `R/BRIEFS/B1_COMMON.md` host and records rules, with WORKING_ITEMS in ROOT's place.

**Basis.**
- **The design** (read with `git show`, never checked out): branch `codex/piping-t4-pressure-stress-20261009` at `471ad93f48`. `R4/T4-I10/SLOT_TABLE.md` sha256 `57a565e3…6e99` (verified). `R4/T4-I10/SHA256SUMS` sha256 `e8e7db1a…0e0b`; all 8 listed files verify.
- **T4's rulings:** `R4/T4_RULINGS.md` at `1b682630e4`, a descendant of `471ad93f48`. It rules SP-1 as a declared exception, the refused-demo re-pin, the residual shape (legacy code), and that annotation joints are refused on the exact route. That last ruling postdates the slot table.
- **The code basis:** `ed012c7ccf` (main `ec5d397359` plus T3's U3). `b2` `e582b61f9e`, also from `ec5d397359`; `origin`'s `b2` head is still `e582b61f9e`.
- **T3's authority:** RR "Owner decision: M07's flawed joint element, option A; …", RR "T4 plan 01's annex A: T3's agreement recorded; …", `R/I115/t4_annex_check_01/RETURN.md`, the five T3 constraints in the brief, and `T/DESIGN_NUMERICS/S11G_GUARD.md` (revision 2.2) and `DESIGN.md` §4.3.1.

**Method.**
- Read-only: `git show`, `git archive` into `WT/scratch/rv130/`, and `git merge-file -p` on scratch copies. No cargo, no Git write in any worktree, and `WT/t4` untouched.
- An independent census of the old joint's reach (`_run_records/rv130_sites.py`), different from T4's `sites.py`. It scans the whole basis tree (fixtures, apps, schemas and docs included) for a wider token set, finds enclosing functions by brace depth, and maps each hit onto the slot table's citations.
- Exact-rational checks of the connector mathematics (`rv130_connector_math.py`).
- A shape enumeration (`rv130_joint_shapes.py`).
- Three-way merge simulations against `b2` (`rv130_overlap.py`, `rv130_lib_gaps.py`).
- T4's `sites.py`, `b2_overlap.py` and `friction_basis.py` were re-run, and all three reproduce their committed stdout byte for byte.

## Verdict: PASS WITH AMENDMENTS (0 BLOCKING, 9 SHOULD-FIX, 10 NOTE)

The slot table is sound in structure, and its mathematics on T3's surfaces is right. Every item 1–11 can be agreed on the conditions below. The amendments are text changes to the slot table and test plan, made before code.

## Findings

### SHOULD-FIX

- **S-1 (slot coverage).** The replaced span still reaches published per-pipe evidence, and S20 does not list it.
  - `exact_case_evidence` builds `"pipe_sections"` from every `built.pipes` entry (`PP/src/lib.rs:5568`), with `.expect("every built exact member has source geometry")`. `formation_entity_bodies` also maps every built pipe (`:1207`).
  - S20 lists only the recovery loop (`:4927`, with `:4933`, `:5060`, `:5236`, `:5359`).
  - Under `replaces_span` the pipe stays in `built.pipes`, as curved spans do. An exact-family case with `pressure_regions: []` would then publish a section record for a span that is not assembled. Whether it does depends on T4-U2a's v3 evidence builder.
  - **Amend S20:** exclude replaced spans from every published per-pipe evidence list, or state why one remains, and have T4-U2a's v3 evidence follow the same rule.
- **S-2 (no silent skip; rulings).** §4.2's row "no connector, `not_solver_consumed` → admitted as annotation" admits annotation joints on v3. `RETURN.md` also proposes exempting them from `JOINT_PRESSURE_INTERFACE_UNRESOLVED`.
  - Both are superseded by T4_RULINGS at `1b682630e4`: annotation joints are admitted only on the pressure-free route. On v2 they take the composition refusal; on v3, the seam's named refusal.
  - **Amend §4.2** to that ruling, and name the v3 code.
- **S-3 (K-D5; item 5).** The table re-forms r in `Wide<2>` but does not say how the binary64 path forms r.
  - **Specify r = (xⱼ − xᵢ) + (aⱼ − aᵢ).** Never form the absolute attachment positions pᵢ = xᵢ + aᵢ (compare T4-U1's "never form an absolute centre").
  - **The probe** (`rv130_connector_math.py` §E): one connector, J1's K, nonzero offsets, node i restrained.

    | Coordinates | r error, absolute-position form | r error, node-difference form | K-D5 trigger, absolute | K-D5 trigger, node-difference |
    |---|---|---|---|---|
    | Ordinary | 2.7e-16 m | 2.9e-17 m | 1.35e-6 | 1.01e-6 |
    | UTM | 2.8e-10 m | 2.9e-17 m | **1.39** (demotes) | 6.5e-7 |

  - So only the UTM case kills the absolute-position form, and only when the offsets are nonzero: with zero offsets, both forms give the exact r.
  - **The required "undemoted at UTM" case** therefore carries nonzero offsets whose sums are inexact at UTM magnitude, a skew Q and a coupled K (H_tr ≠ 0), in both modes.
- **S-4 (S11-G S13; item 6).** The `Formation::Bounded` bound on +BᵀKq_ref must be a proven upper bound on |fl(term) − exact(term)|, where the exact term is formed from the binary64 held operands (xᵢ, xⱼ, aᵢ, aⱼ, Q, K, q_ref).
  - **Write the r operand as |xⱼ − xᵢ| + |aⱼ − aᵢ| per component, not |r̂|.** Under cancellation (JR admits coincident attachments) a bound on |r̂| fails. In 2,000 decimal-authored coincident-attachment cases, |r̂ − r| > γ₃|r̂| in 1,083. The operand-magnitude bound holds, at 0.22 of γ₃ at most (§F).
  - **State the full rounding count:** r, the Qᵀ·S products, K·q_ref and Bᵀ·g, rounded upward.
  - **In T8's FORMATION_SITES entry,** list the bound helper's name as a token, as `push_exact_pressure_operands` lists `exact_pressure_operand_bound(`.
- **S-5 (W4 successor; item 4).** The deleted T4 tripwire (`FK/tests/k5_constrained_bodies.rs:992`) proved, bit for bit, that W4's tie space is the null space of the **represented** binary64 element. The connector's binary64 Ke = fl(BᵀKB) is not exactly rigid-null, so that form cannot carry over. The successor must state the claim on the exact B formed from the connector's own binary64 inputs, and it needs four parts:
  - (a) rank B = 6 and B·rigid = 0 for the six modes about an arbitrary origin. Cases: UTM coordinates, offsets, skew Q, r = 0, coincident node positions.
  - (b) a tripwire property: the test fails if the FK formula changes. For example, FK's `b()` agrees entrywise, within its rounding, with the exact B from the same inputs.
  - (c) classification tests: PD → link; singular or indefinite → `ConnectorSemidefinite`. They include a PSD (hinge) case that is a real mechanism, so a "PSD as link" mutant publishes Restrained and is killed.
  - (d) **B10 scans the PD decision function.** B10 scans only `rigid_body.rs` (`k5_constrained_bodies.rs:22`), so widen its sources if the function lives in `FK/src/connector.rs`.

  The PD decision is taken on the same binary64 K the assembly uses (after the decode from H, Ls).
- **S-6 (W1 first; item 11; constraint 4).** Every new joint input must ride inside the `objective_connector` Value (or be `Option<Value>`): JR's `JointHardware`, `JointPressureModel`, the calibration descriptor and the topology.
  - **Why.** A new serde-typed field on `PreviewComponent` puts a parse error ahead of W1's admission (`CapturedInvocation::parse`, `PP/src/lib.rs:2258`, runs before `admit` at `:2263`).
  - **Make this explicit for these fields.** §4.3 already says nothing is added to `parse`.
  - **Units.** The Value bypasses `normalize_model_units` (`:8146`), so the decoder converts or refuses its units itself.
- **S-7 (constraint 5).** §4.3's list of priced layouts that must not change omits `straight_pipe::StraightPipeElement`, which is `BuiltModel.pipes`' element and is priced in `retained_memory.rs`. It also omits `LinearSupport`, `SpringEntry`, `PrimitiveLoad` and `StationResultants`.
  - **Add them.** S20's replaced-span skip must use a lookup set, as `curved_bends_by_pipe` does, never a new field on `StraightPipeElement`, `FrameElement` or `PreviewPipe`.
- **S-8 (test coverage).** `PP/src/f1b_tests.rs:571` asserts that F1b's declared subset covers user elements (`:597 assert!(users > 0, "user stiffness elements")`). The table marks it M.
  - After T4-U3 it is an R: it needs a v3 connector request in the declared subset.
  - Otherwise F1b's dense/sparse wiring parity loses connector coverage, or the assertion is dropped.
- **S-9 (S11-G recovery; item 6).** With connector rows outside R-b′, as curved rows are, connector rows are guarded by neither K-D5 nor S11-G. Member actions are outside EF (DESIGN §4.3.1), and R-b′ is excluded.
  - Their formation noise is about γ·|B||d| from the B̂ entries alone. Rigid translations cancel exactly (the ±Qᵀ columns), so what remains comes from rigid rotation × (|a| + |r|).
  - **Accept it as curved is accepted,** but record it in S11-G's change record as a declared coverage limit.
  - **Form q − q_ref inside one exact sum** before rounding.
  - `RecoveryRecord` stays unchanged.

### NOTE

- **N-1.** A missed test site: `PP/src/source_recovery.rs:1630-1633` (`#[cfg(test)]` `Fixture::new`) calls `assemble_global_stiffness_with_user_elements` with `built.user_stiffness_elements`. It is mechanical, and the compiler forces it.
- **N-2. Not dispositioned:**
  - the legacy-field unit validation and normalization: `normalize_model_units` (`PP/src/lib.rs:8466`, `:8621-8650`, `:8777-8840`) and `validate_units` (`PP/src/validation.rs:601`, `:734-791`);
  - the validation helpers: `validation.rs:1556`, `:1776`, `:1812`, `:1841`, `:1857`.

  State whether they are kept (documents stay readable) or deleted. As they stand, an annotation joint carrying legacy rates in a bad unit is refused by `validate_units`.
- **N-3. Site tables.**
  - S15 also needs rows for every new rule-8 accumulation in files FK's `s11_site_table.rs` already scans: SA, `formation_check.rs`, `FK/lib.rs` and `sparse.rs`. S4's two-stage allowance is likely to add some.
  - T8 and rules 5–6 of `s11f_site_test.rs` scan only the listed `PRODUCT`/`KERNEL` sources. The T4-U3 diff reviewer must confirm that no new PP module pushes, folds or solves; any that does goes into `PRODUCT`.
- **N-4. The `s11f` hunk (b).**
  - Its gap to `b2` is **32** unchanged lines in the post-U3 base; the slot table's 36 is in main's coordinates. It merges cleanly either way.
  - The count-0 producer row is optional: rule 8 only checks that a listed count-0 name exists. So (b) can be a pure deletion of `:511`.
- **N-5. K2b scaling.** Forming the scaled connector as Bᵀ(2ᵇK)B equals 2ᵇ·fl(BᵀKB) bit for bit only if no intermediate is subnormal, and the census covers only K and the formed Ke entries.
  - Scale the formed Ke (`force_scaled_matrix`, as curved does), or census the intermediates.
  - F1b refuses connectors at b ≠ 0, so nothing is published either way.
- **N-6. An unspecified shape.** A valid v3 connector whose `mechanics_interface.solver_consumption` declares something else, e.g. `not_solver_consumed`, is not covered (4 of 360 enumerated shapes). Refuse it as `OBJECTIVE_CONNECTOR_INPUT_INCOMPLETE`, or define it.
- **N-7.** "Stress-free (Kq_ref = 0) gives no terms" must be decided exactly. With a PSD K and q_ref in null(K), binary64 K·q_ref can be a tiny nonzero.
- **N-8. The PD decision method.** An exact LDLᵀ over rationals, with no square root, is sound. So is a one-sided certified test that never answers PD wrongly; an uncertified K is then unqualified. Section §D shows why a tolerance test is not enough: binary64 pivots [3, 0] for a block that is exactly indefinite.
- **N-9. Authoring surfaces for J-B to disposition** (not T3's):
  - OA's contract case `case_67_accept_set_field_component_expansion_joint_stiffness.json`;
  - `schemas/component.schema.yaml` and the component libraries carrying the four rates;
  - `tests/test_component_section_schema.py`'s completeness codes. These share names with the PP warnings T4-U3 removes, but are separate.
- **N-10. The M03 text's fixture radius.** At `b2` the M03 text is pinned only in the precision-1 pair, which U3 deletes; after J0b, nowhere. Any T4 fixture with a curved (mixed) body published before T4-U3 carries the old text, and T4-U3 would then re-pin it (item 3).

## 1. Slot coverage (independent census)

**The census** (`rv130_sites.stdout.txt`): 1,086 token hits at `ed012c7ccf`.
- 595 are in `.rs`, `.ts`, `.tsx` and `.py` files; 319 of those map to a slot-table citation.
- The rest were dispositioned by hand:
  - **Covered by the table, but the parser missed the mapping:**
    - continuation lines after an arrow (S18's builder lines `PP/src/lib.rs:7337-7593` were attributed to `preview_physics.rs`);
    - rows with an empty path cell (the `f1b_tests` helpers);
    - generic rows ("TS and OA authoring tests (J-B)", "NI fixtures …", "Harness …");
    - doc comments (S8, S10–S12 docs);
    - the U3 tests' comments.
  - **The legacy input surfaces:** TS authoring (`PropertyInspector.tsx`, `ModelTree.tsx`, `types.ts`, `modelView.ts`, `NativePackagePanel.tsx`), OA's `field_rules` and its creation resolvers, and their tests. These are commit 7 (J-B) and not T3 surfaces.
  - **The H-4 row kind and summary key** (`ReportPanel.tsx`, `records.py`, `retained_precision.py`, RE, semantic contracts, successor fixtures): unchanged until B7, as ruled.
  - **Missed:** S-1 (the replaced span in published evidence), N-1 (a test site) and N-2 (unit validation and normalization).
- **Non-code files:**
  - historical REPRO and witness records: unchanged;
  - the refused demo's model and envelopes: SP-4, item 10;
  - the reviewed semantic contracts: the H-4 row kind and the retired `expansion_joint_pressure_thrust_load_review`, both untouched by T4-U3;
  - docs: N-9 and §4.5's README list.

**The slot citations checked against the bytes:** S1, S5, S8, S9, S11, S12, S16–S20, §4.4 and the T8 claim. They hold, except S-1 and N-1.

## 2. No silent skip (item 8; §4.2)

**The shape enumeration** (`rv130_joint_shapes.stdout.txt`): 360 shapes (version × connector state × consumption × pipe ref × rates), with T4_RULINGS' amendments applied. Every shape reaches a named blocking code or an admitted path, and none falls through. One admitted shape class is unspecified (N-6). The v3 annotation row follows the ruling, not §4.2 (S-2).

**The old-to-new code map covers all 11 joint codes PP emits today.**
- **The gate:** `JOINT_ELEMENT_STIFFNESS_INCOMPLETE`, `_MAPPING_UNRESOLVED` and `_EQUILIBRIUM_UNQUALIFIED` (`preview_physics.rs:145`, `:181`, `:207`).
- **The builder:** `EXPANSION_JOINT_MACRO_ELEMENT_INPUT_INVALID` (`PP/src/lib.rs:7588`).
- **Validation:** `EXPANSION_JOINT_MECHANICS_INTERFACE_UNSUPPORTED` (`validation.rs:1159`), five input warnings and `…USER_STIFFNESS_REVIEWED` (`:1317-1395`).
- **Where they go:** four map to the legacy code or a named connector successor; `MECHANICS_INTERFACE_UNSUPPORTED` becomes the legacy code or the annotation info; six are removed.

**The backstops, verified in code:**

| Backstop | Where | What happens |
|---|---|---|
| NI | `solve_active_set_frame_with_mode_and_springs` validates first (`NI/src/lib.rs:579`) | errors map to blocking `NONLINEAR_SUPPORT_LOOP_BLOCKED` (`PP/src/lib.rs:6740-6750`) |
| W1 | `F::Components` (`retained_memory.rs:755-756`, `:801-802`) | refused before any joint code |
| Source | the components clause (`source_recovery.rs:579-585`) | already covers connectors |
| K-D5 | `FormationCheckUnavailable` on any failure (`formation_check.rs:155-180`) | demoted to Sensitive |
| F1b | §4 | refused at b ≠ 0 |

**U3's four tests** (`PP/src/lib.rs:17393`, `:17409`, `:17471`, `:17543`) move to the legacy code with their shapes kept. Every incomplete or unmapped joint stays refused, so T3's annex condition 6 holds.

## 3. T3's constraints

| # | Constraint | Result |
|---|---|---|
| 1 | Incomplete or unmapped joints stay refused, with a code map | **Holds** (§2). Successor granularity for legacy joints is one code (D-4: nothing solved or converted). Named connector successors exist. N-6 is open |
| 2 | W4's tie reduction stays; only its producer goes | **Holds.** `assess_constrained_bodies` and `reduce_constrained_body` are untouched. `user_element_tie`, `TieRefusal` and SA's `UserTie` are deleted, and SA passes `&[]` ties. The K5 corpora are unchanged |
| 3 | Edits stay out of `retained_product.rs` and `s11f_site_test.rs` where possible; exact hunks where not | **Holds, with exact hunks.** `retained_product.rs`: one line, `:1558`. `s11f`: (a) insert after `:221`, (b) `:511`, (c) insert after `:1382`. No other `s11f` row moves: `run_linear_static_preview_observed`'s rule-8 count stays 2, since `a() + b()` is not a rule-8 shape (`s11f:868-885`) |
| 4 | W1 refuses component models before any joint-specific code | **Holds.** `objective_connector: Option<serde_json::Value>` (`PP/src/lib.rs:363`); `parse` at `:2258`, admission at `:2263`. Condition S-6 |
| 5 | `LIMITATIONS`, reviewed-input text, PP's lock and the priced layouts stay byte-identical | **Holds.** `LIMITATIONS` (`preview_physics.rs:73-81`) is untouched: T4-U3 deletes only `:106-213`. No reviewed input is edited (14 at the basis, 17 at `b2`; the 9 semantic contracts keep the H-4 row kind). PP's `Cargo.lock` is unchanged, because the connector is a module with no new crate edge. No priced layout is edited. Condition S-7 |

## 4. The mathematics on T3's surfaces

**W4 (item 4).** The link rule is correct (`rv130_connector_math.py` §A–C).
- **The exact checks.** For 60 exact-rational cases, rank B = 6 and B·rigid = 0 for all six modes about an arbitrary origin: 15 general, 15 with r = 0, 15 with coincident node positions, and 15 with a binary64 Q (only invertible).
- **PD and PSD.** For PD K, rank(BᵀKB) = 6, so null(BᵀKB) = null(B) is the pair's rigid space: a link, joining one objective sub-body. For a PSD K of rank 5, rank(BᵀKB) = 5: a release, correctly unqualified and left to the matrix gate.
- **What the reduction did before.** The old element's "tie" {uᵢ = uⱼ, θᵢ = θⱼ} is strained by a rigid rotation when r ≠ 0. That is why W4 represented it with virtual positions.
- **Deciding PD.** "Exactly and libm-free" is achievable (N-8). The successor tests and B10 are S-5.

**K-D5 (item 5).**
- **The decode is outside EF.** Decoding K = D⁻ᵀHD⁻¹ from (H, Ls), and aᵢ from Qᵢ and the offset, is input representation. D1 §4.3.1: "EF is blind by design to the difference between the intended and the represented binary64 inputs". The precedent is a frame's binary64-derived section values, which K-D5 takes as given.
- **The conditions:**
  - one decode feeds every consumer: dense and sparse assembly, NI-linear evidence, the census, the q_ref term, recovery, W4's PD decision and K-D5;
  - the decode is covered by independent reference tests (H → K congruence, the offset frames), because K-D5 cannot see a decode defect;
  - r, S(·), Qᵀ and BᵀKB are re-formed inside EF, at p = 128.
- **The required kills are real,** on S-3's conditions:
  - The "undemoted" cases kill a residual lateral or unavailable demotion, and any B convention mismatch between the product and K-D5. At UTM with offsets, they also kill absolute-position formation.
  - "A perturbed Ke demotes" kills a K-D5 that skips connectors or shares the product's Ke. It must perturb only the product's assembled matrix, above the criterion, with an unperturbed control that passes.

**S11-G (item 6).**
- **+BᵀKq_ref is correctly a formed `Formation::Bounded` term.**
  - It is self-equilibrated exactly, because B·rigid = 0 makes it orthogonal to every rigid mode, so its net force and moment are zero. The precedent is curved thermal K·u_free.
  - The flag only adds |t| to P.
  - The term's bound goes into B, which is judged against the **unfloored** T0 (`load_ledger.rs:640-644`; `formation_guard.rs:216-241`, `row.bound >= t0`). So the SF-4 floor cannot hide it.
  - SF-4's premise, a defect ≤ u·|t|, does not hold for this term, but nothing relies on it here.
  - Condition: S-4.
- **Connector rows outside R-b′, `ExactAccumulator`, `RecoveryRecord` unchanged:** agreed, with S-9.

**F1b (item 7).** It fails closed at b ≠ 0.
- **The order:** the family check comes first (`PP/src/lib.rs:1558`).
- **The code:** `NotAdmitted` maps to `NUMERICAL_INTEGRITY_UNRESOLVED` ("range: family not admitted under force scaling: …", `:1806-1810`).
- **Before any publication:** admission (`:1475`) precedes publication (`:1485`), and b = 0 returns `NotEngaged` (`:1472`).
- K2b's census and scaling with connectors only choose b (N-5).

**Item 11.** Agreed, with S-6.

## 5. Items 1, 2, 3, 9 and 10: facts

- **Item 1.** `retained_product.rs:1558`: `|| !built.user_stiffness_elements.is_empty()` becomes `connectors`.
  - `b2` inserts 5 lines after main 1554 (ED 1552), and U3 deletes main 1563. Between them are five unchanged lines.
  - The simulated merge of T4's hunk against `b2` + U3 is clean.
- **Item 2.** The `s11f` hunks (a)–(c) merge cleanly. Gaps in the post-U3 base: 322, **32** and 839.
  - T8 (`s11f:1429-1481`) looks items up only in `PRODUCT[0]` = `PP/lib.rs`, and maps every formed site to `PP/lib.rs` (`:1475-1479`).
  - FK's row `:194` (`add_relative_dof_stiffness`, 4) goes. N-3 applies.
- **Item 3.**
  - **The M03 text:** `SA:1539`, in `symmetry_basis` for every unqualified body.
  - **The strict-gap reason:** `SA:2577`.
  - **Neither is a reviewed input, a successor pin, a reader corpus string or a committed fixture string** at the basis: no fixture holds "mixed or explicit-matrix" or "mixed/curved/user/affine".
  - **T3's pins:** `SA/k5_tests.rs:1226` (the K5 test's "basis text unchanged") and NI `:4780` and `:4922` (substrings).
- **Item 9.** The readers reject retired codes:
  - RE `preview_physics_evidence.rs:51`, `:304`;
  - PY `core/analysis_runs/preview_physics_evidence.py:24`, `:242`;
  - TS `previewPhysicsEvidence.ts:14`, `:238`.

  So extending their lists with `JOINT_ELEMENT_*` would make historical results unreadable. `REVIEWED_INPUTS` are the retained reader's statics. W1 refuses components, and v3 is not a W1 route.
- **Item 10.** The two refused-demo envelopes, identical at sha256 `2cb29453…`, are blocked today by 4 `PRESSURE_MODEL_REAUTHOR_REQUIRED` and carry the info `EXPANSION_JOINT_USER_STIFFNESS_REVIEWED`.
  - After T4-U3 they gain the legacy code and lose that info. Their `LIMITATIONS` strings are unchanged.
  - The hash appears only in `preview_physics_fixture_generation.json:1038` and `:1066`.
  - **Consumers:**
    - the shared tamper vector uses the sparse file as base "blocked". Its variants C2, V7 and A4-N8 address no diagnostic by index, so C2 must still be "accepted";
    - `tests/test_preview_physics_consumer_contract.py:1024` checks the hash against the manifest and the status;
    - `App.test.tsx:14697` checks the status and the rows.
  - `result_export_v0_2.json`: confirmed, no re-pin. Its joint strings are model-input `completeness` values, and the HR test refuses the joint, then re-runs joint-free (`HR/src/result_envelope_binding.rs:446-480`).

## 6. The `b2` overlap, re-measured against `e582b61f9e`

`B2U` = `b2` merged with U3 (base main) is clean for all three files. T4's hunks merge cleanly against `B2U` (base `ed012c7ccf`), and every hunk and every `b2` line survives.

| File | `b2` (in post-U3 coordinates) | T4-U3 | Gap (unchanged lines) |
|---|---|---|---|
| PP `lib.rs` | 13 hunks, ED 2176–3423.5 | about 33 sites | ≥ **114**: ED 3538-3545 (114.5), ED 2050 (126), the gate call ED 2412 (207.5), the summary count ED 2779 (180) |
| `retained_product.rs` | insert after ED 1552 | `:1558` | **5** |
| `PP/tests/s11f_site_test.rs` | insert after ED 543 | after `:221`, `:511`, after `:1382` | 322 / **32** / 839 |
| `retained_product_tests.rs`, RE contract test, `previewService.ts`, FK `structural.rs`, `retainedPrecision.ts` | `b2` hunks | none (H-4; S10 needs no new export) | — |

T4-U3 must re-run the merge against `b2`'s actual head before landing; J0b changes the base.

## 7. Items 1–11: recommendations (WORKING_ITEMS decides)

| # | Recommendation |
|---|---|
| 1 | **Accept the one-line hunk.** It is merge-clean. The predicate alternative still edits `retained_product.rs`, in T3's lane, for no gain. Re-run the merge before landing |
| 2 | **Accept hunks (a)–(c) exactly;** (b) may be a pure deletion (N-4). FK: drop row `:194`, add `connector.rs` to `SOURCES`, plus N-3's rows. **Keep T8 unchanged,** with the producer in `lib.rs` outside `b2`'s range, e.g. beside `push_exact_pressure_operands` (`:3897`, gap 473) |
| 3 | **Correct both texts in T4-U3, as declared changes, not at B7.** The published-text rule applies (RR U3 Stage 2 ruling 4), and neither text is a reviewed input or corpus string. T3 re-baselines `SA/k5_tests.rs:1225-1226` to the corrected text (its purpose, that W4 adds no text, is kept) and NI `:4780` and `:4922`. Mind N-10 |
| 4 | **Agree on the link rule** (exactly verified). Conditions: S-5. **B10 scans the definiteness function: yes** |
| 5 | **Yes, outside EF,** on §4's three conditions. The kills are real, with S-3 |
| 6 | **Agree,** with S-4 (the bound) and S-9 (disclosure and the exact q − q_ref) |
| 7 | **Agree, fails closed.** N-5 |
| 8 | **Confirm the map and the backstops,** with S-2 and N-6. A T3 reviewer re-checks on the diff |
| 9 | **Yes,** outside `REVIEWED_INPUTS` until B7, or until W1 admits v3 components. Do not extend the readers' retired-code lists |
| 10 | **Accept** the three files (two envelopes and the manifest), regenerated by the committed recipe. Mechanical byte evidence: the old bytes with only the declared diagnostic edits equal the regenerated bytes, and the three readers still accept tamper variant C2. `result_export_v0_2.json` needs no re-pin |
| 11 | **Agree,** with S-6 |

## 8. Evidence (`_run_records/`)

Commands, run from `WT/scratch/rv130` with `WT/venv/bin/python -I`. All five reproduced byte for byte on a second run.

| Script | Command | Output |
|---|---|---|
| `rv130_sites.py` | `rv130_sites.py NUM <SLOT_TABLE.md extracted at 471ad93f48>` | `rv130_sites.stdout.txt` |
| `rv130_overlap.py` | `rv130_overlap.py NUM <scratch>` | `rv130_overlap.stdout.txt` |
| `rv130_lib_gaps.py` | `rv130_lib_gaps.py NUM <scratch>` | `rv130_lib_gaps.stdout.txt` |
| `rv130_connector_math.py` | no arguments | `rv130_connector_math.stdout.txt` |
| `rv130_joint_shapes.py` | no arguments | `rv130_joint_shapes.stdout.txt` |

**Host.** No cargo or heavy job ran, and no Git write was made in any worktree. Scratch is `WT/scratch/rv130/` only. Nothing was written to the system temp directory.
