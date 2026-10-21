//! The source-route replay census: J7 and the committed source controls in the four
//! configurations ({R-A off, R-A on} x {full replay, bind-only}) (DEL-04-08,
//! "Source-route replay design"; scratch prototype, never merged). Compiled only under the
//! opt-in `census-probe` feature; every target is `#[ignore]`. Measurement only: the
//! 8,000,000 per-case limit, every gate and every check are unchanged, and no committed
//! fixture is written. Outputs go only under `REPLAY_CENSUS_OUT`. R-A on with the full
//! replay is main: it must reproduce the committed bytes. R-A off with the full replay must
//! reproduce the pre-R-A bytes, read from `REPLAY_CENSUS_PRE_RA` (an extract of main
//! `9e03991d39`'s `fixtures/` and `core/product_physics/tests/pressure_source_join.rs`).
//! Ported from R-A's census (`ra_j7_census_tests.rs` at 4d956a6b8a).
//! Standard claim fence applies (F-PIP-2; claims taxonomy per DEC-081).
use super::replay_method_census::{self as rmc, publication_check, records_json, under, Cfg, CONFIGS};
use super::*;
use open_pipe_stress_frame_kernel::structural::retained_api::census_probe::replay;
use std::panic::{catch_unwind, AssertUnwindSafe};

fn project_root() -> std::path::PathBuf {
    std::path::Path::new(env!("CARGO_MANIFEST_DIR")).join("../..")
}
/// Writes `bytes` to `REPLAY_CENSUS_OUT/<rel>`; nothing when the variable is unset.
fn write_out(rel: &str, bytes: &[u8]) {
    let Some(dir) = std::env::var_os("REPLAY_CENSUS_OUT") else { return };
    let path = std::path::PathBuf::from(dir).join(rel);
    if let Some(parent) = path.parent() {
        std::fs::create_dir_all(parent).unwrap();
    }
    std::fs::write(&path, bytes).unwrap();
}
fn panic_text(p: Box<dyn std::any::Any + Send>) -> String {
    p.downcast_ref::<String>().cloned().or_else(|| p.downcast_ref::<&str>().map(|s| s.to_string())).unwrap_or_default()
}
fn env_usize(name: &str) -> Option<usize> {
    std::env::var(name).ok().and_then(|v| v.parse().ok())
}
/// Runs `f` over `jobs` on `REPLAY_CENSUS_THREADS` worker threads (default 1), keeping order.
fn parallel<J: Sync, T: Send>(jobs: &[J], f: impl Fn(&J) -> T + Sync) -> Vec<T> {
    let threads = env_usize("REPLAY_CENSUS_THREADS").unwrap_or(1).max(1).min(jobs.len().max(1));
    let next = std::sync::atomic::AtomicUsize::new(0);
    let mut out: Vec<(usize, T)> = std::thread::scope(|scope| {
        let handles: Vec<_> = (0..threads)
            .map(|_| {
                std::thread::Builder::new().stack_size(256 << 20).spawn_scoped(scope, || {
                    let mut mine = Vec::new();
                    loop {
                        let i = next.fetch_add(1, std::sync::atomic::Ordering::SeqCst);
                        if i >= jobs.len() {
                            break mine;
                        }
                        let started = std::time::Instant::now();
                        let value = f(&jobs[i]);
                        eprintln!("REPLAY_CENSUS job {i}/{} done in {:.1}s", jobs.len(), started.elapsed().as_secs_f64());
                        mine.push((i, value));
                    }
                }).unwrap()
            })
            .collect();
        handles.into_iter().flat_map(|h| h.join().unwrap()).collect()
    });
    out.sort_by_key(|(i, _)| *i);
    out.into_iter().map(|(_, v)| v).collect()
}


fn escape(k: &str) -> String {
    k.replace('~', "~0").replace('/', "~1")
}
/// Every JSON pointer at which `a` and `b` differ (an array of different length, or a
/// key on one side only, is reported at that node).
fn diff(a: &Value, b: &Value, path: &str, out: &mut Vec<String>) {
    match (a, b) {
        (Value::Object(x), Value::Object(y)) => {
            let keys: BTreeSet<&String> = x.keys().chain(y.keys()).collect();
            for k in keys {
                let p = format!("{path}/{}", escape(k));
                match (x.get(k), y.get(k)) {
                    (Some(l), Some(r)) => diff(l, r, &p, out),
                    _ => out.push(p),
                }
            }
        }
        (Value::Array(x), Value::Array(y)) if x.len() == y.len() => {
            for (i, (l, r)) in x.iter().zip(y).enumerate() {
                diff(l, r, &format!("{path}/{i}"), out);
            }
        }
        _ => {
            if a != b {
                out.push(path.to_owned());
            }
        }
    }
}
fn segments(pointer: &str) -> Vec<String> {
    pointer.split('/').skip(1).map(|s| s.replace("~1", "/").replace("~0", "~")).collect()
}
/// R-A's census allowance, strictly (`replay_method_census::allowed_work_change`).
fn allowed_envelope_path(pointer: &str, off: &Value, on: &Value) -> bool {
    let s = segments(pointer);
    let at = |e: &Value| s.iter().try_fold(e, |v, k| match v {
        Value::Object(m) => m.get(k),
        Value::Array(x) => k.parse::<usize>().ok().and_then(|i| x.get(i)),
        _ => None,
    }).cloned().unwrap_or(Value::Null);
    super::replay_method_census::allowed_work_change(&s, off, on, &at(off), &at(on))
}
fn classify_envelope(off: &Value, on: &Value) -> Value {
    let mut paths = Vec::new();
    diff(off, on, "", &mut paths);
    let (allowed, not_allowed): (Vec<_>, Vec<_>) = paths.into_iter().partition(|p| allowed_envelope_path(p, off, on));
    json!({"allowed": allowed, "not_allowed": not_allowed})
}


fn pre_ra_root() -> std::path::PathBuf {
    std::path::PathBuf::from(std::env::var_os("REPLAY_CENSUS_PRE_RA").expect("REPLAY_CENSUS_PRE_RA: an extract of 9e03991d39"))
}
/// The committed root for a configuration's baseline: main's for R-A on, 9e03991d39's for R-A off.
fn baseline_root(cfg: Cfg) -> std::path::PathBuf {
    if cfg.ra_off { pre_ra_root() } else { project_root() }
}
fn configs() -> Vec<Cfg> {
    match std::env::var("REPLAY_CENSUS_CONFIGS") {
        Ok(v) => CONFIGS.into_iter().filter(|c| v.split(',').any(|x| x == c.name())).collect(),
        Err(_) => CONFIGS.to_vec(),
    }
}
/// The full-replay configuration at the same R-A setting.
fn full_of(cfg: Cfg) -> Cfg {
    Cfg { bind: false, ..cfg }
}

// ---------------------------------------------------------------- target 1: J7

fn j7_public_checks(id: &str, public: &Result<Value, String>, method: &Option<Result<SelectedSourceRecovery, RecoveryFailure>>) -> Vec<String> {
    let mut failures = Vec::new();
    if let Ok(env) = public {
        if !PUBLISHED.contains(&id) {
            if env.get("source_block_recovery").is_some() {
                failures.push("source publication on an unpublished case".into());
            }
            if env["producer"]["semantic_contract_id"] != PRESSURE_1 {
                failures.push(format!("identity {}", env["producer"]["semantic_contract_id"]));
            }
        }
    }
    let declines: Vec<String> = public.as_ref().map(|env| env["diagnostics"].as_array().unwrap().iter()
        .filter(|d| d["code"] == "SOURCE_BLOCK_RECOVERY_UNAVAILABLE").map(|d| d["message"].as_str().unwrap().to_owned()).collect())
        .unwrap_or_default();
    match (method, declines.as_slice()) {
        (_, []) => {}
        (Some(Err(f)), [text]) => {
            if *text != format!("The bounded retained-source method did not produce a selected response: {f:?}") {
                failures.push("public decline text differs from the direct method's failure".into());
            }
        }
        (_, other) => failures.push(format!("public attempt without a matching direct decline: {other:?}")),
    }
    failures
}

/// One configuration of one J7 entry: J7's `census_entry` logic without its assertions, with
/// the replay probe's records of the public run.
fn j7_side(case: &Value, request: &Value, mode: PreviewSolverMode, cfg: Cfg) -> Value {
    let id = case["id"].as_str().unwrap();
    replay::drain();
    let public = under(cfg, || run_linear_static_preview_value_with_mode(request.clone(), mode).map(|e| serde_json::to_value(e).unwrap()));
    let public_records = replay::drain();
    let owned = Owned::actual(request, mode);
    let method = owned.as_ref().ok().map(|o| {
        under(cfg, || solve_ordinary(o.input(), exact::Limits { operations: PHYSICS_SOURCE_WORK_LIMIT, ..Default::default() }, ForceScale::UNSCALED))
    });
    replay::drain();
    let checks = j7_public_checks(id, &public, &method);
    let run = Run { public, owned, method };
    let first = catch_unwind(AssertUnwindSafe(|| first_cause(&run)))
        .unwrap_or_else(|p| json!({"class": "census_unclassified", "panic": panic_text(p)}));
    let mut entry = json!({"id": id, "family": case["family"], "mode": mode.as_str(), "public": public_value(&run.public),
        "first_cause": first});
    if let (Some(Ok(m)), Ok(o)) = (&run.method, &run.owned) {
        let (n, p) = method_comparison(&references()["cases"][id], m, o);
        entry["method_only_comparison"] = json!({"rows": n, "pass": p});
    }
    let publication = match (&run.public, &run.method) {
        (Ok(env), Some(Ok(m))) if env.get("source_block_recovery").is_some() => {
            let (checked, failures) = publication_check(request, mode, env, m);
            json!({"checked": checked, "failures": failures})
        }
        _ => Value::Null,
    };
    json!({"entry": entry, "public_checks": checks, "publication_check": publication, "records": records_json(&public_records)})
}

fn committed_lines(text: &str) -> BTreeMap<(String, String), String> {
    let doc: Value = serde_json::from_str(text).unwrap();
    let entries = doc["entries"].as_array().unwrap();
    let lines: Vec<&str> = text.lines().skip(1).take(entries.len()).collect();
    entries.iter().zip(lines).map(|(e, l)| {
        ((e["id"].as_str().unwrap().to_owned(), e["mode"].as_str().unwrap().to_owned()), l.strip_suffix(',').unwrap_or(l).to_owned())
    }).collect()
}

fn j7_entry(case: &Value, mode: PreviewSolverMode, baselines: &BTreeMap<&'static str, BTreeMap<(String, String), String>>) -> Value {
    let id = case["id"].as_str().unwrap().to_owned();
    let request = current_request(case);
    let mut sides: BTreeMap<&'static str, Value> = BTreeMap::new();
    for cfg in configs() {
        let side = catch_unwind(AssertUnwindSafe(|| j7_side(case, &request, mode, cfg)))
            .unwrap_or_else(|p| json!({"panic": panic_text(p)}));
        sides.insert(cfg.name(), side);
    }
    let key = (id.clone(), mode.as_str().to_owned());
    let mut out = json!({"id": id, "mode": mode.as_str()});
    let mut violations: Vec<String> = Vec::new();
    for cfg in configs() {
        let s = &sides[cfg.name()];
        if let Some(p) = s.get("panic") {
            violations.push(format!("{}: panic {p}", cfg.name()));
            continue;
        }
        out[cfg.name()] = json!({"class": s["entry"]["first_cause"]["class"], "work": s["entry"]["first_cause"]["work"]["charged"],
            "publication_check": s["publication_check"], "public_checks": s["public_checks"],
            "shadow_checked": s["records"]["shadow_checked"], "shadow_mismatches": s["records"]["shadow_mismatches"],
            "cases": s["records"]["cases"], "public": s["entry"]["public"]});
        for c in s["public_checks"].as_array().unwrap() {
            violations.push(format!("{}: {c}", cfg.name()));
        }
        if let Some(f) = s["publication_check"]["failures"].as_array() {
            for c in f {
                violations.push(format!("{}: publication check: {c}", cfg.name()));
            }
        }
        if let Some(m) = s["entry"].get("method_only_comparison") {
            if m["rows"] != m["pass"] {
                violations.push(format!("{}: direct-method rows outside the frozen criterion {m}", cfg.name()));
            }
        }
        for m in s["records"]["shadow_mismatches"].as_array().into_iter().flatten() {
            violations.push(format!("{}: shadow mismatch: {m}", cfg.name()));
        }
        if !cfg.bind {
            // The control: the full replay reproduces the committed line (main for R-A on,
            // 9e03991d39 for R-A off).
            let line = serde_json::to_string(&s["entry"]).unwrap();
            let equal = baselines.get(cfg.ra()).and_then(|b| b.get(&key)) == Some(&line);
            out[cfg.name()]["baseline_equal_bytes"] = json!(equal);
            if !equal {
                violations.push(format!("{}: entry differs from the committed {} line", cfg.name(), if cfg.ra_off { "9e03991d39" } else { "main" }));
            }
        } else if let Some(full) = sides.get(full_of(cfg).name()).filter(|f| f.get("panic").is_none()) {
            let mut moved = Vec::new();
            diff(&full["entry"], &s["entry"], "", &mut moved);
            out[cfg.name()]["moved_vs_full"] = json!(moved);
            let class = full["entry"]["first_cause"]["class"].as_str().unwrap_or_default();
            for p in &moved {
                let ok = class == "selected_published" && (p == "/public/envelope_sha256" || p == "/public/diagnostics_sha256");
                if !ok {
                    violations.push(format!("{}: entry field moved vs full: {p}", cfg.name()));
                }
            }
        }
    }
    out["violations"] = json!(violations);
    out
}

fn j7_cases() -> Vec<&'static Value> {
    let ids: Option<BTreeSet<String>> = std::env::var("REPLAY_CENSUS_IDS").ok().map(|s| s.split(',').map(str::to_owned).collect());
    let mut cases: Vec<&Value> = inputs()["cases"].as_array().unwrap().iter()
        .filter(|c| ids.as_ref().map_or(true, |ids| ids.contains(c["id"].as_str().unwrap()))).collect();
    if let Some(n) = env_usize("REPLAY_CENSUS_LIMIT") {
        cases.truncate(n);
    }
    cases
}

#[test]
#[ignore = "replay census: J7 in the four configurations (run with --features census-probe --ignored)"]
fn replay_census_j7() {
    let mut baselines = BTreeMap::new();
    baselines.insert("on", committed_lines(EXPECTED));
    if let Ok(text) = std::fs::read_to_string(pre_ra_root().join("fixtures/results/j7_rf_census_expected.json")) {
        baselines.insert("off", committed_lines(&text));
    }
    let jobs: Vec<(&Value, PreviewSolverMode)> = j7_cases().into_iter().flat_map(|c| MODES.map(|m| (c, m))).collect();
    let started = std::time::Instant::now();
    let results = parallel(&jobs, |(case, mode)| j7_entry(case, *mode, &baselines));
    let mut classes: BTreeMap<String, BTreeMap<String, usize>> = BTreeMap::new();
    let mut baseline_equal: BTreeMap<String, usize> = BTreeMap::new();
    let mut moved: BTreeMap<String, BTreeMap<String, BTreeMap<String, usize>>> = BTreeMap::new();
    let mut violations = Vec::new();
    for r in &results {
        for cfg in configs() {
            let c = &r[cfg.name()];
            *classes.entry(cfg.name().into()).or_default().entry(c["class"].as_str().unwrap_or("panic").into()).or_default() += 1;
            if c["baseline_equal_bytes"] == true {
                *baseline_equal.entry(cfg.name().into()).or_default() += 1;
            }
            let class = r[full_of(cfg).name()]["class"].as_str().unwrap_or("panic").to_owned();
            for p in c["moved_vs_full"].as_array().into_iter().flatten() {
                *moved.entry(cfg.name().into()).or_default().entry(class.clone()).or_default().entry(p.as_str().unwrap().into()).or_default() += 1;
            }
        }
        let v = r["violations"].as_array().unwrap();
        if !v.is_empty() {
            violations.push(json!({"id": r["id"], "mode": r["mode"], "violations": v}));
        }
    }
    let summary = json!({"artifact": "replay-census-j7", "entries": results.len(), "seconds": started.elapsed().as_secs_f64(),
        "configs": configs().iter().map(|c| format!("{} {:?}", c.name(), rmc::switches(*c, replay::Mutant::None))).collect::<Vec<_>>(),
        "baselines": baselines.keys().collect::<Vec<_>>(),
        "classes": classes, "baseline_equal_bytes": baseline_equal, "moved_vs_full_by_class": moved,
        "entries_with_violations": violations.len(), "violations": violations});
    println!("REPLAY_CENSUS_J7 {}", serde_json::to_string(&json!({"entries": summary["entries"], "classes": summary["classes"],
        "baseline_equal_bytes": summary["baseline_equal_bytes"], "moved_vs_full_by_class": summary["moved_vs_full_by_class"],
        "entries_with_violations": summary["entries_with_violations"]})).unwrap());
    write_out("j7_summary.json", serde_json::to_string_pretty(&summary).unwrap().as_bytes());
    let lines: Vec<String> = results.iter().map(|r| serde_json::to_string(r).unwrap()).collect();
    write_out("j7_entries.jsonl", (lines.join("\n") + "\n").as_bytes());
}

// --------------------------------------------------- target 2: committed source controls

const RAW_FAMILIES: [(&str, &[&str]); 2] = [
    ("physics_source", &["n05", "n06", "n05_unicode", "n05_units", "fields", "mixed", "mixed_units"]),
    ("load_reference_source", &["n05", "n06", "eigen_motion", "fields", "mixed"]),
];
fn fixture_request(family: &str, name: &str) -> Value {
    let path = project_root().join(format!("fixtures/product_preview/pressure_source/{family}/{name}.request.json"));
    serde_json::from_str(&std::fs::read_to_string(path).unwrap()).unwrap()
}
// The O4 controls, as `source_receipt/o4_source_tests.rs` builds them (copied: private there).
const O4_TIMOSHENKO: &str = "timoshenko_annulus_energy_v1";
fn o4_with_shear_model(mut request: Value, shear_model: &str) -> Value {
    request["model"]["pressure_contract"]["shear_model"] = json!(shear_model);
    request
}
fn o4_with_section(mut request: Value, pipe: usize, mill: Option<f64>, allowance: f64) -> Value {
    let section = &mut request["model"]["pipe_segments"][pipe]["section"];
    if let Some(mill) = mill {
        section["mill_tolerance"] = json!({"value": mill, "unit": "m"});
    }
    section["corrosion_allowance"] = json!({"value": allowance, "unit": "m"});
    request
}
fn o4_two_member(mut request: Value) -> Value {
    let model = &mut request["model"];
    assert_eq!(model["pipe_segments"].as_array().unwrap().len(), 1);
    let mut mid = model["nodes"][1].clone();
    mid["id"] = json!("independent-mid");
    mid["label"] = json!("Invented independent-mid");
    mid["position"] = json!({"x": 1.0, "y": 0, "z": 0});
    model["nodes"].as_array_mut().unwrap().insert(1, mid);
    let mut second = model["pipe_segments"][0].clone();
    model["pipe_segments"][0]["to"] = json!("independent-mid");
    second["id"] = json!("independent-member-2");
    second["label"] = json!("Invented independent-member-2");
    second["from"] = json!("independent-mid");
    model["pipe_segments"].as_array_mut().unwrap().push(second);
    request
}
fn o4_controls() -> Vec<(&'static str, Value)> {
    let fields = || fixture_request("physics_source", "fields");
    vec![
        ("timoshenko-n05", o4_with_shear_model(fixture_request("physics_source", "n05"), O4_TIMOSHENKO)),
        ("dual-basis-fields", o4_with_section(fields(), 0, Some(0.0005), 0.001)),
        ("timoshenko-dual-basis-fields", o4_with_shear_model(o4_with_section(fields(), 0, Some(0.0005), 0.001), O4_TIMOSHENKO)),
        ("mixed-two-member", o4_with_section(o4_two_member(fields()), 0, Some(0.0005), 0.001)),
    ]
}

#[derive(Clone)]
enum Kind {
    Raw { family: &'static str, name: &'static str },
    O4 { id: &'static str },
    Rf { id: String },
}
struct Control {
    kind: Kind,
    label: String,
    request: Value,
    mode: PreviewSolverMode,
}
fn source_controls() -> Vec<Control> {
    let mut out = Vec::new();
    for (family, names) in RAW_FAMILIES {
        for name in names {
            for mode in MODES {
                out.push(Control { kind: Kind::Raw { family, name }, label: format!("{family}/{name}/{}", mode.as_str()),
                    request: fixture_request(family, name), mode });
            }
        }
    }
    for (id, request) in o4_controls() {
        let mut modes = vec![PreviewSolverMode::SparseInteractive];
        if id == "dual-basis-fields" {
            modes.push(PreviewSolverMode::DenseScrutiny);
        }
        for mode in modes {
            out.push(Control { kind: Kind::O4 { id }, label: format!("o4/{id}/{}", mode.as_str()), request: request.clone(), mode });
        }
    }
    for id in PUBLISHED {
        let case = inputs()["cases"].as_array().unwrap().iter().find(|c| c["id"] == id).unwrap();
        for mode in MODES {
            out.push(Control { kind: Kind::Rf { id: id.to_owned() }, label: format!("rf/{id}/{}", mode.as_str()), request: current_request(case), mode });
        }
    }
    let sensitive: Value = serde_json::from_str(&std::fs::read_to_string(
        std::path::Path::new(env!("CARGO_MANIFEST_DIR")).join("tests/fixtures/rf_source_method/order_four_sensitive.request.json")).unwrap()).unwrap();
    for mode in MODES {
        out.push(Control { kind: Kind::Rf { id: "order_four_sensitive".into() }, label: format!("rf/order_four_sensitive/{}", mode.as_str()),
            request: sensitive.clone(), mode });
    }
    out
}


/// One public run under `cfg`: exact bytes, value, the replay records, and the reader verdicts.
fn control_side(c: &Control, cfg: Cfg) -> Value {
    replay::drain();
    let envelope = under(cfg, || run_linear_static_preview_value_with_mode(c.request.clone(), c.mode));
    let records = replay::drain();
    let (bytes, value) = match &envelope {
        Ok(e) => (serde_json::to_string(e).unwrap(), serde_json::to_value(e).unwrap()),
        Err(e) => (String::new(), json!({"refused": e})),
    };
    let (direct, method) = rmc::method(&c.request, c.mode, cfg.ra_off);
    let publication = match &method {
        Some(m) if value.get("source_block_recovery").is_some() => {
            let (checked, failures) = publication_check(&c.request, c.mode, &value, m);
            json!({"checked": checked, "failures": failures})
        }
        Some(_) => json!({"checked": 0, "failures": ["no source publication"]}),
        None => json!({"checked": 0, "failures": [format!("direct method not selected: {}", direct["outcome"])]}),
    };
    let invocation = json!({"request": c.request, "solver_mode": c.mode.as_str()});
    use open_pipe_stress_result_export::{physics_source as ps, reader_verdict as rv};
    let verdict = rv::validate("pressure-source", &value, if matches!(c.kind, Kind::O4 { .. }) { Some(&c.request["model"]) } else { None }, Some(&invocation));
    let validate_in = format!("{:?}", ps::validate_in(&value, Some(&invocation), ps::SourceContract::PressureV3));
    json!({"bytes": bytes, "value": value, "records": records_json(&records), "direct_outcome": direct["outcome"],
        "direct_work": direct["work"]["charged"], "publication_check": publication, "reader_verdict": verdict, "validate_in": validate_in})
}

// MJ9's public accounting (`tests/pressure_source_join/consequences.rs`, copied), as a report.
fn mj9_count(value: &Value) -> u64 {
    value.as_array().map_or(0, |a| a.len() as u64)
}
fn mj9_utf8(value: &Value) -> u64 {
    value.as_str().map_or(0, |s| s.len() as u64)
}
fn mj9_accounting(request: &Value, source: &Value) -> Vec<String> {
    let text = serde_json::to_string(request).unwrap();
    let e = open_pipe_stress_canonical_json::canonical_json_checked_v1_text(&text).unwrap().len() as u64;
    let rows = mj9_count(&source["results"]);
    let diagnostics = source["diagnostics"].as_array().cloned().unwrap_or_default();
    let diagnostic_bytes: u64 = diagnostics.iter().map(|d| mj9_utf8(&d["id"]) + mj9_utf8(&d["code"]) + mj9_utf8(&d["message"])
        + d["affected_refs"].as_array().into_iter().flatten().map(mj9_utf8).sum::<u64>()).sum();
    let model = &request["model"];
    let p = 1024 + 32 * rows + 32 * diagnostics.len() as u64 + 12 * diagnostic_bytes
        + mj9_count(&model["load_cases"]) * (32000 * mj9_count(&model["pipe_segments"]) + 64 * mj9_count(&model["nodes"]).pow(2) + 256 * rows);
    let body = &source["source_block_recovery"]["body"];
    let mut failures = Vec::new();
    let publication = body["invocation_work"]["publication_charged"].as_u64();
    if publication != Some(24 * e + p) {
        failures.push(format!("publication_charged {publication:?} != 24E + P = {}", 24 * e + p));
    }
    let cases: u64 = body["cases"].as_array().into_iter().flatten()
        .map(|c| c["work"]["charged"].as_u64().unwrap_or(0) + c["work"]["reserved_unobserved_failure"].as_u64().unwrap_or(0)).sum();
    let charged = body["invocation_work"]["charged"].as_u64();
    if charged != publication.map(|x| x + cases) {
        failures.push(format!("invocation charged {charged:?} != cases {cases} + publication {publication:?}"));
    }
    failures
}
/// MJ6's `CURRENT_SOURCE_BASIS`, read from `tests/pressure_source_join.rs`:
/// "family/name/mode" -> (request sha256, length, sha256).
fn mj6_basis(root: &std::path::Path) -> BTreeMap<String, (String, usize, String)> {
    let text = std::fs::read_to_string(root.join("core/product_physics/tests/pressure_source_join.rs")).unwrap();
    let mut out = BTreeMap::new();
    for line in text.lines().map(str::trim).filter(|l| l.starts_with("(Family::")) {
        let f: Vec<&str> = line.trim_start_matches('(').trim_end_matches("),").split(", ").collect();
        let family = if f[0] == "Family::Physics" { "physics_source" } else { "load_reference_source" };
        let mode = if f[3] == "PreviewSolverMode::SparseInteractive" { "sparse_interactive" } else { "dense_scrutiny" };
        let unq = |s: &str| s.trim_matches('"').to_owned();
        out.insert(format!("{family}/{}/{mode}", unq(f[1])), (unq(f[2]), f[4].parse().unwrap(), unq(f[5])));
    }
    out
}


#[test]
#[ignore = "replay census: the committed source controls in the four configurations (run with --features census-probe --ignored)"]
fn replay_census_source_controls() {
    let controls = source_controls();
    let started = std::time::Instant::now();
    let sides: Vec<BTreeMap<&'static str, Value>> = parallel(&controls, |c| {
        configs().into_iter().map(|cfg| {
            (cfg.name(), catch_unwind(AssertUnwindSafe(|| control_side(c, cfg))).unwrap_or_else(|p| json!({"panic": panic_text(p)})))
        }).collect()
    });
    let corpus_of = |root: &std::path::Path| -> Value {
        corpus_storage::expand(serde_json::from_str(&std::fs::read_to_string(root.join("fixtures/results/pressure_source_reader_corpus.json")).unwrap()).unwrap())
    };
    let mut roots: BTreeMap<&'static str, (std::path::PathBuf, BTreeMap<String, (String, usize, String)>, Value)> = BTreeMap::new();
    for ra in ["off", "on"] {
        let root = baseline_root(Cfg { ra_off: ra == "off", bind: false });
        let mj6 = mj6_basis(&root);
        let corpus = corpus_of(&root);
        roots.insert(ra, (root, mj6, corpus));
    }
    let mut reports = Vec::new();
    let mut o4_docs: BTreeMap<&'static str, Vec<Value>> = BTreeMap::new();
    for (c, side) in controls.iter().zip(&sides) {
        let mut report = json!({"label": c.label, "mode": c.mode.as_str()});
        let mut violations: Vec<String> = Vec::new();
        for cfg in configs() {
            let s = &side[cfg.name()];
            if let Some(p) = s.get("panic") {
                violations.push(format!("{}: panic {p}", cfg.name()));
                continue;
            }
            let (root, mj6, corpus) = &roots[cfg.ra()];
            let invocation = json!({"request": c.request, "solver_mode": c.mode.as_str()});
            let mut r = json!({"records": s["records"], "direct_outcome": s["direct_outcome"], "direct_work": s["direct_work"],
                "publication_check": s["publication_check"], "reader_verdict": s["reader_verdict"], "validate_in": s["validate_in"],
                "invocation_work": s["value"]["source_block_recovery"]["body"]["invocation_work"],
                "case_work": s["value"]["source_block_recovery"]["body"]["cases"].as_array().into_iter().flatten().map(|x| x["work"].clone()).collect::<Vec<_>>(),
                "selected": s["value"]["source_block_recovery"]["body"]["cases"].as_array().into_iter().flatten().map(|x| x["selected_method"].clone()).collect::<Vec<_>>(),
                "identity": s["value"]["producer"]["semantic_contract_id"]});
            for m in s["records"]["shadow_mismatches"].as_array().into_iter().flatten() {
                violations.push(format!("{}: shadow mismatch {m}", cfg.name()));
            }
            let bytes = s["bytes"].as_str().unwrap().as_bytes();
            if !cfg.bind {
                let mut baseline: Vec<String> = Vec::new();
                match &c.kind {
                    Kind::Raw { family, name } => {
                        let path = root.join(format!("fixtures/product_preview/pressure_source/{family}/{name}-{}.raw.json", c.mode.as_str()));
                        let committed = std::fs::read(&path).unwrap();
                        if bytes != committed.as_slice() {
                            let first = bytes.iter().zip(&committed).position(|(a, b)| a != b);
                            baseline.push(format!("bytes differ from {}: len {} vs {}, first difference {first:?}", path.display(), bytes.len(), committed.len()));
                        }
                        match mj6.get(&c.label) {
                            None => baseline.push("no MJ6 basis entry".into()),
                            Some((_, length, sha256)) => {
                                if bytes.len() != *length || sha(bytes) != *sha256 {
                                    baseline.push(format!("MJ6 basis: len {} sha {} vs pinned {length} {sha256}", bytes.len(), sha(bytes)));
                                }
                            }
                        }
                    }
                    Kind::O4 { id } => {
                        o4_docs.entry(cfg.name()).or_default().push(json!({"id": id, "solver_mode": c.mode.as_str(), "invocation": invocation, "source": s["value"]}));
                    }
                    Kind::Rf { id } => {
                        let base_id = format!("rf_source_method:{id}:{}:genuine", c.mode.as_str());
                        let bases: Vec<_> = corpus["entries"].as_array().unwrap().iter().filter(|e| e["id"] == base_id).collect();
                        if bases.len() != 1 {
                            baseline.push(format!("{} J2 bases for {base_id}", bases.len()));
                        } else {
                            if bases[0]["invocation"] != invocation {
                                baseline.push("J2 base invocation differs".into());
                            }
                            if serde_json::to_vec(&bases[0]["source"]).unwrap() != serde_json::to_vec(&s["value"]).unwrap() {
                                baseline.push("envelope bytes differ from the J2 base".into());
                            }
                        }
                    }
                }
                r["mj9"] = json!(if matches!(c.kind, Kind::Raw { .. }) { mj9_accounting(&c.request, &s["value"]) } else { vec![] });
                violations.extend(baseline.iter().map(|b| format!("{}: baseline: {b}", cfg.name())));
                r["baseline_failures"] = json!(baseline);
            } else {
                let full = &side[full_of(cfg).name()];
                if full.get("panic").is_none() {
                    let d = classify_envelope(&full["value"], &s["value"]);
                    for p in d["not_allowed"].as_array().unwrap() {
                        violations.push(format!("{}: not allowed vs full: {p}", cfg.name()));
                    }
                    r["diff_vs_full"] = d;
                    r["reader_verdict_equal_full"] = json!(full["reader_verdict"] == s["reader_verdict"] && full["validate_in"] == s["validate_in"]);
                }
                if matches!(c.kind, Kind::O4 { .. }) {
                    o4_docs.entry(cfg.name()).or_default().push(json!({"id": match &c.kind { Kind::O4 { id } => *id, _ => "" }, "solver_mode": c.mode.as_str(), "invocation": invocation, "source": s["value"]}));
                }
                if matches!(c.kind, Kind::Raw { .. }) {
                    r["mj9"] = json!(mj9_accounting(&c.request, &s["value"]));
                }
                let rel = match &c.kind {
                    Kind::Raw { family, name } => format!("controls/{}/{family}/{name}-{}.raw.json", cfg.name(), c.mode.as_str()),
                    Kind::O4 { id } => format!("controls/{}/o4/{id}-{}.json", cfg.name(), c.mode.as_str()),
                    Kind::Rf { id } => format!("controls/{}/rf/{id}-{}.json", cfg.name(), c.mode.as_str()),
                };
                write_out(&rel, bytes);
            }
            for f in r["mj9"].as_array().into_iter().flatten() {
                violations.push(format!("{}: MJ9 {f}", cfg.name()));
            }
            for f in s["publication_check"]["failures"].as_array().into_iter().flatten() {
                if !(matches!(c.kind, Kind::Raw { family: "load_reference_source", .. }) && f.as_str().is_some_and(|x| x.starts_with("direct method not selected") || x == "no source publication")) {
                    r["publication_failures_noted"] = json!(true);
                }
            }
            report[cfg.name()] = r;
        }
        report["violations"] = json!(violations);
        reports.push(report);
    }
    // The O4 document, as `o4_source_controls_are_current` writes it.
    let document = |entries: Vec<Value>| json!({"artifact": "o4-source-controls", "schema_version": "1.0.0",
        "provenance": "invented in-memory re-authorings of the committed pressure-source n05 and fields requests (O4 design section 6); test-only",
        "entries": entries});
    let mut o4 = json!({});
    for cfg in configs() {
        let text = format!("{}\n", serde_json::to_string(&document(o4_docs.remove(cfg.name()).unwrap_or_default())).unwrap());
        let committed = std::fs::read_to_string(baseline_root(full_of(cfg)).join("fixtures/product_preview/pressure_source/o4/o4_source_controls.json")).unwrap();
        o4[cfg.name()] = json!({"bytes_equal_committed": text == committed});
        if cfg.bind {
            let full_committed: Value = serde_json::from_str(&committed).unwrap();
            let mine: Value = serde_json::from_str(&text).unwrap();
            let mut paths = Vec::new();
            diff(&full_committed, &mine, "", &mut paths);
            o4[cfg.name()]["paths_vs_committed_full"] = json!(paths);
        }
        write_out(&format!("controls/{}/o4/o4_source_controls.json", cfg.name()), text.as_bytes());
    }
    let violations: Vec<Value> = reports.iter().flat_map(|r| r["violations"].as_array().unwrap().iter().map(move |v| json!([r["label"], v]))).collect();
    let summary = json!({"artifact": "replay-census-source-controls", "controls": reports.len(), "seconds": started.elapsed().as_secs_f64(),
        "o4_document": o4, "violations": violations});
    println!("REPLAY_CENSUS_CONTROLS {}", serde_json::to_string(&json!({"controls": reports.len(), "o4_document": summary["o4_document"],
        "violations": summary["violations"].as_array().unwrap().len()})).unwrap());
    write_out("controls_summary.json", serde_json::to_string_pretty(&summary).unwrap().as_bytes());
    write_out("controls_reports.json", serde_json::to_string_pretty(&json!(reports)).unwrap().as_bytes());
}
