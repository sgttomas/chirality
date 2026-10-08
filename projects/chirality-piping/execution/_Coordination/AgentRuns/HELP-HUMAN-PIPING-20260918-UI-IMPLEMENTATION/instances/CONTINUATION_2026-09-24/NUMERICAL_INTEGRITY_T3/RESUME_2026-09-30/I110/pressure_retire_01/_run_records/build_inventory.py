"""I110: build inventory.json from the probe tree at NUM HEAD (and b2 refs for B3a). Paths use placeholders."""
import json, re, subprocess, sys, collections
TREE = sys.argv[1]            # WT/t3-pret
OUT = sys.argv[2]
P = TREE + '/projects/chirality-piping/'
MECH = [l.strip() for l in open(sys.argv[3]) if l.strip()]

def line_of(path, needle, nth=1, regex=False):
    n = 0
    for i, l in enumerate(open(P + path, encoding='utf-8'), 1):
        if (re.search(needle, l) if regex else needle in l):
            n += 1
            if n == nth: return i
    raise SystemExit(f'not found: {path}: {needle}')

def ph(path):
    if path.startswith('core/product_physics/'): return 'PP/' + path[len('core/product_physics/'):]
    if path.startswith('core/reporting/result_export/'): return 'RE/' + path[len('core/reporting/result_export/'):]
    return 'P/' + path

E = []
def add(area, path, needle, kind, premise, disposition, note, nth=1, regex=False, label=None):
    E.append(dict(area=area, site=f'{ph(path)}:{line_of(path, needle, nth, regex)}', symbol=label or needle.strip()[:90],
                  kind=kind, premise=premise, disposition=disposition, note=note, branch='NUM 9cd61ba201'))

PR = 'core/product_physics/src/pressure_runtime.rs'
add('PP', PR, '(Some("1.0.0"), Some("legacy_pressure_v1"))', 'acceptance', 'label', 'becomes a refusal',
    '0.3.0 + 1.0.0/legacy_pressure_v1 refused with PRESSURE_MODEL_REAUTHOR_REQUIRED (Q4); the only product acceptance of the label on NUM')
add('PP', PR, 'supported pressure contracts are 1.0.0/legacy_pressure_v1', 'refusal', 'label', 'edit message',
    'PRESSURE_CONTRACT_UNSUPPORTED text names only 2.0.0/exact_straight_pressure_v2')
add('PP', PR, '"0.1.0" | "0.2.0" => {', 'acceptance', 'implicit', 'keep (D-1 option A)',
    'implicit form: no contract; stays the pressure-free namespace (components, nonlinear/constant-effort supports, combinations, equivalent_static, B1 D1.3)')
add('PP', PR, '&& load.magnitude.value != 0.0', 'refusal', 'implicit', 'becomes a refusal (D-2 option A1)',
    'refuse every pressure-category/dimension primitive in a non-exact document, zero included (as the exact profile already does)')
add('PP', PR, 'if crate::historical_pressure_reference::active() {', 'scope', 'pressure', 'remove (stage 2)',
    'test-only suspension of the legacy-pressure refusal; serves O2 and O4 (held) until the M07 ruling')
add('PP', PR, 'a fresh solve cannot publish the legacy nonzero pressure model', 'refusal', 'implicit', 'edit message',
    'PRESSURE_MODEL_REAUTHOR_REQUIRED text: legacy pressure is retired; re-author to 2.0.0/exact_straight_pressure_v2 (pressure_regions incl. [] and E/nu)')
add('PP', PR, 'fn profile_dispatch_requires_explicit_regions_and_refuses_legacy_pressure', 'test', 'implicit', 'edit test',
    'its final case (0.2.0 zero-valued pressure primitive accepted) inverts under A1; add the label refusal')
HP = 'core/product_physics/src/historical_pressure_reference.rs'
add('PP', HP, '//! Private test-only execution of retained historical pressure premises.', 'scope', 'shared', 'held (M07 ruling)',
    'module doc names both premises; held with the scope file')
add('PP', HP, 'pub(super) fn active()', 'scope', 'shared', 'held (M07 ruling)', 'thread-local flag read by both bypasses')
add('PP', HP, 'pub(super) fn with_scope', 'scope', 'shared', 'held (M07 ruling)', 'entered by the pressure oracles and by O1-O4')
add('PP', HP, 'pub(super) fn run(', 'scope', 'pressure', 'held (M07 ruling); then remove (stage 2)', 'asserts 0.1.0/0.2.0 legacy input; used via historical_pressure_preview by O2, O4 and the pressure oracles')
L = 'core/product_physics/src/lib.rs'
add('PP', L, 'mod historical_pressure_reference;', 'scope', 'shared', 'held (M07 ruling)', 'module declaration')
for needle, note in [
    ('struct PressureThrustLoad {', 'legacy thrust record (with PressureThrustSource, ExpansionJointPressureThrustInput)'),
    ('fn build_pressure_thrust_loads(', 'legacy thrust from pressure primitives x internal or joint effective area'),
    ('fn genuine_pressure_element_target(', 'selects pressure primitives for the legacy path'),
    ('fn expansion_joint_pressure_thrust_inputs_by_pipe(', 'joint effective-area thrust inputs'),
    ('fn add_pressure_thrust_loads(', 'assembles legacy thrust into the load vector'),
    ('fn add_curved_bend_pressure_thrust_load(', 'legacy bend radial pressure-thrust loads'),
    ('fn pressure_thrusts_for_pipe(', 'per-pipe thrust for the fixed-end correction'),
    ('struct ExpansionJointPressureThrustAggregate {', 'joint thrust review aggregate'),
    ('fn append_expansion_joint_pressure_thrust_results(', 'expansion_joint_pressure_thrust_load_review rows'),
    ('fn pressure_for_pipe(', 'net legacy pressure per pipe for thin-wall membrane stress'),
    ('let include_pressure_longitudinal = !pressure_thrust_active;', 'legacy longitudinal-pressure inclusion switch'),
    ('let pressure_thrust_loads =', 'case-solve call site of the legacy thrust builder'),
    ('Some("pressure_thrust_load")', 'W2 admission family for legacy thrust (unreachable after A1)'),
]:
    add('PP', L, needle, 'computation', 'pressure', 'remove (stage 2)', note + '; exercised by O2/O4 (held)')
add('PP', L, 'fn recover_section_stress(', 'computation', 'pressure', 'edit (drop pressure parameter)', 'legacy PressureBasis input; None on every exact path')
add('PP', L, '"pipe_section_pressure_hoop_stress",', 'computation', 'pressure', 'remove', 'legacy hoop/longitudinal row emission (endpoint)', nth=1)
add('PP', L, '"pipe_section_pressure_hoop_stress",', 'computation', 'pressure', 'remove', 'legacy hoop/longitudinal row emission (station)', nth=2)
add('PP', L, 'fn open_formula_summary_mpa', 'computation', 'pressure', 'edit (drop include_pressure_longitudinal)', 'legacy summary includes pressure longitudinal')
add('PP', L, 'pub component_pressure_thrust_load_count: usize,', 'type/field', 'pressure', 'keep (always 0)',
    'public MechanicsSummary field; removing it changes every envelope, exact included')
add('PP', L, '| "pipe_section_pressure_hoop_stress"', 'computation', 'pressure', 'keep', 'exact retain-list entry; a no-op for exact, kept for byte identity')
add('PP', L, '"EXPANSION_JOINT_PRESSURE_THRUST_APPLIED",', 'computation', 'pressure', 'remove', 'diagnostic of the legacy joint thrust')
# historical-scope tests
HIST_PRESSURE = ['valid_invented_model_exposes_endpoint_stress_components_historical_pressure_premise',
 'pressure_thrust_applies_axial_fixed_end_correction_without_longitudinal_rows_historical_pressure_premise',
 'pressure_load_direction_does_not_change_thrust_magnitude_or_sign_historical_pressure_premise',
 'generated_result_metadata_and_historical_quantization_match_legacy_fixture_historical_pressure_premise',
 'mixed_units_are_normalized_at_preview_mechanics_boundary_historical_pressure_premise',
 'endpoint_section_cut_fixed_and_free_pressure_thermal_match_uniform_stations_historical_pressure_premise',
 'endpoint_section_cut_genuine_pressure_preserves_existing_result_leaves_historical_pressure_premise',
 'endpoint_section_cut_two_genuine_pressures_sum_once_for_thrust_and_stress_historical_pressure_premise',
 'endpoint_section_cut_curved_endpoints_use_all_six_arc_resultants_historical_pressure_premise',
 'endpoint_section_cut_curved_bend_pressure_shows_membrane_end_and_station_state_historical_pressure_premise',
 'curved_bend_macro_span_pressure_reaches_nonlinear_loop_with_same_vector_historical_pressure_premise']
for t in HIST_PRESSURE:
    add('PP', L, f'fn {t}(', 'test', 'pressure', 'delete the test', 'historical-scope legacy nonzero-pressure oracle (P2: fails once the scope bypass goes)')
for t in ['valid_invented_model_exposes_nonlinear_support_loop_evidence_historical_pressure_premise',
          'expansion_joint_pressure_thrust_uses_user_effective_area_as_load_side_evidence_historical_pressure_premise']:
    add('PP', L, f'fn {t}(', 'test', 'shared', 'held (M07 ruling); pressure premise goes in stage 2', 'O2/O4: legacy nonzero-pressure oracle that also carries joint C-150 (request_with_refused_joint)')
for t, note in [('current_composite_derived_normal_friction_and_reversal', 'enters with_scope for the M07 joint only; its pressures are zeroed by mechanical_fixture_for_test'),
                ('expansion_joint_user_stiffness_emits_macro_element_review_rows', 'enters with_scope for the M07 joint only; zeroed pressures')]:
    add('PP', L, f'fn {t}(', 'test', 'shared', 'held (M07 ruling)', note + '; P3: passes with pressures stripped and no pressure bypass')
add('PP', L, 'fn private_historical_pressure_scope_restores_public_refusal_and_rejects_exact(', 'test', 'pressure', 'edit test (stage 2)',
    'uses run(); keep the ordinary-route refusal of the demo, drop the scope parts when run() goes')
add('PP', L, 'fn private_historical_scope_restores_after_unwind_and_is_thread_local(', 'test', 'shared', 'held (M07 ruling)', 'scope mechanics')
for h, note in [('fn historical_pressure_preview(', 'helper used by O4 (held)'), ('fn historical_pressure_preview_with_mode(', 'helper used by O2 (held)')]:
    add('PP', L, h, 'test', 'pressure', 'delete (stage 2)', note)
for h in ['fn fixed_fixed_pressure_request(', 'fn endpoint_section_cut_pressure_request(']:
    add('PP', L, h, 'test', 'implicit', 'keep', 'also builds the two hydrotest-pressure refusal tests (input_contract_hydrotest_pressure_blocks_instead_of_silently_ignoring, endpoint_section_cut_mixed_hydrotest_pressure_blocks_entire_solve), which pass under P2/P3')
add('PP', L, 'fn curved_bend_pressure_load(', 'test', 'pressure', 'delete', 'nonzero legacy pressure primitive helper; historical users only')
add('PP', L, 'fn mechanical_fixture_for_test(', 'test', 'implicit', 'edit test (strip, not zero; D-2 A1)',
    f'zeroes the demo pressure primitives for {len(MECH)} named tests; P3: stripping instead leaves all 39 non-held users passing, no re-pin; O1 and O3 (held) keep zeroing')
for t in MECH:
    if t in ('current_composite_derived_normal_friction_and_reversal', 'expansion_joint_user_stiffness_emits_macro_element_review_rows'):
        continue  # O1, O3: held, listed above
    add('PP', L, f'fn {t}(', 'test', 'implicit', 'edit via helper (A1)', 'solves the demo with zero-valued legacy pressure primitives; P2 refuses it, P3 (stripped) passes unchanged' if t != 'valid_invented_model_exposes_endpoint_stress_components_without_pressure' else 'already strips the pressures (mechanical_stress_fixture_for_test); unaffected')
add('PP', L, 'fn request_with_refused_joint(', 'fixture', 'shared', 'held (M07 ruling)', 'unchanged demo incl. joint C-150 and nonzero legacy pressure')
S11F = 'core/product_physics/src/s11f_tests.rs'
for t in ['fn f10_pressure_and_joint_thrust_g1e8(', 'fn f10_pressure_and_joint_thrust_g1e80(', 'fn f10_pressure(', 'fn pressure_joint(', 'fn pressure(id']:
    add('PP', S11F, t, 'test', 'pressure', 'delete the test', 'S11-F F10 (E15/E16) legacy pressure and joint-thrust fold, inside with_scope')
S11G = 'core/product_physics/src/s11g_tests.rs'
add('PP', S11G, 'fn t6a_collinear_runs_are_silent_with_the_floor(', 'test', 'pressure', 'edit test (drop the pressure-run row)', 'fifth run uses legacy thrust inside with_scope')
add('PP', S11G, 'fn pressure(id', 'test', 'pressure', 'delete', 'nonzero legacy pressure helper')
PP_ = 'core/product_physics/src/'
add('PP', PP_+'preview_physics.rs', 'if crate::historical_pressure_reference::active() {', 'scope', 'M07', 'held (M07 ruling)', 'joint-refusal bypass; shares the scope flag')
add('PP', PP_+'preview_physics.rs', '"pipe_section_pressure_hoop_stress",', 'schema-enum', 'pressure', 'keep',
    'preview-physics-1 kind lists (published contract); no producer emits them after retirement')
add('PP', PP_+'source_recovery.rs', 'pub pressure_thrust_loads:', 'computation', 'pressure', 'remove', 'always empty after retirement')
add('PP', PP_+'source_recovery.rs', 'legacy source-blocks namespace requires model0.1/0.2', 'acceptance', 'implicit', 'keep (D-1 A)', 'source-block recovery domain is 0.1.0/0.2.0 only')
add('PP', PP_+'retained_product.rs', 'pressure: &[PressureThrustLoad],', 'computation', 'pressure', 'remove parameter', 'B1 plumbing; always empty in D1 (D1.7 nodal primitives only)')
add('PP', PP_+'retained_product.rs', '|| !pressure.is_empty()', 'computation', 'pressure', 'remove', 'B1 plumbing guard')
add('PP', PP_+'retained_memory.rs', 'if !matches!(m.schema_version.as_str(), "0.1.0" | "0.2.0") {', 'acceptance', 'implicit', 'keep (D-1 A; B0 D1.3)', 'retained route domain = implicit form only; label already refused (F::PressureContract)')
add('PP', PP_+'source_receipt.rs', 'pressure_thrust_loads: input.pressure_thrust_loads,', 'computation', 'pressure', 'remove', 'plumbing')
add('PP', PP_+'source_receipt/tests.rs', 'fn legacy_model_three_retains_ordinary_route_without_old_source_namespace', 'test', 'label', 'becomes a refusal test',
    'only NUM test that solves a 0.3.0 legacy-labelled model; becomes the ordinary-route label refusal')
add('PP', PP_+'f1a_tests.rs', 'let thrust = build_pressure_thrust_loads(', 'test', 'pressure', 'edit test', 'guard inputs build legacy thrust')
add('PP', PP_+'f1b_tests.rs', '"pressure_thrust_load"', 'test', 'pressure', 'edit test (drop family)', 'f1b_admission_names_each_family')
add('PP', PP_+'retained_facade_tests.rs', 'if load["category"] == "pressure" || load["dimension"] == "pressure" { load["magnitude"]["value"] = json!(0.0); }', 'test', 'implicit', 'edit test (no-op loop; drop)', 'preview_physics_invented_model has no pressure primitive')
add('PP', PP_+'validation.rs', '.pressure_thrust_reference', 'acceptance', 'pressure', 'keep (route to T4)', 'expansion-joint metadata field required by validation; model data, not computation')
T = 'core/product_physics/tests/'
add('PP', T+'f1b_w2_runtime.rs', 'fn f1b_w2_admission_refuses_a_zero_legacy_pressure_as_pressure_thrust(', 'test', 'implicit', 'delete the test', 'pins legacy thrust family reached by a zero-valued legacy pressure (two SHA-256 pins)')
add('PP', T+'f1b_w2_runtime.rs', '"pressure_thrust_load" => loads.push', 'test', 'implicit', 'delete', 'family builder')
add('PP', T+'pressure_runtime.rs', 'fn namespaces_and_nonzero_legacy_pressure_cannot_silently_fallback(', 'test', 'implicit', 'keep; extend', 'add label and zero-valued cases')
add('PP', T+'preview_physics_runtime.rs', 'invented_preview_model.json', 'test', 'implicit', 'check under A1', 'reads the demo')
add('PP', T+'represented_gap_publication.rs', 'invented_preview_model.json', 'test', 'implicit', 'check under A1', 'reads the demo')
add('PP', 'core/product_physics/examples/preview_result.rs', 'invented_preview_model.json', 'doc', 'implicit', 'keep', 'example prints the refused demo')
# loads and solver crates
SR = 'core/loads/stress_recovery/src/lib.rs'
for needle, note in [('pub struct PressureBasis {', 'thin-wall membrane input'), ('pub struct PressureBasisUnitMetadata {', 'unit metadata'),
                     ('pub pressure_hoop: Option<f64>,', 'StressComponents legacy fields'), ('pub pressure_hoop_range: Option<f64>,', 'range fields'),
                     ('fn pressure_membrane(', 'legacy thin-wall hoop/longitudinal formula'), ('if let Some(pressure) = &input.pressure {', 'recovery call')]:
    add('loads', SR, needle, 'computation', 'pressure', 'remove', note)
CB = 'core/solver/curved_bend/src/lib.rs'
add('solver', CB, 'pub fn consistent_radial_pressure_nodal_loads(', 'computation', 'pressure', 'remove', 'legacy bend pressure thrust')
add('solver', CB, 'pub fn arc_section_resultants_with_radial_pressure(', 'computation', 'pressure', 'remove (callers with zero thrust use the plain form)', 'legacy bend pressure stations')
add('solver', 'core/loads/primitive_loads/src/lib.rs', '"pressure" => Ok(Self::Pressure),', 'acceptance', 'implicit', 'keep', 'category must still parse so it can be refused by name')
add('solver', 'core/solver/frame_kernel/src/lib.rs', 'Self::Pressure => "pressure",', 'type/field', 'exact', 'keep', 'ledger source used by the exact eigenload')
# runner
R = 'core/runner/headless/'
for needle, note in [('fn preview_bridge_executes_product_physics_with_deterministic_refs(', 'zeroes pressure in memory'),]:
    add('runner', R+'src/lib.rs', needle, 'test', 'implicit', 'edit test (strip; A1)', note + '; P3: passes stripped')
add('runner', R+'src/lib.rs', 'if load.category == "pressure" || load.dimension == "pressure" {', 'test', 'implicit', 'edit test (strip; A1)', 'second zeroing helper', nth=2)
add('runner', R+'src/lib.rs', 'if load["category"] == "pressure" || load["dimension"] == "pressure" {', 'test', 'implicit', 'edit test (strip; A1)', 'third zeroing helper')
add('runner', R+'src/result_envelope_binding.rs', 'fn unpressurized_binding_model(', 'test', 'implicit', 'edit test (strip; A1)', 'zeroes historical fixture pressures')
add('runner', R+'src/result_envelope_binding.rs', 'fn public_nonzero_legacy_pressure_refuses_before_opaque_proof_or_export(', 'test', 'implicit', 'keep', 'refusal')
add('runner', R+'src/result_envelope_binding.rs', 'fn qualified_actual_solved_documents_match_explicit_library_and_bind_model_identity(', 'test', 'implicit', 'edit test (A1)',
    'P3: its case curved-pressure-full has pressure as its only load; stripped it is load-free (LOAD_INPUT_MISSING); expect the refusal or drop the case (already a refusal case of the test above)')
add('runner', R+'tests/preview_physics_admission.rs', 'if load["category"] == "pressure" {', 'test', 'implicit', 'edit test (strip; A1)', 'realized_joint_is_refused...: zeroes to isolate the M07 refusal')
add('runner', R+'src/bin/openpipestress-runner.rs', 'fn original_legacy_nonzero_pressure_fixture_is_not_a_current_cli_solve(', 'test', 'implicit', 'keep', 'refusal')
add('runner', R+'src/benchmark_binding.rs', '"STRESS-PRESSURE-MEMBRANE-ORIGINAL" => {', 'benchmark', 'pressure', 'remove', 'binds the legacy membrane benchmark')
add('runner', R+'src/benchmark_binding.rs', '"MECH-TP-PHYS-008-THERMAL-PRESSURE-AXIAL-EFFECTS" => {', 'benchmark', 'pressure', 'keep', 'frame-kernel benchmark with an explicit named axial force; no legacy product path')
# RE
add('RE', 'core/reporting/result_export/tests/physics_contract.rs', 'json!("legacy_pressure_v1"),', 'test', 'label', 'keep', 'tamper test: the label in exact evidence is refused')
add('RE', 'core/reporting/result_export/src/retained_precision.rs', '&& model["pressure_contract"].is_null()', 'reader-branch', 'label', 'keep', 'RS reader: any pressure_contract is G8 INVOCATION_MISMATCH on NUM')
add('RE', 'core/reporting/result_export/src/retained_precision.rs', '| "pipe_section_pressure_hoop_stress"', 'reader-branch', 'pressure', 'keep', 'kind classification (accepted B1 reader)')
# Python
add('python', 'core/analysis_runs/retained_precision.py', 'model.get("pressure_contract") is None', 'reader-branch', 'label', 'keep', 'PY reader: refuses any contract (G8 INVOCATION_MISMATCH)')
add('python', 'core/analysis_runs/records.py', '"pipe_section_pressure_hoop_stress": "stress",', 'reader-branch', 'pressure', 'keep', 'kind-to-dimension map for historical results')
add('python', 'core/product_preview/service.py', 'invented_mechanics_result.json', 'ui-path', 'pressure', 'decision D-3', 'serves the frozen legacy-pressure result as the technical-preview mechanics result')
add('python', 'tests/product_preview/test_product_preview_service.py', 'component_pressure_thrust_load_count', 'test', 'pressure', 'decision D-3', 'asserts legacy thrust and hoop rows of the frozen result')
add('python', 'tests/test_headless_runner_contract.py', 'LEGACY_PRESSURE_PREVIEW_FIXTURE = (', 'test', 'implicit', 'keep', 'final and compatibility runner refusal controls')
add('python', 'tests/test_headless_runner_contract.py', 'if (load["category"] == "pressure" or load["dimension"] == "pressure")', 'test', 'implicit', 'check (A1)', 'pressure selection in the refusal assertion')
add('python', 'tests/test_results_schema.py', 'invented_mechanics_result.json', 'test', 'pressure', 'decision D-3', 'schema checks over the frozen legacy result (hoop rows)')
add('python', 'tests/test_analysis_run_records.py', 'invented_mechanics_result.json', 'test', 'pressure', 'decision D-3', 'frozen legacy result as analysis-run input')
add('python', 'tests/test_preview_physics_consumer_contract.py', 'PRESSURE_MODEL_REAUTHOR_REQUIRED', 'test', 'implicit', 'keep', 'refusal consumer')
# app
A = 'apps/desktop/'
add('app', A+'src/features/load-cases/LoadCaseManagerPanel.tsx', '<option value="pressure">pressure</option>', 'ui-path', 'implicit', 'remove (A1)', 'authors legacy pressure primitives')
for needle in ['if (category === "pressure") return projectPressureUnit(model);', 'if (category === "pressure") return "Pressure primitive load";', 'if (category === "pressure") {']:
    add('app', A+'src/features/load-cases/LoadCaseManagerPanel.tsx', needle, 'ui-path', 'implicit', 'remove (A1)', 'pressure primitive helpers')
add('app', A+'src/App.test.tsx', 'queues and applies a pressure primitive load through the manager panel', 'test', 'implicit', 'becomes a refusal test (A1)', 'panel no longer offers the category; exact panel named')
add('app', A+'src/features/pressure-authoring/PressureAuthoringPanel.tsx', ': "legacy")', 'ui-path', 'implicit', 'edit text', '0.1.0/0.2.0 shown as pressure mode "legacy"; becomes "none (pressure-free)"')
add('app', A+'src/features/pressure-authoring/PressureAuthoringPanel.tsx', 'export const EXACT_PROFILE', 'ui-path', 'exact', 'keep', 'only profile offered')
add('app', A+'src/services/projectService.ts', 'schema_version: SUPPORTED_MODEL_SCHEMA_VERSION,', 'ui-path', 'implicit', 'keep (D-1 A)', 'blank document is 0.2.0 (implicit form, no pressure)')
add('app', A+'src/services/projectService.ts', 'export const BLANK_LOAD_STATE_PRESSURE_CONTRACT', 'ui-path', 'exact', 'keep', '0.4.0 blank carries the exact contract')
add('app', A+'src/services/previewService.ts', 'invented_mechanics_result_precision_1_sparse.json', 'ui-path', 'shared', 'held (M07 ruling)', 'browser reference preview: bundled precision-1 demo results computed with legacy pressure and joint C-150')
add('app', A+'src/features/results/retainedPrecision.ts', 'model.pressure_contract == null', 'reader-branch', 'label', 'keep', 'TS reader: any contract is G8 INVOCATION_MISMATCH on NUM')
add('app', A+'src-tauri/src/model_document_migration.rs', 'pub const SUPPORTED_MODEL_SCHEMA_VERSION: &str = "0.2.0";', 'acceptance', 'implicit', 'keep (D-1 A)', '0.1.0 -> 0.2.0 no-op migration target; never writes a pressure contract')
add('app', A+'src-tauri/src/model_document_migration.rs', 'legacy["load_cases"] = json!([{"id":"case:old","primitive_loads":[{"category":"pressure"', 'test', 'implicit', 'keep', 'migration leaves an old pressure primitive untouched; the solve refuses it')
add('app', A+'src-tauri/src/lib.rs', 'fn assert_bundled_demo_refused(', 'test', 'implicit', 'keep', 'bundled demo refused with PRESSURE_MODEL_REAUTHOR_REQUIRED')
add('ops', 'core/model_operations/operation_applier/src/lib.rs', '} else if category == "pressure" {', 'operation', 'implicit', 'becomes a refusal (A1)', 'create_primitive_load accepts the pressure category')
add('ops', 'core/model_operations/operation_applier/src/lib.rs', 'if category == "pressure" && stored_pressure_unit.is_none() {', 'operation', 'implicit', 'remove (A1)', 'unit gate for pressure primitives')
add('ops', 'core/model_operations/operation_applier/src/lib.rs', 'fn explicit_create_primitive_load_payload_applies_pressure_and_thermal_only(', 'test', 'implicit', 'edit test (A1)', 'applies a pressure primitive')
add('ops', 'core/model_operations/operation_applier/src/lib.rs', 'fn explicit_create_primitive_load_preserves_compatible_entered_units(', 'test', 'implicit', 'edit test (A1)', 'pressure unit case')
add('ops', 'core/model_operations/operation_applier/src/pressure_authoring.rs', 'Exact profile admits no pressure primitives, including zero', 'operation', 'exact', 'keep', 'profile switch already refuses primitives')
# fixtures and goldens
add('fixtures', 'fixtures/product_preview/invented_preview_model.json', '"category": "pressure"', 'fixture', 'shared', 'keep (refusal control; M07 joint for I111)', '0.1.0 demo, 4 nonzero legacy pressure primitives; bundled demo, refused today')
add('fixtures', 'fixtures/results/invented/result_export_v0_2.json', '"category": "pressure"', 'fixture', 'implicit', 'keep (historical producer cases)', '3 producer cases carry nonzero legacy pressure; runner tests zero them in memory')
add('fixtures', 'validation/witness/inputs/tp_runner_015_final_cli_solve_input.json', '"category": "pressure"', 'fixture', 'implicit', 'keep (witness evidence)', 'immutable witness input')
add('fixtures', 'fixtures/product_preview/invented_mechanics_result.json', 'pressure_hoop', 'golden', 'shared', 'decision D-3', 'frozen result of the demo (legacy nonzero pressure, joint C-150); app/Python/RE reader inputs and the deleted oracle')
for f in ['fixtures/product_preview/invented_mechanics_result_precision_1_sparse.json', 'fixtures/product_preview/invented_mechanics_result_precision_1_dense.json']:
    add('fixtures', f, 'pressure_hoop', 'golden', 'shared', 'held (M07 ruling)', "the browser's bundled precision-1 demo results (legacy pressure and joint C-150)")
# schemas and docs
add('schemas', 'schemas/results.v0.3.schema.yaml', '"product_preview_mechanics_v1",', 'schema-enum', 'implicit', 'keep', 'non-exact profile id; still produced for pressure-free 0.1.0/0.2.0')
add('schemas', 'schemas/results.v0.3.schema.yaml', 'pressure_hoop', 'schema-enum', 'pressure', 'keep', 'historical result kinds/components (published)')
add('docs', 'docs/validation_manual/cases/stress/stress-pressure-membrane-original.md', 'STRESS-PRESSURE-MEMBRANE-ORIGINAL', 'doc', 'pressure', 'remove', 'manual page of the retired membrane benchmark')
add('docs', 'docs/validation_manual/index.md', 'STRESS-PRESSURE-MEMBRANE-ORIGINAL', 'doc', 'pressure', 'edit', 'index row')
add('docs', 'validation/hand_calcs/stress/pressure_membrane.md', 'STRESS-PRESSURE-MEMBRANE-ORIGINAL', 'doc', 'pressure', 'remove', 'hand calc')
add('docs', 'validation/benchmarks/stress/src/lib.rs', 'pub fn pressure_membrane_fixture()', 'benchmark', 'pressure', 'remove', 'benchmark fixture over PressureBasis')
add('docs', 'apps/desktop/SMOKE.md', 'invented_mechanics_result.json', 'doc', 'pressure', 'decision D-3', 'smoke text over the frozen legacy result')

# B3a on b2 (WORKING_ITEMS drops it separately); completeness only
def git(*a): return subprocess.run(['git', '-C', TREE] + list(a), capture_output=True, text=True, env={'GIT_OPTIONAL_LOCKS': '0', 'PATH': '/usr/bin:/bin:/usr/local/bin:/opt/homebrew/bin'}).stdout
seen = set()
for ref, name in [('72b3e5d9ea', 'b2'), ('codex/piping-t3-b2-p-20261008', 'b2-p'), ('codex/piping-t3-b2-r-20261008', 'b2-r'), ('codex/piping-t3-b2-t-20261008', 'b2-t')]:
    sha = git('rev-parse', '--short=10', ref).strip()
    nummap = set(l.split(':', 1)[0] + ':' + l.split(':', 2)[1] for l in git('grep', '-n', 'legacy_pressure_v1', '9cd61ba201', '--', 'projects/chirality-piping', ':!projects/chirality-piping/execution').splitlines() for _ in [0])
    for l in git('grep', '-n', 'legacy_pressure_v1', ref, '--', 'projects/chirality-piping', ':!projects/chirality-piping/execution').splitlines():
        _, path, ln, text = l.split(':', 3)
        path = path[len('projects/chirality-piping/'):]
        if path in ('core/product_physics/src/pressure_runtime.rs', 'core/product_physics/src/source_receipt/tests.rs', 'core/reporting/result_export/tests/physics_contract.rs'):
            continue  # also on NUM, inventoried above
        key = (path, text.strip())
        if key in seen: continue
        seen.add(key)
        E.append(dict(area='b2 (B3a)', site=f'{ph(path)}:{ln}', symbol=text.strip()[:90], kind='b3a', premise='label',
                      disposition='dropped with B3a (WORKING_ITEMS)', note='B3a admission/test of the label', branch=f'{name} {sha}'))

E = [e for e in E if e]
counts = collections.Counter((e['area'], e['kind']) for e in E)
summary = dict(total=len(E), by_area=collections.Counter(e['area'] for e in E), by_kind=collections.Counter(e['kind'] for e in E),
               by_premise=collections.Counter(e['premise'] for e in E), by_disposition=collections.Counter(e['disposition'] for e in E),
               by_area_kind={f'{a}|{k}': v for (a, k), v in sorted(counts.items())})
json.dump(dict(basis='product code of NUM 9cd61ba201 = PR-B1 head f4a0430412 = main 7eae707bb7 after #1154 (NUM ccc087edb4 has no product diff); b2 refs for B3a', premises={
    'label': '0.3.0 with pressure_contract 1.0.0/legacy_pressure_v1', 'implicit': 'model 0.1.0/0.2.0 (no contract): pressure only as primitive loads',
    'pressure': 'legacy pressure computation or the pressure part of the historical scope', 'shared': 'historical scope code or tests used by both premises (pressure, M07)',
    'M07': "M07's user-stiffness joint premise only", 'exact': 'exact-contract site, listed for contrast'}, summary=summary, sites=E), open(OUT, 'w'), indent=1)
print(json.dumps(summary, indent=1))

# ---- normalized disposition classes (the brief's vocabulary plus three) ----
def cls(d):
    d = d.lower()
    if 'b3a' in d: return 'dropped with B3a (b2)'
    if d.startswith('held'): return 'held (M07 ruling)'
    if d.startswith('decision'): return 'decision (D-3)'
    if d.startswith('becomes a refusal'): return 'becomes a refusal'
    if d.startswith('delete'): return 'delete the test' 
    if d.startswith('remove'): return 'remove'
    if d.startswith('edit') or d.startswith('check'): return 'edit'
    if d.startswith('keep'): return 'keep'
    if d.startswith('dropped'): return 'dropped with B3a (b2)'
    return d
data = json.load(open(OUT))
for e in data['sites']:
    e['class'] = cls(e['disposition'])
    if e['class'] == 'delete the test' and e['kind'] not in ('test',): e['class'] = 'remove'
def stage(e):
    c, d = e['class'], e['disposition'].lower()
    if c == 'held (M07 ruling)': return 'held'
    if c == 'dropped with B3a (b2)': return 'b2'
    if c == 'keep': return '-'
    if 'stage 2' in d or e['kind'] in ('computation', 'benchmark'): return '2'
    if e['area'] == 'docs' and 'D-3' not in e['disposition']: return '2'
    if e['site'].split(':')[0] in ('PP/src/f1a_tests.rs', 'PP/src/f1b_tests.rs'): return '2'
    if c == 'decision (D-3)': return 'D-3'
    return '1'
for e in data['sites']:
    e['stage'] = stage(e)
data['summary']['by_stage'] = collections.Counter(e['stage'] for e in data['sites'])
by = collections.Counter((e['area'], e['class']) for e in data['sites'])
data['summary']['by_class'] = collections.Counter(e['class'] for e in data['sites'])
data['summary']['by_area_class'] = {f'{a}|{c}': v for (a, c), v in sorted(by.items())}
json.dump(data, open(OUT, 'w'), indent=1)
print(json.dumps(data['summary']['by_class'], indent=1)); print(json.dumps(data['summary']['by_stage'], indent=1))
