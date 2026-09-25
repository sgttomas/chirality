# Individual regression-test purpose dispositions

Completed the 38 assigned nonpressure-classified tests individually in `DISPOSITIONS.json`. Each record names its exact test/source line, pressure dependency, proposed current-public input delta, assertions to retain, expectations requiring independent treatment, verification and unresolved concern. All 38 inspected test bodies match FREEZE_01. Full request/fixture and relevant builders/direct-oracle helpers were read; no source, tests or pressure-module bytes were edited, and no builds/tests/delegation occurred.

The manager's separate observational scratch run reports `PRESSURE_MODEL_REAUTHOR_REQUIRED` before failure in all 50 cases. Its `REGRESSION_DIAGNOSIS/OBSERVED_CAUSES.json` supports the preceding gate diagnosis; it does not show that any proposed zero-pressure input passes or preserves numerical responses. The initial empty diagnostic fields in the classification file were missing capture, not evidence that pressure was absent.

For ordinary feature/diagnostic coverage, the proposed operation is a purpose-specific local copy that zeros only the four named inherited pressure primitives (two at1.2MPa in L-100, two at0.6MPa in L-200), while preserving all other values and retaining a source comment. It does not change `request()` or the bundled example globally. The exact operation is expanded in the JSON. Recomputed numeric values, contact states, rounding and row presence cannot be assumed unchanged.

Four initial classifications need a substantive split:

- `endpoint_section_cut_curved_endpoints_use_all_six_arc_resultants` deliberately applies2MPa and builds its cap/radial pressure oracle. Retain that historical case; prepare a separately verified pressure-free mechanical endpoint-cut counterpart. Exact curved pressure is still unsupported.
- `mixed_units_are_normalized_at_preview_mechanics_boundary` converts nonzero pressure to kPa and compares hoop stress. A0Pa/0kPa check would be vacuous. Split nonpressure unit parity from an independently checked nonzero exact-region pressure-unit counterpart.
- `valid_invented_model_exposes_endpoint_stress_components` asserts that longitudinal-pressure rows are absent under nonzero thrust. Keeping zero-valued pressure primitives changes that condition: `pressure_for_pipe` returns `Some(0)` and zero longitudinal rows can appear. Split mechanical row coverage from historical pressure publication and new exact surface/wall stress coverage.
- `valid_invented_model_exposes_nonlinear_support_loop_evidence` explicitly preserves historical no-spring/qL/2 loading and fixes friction0.489527 and normal48.952719. Those values must not be replaced by newly observed zero-pressure output. A current counterpart needs independently derived active-set and reaction expectations.

One test needs an especially small correction: `curved_bend_macro_element_emits_arc_interior_station_results` is already pressure-free in its curved branch and passed those assertions in the preserved run. Only its late straight `request()` metadata comparator inherits pressure. Leave the curved input and all its numerical expectations unchanged; isolate only the straight comparator.

The remaining proposals preserve authored input echoes, diagnostic targets, metadata, invariants and existing tolerances. Numeric relations that depend on distinct nonzero operands or rounding still require demonstrated coverage. Legacy SIF review-row/combination transport tests are not physical qualification of the known SIF or nonlinear-superposition limitations.

These are reviewable proposals, not passes, accepted new oracles or permission to bypass the public pressure refusal. The manager owns the remaining12 classifications, any historical replay disposition, implementation and reruns. Actual harness parent is `/root`; assignment issuer/integrator is `/root/physics_manager`; role is retained TASK Type2. Earlier assignments remain historical.
