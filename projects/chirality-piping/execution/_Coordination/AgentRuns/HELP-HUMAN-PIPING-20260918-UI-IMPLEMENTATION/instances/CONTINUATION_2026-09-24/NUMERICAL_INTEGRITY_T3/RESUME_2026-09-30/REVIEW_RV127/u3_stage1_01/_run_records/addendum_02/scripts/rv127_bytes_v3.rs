//! RV127 probe-only harness (never committed; placed in WT/rv127/{base,cand} archive copies).
//! For each input payload and both solver modes: the SHA-256 of PP's ordinary envelope, the
//! retained direct entry's publication (W1) and its kind, the runner's serialized output, its
//! mechanics envelope, its RE export document and export unavailability, and the runner's
//! retained headless output; plus every blocking diagnostic (code, refs, message).
//! Inputs: RV127_INPUTS; output: RV127_OUT; full outputs dumped to RV127_DUMP/<index>_<mode>_<kind>.json (v3).
use open_pipe_stress_headless_runner::{
    run_preview_model_value_with_mode, run_preview_model_value_with_retained_headless, PrivacyContext,
    ProfessionalBoundary, Provenance, RedistributionStatus, Reference, RunnerOperation, RunnerRequest,
    TbdDecisions,
};
use open_pipe_stress_product_physics::{
    run_linear_static_preview_value_with_mode, run_linear_static_preview_value_with_retained_direct,
    MechanicsEnvelope, PreviewSolverMode, RetainedPublication,
};
use serde_json::{json, Value};
use sha2::{Digest, Sha256};

fn sha(bytes: &[u8]) -> String {
    format!("{:x}", Sha256::digest(bytes))
}
/// `-0.0` number tokens in serialized JSON (a "-0.0" not followed by a digit or exponent).
fn neg_zero(bytes: &[u8]) -> usize {
    let pat = b"-0.0";
    (0..bytes.len().saturating_sub(3)).filter(|&i| &bytes[i..i + 4] == pat
        && !matches!(bytes.get(i + 4), Some(c) if c.is_ascii_digit() || *c == b'e' || *c == b'E')).count()
}
fn blocking(envelope: &MechanicsEnvelope) -> Value {
    json!(envelope.diagnostics.iter().filter(|d| d.severity == "blocking")
        .map(|d| json!([d.code, d.affected_refs, d.message])).collect::<Vec<_>>())
}
fn request(model: &Value) -> RunnerRequest {
    let id = model["project"]["id"].as_str().unwrap_or("project:none");
    RunnerRequest {
        request_id: "rv127-bytes".into(),
        operation: RunnerOperation::Solve,
        operation_ref: Reference::new("api_operation", "ops.solve.job"),
        project_ref: Reference::new("project", id),
        model_ref: Reference::new("model", id),
        unit_system_ref: Reference::new("unit_system", "invented-si"),
        load_basis_refs: model["load_cases"].as_array().map(|cases| cases.iter()
            .map(|c| Reference::new("load_case", c["id"].as_str().unwrap_or(""))).collect()).unwrap_or_default(),
        input_manifest_ref: Reference::new("audit_manifest", "rv127-input-manifest"),
        requested_outputs: vec!["result_envelope".into(), "audit_manifest".into(), "diagnostics".into()],
        privacy: PrivacyContext::local_first_public_metadata(),
        provenance: Provenance {
            source_name: "RV127 byte reproduction".into(),
            source_location: "fixtures".into(),
            source_license: "project invented".into(),
            contributor: "OpenPipeStress".into(),
            contributor_certification: "invented non-engineering example".into(),
            redistribution_status: RedistributionStatus::InventedNonEngineeringExample,
            review_status: "pending".into(),
        },
        professional_boundary: ProfessionalBoundary::project_default(),
        tbd_decisions: TbdDecisions::d33_local_cli_policy(),
    }
}

#[test]
fn rv127_bytes() {
    let Ok(inputs) = std::env::var("RV127_INPUTS") else { return };
    let out = std::env::var("RV127_OUT").unwrap();
    let items: Vec<Value> = serde_json::from_slice(&std::fs::read(inputs).unwrap()).unwrap();
    use std::io::Write;
    let mut file = std::fs::File::create(&out).unwrap();
    let dump = std::env::var("RV127_DUMP").ok();
    let put = |index: usize, mode: &str, kind: &str, bytes: &[u8]| {
        if let Some(dir) = &dump {
            std::fs::write(format!("{dir}/{index}_{mode}_{kind}.json"), bytes).unwrap();
        }
    };
    for (index, item) in items.iter().enumerate() {
        for (mode_name, mode) in [("sparse_interactive", PreviewSolverMode::SparseInteractive),
                                  ("dense_scrutiny", PreviewSolverMode::DenseScrutiny)] {
            let payload = item["payload"].clone();
            let ordinary = match run_linear_static_preview_value_with_mode(payload.clone(), mode) {
                Ok(e) => { let b = serde_json::to_vec(&e).unwrap(); put(index, mode_name, "ordinary", &b); json!({"sha": sha(&b), "neg_zero": neg_zero(&b), "status": e.status.mechanics, "blocking": blocking(&e)}) }
                Err(error) => json!({"error": error}),
            };
            let retained = match run_linear_static_preview_value_with_retained_direct(payload.clone(), mode) {
                Ok(output) => {
                    let domain = output.admission().map(|a| format!("{:?}/{:?}", a.profile, a.allowance));
                    match output.into_publication() {
                        RetainedPublication::Ordinary(e) => json!({"kind": "ordinary", "sha": sha(&serde_json::to_vec(&e).unwrap()), "status": e.status.mechanics, "blocking": blocking(&e), "domain": domain}),
                        RetainedPublication::Successor(doc) => { let b = serde_json::to_vec(&doc).unwrap(); put(index, mode_name, "successor", &b); json!({"kind": "successor", "sha": sha(&b), "domain": domain}) }
                    }
                }
                Err(error) => json!({"error": error}),
            };
            let runner = match run_preview_model_value_with_mode(request(&payload["model"]), payload.clone(), mode) {
                Ok(o) => { if let Some(m) = o.mechanics_envelope.as_ref() { put(index, mode_name, "mechanics", &serde_json::to_vec(m).unwrap()); }
                    if let Some(d) = o.result_envelope_document.as_ref() { put(index, mode_name, "document", &serde_json::to_vec(d).unwrap()); }
                    put(index, mode_name, "output", &serde_json::to_vec(&o).unwrap());
                    json!({
                    "output": sha(&serde_json::to_vec(&o).unwrap()),
                    "mechanics": o.mechanics_envelope.as_ref().map(|m| sha(&serde_json::to_vec(m).unwrap())),
                    "blocking": o.mechanics_envelope.as_ref().map(blocking),
                    "document": o.result_envelope_document.as_ref().map(|d| sha(&serde_json::to_vec(d).unwrap())),
                    "document_neg_zero": o.result_envelope_document.as_ref().map(|d| neg_zero(&serde_json::to_vec(d).unwrap())),
                    "unavailability": o.canonical_export_unavailability,
                }) },
                Err(error) => json!({"error": error}),
            };
            let headless = match run_preview_model_value_with_retained_headless(request(&payload["model"]), payload.clone(), mode, None) {
                Ok(o) => {
                    let domain = o.admission().map(|a| format!("{:?}/{:?}", a.profile, a.allowance));
                    let o = o.output();
                    json!({"output": sha(&serde_json::to_vec(o).unwrap()),
                        "document": o.result_envelope_document.as_ref().map(|d| sha(&serde_json::to_vec(d).unwrap())),
                        "status": o.mechanics_envelope.as_ref().map(|m| m.status.mechanics.clone()), "domain": domain})
                }
                Err(error) => json!({"error": error}),
            };
            writeln!(file, "{}", serde_json::to_string(&json!({"set": item["set"], "label": item["label"], "mode": mode_name,
                "ordinary": ordinary, "retained_direct": retained, "runner": runner, "runner_retained_headless": headless})).unwrap()).unwrap();
            file.flush().unwrap();
        }
        eprintln!("rv127 {index}/{} {}", items.len(), item["label"]);
    }
}
