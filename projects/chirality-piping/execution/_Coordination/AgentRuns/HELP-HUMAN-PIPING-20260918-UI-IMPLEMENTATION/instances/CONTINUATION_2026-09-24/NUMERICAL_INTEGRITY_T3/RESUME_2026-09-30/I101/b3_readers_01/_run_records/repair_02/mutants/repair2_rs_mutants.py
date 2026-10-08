"""I101 repair 02: the RS mutant restoring hash-map order in physics-1's transport check (RV120 N2), on b2-r 7873884fb4."""
PE = "core/reporting/result_export/src/physics_evidence.rs"
M = [
 ("N2H", "transport: the cases read in HashMap order again", PE,
  '''    for case in array(&evidence["exact_cases"])? {
        let cid = text(&case["load_case_id"])?;''',
  '''    for (cid, case) in &cases {
        let cid: &str = cid;'''),
]
