//! I101 scratch harness (never committed): the RS reader's three readings of I100's addendum-01 shapes.
//! ADD1_INPUTS names I100's input lines ({name, base, source, invocation}); ADD1_OUT receives one line per shape.
use open_pipe_stress_result_export::retained_precision as rp;
use serde_json::{json, Value};
use std::io::Write;
#[test]
fn i101_add1_readings() {
    let one = |r: Result<rp::Validation, rp::ValidationError>| match r {
        Ok(v) => json!({"ok": {"eligible": v.numerical_eligible}}),
        Err(e) => json!({"gate": e.gate, "code": e.code}),
    };
    let text = std::fs::read_to_string(std::env::var("ADD1_INPUTS").unwrap()).unwrap();
    let mut out = std::fs::File::create(std::env::var("ADD1_OUT").unwrap()).unwrap();
    let mut n = 0;
    for line in text.lines().filter(|l| !l.trim().is_empty()) {
        let d: Value = serde_json::from_str(line).unwrap();
        let (s, inv) = (&d["source"], &d["invocation"]);
        let row = json!({"name": d["name"], "base": d["base"], "bound": one(rp::validate(s, Some(inv))), "unbound": one(rp::validate(s, None)),
            "transport": one(rp::validate_transport_metadata(s))});
        writeln!(out, "{}", serde_json::to_string(&row).unwrap()).unwrap();
        n += 1;
    }
    assert_eq!(n, 52);
}
