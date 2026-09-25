//! Manager diagnostic clone checking declared annulus/assembly coherence.
//! The new thin-wall control was authored after source inspection; it is not an
//! independently frozen engineering oracle. Original helper code came from the
//! pressure integration tests; this diagnostic is superseded by independent qualification.

use open_pipe_stress_product_physics::{
    run_linear_static_preview_with_mode, LinearStaticPreviewRequest, MechanicsEnvelope,
    PreviewSolverMode, ResultItem,
};
use serde_json::{json, Value};
use std::f64::consts::PI;

const CASE: &str = "case:pressure-oracle";
const REGION: &str = "region:pressure-oracle";
const PIPE: &str = "pipe:A-B";
const ROOT: &str = "node:A";
const TIP: &str = "node:B";
const ROOT_SUPPORT: &str = "support:A";
const TIP_SUPPORT: &str = "support:B";
const AS: f64 = 0.0011 * PI;
const EA: f64 = 220_000_000.0 * PI;
const P: f64 = 5000.0 * PI;
const LENGTH: f64 = 6.0;
const STATIONS: [(&str, f64); 5] = [
    ("end_i", 0.0),
    ("quarter_1", 0.25),
    ("midspan", 0.5),
    ("quarter_3", 0.75),
    ("end_j", 1.0),
];
const MODES: [PreviewSolverMode; 2] = [
    PreviewSolverMode::SparseInteractive,
    PreviewSolverMode::DenseScrutiny,
];

fn close(actual: f64, expected: f64, zero_scale: f64, context: &str) {
    assert!(actual.is_finite(), "{context}: nonfinite {actual}");
    let tolerance = 1.0e-9
        * if expected == 0.0 {
            zero_scale.abs()
        } else {
            expected.abs()
        };
    assert!(
        (actual - expected).abs() <= tolerance,
        "{context}: actual={actual:.17e}; expected={expected:.17e}; tolerance={tolerance:.17e}"
    );
}

fn node(id: &str, position: [f64; 3]) -> Value {
    json!({"id":id,"position":{"x":position[0],"y":position[1],"z":position[2]},
        "provenance":"independent_pressure_runtime_oracle"})
}

fn anchor(id: &str, node_id: &str) -> Value {
    json!({"id":id,"node":node_id,"family":"anchor",
        "restraints":["UX","UY","UZ","RX","RY","RZ"],
        "provenance":"independent_pressure_runtime_oracle"})
}

fn terminal(node_id: &str, transfer: bool) -> Value {
    json!({"node_ref":node_id,"closure_transfer":if transfer {"transfers_to_wall"}
        else {"separately_supported_or_compensated"},
        "provenance":"explicit_independent_pressure_boundary"})
}

fn material(id: &str, e: f64, nu: f64) -> Value {
    json!({"id":id,"constitutive_basis":"homogeneous_isotropic_E_nu_v1",
        "elastic_modulus":{"value":e,"unit":"Pa"},
        "poisson_ratio":{"value":nu,"unit":"1"},
        "thermal_expansion_coefficient":{"value":0.000012,"unit":"1/degC"},
        "temperature_points":[],"provenance":"synthetic_isotropic_reference_no_catalog"})
}

fn pipe(id: &str, from: &str, to: &str, outside: f64, wall: f64, material_id: &str) -> Value {
    json!({"id":id,"from":from,"to":to,
        "section":{"outside_diameter":{"value":outside,"unit":"m"},
            "wall_thickness":{"value":wall,"unit":"m"}},
        "material":material_id,"y_reference":{"x":0.0,"y":0.0,"z":1.0},
        "provenance":"synthetic_straight_annulus"})
}

fn model(fixed: bool, transfer: bool, thermal: f64) -> Value {
    let mut supports = vec![anchor(ROOT_SUPPORT, ROOT)];
    if fixed {
        supports.push(anchor(TIP_SUPPORT, TIP));
    }
    let loads = if thermal == 0.0 {
        vec![]
    } else {
        vec![json!({"id":"load:thermal","category":"thermal",
            "target":{"type":"element","pipe":PIPE},"direction":"global_x",
            "magnitude":{"value":thermal/0.000012,"unit":"degC"},
            "dimension":"temperature_interval","provenance":"independent_thermal_strain"})]
    };
    json!({"model":{
        "schema_version":"0.3.0","document_kind":"openpipestress.product_preview.model",
        "pressure_contract":{"version":"2.0.0","mode":"exact_straight_pressure_v2"},
        "project":{"id":"project:pressure-oracle","units":{"length":"m","force":"N",
            "angle":"rad","pressure":"Pa","stress":"Pa","temperature":"degC"}},
        "analysis_status":{"mechanics":"ready_for_preview_diagnostics",
            "rule_check":"not_performed_user_rule_inputs_missing","professional_acceptance":"not_provided"},
        "nodes":[node(ROOT,[0.0,0.0,0.0]),node(TIP,[LENGTH,0.0,0.0])],
        "pipe_segments":[pipe(PIPE,ROOT,TIP,0.12,0.01,"material:one")],
        "supports":supports,"components":[],
        "materials":[material("material:one",200e9,0.3)],
        "load_cases":[{"id":CASE,"primitive_loads":loads,"pressure_regions":[{
            "id":REGION,"member_pipe_ids":[PIPE],
            "pressure_basis":"internal_differential_zero_external_v1",
            "pressure":{"value":2e6,"unit":"Pa"},
            "terminals":[terminal(ROOT,transfer),terminal(TIP,transfer)],
            "provenance":"independent_pressure_region"}],
            "provenance":"synthetic_load_case"}],"combinations":[]
    },"materials":[]})
}

fn solve(input: Value, mode: PreviewSolverMode) -> MechanicsEnvelope {
    let request: LinearStaticPreviewRequest = serde_json::from_value(input)
        .expect("the independently authored public DTO must deserialize");
    run_linear_static_preview_with_mode(request, mode)
}

fn solved(result: &MechanicsEnvelope) {
    assert_eq!(
        result.status.mechanics, "MECHANICS_SOLVED",
        "public entrypoint must solve the supported reference: {:?}",
        result.diagnostics
    );
    assert!(!result.accepted_model_state_mutated);
    assert!(result.results.iter().all(|r| r.value.is_finite()));
    assert!(
        !result
            .diagnostics
            .iter()
            .any(|d| d.severity == "blocking" || d.severity == "failure"),
        "successful reference carries blocking diagnostics: {:?}",
        result.diagnostics
    );
}

fn row<'a>(
    result: &'a MechanicsEnvelope,
    kind: &str,
    entity: &str,
    component: &str,
    location: Option<&str>,
) -> &'a ResultItem {
    let matching: Vec<_> = result
        .results
        .iter()
        .filter(|r| {
            r.kind == kind
                && r.entity_ref == entity
                && r.metadata.as_ref().is_some_and(|m| {
                    m.component == component && location.is_none_or(|loc| m.location == loc)
                })
        })
        .collect();
    assert_eq!(
        matching.len(),
        1,
        "expected one real row kind={kind}, entity={entity}, component={component}, location={location:?}; candidates={:?}",
        result.results.iter().filter(|r| r.entity_ref == entity).collect::<Vec<_>>()
    );
    matching[0]
}

fn displacement(result: &MechanicsEnvelope, node_id: &str, vector: [f64; 3], scale_m: f64) {
    for (axis, expected) in ["x", "y", "z"].iter().zip(vector) {
        let r = row(
            result,
            &format!("global_nodal_displacement_{axis}"),
            node_id,
            &format!("nodal_displacement_{axis}"),
            None,
        );
        assert_eq!(r.unit, "mm");
        close(
            r.value / 1000.0,
            expected,
            scale_m,
            &format!("{node_id} displacement {axis}"),
        );
        let rotation = row(
            result,
            &format!("global_nodal_rotation_{axis}"),
            node_id,
            &format!("nodal_rotation_{axis}"),
            None,
        );
        assert_eq!(rotation.unit, "rad");
        close(
            rotation.value,
            0.0,
            scale_m / LENGTH,
            &format!("{node_id} rotation {axis}"),
        );
    }
}

fn support(result: &MechanicsEnvelope, id: &str, force: [f64; 3], force_scale: f64) {
    for (component, expected) in ["Fx", "Fy", "Fz"].into_iter().zip(force) {
        let r = row(
            result,
            "support_reaction_component_v2",
            id,
            component,
            Some("node"),
        );
        assert_eq!(r.unit, "N");
        assert_eq!(r.metadata.as_ref().unwrap().coordinate_system, "global");
        close(r.value, expected, force_scale, &format!("{id} {component}"));
    }
    for component in ["Mx", "My", "Mz"] {
        let r = row(
            result,
            "support_reaction_component_v2",
            id,
            component,
            Some("node"),
        );
        assert_eq!(r.unit, "N*m");
        assert_eq!(r.metadata.as_ref().unwrap().coordinate_system, "global");
        close(
            r.value,
            0.0,
            force_scale * LENGTH,
            &format!("{id} {component}"),
        );
    }
}

fn pressure_row(
    result: &MechanicsEnvelope,
    kind: &str,
    pipe_id: &str,
    component: &str,
    location: &str,
    expected: f64,
    scale: f64,
) {
    let r = row(result, kind, pipe_id, component, Some(location));
    let stress = kind.contains("stress");
    assert_eq!(r.unit, if stress { "Pa" } else { "N" });
    assert_eq!(
        r.metadata.as_ref().unwrap().coordinate_system,
        if stress {
            "pipe_section"
        } else {
            "element_local"
        }
    );
    let basis = r
        .basis_ref
        .as_ref()
        .expect("new physical rows retain their actual case identity");
    assert_eq!(basis.ref_type, "load_case");
    assert_eq!(basis.ref_id, CASE);
    close(
        r.value,
        expected,
        scale,
        &format!("{pipe_id} {component} {location}"),
    );
}

fn pressure_fields(
    result: &MechanicsEnvelope,
    pipe_id: &str,
    wall_at_fraction: impl Fn(f64) -> f64,
    p: f64,
    ri: f64,
    ro: f64,
    force_scale: f64,
) {
    let area = PI * (ro * ro - ri * ri);
    // Frozen common bore is exactly 0.05 m: keep the analytical area coefficient
    // identical to P's independent definition, so exact zero S is not replaced
    // by cancellation noise from a different floating expression.
    assert_eq!(ri, 0.05);
    let cap = p * 0.0025 * PI;
    let hoop_inner = p * (ro * ro + ri * ri) / (ro * ro - ri * ri);
    let hoop_outer = p * 2.0 * ri * ri / (ro * ro - ri * ri);
    for (location, fraction) in STATIONS {
        let wall = wall_at_fraction(fraction);
        for (kind, component, expected, scale) in [
            (
                "pipe_wall_axial_force_v2",
                "wall_axial_force",
                wall,
                force_scale,
            ),
            (
                "pipe_effective_axial_force_v2",
                "effective_axial_force",
                wall - cap,
                force_scale,
            ),
            (
                "pipe_axial_membrane_stress_v2",
                "axial_membrane_stress",
                wall / area,
                force_scale / area,
            ),
            (
                "pipe_lame_radial_stress_v2",
                "lame_inner_radial_stress",
                -p,
                force_scale / area,
            ),
            (
                "pipe_lame_radial_stress_v2",
                "lame_outer_radial_stress",
                0.0,
                force_scale / area,
            ),
            (
                "pipe_lame_hoop_stress_v2",
                "lame_inner_hoop_stress",
                hoop_inner,
                force_scale / area,
            ),
            (
                "pipe_lame_hoop_stress_v2",
                "lame_outer_hoop_stress",
                hoop_outer,
                force_scale / area,
            ),
        ] {
            pressure_row(result, kind, pipe_id, component, location, expected, scale);
        }
    }
    pressure_row(
        result,
        "pipe_wall_endpoint_action_v2",
        pipe_id,
        "wall_axial_end_action",
        "end_i",
        -wall_at_fraction(0.0),
        force_scale,
    );
    pressure_row(
        result,
        "pipe_wall_endpoint_action_v2",
        pipe_id,
        "wall_axial_end_action",
        "end_j",
        wall_at_fraction(1.0),
        force_scale,
    );
    for r in result.results.iter().filter(|r| r.entity_ref == pipe_id) {
        assert!(
            r.kind != "element_local_axial_force"
                && r.kind != "element_local_axial_normal_stress"
                && !r.kind.contains("pressure_longitudinal")
                && !r.kind.contains("pressure_hoop"),
            "exact member leaked competing legacy pressure/axial semantics: {r:?}"
        );
    }
}

fn region_evidence(result: &MechanicsEnvelope, members: &[&str]) {
    let pressure = result
        .contract_evidence
        .as_ref()
        .expect("bound normalized pressure evidence")["pressure"]
        .as_array()
        .expect("pressure evidence array");
    let entry = pressure
        .iter()
        .find(|p| p["region_id"] == REGION && p["load_case_id"] == CASE)
        .expect("region and load case jointly identify actual normalized inputs");
    for member in members {
        assert!(entry["member_pipe_ids"]
            .as_array()
            .unwrap()
            .iter()
            .any(|v| v == member));
    }
    let ids = entry["result_ids"]
        .as_array()
        .expect("region evidence binds actual pressure rows");
    for r in result.results.iter().filter(|r| pressure_kind(&r.kind)) {
        assert!(
            ids.iter().any(|id| id == &r.id),
            "pressure row absent from region mapping: {}",
            r.id
        );
    }
}

fn pressure_kind(kind: &str) -> bool {
    matches!(
        kind,
        "pipe_wall_endpoint_action_v2"
            | "pipe_wall_axial_force_v2"
            | "pipe_effective_axial_force_v2"
            | "pipe_axial_membrane_stress_v2"
            | "pipe_lame_radial_stress_v2"
            | "pipe_lame_hoop_stress_v2"
    )
}

fn case_row<'a>(
    result: &'a MechanicsEnvelope,
    case_id: &str,
    kind: &str,
    entity: &str,
    component: &str,
    location: Option<&str>,
) -> &'a ResultItem {
    let matching: Vec<_> = result
        .results
        .iter()
        .filter(|r| {
            r.kind == kind
                && r.entity_ref == entity
                && r.basis_ref
                    .as_ref()
                    .is_some_and(|b| b.ref_type == "load_case" && b.ref_id == case_id)
                && r.metadata.as_ref().is_some_and(|m| {
                    m.component == component && location.map_or(true, |l| m.location == l)
                })
        })
        .collect();
    assert_eq!(matching.len(),1,"case-qualified real row missing/ambiguous: {case_id} {kind} {entity} {component} {location:?}");
    matching[0]
}


#[test]
fn thin_annulus_runtime_geometry_coherence_probe() {
    let mut input=model(false,true,0.0);
    input["model"]["pipe_segments"][0]["section"]["wall_thickness"]["value"]=json!(1e-12);
    input["model"]["load_cases"][0]["pressure_regions"][0]["pressure"]["value"]=json!(1e-6);
    let output=solve(input,PreviewSolverMode::SparseInteractive);solved(&output);
    let geometry=&output.contract_evidence.as_ref().unwrap()["pressure"][0]["geometry"][0];
    let ri=geometry["ri_m"].as_f64().unwrap();let ro=geometry["ro_m"].as_f64().unwrap();
    // Diagnostic coherence check from the actually declared binary64 radii, not a new engineering oracle.
    let expected=6.0*0.4*1e-6*ri*ri/(200e9*(ro-ri)*(ro+ri));
    let ux=output.results.iter().find(|r|r.entity_ref==TIP && r.metadata.as_ref().is_some_and(|m|m.component=="nodal_displacement_x")).unwrap().value/1000.0;
    eprintln!("ri={ri:.17e} ro={ro:.17e} expected={expected:.17e} actual={ux:.17e} relative={:.17e}",(ux-expected)/expected);
    close(ux,expected,expected,"declared annulus geometry/assembly coherence");
}
