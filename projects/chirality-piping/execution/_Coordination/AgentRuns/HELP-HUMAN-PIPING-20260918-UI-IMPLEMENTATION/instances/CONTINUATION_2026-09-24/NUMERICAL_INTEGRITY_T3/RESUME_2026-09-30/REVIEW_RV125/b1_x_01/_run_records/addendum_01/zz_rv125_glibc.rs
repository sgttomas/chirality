//! RV125 ADDENDUM_01 (RV-X of PR-B1; disposable archive copy only, never committed): checks of the
//! platform test repair (`d07006c2f0` → `7f5f72912e`) on macOS.
//! 1. `CAP_MAXIMAL_RING`, read from both test sources: the two tables are equal, and each entry is
//!    bit-for-bit this platform's `10·cos t`, `10·sin t` (so the macOS input is unchanged).
//! 2. The glibc variants are exactly a one-ulp change of one value: applying it to the macOS
//!    successor and recomputing the two hashes (C1 §3, the wire's own `domain_hash`) must give the
//!    repair's glibc hashes, for W-C2's dense document and for (C, B, A)'s dense pin.
//! 3. (A, A2)'s dense successor (never observed on glibc): its macOS pin, whether it carries the
//!    differing value, and whether its cases' rows equal W-C2's case A row for row.
use super::*;
use serde_json::{json, Value};
use sha2::{Digest, Sha256};
use std::path::Path;

fn sha(bytes: &[u8]) -> String { format!("{:x}", Sha256::digest(bytes)) }

fn ring_from(source: &str) -> Vec<(u64, u64)> {
    let start = source.find("const CAP_MAXIMAL_RING: [(u64, u64); 32] = [").expect("ring table");
    let body = &source[start..start + source[start..].find("];").unwrap()];
    let hex: Vec<u64> = body.split("0x").skip(1).map(|h| u64::from_str_radix(&h[..16], 16).unwrap()).collect();
    assert_eq!(hex.len(), 64);
    hex.chunks(2).map(|p| (p[0], p[1])).collect()
}

fn fixture_text(mode: PreviewSolverMode) -> String {
    let path = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join(format!("../../fixtures/results/retained_precision_w_c2_successor_{}.json", mode.as_str()));
    std::fs::read_to_string(path).unwrap()
}

/// The successor's two hashes recomputed from its envelope and body (C1 §3, `retained_wire::finish`).
fn rehash(successor: &Value) -> (String, String, Value) {
    let mut env = successor.clone();
    let mut rp = env.as_object_mut().unwrap().remove("retained_precision").unwrap();
    let publication = retained_wire::domain_hash("retained_precision_publication_mp_v2", &env).unwrap();
    rp["body"]["publication_sha256"] = json!(publication);
    let receipt = retained_wire::domain_hash("retained_precision_receipt_mp_v2", &rp["body"]).unwrap();
    rp["receipt_sha256"] = json!(receipt);
    env.as_object_mut().unwrap().insert("retained_precision".into(), rp);
    (publication, receipt, env)
}

/// Every place in `v` holding the number `x` (by bits), as JSON pointers.
fn places(v: &Value, x: f64, at: String, out: &mut Vec<String>) {
    match v {
        Value::Number(n) if n.as_f64().is_some_and(|y| y.to_bits() == x.to_bits()) => out.push(at),
        Value::Array(a) => a.iter().enumerate().for_each(|(i, e)| places(e, x, format!("{at}/{i}"), out)),
        Value::Object(o) => o.iter().for_each(|(k, e)| places(e, x, format!("{at}/{k}"), out)),
        _ => {}
    }
}

fn direct_successor(raw: &Value, mode: PreviewSolverMode) -> Value {
    let output = run_linear_static_preview_value_with_retained_direct(raw.clone(), mode).unwrap();
    output.successor().cloned().expect("registered: a successor")
}

fn case_rows(doc: &Value, case: &str) -> Vec<String> {
    let mut rows: Vec<String> = doc["results"].as_array().unwrap().iter().filter(|r| r["basis_ref"]["ref_id"] == case)
        .map(|r| format!("{}|{}|{:016x}", r["kind"].as_str().unwrap(), r["entity_ref"].as_str().unwrap_or(""), r["value"].as_f64().unwrap().to_bits()))
        .collect();
    rows.sort();
    rows
}

const MACOS: f64 = 1.6258317075882521e-12;
const GLIBC_VALUE: f64 = 1.6258317075882523e-12;

#[test]
#[ignore]
fn zz_rv125_glibc() {
    let out = std::env::var("RV125_GLIBC_OUT").expect("RV125_GLIBC_OUT");
    let mut rows = Vec::new();
    // 1. The ring.
    let law = ring_from(include_str!("retained_memory_law_tests.rs"));
    let common = ring_from(include_str!("../tests/common/b1_sq_inputs.rs"));
    assert_eq!(law, common, "the two CAP_MAXIMAL_RING tables");
    let mut exact = 0;
    let mut worst_absolute_clause_ulps = 0u64;
    for (i, &(x, y)) in law.iter().enumerate() {
        let t = 2.0 * std::f64::consts::PI * i as f64 / 32.0;
        let (cx, cy) = (10.0 * t.cos(), 10.0 * t.sin());
        exact += usize::from(cx.to_bits() == x) + usize::from(cy.to_bits() == y);
        // What the repair's check would admit: ≤ 1 ulp, or |Δ| ≤ 1e-14 (in ulps of each coordinate).
        for v in [f64::from_bits(x), f64::from_bits(y)] {
            if v.abs() >= 1.0 {
                let ulp = v.abs().next_up() - v.abs();
                worst_absolute_clause_ulps = worst_absolute_clause_ulps.max((1e-14 / ulp) as u64);
            }
        }
    }
    rows.push(json!({"check": "ring", "tables_equal": true, "coordinates_bit_exact_on_this_platform": exact, "of": 64,
        "absolute_clause_admits_up_to_ulps": worst_absolute_clause_ulps}));
    assert_eq!(exact, 64, "the macOS ring is libSystem's cos and sin bit for bit");
    assert_eq!(GLIBC_VALUE.to_bits(), MACOS.to_bits() + 1, "one ulp");
    // 2a. W-C2's dense document: the repair's three replacements against a recomputation.
    let mode = PreviewSolverMode::DenseScrutiny;
    let text = fixture_text(mode);
    let doc: Value = serde_json::from_str(&text).unwrap();
    let macos = doc["source"].clone();
    let (p0, r0, _) = rehash(&macos);
    assert_eq!((p0.as_str(), r0.as_str()), (macos["retained_precision"]["body"]["publication_sha256"].as_str().unwrap(),
        macos["retained_precision"]["receipt_sha256"].as_str().unwrap()), "control: the macOS fixture rehashes to itself");
    let mut at = Vec::new();
    places(&macos, MACOS, String::new(), &mut at);
    let mut glibc = macos.clone();
    for p in &at { *glibc.pointer_mut(p).unwrap() = json!(GLIBC_VALUE); }
    let (p1, r1, glibc) = rehash(&glibc);
    let replaced = [("\"value\": 1.6258317075882521e-12", "\"value\": 1.6258317075882523e-12"),
        ("\"publication_sha256\": \"57624d75437e678852dfc7657a19d31ee133340435e9d5ce3a31b295cbebc718\"", "\"publication_sha256\": \"35fa7acae6fbd731ff50b611aec588e673f32978af80a9bb89a7c27f66e88fd7\""),
        ("\"receipt_sha256\": \"612e23ca4b90604b3d2351fd7465d2e3cefb0f3fbb36bdea39efaa82a68bc07a\"", "\"receipt_sha256\": \"ca6a62a6187a08d7b2e2643911fd232b02076b9032be1455754ff780540995f2\"")];
    let repaired_text = replaced.iter().fold(text.clone(), |t, (a, b)| { assert_eq!(t.matches(a).count(), 1); t.replacen(a, b, 1) });
    let repaired: Value = serde_json::from_str(&repaired_text).unwrap();
    let w_c2_ok = (p1.as_str(), r1.as_str()) == ("35fa7acae6fbd731ff50b611aec588e673f32978af80a9bb89a7c27f66e88fd7", "ca6a62a6187a08d7b2e2643911fd232b02076b9032be1455754ff780540995f2")
        && repaired["source"] == glibc;
    let sparse: Value = serde_json::from_str(&fixture_text(PreviewSolverMode::SparseInteractive)).unwrap();
    let mut sparse_at = Vec::new();
    places(&sparse["source"], MACOS, String::new(), &mut sparse_at);
    rows.push(json!({"check": "w_c2_sparse_value_places", "places": sparse_at}));
    rows.push(json!({"check": "w_c2_dense_glibc", "value_places": at, "recomputed_publication": p1, "recomputed_receipt": r1,
        "equals_repair_variant": w_c2_ok, "glibc_published_bytes_sha": sha(&serde_json::to_vec(&glibc).unwrap())}));
    assert!(w_c2_ok, "W-C2: the glibc variant is exactly the one-ulp value with its two hashes");
    // 2b. (C, B, A)'s dense pin.
    let raw = doc["invocation"]["request"].clone();
    let order = |ids: &[&str]| { let mut r = raw.clone(); let all = r["model"]["load_cases"].as_array().unwrap().clone();
        r["model"]["load_cases"] = Value::Array(ids.iter().map(|id| all.iter().find(|c| c["id"] == *id).unwrap().clone()).collect()); r };
    let cba = direct_successor(&order(&["case-c", "case-b", "case-a"]), mode);
    let cba_macos = (cba["retained_precision"]["receipt_sha256"].as_str().unwrap().to_owned(), sha(&serde_json::to_vec(&cba).unwrap()));
    assert_eq!((cba_macos.0.as_str(), cba_macos.1.as_str()), ("7aeecbac57426a2104c3b9f958862daf3e9b2c0f00582599c0210121681db6a1", "c719bd8d3281d3bd3c0a731e8ba5ede8901938d10634db8078c6f6fa96d0b6d8"), "CBA's macOS pin");
    let mut at = Vec::new();
    places(&cba, MACOS, String::new(), &mut at);
    let mut g = cba.clone();
    for p in &at { *g.pointer_mut(p).unwrap() = json!(GLIBC_VALUE); }
    let (_, rg, g) = rehash(&g);
    let cba_glibc = (rg, sha(&serde_json::to_vec(&g).unwrap()));
    let cba_ok = (cba_glibc.0.as_str(), cba_glibc.1.as_str()) == ("255785d20cf0aa9f497ea324d744eb3e946871d5aac863ed8d0081d0521e8c92", "a320a5d33707c1fc8c12a35de624720dddbc35084979522c96ab1906e17c708f");
    rows.push(json!({"check": "cba_dense_glibc", "value_places": at, "recomputed": [cba_glibc.0, cba_glibc.1], "equals_repair_pair": cba_ok}));
    assert!(cba_ok, "CBA: the glibc pair is exactly the one-ulp value with its two hashes");
    // 3. (A, A2) dense.
    let mut a2raw = raw.clone();
    let mut a2 = a2raw["model"]["load_cases"][0].clone();
    a2["id"] = json!("case-a2");
    for load in a2["primitive_loads"].as_array_mut().unwrap() { load["id"] = json!(format!("{}:a2", load["id"].as_str().unwrap())); }
    a2raw["model"]["load_cases"].as_array_mut().unwrap().push(a2);
    let all = a2raw["model"]["load_cases"].as_array().unwrap().clone();
    a2raw["model"]["load_cases"] = Value::Array(["case-a", "case-a2"].iter().map(|id| all.iter().find(|c| c["id"] == *id).unwrap().clone()).collect());
    let aa2 = direct_successor(&a2raw, mode);
    let aa2_macos = (aa2["retained_precision"]["receipt_sha256"].as_str().unwrap().to_owned(), sha(&serde_json::to_vec(&aa2).unwrap()));
    let mut at = Vec::new();
    places(&aa2, MACOS, String::new(), &mut at);
    let wc2_a = case_rows(&macos, "case-a");
    let (aa2_a, aa2_a2) = (case_rows(&aa2, "case-a"), case_rows(&aa2, "case-a2"));
    rows.push(json!({"check": "aa2_dense", "macos_pin": [aa2_macos.0, aa2_macos.1],
        "pin_equals_AA2_PINNED": (aa2_macos.0.as_str(), aa2_macos.1.as_str()) == ("30001ccf42ad12acd9dbb458392fee514946c1a52aa0d4e5f0b20bde5b09ea71", "f4075cdc80eff27099a28f787cec07080b745eca2d598eb3381a84ec03964176"),
        "differing_value_places": at, "case_a_rows_equal_w_c2_case_a": aa2_a == wc2_a, "case_a2_rows_equal_w_c2_case_a": aa2_a2 == wc2_a, "rows": wc2_a.len()}));
    std::fs::write(&out, serde_json::to_string_pretty(&rows).unwrap() + "\n").unwrap();
    println!("RV125_GLIBC_OUT rows={}", rows.len());
}
