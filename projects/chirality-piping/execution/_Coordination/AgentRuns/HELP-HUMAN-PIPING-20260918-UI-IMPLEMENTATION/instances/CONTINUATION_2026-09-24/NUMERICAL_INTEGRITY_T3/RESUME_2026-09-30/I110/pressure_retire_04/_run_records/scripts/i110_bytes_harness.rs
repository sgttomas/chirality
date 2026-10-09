//! I110 round 2 probe-only harness (never committed): for each input payload and both
//! solver modes, the SHA-256 of (1) PP's ordinary envelope, (2) the retained direct
//! entry's publication (and its kind), (3) the runner's mechanics envelope, result
//! export document and export unavailability. Inputs: I110_INPUTS; output: I110_OUT.
//! Round 3 (H-1): each row also carries `h1`, the count of negative-zero tokens
//! (`-0.0` not followed by a digit or exponent) in the ordinary envelope and in the
//! runner's export document; it is reported, not compared.
//! Round 4 (declared text changes): I110_TEXTS names [old, new] string pairs. Each row
//! carries `texts`: per output, the count of each old and new string, and the SHA-256
//! of the output with every new string replaced by its old one (`norm`), which equals
//! B's SHA exactly when the output differs from B only in the declared strings.
use open_pipe_stress_headless_runner::{
    run_preview_model_value_with_mode, PrivacyContext, ProfessionalBoundary, Provenance,
    RedistributionStatus, Reference, RunnerOperation, RunnerRequest, TbdDecisions,
};
use open_pipe_stress_product_physics::{
    run_linear_static_preview_value_with_mode, run_linear_static_preview_value_with_retained_direct,
    PreviewSolverMode, RetainedPublication,
};
use serde_json::{json, Value};
use sha2::{Digest, Sha256};

fn sha(bytes: &[u8]) -> String {
    format!("{:x}", Sha256::digest(bytes))
}
fn neg_zero_tokens(bytes: &[u8]) -> usize {
    let pattern = b"-0.0";
    (0..bytes.len().saturating_sub(pattern.len() - 1))
        .filter(|&i| &bytes[i..i + pattern.len()] == pattern)
        .filter(|&i| bytes.get(i + pattern.len()).map_or(true, |c| !c.is_ascii_digit() && *c != b'e' && *c != b'E'))
        .count()
}
fn text_pairs() -> Vec<(String, String)> {
    std::env::var("I110_TEXTS").ok().map(|t| serde_json::from_str(&t).unwrap()).unwrap_or_default()
}
fn count(hay: &[u8], needle: &[u8]) -> usize {
    if needle.is_empty() || hay.len() < needle.len() { return 0; }
    (0..=hay.len() - needle.len()).filter(|&i| &hay[i..i + needle.len()] == needle).count()
}
fn text_report(bytes: &[u8], pairs: &[(String, String)]) -> Value {
    let mut norm = bytes.to_vec();
    let mut counts = Vec::new();
    for (old, new) in pairs {
        counts.push(json!([count(bytes, old.as_bytes()), count(bytes, new.as_bytes())]));
        if !new.is_empty() && new != old {
            let mut out = Vec::with_capacity(norm.len());
            let mut i = 0;
            while i < norm.len() {
                if norm[i..].starts_with(new.as_bytes()) { out.extend_from_slice(old.as_bytes()); i += new.len(); } else { out.push(norm[i]); i += 1; }
            }
            norm = out;
        }
    }
    json!({"counts": counts, "norm": sha(&norm)})
}
fn request(model: &Value) -> RunnerRequest {
    let id = model["project"]["id"].as_str().unwrap_or("project:none");
    RunnerRequest {
        request_id: "i110-bytes".into(),
        operation: RunnerOperation::Solve,
        operation_ref: Reference::new("api_operation", "ops.solve.job"),
        project_ref: Reference::new("project", id),
        model_ref: Reference::new("model", id),
        unit_system_ref: Reference::new("unit_system", "invented-si"),
        load_basis_refs: model["load_cases"].as_array().map(|cases| cases.iter()
            .map(|c| Reference::new("load_case", c["id"].as_str().unwrap_or("")))
            .collect()).unwrap_or_default(),
        input_manifest_ref: Reference::new("audit_manifest", "i110-input-manifest"),
        requested_outputs: vec!["result_envelope".into(), "audit_manifest".into(), "diagnostics".into()],
        privacy: PrivacyContext::local_first_public_metadata(),
        provenance: Provenance {
            source_name: "I110 byte-equality harness".into(),
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
fn i110_bytes() {
    let Ok(inputs) = std::env::var("I110_INPUTS") else { return };
    let out = std::env::var("I110_OUT").unwrap();
    let items: Vec<Value> = serde_json::from_slice(&std::fs::read(inputs).unwrap()).unwrap();
    use std::io::Write;
    let mut file = std::fs::OpenOptions::new().create(true).truncate(true).write(true).open(&out).unwrap();
    // I110_SETS: the sets this pass runs; I110_RETAINED=1: also run the retained direct
    // entry (W1) for B1 (the registered profile is the debug build only).
    let sets = std::env::var("I110_SETS").unwrap_or_else(|_| "E,F,B1".into());
    let retained_pass = std::env::var("I110_RETAINED").as_deref() == Ok("1");
    let pairs = text_pairs();
    for (index, item) in items.iter().enumerate() {
        if !sets.split(',').any(|s| item["set"] == s) {
            continue;
        }
        let started = std::time::Instant::now();
        for (mode_name, mode) in [("sparse_interactive", PreviewSolverMode::SparseInteractive), ("dense_scrutiny", PreviewSolverMode::DenseScrutiny)] {
            let payload = item["payload"].clone();
            let mut h1 = json!({});
            let mut texts = json!({});
            let ordinary = match run_linear_static_preview_value_with_mode(payload.clone(), mode) {
                Ok(envelope) => {
                    let bytes = serde_json::to_vec(&envelope).unwrap();
                    h1["ordinary"] = json!(neg_zero_tokens(&bytes));
                    texts["ordinary"] = text_report(&bytes, &pairs);
                    json!({"sha": sha(&bytes), "status": envelope.status.mechanics})
                }
                Err(error) => json!({"error": sha(error.as_bytes())}),
            };
            // W1 through the retained direct entry for B1's corpus (the other sets are
            // outside D1 or carry no retained work; they take the ordinary and runner entries).
            let retained = if !retained_pass || item["set"] != "B1" { json!({"kind": "not_run"}) } else { match run_linear_static_preview_value_with_retained_direct(payload.clone(), mode) {
                Ok(output) => match output.into_publication() {
                    RetainedPublication::Ordinary(envelope) => { let b = serde_json::to_vec(&envelope).unwrap(); texts["retained"] = text_report(&b, &pairs); json!({"kind": "ordinary", "sha": sha(&b)}) },
                    RetainedPublication::Successor(doc) => { let b = serde_json::to_vec(&doc).unwrap(); texts["retained"] = text_report(&b, &pairs); json!({"kind": "successor", "sha": sha(&b)}) },
                },
                Err(error) => json!({"error": sha(error.as_bytes())}),
            } };
            let runner = match run_preview_model_value_with_mode(request(&payload["model"]), payload.clone(), mode) {
                Ok(output) => json!({
                    "mechanics": output.mechanics_envelope.as_ref().map(|m| { let b = serde_json::to_vec(m).unwrap(); texts["mechanics"] = text_report(&b, &pairs); sha(&b) }),
                    "document": output.result_envelope_document.as_ref().map(|d| {
                        let bytes = serde_json::to_vec(d).unwrap();
                        h1["document"] = json!(neg_zero_tokens(&bytes));
                        texts["document"] = text_report(&bytes, &pairs);
                        sha(&bytes)
                    }),
                    "unavailability": output.canonical_export_unavailability,
                }),
                Err(error) => json!({"error": sha(error.as_bytes())}),
            };
            writeln!(file, "{}", serde_json::to_string(&json!({"set": item["set"], "label": item["label"], "mode": mode_name,
                "ordinary": ordinary, "retained": retained, "runner": runner, "h1": h1, "texts": texts})).unwrap()).unwrap();
            file.flush().unwrap();
        }
        eprintln!("i110 {index}/{} {:.1}s {}", items.len(), started.elapsed().as_secs_f64(), item["label"]);
    }
}
