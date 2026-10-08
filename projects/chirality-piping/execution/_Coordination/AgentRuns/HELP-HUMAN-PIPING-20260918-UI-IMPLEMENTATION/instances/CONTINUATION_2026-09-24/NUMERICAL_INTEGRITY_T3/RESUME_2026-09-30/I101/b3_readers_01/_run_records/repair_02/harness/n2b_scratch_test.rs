// I101 repair 02, scratch only (appended to RE tests/retained_precision_contract.rs in the b2-r working tree for one run,
// then removed; never committed): RS's physics-1 base validator on the bound and unbound path, two faults in two
// exact_cases entries of the exact two_case_synthetic, read 64 times in one process.
#[test]
fn i101_scratch_bound_path_order() {
    use serde_json::json;
    let shared = corpus();
    let shape = ExactShape { name: "scratch", base: "two_case_synthetic", edits: vec![
        set(json!(["contract_evidence", "exact_cases", 0, "profile_mode"]), json!("x")),
        set(json!(["contract_evidence", "exact_cases", 1, "material_basis"]), json!(0)),
    ], invocation_edits: vec![], after: vec![] };
    let (source, invocation) = b3b_input(&shared, &shape);
    let mut seen = std::collections::BTreeSet::new();
    for _ in 0..64 { seen.insert(readings(&source, &invocation).to_string()); }
    println!("I101_SCRATCH {}", seen.len());
    for s in &seen { println!("I101_SCRATCH {s}"); }
}
