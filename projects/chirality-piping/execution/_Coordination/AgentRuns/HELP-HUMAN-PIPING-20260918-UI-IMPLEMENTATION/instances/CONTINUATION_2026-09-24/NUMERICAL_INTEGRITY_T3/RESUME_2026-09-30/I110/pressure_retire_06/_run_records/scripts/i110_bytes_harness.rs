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
//! Round 6 (ROOT's extended check for T2): each output's `texts` entry also carries
//! `norm_receipt`: the SHA-256 of `norm` after every source-block receipt in it (any object
//! with a `source_block_recovery` member carrying `body.publication_sha256` and
//! `receipt_sha256`) has its two digests recomputed from the normalized content with the
//! product's digest rule (PP `source_receipt::hash`: SHA-256 of the RFC 8785 text of
//! {"domain": d, "payload": p}; publication = the object without `source_block_recovery`,
//! domain `source_blocks_publication_v1`; receipt = `body` with that publication digest,
//! domain `source_blocks_receipt_v1`) and substituted in place; `receipts`: the number of such
//! receipts; and `rule_holds`: whether the rule reproduces the output's own digests.
//! `norm_receipt` equals B's SHA exactly when the output differs from B only in the
//! declared strings and in those recomputed digests. I110_DUMP_DIR with I110_DUMP_MATCH (a
//! label substring): write each matching output's bytes there (probe only).
//! Documents (probe extension beyond ROOT's two receipt digests, reported separately):
//! the runner's result export document embeds the source's receipt and also binds the source
//! by two product hashes, the source checksum (`raw_source_hashes`, `run_hashes` and both
//! `source_origin_bindings` checksums: result_export `derivative::digest` of the mechanics
//! envelope) and `derivative_hash` (`digest` of the document without it). `doc_ext` carries
//! `norm_document`: the SHA-256 of the document's `norm` with the receipt digests, the source
//! checksum and the derivative hash each recomputed by those rules from the normalized
//! content; and `rules_hold`: whether those rules reproduce the output's own values.
use open_pipe_stress_canonical_json::canonical_json_checked_v1_text;
use open_pipe_stress_result_export::derivative::digest as export_digest;
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
fn domain_hash(domain: &str, payload: &Value) -> String {
    let text = serde_json::to_string(&json!({"domain": domain, "payload": payload})).unwrap();
    sha(canonical_json_checked_v1_text(&text).unwrap().as_bytes())
}
/// Every source-block receipt in `value`: (old publication, new publication, old receipt, new receipt).
fn receipts(value: &Value, found: &mut Vec<(String, String, String, String)>) {
    match value {
        Value::Object(map) => {
            if let Some(recovery) = map.get("source_block_recovery") {
                if let (Some(p), Some(r)) = (recovery["body"]["publication_sha256"].as_str(), recovery["receipt_sha256"].as_str()) {
                    let mut publication = value.clone();
                    publication.as_object_mut().unwrap().remove("source_block_recovery");
                    let new_p = domain_hash("source_blocks_publication_v1", &publication);
                    let mut body = recovery["body"].clone();
                    body["publication_sha256"] = json!(new_p);
                    let new_r = domain_hash("source_blocks_receipt_v1", &body);
                    found.push((p.to_string(), new_p, r.to_string(), new_r));
                }
            }
            for v in map.values() { receipts(v, found); }
        }
        Value::Array(items) => for v in items { receipts(v, found); },
        _ => {}
    }
}
fn replace_all(hay: &[u8], old: &[u8], new: &[u8]) -> Vec<u8> {
    let mut out = Vec::with_capacity(hay.len());
    let mut i = 0;
    while i < hay.len() {
        if !old.is_empty() && hay[i..].starts_with(old) { out.extend_from_slice(new); i += old.len(); } else { out.push(hay[i]); i += 1; }
    }
    out
}
fn text_report(bytes: &[u8], pairs: &[(String, String)]) -> Value {
    let mut norm = bytes.to_vec();
    let mut counts = Vec::new();
    for (old, new) in pairs {
        counts.push(json!([count(bytes, old.as_bytes()), count(bytes, new.as_bytes())]));
        if !new.is_empty() && new != old {
            norm = replace_all(&norm, new.as_bytes(), old.as_bytes());
        }
    }
    let mut report = json!({"counts": counts, "norm": sha(&norm)});
    if let (Ok(original), Ok(normalized)) = (serde_json::from_slice::<Value>(bytes), serde_json::from_slice::<Value>(&norm)) {
        let (mut own, mut found) = (Vec::new(), Vec::new());
        receipts(&original, &mut own);
        receipts(&normalized, &mut found);
        if !found.is_empty() {
            let mut fixed = norm.clone();
            for (old_p, new_p, old_r, new_r) in &found {
                fixed = replace_all(&fixed, format!("\"{old_p}\"").as_bytes(), format!("\"{new_p}\"").as_bytes());
                fixed = replace_all(&fixed, format!("\"{old_r}\"").as_bytes(), format!("\"{new_r}\"").as_bytes());
            }
            report["norm_receipt"] = json!(sha(&fixed));
            report["receipts"] = json!(found.len());
            report["rule_holds"] = json!(own.iter().all(|(p, np, r, nr)| p == np && r == nr));
        }
    }
    report
}
fn normalize(bytes: &[u8], pairs: &[(String, String)]) -> Vec<u8> {
    let mut norm = bytes.to_vec();
    for (old, new) in pairs {
        if !new.is_empty() && new != old { norm = replace_all(&norm, new.as_bytes(), old.as_bytes()); }
    }
    norm
}
fn quoted(hex: &str) -> Vec<u8> { format!("\"{hex}\"").into_bytes() }
/// The document's extended check (see the header): None when the document carries no receipt.
fn doc_ext(mechanics: &[u8], document: &[u8], pairs: &[(String, String)]) -> Option<Value> {
    let (norm_m, norm_d) = (normalize(mechanics, pairs), normalize(document, pairs));
    let mech_c: Value = serde_json::from_slice(mechanics).ok()?;
    let doc_c: Value = serde_json::from_slice(document).ok()?;
    let mut found = Vec::new();
    receipts(&serde_json::from_slice(&norm_m).ok()?, &mut found);
    if found.is_empty() { return None; }
    let (mut fixed_m, mut fixed_d) = (norm_m, norm_d);
    for (old_p, new_p, old_r, new_r) in &found {
        for (o, n) in [(old_p, new_p), (old_r, new_r)] {
            fixed_m = replace_all(&fixed_m, &quoted(o), &quoted(n));
            fixed_d = replace_all(&fixed_d, &quoted(o), &quoted(n));
        }
    }
    let (old_src, new_src) = (export_digest(&mech_c).ok()?, export_digest(&serde_json::from_slice(&fixed_m).ok()?).ok()?);
    let reproducibility = &doc_c["result_envelope"]["reproducibility"];
    let src_rule = reproducibility["raw_source_hashes"][0]["value"] == json!(old_src);
    let mut doc_c_wo = doc_c.clone();
    doc_c_wo["result_envelope"]["reproducibility"].as_object_mut()?.remove("derivative_hash");
    let der_rule = reproducibility["derivative_hash"]["value"] == json!(export_digest(&doc_c_wo).ok()?);
    let src_count = count(&fixed_d, &quoted(&old_src));
    fixed_d = replace_all(&fixed_d, &quoted(&old_src), &quoted(&new_src));
    let mut dd: Value = serde_json::from_slice(&fixed_d).ok()?;
    let old_der = dd["result_envelope"]["reproducibility"]["derivative_hash"]["value"].as_str()?.to_string();
    dd["result_envelope"]["reproducibility"].as_object_mut()?.remove("derivative_hash");
    let new_der = export_digest(&dd).ok()?;
    fixed_d = replace_all(&fixed_d, &quoted(&old_der), &quoted(&new_der));
    Some(json!({"norm_document": sha(&fixed_d), "rules_hold": src_rule && der_rule, "source_checksum_occurrences": src_count, "receipts": found.len()}))
}
fn dump(label: &Value, mode: &str, name: &str, bytes: &[u8]) {
    if let (Ok(dir), Ok(pattern)) = (std::env::var("I110_DUMP_DIR"), std::env::var("I110_DUMP_MATCH")) {
        let label = label.as_str().unwrap_or("");
        if label.contains(&pattern) {
            let safe: String = label.chars().map(|c| if c.is_ascii_alphanumeric() || c == '-' || c == '_' || c == '.' { c } else { '_' }).collect();
            std::fs::write(format!("{dir}/{safe}__{mode}__{name}.json"), bytes).unwrap();
        }
    }
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
                    texts["ordinary"] = text_report(&bytes, &pairs); dump(&item["label"], mode_name, "ordinary", &bytes);
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
                Ok(output) => {
                    if let (Some(m), Some(d)) = (output.mechanics_envelope.as_ref(), output.result_envelope_document.as_ref()) {
                        if let Some(ext) = doc_ext(&serde_json::to_vec(m).unwrap(), &serde_json::to_vec(d).unwrap(), &pairs) { texts["doc_ext"] = ext; }
                    }
                    json!({
                    "mechanics": output.mechanics_envelope.as_ref().map(|m| { let b = serde_json::to_vec(m).unwrap(); texts["mechanics"] = text_report(&b, &pairs); dump(&item["label"], mode_name, "mechanics", &b); sha(&b) }),
                    "document": output.result_envelope_document.as_ref().map(|d| {
                        let bytes = serde_json::to_vec(d).unwrap();
                        h1["document"] = json!(neg_zero_tokens(&bytes));
                        texts["document"] = text_report(&bytes, &pairs); dump(&item["label"], mode_name, "document", &bytes);
                        sha(&bytes)
                    }),
                    "unavailability": output.canonical_export_unavailability,
                })},
                Err(error) => json!({"error": sha(error.as_bytes())}),
            };
            writeln!(file, "{}", serde_json::to_string(&json!({"set": item["set"], "label": item["label"], "mode": mode_name,
                "ordinary": ordinary, "retained": retained, "runner": runner, "h1": h1, "texts": texts})).unwrap()).unwrap();
            file.flush().unwrap();
        }
        eprintln!("i110 {index}/{} {:.1}s {}", items.len(), started.elapsed().as_secs_f64(), item["label"]);
    }
}
