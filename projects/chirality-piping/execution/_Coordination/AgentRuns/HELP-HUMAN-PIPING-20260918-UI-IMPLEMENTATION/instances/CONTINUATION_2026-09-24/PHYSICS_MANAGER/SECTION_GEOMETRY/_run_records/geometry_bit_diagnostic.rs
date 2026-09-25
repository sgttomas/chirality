//! Source-faithful section properties and public runtime response.
//! Independent source OD/effective-wall expectations were frozen before repair.
//! The older rounded-radii reference remains comparison evidence only.

use open_pipe_stress_product_physics::{
    run_linear_static_preview_with_mode, LinearStaticPreviewRequest, MechanicsEnvelope,
    PreviewSolverMode, ResultItem,
};
use serde_json::{json, Value};

const SOURCE: &str = include_str!("/private/tmp/piping-pressure-stress-20260924/projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/PHYSICS_MANAGER/SECTION_GEOMETRY/SOURCE_ODWALL_EXPECTATIONS.json");
const NEAR: &str = include_str!("/private/tmp/piping-pressure-stress-20260924/projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/PHYSICS_MANAGER/SECTION_GEOMETRY/NEAR_INCOMPRESSIBLE_EXPECTATIONS.json");
const CASE: &str = "case:source-section";
const REGION: &str = "region:source-section";
const PIPE: &str = "pipe:source-section";
const A: &str = "node:section-a";
const B: &str = "node:section-b";
const MODES: [PreviewSolverMode; 2] = [
    PreviewSolverMode::SparseInteractive,
    PreviewSolverMode::DenseScrutiny,
];

fn oracle() -> Value {
    serde_json::from_str(SOURCE).unwrap()
}

fn expected(case: &Value, key: &str) -> f64 {
    case[key]["f64"]
        .as_f64()
        .expect("independent finite reference")
}

fn close(actual: f64, reference: f64, zero_scale: f64, label: &str) {
    assert!(actual.is_finite(), "{label}: nonfinite {actual}");
    let tolerance = 1e-9
        * if reference == 0.0 {
            zero_scale.abs()
        } else {
            reference.abs()
        };
    assert!(
        (actual - reference).abs() <= tolerance,
        "{label}: actual={actual:.17e}; source reference={reference:.17e}; tolerance={tolerance:.17e}"
    );
}

fn anchor(id: &str, node: &str) -> Value {
    json!({"id":id,"node":node,"family":"anchor",
        "restraints":["UX","UY","UZ","RX","RY","RZ"],
        "provenance":"independent_section_geometry_control"})
}

fn fixture(inputs: &Value, fixed: bool, pressurized: bool) -> Value {
    let mut supports = vec![anchor("support:section-a", A)];
    if fixed {
        supports.push(anchor("support:section-b", B));
    }
    let mut loads = Vec::new();
    for (id, direction, dimension, unit, magnitude) in [
        (
            "load:tip-y",
            "global_y",
            "force",
            "N",
            inputs["tip_Fy_N"].as_f64().unwrap_or(0.0),
        ),
        (
            "load:tip-torque",
            "rotation_x",
            "moment",
            "N*m",
            inputs["tip_Mx_Nm"].as_f64().unwrap_or(0.0),
        ),
    ] {
        if magnitude != 0.0 {
            loads.push(json!({"id":id,"category":if dimension=="moment" {"concentrated_moment"} else {"concentrated_force"},
                "target":{"type":"node","node":B},"direction":direction,
                "dimension":dimension,"magnitude":{"value":magnitude,"unit":unit},
                "provenance":"independent_section_geometry_reference"}));
        }
    }
    let regions = if pressurized {
        vec![json!({"id":REGION,"member_pipe_ids":[PIPE],
            "pressure_basis":"internal_differential_zero_external_v1",
            "pressure":{"value":inputs["p_Pa"],"unit":"Pa"},
            "terminals":[
                {"node_ref":A,"closure_transfer":"transfers_to_wall","provenance":"explicit_test_closure"},
                {"node_ref":B,"closure_transfer":"transfers_to_wall","provenance":"explicit_test_closure"}],
            "provenance":"independent_geometry_pressure_reference"})]
    } else {
        vec![]
    };
    json!({"model":{
        "schema_version":"0.3.0","document_kind":"openpipestress.product_preview.model",
        "pressure_contract":{"version":"2.0.0","mode":"exact_straight_pressure_v2"},
        "project":{"id":"project:section-oracle","units":{"length":"m","force":"N","angle":"rad",
            "pressure":"Pa","stress":"Pa","temperature":"degC"}},
        "analysis_status":{"mechanics":"ready_for_preview_diagnostics",
            "rule_check":"not_performed_user_rule_inputs_missing","professional_acceptance":"not_provided"},
        "nodes":[{"id":A,"position":{"x":0.0,"y":0.0,"z":0.0},"provenance":"synthetic"},
            {"id":B,"position":{"x":inputs["L_m"],"y":0.0,"z":0.0},"provenance":"synthetic"}],
        "pipe_segments":[{"id":PIPE,"from":A,"to":B,"section":{
            "outside_diameter":{"value":inputs["OD_m"],"unit":"m"},
            "wall_thickness":{"value":inputs["wall_m"],"unit":"m"}},
            "material":"material:section","y_reference":{"x":0.0,"y":1.0,"z":0.0},
            "provenance":"arithmetic_geometry_control_not_manufactured_pipe"}],
        "materials":[{"id":"material:section","constitutive_basis":"homogeneous_isotropic_E_nu_v1",
            "elastic_modulus":{"value":inputs["E_Pa"],"unit":"Pa"},
            "poisson_ratio":{"value":inputs["nu"],"unit":"1"},
            "provenance":"synthetic_isotropic_input"}],
        "supports":supports,"components":[],
        "load_cases":[{"id":CASE,"primitive_loads":loads,"pressure_regions":regions,
            "provenance":"independent_reference"}],"combinations":[]
    },"materials":[]})
}

fn solve(input: Value, mode: PreviewSolverMode) -> MechanicsEnvelope {
    let request: LinearStaticPreviewRequest = serde_json::from_value(input).unwrap();
    run_linear_static_preview_with_mode(request, mode)
}

fn solved(result: &MechanicsEnvelope) {
    assert_eq!(
        result.status.mechanics, "MECHANICS_SOLVED",
        "{:?}",
        result.diagnostics
    );
    assert!(!result.accepted_model_state_mutated);
    assert!(result.results.iter().all(|r| r.value.is_finite()));
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
                && r.basis_ref
                    .as_ref()
                    .is_some_and(|b| b.ref_type == "load_case" && b.ref_id == CASE)
                && r.metadata.as_ref().is_some_and(|m| {
                    m.component == component && location.map_or(true, |l| m.location == l)
                })
        })
        .collect();
    assert_eq!(
        matching.len(),
        1,
        "missing/ambiguous actual row: {kind} {entity} {component} {location:?}"
    );
    matching[0]
}

fn scalar(
    result: &MechanicsEnvelope,
    kind: &str,
    entity: &str,
    component: &str,
    location: Option<&str>,
    unit: &str,
) -> f64 {
    let actual = row(result, kind, entity, component, location);
    assert_eq!(actual.unit, unit);
    actual.value
}

fn geometry<'a>(result: &'a MechanicsEnvelope, pressurized: bool) -> &'a Value {
    let evidence = result
        .contract_evidence
        .as_ref()
        .expect("exact source geometry evidence");
    let case = evidence["exact_cases"]
        .as_array()
        .unwrap()
        .iter()
        .find(|c| c["load_case_id"] == CASE)
        .expect("actual case evidence");
    let section = case["pipe_sections"]
        .as_array()
        .expect("all exact members have section evidence")
        .iter()
        .find(|s| s["pipe_id"] == PIPE)
        .expect("actual member source section");
    if pressurized {
        let region = evidence["pressure"]
            .as_array()
            .unwrap()
            .iter()
            .find(|p| p["region_id"] == REGION && p["load_case_id"] == CASE)
            .unwrap();
        let counterpart = region["geometry"]
            .as_array()
            .unwrap()
            .iter()
            .find(|p| p["pipe_id"] == PIPE)
            .unwrap();
        for key in [
            "geometry_basis",
            "outside_diameter_m",
            "effective_wall_thickness_m",
            "ri_m",
            "ro_m",
            "Ai_m2",
            "As_m2",
            "I_m4",
            "J_m4",
            "Z_m3",
        ] {
            assert_eq!(
                counterpart[key], section[key],
                "pressure and frame section disagree: {key}"
            );
        }
    } else {
        assert_eq!(
            evidence["pressure"],
            json!([]),
            "unpressurized pipe acquired a fake pressure region"
        );
    }
    section
}

fn check_geometry(result: &MechanicsEnvelope, case: &Value, pressurized: bool) {
    let section = geometry(result, pressurized);
    assert_eq!(section["geometry_basis"], "authored_normalized_od_wall_v1");
    assert_eq!(
        section["outside_diameter_m"].as_f64().unwrap(),
        case["inputs"]["OD_m"].as_f64().unwrap()
    );
    assert_eq!(
        section["effective_wall_thickness_m"].as_f64().unwrap(),
        case["inputs"]["wall_m"].as_f64().unwrap()
    );
    for key in ["ro", "ri"] {
        let bits =
            u64::from_str_radix(case[format!("{key}_bits_hex")].as_str().unwrap(), 16).unwrap();
        assert_eq!(
            section[format!("{key}_m")].as_f64().unwrap().to_bits(),
            bits,
            "derived rounded radius is distinct from source property basis"
        );
    }
    for (field, reference) in [
        ("Ai_m2", "Ai_m2"),
        ("As_m2", "A_m2"),
        ("I_m4", "I_m4"),
        ("J_m4", "J_m4"),
        ("Z_m3", "Z_m3"),
    ] {
        close(
            section[field].as_f64().unwrap(),
            expected(case, reference),
            0.0,
            field,
        );
    }
}

fn check_response(result: &MechanicsEnvelope, case: &Value, pressure: bool) {
    let inputs = &case["inputs"];
    let reference_x = if pressure {
        expected(case, "free_pressure_extension_m")
    } else {
        0.0
    };
    close(
        scalar(
            result,
            "global_nodal_displacement_x",
            B,
            "nodal_displacement_x",
            None,
            "mm",
        ) / 1000.0,
        reference_x,
        expected(case, "free_pressure_extension_m"),
        "source pressure extension",
    );
    close(
        scalar(
            result,
            "global_nodal_displacement_y",
            B,
            "nodal_displacement_y",
            None,
            "mm",
        ) / 1000.0,
        expected(case, "tip_bending_y_m"),
        0.0,
        "source I bending displacement",
    );
    close(
        scalar(
            result,
            "global_nodal_rotation_z",
            B,
            "nodal_rotation_z",
            None,
            "rad",
        ),
        expected(case, "tip_rotation_z_rad"),
        0.0,
        "source I bending rotation",
    );
    close(
        scalar(
            result,
            "global_nodal_rotation_x",
            B,
            "nodal_rotation_x",
            None,
            "rad",
        ),
        expected(case, "tip_rotation_x_rad"),
        0.0,
        "source J torsional rotation",
    );
    let bending = inputs["tip_Fy_N"].as_f64().unwrap() * inputs["L_m"].as_f64().unwrap()
        / expected(case, "Z_m3");
    let normal = if pressure {
        expected(case, "maximum_absolute_normal_stress_Pa")
    } else {
        bending
    };
    close(
        scalar(
            result,
            "pipe_elastic_normal_stress_maximum_v2",
            PIPE,
            "maximum_absolute_normal_stress",
            Some("governing_station"),
            "Pa",
        ),
        normal,
        0.0,
        "source A/Z normal maximum",
    );
    for (component, key, unit) in [
        ("Fy", "root_force_Fy_N", "N"),
        ("Mz", "root_moment_Mz_Nm", "N*m"),
        ("Mx", "root_moment_Mx_Nm", "N*m"),
    ] {
        close(
            scalar(
                result,
                "support_reaction_component_v2",
                "support:section-a",
                component,
                Some("node"),
                unit,
            ),
            expected(case, key),
            0.0,
            "actual support-on-pipe reaction",
        );
    }
    if pressure {
        for location in ["end_i", "quarter_1", "midspan", "quarter_3", "end_j"] {
            for (kind, component, key) in [
                ("pipe_wall_axial_force_v2", "wall_axial_force", "P_N"),
                (
                    "pipe_axial_membrane_stress_v2",
                    "axial_membrane_stress",
                    "axial_membrane_Pa",
                ),
                (
                    "pipe_lame_radial_stress_v2",
                    "lame_inner_radial_stress",
                    "lame_inner_radial_Pa",
                ),
                (
                    "pipe_lame_radial_stress_v2",
                    "lame_outer_radial_stress",
                    "lame_outer_radial_Pa",
                ),
                (
                    "pipe_lame_hoop_stress_v2",
                    "lame_inner_hoop_stress",
                    "lame_inner_hoop_Pa",
                ),
                (
                    "pipe_lame_hoop_stress_v2",
                    "lame_outer_hoop_stress",
                    "lame_outer_hoop_Pa",
                ),
            ] {
                let stress = kind.contains("stress");
                close(
                    scalar(
                        result,
                        kind,
                        PIPE,
                        component,
                        Some(location),
                        if stress { "Pa" } else { "N" },
                    ),
                    expected(case, key),
                    if stress {
                        expected(case, "axial_membrane_Pa")
                    } else {
                        expected(case, "P_N")
                    },
                    key,
                );
            }
        }
    }
}

#[test]
fn ordinary_source_annulus_properties_and_all_responses() {
    let reference = oracle();
    let case = &reference["cases"][0];
    for mode in MODES {
        let result = solve(fixture(&case["inputs"], false, true), mode);
        solved(&result);
        check_response(&result, case, true);
        check_geometry(&result, case, true);
    }
}

#[test]
fn thin_source_wall_drives_extension_stress_bending_and_torsion() {
    let reference = oracle();
    let case = &reference["cases"][1];
    for mode in MODES {
        let result = solve(fixture(&case["inputs"], false, true), mode);
        solved(&result);
        check_response(&result, case, true);
        check_geometry(&result, case, true);
        let actual = scalar(
            &result,
            "global_nodal_displacement_x",
            B,
            "nodal_displacement_x",
            None,
            "mm",
        ) / 1000.0;
        let rounded_radius = expected(
            &case["earlier_declared_radius_comparison"],
            "free_pressure_extension_m",
        );
        assert!(
            (actual - rounded_radius).abs() > 1e-9 * actual.abs(),
            "rounded-radius alternative silently replaced the source-wall target"
        );
    }
}

#[test]
fn unpressurized_thin_member_uses_same_source_section_without_fake_region() {
    let reference = oracle();
    let case = &reference["cases"][1];
    for mode in MODES {
        let result = solve(fixture(&case["inputs"], false, false), mode);
        solved(&result);
        check_response(&result, case, false);
        check_geometry(&result, case, false);
    }
}

#[test]
fn representable_i_and_j_survive_an_unrepresentable_naive_intermediate() {
    let reference = oracle();
    let case = &reference["representable_range_control"];
    assert!(expected(case, "I_m4").is_finite() && expected(case, "J_m4").is_finite());
    assert!(case["unrepresentable_intermediate"]["f64"].is_null());
    for mode in MODES {
        let result = solve(fixture(&case["inputs"], true, true), mode);
        solved(&result);
        check_geometry(&result, case, true);
        close(
            scalar(
                &result,
                "pipe_wall_axial_force_v2",
                PIPE,
                "wall_axial_force",
                Some("end_i"),
                "N",
            ),
            expected(case, "fixed_wall_force_N"),
            0.0,
            "finite range-control wall force",
        );
    }
}

#[test]
fn unrepresented_gap_and_nonrepresentable_final_sections_block() {
    let reference = oracle();
    for boundary in reference["blocked_boundaries"].as_array().unwrap() {
        let mut inputs = reference["cases"][0]["inputs"].clone();
        inputs["OD_m"] = boundary["OD_m"].clone();
        inputs["wall_m"] = boundary["wall_m"].clone();
        inputs["tip_Fy_N"] = json!(0.0);
        inputs["tip_Mx_Nm"] = json!(0.0);
        for mode in MODES {
            let result = solve(fixture(&inputs, true, true), mode);
            assert_ne!(
                result.status.mechanics, "MECHANICS_SOLVED",
                "invalid range control {}",
                boundary["id"]
            );
            assert!(result
                .diagnostics
                .iter()
                .any(|d| d.severity == "blocking" || d.severity == "failure"));
            assert!(result.results.iter().all(|r| r.value.is_finite()));
            assert!(!result
                .results
                .iter()
                .any(|r| r.kind == "pipe_wall_axial_force_v2"));
        }
    }
}

#[test]
fn near_incompressible_source_net_load_retains_its_nonzero_extension() {
    let references: Value = serde_json::from_str(NEAR).unwrap();
    for case in references["cases"].as_array().unwrap() {
        let mut inputs = references["inputs"].clone();
        let bits = u64::from_str_radix(case["nu_bits_hex"].as_str().unwrap(), 16).unwrap();
        inputs["nu"] = json!(f64::from_bits(bits));
        for mode in MODES {
            let result = solve(fixture(&inputs, false, true), mode);
            solved(&result);
            let displacement = scalar(
                &result,
                "global_nodal_displacement_x",
                B,
                "nodal_displacement_x",
                None,
                "mm",
            ) / 1000.0;
            close(
                displacement,
                expected(case, "extension_m"),
                0.0,
                "near-incompressible source extension",
            );
            assert!(
                displacement > 0.0,
                "admissible nonzero source load was lost"
            );
            let pressure = &result.contract_evidence.as_ref().unwrap()["pressure"][0];
            let actual_nu = pressure["materials"][0]["nu"]
                .as_f64()
                .expect("actual selected nu");
            assert_eq!(actual_nu.to_bits(), bits);
            close(
                scalar(
                    &result,
                    "pipe_wall_axial_force_v2",
                    PIPE,
                    "wall_axial_force",
                    Some("end_j"),
                    "N",
                ),
                expected(case, "wall_force_N"),
                0.0,
                "near-incompressible wall force",
            );
        }
    }
    let mut invalid = references["inputs"].clone();
    invalid["nu"] = json!(0.5);
    for mode in MODES {
        let result = solve(fixture(&invalid, false, true), mode);
        assert_ne!(result.status.mechanics, "MECHANICS_SOLVED");
        assert!(result
            .diagnostics
            .iter()
            .any(|d| d.code == "EXACT_PRESSURE_MATERIAL_INVALID"));
    }
}

fn main() {
    let all=oracle();
    let large=&all["representable_range_control"];
    let input=&large["inputs"];
    println!("{}",json!({"event":"source_input_decode","case":"range","OD":input["OD_m"],"OD_bits":format!("{:016x}",input["OD_m"].as_f64().unwrap().to_bits()),"wall":input["wall_m"],"wall_bits":format!("{:016x}",input["wall_m"].as_f64().unwrap().to_bits()),"expected_OD_bits":"4ffba2bfd0d5ff5b","expected_wall_bits":"4fdba2bfd0d5ff5b"}));
    for mode in MODES {
        let out=solve(fixture(input,true,true),mode);
        println!("{}",json!({"event":"range_geometry","mode":mode.as_str(),"status":out.status.mechanics,"section":geometry(&out,true)}));
    }
    let refs:Value=serde_json::from_str(NEAR).unwrap();
    for case in refs["cases"].as_array().unwrap() {
        let mut input=refs["inputs"].clone();
        let bits=u64::from_str_radix(case["nu_bits_hex"].as_str().unwrap(),16).unwrap();
        input["nu"]=json!(f64::from_bits(bits)); // identical to unchanged original test
        for mode in MODES {
            let out=solve(fixture(&input,false,true),mode);
            let ux=scalar(&out,"global_nodal_displacement_x",B,"nodal_displacement_x",None,"mm")/1000.0;
            let reference=expected(case,"extension_m");
            let area=geometry(&out,true)["As_m2"].as_f64().unwrap();
            let nu=out.contract_evidence.as_ref().unwrap()["pressure"][0]["materials"][0]["nu"].as_f64().unwrap();
            println!("{}",json!({"event":"near_response","reference_case":case["id"],"mode":mode.as_str(),"status":out.status.mechanics,"input_nu_bits":format!("{:016x}",bits),"reported_nu_bits":format!("{:016x}",nu.to_bits()),"source_OD_bits":format!("{:016x}",input["OD_m"].as_f64().unwrap().to_bits()),"source_wall_bits":format!("{:016x}",input["wall_m"].as_f64().unwrap().to_bits()),"actual_extension_m":ux,"reference_extension_m":reference,"relative_extension_error":(ux-reference)/reference,"response_inferred_rhs_N":ux*input["E_Pa"].as_f64().unwrap()*area/input["L_m"].as_f64().unwrap(),"source_reference_rhs_N":expected(case,"source_net_axial_rhs_N"),"inferred_rhs_status":"derived from response and declared section; not a direct captured assembly vector"}));
        }
    }
}
