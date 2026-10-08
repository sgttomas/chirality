//! I101 scratch harness (never committed): the RS reader's bound verdict with its detail, for input lines whose name
//! contains DETAIL_NAME (DETAIL_INPUTS names the lines). Printed only.
use open_pipe_stress_result_export::retained_precision as rp;
use serde_json::Value;
#[test]
fn i101_detail() {
    let want = std::env::var("DETAIL_NAME").unwrap();
    for line in std::fs::read_to_string(std::env::var("DETAIL_INPUTS").unwrap()).unwrap().lines().filter(|l| !l.trim().is_empty()) {
        let d: Value = serde_json::from_str(line).unwrap();
        if !d["name"].as_str().unwrap().contains(&want) { continue; }
        match rp::validate(&d["source"], Some(&d["invocation"])) {
            Ok(v) => println!("I101_DETAIL {} [{}]: ok eligible={}", d["name"], d["base"], v.numerical_eligible),
            Err(e) => println!("I101_DETAIL {} [{}]: {} {} {:?}", d["name"], d["base"], e.gate, e.code, e.detail),
        }
    }
}
