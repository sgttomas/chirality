
/// RV123 scratch: an exact successor with an `unavailable` case whose members were prepared
/// (the n-case serializer's unavailable branch): S-1's route H on its preparation, DEF-E's id.
#[test]
fn rv123_exact_unavailable_case_branch_explore() {
    use super::retained_wire as wire;
    use super::retained_receipt::TraceFault as F;
    let mut raw = raw();
    let mut second = raw["model"]["load_cases"][0].clone();
    second["id"] = json!("case-2");
    for load in second["primitive_loads"].as_array_mut().unwrap() {
        load["id"] = json!(format!("{}:2", load["id"].as_str().unwrap()));
    }
    raw["model"]["load_cases"].as_array_mut().unwrap().push(second);
    let raw = exact3(raw);
    for (fname, fault) in [("maxima", F::Maxima), ("values", F::ValuesCompletion)] {
        for mode in MODES {
            hooks::fault_next_candidate(fault);
            let (_, retained, captured) = exact_w1(&raw, mode);
            let left = hooks::armed_names();
            hooks::disarm();
            let Some(successor) = captured else {
                println!("RV123_UNAVAILABLE {fname} {} successor=none w1={:?} armed_left={left:?}", mode.as_str(), retained.as_ref().err());
                continue;
            };
            let body = &successor["retained_precision"]["body"];
            let statuses: Vec<&str> = body["cases"].as_array().unwrap().iter().map(|c| c["status"].as_str().unwrap()).collect();
            let mut prep = Vec::new();
            for source in body["sources"].as_array().unwrap() {
                if source["preparation"].is_null() { prep.push("none".to_owned()); continue; }
                let attempt = &body["product_attempts"][source["preparation"]["attempt_ref"].as_u64().unwrap() as usize];
                let e = source["preparation"]["sha256"] == json!(preparation_hash(attempt, wire::EXACT_DEFINITION_SHA256));
                let o = source["preparation"]["sha256"] == json!(preparation_hash(attempt, wire::DEFINITION_SHA256));
                prep.push(format!("{}:{}:defE={e}:defO={o}", attempt["result"]["kind"].as_str().unwrap_or("?"), attempt["definition_id"].as_str().unwrap_or("?")));
            }
            let entries_equal_plain: Vec<bool> = {
                let plain: Value = serde_json::from_slice(&plain(mode, &raw)).unwrap();
                (0..2).map(|i| successor["contract_evidence"]["exact_cases"][i] == plain["contract_evidence"]["exact_cases"][i]).collect()
            };
            println!("RV123_UNAVAILABLE {fname} {} statuses={statuses:?} w1={:?} preparations={prep:?} evidence_entry_unchanged={entries_equal_plain:?} identity={} armed_left={left:?}",
                mode.as_str(), retained.as_ref().err(), successor["producer"]["semantic_contract_id"]);
        }
    }
}
