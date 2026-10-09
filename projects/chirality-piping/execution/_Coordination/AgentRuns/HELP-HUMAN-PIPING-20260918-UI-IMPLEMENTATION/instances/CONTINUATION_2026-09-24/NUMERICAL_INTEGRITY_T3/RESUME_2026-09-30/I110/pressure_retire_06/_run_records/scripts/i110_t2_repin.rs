//! I110 round 6 probe (never committed): T2 re-pin of the source-block carriers under ROOT's
//! extended mechanical check.
//!   (i)   take the committed bytes and replace only the declared string;
//!   (ii)  recompute `publication_sha256` and `receipt_sha256` from the edited content with the
//!         product's own digest rule (PP `source_receipt::hash`: SHA-256 of the RFC 8785 text of
//!         {"domain": d, "payload": p}; publication = the envelope without `source_block_recovery`,
//!         domain `source_blocks_publication_v1`; receipt = `body`, domain `source_blocks_receipt_v1`),
//!         substituting each digest in place;
//!   (iii) the result must equal the head's own output byte for byte (same serialization as the
//!         committed file: struct order or sorted keys, two-space pretty, no trailing newline).
//! Env: I110_ROOT (the project root P), I110_OUT (output dir), I110_MODE = "baseline" (the head
//! without T2: check the rule on the committed digests and that the head reproduces each file) or
//! "repin" (the head with T2: (i)-(iii), and write each re-pinned file). I110_PIN_OLD/I110_PIN_NEW:
//! the compact envelopes of the Rust pin's request before and after T2 (both modes).
use open_pipe_stress_canonical_json::canonical_json_checked_v1_text;
use open_pipe_stress_product_physics::{run_linear_static_preview_value_with_mode, PreviewSolverMode};
use serde_json::{json, Value};
use sha2::{Digest, Sha256};

const OLD: &str = "Pressure thrust and pressure stress retain the existing preview formulation and capability qualifications; pressure formulation qualification remains open.";
const NEW: &str = "Pressure is not solved on this profile: legacy pressure inputs are refused, and pressure is solved only on the exact straight-pressure profile, under that profile's own qualifications.";

fn hex(bytes: &[u8]) -> String {
    format!("{:x}", Sha256::digest(bytes))
}
fn hash(domain: &str, payload: &Value) -> String {
    let text = serde_json::to_string(&json!({"domain": domain, "payload": payload})).unwrap();
    hex(canonical_json_checked_v1_text(&text).unwrap().as_bytes())
}
/// The product's two receipt digests of a source-block document.
fn digests(doc: &Value) -> (String, String) {
    let mut publication = doc.clone();
    publication.as_object_mut().unwrap().remove("source_block_recovery");
    let publication_sha = hash("source_blocks_publication_v1", &publication);
    let mut body = doc["source_block_recovery"]["body"].clone();
    body["publication_sha256"] = json!(publication_sha);
    (publication_sha, hash("source_blocks_receipt_v1", &body))
}
fn replace_once(text: &str, old: &str, new: &str, what: &str) -> String {
    assert_eq!(text.matches(old).count(), 1, "{what}: exactly one occurrence");
    text.replacen(old, new, 1)
}
/// (i) and (ii): the committed text, edited.
fn edit(old_text: &str) -> String {
    let old_doc: Value = serde_json::from_str(old_text).unwrap();
    let old_pub = old_doc["source_block_recovery"]["body"]["publication_sha256"].as_str().unwrap().to_string();
    let old_rec = old_doc["source_block_recovery"]["receipt_sha256"].as_str().unwrap().to_string();
    let text = replace_once(old_text, OLD, NEW, "declared string");
    let doc: Value = serde_json::from_str(&text).unwrap();
    let (new_pub, new_rec) = digests(&doc);
    let text = replace_once(&text, &old_pub, &new_pub, "publication_sha256");
    replace_once(&text, &old_rec, &new_rec, "receipt_sha256")
}
fn struct_order(text: &str) -> bool {
    let doc: Value = serde_json::from_str(text).unwrap();
    // serde_json's Value (no preserve_order) sorts keys; a sorted file starts with the first key.
    !text.starts_with("{\n  \"accepted_model_state_mutated\"") && doc.get("accepted_model_state_mutated").is_some()
}

#[test]
fn i110_t2_repin() {
    let Ok(root) = std::env::var("I110_ROOT") else { return };
    let out = std::env::var("I110_OUT").unwrap();
    let mode_name = std::env::var("I110_MODE").unwrap();
    let mut report = Vec::new();
    let files = [
        "multicase-dense_scrutiny", "multicase-sparse_interactive", "n05-dense_scrutiny",
        "n05-sparse_interactive", "n06-dense_scrutiny", "n06-sparse_interactive",
    ];
    for dir in ["", "ui/"] {
        for name in files {
            let rel = format!("fixtures/product_preview/source_blocks/{dir}{name}");
            let committed = std::fs::read_to_string(format!("{root}/{rel}.raw.json")).unwrap();
            let request: Value = serde_json::from_str(&std::fs::read_to_string(format!("{root}/{rel}.request.json")).unwrap()).unwrap();
            let mode = if name.ends_with("dense_scrutiny") { PreviewSolverMode::DenseScrutiny } else { PreviewSolverMode::SparseInteractive };
            let envelope = run_linear_static_preview_value_with_mode(request, mode).unwrap();
            let sorted = !struct_order(&committed);
            let head = if sorted {
                serde_json::to_string_pretty(&serde_json::to_value(&envelope).unwrap()).unwrap()
            } else {
                serde_json::to_string_pretty(&envelope).unwrap()
            };
            let committed_doc: Value = serde_json::from_str(&committed).unwrap();
            let (p, r) = digests(&committed_doc);
            let rule_holds = p == committed_doc["source_block_recovery"]["body"]["publication_sha256"]
                && r == committed_doc["source_block_recovery"]["receipt_sha256"];
            if mode_name == "baseline" {
                report.push(json!({"file": format!("P/{rel}.raw.json"), "serialization": if sorted {"sorted keys"} else {"struct order"},
                    "rule_reproduces_committed_digests": rule_holds, "head_reproduces_committed_bytes": head == committed,
                    "committed_sha256": hex(committed.as_bytes())}));
            } else {
                let edited = edit(&committed);
                let equal = edited == head;
                std::fs::write(format!("{out}/{}{name}.raw.json", dir.replace('/', "__")), &edited).unwrap();
                let edited_doc: Value = serde_json::from_str(&edited).unwrap();
                report.push(json!({"file": format!("P/{rel}.raw.json"), "serialization": if sorted {"sorted keys"} else {"struct order"},
                    "rule_reproduces_committed_digests": rule_holds,
                    "old_sha256": hex(committed.as_bytes()), "new_sha256": hex(edited.as_bytes()),
                    "old_publication_sha256": committed_doc["source_block_recovery"]["body"]["publication_sha256"],
                    "new_publication_sha256": edited_doc["source_block_recovery"]["body"]["publication_sha256"],
                    "old_receipt_sha256": committed_doc["source_block_recovery"]["receipt_sha256"],
                    "new_receipt_sha256": edited_doc["source_block_recovery"]["receipt_sha256"],
                    "edited_equals_head_output_bytes": equal}));
                assert!(equal, "(iii) failed for {rel}");
            }
        }
    }
    // The Rust pin: compact envelopes from PP's test (to_vec of the struct), before and after T2.
    if let (Ok(old_dir), Ok(new_dir)) = (std::env::var("I110_PIN_OLD"), std::env::var("I110_PIN_NEW")) {
        for m in ["SparseInteractive", "DenseScrutiny"] {
            let old = std::fs::read_to_string(format!("{old_dir}/{m}.json")).unwrap();
            let new = std::fs::read_to_string(format!("{new_dir}/{m}.json")).unwrap();
            let old_doc: Value = serde_json::from_str(&old).unwrap();
            let (p, r) = digests(&old_doc);
            let rule_holds = p == old_doc["source_block_recovery"]["body"]["publication_sha256"] && r == old_doc["source_block_recovery"]["receipt_sha256"];
            let edited = edit(&old);
            report.push(json!({"pin": format!("PP/tests/f1b_w2_runtime.rs f1b_w2_exact_block_selection_of_a_range_triggered_case_publishes_mains_bytes {m}"),
                "rule_reproduces_committed_digests": rule_holds, "old_sha256": hex(old.as_bytes()), "edited_sha256": hex(edited.as_bytes()),
                "head_sha256": hex(new.as_bytes()), "edited_equals_head_output_bytes": edited == new}));
            assert_eq!(edited, new, "(iii) failed for the pin, {m}");
        }
    }
    std::fs::write(format!("{out}/report_{mode_name}.json"), serde_json::to_string_pretty(&report).unwrap()).unwrap();
}
