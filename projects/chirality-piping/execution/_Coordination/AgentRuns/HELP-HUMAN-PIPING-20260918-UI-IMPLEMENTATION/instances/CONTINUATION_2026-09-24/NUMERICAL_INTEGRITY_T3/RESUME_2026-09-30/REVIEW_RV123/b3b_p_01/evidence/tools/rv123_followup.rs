
/// RV123 scratch follow-up (1): the unavailable branch through the actual Direct entry (the
/// candidate fault is applied at G-C to the case in the capture's own fields).
#[test]
fn rv123_followup_unavailable_branch_direct() {
    use super::retained_wire as wire;
    use super::retained_receipt::TraceFault as F;
    let mut two = raw();
    let mut second = two["model"]["load_cases"][0].clone();
    second["id"] = json!("case-2");
    for load in second["primitive_loads"].as_array_mut().unwrap() {
        load["id"] = json!(format!("{}:2", load["id"].as_str().unwrap()));
    }
    two["model"]["load_cases"].as_array_mut().unwrap().push(second);
    let two = exact3(two);
    for (fname, fault) in [("maxima", F::Maxima), ("values", F::ValuesCompletion), ("after_helper", F::AfterHelper)] {
        for mode in MODES {
            hooks::fault_next_candidate(fault);
            let raw = two.clone();
            let (output, counts, captured) = hooks::counted_with_successor(move || run_linear_static_preview_value_with_retained_direct(raw, mode).unwrap());
            let left = hooks::armed_names();
            hooks::disarm();
            let w1 = output.retained().map(|r| r.as_ref().err().cloned());
            let Some(successor) = captured else {
                println!("RV123_FOLLOW_UNAV {fname} {} successor=none w1={w1:?} counts={counts:?} armed_left={left:?}", mode.as_str());
                continue;
            };
            let body = &successor["retained_precision"]["body"];
            let statuses: Vec<&str> = body["cases"].as_array().unwrap().iter().map(|c| c["status"].as_str().unwrap()).collect();
            let mut prep = Vec::new();
            for source in body["sources"].as_array().unwrap() {
                if source["preparation"].is_null() { prep.push("none".to_owned()); continue; }
                let attempt = &body["product_attempts"][source["preparation"]["attempt_ref"].as_u64().unwrap() as usize];
                let e = source["preparation"]["sha256"] == json!(preparation_hash(attempt, wire::EXACT_DEFINITION_SHA256));
                prep.push(format!("{}:{}:defE={e}", attempt["result"]["kind"].as_str().unwrap_or("?"), attempt["definition_id"].as_str().unwrap_or("?")));
            }
            let plain: Value = serde_json::from_slice(&plain(mode, &two)).unwrap();
            let unchanged: Vec<bool> = (0..2).map(|i| successor["contract_evidence"]["exact_cases"][i] == plain["contract_evidence"]["exact_cases"][i]).collect();
            let patched = open_pipe_stress_result_export::rv123_exact_reader::validate(&successor, None).map(|v| v.numerical_eligible).map_err(|e| (e.gate, e.code, e.detail));
            println!("RV123_FOLLOW_UNAV {fname} {} statuses={statuses:?} preparations={prep:?} entry_unchanged={unchanged:?} identity={} patched_rs_g0_g7={patched:?} w1={w1:?} armed_left={left:?}",
                mode.as_str(), successor["producer"]["semantic_contract_id"]);
        }
    }
}

/// RV123 scratch follow-up (2): ν = 0.3 against its preview twin (G authored as Ĝ), row by row
/// with absolute differences and each kind's largest magnitude.
#[test]
fn rv123_followup_nu_03_rows() {
    let mut x = m3x();
    x["model"]["materials"][0]["poisson_ratio"] = json!({"value": 0.3, "unit": "1"});
    let twin = rv123_preview_twin(&x);
    for mode in MODES {
        let (_, _, a) = exact_w1(&x, mode);
        let (_, _, b) = exact_w1(&twin, mode);
        let (a, b) = (a.unwrap(), b.unwrap());
        let rows = |s: &Value| s["results"].as_array().unwrap().iter().map(|r| (r["id"].as_str().unwrap().to_owned(), (r["kind"].as_str().unwrap().to_owned(), r["value"].as_f64().unwrap_or(f64::NAN)))).collect::<std::collections::BTreeMap<_, _>>();
        let (ra, rb) = (rows(&a), rows(&b));
        let mut kind_max: std::collections::BTreeMap<String, f64> = Default::default();
        for (k, v) in ra.values() { let m = kind_max.entry(k.clone()).or_insert(0.0); *m = m.max(v.abs()); }
        let mut worst_scaled = (0.0f64, String::new());
        for (id, (k, va)) in &ra {
            let vb = rb[id].1;
            if va.to_bits() == vb.to_bits() { continue; }
            let scale = kind_max[k].max(f64::MIN_POSITIVE);
            let scaled = (va - vb).abs() / scale;
            if scaled > worst_scaled.0 { worst_scaled = (scaled, id.clone()); }
            println!("RV123_FOLLOW_NU {} {id} {k} exact={va:e} twin={vb:e} absdiff={:e} kind_max={scale:e} scaled={scaled:e}", mode.as_str(), (va - vb).abs());
        }
        println!("RV123_FOLLOW_NU_WORST {} {worst_scaled:?}", mode.as_str());
    }
}
