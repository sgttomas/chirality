# Affine core implementation return

Implemented and returned to WORKING_ITEMS `/root/numerical_resume`; source ownership is released to the parent. The eight focused tests passed in the parent-run lane. This is bounded declared-source arithmetic evidence, not product/source-family qualification, independent review clearance, engineering acceptance or release.

## Result and API

`exact_boundary::functionals` evaluates `offset + Σ coefficient*u` over the exact Response before displacement projection. Offset/coefficient recipes are ordered sums of ordered products of finite binary64 atoms. The helper retains their actual atom bits and order; it does not replace a recipe with a rounded coefficient. Prescribed values contribute to the exact offset. Both coordinates in each free block share their denominator; different blocks use bounded exact rational sums. Range and budget failures remain explicit. The existing outward projection helper supplies the final value, exact sign, enclosure, error bounds, basis and caller's explicit criterion, including exact-zero handling.

Typed identities cover member ends, sections, distinct ground springs, source reactions, node displacement components and explicitly declared affine quantities. Units include N, N*m, m, mm and radians. SourceReaction is separate from the existing mandatory Displacement/Reaction leaf types. The source-owning product adapter still owns mechanical completeness, producer ownership, all requested row coverage, local/global source closure and sign/unit meaning.

The concrete call sequence is:

1. `AttemptBudget::new(limits)`; reserve adapter work with `charge(AttemptStage::SourceClosure, count)` before doing that work.
2. `Context::prepare_with_budget(system, identity, force_basis, &mut budget)` and `context.solve_with_budget(&mut budget)`.
3. `FunctionalPlan::new(&context, descriptors, &mut budget)`; `response.evaluate_functionals(&plan, &mut budget)`.
4. `response.project_with_budget(Quantity, dof, relative_limit, &mut budget)` for all legacy 2*n leaves; `set.project(index, relative_limit, &mut budget)` for all plan rows. Metered contact proofs are available through `gap_proof_with_budget`.
5. `set.retain(contacts, dof_projections, functional_projections, &mut budget)`. The companion constructs and owns the RetainedResponse from the same live Response, then retains every ordered descriptor, private ratio and projection.
6. `retained.replay_against(expected_system, identity, force_basis, independently_rebuilt_descriptors, expected_contacts, relative_limit, &mut budget)`. Replay rebuilds once, checks source bits/order, minors, ratios, contacts, mandatory DOF leaves and complete functional coverage against the independently supplied current plan.

Read-only `response()`, `descriptors()`, `ratios()` and `projections()` expose retained evidence. Projection getters expose index, value, interval, absolute/relative bounds, criterion, basis and exact sign. Replay-check getters report coverage. There is no public constructor for an evaluated ratio, qualified projection, retained companion or replay success.

The non-cloneable budget retains accepted charges and denied reservations across failures and retries. `Attempt.work` and `budget.report()` are cumulative, so successive reports must not be summed. `stage()` gives the reached stage. A private attempt token prevents a new budget from reusing an existing metered Context. Private markers reject legacy unmetered solves and per-call DOF/contact proofs from the new retention path. Legacy arithmetic, predicates, projection and retention algorithms remain unchanged. Their old accessors are not whole-attempt totals; for the new path the prefix through solve may include earlier source-closure work. Use the budget report for the full run.

## Observed checks and limits

Parent executed the focused command recorded in [`core_functionals_02.json`](../_run_records/core_functionals_02.json), using the dedicated `/private/tmp/piping-source-recovery-frame-target`, offline/locked/jobs2. [Raw output](../_run_records/core_functionals_02.log): **8 passed, 0 failed, 77 filtered out**. No child source edit occurred after the formatted static-ready message or during that rerun.

The groups cover positive/negative torque with a tiny relative twist lost by projecting rotations first; exact product-recipe cancellation; all-fixed and mixed prescribed partitions; a generic 2x2 rational oracle and two/three independent blocks; exact zero versus nonzero unprojectable response; retained/current plan order, atom, offset, identity, policy, source and corrupted-ratio/projection rejection; foreign-plan and fresh-ledger rejection; unmetered-call bypass rejection; long-ID/operation-budget refusals, range failure and cumulative retry accounting. Expected rational outcomes were independently checked with Python Fraction elimination and recorded in [provenance](PROVENANCE.json).

[The first compile log](../_run_records/core_functionals_01.log) remains preserved: duplicate `Debug` derive on ProjectionData caused E0119 before tests. The derive was corrected; the successful rerun covers the repaired candidate. Rustfmt completed on exactly the three owned Rust files. No child Cargo, Git, npm, native/browser or full-suite operation occurred.

The 77 filtered tests are not claimed passed. Fresh independent review of the coherent helper/adapter/facade diff, remaining appropriate checks and the actual product N05/N06 both-mode witnesses remain with the manager. No product qualification, rotated-source closure, unsupported producer coverage or nonlinear derived-result claim follows from these core tests. Hard limits were not raised.

## Source and execution provenance

[PROVENANCE.json](PROVENANCE.json) records actual harness-native parentage, role/instruction origins and SHA-256 hashes, selected design/review hashes, supplied checkout/base, scope, final source hashes and actual verification references. No additional skill, workflow or full role was selected; no descendants were created.

| Repository-relative file | SHA-256 |
|---|---|
| `projects/chirality-piping/core/solver/frame_kernel/src/structural/exact_boundary.rs` | `28cf0b7839f1b81e61377e7fabdb42f5f96956b69849701de62097a52da39e80` |
| `projects/chirality-piping/core/solver/frame_kernel/src/structural/exact_boundary/functionals.rs` | `511bfb50673ea252eaf0007bed5f4ae2ecf561fd93d2c6772b793c627a8faead` |
| `projects/chirality-piping/core/solver/frame_kernel/src/structural/exact_boundary/functionals/tests.rs` | `98547916b3a9f9587d79baa5a476902a5603792332fcdf257ace54ffff035493` |
