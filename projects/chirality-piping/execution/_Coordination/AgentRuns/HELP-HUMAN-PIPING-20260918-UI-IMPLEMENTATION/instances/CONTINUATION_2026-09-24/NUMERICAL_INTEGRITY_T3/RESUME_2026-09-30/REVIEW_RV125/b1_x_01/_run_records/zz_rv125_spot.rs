//! RV125 (RV-X of PR-B1; disposable archive copy only, never committed): spot checks on the PR
//! head's Direct entry, registered and Stale, with B1's three-case input W-C2.
//! - W-C2 (the request inside each committed W-C2 successor fixture), both modes: the Direct
//!   entry's one publication, its class, build status and refusal, its published bytes' sha256
//!   against SP's pins, and (registered) the successor against the fixture's `source`; the
//!   Rust reader on it, bound, unbound and transport; the successor and invocation written for
//!   the Python and TypeScript readers.
//! - W-C2 permuted (c, a, b): the same three cases in another request order. Each case's rows,
//!   by (kind, entity) and its own case, and its preview evidence must carry the same values as
//!   in request order a, b, c; each case's status and the receipt's owners must follow the case,
//!   not its position (the ordinal mapping).
//! - W-C2 with one pressure region on its third case: D1.5 refuses every case's pressure, so the
//!   Direct entry publishes exactly the value route's bytes, with no notice.
//! Expectations are asserted here; every row is also written to RV125_OUT as JSON.
use super::*;
use serde_json::{json, Value};
use sha2::{Digest, Sha256};
use std::path::Path;

fn sha(bytes: &[u8]) -> String { format!("{:x}", Sha256::digest(bytes)) }

const SP_PINNED_BYTES: [(&str, &str); 2] = [
    ("sparse_interactive", "c7a1859330e9e36e18f5572838dbad72ea251a817241acc6968f8f83b70170fa"),
    ("dense_scrutiny", "a77c010b4ae7ffa9c535c31305b8a91fcc3c05e8a512075fa5b4694dbae3062c"),
];

fn fixture(mode: PreviewSolverMode) -> Value {
    let path = Path::new(env!("CARGO_MANIFEST_DIR"))
        .join(format!("../../fixtures/results/retained_precision_w_c2_successor_{}.json", mode.as_str()));
    serde_json::from_slice(&std::fs::read(path).unwrap()).unwrap()
}

fn permuted(raw: &Value, order: &[&str]) -> Value {
    let mut raw = raw.clone();
    let cases = raw["model"]["load_cases"].as_array().unwrap().clone();
    raw["model"]["load_cases"] = Value::Array(order.iter().map(|id| cases.iter().find(|c| c["id"] == *id).unwrap().clone()).collect());
    raw
}

fn with_pressure_on_third(raw: &Value) -> Value {
    let mut raw = raw.clone();
    let pipe = raw["model"]["pipe_segments"][0].clone();
    raw["model"]["load_cases"][2]["pressure_regions"] = json!([{"id": "region:rv125", "member_pipe_ids": [pipe["id"]],
        "pressure_basis": "internal_differential_zero_external_v1", "pressure": {"value": 1.0e5, "unit": "Pa"},
        "terminals": [
            {"node_ref": pipe["from"], "closure_transfer": "transfers_to_wall", "provenance": "explicit_test_closure"},
            {"node_ref": pipe["to"], "closure_transfer": "transfers_to_wall", "provenance": "explicit_test_closure"}],
        "provenance": "invented_rv125_pressure_control"}]);
    raw
}

struct Run { row: Value, published: Vec<u8>, successor: Option<Value>, value_bytes: Option<Vec<u8>> }

fn run(label: &str, raw: &Value, mode: PreviewSolverMode) -> Run {
    let value = run_linear_static_preview_value_with_mode(raw.clone(), mode);
    let value_bytes = value.as_ref().ok().map(|e| serde_json::to_vec(e).unwrap());
    let output = run_linear_static_preview_value_with_retained_direct(raw.clone(), mode).expect("direct entry");
    let envelope_bytes = serde_json::to_vec(output.envelope()).unwrap();
    let profile = output.admission().map(|r| format!("{:?}", r.profile));
    let refusal = output.admission().and_then(|r| r.law().refusal.map(|x| format!("{x:?}")));
    let cause = match output.retained() { None => "none".to_string(), Some(Ok(_)) => "successor".into(), Some(Err(f)) => format!("{f:?}") };
    let successor = output.successor().cloned();
    let published = match output.into_publication() {
        RetainedPublication::Successor(v) => serde_json::to_vec(&v).unwrap(),
        RetainedPublication::Ordinary(e) => serde_json::to_vec(&e).unwrap(),
    };
    let doc: Value = serde_json::from_slice(&published).unwrap();
    let notices = doc["diagnostics"].as_array().map_or(0, |d| d.iter().filter(|x| x["code"] == "RETAINED_PRECISION_UNAVAILABLE").count());
    let class = if successor.is_some() { "successor" } else if Some(&published) == value_bytes.as_ref() { "exact" } else { "OTHER" };
    let row = json!({"label": label, "mode": mode.as_str(), "class": class, "profile": profile, "refusal": refusal, "cause": cause,
        "published_sha": sha(&published), "value_sha": value_bytes.as_ref().map(|b| sha(b)),
        "envelope_equals_value_route": Some(&envelope_bytes) == value_bytes.as_ref(), "unavailable_diagnostics": notices,
        "load_cases": raw["model"]["load_cases"].as_array().map_or(0, |c| c.len())});
    Run { row, published, successor, value_bytes }
}

/// Each case's rows keyed by (case, kind, entity), with the value's bits; and each preview case's
/// evidence keyed by its case id. Row ids are left out (a case after the first is qualified).
fn per_case(doc: &Value) -> (Vec<(String, String, String, String)>, Vec<(String, String)>) {
    let mut rows: Vec<_> = doc["results"].as_array().unwrap().iter().map(|r| (
        r["basis_ref"]["ref_id"].as_str().unwrap_or("").to_owned(), r["kind"].as_str().unwrap().to_owned(),
        r["entity_ref"].as_str().unwrap_or("").to_owned(),
        format!("{:016x}|{}", r["value"].as_f64().unwrap().to_bits(), r.get("recovery_method").map_or("-".to_string(), |m| m.to_string())))).collect();
    rows.sort();
    let mut evidence: Vec<_> = doc["contract_evidence"]["preview_cases"].as_array().map_or(vec![], |cs| cs.iter().map(|c| {
        let mut c = c.clone();
        // result ids inside the evidence are qualified by position; compare the numbers only.
        for x in c["pipe_stress_extrema"].as_array_mut().into_iter().flatten() { x.as_object_mut().unwrap().remove("result_id"); }
        for x in c["intensified_measures"].as_array_mut().into_iter().flatten() { x.as_object_mut().unwrap().remove("result_id"); }
        (c["load_case_id"].as_str().unwrap().to_owned(), c.to_string())
    }).collect());
    evidence.sort();
    (rows, evidence)
}

fn statuses(successor: &Value) -> Vec<(String, String)> {
    let mut s: Vec<_> = successor["retained_precision"]["body"]["cases"].as_array().unwrap().iter()
        .map(|c| (c["basis_ref"]["ref_id"].as_str().unwrap().to_owned(), c["status"].as_str().unwrap().to_owned())).collect();
    s.sort();
    s
}

/// The receipt's owners must follow the case: every Run's origin owner, every call owner and every
/// execution-order entry names the request index whose case the Run's source owns.
fn owners_follow_cases(successor: &Value, raw: &Value) -> bool {
    let b = &successor["retained_precision"]["body"];
    let ids: Vec<&str> = raw["model"]["load_cases"].as_array().unwrap().iter().map(|c| c["id"].as_str().unwrap()).collect();
    let source_case = |si: u64| b["sources"][si as usize]["owner"]["case_index"].as_u64();
    let mut ok = true;
    for (ci, c) in b["cases"].as_array().unwrap().iter().enumerate() {
        ok &= c["basis_ref"]["ref_id"] == ids[ci];
        if !c["run"].is_null() {
            ok &= c["run"]["origin"]["owner_ref"] == json!({"kind": "case", "index": ci});
            ok &= source_case(c["run"]["origin"]["source_ref"].as_u64().unwrap()) == Some(ci as u64);
            ok &= b["sources"][c["source_ref"].as_u64().unwrap() as usize]["owner"]["case_id"] == ids[ci];
        }
        if let Some(a) = c["product_attempt_ref"].as_u64() {
            ok &= b["product_attempts"][a as usize]["owner_ref"] == json!({"kind": "case", "index": ci});
        }
    }
    for call in b["calls"].as_array().unwrap() {
        for (pos, owner) in call["owner_refs"].as_array().unwrap().iter().enumerate() {
            let si = call["source_refs"][pos].as_u64().unwrap();
            ok &= owner["index"].as_u64() == source_case(si);
        }
    }
    for entry in b["work"]["execution_order"].as_array().unwrap() {
        let ci = entry["index"].as_u64().unwrap() as usize;
        ok &= !b["cases"][ci]["run"].is_null();
    }
    ok
}

fn reader_rows(label: &str, mode: PreviewSolverMode, successor: &Value, invocation: &Value) -> Value {
    use open_pipe_stress_result_export::retained_precision as rx;
    let show = |r: Result<rx::Validation, rx::ValidationError>| match r {
        Ok(v) => json!({"ok": true, "bound": v.invocation_bound, "eligible": v.numerical_eligible, "classes": v.classifications.len()}),
        Err(e) => json!({"ok": false, "gate": e.gate, "code": e.code, "detail": e.detail}),
    };
    json!({"label": label, "mode": mode.as_str(), "rs_bound": show(rx::validate(successor, Some(invocation))),
        "rs_unbound": show(rx::validate(successor, None)), "rs_transport": show(rx::validate_transport_metadata(successor))})
}

#[test]
#[ignore]
fn zz_rv125_spot() {
    let out = std::env::var("RV125_OUT").expect("RV125_OUT");
    let mut rows = Vec::new();
    let mut registered = None;
    for (mode, (name, pinned)) in [PreviewSolverMode::SparseInteractive, PreviewSolverMode::DenseScrutiny].into_iter().zip(SP_PINNED_BYTES) {
        assert_eq!(mode.as_str(), name);
        let doc = fixture(mode);
        let raw = doc["invocation"]["request"].clone();
        assert_eq!(doc["invocation"]["solver_mode"], name);
        // 1. W-C2 through the Direct entry.
        let w = run("w_c2", &raw, mode);
        let this = w.row["profile"] == json!("Registered");
        assert_eq!(*registered.get_or_insert(this), this, "one build status");
        let registered = this;
        assert!(w.row["envelope_equals_value_route"].as_bool().unwrap(), "{name}: the ordinary owner is the value route's");
        rows.push(w.row.clone());
        if registered {
            let successor = w.successor.clone().expect("registered: a successor");
            assert_eq!(w.row["refusal"], Value::Null, "{name}: admitted");
            assert_eq!(sha(&w.published), pinned, "{name}: SP's pinned published bytes");
            assert_eq!(successor, doc["source"], "{name}: the committed fixture's source");
            assert_eq!(statuses(&successor), [("case-a".into(), "selected".into()), ("case-b".into(), "not_required".into()), ("case-c".into(), "unavailable".into())]);
            assert!(owners_follow_cases(&successor, &raw), "{name}: owners follow cases");
            let invocation = json!({"request": raw, "solver_mode": name});
            let readers = reader_rows("w_c2", mode, &successor, &invocation);
            assert_eq!(readers["rs_bound"]["ok"], true, "{name}: {readers}");
            rows.push(readers);
            std::fs::write(format!("{out}.w_c2_{name}.source.json"), &w.published).unwrap();
            std::fs::write(format!("{out}.w_c2_{name}.invocation.json"), serde_json::to_vec(&invocation).unwrap()).unwrap();
            // 2. Permuted: c, a, b.
            let raw_p = permuted(&raw, &["case-c", "case-a", "case-b"]);
            let p = run("w_c2_cab", &raw_p, mode);
            rows.push(p.row.clone());
            let successor_p = p.successor.clone().expect("permuted: a successor");
            assert_eq!(statuses(&successor_p), statuses(&successor), "{name}: statuses follow the cases");
            assert!(owners_follow_cases(&successor_p, &raw_p), "{name}: permuted owners follow cases");
            let (rows_a, ev_a) = per_case(&successor);
            let (rows_p, ev_p) = per_case(&successor_p);
            let differing: Vec<_> = rows_a.iter().zip(&rows_p).filter(|(x, y)| x != y).map(|(x, y)| json!([x, y])).take(10).collect();
            rows.push(json!({"label": "w_c2_cab_vs_abc", "mode": name, "rows": [rows_a.len(), rows_p.len()],
                "rows_equal": rows_a == rows_p, "evidence_equal": ev_a == ev_p, "first_differing": differing,
                "summary_abc": successor["summary"], "summary_cab": successor_p["summary"]}));
            assert_eq!(rows_a, rows_p, "{name}: each case's rows and values follow the case");
            assert_eq!(ev_a, ev_p, "{name}: each case's evidence follows the case");
            let invocation_p = json!({"request": raw_p, "solver_mode": name});
            let readers_p = reader_rows("w_c2_cab", mode, &successor_p, &invocation_p);
            assert_eq!(readers_p["rs_bound"]["ok"], true, "{name}: {readers_p}");
            rows.push(readers_p);
            std::fs::write(format!("{out}.w_c2_cab_{name}.source.json"), &p.published).unwrap();
            std::fs::write(format!("{out}.w_c2_cab_{name}.invocation.json"), serde_json::to_vec(&invocation_p).unwrap()).unwrap();
        } else {
            assert_eq!(w.row["class"], "exact", "{name}: Stale publishes the ordinary bytes");
            assert_eq!(w.row["unavailable_diagnostics"], 0);
            assert_eq!(Some(w.published.clone()), w.value_bytes, "{name}: Stale = value route");
        }
        // 3. Pressure on the third case.
        let q = run("w_c2_pressure_on_third", &with_pressure_on_third(&raw), mode);
        assert_eq!(q.row["class"], "exact", "{name}: {}", q.row);
        assert_eq!(q.row["unavailable_diagnostics"], 0);
        if registered {
            assert_eq!(q.row["refusal"], json!("Family(Case, PressureRegions)"), "{name}: D1.5");
        }
        rows.push(q.row);
    }
    std::fs::write(&out, serde_json::to_string_pretty(&rows).unwrap() + "\n").unwrap();
    println!("RV125_OUT rows={} registered={registered:?}", rows.len());
}

/// The request with its load cases replaced by copies of case `from`, one per id (load ids
/// suffixed with the id), in the given order.
fn copies(raw: &Value, plan: &[(&str, &str)]) -> Value {
    let mut raw = raw.clone();
    let cases = raw["model"]["load_cases"].as_array().unwrap().clone();
    raw["model"]["load_cases"] = Value::Array(plan.iter().map(|(from, id)| {
        let mut case = cases.iter().find(|c| c["id"] == *from).unwrap().clone();
        if from != id {
            case["id"] = json!(id);
            for load in case["primitive_loads"].as_array_mut().unwrap() {
                load["id"] = json!(format!("{}:{id}", load["id"].as_str().unwrap()));
            }
        }
        case
    }).collect());
    raw
}

/// One case's rows by (kind, entity) with value bits and method; its evidence without ids; and the
/// Rust reader's classifications of its rows by (kind, entity).
fn case_view(doc: &Value, case: &str, invocation: &Value) -> Value {
    use open_pipe_stress_result_export::retained_precision as rx;
    let results = doc["results"].as_array().unwrap();
    let mut rows: Vec<String> = results.iter().filter(|r| r["basis_ref"]["ref_id"] == case).map(|r| format!("{}|{}|{:016x}|{}",
        r["kind"].as_str().unwrap(), r["entity_ref"].as_str().unwrap_or(""), r["value"].as_f64().unwrap().to_bits(),
        r.get("recovery_method").map_or("-".to_string(), |m| m.to_string()))).collect();
    rows.sort();
    let mut evidence = doc["contract_evidence"]["preview_cases"].as_array().unwrap().iter().find(|c| c["load_case_id"] == case).cloned().unwrap_or(Value::Null);
    if let Some(o) = evidence.as_object_mut() {
        o.remove("load_case_id");
        for list in ["pipe_stress_extrema", "intensified_measures"] {
            for x in o.get_mut(list).and_then(Value::as_array_mut).into_iter().flatten() { x.as_object_mut().unwrap().remove("result_id"); }
        }
    }
    let mut classes: Vec<String> = match rx::validate(doc, Some(invocation)) {
        Ok(v) => v.classifications.iter().filter(|c| c.basis_ref["ref_id"] == case).map(|c| {
            let row = results.iter().find(|r| r["id"].as_str() == Some(c.result_id.as_str())).unwrap();
            format!("{}|{}|{:016x}|{:?}|{:?}", row["kind"].as_str().unwrap(), row["entity_ref"].as_str().unwrap_or(""), c.normalized_bits, c.scale_bits, c.class)
        }).collect(),
        Err(e) => vec![format!("REFUSED {} {}", e.gate, e.code)],
    };
    classes.sort();
    let status = doc["retained_precision"]["body"]["cases"].as_array().map(|cs| cs.iter().find(|c| c["basis_ref"]["ref_id"] == case).map(|c| c["status"].clone()));
    json!({"rows": rows, "evidence": evidence, "classes": classes, "status": status})
}

fn notice_ids(doc: &Value) -> Vec<String> {
    doc["diagnostics"].as_array().unwrap().iter()
        .filter(|d| d["code"] == "RETAINED_PRECISION_UNAVAILABLE" && d["message"].as_str().is_some_and(|m| m.starts_with(RETAINED_UNAVAILABLE_NOTICE)))
        .map(|d| d["id"].as_str().unwrap().to_owned()).collect()
}

/// RV125's probes of custody and the transaction at C = 3 (registered build only):
/// - a a2 a3 (three copies of W-C2's selected case): every case selected, each with exactly the
///   rows, evidence, status and reader classes of case a alone (c = 1);
/// - b b2 b3 (not_required): A empty, the exact ordinary bytes, no notice;
/// - c c2 c3 (unavailable): no case selected, so the ordinary bytes with one N1 notice per case
///   in A, in request order, and nothing else changed;
/// - b c c2: A = {c, c2}: two notices, in request order, none for b.
#[test]
#[ignore]
fn zz_rv125_probe() {
    let out = std::env::var("RV125_PROBE_OUT").expect("RV125_PROBE_OUT");
    let mut rows = Vec::new();
    for mode in [PreviewSolverMode::SparseInteractive, PreviewSolverMode::DenseScrutiny] {
        let name = mode.as_str();
        let base = fixture(mode)["invocation"]["request"].clone();
        let invocation_of = |raw: &Value| json!({"request": raw, "solver_mode": name});
        let first = run("a_alone", &copies(&base, &[("case-a", "case-a")]), mode);
        if first.row["profile"] != json!("Registered") {
            rows.push(json!({"mode": name, "skipped": "not the registered build"}));
            continue;
        }
        let alone_raw = copies(&base, &[("case-a", "case-a")]);
        let alone = first.successor.clone().expect("case a alone publishes");
        let reference = case_view(&alone, "case-a", &invocation_of(&alone_raw));
        rows.push(first.row.clone());
        // a a2 a3
        let raw = copies(&base, &[("case-a", "case-a"), ("case-a", "case-a2"), ("case-a", "case-a3")]);
        let r = run("a_a2_a3", &raw, mode);
        rows.push(r.row.clone());
        let successor = r.successor.clone().unwrap_or_else(|| panic!("{name}: a a2 a3 publishes: {}", r.row));
        assert!(owners_follow_cases(&successor, &raw), "{name}");
        for case in ["case-a", "case-a2", "case-a3"] {
            let view = case_view(&successor, case, &invocation_of(&raw));
            let same = view["rows"] == reference["rows"] && view["evidence"] == reference["evidence"] && view["classes"] == reference["classes"];
            rows.push(json!({"label": "a_a2_a3_vs_a_alone", "mode": name, "case": case, "status": view["status"], "rows_equal": view["rows"] == reference["rows"],
                "evidence_equal": view["evidence"] == reference["evidence"], "classes_equal": view["classes"] == reference["classes"],
                "classes": view["classes"].as_array().map(Vec::len)}));
            assert!(same, "{name} {case}: custody: {view} vs {reference}");
            assert_eq!(view["status"], json!("selected"));
        }
        // b b2 b3: A empty.
        let raw = copies(&base, &[("case-b", "case-b"), ("case-b", "case-b2"), ("case-b", "case-b3")]);
        let r = run("b_b2_b3", &raw, mode);
        assert_eq!((r.row["class"].as_str(), r.row["cause"].as_str(), r.row["unavailable_diagnostics"].as_u64()), (Some("exact"), Some("NoTriggeredCase"), Some(0)), "{name}: {}", r.row);
        rows.push(r.row);
        // c c2 c3, and b c c2: the fallback's notices.
        for (label, plan, expected) in [
            ("c_c2_c3", vec![("case-c", "case-c"), ("case-c", "case-c2"), ("case-c", "case-c3")], vec!["case-c", "case-c2", "case-c3"]),
            ("b_c_c2", vec![("case-b", "case-b"), ("case-c", "case-c"), ("case-c", "case-c2")], vec!["case-c", "case-c2"]),
        ] {
            let raw = copies(&base, &plan);
            let r = run(label, &raw, mode);
            let published: Value = serde_json::from_slice(&r.published).unwrap();
            let ids = notice_ids(&published);
            let mut prefix = published.clone();
            let diagnostics = prefix["diagnostics"].as_array_mut().unwrap();
            let keep = diagnostics.len().saturating_sub(expected.len());
            diagnostics.truncate(keep);
            let value: Value = serde_json::from_slice(r.value_bytes.as_ref().unwrap()).unwrap();
            let want: Vec<String> = expected.iter().map(|c| format!("diagnostic:retained-precision:{c}:unavailable")).collect();
            rows.push(json!({"label": label, "mode": name, "cause": r.row["cause"], "class": r.row["class"], "notice_ids": ids,
                "prefix_equals_value_route": prefix == value, "published_sha": r.row["published_sha"]}));
            assert!(r.successor.is_none(), "{name} {label}: no case selected");
            assert_eq!(ids, want, "{name} {label}: one N1 notice per case in A, in request order");
            assert_eq!(prefix, value, "{name} {label}: the ordinary bytes before the notices");
        }
    }
    std::fs::write(&out, serde_json::to_string_pretty(&rows).unwrap() + "\n").unwrap();
    println!("RV125_PROBE_OUT rows={}", rows.len());
}
