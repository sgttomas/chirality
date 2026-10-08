//! RV120 (B3 review) raw runner for the Rust reader. Not part of any candidate; copied into the reviewer's probe copy only.
//! RV120_IN: JSON lines {name, source, invocation}; RV120_OUT: JSON lines {name, bound, unbound, transport}.
use open_pipe_stress_result_export::retained_precision as rp;
use serde_json::{json, Value};
use std::io::{BufRead, Write};
fn one(r: Result<rp::Validation, rp::ValidationError>) -> Value {
    match r {
        Ok(v) => json!({"ok": {"eligible": v.numerical_eligible, "bound": v.invocation_bound}}),
        Err(e) => json!({"gate": e.gate, "code": e.code, "detail": e.detail}),
    }
}
#[test]
fn rv120_b3_raw() {
    let (Ok(input), Ok(out)) = (std::env::var("RV120_IN"), std::env::var("RV120_OUT")) else { return };
    let mut o = std::fs::File::create(out).unwrap();
    for line in std::io::BufReader::new(std::fs::File::open(input).unwrap()).lines() {
        let line = line.unwrap();
        if line.trim().is_empty() {
            continue;
        }
        let d: Value = serde_json::from_str(&line).unwrap();
        let (s, inv) = (&d["source"], &d["invocation"]);
        let r = json!({"name": d["name"], "bound": one(rp::validate(s, Some(inv))), "unbound": one(rp::validate(s, None)),
            "transport": one(rp::validate_transport_metadata(s))});
        writeln!(o, "{}", serde_json::to_string(&r).unwrap()).unwrap();
    }
}
