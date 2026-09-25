//! Actual-entrypoint companion to independently derived STRESS_REFERENCE X1.
//! The construction was independently checked by ASSEMBLY_ORACLE before this test.
use open_pipe_stress_product_physics::{
    run_linear_static_preview_with_mode, LinearStaticPreviewRequest, MechanicsEnvelope,
    PreviewSolverMode,
};
use serde_json::{json, Value};
use std::f64::consts::PI;

fn fixture() -> Value {
    json!({"model":{
        "schema_version":"0.3.0","document_kind":"openpipestress.product_preview.model",
        "pressure_contract":{"version":"2.0.0","mode":"exact_straight_pressure_v2"},
        "project":{"id":"project:elastic-extrema","units":{"length":"m","force":"N","angle":"rad","pressure":"Pa","stress":"Pa","temperature":"degC"}},
        "analysis_status":{"mechanics":"ready_for_preview_diagnostics","rule_check":"not_performed_user_rule_inputs_missing","professional_acceptance":"not_provided"},
        "nodes":[{"id":"node:a","position":{"x":0.0,"y":0.0,"z":0.0},"provenance":"independent_statics"},{"id":"node:b","position":{"x":1.0,"y":0.0,"z":0.0},"provenance":"independent_statics"}],
        "pipe_segments":[{"id":"pipe:a-b","from":"node:a","to":"node:b","section":{"outside_diameter":{"value":0.12,"unit":"m"},"wall_thickness":{"value":0.01,"unit":"m"}},"material":"material:m","y_reference":{"x":0.0,"y":1.0,"z":0.0},"provenance":"independent_statics"}],
        "supports":[{"id":"support:a","node":"node:a","family":"anchor","restraints":["UX","UY","UZ","RX","RY","RZ"],"provenance":"independent_statics"}],"components":[],
        "materials":[{"id":"material:m","constitutive_basis":"homogeneous_isotropic_E_nu_v1","elastic_modulus":{"value":200e9,"unit":"Pa"},"poisson_ratio":{"value":0.3,"unit":"1"},"provenance":"synthetic_isotropic_annulus"}],
        "load_cases":[{"id":"case:x1","pressure_regions":[],"primitive_loads":[],"provenance":"independent_statics"}],"combinations":[]},"materials":[]})
}
fn nodal(id: &str, direction: &str, value: f64, moment: bool) -> Value {
    json!({"id":id,"category":if moment {"concentrated_moment"} else {"concentrated_force"},"target":{"type":"node","node":"node:b"},"direction":direction,"magnitude":{"value":value,"unit":if moment {"N*m"} else {"N"}},"dimension":if moment {"moment"} else {"force"},"provenance":"independent_statics"})
}
fn solve(wire: Value, mode: PreviewSolverMode) -> MechanicsEnvelope {
    let request: LinearStaticPreviewRequest = serde_json::from_value(wire).unwrap();
    let output = run_linear_static_preview_with_mode(request, mode);
    assert_eq!(
        output.status.mechanics, "MECHANICS_SOLVED",
        "{:?}",
        output.diagnostics
    );
    assert!(!output
        .diagnostics
        .iter()
        .any(|d| d.code == "EXACT_STRESS_GOVERNING_MAXIMUM_UNAVAILABLE"));
    output
}
fn close(a: f64, b: f64, scale: f64) {
    assert!(
        a.is_finite() && (a - b).abs() <= 1e-9 * b.abs().max(scale),
        "{a:.17e} != {b:.17e}"
    );
}
#[test]
fn coverage_probe_two_cases() {
    let mut wire=fixture();
    wire["model"]["materials"][0]["elastic_modulus"]["value"]=json!(1e308);
    wire["model"]["load_cases"][0]["primitive_loads"]=json!([nodal("load:small","global_x",1000.0,false)]);
    let area=PI*(0.06_f64.powi(2)-0.05_f64.powi(2));
    let z=PI*(0.06_f64.powi(4)-0.05_f64.powi(4))/4.0/0.06;
    let mut second=wire["model"]["load_cases"][0].clone();second["id"]=json!("case:large");
    second["primitive_loads"]=json!([nodal("load:large-force","global_x",0.7*f64::MAX*area,false),nodal("load:large-moment","rotation_z",0.7*f64::MAX*z,true)]);
    wire["model"]["load_cases"].as_array_mut().unwrap().push(second);
    let request:LinearStaticPreviewRequest=serde_json::from_value(wire).unwrap();
    let output=run_linear_static_preview_with_mode(request,PreviewSolverMode::SparseInteractive);
    eprintln!("status={} max={:?} diagnostics={:?}",output.status.mechanics,output.summary.max_open_formula_stress,output.diagnostics);
    assert_eq!(output.status.mechanics,"MECHANICS_SOLVED");
    assert!(output.diagnostics.iter().any(|d|d.code=="EXACT_STRESS_GOVERNING_MAXIMUM_UNAVAILABLE"));
    assert!(output.results.iter().any(|r|r.kind=="pipe_elastic_normal_stress_maximum_v2"));
    assert!(output.summary.max_open_formula_stress.is_none(),"incomplete all-case domain cannot publish successful-subset maximum");
}
