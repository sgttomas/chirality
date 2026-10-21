//! The source-route replay census sweeps (DEL-04-08, "Source-route replay design"; scratch
//! prototype, never merged): O4's single-member source-work sweep, two-case and many-case
//! invocations, listed requests and the fault-model mutants, each in the census's four
//! configurations ({R-A off, R-A on} x {full replay, bind-only}). Compiled only under the
//! opt-in `census-probe` feature (included from `o4_m3_judging_tests.rs`); every target is
//! `#[ignore]`. Measurement only: the 8,000,000 per-case and 64,000,000 invocation limits,
//! every gate and every check are unchanged, and nothing here asserts a census outcome.
//! Records go to `REPLAY_CENSUS_OUT`. Every model is invented. Ported from R-A's census
//! (`ra_census_tests.rs` on `claude/piping-ra-census-20261021` at 4d956a6b8a).
//! Standard claim fence applies (F-PIP-2; claims taxonomy per DEC-081).
use super::*;
use crate::source_recovery::j7_rf_census::replay_method_census::{self as rm, Cfg, CONFIGS};
use open_pipe_stress_frame_kernel::structural::retained_api::census_probe::replay::{self, Mutant};

const SECTIONS: [(f64, f64); 5] = [(0.168, 0.007), (0.219, 0.0082), (0.324, 0.0095), (0.114, 0.006), (0.273, 0.0093)];
const MODE: PreviewSolverMode = PreviewSolverMode::SparseInteractive;

fn out_dir() -> Option<std::path::PathBuf> {
    std::env::var_os("REPLAY_CENSUS_OUT").map(std::path::PathBuf::from)
}
fn pilot() -> Option<usize> {
    std::env::var("REPLAY_CENSUS_PILOT").ok().and_then(|v| v.parse().ok())
}
fn write(name: &str, rows: &[Value]) {
    if let Some(dir) = out_dir() {
        std::fs::create_dir_all(&dir).unwrap();
        std::fs::write(dir.join(name), serde_json::to_vec(rows).unwrap()).unwrap();
    }
}
fn write_file(rel: &str, bytes: &[u8]) {
    if let Some(dir) = out_dir() {
        let p = dir.join(rel);
        std::fs::create_dir_all(p.parent().unwrap()).unwrap();
        std::fs::write(p, bytes).unwrap();
    }
}
fn name_of(raw: &Value) -> String {
    format!("{:x}", Sha256::digest(serde_json::to_vec(raw).unwrap()))
}

/// An envelope's outcome class, as R-A's census records it.
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
/// Every differing leaf path between two envelopes, classified against R-A's census allowance.
fn diff(full: &Value, bind: &Value) -> (Vec<String>, Vec<String>) {
    let (mut allowed, mut violations) = (Vec::new(), Vec::new());
    fn walk(a: &Value, b: &Value, path: &mut Vec<String>, root: (&Value, &Value), allowed: &mut Vec<String>, violations: &mut Vec<String>) {
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
                if rm::allowed_work_change(path, root.0, root.1, a, b) {
                    allowed.push(at);
                } else {
                    violations.push(at);
                }
            }
        }
    }
    walk(full, bind, &mut Vec::new(), (full, bind), &mut allowed, &mut violations);
    (allowed, violations)
}
fn source_diagnostics(env: &Value) -> Vec<Value> {
    env["diagnostics"].as_array().into_iter().flatten().filter(|d| d["code"].as_str().is_some_and(|c| c.starts_with("SOURCE_BLOCK")))
        .map(|d| json!({"code": d["code"], "message": d["message"].as_str().map(|m| m.chars().take(800).collect::<String>())})).collect()
}

/// One configuration of one request: the internal observed run with its ledger and the
/// replay probe's finalization records, and the product entry.
struct Side {
    record: Value,
    internal: Value,
    public: Result<Value, String>,
}
fn side(raw: &Value, cfg: Cfg, mutant: Mutant) -> Side {
    let (request, capture) = source_receipt::CapturedInvocation::parse(raw.clone(), MODE).expect("parses");
    let route = w1_route(&request.model).unwrap_or_default();
    let mut budget = w1_budget(route);
    let _ = replay::drain();
    let envelope = rm::under_mutant(cfg, mutant, || run_linear_static_preview_observed(request, MODE, Some(&capture), &mut budget, None));
    let records = rm::records_json(&replay::drain());
    let internal = serde_json::to_value(&envelope).unwrap();
    let public = rm::under_mutant(cfg, mutant, || run_linear_static_preview_value_with_mode(raw.clone(), MODE)).map(|e| serde_json::to_value(e).unwrap());
    let public_records = rm::records_json(&replay::drain());
    let receipt = internal["source_block_recovery"]["body"].clone();
    let record = json!({
        "internal": {"class": class(&internal), "case_charges": receipt["cases"].as_array().map(|c| c.iter().map(|c| c["work"]["charged"].clone()).collect::<Vec<_>>()),
            "invocation_work": receipt["invocation_work"],
            "budget": {"charged": budget.charged, "failed_charged": budget.failed_charged, "publication_charged": budget.publication_charged,
                "rejected": budget.rejected, "attempts": budget.attempts, "per_case_limit": budget.per_case_limit},
            "diagnostics": source_diagnostics(&internal),
            "finalization": records},
        "public": match &public {
            Ok(env) => json!({"class": class(env), "identity": env["producer"]["semantic_contract_id"], "diagnostics": source_diagnostics(env),
                "finalization": public_records}),
            Err(e) => json!({"refused": e, "finalization": public_records}),
        },
    });
    Side { record, internal, public }
}
fn shadow_findings(name: &str, s: &Side) -> Vec<String> {
    let mut f = Vec::new();
    for at in ["internal", "public"] {
        let r = &s.record[at]["finalization"];
        for m in r["shadow_mismatches"].as_array().into_iter().flatten() {
            f.push(format!("{name} {at}: shadow mismatch {m}"));
        }
    }
    f
}
/// Each load case of a selected envelope against the direct method on that case alone.
fn publication(raw: &Value, env: &Value, ra_off: bool) -> (usize, Vec<String>) {
    let (mut checked, mut failures) = (0usize, Vec::new());
    let cases = raw["model"]["load_cases"].as_array().unwrap();
    for case in cases {
        let id = case["id"].as_str().unwrap();
        let mut single = raw.clone();
        single["model"]["load_cases"] = json!([case]);
        let Some(direct) = rm::method(&single, MODE, ra_off).1 else {
            failures.push(format!("{id}: the direct method did not select"));
            continue;
        };
        let (n, f) = rm::publication_check_case(raw, MODE, env, &direct, id);
        checked += n;
        failures.extend(f);
    }
    (checked, failures)
}
/// The declared-problem oracle's input for a selected bind-only run: the product's test-only
/// dump of the same run, the published envelope, the request, its theory and allowance.
fn oracle_input(raw: &Value, cfg: Cfg, mutant: Mutant, info: &Value, rel: &str) -> bool {
    let (Some(theory), Some(allowance)) = (info["theory"].as_str(), info["allowance"].as_str()) else { return false };
    let (on, records) = rm::under_mutant(cfg, mutant, || source_receipt::with_source_dump(|| {
        run_linear_static_preview_value_with_mode(raw.clone(), MODE).map(|e| serde_json::to_value(e).unwrap())
    }));
    let _ = replay::drain();
    let Ok(on) = on else { return false };
    if !on["source_block_recovery"].is_object() {
        return false;
    }
    let dump = json!({"artifact": "o4-source-declared-problem-dump", "schema_version": "1.0.0", "solver_mode": MODE.as_str(),
        "publication_sha256": on["source_block_recovery"]["body"]["publication_sha256"], "records": records});
    write_file(&format!("{rel}/request.json"), &serde_json::to_vec(raw).unwrap());
    write_file(&format!("{rel}/envelope.json"), &serde_json::to_vec(&on).unwrap());
    write_file(&format!("{rel}/dump.json"), &serde_json::to_vec(&dump).unwrap());
    write_file(&format!("{rel}/meta.json"), &serde_json::to_vec(&json!({"theory": theory, "allowance": allowance, "config": cfg.name(),
        "mutant": mutant.name()})).unwrap());
    true
}
/// The census's rules on one request, per R-A setting: bind-only against the full replay.
fn judge(raw: &Value, info: &Value, sides: &BTreeMap<&'static str, Side>) -> Value {
    let mut out = json!({});
    let mut findings: Vec<String> = Vec::new();
    for (n, s) in sides {
        findings.extend(shadow_findings(n, s));
    }
    for ra_off in [true, false] {
        let (fcfg, bcfg) = (Cfg { ra_off, bind: false }, Cfg { ra_off, bind: true });
        let (Some(full), Some(bind)) = (sides.get(fcfg.name()), sides.get(bcfg.name())) else { continue };
        let (cf, cb) = (full.record["internal"]["class"].as_str().unwrap(), bind.record["internal"]["class"].as_str().unwrap());
        let rule = if cf == cb { "preserved" } else if cb == "selected" { "newly_selected" } else if cf == "selected" { "lost_selection" } else { "changed_non_selection" };
        let (mut allowed, mut violations) = (Vec::new(), Vec::new());
        if rule == "preserved" || rule == "changed_non_selection" {
            let (a, v) = diff(&full.internal, &bind.internal);
            allowed.extend(a.into_iter().map(|p| format!("internal/{p}")));
            violations.extend(v.into_iter().map(|p| format!("internal/{p}")));
            match (&full.public, &bind.public) {
                (Ok(x), Ok(y)) => {
                    let (a, v) = diff(x, y);
                    allowed.extend(a.into_iter().map(|p| format!("public/{p}")));
                    violations.extend(v.into_iter().map(|p| format!("public/{p}")));
                }
                (Err(x), Err(y)) if rm::mask_work(x) == rm::mask_work(y) => {}
                _ => violations.push("public outcome".into()),
            }
        }
        let (mut checked, mut pub_failures) = (0usize, Vec::new());
        let mut oracle = false;
        if let Ok(env) = &bind.public {
            if env["source_block_recovery"].is_object() && (rule == "newly_selected" || std::env::var("REPLAY_CENSUS_PUBLICATION_ALL").is_ok()) {
                (checked, pub_failures) = publication(raw, env, ra_off);
            }
            if rule == "newly_selected" && env["source_block_recovery"].is_object() {
                let name = name_of(raw);
                write_file(&format!("newly_selected/{}/{name}.request.json", bcfg.ra()), &serde_json::to_vec(raw).unwrap());
                write_file(&format!("newly_selected/{}/{name}.envelope.json", bcfg.ra()), &serde_json::to_vec(env).unwrap());
                oracle = oracle_input(raw, bcfg, Mutant::None, info, &format!("oracle/{}/{name}", bcfg.ra()));
            }
        }
        if rule == "newly_selected" {
            // Every finalization the bind-only replay passed was judged by the shadow.
            for at in ["internal", "public"] {
                for c in bind.record[at]["finalization"]["cases"].as_array().into_iter().flatten() {
                    if c["outcome"] == "ok" && c["shadow"] != "ok" {
                        findings.push(format!("{} {at}: case {} passed bind-only without a passing shadow: {}", bcfg.name(), c["case_id"], c["shadow"]));
                    }
                }
            }
        }
        if rule == "lost_selection" {
            findings.push(format!("R-A {}: a case selected with the full replay is not selected bind-only", bcfg.ra()));
        }
        findings.extend(violations.iter().map(|v| format!("R-A {}: difference outside the allowance: {v}", bcfg.ra())));
        findings.extend(pub_failures.iter().map(|p| format!("R-A {}: publication: {p}", bcfg.ra())));
        out[bcfg.ra()] = json!({"rule": rule, "full": cf, "bind": cb, "allowed_paths": allowed.len(), "allowed": allowed,
            "violations": violations, "publication_checked": checked, "publication": pub_failures, "oracle_input": oracle});
    }
    out["findings"] = json!(findings);
    out
}
fn census(raw: &Value, info: &Value) -> Value {
    let mut sides = BTreeMap::new();
    for cfg in CONFIGS {
        sides.insert(cfg.name(), side(raw, cfg, Mutant::None));
    }
    let judged = judge(raw, info, &sides);
    let mut row = json!({"judged": judged});
    for (k, s) in &sides {
        row[*k] = s.record.clone();
    }
    row
}
fn summary_line(tag: &str, label: &str, row: &Value) {
    let c = |k: &str| row[k]["internal"]["class"].as_str().unwrap_or("?").to_owned();
    println!("{tag} {label} off_full={} off_bind={} on_full={} on_bind={} rule_off={} rule_on={} charges_on_full={} charges_on_bind={} inv_on_bind={} findings={}",
        c("off_full"), c("off_bind"), c("on_full"), c("on_bind"), row["judged"]["off"]["rule"], row["judged"]["on"]["rule"],
        row["on_full"]["internal"]["case_charges"], row["on_bind"]["internal"]["case_charges"],
        row["on_bind"]["internal"]["budget"]["charged"], row["judged"]["findings"].as_array().map_or(0, Vec::len));
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
                                info["theory"] = json!(theory);
                                info["allowance"] = json!(allowance);
                                info["style"] = json!(style);
                                info["layout"] = json!(layout);
                                docs.push((raw, info, format!("{layout} {section:?} {lname} r={ratio:e} {theory} {style} {allowance}")));
                            }
                        }
                    }
                }
            }
        }
    }
    if let Some(n) = pilot() {
        let step = (docs.len() / n.max(1)).max(1);
        docs = docs.into_iter().step_by(step).take(n).collect();
    }
    docs
}

#[test]
#[ignore = "replay census: O4's single-member sweep in the four configurations (run with --features census-probe --ignored)"]
fn replay_census_single_members() {
    let mut rows = Vec::new();
    let started = std::time::Instant::now();
    for (raw, info, label) in sweep_docs(&["rf345", "zhinge122"]) {
        let t = std::time::Instant::now();
        let mut row = census(&raw, &info);
        row["info"] = info;
        row["label"] = json!(label);
        row["seconds"] = json!(t.elapsed().as_secs_f64());
        summary_line("REPLAY_SWEEP", &label, &row);
        rows.push(row);
    }
    println!("REPLAY_SWEEP documents={} seconds={:.1}", rows.len(), started.elapsed().as_secs_f64());
    write("single_members.json", &rows);
}

fn with_cases(raw: &Value, n: usize, scale: impl Fn(usize) -> f64) -> Value {
    let mut raw = raw.clone();
    let cases = raw["model"]["load_cases"].as_array_mut().unwrap();
    let first = cases[0].clone();
    for i in 1..n {
        let mut c = first.clone();
        c["id"] = json!(format!("case{}", i + 1));
        for l in c["primitive_loads"].as_array_mut().unwrap() {
            let v = l["magnitude"]["value"].as_f64().unwrap();
            l["magnitude"]["value"] = json!(decimal(v * scale(i), 3));
            l["id"] = json!(format!("{}:{}", l["id"].as_str().unwrap(), i + 1));
        }
        cases.push(c);
    }
    raw
}

/// RF §5.2 (6): two-case invocations, a decimal Z-hinge case then a second case on the same
/// structure (its moment halved, as an authored decimal), as R-A's census built them.
#[test]
#[ignore = "replay census: two-case invocations (run with --features census-probe --ignored)"]
fn replay_census_multi_case() {
    let mut rows = Vec::new();
    for (raw, info, label) in sweep_docs(&["zhinge122"]).into_iter().filter(|(_, i, _)| i["style"] == "decimal") {
        let raw = with_cases(&raw, 2, |_| 0.5);
        let mut row = census(&raw, &info);
        row["info"] = info;
        row["label"] = json!(label);
        summary_line("REPLAY_MULTI", &label, &row);
        rows.push(row);
    }
    write("multi_case.json", &rows);
}

/// RF §5.2 (6) near the invocation limit: R-A's census's 36 invocations of 8, 9 and 10 load
/// cases on one decimal Z-hinge structure, each later case's moment scaled by 1 + i/10.
#[test]
#[ignore = "replay census: many-case invocations near the invocation limit (run with --features census-probe --ignored)"]
fn replay_census_many_cases() {
    let mut rows = Vec::new();
    let docs: Vec<_> = sweep_docs(&["zhinge122"]).into_iter().filter(|(_, i, _)| i["style"] == "decimal").collect();
    let step = (docs.len() / 12).max(1);
    for (raw, info, label) in docs.into_iter().step_by(step).take(12) {
        for n in [8usize, 9, 10] {
            let raw = with_cases(&raw, n, |i| 1.0 + i as f64 / 10.0);
            let mut row = census(&raw, &info);
            row["info"] = info.clone();
            row["label"] = json!(format!("{label} cases={n}"));
            summary_line("REPLAY_MANY", &format!("{label} cases={n}"), &row);
            rows.push(row);
        }
    }
    write("many_cases.json", &rows);
}

/// Any requests, one path per line in the file named by `REPLAY_CENSUS_REQUESTS`.
#[test]
#[ignore = "replay census: listed requests (run with --features census-probe --ignored)"]
fn replay_census_listed_requests() {
    let Ok(list) = std::env::var("REPLAY_CENSUS_REQUESTS") else { return };
    let mut rows = Vec::new();
    for path in std::fs::read_to_string(list).unwrap().lines().filter(|l| !l.trim().is_empty()) {
        let raw: Value = serde_json::from_str(&std::fs::read_to_string(path.trim()).unwrap()).unwrap();
        let theory = if raw["model"]["pressure_contract"]["shear_model"].as_str().is_some_and(|s| s.contains("timoshenko")) { "timo" } else { "eb" };
        let info = json!({"theory": theory, "allowance": "zero"});
        let mut row = census(&raw, &json!({}));
        row["label"] = json!(path.trim());
        row["info"] = info;
        summary_line("REPLAY_LISTED", path.trim(), &row);
        rows.push(row);
    }
    write("listed.json", &rows);
}

// ------------------------------------------------------------------------- mutants

fn fixture(family: &str, name: &str) -> Value {
    let p = std::path::Path::new(env!("CARGO_MANIFEST_DIR")).join(format!("../../fixtures/product_preview/pressure_source/{family}/{name}.request.json"));
    serde_json::from_str(&std::fs::read_to_string(p).unwrap()).unwrap()
}
/// Every published projection and row value, by id: value bits, interval, both bounds.
fn published(env: &Value) -> BTreeMap<String, String> {
    let mut out = BTreeMap::new();
    for case in env["source_block_recovery"]["body"]["cases"].as_array().into_iter().flatten() {
        for p in case["projections"].as_array().into_iter().flatten() {
            out.insert(format!("projection {}", p["functional_id"].as_str().unwrap_or_default()),
                format!("{} {} {} {}", p["value_bits"], p["interval"], p["absolute_error_bound"], p["relative_error_bound"]));
        }
    }
    for r in env["results"].as_array().into_iter().flatten() {
        out.insert(format!("row {}", r["id"].as_str().unwrap_or_default()), format!("{:016x}", r["value"].as_f64().map_or(0, f64::to_bits)));
    }
    out
}
fn reader(raw: &Value, env: &Value) -> Value {
    use open_pipe_stress_result_export::physics_source as ps;
    let invocation = json!({"request": raw, "solver_mode": MODE.as_str()});
    json!({"validate_in": format!("{:?}", ps::validate_in(env, Some(&invocation), ps::SourceContract::PressureV3)),
        "transport": format!("{:?}", ps::validate_transport_metadata_in(env, ps::SourceContract::PressureV3))})
}

/// The fault models, each with the full replay and bind-only at R-A on (and R-A off), on a
/// small set: four committed raw source controls, one PIN-OFF-345 control, one
/// load/reference-state control and two decimal Z-hinge documents selected today. Supporting
/// evidence only: each mutant is injected into the live attempt, the retained copy or the
/// captured rebuild, never into the replay.
#[test]
#[ignore = "replay census: mutants (run with --features census-probe --ignored)"]
fn replay_census_mutants() {
    let mut docs: Vec<(String, Value, Value)> = Vec::new();
    for name in ["n05", "n06", "fields", "mixed"] {
        docs.push((format!("physics_source/{name}"), fixture("physics_source", name), json!({})));
    }
    let pin = crate::source_recovery::j7_rf_census::inputs()["cases"].as_array().unwrap().iter()
        .find(|c| c["id"] == "RF-SKEW-T-PIN-OFF-345-r1e-08").unwrap().clone();
    docs.push(("rf/RF-SKEW-T-PIN-OFF-345-r1e-08".into(), crate::source_recovery::j7_rf_census::current_request(&pin), json!({})));
    docs.push(("load_reference_source/n05".into(), fixture("load_reference_source", "n05"), json!({})));
    let mut zh = 0;
    for theory in ["eb", "timo"] {
        for (raw, info, label) in sweep_docs(&["zhinge122"]) {
            if zh >= 2 || info["style"] != "decimal" || info["theory"] != theory || info["allowance"] != "zero" {
                continue;
            }
            let s = side(&raw, Cfg { ra_off: false, bind: false }, Mutant::None);
            if s.record["internal"]["class"] == "selected" {
                docs.push((format!("zhinge/{label}"), raw, info));
                zh += 1;
                break;
            }
        }
    }
    let configs: Vec<Cfg> = match std::env::var("REPLAY_CENSUS_CONFIGS") {
        Ok(v) => CONFIGS.into_iter().filter(|c| v.split(',').any(|x| x == c.name())).collect(),
        Err(_) => vec![Cfg { ra_off: false, bind: false }, Cfg { ra_off: false, bind: true }],
    };
    let mut rows = Vec::new();
    for (di, (label, raw, info)) in docs.iter().enumerate() {
        for &cfg in &configs {
            let base = side(raw, cfg, Mutant::None);
            let base_pub = base.public.as_ref().ok().filter(|e| e["source_block_recovery"].is_object()).map(published);
            write_file(&format!("mutants/{di}/none/{}.request.json", cfg.name()), &serde_json::to_vec(raw).unwrap());
            if let Ok(env) = &base.public {
                write_file(&format!("mutants/{di}/none/{}.envelope.json", cfg.name()), &serde_json::to_vec(env).unwrap());
            }
            rows.push(json!({"doc": label, "index": di, "config": cfg.name(), "mutant": "none", "record": base.record,
                "public_class": base.record["public"]["class"]}));
            for m in Mutant::ALL {
                let s = side(raw, cfg, m);
                let mut row = json!({"doc": label, "index": di, "config": cfg.name(), "mutant": m.name(), "record": s.record,
                    "internal_class": s.record["internal"]["class"], "public_class": s.record["public"]["class"],
                    "public_refused": s.record["public"]["refused"]});
                match &s.public {
                    Ok(env) if env["source_block_recovery"].is_object() => {
                        let now = published(env);
                        let differs: Vec<String> = match &base_pub {
                            Some(b) => now.iter().filter(|(k, v)| b.get(*k) != Some(v)).map(|(k, _)| k.clone())
                                .chain(b.keys().filter(|k| !now.contains_key(*k)).cloned()).collect(),
                            None => vec!["no unmutated source publication to compare".into()],
                        };
                        row["published"] = json!(true);
                        row["published_tokens_differing"] = json!(differs.len());
                        row["published_differing_sample"] = json!(differs.iter().take(8).collect::<Vec<_>>());
                        row["reader"] = reader(raw, env);
                        write_file(&format!("mutants/{di}/{}/{}.request.json", m.name(), cfg.name()), &serde_json::to_vec(raw).unwrap());
                        write_file(&format!("mutants/{di}/{}/{}.envelope.json", m.name(), cfg.name()), &serde_json::to_vec(env).unwrap());
                        row["oracle_input"] = json!(oracle_input(raw, cfg, m, info, &format!("mutant_oracle/{di}-{}-{}", m.name(), cfg.name())));
                    }
                    _ => {
                        row["published"] = json!(false);
                    }
                }
                println!("REPLAY_MUTANT {label} {} {} internal={} public={} published={} differing={} applied={}",
                    cfg.name(), m.name(), row["internal_class"], row["public_class"], row["published"], row["published_tokens_differing"],
                    s.record["public"]["finalization"]["mutants_applied"]);
                rows.push(row);
            }
        }
    }
    write("mutants.json", &rows);
}
