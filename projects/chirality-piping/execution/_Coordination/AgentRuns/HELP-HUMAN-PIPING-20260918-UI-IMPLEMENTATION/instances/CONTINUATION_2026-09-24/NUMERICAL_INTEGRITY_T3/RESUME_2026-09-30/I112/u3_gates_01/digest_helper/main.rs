//! I112 (U3 gates) scratch helper, never committed to the product: the source-block receipt's two digests of
//! each JSON document named on the command line, by the product's rule (PP `source_receipt::hash`: SHA-256 of
//! `canonical_json_checked_v1_text(serde_json::to_string({"domain": d, "payload": p}))`; publication = the
//! document without `source_block_recovery`, domain `source_blocks_publication_v1`; receipt = `body` with its
//! `publication_sha256` set to that value, domain `source_blocks_receipt_v1`), the same rule I110's round-6
//! probe used. Prints one JSON line per file: {file, publication_sha256, receipt_sha256} or {file, error}.
use open_pipe_stress_canonical_json::canonical_json_checked_v1_text;
use serde_json::{json, Value};
use sha2::{Digest, Sha256};

fn hash(domain: &str, payload: &Value) -> Result<String, String> {
    let text = serde_json::to_string(&json!({"domain": domain, "payload": payload})).map_err(|e| e.to_string())?;
    Ok(format!("{:x}", Sha256::digest(canonical_json_checked_v1_text(&text)?.as_bytes())))
}

fn digests(doc: &Value) -> Result<(String, String), String> {
    let mut publication = doc.clone();
    publication.as_object_mut().ok_or("not an object")?.remove("source_block_recovery");
    let p = hash("source_blocks_publication_v1", &publication)?;
    let mut body = doc["source_block_recovery"]["body"].clone();
    if !body.is_object() {
        return Err("no source_block_recovery.body".into());
    }
    body["publication_sha256"] = json!(p);
    Ok((p.clone(), hash("source_blocks_receipt_v1", &body)?))
}

fn main() {
    for path in std::env::args().skip(1) {
        let out = std::fs::read_to_string(&path).map_err(|e| e.to_string())
            .and_then(|t| serde_json::from_str::<Value>(&t).map_err(|e| e.to_string()))
            .and_then(|doc| digests(&doc));
        match out {
            Ok((p, r)) => println!("{}", json!({"file": path, "publication_sha256": p, "receipt_sha256": r})),
            Err(e) => println!("{}", json!({"file": path, "error": e})),
        }
    }
}
