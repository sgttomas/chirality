# Bounded retained-source solve and recovery design

Status: HELPS_HUMANS proposal for ROOT selection and WORKING_ITEMS implementation; no production change, new-method admission, Current qualification or release. Date: 2026-09-24 local. The active author is `/root/numerical_resume/source_recovery_design`, commissioned by ROOT `/root` through WORKING_ITEMS `/root/numerical_resume`, which is also the actual harness-native parent. The assigned corrections checkout is the only basis used; the larger successor checkout was not touched.

## 1. Selected purpose and limits

The ROOT brief requires a general retained-source solve for complete connected free blocks of order at most two, plus member/spring linear-function recovery before binary64 projection. Preserve the analytical relative 1e-9 criterion, exact contact semantics, protected checks and historical evidence. Eligibility must follow actual equations and recovery-source support, never fixture IDs, named nodes, a coordinate fixture, chosen load magnitude, or a convenient result. No precision2 persistence framework or mandatory comparison-inverse certificate is proposed.

The design interpretation is to extend the existing private `exact_boundary` arithmetic and owned-response seam, with a small source-bound recovery plan and a separate product adapter. Exact source-solving can be selected after an ordinary route reports assembly loss or sensitivity, provided independent source completeness, admissible family, positivity, equilibrium, recovery and projection conditions pass. This is a new bounded selected method; it is not a silent change to existing strict-gap integration's ordinary-precondition rule. ROOT owns prospective selection of that method and its combined carrier semantics.

The current Sensitive containment (freeze04 per parent's final update) remains correct until that selection and its implementation evidence exist. A newly accurate displacement with unproved or mixed force recovery must remain unqualified. A source certificate is specific to declared binary64 operands; it is not exactness of pi, geometry, material properties or physical engineering reality.

## 2. Retained source and eligibility

Use the actual load-case/material basis and final selected state. Freeze before reduction/scaling/factorization:

- Complete ordered stiffness terms, original represented aggregate, free/global map and prescribed `(global_dof, value_bits)` partition. Existing `AssemblyEvidence` already retains global element entries and springs separately. It does not currently attach element/support identity to every `StiffnessContribution`.
- Complete identified load terms, including small tails, or an explicitly weaker `DeclaredVector` basis. For source-preserving product admission, build identified terms at the actual load-producing seams rather than reconstructing them from the final summed vector. Nodal loads, constant effort, uniform/thermal/pressure contributions must each be covered if present. No empty list or zero-value shortcut proves an unsupported producer absent.
- Recovery descriptors from the same built elements/supports/load producers: actual local matrix, actual transform, scatter map, element/support IDs, units, end/station/sign convention, and fixed-end/initial-strain/affine load terms. Retain stable offsets or an owned companion source table identifying which ordered assembly/load contributions each descriptor owns. A caller-authored label alone is not coverage.
- Original authored input/case identity and normalized operand bits; basis/material changes invalidate reuse. IDs serve provenance and output mapping only.

Run existing Context validation: finite inputs, dimensions, complete disjoint partition, ordered contribution coverage against the supplied aggregate, exact source symmetry, and exact nonzero free graph. Every free connected component must have size <=2. For each singleton require a>0; for each 2x2 symmetric block require a>0 and ac-b²>0 in exact admitted arithmetic. Wholly constrained systems have no free positivity obligation but still require complete source, imposed values and correct reactions/recovery. Retain model-family/geometry evidence separately from the represented-block proof. A failed exact minor is not by itself a physical mechanism diagnosis.

The existing hard ceilings remain 256 DOFs, 16,384 source terms and supported expansion/range limits; defaults are 256 expansion terms and 2,000,000 conservative charged operations. Recovery terms, descriptor copies, checks and replays must consume explicit bounded resources too. Do not quietly raise those values to fit a case.

### Local/global source compatibility and rotations

For element scatter E and local displacement transform T, the mechanical identity is K_e = Eᵀ Tᵀ K_L T E and d_L = T E u. Current `AssemblyEvidence` stores already rounded global element entries; `straight_pipe::recover_local_forces` recomputes K_L and T then performs floating products. These are different arithmetic sources unless compatibility is established.

Minimum adapter: supported straight frames, ground springs, fully represented supported loads, and an exact comparison showing the retained local/transform recipe yields the same element stiffness source used for solving. A signed-permutation T and matching matrix entries provide a cheap sufficient construction: multiplication by 0/±1 and permutation add no coefficient-rounding mismatch. Test source matrices, not coordinates. Different lengths, sections, loads, IDs, positions, DOF orderings and signed axis orientations remain eligible when their actual free graph and source closure pass. This is a structural/source-family boundary, not an N05 exemption.

The generic functional algebra can evaluate arbitrary represented T operands by retaining products rather than rounding a precomputed K_L*T coefficient. That alone does not prove its recovery agrees with separately rounded K_global. Arbitrary rotations need exact local/global closure or a separately reviewed source-formation discrepancy bound meeting the required quantity criterion; the minimum tranche supplies neither a new rotated-source assembler nor that bound. They remain unsupported when this warrant is absent, even if only two DOFs happen to remain free.

Arbitrary rotation commonly makes a free block larger than two. Reject it as unsupported, even if a local-coordinate picture looks decoupled. Never discard a tiny coupling, split a connected block, select only a loaded torsional pair, or infer exact zeros from a rounded aggregate. Permuting DOFs does not change block order. A future coordinate-reduced method must independently prove the exact invertible transformation, transformed constraints/loads, and reconstruction; it is not part of this tranche. A support layout can make genuinely uncoupled small blocks without axis alignment; the algebraic API supports those represented systems, but product-family admission still needs source closure.

## 3. Exact solve and affine functional derivation

Write the complete source equations as K u = f + r, with u_c prescribed. On free rows,

    K_ff u_f = h = f_f - K_fc u_c.

All terms in h are exact sums/products of the retained declared operands. They are not formed from a rounded reduced RHS. For a block B=[[a,b],[b,c]], Δ=ac-b²>0,

    n1 = c*h1 - b*h2, n2 = a*h2 - b*h1,
    u1 = n1/Δ, u2 = n2/Δ.

For a singleton, u=h/a. Existing Context/Response already implements these ratios, prescribed values and full reactions. Its exact original-free-equation check must remain non-vacuous.

Every targeted scalar recovery has the affine form

    q = β + Σ_j ℓ_j u_j.

Evaluate the prescribed part β_c=β+Σ_c ℓ_c u_c exactly. For one 2x2 free block, form

    q_B = (ℓ1*n1 + ℓ2*n2)/Δ.

For a singleton q_B=ℓ*h/a. Sum block ratios and β_c exactly, then project q once. A functional may span several independent blocks; all contributing blocks must be included. Prefer one shared denominator per block rather than multiplying identical denominators for each DOF. Across blocks, bounded cross-products are valid; if their range or budget cannot be supported, reject explicitly. Do not install arbitrary-precision storage or unbounded rational normalization in this tranche.

The coefficient ℓ may itself be an exact sum of products of retained binary64 operands (for a local member row, K_L[r,p]*T[p,j]). Retain these atoms and form them with the checked expansion product, or derive them through a private source constructor. An already rounded aggregate coefficient is a weaker declared source; it cannot be relabelled as the exact product recipe. All exactness depends on the helper's established finite nearest-rounding/FMA/gradual-underflow assumptions and checked range; unsupported arithmetic remains an error.

### Member end forces and local deformation

For an ordinary straight elastic member,

    d_L = T E u,
    p_L = K_L d_L - f_equiv,L,
    p_L,r = Σ_p,j K_L[r,p] T[p,j] u_map(j) - f_equiv,L,r.

Initial strain/free expansion is incorporated once through its signed equivalent load or the established equivalent affine correction, not subtracted twice. Point nodal loads are in global f; they are not automatically fixed-end member loads. Distributed, thermal and pressure effects must preserve the existing documented signs and ownership. The product's current straight path subtracts `equivalent_nodal_loads_with_spans`, then calls `corrected_local_forces_for_axial_effects`; translate that full signed expression, never just K_L*d. Unsupported curved macro-elements, releases or load-recovery families keep their explicit unqualified status.

Retain all 12 local node-on-element end components when claiming complete member recovery. Interior section-cut quantities are different affine functionals, using the source member end ratio plus actual span/load moments. The product's current j-side station convention negates the i-side action consistently. Evaluate any cancellation-prone station/load combination before projection as well. Merely correcting end rows and then subtracting nearly equal projected end/load terms can reproduce this defect downstream. Exact local deformations can use the same functional engine if needed; they are not mandatory new public rows.

### Spring device action versus equilibrium reaction

For a ground spring with extension x=sᵀu-g, k>0 and same-state ground/reference movement g, the spring-on-pipe generalized action is -s*k*(sᵀu-g). Each component is affine. For existing scalar DOF springs s is the signed axis selector and g=0; use their actual source k. Recover each spring separately. Multiple springs at the same DOF have different IDs and independent actions; any aggregate is an explicit sum, not an overwritten map slot. A prescribed DOF can also have a spring; its spring action and its ideal-constraint reaction remain separate quantities.

The equilibrium reaction is r_i=Σ_j K_ij*u_j-f_i, using every original source contribution and applied-load term. It is exactly zero on free equilibrium rows and is the ideal constraint's action at prescribed rows. Since spring stiffness is included in K, this residual does not report the free spring action. At constrained rows with springs, report r and the device action separately; if a support total is needed, define which constraints/devices it contains before summing. Preserve rotational actions in N*m as well as translational actions in N. The existing product support resultant path only emits translational vectors and is insufficient by itself to observe N05's signed root RX spring torque.

### Why N05/N06 require this seam

For [[a+k,-a],[-a,a]] and f=[0,T], exact source equations give u_root=T/k, u_tip=T/k+T/a, member end-j torsion T, end-i torsion -T and spring-on-pipe action -T. Free root equilibrium reaction is zero. The physical-source reference uses a=687800*pi; the observed N05 product coefficient inferred from retained source expansion is `0x1.07c49b6ac7e26p+21`, while the independent NP-A primitive freezes `...e22`. Keep both identities. The N05 diagnosis measures their approximately 7.93e-16 physical coefficient difference separately from the much larger lost-spring amplification.

The included [Fraction probe](_run_records/reference_probe.py) and [raw results](_run_records/REFERENCE_PROBE.json) check the formulas against independently coded rational elimination. With the diagnosed N05 coefficient and exact decoded binary64 k/T, projecting u first then forming a*(u_tip-u_root) has relative error about +3.377912085e-7. Reusing that coefficient illustratively with N06's k=1e-12, T=1e-16 makes both projected rotations equal, so reconstructed torque is zero. Direct exact functional evaluation gives the declared ±T in both examples. These are source-arithmetic design checks, not a new full N06 coefficient capture, production run, or interval-certificate execution.

## 4. API, ownership and replay

The implementer may choose names; the following responsibilities are mandatory.

1. **Private source plan.** A source-owning product/assembly adapter constructs `RecoverySources` with ordered member/support/load descriptors and all requested quantity keys. It checks exact assembly/recovery closure and every relevant term's ownership. A model hash alone is not enough. Generic low-level affine constructors may prove arithmetic for explicitly declared operands, but cannot grant product mechanical provenance to arbitrary caller-supplied rows.
2. **Private evaluated functionals.** Add a bounded `Response::evaluate_functionals(...)` returning an `Attempt<FunctionalSet>` that borrows the exact same Response and validated plan. Each result owns a private Ratio and typed quantity identity: case, element/support, row/axis, end or station, unit and sign convention. Use separate typed handles rather than overloading existing `Quantity::{Displacement,Reaction}` plus DOF; existing projection retention requires exactly 2*n unique DOF leaves.
3. **Qualified final projection.** Reuse the reviewed `project` algorithm for each functional ratio with the unchanged relative 1e-9 criterion. A `QualifiedFunctionalProjection` binds live response, plan and functional identity, with value, exact sign, interval, absolute/relative error bounds, criterion and basis. The exact-zero shortcut applies only to exact ratio zero; a tiny nonzero interval crossing zero is unresolved, never snapped. Correct-rounding is not claimed by an error enclosure.
4. **Owned retention.** Extend owned evidence with a `RetainedFunctionalSet` companion bound to the existing private `RetainedResponse`. It retains the actual ordered descriptor operands, functional ratios and projections and exact coverage. Existing `RetainedResponse` displacement/reaction/contact proof stays intact; a companion avoids breaking DOF coverage semantics. No public/import constructor can fabricate success.
5. **Independent expected-source replay.** Replay validates expected current source/plan/criterion/limits, rebuilds the source Context and its minors/ratios, regenerates all functionals and projections, and compares their exact recorded bytes/metadata. Self-replay is consistency, not correspondence with a current invocation. Changed loads, k, local coefficients, transform, prescribed value, order, member ID/map, end sign, offset, station or policy invalidates reuse. Do not trust the sign of an unvalidated imported expansion.
6. **Whole-attempt accounting.** Bound and precharge O(n) traversals, term products, metadata sizing/comparison, copies and replay. Preserve accepted charges and denied reservations on failures. Apply one parent cap with decreasing remainder across Context preparation/solve, functional evaluation, all projections and retention/replay; current per-call caps alone are not a total-run bound. Reserve a truthful maximum only where the legacy constructor cannot return failure work; prefer a metered wrapper exposing actual stage/charge. No retry resets the budget. Include long identifiers and overflow controls from RET-01.

Suggested error categories reuse existing exact errors where possible: invalid source/coverage/partition, unsupported family/block/functional, nonpositive source minor, exact range/arithmetic failure, budget, projection unresolved, or stale/mismatched source. Preserve the actual cause and reached stage. None manufactures zero, physical mechanism, or a successful ordinary report. A source failure must not be rescued with the same rounded LU result.

No external schema field is allocated here. A minimal internal receipt needs source level and source binding, selected method, requested mode and ordinary attempt outcome, block/projection/recovery coverage, actual work and failure stage. ROOT decides how those facts fit the combined carrier. Only add durable fields if current carriers cannot distinguish those facts; do not create a general precision2 store or reopen unrelated historical import behavior.

## 5. Product route and selected-mode truthfulness

The route owner should integrate in these bounded seams (repository-relative under `projects/chirality-piping`):

| Seam | Required behavior |
|---|---|
| `core/solver/nonlinear_integration/src/structural_adapter.rs::AssemblyEvidence` | Preserve source inventory and expose a shared exact source/functional adapter. Reuse relevant family/geometry checks without treating a geometry count as the exact solve proof. This existing location need not imply that nonlinear integration is enabled in the first tranche. |
| `core/product_physics/src/lib.rs::solve_load_case` force assembly | Capture complete supported source load contributions as they are added. Keep modulus/case ownership. Mark unsupported producers before selecting recovery. |
| `solve_preview_reduced_system` / `PreviewLinearSolve` | Carry an owned selected solution basis and optional private retained recovery, not just projected free `Vec<f64>` and the ordinary report. Attempt ordinary dense/sparse on its selected path if policy requires/permits it; retain rejection/sensitivity truthfully. Exact recovery may resolve retained-source assembly loss without demanding a successful rounded-system solve, otherwise N06 is unreachable. |
| Final selection in `solve_load_case` | Select one source response atomically for all displacement, reaction, member and spring quantities. Do not select ordinary displacements with exact forces from a different case/state, or exact displacement with ordinary force recovery. If an actual final nonlinear state exists, its retained source must be used; the minimum no-contact tranche declines nonlinear support cases. |
| `recover_local_forces_from_global_model` caller and `corrected_local_forces` | On the selected exact route use retained functional projections, including fixed-end corrections; do not call the projected-u recovery path. Leave ordinary route behavior intact. |
| Reaction/support and station publication | Use exact constrained reactions and separately recovered signed per-device actions. Emit an observable signed rotational spring action using a ROOT-owned existing/new row contract, not a zero free-equilibrium row or invented translational resultant. Keep complete 12 end and applicable station mappings. |
| `append_linear_solver_mode_evidence` and integrity admission | Requested mode and actual selected method are distinct. Record ordinary dense/sparse attempts and any rejected report as such; selected exact response is the same method available from both modes. Never label it dense factor success, sparse LDL success, dense fallback, or sparse parity merely because that mode was requested. |

The current ordinary rounded aggregate can remain available for diagnostics, but its assembly-loss/residual/condition evidence is not silently reinterpreted as evidence of the exact source method. For exact source selection, positive source minors and exact free equilibrium are the structural/solve warrant; per-quantity projection is a separate accuracy warrant. Published-u residual observations may differ because projection destroys tiny deformation information. Preserve that distinction rather than requiring contradictory identities of projected quantities. A known discrepancy must be attributed and bounded at the quantity/source level.

A successful private method cannot bypass the current shared Rust/Python/TS Sensitive gate by flipping `accuracy_evidence` to `reference_verified` or relabelling the ordinary report `checked`. ROOT must allocate genuine selected-method admission backed by a source-owned receipt. Until all consumers understand it and actual case coverage is complete, results can remain inspectable and numerically recovered but unavailable for qualified Current/rule/export. Existing historical Sensitive rows stay unqualified.

Derived stress, displacement magnitudes, maxima, combinations and display unit conversion have their own operations. Feed them the selected correctly recovered source quantities, preserve finite/range checks and test their actual critical output accuracy. Do not claim the affine certificate also certifies a square root, maximum selection, nonlinear stress expression or a later cancellation. Where a derived signed linear combination can cancel, compose it from retained functionals before projection. A first tranche may withhold unsupported derived use explicitly; it may not declare the whole envelope recovered while required consumer quantities still use an uncertified mixed basis. ROOT owns the smallest coherent carrier/admission allocation.

## 6. Controls and pass/fail criteria

These are implementation obligations, not executed results in this design.

| Control | Required evidence/outcome |
|---|---|
| Unchanged actual N05 and N06 authored product observers, both `dense_scrutiny` and `sparse_interactive` | Retain exact candidate/input/coefficient/load source and actual routes. Compare signed root/tip rotations, both signed member torsions, interior torsion and actual signed spring action against frozen physical references at unchanged relative 1e-9. Zero components use their actual protected predicate. N06 must actually select the stronger method despite lost rounded spring. Observer exit 0 alone is not a pass. |
| NP-A frozen coefficient and ULP sweep separately | Preserve `...e22` matrix oracle, both parity anchors for ties if expanding coverage, intended-versus-stored results and exact source spring. Do not substitute N05's `...e26`. Include positive/negative and zero loads and spring scales across stored-loss onset. |
| General layout/identity coverage | Rename all IDs, change lengths/materials/load scales/origins, permute global DOFs and signed axes, multiple independent supported blocks, and different grounded DOF placements. Admission and transformed results follow source structure, not fixture recognition. |
| Rotated/coupled and size controls | A small represented 2x2 coupled block succeeds algebraically. A rotated physical layout with >2 free connected DOFs fails with exact block order. A tiny nonzero connecting term fails just like a large one. A <=2 rotated layout with unproved local/global source closure remains unsupported. Signed-permutation variants with source closure qualify. |
| Prescribed and load controls | Nonzero imposed u_c; all-fixed system; applied load on constrained row; positive/negative fixed-end load; direct nodal load distinguished from member equivalent load; absorbed load tail; multiple springs at one DOF; spring on a prescribed DOF. Verify ideal reaction, each device action and member-end signs independently. Product prescribed-displacement support is not invented if still gated elsewhere; kernel witness does not claim that UI route. |
| Projection-only negative | Install projected source u into the old member recovery: N05 must expose its failed torque criterion and N06 its erased torque. The new final functional projection must pass. This establishes that the correction reaches forces rather than only rotations. |
| Source/method mutation | Alter one stiffness/load tail, k, prescribed value, transform, local row sign, fixed-end offset, case, source identity/order, member/support map or functional coverage. Regeneration or admission rejects the mismatch; a forged accuracy label or copied receipt cannot qualify it. Include a different internally consistent source checked against the original expected invocation. |
| Arithmetic/work rejection | Nonfinite, underflow/overflow products, unsupported block, nonpositive minor, empty/incomplete source, duplicate maps/keys, missing/extra projection slots, zero/one-below budget, long IDs, dynamic-size overflow, source-changing retry, and sign/zero-crossing intervals. No fake zero or stale success; attempts and failures retain charges/stage. |
| General existing numerical checks | Preserve N01–N09/R01–R07, exact-boundary/gap/retention controls, ordinary unscaled DEC-050/053 observations, contact affine 1e-12/count/cap rules, broader unaffected standard suite and registered DEC-025 candidate sweep. Reassess affected checks on final source rather than reusing an invalidated pass. |
| Actual consumer paths | Both-mode real headless solve plus canonical-export gate, Rust/Python/TS shared standing, product/currentness binding and required native save/reopen/result/export/rule paths under the owning lane. Read-only replay or reconstructed function calls do not stand in for these routes. Unqualified unsupported cases remain blocked consistently. |

Independent review must cover the new complete frozen helper/adapter/product diff, mathematical source-to-functional mapping, actual both-mode output and mutation failures. The existing exact-boundary reviews qualify reuse of their specific arithmetic/projection/retention seams; they do not qualify this new method, descriptor ownership, force recovery or product admission. A future evaluator should derive expected mechanics independently of the implementation and keep full source hashes and raw outputs.

## 7. Minimum implementable tranche and handoff

1. Add the private exact affine-functional engine and retained companion with independent algebra/source/range/accounting review. Use generic matrices/partitions, not product fixtures, for its initial controls.
2. Add a no-contact straight-frame/positive-ground-spring adapter with complete nodal-load contributions, exact local/global source closure and free blocks <=2. Include all supported zero/prescribed kernel behavior. Initially decline bend/user-matrix/release/contact and non-nodal product load families unless their recovery descriptors and source closure are implemented and reviewed in the same tranche. An unsupported family remains an open recovery requirement, not an inferred zero load.
3. Integrate actual primary member/spring/reaction recovery, all consumed same-source station rows, requested-mode/selected-method truthfulness, and unchanged N05/N06 product comparisons in both modes. Add an actual signed rotational spring result to the ROOT-owned output contract if none exists.
4. ROOT selects and integrates minimal method/carrier admission with complete consumer coverage. Keep ordinary Sensitive containment until that concrete evidence-backed path can be admitted. Obtain fresh review, required checks and lane-owned native evidence on the actual candidate.

This is the smallest coherent source-recovery tranche, not completion of general coupled models, arbitrary rotations, all nonlinear/load families, precision2 persistence, or all numerical programme obligations. No new user decision is needed merely to write this proposal; ROOT retains the carrier/semantic allocation and any prospective method selection. WORKING_ITEMS receives implementable seams, safeguards, rejection cases and validation requirements without authority to relax a protected test.

## 8. Evidence basis and claims

[`_run_records/INPUT_MANIFEST.json`](_run_records/INPUT_MANIFEST.json) records actual instruction/source/evidence origins and hashes. Root/Piping/LOOP_INIT and full HELPS_HUMANS bodies were read; no other full role body, skill body or workflow was selected. The task authors a bounded design, not a reusable workflow. The brief's no-Git limit superseded routine root-discovery Git commands; checkout/base identity is explicitly parent-supplied.

Reuse basis: `CORRECTNESS_DESIGN/NUMERICAL_REFERENCE.md` as qualified by `NUMERICAL_POLICY_REVIEW/RETURN.md`; `NUMERICAL_INTEGRITY/REFERENCE_REVIEW/{RETURN.md,_run_records/DERIVATIONS.md}`; exact-boundary KERNEL/PROJECTION/RETENTION independent reviews and RET-01 repair/runtime backchecks. Their applicability is retained: componentwise backward error is not forward accuracy; exact source contributions do not recreate discarded primitive coefficients; member end-force signs follow the existing straight-frame theory; source predicates, outward projection and private retention have bounded hypotheses.

Those records already qualify primary LAPACK DPOSVX/DPORFS/DPOCON/DPOEQUB, the TU Delft Euler–Bernoulli source and the cited Higham–Mary/Rump–Jeannerod analyses. No new literature-dependent theorem or current version claim is introduced here, so no fresh web retrieval is claimed. The new affine-functional formula follows direct substitution and distributivity, and the included independent Fraction/Gauss design checks demonstrate those identities in bounded cases. Those checks are neither Rust execution nor independent review of this author's proposal.
