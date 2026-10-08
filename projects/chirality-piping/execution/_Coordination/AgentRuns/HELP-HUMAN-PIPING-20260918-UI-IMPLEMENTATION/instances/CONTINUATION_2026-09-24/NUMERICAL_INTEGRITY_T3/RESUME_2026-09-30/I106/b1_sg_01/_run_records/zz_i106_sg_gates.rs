//! I106 B1 SG (disposable copies only, never committed): I61's u9_g8_01 pressure harness
//! (`R/I61/u9_g8_01/_run_records/zz_i61_u9g8_pressure.rs`), adapted to B1. Its four requests and
//! their records are I61's; B1 adds three:
//! - `milestone_two_cases_pressure_on_second`: the milestone with a copy of its one case as
//!   `case-2` (load ids suffixed `:2`), with one pressure region on `case-2` only. Inside D1.4 at
//!   C = 3, so D1.5's every-case check refuses it (B1 SA);
//! - `n05_two_cases`: SP's multi-case coexistence pin input (`retained_facade_tests.rs`
//!   `n05_two_cases`, ported verbatim, reading the fixture by path);
//! - `w_c2`: the request inside the committed W-C2 successor fixture of each mode (absent in a tree
//!   without it), whose registered Direct successor is compared with that fixture's `source`.
//! For each request and mode it records the value route's envelope and the Direct entry's one
//! publication: its bytes, class (`exact`, the value route's bytes; `successor`), build status,
//! G-A's refusal (clause and fact), the private W1 result, every RETAINED_PRECISION_UNAVAILABLE
//! diagnostic (`notices`, as I61 counted) and the N1 notices among them (`n1_notices`).
//! Expectations are checked by the records-side summary, not here.
use super::*;
use serde_json::{json, Value};
use sha2::{Digest, Sha256};
use std::path::Path;

const PROV: &str = "invented_t3_f1b_w2_runtime_input_no_library_data";
const ALL: [&str; 6] = ["UX", "UY", "UZ", "RX", "RY", "RZ"];

fn sha(bytes: &[u8]) -> String { format!("{:x}", Sha256::digest(bytes)) }
fn bytes(e: &MechanicsEnvelope) -> Vec<u8> { serde_json::to_vec(e).unwrap() }

/// Verbatim port of `tests/f1b_w2_runtime.rs::phys_r4` at the PR head.
fn phys_r4(pressurized: bool) -> Value {
    let (a, b) = ("node:section-a", "node:section-b");
    let fixed = |id: &str, node: &str| {
        json!({"id": id, "node": node, "family": "anchor", "restraints": ALL,
               "provenance": "independent_section_geometry_control"})
    };
    let mut supports = vec![fixed("support:section-a", a)];
    let mut loads = Vec::new();
    let mut regions = Vec::new();
    if pressurized {
        supports.push(fixed("support:section-b", b));
        regions.push(json!({"id": "region:source-section", "member_pipe_ids": ["pipe:source-section"],
            "pressure_basis": "internal_differential_zero_external_v1",
            "pressure": {"value": 4.7e-170, "unit": "Pa"},
            "terminals": [
                {"node_ref": a, "closure_transfer": "transfers_to_wall", "provenance": "explicit_test_closure"},
                {"node_ref": b, "closure_transfer": "transfers_to_wall", "provenance": "explicit_test_closure"}],
            "provenance": "independent_geometry_pressure_reference"}));
    } else {
        let tip = f64::from_bits(0x0031fa182c40c60d);
        loads.push(json!({"id": "load:tip-y", "category": "concentrated_force",
            "target": {"type": "node", "node": b}, "direction": "global_y", "dimension": "force",
            "magnitude": {"value": tip, "unit": "N"}, "provenance": PROV}));
        loads.push(
            json!({"id": "load:tip-torque", "category": "concentrated_moment",
            "target": {"type": "node", "node": b}, "direction": "rotation_x", "dimension": "moment",
            "magnitude": {"value": tip, "unit": "N*m"}, "provenance": PROV}),
        );
    }
    json!({"model": {
        "schema_version": "0.3.0", "document_kind": "openpipestress.product_preview.model",
        "pressure_contract": {"version": "2.0.0", "mode": "exact_straight_pressure_v2"},
        "project": {"id": "project:section-oracle", "units": {"length": "m", "force": "N", "angle": "rad",
            "pressure": "Pa", "stress": "Pa", "temperature": "degC"}},
        "analysis_status": {"mechanics": "ready_for_preview_diagnostics",
            "rule_check": "not_performed_user_rule_inputs_missing", "professional_acceptance": "not_provided"},
        "nodes": [{"id": a, "position": {"x": 0.0, "y": 0.0, "z": 0.0}, "provenance": PROV},
            {"id": b, "position": {"x": 1.0, "y": 0.0, "z": 0.0}, "provenance": PROV}],
        "pipe_segments": [{"id": "pipe:source-section", "from": a, "to": b, "section": {
            "outside_diameter": {"value": 4e-77, "unit": "m"},
            "wall_thickness": {"value": 1e-77, "unit": "m"}},
            "material": "material:section", "y_reference": {"x": 0.0, "y": 1.0, "z": 0.0},
            "provenance": PROV}],
        "materials": [{"id": "material:section", "constitutive_basis": "homogeneous_isotropic_E_nu_v1",
            "elastic_modulus": {"value": 1.0, "unit": "Pa"},
            "poisson_ratio": {"value": 0.1, "unit": "1"}, "provenance": PROV}],
        "supports": supports, "components": [],
        "load_cases": [{"id": "case:source-section", "primitive_loads": loads, "pressure_regions": regions,
            "provenance": PROV}], "combinations": []
    }, "materials": []})
}

fn milestone() -> Value {
    let path = Path::new(env!("CARGO_MANIFEST_DIR")).join("../../fixtures/product_preview/rf_skew_t_cant_off_122_r1e-04.request.json");
    serde_json::from_slice(&std::fs::read(path).unwrap()).unwrap()
}

/// The milestone with one pressure region on its first member, in its own (0.1.0) namespace:
/// the only change is the case's `pressure_regions`.
fn milestone_with_pressure() -> Value {
    let mut raw = milestone();
    let pipe = raw["model"]["pipe_segments"][0].clone();
    let (id, from, to) = (pipe["id"].clone(), pipe["from"].clone(), pipe["to"].clone());
    raw["model"]["load_cases"][0]["pressure_regions"] = json!([{"id": "region:i61-u9g8", "member_pipe_ids": [id],
        "pressure_basis": "internal_differential_zero_external_v1",
        "pressure": {"value": 1.0e5, "unit": "Pa"},
        "terminals": [
            {"node_ref": from, "closure_transfer": "transfers_to_wall", "provenance": "explicit_test_closure"},
            {"node_ref": to, "closure_transfer": "transfers_to_wall", "provenance": "explicit_test_closure"}],
        "provenance": "invented_i61_u9g8_pressure_control"}]);
    raw
}

/// B1: the milestone with a second case (`case-2`, a copy, load ids suffixed `:2`) that alone
/// carries one pressure region: c = 2, the pressure on the non-first case.
fn milestone_two_cases_pressure_on_second() -> Value {
    let mut raw = milestone();
    let mut second = raw["model"]["load_cases"][0].clone();
    second["id"] = json!("case-2");
    for load in second["primitive_loads"].as_array_mut().unwrap() {
        load["id"] = json!(format!("{}:2", load["id"].as_str().unwrap()));
    }
    raw["model"]["load_cases"].as_array_mut().unwrap().push(second);
    let with_pressure = milestone_with_pressure();
    raw["model"]["load_cases"][1]["pressure_regions"] = with_pressure["model"]["load_cases"][0]["pressure_regions"].clone();
    raw
}

/// Verbatim port of `retained_facade_tests.rs::n05_two_cases` at `0d19f995b5` (SP's multi-case
/// coexistence pin input), reading the fixture by path instead of `include_str!`.
fn n05_two_cases() -> Value {
    let path = Path::new(env!("CARGO_MANIFEST_DIR")).join("../../fixtures/product_preview/source_blocks/n05-sparse_interactive.request.json");
    let mut raw: Value = serde_json::from_slice(&std::fs::read(path).unwrap()).unwrap();
    let mut second = raw["model"]["load_cases"][0].clone();
    second["id"] = json!("case-2");
    for load in second["primitive_loads"].as_array_mut().unwrap() {
        load["id"] = json!(format!("{}:2", load["id"].as_str().unwrap()));
    }
    raw["model"]["load_cases"].as_array_mut().unwrap().push(second);
    raw
}

/// The request inside the committed W-C2 successor fixture of `mode`, if the tree has it.
fn w_c2_request(mode: PreviewSolverMode) -> Option<Value> {
    let path = Path::new(env!("CARGO_MANIFEST_DIR")).join(format!("../../fixtures/results/retained_precision_w_c2_successor_{}.json", mode.as_str()));
    let doc: Value = serde_json::from_slice(&std::fs::read(path).ok()?).unwrap();
    Some(doc["invocation"]["request"].clone())
}

#[test]
#[ignore]
fn zz_i106_sg_gates() {
    let cases = [("milestone", Some(milestone())), ("milestone_with_pressure", Some(milestone_with_pressure())),
        ("phys_r4_pressurized", Some(phys_r4(true))), ("phys_r4_without_pressure", Some(phys_r4(false))),
        ("milestone_two_cases_pressure_on_second", Some(milestone_two_cases_pressure_on_second())),
        ("n05_two_cases", Some(n05_two_cases())), ("w_c2", None)];
    let mut rows = Vec::new();
    for (label, fixed) in cases {
        for mode in [PreviewSolverMode::SparseInteractive, PreviewSolverMode::DenseScrutiny] {
            let Some(raw) = fixed.clone().or_else(|| w_c2_request(mode)) else {
                rows.push(json!({"label": label, "mode": mode.as_str(), "direct": "ABSENT"}));
                continue;
            };
            let value = run_linear_static_preview_value_with_mode(raw.clone(), mode);
            let value_bytes = value.as_ref().map(bytes).ok();
            let (value_status, blocking): (String, Vec<String>) = match &value {
                Ok(e) => (e.status.mechanics.clone(), e.diagnostics.iter().filter(|d| d.severity == "blocking").map(|d| d.code.clone()).collect()),
                Err(s) => (format!("ERR:{s}"), vec![]),
            };
            let out = run_linear_static_preview_value_with_retained_direct(raw.clone(), mode);
            let row = match out {
                Err(s) => json!({"label": label, "mode": mode.as_str(), "direct": format!("ERR:{s}")}),
                Ok(o) => {
                    let profile = o.admission().map(|r| format!("{:?}", r.profile));
                    let refusal = o.admission().and_then(|r| r.law().refusal.map(|x| format!("{x:?}")));
                    let clause = o.admission().and_then(|r| r.law().refusal.map(|x| x.clause().map_or("bound", |c| c.id()).to_string()));
                    let cause = match o.retained() { None => "none".to_string(), Some(Ok(_)) => "successor".into(), Some(Err(f)) => format!("{f:?}") };
                    let successor = o.successor().is_some();
                    let published = match o.into_publication() {
                        RetainedPublication::Successor(v) => serde_json::to_vec(&v).unwrap(),
                        RetainedPublication::Ordinary(e) => bytes(&e),
                    };
                    if successor {   // the published successor, for a value comparison with its pinned fixture
                        let dir = std::env::var("I106_SG_GATES_OUT").expect("I106_SG_GATES_OUT");
                        std::fs::write(format!("{dir}.successor_{label}_{}.json", mode.as_str()), &published).unwrap();
                    }
                    let notices = serde_json::from_slice::<Value>(&published).ok()
                        .and_then(|p| p["diagnostics"].as_array().map(|d| d.iter().filter(|x| x["code"] == "RETAINED_PRECISION_UNAVAILABLE").count()))
                        .unwrap_or(0);
                    let n1_notices = serde_json::from_slice::<Value>(&published).ok()
                        .and_then(|p| p["diagnostics"].as_array().map(|d| d.iter().filter(|x| x["code"] == "RETAINED_PRECISION_UNAVAILABLE"
                            && x["message"].as_str().is_some_and(|m| m.starts_with(RETAINED_UNAVAILABLE_NOTICE))).count()))
                        .unwrap_or(0);
                    let class = if successor { "successor" } else if Some(&published) == value_bytes.as_ref() { "exact" } else { "OTHER" };
                    json!({"label": label, "mode": mode.as_str(), "value_sha": value_bytes.as_ref().map(|b| sha(b)),
                        "value_status": value_status, "value_blocking": blocking,
                        "direct_sha": sha(&published), "class": class, "notices": notices, "n1_notices": n1_notices,
                        "load_cases": raw["model"]["load_cases"].as_array().map_or(0, |c| c.len()),
                        "profile": profile, "refusal": refusal, "clause": clause, "cause": cause})
                }
            };
            rows.push(row);
        }
    }
    let out = std::env::var("I106_SG_GATES_OUT").expect("I106_SG_GATES_OUT");
    std::fs::write(&out, serde_json::to_string_pretty(&rows).unwrap() + "\n").unwrap();
    println!("I106_SG_GATES_OUT rows={}", rows.len());
}
