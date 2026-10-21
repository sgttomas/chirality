//! R-A census sweeps (DEL-04-08 Design `source-work-nondyadic-inputs.md` §5): O4's source-work
//! sweeps, the matched-input ablations of the Z-hinge sweep and multi-case invocations, each run
//! with R-A's census switches off and on. Compiled only under the opt-in `census-probe` feature
//! (included from `o4_m3_judging_tests.rs`); every target is `#[ignore]`. Measurement only: the
//! 8,000,000 per-case limit, every gate and every check are unchanged, and nothing here asserts a
//! census outcome. Records go to `RA_CENSUS_OUT` when it is set; `RA_CENSUS_PILOT=<n>` keeps the
//! first n documents of a sweep. Every model is invented.
//! Standard claim fence applies (F-PIP-2; claims taxonomy per DEC-081).
use super::*;
use crate::source_recovery::j7_rf_census::ra_method_census as rm;
use crate::source_recovery::SelectedSourceRecovery;
use open_pipe_stress_frame_kernel::structural::exact_boundary::exact_operation_count as count;
use open_pipe_stress_frame_kernel::structural::retained_api::census_probe::ra;

const SECTIONS: [(f64, f64); 5] = [(0.168, 0.007), (0.219, 0.0082), (0.324, 0.0095), (0.114, 0.006), (0.273, 0.0093)];
const MODE: PreviewSolverMode = PreviewSolverMode::SparseInteractive;
const WORK_CODES: [&str; 3] = ["SOURCE_BLOCK_RECOVERY_SELECTED", "SOURCE_BLOCK_RECOVERY_UNAVAILABLE", "SOURCE_BLOCK_RECOVERY_FINALIZATION_FAILED"];

fn out_dir() -> Option<std::path::PathBuf> {
    std::env::var_os("RA_CENSUS_OUT").map(std::path::PathBuf::from)
}
fn pilot() -> Option<usize> {
    std::env::var("RA_CENSUS_PILOT").ok().and_then(|v| v.parse().ok())
}
fn write(name: &str, rows: &[Value]) {
    if let Some(dir) = out_dir() {
        std::fs::create_dir_all(&dir).unwrap();
        std::fs::write(dir.join(name), serde_json::to_vec(rows).unwrap()).unwrap();
    }
}

/// An envelope's outcome class, as the census records it.
fn class(env: &Value) -> &'static str {
    let codes: Vec<&str> = env["diagnostics"].as_array().into_iter().flatten().filter_map(|d| d["code"].as_str()).collect();
    if env["source_block_recovery"].is_object() {
        "selected"
    } else if codes.contains(&"SOURCE_BLOCK_RECOVERY_FINALIZATION_FAILED") {
        "blocking_finalization_failed"
    } else if codes.contains(&"SOURCE_BLOCK_RECOVERY_UNAVAILABLE") {
        "declined"
    } else {
        "not_attempted"
    }
}
/// Masks digit runs, so two texts that differ only in printed numbers compare equal.
fn mask(s: &str) -> String {
    let mut out = String::with_capacity(s.len());
    let mut digits = false;
    for ch in s.chars() {
        if ch.is_ascii_digit() {
            if !digits {
                out.push('#');
            }
            digits = true;
        } else {
            digits = false;
            out.push(ch);
        }
    }
    out
}
/// Every differing leaf path between two envelopes, classified against §5's allowance: a work
/// counter (under a `work` or `invocation_work` object), a hash (`*_sha256`, `*_digest`), or a
/// work-printing diagnostic whose text differs only in its printed numbers. Anything else is a
/// violation, which stops R-A for diagnosis.
fn diff(off: &Value, on: &Value) -> (Vec<String>, Vec<String>) {
    let (mut allowed, mut violations) = (Vec::new(), Vec::new());
    fn walk(a: &Value, b: &Value, path: &mut Vec<String>, root: &Value, allowed: &mut Vec<String>, violations: &mut Vec<String>) {
        match (a, b) {
            (Value::Object(x), Value::Object(y)) => {
                for k in x.keys().chain(y.keys().filter(|k| !x.contains_key(*k))) {
                    path.push(k.clone());
                    walk(x.get(k).unwrap_or(&Value::Null), y.get(k).unwrap_or(&Value::Null), path, root, allowed, violations);
                    path.pop();
                }
            }
            (Value::Array(x), Value::Array(y)) if x.len() == y.len() => {
                for (i, (p, q)) in x.iter().zip(y).enumerate() {
                    path.push(i.to_string());
                    walk(p, q, path, root, allowed, violations);
                    path.pop();
                }
            }
            _ if a == b => {}
            _ => {
                let at = path.join("/");
                let work = path.iter().any(|k| k == "work" || k == "invocation_work");
                let hash = path.last().is_some_and(|k| k.ends_with("sha256") || k.ends_with("digest"));
                let text = path.len() == 3 && path[0] == "diagnostics" && path[2] == "message"
                    && path[1].parse::<usize>().ok().and_then(|i| root["diagnostics"][i]["code"].as_str()).is_some_and(|c| WORK_CODES.contains(&c))
                    && a.as_str().zip(b.as_str()).is_some_and(|(x, y)| mask(x) == mask(y));
                if work || hash || text {
                    allowed.push(at);
                } else {
                    violations.push(at);
                }
            }
        }
    }
    walk(off, on, &mut Vec::new(), off, &mut allowed, &mut violations);
    (allowed, violations)
}

/// One side (R-A off or on) of one request: the internal observed run with its ledger, the
/// product entry, the direct method, the probe's records and the operation counter's control.
struct Side {
    record: Value,
    internal: Value,
    public: Result<Value, String>,
    direct: Option<SelectedSourceRecovery>,
}
fn side(raw: &Value, on: bool) -> Side {
    let (request, capture) = source_receipt::CapturedInvocation::parse(raw.clone(), MODE).expect("parses");
    let route = w1_route(&request.model).unwrap_or_default();
    let mut budget = w1_budget(route);
    let _ = ra::drain();
    count::reset();
    let envelope = rm::under(on, || run_linear_static_preview_observed(request, MODE, Some(&capture), &mut budget, None));
    let totals = count::totals();
    let records = rm::records_json(&ra::drain());
    let internal = serde_json::to_value(&envelope).unwrap();
    let public = rm::under(on, || run_linear_static_preview_value_with_mode(raw.clone(), MODE)).map(|e| serde_json::to_value(e).unwrap());
    let _ = ra::drain();
    let (method, direct) = rm::method(raw, MODE, on);
    let receipt = internal["source_block_recovery"]["body"].clone();
    let record = json!({
        "internal": {"class": class(&internal), "case_charges": receipt["cases"].as_array().map(|c| c.iter().map(|c| c["work"]["charged"].clone()).collect::<Vec<_>>()),
            "invocation_work": receipt["invocation_work"],
            "budget": {"charged": budget.charged, "failed_charged": budget.failed_charged, "publication_charged": budget.publication_charged,
                "rejected": budget.rejected, "attempts": budget.attempts, "per_case_limit": budget.per_case_limit},
            "diagnostics": internal["diagnostics"].as_array().into_iter().flatten().filter(|d| d["code"].as_str().is_some_and(|c| c.starts_with("SOURCE_BLOCK")))
                .map(|d| json!({"code": d["code"], "message": d["message"].as_str().map(|m| m.chars().take(600).collect::<String>())})).collect::<Vec<_>>()},
        "public": match &public { Ok(env) => json!({"class": class(env), "identity": env["producer"]["semantic_contract_id"]}), Err(e) => json!({"refused": e}) },
        "method": method,
        "records": records,
        "operation_control": {"shortfalls": totals.shortfalls(), "mul_calls": totals.mul.calls, "pairs": totals.pairs,
            "charged": totals.mul.charged + totals.add.charged, "counted": totals.mul.counted + totals.add.counted},
    });
    Side { record, internal, public, direct }
}
/// §5's pre-registered rules on one request.
fn judge(raw: &Value, off: &Side, on: &Side) -> Value {
    let (ci, cn) = (off.record["internal"]["class"].as_str().unwrap(), on.record["internal"]["class"].as_str().unwrap());
    let mut findings: Vec<String> = Vec::new();
    for (name, s) in [("off", off), ("on", on)] {
        if s.record["operation_control"]["shortfalls"] != 0 {
            findings.push(format!("{name}: a Work call charged less than it executed"));
        }
        for m in [&s.record["records"]["shadow_mismatches"], &s.record["method"]["records"]["shadow_mismatches"]] {
            if m.as_array().is_some_and(|m| !m.is_empty()) {
                findings.push(format!("{name}: shadow mismatch {m}"));
            }
        }
    }
    let rule = if ci == cn { "preserved" } else if cn == "selected" { "newly_selected" } else if ci == "selected" { "lost_selection" } else { "changed_non_selection" };
    let (mut allowed, mut violations) = (Vec::new(), Vec::new());
    if rule == "preserved" || rule == "changed_non_selection" {
        let (a, v) = diff(&off.internal, &on.internal);
        allowed.extend(a.into_iter().map(|p| format!("internal/{p}")));
        violations.extend(v.into_iter().map(|p| format!("internal/{p}")));
        match (&off.public, &on.public) {
            (Ok(x), Ok(y)) => {
                let (a, v) = diff(x, y);
                allowed.extend(a.into_iter().map(|p| format!("public/{p}")));
                violations.extend(v.into_iter().map(|p| format!("public/{p}")));
            }
            (Err(x), Err(y)) if mask(x) == mask(y) => {}
            _ => violations.push("public outcome".into()),
        }
    }
    // The method level: off and on must agree on everything but work.
    let (mo, mn) = (&off.record["method"], &on.record["method"]);
    for k in ["outcome", "response_digest", "retained_digest", "stage", "helper_stage", "error"] {
        if mo[k] != mn[k] && !(k == "error" && mo[k].as_str().zip(mn[k].as_str()).is_some_and(|(x, y)| mask(x) == mask(y))) {
            violations.push(format!("method/{k}"));
        }
    }
    let (mut publication, mut checked) = (Vec::new(), 0usize);
    if let Ok(env) = &on.public {
        if env["source_block_recovery"].is_object() {
            // Each load case against the direct method on that case alone.
            for case in raw["model"]["load_cases"].as_array().unwrap() {
                let id = case["id"].as_str().unwrap();
                let mut single = raw.clone();
                single["model"]["load_cases"] = json!([case]);
                let direct = if raw["model"]["load_cases"].as_array().unwrap().len() == 1 { None } else { rm::method(&single, MODE, true).1 };
                let Some(direct) = direct.as_ref().or(on.direct.as_ref()) else {
                    publication.push(format!("{id}: the direct method did not select"));
                    continue;
                };
                let (n, f) = rm::publication_check_case(raw, MODE, env, direct, id);
                checked += n;
                publication.extend(f);
            }
        }
    }
    if rule == "newly_selected" {
        if let (Some(dir), Ok(env)) = (out_dir(), &on.public) {
            let d = dir.join("newly_selected");
            std::fs::create_dir_all(&d).unwrap();
            let name = format!("{:x}", Sha256::digest(serde_json::to_vec(raw).unwrap()));
            std::fs::write(d.join(format!("{name}.request.json")), serde_json::to_vec(raw).unwrap()).unwrap();
            std::fs::write(d.join(format!("{name}.envelope.json")), serde_json::to_vec(env).unwrap()).unwrap();
        }
    }
    if rule == "lost_selection" {
        findings.push("a case selected off is not selected on".into());
    }
    findings.extend(violations.iter().map(|v| format!("difference outside the allowance: {v}")));
    findings.extend(publication.iter().map(|p| format!("publication: {p}")));
    json!({"rule": rule, "allowed_paths": allowed.len(), "violations": violations, "publication_checked": checked, "publication": publication, "findings": findings})
}
fn census(raw: &Value) -> Value {
    let off = side(raw, false);
    let on = side(raw, true);
    let judged = judge(raw, &off, &on);
    json!({"off": off.record, "on": on.record, "judged": judged})
}

/// The census inputs of one sweep (O4's `census_sweep` loops), in O4's order.
fn sweep_docs(layouts: &[&str]) -> Vec<(Value, Value, String)> {
    let mut docs = Vec::new();
    for layout in layouts {
        for &section in &SECTIONS {
            let nu = 0.3;
            let lstar = (annular_phi(section.0, section.1, nu, 1.0) / 2.0).sqrt();
            for (lname, length) in [("near_phi2_mm", decimal_mm(lstar)), ("short", 0.75), ("long", 2.5)] {
                for ratio in [1e-8, 1e-12] {
                    for theory in ["eb", "timo"] {
                        for style in ["decimal", "dyadic"] {
                            for allowance in ["zero", "both"] {
                                let (doc, info) = census_document(layout, section, length, ratio, theory, style, allowance);
                                let raw = judged_request(&doc, &format!("invented:o4-census:{layout}:{lname}"));
                                let mut info = info;
                                info["length_class"] = json!(lname);
                                docs.push((raw, info, format!("{layout} {section:?} {lname} r={ratio:e} {theory} {style} {allowance}")));
                            }
                        }
                    }
                }
            }
        }
    }
    if let Some(n) = pilot() {
        // A pilot keeps n documents spread over the sweep, Z-hinge decimal ones included.
        let step = (docs.len() / n.max(1)).max(1);
        docs = docs.into_iter().step_by(step).take(n).collect();
    }
    docs
}
fn run_sweep(name: &str, layouts: &[&str]) {
    let mut rows = Vec::new();
    let started = std::time::Instant::now();
    for (raw, info, label) in sweep_docs(layouts) {
        let t = std::time::Instant::now();
        let mut row = census(&raw);
        row["info"] = info;
        row["label"] = json!(label);
        row["seconds"] = json!(t.elapsed().as_secs_f64());
        println!("RA_CENSUS {name} {label} off={} on={} rule={} charge_off={} charge_on={} findings={}",
            row["off"]["internal"]["class"], row["on"]["internal"]["class"], row["judged"]["rule"],
            row["off"]["internal"]["case_charges"], row["on"]["internal"]["case_charges"], row["judged"]["findings"].as_array().map_or(0, Vec::len));
        rows.push(row);
    }
    println!("RA_CENSUS {name} documents={} seconds={:.1}", rows.len(), started.elapsed().as_secs_f64());
    write(&format!("{name}.json"), &rows);
}

#[test]
#[ignore = "R-A census: O4's single-member sweep off and on (run with --features census-probe --ignored)"]
fn ra_census_single_members() {
    run_sweep("single_members", &["rf345", "zhinge122"]);
}
#[test]
#[ignore = "R-A census: O4's small-frame sweep off and on (run with --features census-probe --ignored)"]
fn ra_census_small_frames() {
    run_sweep("small_frames", &["run2", "lframe"]);
}

/// One Z-hinge document with the named inputs in their dyadic form and the rest decimal
/// (`census_document`'s rules, applied one input at a time; §5 "matched-input ablations").
fn ablation_request(section: (f64, f64), length: f64, ratio: f64, theory: &str, allowance: &str, dyadic_inputs: &[&str]) -> (Value, Value) {
    let dy = |x: &str| dyadic_inputs.contains(&x);
    let (mut d, mut t) = section;
    let (mut e, mut nu) = (2.03e11, 0.3);
    let mut l = length;
    if dy("D") { d = dyadic(d, 6); }
    if dy("t") { t = dyadic(t, 6); }
    if dy("E") { e = 1.5 * 2f64.powi(37); }
    if dy("nu") { nu = 0.3125; }
    if dy("L") { l = dyadic(l, 8); }
    let ro = d / 2.0;
    let ri = ro - t;
    let g = e / (2.0 * (1.0 + nu));
    let j = std::f64::consts::PI / 2.0 * (ro.powi(4) - ri.powi(4));
    let k_exact = ratio * g * j / l;
    let k = if dy("k") { 2f64.powi(k_exact.log2().round() as i32) } else { decimal(k_exact, 3) };
    let m1 = if dy("m1") { 2f64.powi((k.log2() - 4.0) as i32) } else { decimal(0.0617 * k, 3) };
    let (cm, ca) = if allowance == "both" { (0.125 * t, if t < 0.006 { 0.25 * t } else { 0.0015 }) } else { (0.0, 0.0) };
    let doc = json!({"shear_model": theory_token(theory), "material": {"id": "steel", "elastic_modulus_Pa": e, "poisson_ratio": nu},
        "nodes": [{"id": "N0", "xyz_m": [0.0, 0.0, 0.0]}, {"id": "N1", "xyz_m": [l / 3.0, 2.0 * l / 3.0, 2.0 * l / 3.0]}],
        "members": [{"id": "M1", "from": "N0", "to": "N1", "outside_diameter_m": d, "wall_thickness_m": t, "mill_tolerance_m": cm,
            "corrosion_allowance_m": ca, "y_reference": [0.0, 0.0, 1.0]}],
        "supports": [{"id": "rigid:N0", "node": "N0", "kind": "rigid", "restraints": ["UX", "UY", "UZ", "RX", "RY"]},
            {"id": "spring:N0", "node": "N0", "kind": "spring", "dof": "RZ", "stiffness": k, "unit": "N*m/rad"},
            {"id": "rigid:N1", "node": "N1", "kind": "rigid", "restraints": ["UZ", "RX", "RY"]}],
        "loads": [{"id": "l0", "node": "N1", "kind": "moment", "direction": "z", "value": m1, "unit": "N*m"}], "pressure_regions": []});
    let info = json!({"D": d, "t": t, "L": l, "E": e, "nu": nu, "k": k, "m1": m1, "ratio": ratio, "theory": theory, "allowance": allowance,
        "dyadic_inputs": dyadic_inputs});
    (judged_request(&doc, "invented:ra-census:ablation:zhinge122"), info)
}

/// The matched-input ablations: every decimal Z-hinge document of the sweep, all-decimal, each of
/// D, t, L, E, nu, k and m1 dyadic alone, and all dyadic. The all-decimal and all-dyadic forms
/// reproduce the sweep's decimal and dyadic documents.
#[test]
#[ignore = "R-A census: matched-input ablations of the Z-hinge sweep (run with --features census-probe --ignored)"]
fn ra_census_zhinge_ablations() {
    let mut rows = Vec::new();
    let variants: Vec<Vec<&str>> = std::iter::once(vec![])
        .chain(["D", "t", "L", "E", "nu", "k", "m1"].into_iter().map(|x| vec![x]))
        .chain(std::iter::once(vec!["D", "t", "L", "E", "nu", "k", "m1"]))
        .collect();
    let mut n = 0usize;
    'outer: for &section in &SECTIONS {
        let lstar = (annular_phi(section.0, section.1, 0.3, 1.0) / 2.0).sqrt();
        for (lname, length) in [("near_phi2_mm", decimal_mm(lstar)), ("short", 0.75), ("long", 2.5)] {
            for ratio in [1e-8, 1e-12] {
                for theory in ["eb", "timo"] {
                    for allowance in ["zero", "both"] {
                        if pilot().is_some_and(|p| n >= p) {
                            break 'outer;
                        }
                        n += 1;
                        for v in &variants {
                            let (raw, mut info) = ablation_request(section, length, ratio, theory, allowance, v);
                            info["length_class"] = json!(lname);
                            let mut row = census(&raw);
                            row["info"] = info;
                            println!("RA_ABLATION {section:?} {lname} r={ratio:e} {theory} {allowance} dyadic={v:?} off={} on={} charge_off={} charge_on={}",
                                row["off"]["internal"]["class"], row["on"]["internal"]["class"],
                                row["off"]["internal"]["case_charges"], row["on"]["internal"]["case_charges"]);
                            rows.push(row);
                        }
                    }
                }
            }
        }
    }
    write("zhinge_ablations.json", &rows);
}

/// RF §5.2 (6): multi-case invocations that put a decimal Z-hinge case before a second case on
/// the same structure (its moment halved, as an authored decimal), so a newly selecting first case
/// charges the shared invocation ledger before the second attempts.
#[test]
#[ignore = "R-A census: multi-case invocations (run with --features census-probe --ignored)"]
fn ra_census_multi_case() {
    let mut rows = Vec::new();
    let mut n = 0usize;
    for (raw, info, label) in sweep_docs(&["zhinge122"]) {
        if info["style"] != "decimal" || pilot().is_some_and(|p| n >= p) {
            continue;
        }
        n += 1;
        let mut raw = raw;
        let cases = raw["model"]["load_cases"].as_array_mut().unwrap();
        let mut second = cases[0].clone();
        second["id"] = json!("case2");
        for l in second["primitive_loads"].as_array_mut().unwrap() {
            let v = l["magnitude"]["value"].as_f64().unwrap();
            l["magnitude"]["value"] = json!(decimal(0.5 * v, 3));
            l["id"] = json!(format!("{}:2", l["id"].as_str().unwrap()));
        }
        cases.push(second);
        let mut row = census(&raw);
        row["info"] = info;
        row["label"] = json!(label);
        println!("RA_MULTI {label} off={} on={} rule={} charges_off={} charges_on={} inv_off={} inv_on={}",
            row["off"]["internal"]["class"], row["on"]["internal"]["class"], row["judged"]["rule"],
            row["off"]["internal"]["case_charges"], row["on"]["internal"]["case_charges"],
            row["off"]["internal"]["invocation_work"]["charged"], row["on"]["internal"]["invocation_work"]["charged"]);
        rows.push(row);
    }
    write("multi_case.json", &rows);
}

/// The declared-problem oracle's inputs (§5 "Newly selected cases"): for every Z-hinge sweep,
/// ablation and multi-case request that does not select with R-A off, the product's test-only
/// declared-problem dump (`with_source_dump`, the format `o4_source_payload_dump` writes) and the
/// published envelope of the same run with R-A on, the request, and its theory and allowance.
/// `validation/references/o4_retained_source/declared_problem/oracle.py` judges them.
#[test]
#[ignore = "R-A census: declared-problem oracle inputs for newly selected cases (run with --features census-probe --ignored)"]
fn ra_census_oracle_inputs() {
    let Some(dir) = out_dir() else { return };
    let dir = dir.join("oracle");
    let mut requests: Vec<(Value, String, String)> = Vec::new();
    for (raw, info, _) in sweep_docs(&["zhinge122"]) {
        requests.push((raw.clone(), info["theory"].as_str().unwrap().to_owned(), info["allowance"].as_str().unwrap().to_owned()));
        if info["style"] == "decimal" {
            let mut multi = raw;
            let cases = multi["model"]["load_cases"].as_array_mut().unwrap();
            let mut second = cases[0].clone();
            second["id"] = json!("case2");
            for l in second["primitive_loads"].as_array_mut().unwrap() {
                let v = l["magnitude"]["value"].as_f64().unwrap();
                l["magnitude"]["value"] = json!(decimal(0.5 * v, 3));
                l["id"] = json!(format!("{}:2", l["id"].as_str().unwrap()));
            }
            cases.push(second);
            requests.push((multi, info["theory"].as_str().unwrap().to_owned(), info["allowance"].as_str().unwrap().to_owned()));
        }
    }
    for &section in &SECTIONS {
        let lstar = (annular_phi(section.0, section.1, 0.3, 1.0) / 2.0).sqrt();
        for (_, length) in [("near_phi2_mm", decimal_mm(lstar)), ("short", 0.75), ("long", 2.5)] {
            for ratio in [1e-8, 1e-12] {
                for theory in ["eb", "timo"] {
                    for allowance in ["zero", "both"] {
                        for v in ["D", "t", "L", "E", "nu", "k", "m1"] {
                            requests.push((ablation_request(section, length, ratio, theory, allowance, &[v]).0, theory.into(), allowance.into()));
                        }
                    }
                }
            }
        }
    }
    let mut written = 0usize;
    for (raw, theory, allowance) in requests {
        let off = rm::under(false, || run_linear_static_preview_value_with_mode(raw.clone(), MODE)).map(|e| serde_json::to_value(e).unwrap());
        if off.as_ref().is_ok_and(|e| e["source_block_recovery"].is_object()) {
            continue;
        }
        let (on, records) = rm::under(true, || source_receipt::with_source_dump(|| {
            serde_json::to_value(run_linear_static_preview_value_with_mode(raw.clone(), MODE).unwrap()).unwrap()
        }));
        let _ = ra::drain();
        if !on["source_block_recovery"].is_object() {
            println!("RA_ORACLE not selected on: {theory} {allowance}");
            continue;
        }
        let name = format!("{:x}", Sha256::digest(serde_json::to_vec(&raw).unwrap()));
        let d = dir.join(&name);
        std::fs::create_dir_all(&d).unwrap();
        let dump = json!({"artifact": "o4-source-declared-problem-dump", "schema_version": "1.0.0", "solver_mode": MODE.as_str(),
            "publication_sha256": on["source_block_recovery"]["body"]["publication_sha256"], "records": records});
        std::fs::write(d.join("request.json"), serde_json::to_vec(&raw).unwrap()).unwrap();
        std::fs::write(d.join("envelope.json"), serde_json::to_vec(&on).unwrap()).unwrap();
        std::fs::write(d.join("dump.json"), serde_json::to_vec(&dump).unwrap()).unwrap();
        std::fs::write(d.join("meta.json"), serde_json::to_vec(&json!({"theory": theory, "allowance": allowance,
            "off": off.map(|e| class(&e)).unwrap_or("refused")})).unwrap()).unwrap();
        written += 1;
    }
    println!("RA_ORACLE inputs written={written}");
}
