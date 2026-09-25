# Independent pressure assembly oracle — final TASK return

Date: 2026-09-24. Executor /root/numerical_policy_review, TASK Type 2. Actual harness parent /root; issuer/integrator /root/physics_manager. No descendants. Base f702b439536c6e76af8e1c81ee536d5685e87907; actual tested source is bound by the per-run SHA-256 manifests.

**Completed: independent reference freeze and real public-entrypoint integration tests. Corrected frozen suite: 14 passed, 0 failed.** Source test is core/product_physics/tests/pressure_runtime.rs, SHA-256 9493488af21d2459d47cb2f18f3b5e2f4c5da43351bf9a210387067e7839e272. The runtime values come from run_linear_static_preview_with_mode after JSON DTO deserialization, never fabricated result rows or production arithmetic used as expected values.

## Delivered and checked

- REFERENCE_RETURN.md and FROZEN_RUNTIME_EXPECTATIONS.json were frozen before reading the new pressure implementation. Their original freeze bytes remain unchanged; FREEZE_MANIFEST.json binds instruction/design/oracle origins. Exact Fraction/Machin calculations independently confirm the six SI states and additional assembly expectations.
- ADDITIONAL_REFERENCE_CONTROLS.md records the subsequently requested material/case formulas before their first observation, and ROOT's case-scoped region identity/max-displacement allocation. It does not rewrite the older reference or original contract history.
- The public suite exercises both solver modes: six pressure/closure/thermal states; spatial rotation and mm/MPa normalization; equal-bore unequal-wall/E/nu two-span compatibility with either member and terminal-order reversal; mixed transferring/separate closures and signed support reaction vectors; independent distributed axial station recovery; zero/signed pressure, zero nu and thermal reversal.
- Interface checks cover exact kind/component/location/unit semantics, competing legacy axial/pressure row suppression, actual region/case/result-ID binding, repeated region IDs in different cases, duplicate ID rejection within one case, case-order-independent displacement maxima and deterministic case-ID ties with real source references.
- Material checks use an actual tip torque to observe G: missing exact G is accepted with E/nu, conflicting retained G is nonauthoritative, the common selected/interpolated E/nu pair supplies G, strict-interior temperature selection rejects endpoints/extrapolation, selected thermal alpha is used without requiring unused base alpha, missing selected alpha blocks, and nonempty partial overrides cannot merge missing material/nu from the base list. Legacy missing G remains a targeted input error.
- Negative input controls check missing material/region/closure data, unknown closure and pressure basis, member duplication/unknown member/overlap, bore mismatch, noncollinearity, an outside branch at an internal region node, exact pressure primitives, nonzero legacy pressure and namespace/version mismatch.

Nonzero expected values retain relative 1e-9. Expected-zero comparisons use the independently frozen same-dimension fixture scales. No protected existing tolerance, historical numerical oracle, source expectation or legacy fixture was weakened.

The fixtures discriminate omitted/flipped/doubled pressure Poisson terms, cap subtraction/double counting, interior-cap duplication, orientation errors, wall/effective-force conflation and omitted mechanical fixed-end subtraction. No source-injection mutation campaign was executed or claimed.

## Actual runs, including the retained failure

| Run | Result | Evidence and qualification |
|---|---|---|
| First exploratory suite | 10/10 passed | _run_records/pressure_runtime_first.log and RUN1_INPUTS.json. A small input-validator change overlapped the manager's initial source-hold delivery, so this is exploratory, not the final source seal. |
| Expanded frozen suite | 12/14 passed, 2 failed | _run_records/pressure_runtime_final.log and RUN2_INPUTS.json. Both failures were LOAD_INPUT_INVALID before solving because the new torque fixture used translational direction global_x with moment dimension. No numerical expected value was reached or contradicted. |
| Corrected frozen suite | 14/14 passed, Cargo exit 0 | _run_records/pressure_runtime_corrected.log, RUN3_INPUTS.json and RUN3_RESULT.json. All 47 participating source hashes were unchanged after the run. |

The exact fixture correction was global_x to rotation_x in the one torque-load helper. The public wire contract identifies rotation_x as RX. The manager authorized that one-token repair after the failures were reported, retaining the original source/hash/log for ROOT's review delta. All expected values and tolerances were unchanged. The preimage, exact patch and before/after hashes are in _run_records/pressure_runtime_before_wire_fix.rs, WIRE_FIX.patch and WIRE_FIX.json. Before test hash: 5dab6016eee1e2fb14f78891b9b282584cfeee07a969fd4e19c27a73871f20fc.

Executed command, from the pressure worktree:

    CARGO_BUILD_JOBS=2 CARGO_TARGET_DIR=<PHYSICS_MANAGER/PRESSURE_REGIONS/target> cargo test --offline --locked -j2 --manifest-path projects/chirality-piping/core/product_physics/Cargo.toml --test pressure_runtime -- --test-threads=2

Cargo ownership was explicitly acquired/released through physics_manager. No other Cargo process was launched by this TASK. The final source capture traverses local dependency manifests and records source/manifest/lock hashes. A first attempt at that manifest used unavailable Python tomllib; the capture helper was corrected to read the simple dependency path declarations with the standard library. RUN2 truthfully records its post-run acquisition under the manager's source hold; RUN3 verifies the recovered full source set before and after the corrected run. This tooling issue did not change solver/test inputs or erase a failed run.

Only the new integration test and this assigned evidence directory were written. Read-only Git resolved the worktree and inspected the named baseline public DTO/thermal wire contract; no Git mutation occurred. No native/browser operation, configuration edit, release or external-solver result was performed.

## Interpretation and remaining integration

The results support the bounded live straight-annulus assembly/reference and interface claims for these fixtures. They do not establish real-pipe shear/end/weld/interface behavior, arbitrary exterior pressure, curved/Bourdon/pressure-stiffness stability, nonlinear contact, professional acceptance or release fitness. Newer relevant theory and primary-reference applicability were recorded in REFERENCE_RETURN and the upstream pressure qualification.

This TASK independently checked the manager's X1 statics in chat and recorded the derivation in ADDITIONAL_REFERENCE_CONTROLS; the manager owns its separate elastic_extrema_runtime test. It is not part of this 14-test result.

The manager's full-library run and its retained legacy-pressure fixture failures remain separate evidence. This return does not dispose those failures or authorize rewriting their history. ROOT's fresh complete-candidate review, source/schema/consumer integration, protected sweep and actual native/headless/persistence/export witnesses remain required. Later source changes require affected reruns and review coverage. The reported test-only wire delta must be included in the current reviewer basis.

ROOT and physics_manager received the final count, source/test hashes, raw log paths, wire correction and scope limits. Test source is returned frozen; Cargo ownership is released.
