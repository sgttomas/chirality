# I101 repair 03's mutants (mutate.py spec): each restores a hash map's per-process order in one loop the repair moved
# to array or first-appearance order. A mutant is killed when a test fails by an assertion.
RE = "core/reporting/result_export"
M = [
    ("N2bH", "physics-1 base validator: the cases read in HashMap order again (validate_physics_evidence_in)",
     RE + "/src/physics_evidence.rs",
     '''    for case in array(&evidence["exact_cases"])? {
        let case_id = text(&case["load_case_id"])?;
        require(
            keys(''',
     '''    for (&case_id, &case) in &cases {
        require(
            keys('''),
    ("PSH", "preview validator: the supports read in HashMap order again (validate_preview_physics_evidence)",
     RE + "/src/preview_physics_evidence.rs",
     '''        for support in &support_order {
            let components = &actions[support];
''',
     '''        for components in actions.values() {
'''),
    ("PCH", "preview validator: the combinations read in HashMap order again (validate_preview_physics_evidence)",
     RE + "/src/preview_physics_evidence.rs",
     '''    for combination in &combination_order {
        let members = &combined[combination];
''',
     '''    for members in combined.values() {
'''),
]
RS_TESTS = {
    "control": ["--test", "retained_precision_contract", "--test", "preview_physics_contract"],
    "N2bH": ["--test", "retained_precision_contract", "b3"],
    "PSH": ["--test", "preview_physics_contract"],
    "PCH": ["--test", "preview_physics_contract"],
}
