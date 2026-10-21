//! R-A census: J7 and the committed source controls, off and on (DEL-04-08 Design
//! `source-work-nondyadic-inputs.md` §5, "Inputs" and "Records"). Compiled only under
//! the opt-in `census-probe` feature; every target is `#[ignore]`. Measurement only:
//! the 8,000,000 per-case limit, every gate and every check are unchanged, and no
//! committed fixture is written. Outputs go only under `RA_CENSUS_OUT` (skipped when
//! unset). R-A's switches are thread-local, so every run sets them on its own thread.
//! Standard claim fence applies (F-PIP-2; claims taxonomy per DEC-081).
use super::ra_method_census::{self as rmc, publication_check, records_json, under};
use super::*;
use open_pipe_stress_frame_kernel::structural::retained_api::census_probe::{self as w1probe, ra};
use std::panic::{catch_unwind, AssertUnwindSafe};


fn project_root() -> std::path::PathBuf {
    std::path::Path::new(env!("CARGO_MANIFEST_DIR")).join("../..")
}
/// Writes `bytes` to `RA_CENSUS_OUT/<rel>`; nothing when the variable is unset.
fn write_out(rel: &str, bytes: &[u8]) {
    let Some(dir) = std::env::var_os("RA_CENSUS_OUT") else { return };
    let path = std::path::PathBuf::from(dir).join(rel);
    if let Some(parent) = path.parent() {
        std::fs::create_dir_all(parent).unwrap();
    }
    std::fs::write(&path, bytes).unwrap();
}
/// `publication_check`'s result as `{"checked": n, "failures": [...]}`, on the request's
/// first load case (the one the direct method solves).
fn pub_check(request: &Value, mode: PreviewSolverMode, env: &Value, direct: &SelectedSourceRecovery) -> Value {
    let case = request["model"]["load_cases"][0]["id"].as_str().unwrap_or_default();
    let (checked, failures) = publication_check(request, mode, env, direct);
    json!({"checked": checked, "failures": failures, "case": case})
}
/// B1 and B2 tallies from a `records_json` value's row list.
fn row_tallies(records: &Value) -> Value {
    let rows = records["rows"].as_array().cloned().unwrap_or_default();
    json!({"rows_total": rows.len(), "b1_rows": rows.iter().filter(|r| r[3] == "b1").count(),
        "b2_skipped_terms": rows.iter().map(|r| r[4].as_u64().unwrap_or(0)).sum::<u64>(),
        "b2_rows_with_skips": rows.iter().filter(|r| r[4].as_u64().unwrap_or(0) > 0).count()})
}
fn strip_rows(records: &Value) -> Value {
    let mut r = records.clone();
    if let Some(o) = r.as_object_mut() {
        o.remove("rows");
        o.insert("tallies".into(), row_tallies(records));
    }
    r
}
fn panic_text(p: Box<dyn std::any::Any + Send>) -> String {
    p.downcast_ref::<String>().cloned().or_else(|| p.downcast_ref::<&str>().map(|s| s.to_string())).unwrap_or_default()
}
fn env_usize(name: &str) -> Option<usize> {
    std::env::var(name).ok().and_then(|v| v.parse().ok())
}
/// Runs `f` over `jobs` on `RA_CENSUS_THREADS` worker threads (default 1), keeping order.
fn parallel<J: Sync, T: Send>(jobs: &[J], f: impl Fn(&J) -> T + Sync) -> Vec<T> {
    let threads = env_usize("RA_CENSUS_THREADS").unwrap_or(1).max(1).min(jobs.len().max(1));
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
                        eprintln!("RA_CENSUS job {i}/{} done in {:.1}s", jobs.len(), started.elapsed().as_secs_f64());
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

/// R-A's drained records without the per-row list, plus B1/B2 tallies.
fn compact(r: &ra::Records) -> Value {
    let mut v = records_json(r);
    v.as_object_mut().unwrap().remove("rows");
    let mut declined: BTreeMap<String, u64> = BTreeMap::new();
    for row in r.rows.iter().filter(|x| x.path.starts_with("long:")) {
        *declined.entry(row.path.clone()).or_default() += 1;
    }
    v["rows_total"] = json!(r.rows.len());
    v["b1_rows"] = json!(r.rows.iter().filter(|x| x.path == "b1").count());
    v["b1_declined"] = json!(declined);
    v["b2_skipped_terms"] = json!(r.rows.iter().map(|x| x.b2_skipped_terms).sum::<u64>());
    v["b2_rows_with_skips"] = json!(r.rows.iter().filter(|x| x.b2_skipped_terms > 0).count());
    v
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
/// §5's allowance, strictly (`ra_method_census::allowed_work_change`; census review finding 1).
fn allowed_envelope_path(pointer: &str, off: &Value, on: &Value) -> bool {
    let s = segments(pointer);
    let at = |e: &Value| s.iter().try_fold(e, |v, k| match v {
        Value::Object(m) => m.get(k),
        Value::Array(x) => k.parse::<usize>().ok().and_then(|i| x.get(i)),
        _ => None,
    }).cloned().unwrap_or(Value::Null);
    super::ra_method_census::allowed_work_change(&s, off, on, &at(off), &at(on))
}
fn classify_envelope(off: &Value, on: &Value) -> Value {
    let mut paths = Vec::new();
    diff(off, on, "", &mut paths);
    let (allowed, not_allowed): (Vec<_>, Vec<_>) = paths.into_iter().partition(|p| allowed_envelope_path(p, off, on));
    json!({"allowed": allowed, "not_allowed": not_allowed})
}

// ---------------------------------------------------------------- target 1: J7 off/on

fn j7_public_checks(id: &str, run: &Run) -> Vec<String> {
    let mut failures = Vec::new();
    if let Ok(env) = &run.public {
        if !PUBLISHED.contains(&id) {
            if env.get("source_block_recovery").is_some() {
                failures.push("source publication on an unpublished case".into());
            }
            if SOURCE_IDENTITIES.iter().any(|s| env["producer"]["semantic_contract_id"] == *s) {
                failures.push("source identity on an unpublished case".into());
            }
            if env["producer"]["semantic_contract_id"] != PRESSURE_1 {
                failures.push(format!("identity {}", env["producer"]["semantic_contract_id"]));
            }
        }
    }
    let declines: Vec<String> = run.public.as_ref().map(|env| env["diagnostics"].as_array().unwrap().iter()
        .filter(|d| d["code"] == "SOURCE_BLOCK_RECOVERY_UNAVAILABLE").map(|d| d["message"].as_str().unwrap().to_owned()).collect())
        .unwrap_or_default();
    match (&run.method, declines.as_slice()) {
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

/// One side of one J7 entry: J7's `census_entry` logic without its assertions, under
/// R-A `on`, with R-A's records of the public run and of the direct method.
fn j7_side(case: &Value, request: &Value, mode: PreviewSolverMode, on: bool) -> Value {
    let id = case["id"].as_str().unwrap();
    ra::drain();
    let public = under(on, || run_linear_static_preview_value_with_mode(request.clone(), mode).map(|e| serde_json::to_value(e).unwrap()));
    let public_records = ra::drain();
    let owned = Owned::actual(request, mode);
    let method = owned.as_ref().ok().map(|o| {
        under(on, || solve_ordinary(o.input(), exact::Limits { operations: PHYSICS_SOURCE_WORK_LIMIT, ..Default::default() }, ForceScale::UNSCALED))
    });
    let run_method_records = ra::drain();
    let run = Run { public, owned, method };
    let checks = j7_public_checks(id, &run);
    let first = catch_unwind(AssertUnwindSafe(|| first_cause(&run)))
        .unwrap_or_else(|p| json!({"class": "census_unclassified", "panic": panic_text(p)}));
    let mut entry = json!({"id": id, "family": case["family"], "mode": mode.as_str(), "public": public_value(&run.public),
        "first_cause": first});
    if let (Some(Ok(m)), Ok(o)) = (&run.method, &run.owned) {
        let (n, p) = method_comparison(&references()["cases"][id], m, o);
        entry["method_only_comparison"] = json!({"rows": n, "pass": p});
    }
    // ra_method_census's direct method: its work, response and retained digests.
    let (direct, direct_method) = if matches!(run.method, Some(Ok(_))) { rmc::method(request, mode, on) } else { (Value::Null, None) };
    let direct_records = direct.get("records").cloned();
    let mut direct_summary = direct.clone();
    if let Some(o) = direct_summary.as_object_mut() {
        o.remove("records");
    }
    let publication = match (&run.public, &direct_method) {
        (Ok(env), Some(m)) if env.get("source_block_recovery").is_some() => pub_check(request, mode, env, m),
        _ => Value::Null,
    };
    let run_work = match &run.method {
        Some(Ok(m)) => json!(m.summary().work.charged),
        Some(Err(f)) => json!(f.work.charged),
        None => Value::Null,
    };
    json!({"entry": entry, "public_checks": checks, "direct": direct_summary,
        "direct_work_matches_run": direct.is_null() || direct["work"]["charged"] == run_work,
        "publication_check": publication,
        "records": {"public": compact(&public_records), "run_method": compact(&run_method_records),
            "direct_method": direct_records.as_ref().map(strip_rows)}})
}

fn committed_lines() -> BTreeMap<(String, String), String> {
    let entries = expected()["entries"].as_array().unwrap();
    let lines: Vec<&str> = EXPECTED.lines().skip(1).take(entries.len()).collect();
    entries.iter().zip(lines).map(|(e, l)| {
        ((e["id"].as_str().unwrap().to_owned(), e["mode"].as_str().unwrap().to_owned()), l.strip_suffix(',').unwrap_or(l).to_owned())
    }).collect()
}

fn j7_entry(case: &Value, mode: PreviewSolverMode, lines: &BTreeMap<(String, String), String>) -> Value {
    let id = case["id"].as_str().unwrap().to_owned();
    let result = catch_unwind(AssertUnwindSafe(|| {
        let request = current_request(case);
        (j7_side(case, &request, mode, false), j7_side(case, &request, mode, true))
    }));
    let (off, on) = match result {
        Ok(x) => x,
        Err(p) => return json!({"id": id, "mode": mode.as_str(), "panic": panic_text(p), "violations": ["census panic"]}),
    };
    let committed = expected()["entries"].as_array().unwrap().iter().find(|e| e["id"] == id && e["mode"] == mode.as_str());
    let baseline_value = committed == Some(&off["entry"]);
    let baseline_bytes = lines.get(&(id.clone(), mode.as_str().to_owned())) == Some(&serde_json::to_string(&off["entry"]).unwrap());
    let mut baseline_diff = Vec::new();
    if let Some(c) = committed {
        diff(c, &off["entry"], "", &mut baseline_diff);
    }
    let class = off["entry"]["first_cause"]["class"].as_str().unwrap_or_default().to_owned();
    let direct_selected = class.starts_with("selected");
    let published = class == "selected_published";
    let mut moved = Vec::new();
    diff(&off["entry"], &on["entry"], "", &mut moved);
    let mut violations: Vec<String> = Vec::new();
    for p in &moved {
        let ok = (direct_selected && p == "/first_cause/work/charged")
            || (published && (p == "/public/envelope_sha256" || p == "/public/diagnostics_sha256"));
        if !ok {
            violations.push(format!("entry field moved: {p}"));
        }
    }
    if direct_selected {
        for k in ["outcome", "response_digest", "retained_digest"] {
            if off["direct"][k] != on["direct"][k] {
                violations.push(format!("direct method {k} moved"));
            }
        }
    }
    for side in ["off", "on"] {
        let s = if side == "off" { &off } else { &on };
        for c in s["public_checks"].as_array().unwrap() {
            violations.push(format!("{side}: {c}"));
        }
        if let Some(f) = s["publication_check"]["failures"].as_array() {
            for c in f {
                violations.push(format!("{side}: publication check: {c}"));
            }
        }
        if s["direct_work_matches_run"] != true {
            violations.push(format!("{side}: ra_method_census::method work differs from the run's method work"));
        }
        if let Some(m) = s["entry"].get("method_only_comparison") {
            if m["rows"] != m["pass"] {
                violations.push(format!("{side}: direct-method rows outside the frozen criterion {m}"));
            }
        }
    }
    for which in ["public", "run_method", "direct_method"] {
        if let Some(m) = on["records"][which]["shadow_mismatches"].as_array() {
            for x in m {
                violations.push(format!("on: shadow mismatch ({which}): {x}"));
            }
        }
    }
    json!({"id": id, "mode": mode.as_str(), "class_off": class, "class_on": on["entry"]["first_cause"]["class"],
        "baseline_equal_value": baseline_value, "baseline_equal_bytes": baseline_bytes, "baseline_diff": baseline_diff,
        "moved_off_on": moved, "violations": violations,
        "work_off": off["entry"]["first_cause"]["work"]["charged"], "work_on": on["entry"]["first_cause"]["work"]["charged"],
        "off": off, "on": on})
}

fn j7_cases() -> Vec<&'static Value> {
    let ids: Option<BTreeSet<String>> = std::env::var("RA_CENSUS_IDS").ok().map(|s| s.split(',').map(str::to_owned).collect());
    let mut cases: Vec<&Value> = inputs()["cases"].as_array().unwrap().iter()
        .filter(|c| ids.as_ref().map_or(true, |ids| ids.contains(c["id"].as_str().unwrap()))).collect();
    if let Some(n) = env_usize("RA_CENSUS_LIMIT") {
        cases.truncate(n);
    }
    cases
}

#[test]
#[ignore = "R-A census: J7 off/on (run with --features census-probe --ignored)"]
fn ra_census_j7_off_on() {
    let lines = committed_lines();
    let jobs: Vec<(&Value, PreviewSolverMode)> = j7_cases().into_iter().flat_map(|c| MODES.map(|m| (c, m))).collect();
    let started = std::time::Instant::now();
    let results = parallel(&jobs, |(case, mode)| j7_entry(case, *mode, &lines));
    let mut counts_off: BTreeMap<String, usize> = BTreeMap::new();
    let mut counts_on: BTreeMap<String, usize> = BTreeMap::new();
    let mut moved_fields: BTreeMap<String, BTreeMap<String, usize>> = BTreeMap::new();
    let (mut baseline_value, mut baseline_bytes, mut violating) = (0, 0, 0);
    let mut violations = Vec::new();
    let mut selected = Vec::new();
    for r in &results {
        *counts_off.entry(r["class_off"].as_str().unwrap_or("panic").to_owned()).or_default() += 1;
        *counts_on.entry(r["class_on"].as_str().unwrap_or("panic").to_owned()).or_default() += 1;
        baseline_value += usize::from(r["baseline_equal_value"] == true);
        baseline_bytes += usize::from(r["baseline_equal_bytes"] == true);
        let class = r["class_off"].as_str().unwrap_or("panic").to_owned();
        for p in r["moved_off_on"].as_array().into_iter().flatten() {
            *moved_fields.entry(class.clone()).or_default().entry(p.as_str().unwrap().to_owned()).or_default() += 1;
        }
        let v = r["violations"].as_array().unwrap();
        if !v.is_empty() {
            violating += 1;
            violations.push(json!({"id": r["id"], "mode": r["mode"], "violations": v}));
        }
        if class.starts_with("selected") {
            selected.push(json!({"id": r["id"], "mode": r["mode"], "class": class, "work_off": r["work_off"], "work_on": r["work_on"],
                "b1_rows_direct_on": r["on"]["records"]["direct_method"]["tallies"]["b1_rows"],
                "row_paths_direct_on": r["on"]["records"]["direct_method"]["row_paths"],
                "b2_skipped_terms_direct_on": r["on"]["records"]["direct_method"]["tallies"]["b2_skipped_terms"],
                "b1_rows_public_on": r["on"]["records"]["public"]["b1_rows"], "b2_skipped_terms_public_on": r["on"]["records"]["public"]["b2_skipped_terms"],
                "publication_check_on": r["on"]["publication_check"],
                "shadow_checked_on": [r["on"]["records"]["public"]["shadow_checked"], r["on"]["records"]["run_method"]["shadow_checked"], r["on"]["records"]["direct_method"]["shadow_checked"]],
                "public_evaluations_on": r["on"]["records"]["public"]["evaluations"]}));
        }
    }
    let mut committed_classes: BTreeMap<String, usize> = BTreeMap::new();
    for e in expected()["entries"].as_array().unwrap() {
        *committed_classes.entry(e["first_cause"]["class"].as_str().unwrap().to_owned()).or_default() += 1;
    }
    let summary = json!({"artifact": "ra-census-j7-off-on", "entries": results.len(), "seconds": started.elapsed().as_secs_f64(),
        "switches": {"w1": format!("{:?}", rmc::w1_production()), "off": format!("{:?}", rmc::ra_switches(false)), "on": format!("{:?}", rmc::ra_switches(true))},
        "baseline_equal_value": baseline_value, "baseline_equal_bytes": baseline_bytes,
        "classes_off": counts_off, "classes_on": counts_on, "classes_committed": committed_classes,
        "moved_fields_by_class": moved_fields, "entries_with_violations": violating, "violations": violations, "selected": selected});
    println!("RA_CENSUS_J7 {}", serde_json::to_string(&json!({"entries": summary["entries"], "baseline_equal_value": baseline_value,
        "baseline_equal_bytes": baseline_bytes, "classes_off": summary["classes_off"], "classes_on": summary["classes_on"],
        "moved_fields_by_class": summary["moved_fields_by_class"], "entries_with_violations": violating})).unwrap());
    write_out("j7_off_on_summary.json", serde_json::to_string_pretty(&summary).unwrap().as_bytes());
    let lines: Vec<String> = results.iter().map(|r| serde_json::to_string(r).unwrap()).collect();
    write_out("j7_off_on_entries.jsonl", (lines.join("\n") + "\n").as_bytes());
}

// ------------------------------------------------- target 2: J7 metered control, R-A on

/// `j7_rf_census_metered_charges_cover_counted_operations`'s logic under `sw` (and W1's
/// production switches), as a report: every violation is listed, none is asserted.
fn metered(sw: ra::Switches) -> Value {
    use open_pipe_stress_frame_kernel::structural::exact_boundary::exact_operation_count as count;
    w1probe::with(rmc::w1_production(), || ra::with(sw, || {
        count::reset();
        ra::drain();
        let no_attempt: BTreeSet<&str> = expected()["entries"].as_array().unwrap().iter()
            .filter(|e| matches!(e["first_cause"]["class"].as_str(), Some("hash001_unsafe_integral_float" | "ordinary_axis_gate")))
            .map(|e| e["id"].as_str().unwrap()).collect();
        let (mut attempts, mut replays, mut skipped) = (0usize, 0usize, 0usize);
        let (mut attempt_charged, mut attempt_counted, mut replay_charged, mut replay_counted) = (0u64, 0u64, 0u64, 0u64);
        let mut violations: Vec<String> = Vec::new();
        let mut shadow_checked = 0u64;
        let mut shadow_mismatches: Vec<String> = Vec::new();
        let mut b1_rows = 0usize;
        let mut b2_skipped = 0u64;
        let cases = j7_cases();
        for case in &cases {
            let id = case["id"].as_str().unwrap();
            let request = current_request(case);
            for mode in MODES {
                let at = format!("{id} {}", mode.as_str());
                let Ok(owned) = Owned::actual(&request, mode) else {
                    if !no_attempt.contains(id) {
                        violations.push(format!("{at}: an in-family case without an attempt"));
                    }
                    skipped += 1;
                    continue;
                };
                if no_attempt.contains(id) {
                    violations.push(format!("{at}: a pinned no-attempt case reached the method"));
                }
                let before = count::operations();
                let result = solve_ordinary(owned.input(), exact::Limits { operations: PHYSICS_SOURCE_WORK_LIMIT, ..Default::default() }, ForceScale::UNSCALED);
                let counted = count::operations() - before;
                let charged = match &result { Ok(m) => m.summary().work.charged, Err(f) => f.work.charged } as u64;
                if charged < counted {
                    violations.push(format!("{at}: attempt charged {charged} < {counted} counted operations"));
                }
                attempts += 1;
                attempt_charged += charged;
                attempt_counted += counted;
                if let Ok(mut m) = result {
                    let (before, ledger) = (count::operations(), m.summary().work.charged);
                    match m.replay_against(owned.input()) {
                        Err(f) => violations.push(format!("{at}: replay on the selection's ledger: {f:?}")),
                        Ok(()) => {
                            let counted = count::operations() - before;
                            let charged = (m.summary().work.charged - ledger) as u64;
                            if charged < counted {
                                violations.push(format!("{at}: replay charged {charged} < {counted} counted operations"));
                            }
                            replays += 1;
                            replay_charged += charged;
                            replay_counted += counted;
                        }
                    }
                }
                let r = ra::drain();
                shadow_checked += r.shadow_checked;
                shadow_mismatches.extend(r.shadow_mismatches.iter().map(|m| format!("{at}: {m}")));
                b1_rows += r.rows.iter().filter(|x| x.path == "b1").count();
                b2_skipped += r.rows.iter().map(|x| x.b2_skipped_terms).sum::<u64>();
            }
        }
        let totals = count::totals();
        if attempts + skipped != 2 * cases.len() {
            violations.push(format!("attempts {attempts} + skipped {skipped} != {}", 2 * cases.len()));
        }
        if replays == 0 {
            violations.push("no selected attempt was replayed".into());
        }
        if totals.shortfalls() != 0 {
            violations.push(format!("a Work call was charged less than it executed: {totals:?}"));
        }
        if !(totals.mul.calls > 0 && totals.pairs > 0) {
            violations.push(format!("no metered multiplication ran: {totals:?}"));
        }
        if !(totals.mul.min_slack.is_some_and(|s| s >= 0) && totals.add.min_slack.is_some_and(|s| s >= 0)) {
            violations.push(format!("negative or absent min slack: {totals:?}"));
        }
        if !totals.min_pair_slack.is_some_and(|s| s >= 0) {
            violations.push(format!("negative or absent pair slack: {totals:?}"));
        }
        json!({"switches": format!("{sw:?}"), "cases": cases.len(), "attempts": attempts, "replays": replays, "no_attempt": skipped,
            "attempt_charged": attempt_charged, "attempt_counted": attempt_counted, "replay_charged": replay_charged, "replay_counted": replay_counted,
            "shortfalls": totals.shortfalls(), "totals": format!("{totals:?}"), "b1_rows": b1_rows, "b2_skipped_terms": b2_skipped,
            "shadow_checked": shadow_checked, "shadow_mismatches": shadow_mismatches, "violations": violations})
    }))
}

#[test]
#[ignore = "R-A census: J7 metered control under R-A on (run with --features census-probe --ignored)"]
fn ra_census_j7_metered_control() {
    // As briefed (`under(true, ..)`: B1, B2, records and the shadow check), and with the
    // shadow check off: the shadow's long re-evaluation runs on a private ledger that no
    // case ledger reads, but the thread's operation counter counts its calls.
    // The switch-off run is the reference for the charged totals.
    let variants = [rmc::ra_switches(true), ra::Switches { shadow: false, ..rmc::ra_switches(true) }, rmc::ra_switches(false)];
    let started = std::time::Instant::now();
    let reports = parallel(&variants, |sw| metered(*sw));
    let doc = json!({"artifact": "ra-census-j7-metered-control", "seconds": started.elapsed().as_secs_f64(), "variants": reports});
    for r in &reports {
        let mut line = r.clone();
        line.as_object_mut().unwrap().remove("totals");
        println!("RA_CENSUS_METERED {}", serde_json::to_string(&line).unwrap());
    }
    write_out("j7_metered_control.json", serde_json::to_string_pretty(&doc).unwrap().as_bytes());
}

// --------------------------------------------------- target 3: committed source controls

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

/// One public run under R-A `on`: exact bytes, value, R-A's records, and the direct method.
fn control_side(c: &Control, on: bool) -> Value {
    ra::drain();
    let envelope = under(on, || run_linear_static_preview_value_with_mode(c.request.clone(), c.mode));
    let records = ra::drain();
    let (bytes, value) = match &envelope {
        Ok(e) => (serde_json::to_string(e).unwrap(), serde_json::to_value(e).unwrap()),
        Err(e) => (String::new(), json!({"refused": e})),
    };
    let (direct, method) = rmc::method(&c.request, c.mode, on);
    let publication = match &method {
        Some(m) if value.get("source_block_recovery").is_some() => pub_check(&c.request, c.mode, &value, m),
        Some(_) => json!({"checked": 0, "failures": ["no source publication"]}),
        None => json!({"checked": 0, "failures": [format!("direct method not selected: {}", direct["outcome"])]}),
    };
    let invocation = json!({"request": c.request, "solver_mode": c.mode.as_str()});
    use open_pipe_stress_result_export::{physics_source as ps, reader_verdict as rv};
    let verdict = rv::validate("pressure-source", &value, if matches!(c.kind, Kind::O4 { .. }) { Some(&c.request["model"]) } else { None }, Some(&invocation));
    let validate_in = format!("{:?}", ps::validate_in(&value, Some(&invocation), ps::SourceContract::PressureV3));
    let mut direct_summary = direct.clone();
    direct_summary.as_object_mut().unwrap().remove("records");
    json!({"bytes": bytes, "value": value, "records": records_json(&records), "records_compact": compact(&records),
        "direct": direct_summary, "direct_records": direct.get("records").map(strip_rows),
        "publication_check": publication, "reader_verdict": verdict, "validate_in": validate_in})
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
fn mj6_basis() -> BTreeMap<String, (String, usize, String)> {
    let text = std::fs::read_to_string(std::path::Path::new(env!("CARGO_MANIFEST_DIR")).join("tests/pressure_source_join.rs")).unwrap();
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

fn side_summary(s: &Value) -> Value {
    json!({"records": s["records_compact"], "direct": s["direct"], "direct_records": s["direct_records"], "publication_check": s["publication_check"],
        "reader_verdict": s["reader_verdict"], "validate_in": s["validate_in"]})
}

#[test]
#[ignore = "R-A census: the committed source controls off/on (run with --features census-probe --ignored)"]
fn ra_census_source_controls() {
    let controls = source_controls();
    let started = std::time::Instant::now();
    let sides = parallel(&controls, |c| {
        catch_unwind(AssertUnwindSafe(|| (control_side(c, false), control_side(c, true))))
            .unwrap_or_else(|p| { let e = json!({"panic": panic_text(p)}); (e.clone(), e) })
    });
    let mj6 = mj6_basis();
    static CORPUS: std::sync::OnceLock<Value> = std::sync::OnceLock::new();
    let corpus = CORPUS.get_or_init(|| corpus_storage::expand(serde_json::from_str(J2).unwrap()));
    let mut reports = Vec::new();
    let mut o4_off = Vec::new();
    let mut o4_on = Vec::new();
    for (c, (off, on)) in controls.iter().zip(&sides) {
        let mut baseline: Vec<String> = Vec::new();
        let mut report = json!({"label": c.label, "mode": c.mode.as_str()});
        if off.get("panic").is_some() {
            report["panic"] = off["panic"].clone();
            reports.push(report);
            continue;
        }
        let invocation = json!({"request": c.request, "solver_mode": c.mode.as_str()});
        match &c.kind {
            Kind::Raw { family, name } => {
                let path = project_root().join(format!("fixtures/product_preview/pressure_source/{family}/{name}-{}.raw.json", c.mode.as_str()));
                let committed = std::fs::read(&path).unwrap();
                let bytes = off["bytes"].as_str().unwrap().as_bytes();
                if bytes != committed.as_slice() {
                    let first = bytes.iter().zip(&committed).position(|(a, b)| a != b);
                    baseline.push(format!("off bytes differ from {}: len {} vs {}, first difference {first:?}", path.display(), bytes.len(), committed.len()));
                }
                match mj6.get(&c.label) {
                    None => baseline.push("no MJ6 basis entry".into()),
                    Some((request_sha, length, sha256)) => {
                        let request_bytes = std::fs::read(project_root().join(format!("fixtures/product_preview/pressure_source/{family}/{name}.request.json"))).unwrap();
                        if sha(&request_bytes) != *request_sha {
                            baseline.push("MJ6 request sha256".into());
                        }
                        if bytes.len() != *length || sha(bytes) != *sha256 {
                            baseline.push(format!("MJ6 basis: off len {} sha {} vs pinned {length} {sha256}", bytes.len(), sha(bytes)));
                        }
                    }
                }
                let on_bytes = on["bytes"].as_str().unwrap().as_bytes();
                report["mj6_on"] = json!({"length": on_bytes.len(), "sha256": sha(on_bytes),
                    "pinned": mj6.get(&c.label).map(|(_, l, s)| json!([l, s]))});
                report["mj9_off"] = json!(mj9_accounting(&c.request, &off["value"]));
                report["mj9_on"] = json!(mj9_accounting(&c.request, &on["value"]));
                write_out(&format!("controls/on/{family}/{name}-{}.raw.json", c.mode.as_str()), on_bytes);
            }
            Kind::O4 { id } => {
                o4_off.push(json!({"id": id, "solver_mode": c.mode.as_str(), "invocation": invocation, "source": off["value"]}));
                o4_on.push(json!({"id": id, "solver_mode": c.mode.as_str(), "invocation": invocation, "source": on["value"]}));
                let eligible = json!({"ok": true, "eligible": true, "findings": []});
                report["o4_verdict_off_eligible"] = json!(off["reader_verdict"] == eligible);
                report["o4_verdict_on_eligible"] = json!(on["reader_verdict"] == eligible);
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
                    if serde_json::to_vec(&bases[0]["source"]).unwrap() != serde_json::to_vec(&off["value"]).unwrap() {
                        baseline.push("off envelope bytes differ from the J2 base".into());
                    }
                    let mut against_j2 = Vec::new();
                    diff(&bases[0]["source"], &on["value"], "", &mut against_j2);
                    report["on_vs_j2_paths"] = json!(against_j2.len());
                }
                write_out(&format!("controls/on/rf/{id}-{}.json", c.mode.as_str()), on["bytes"].as_str().unwrap().as_bytes());
            }
        }
        report["baseline_failures"] = json!(baseline);
        report["diff_on_vs_off"] = classify_envelope(&off["value"], &on["value"]);
        report["selected_off"] = json!(off["value"]["source_block_recovery"]["body"]["cases"].as_array().into_iter().flatten()
            .map(|x| x["selected_method"].clone()).collect::<Vec<_>>());
        report["selected_on"] = json!(on["value"]["source_block_recovery"]["body"]["cases"].as_array().into_iter().flatten()
            .map(|x| x["selected_method"].clone()).collect::<Vec<_>>());
        report["work_off"] = off["value"]["source_block_recovery"]["body"]["invocation_work"].clone();
        report["work_on"] = on["value"]["source_block_recovery"]["body"]["invocation_work"].clone();
        report["case_work_off"] = json!(off["value"]["source_block_recovery"]["body"]["cases"].as_array().into_iter().flatten().map(|x| x["work"].clone()).collect::<Vec<_>>());
        report["case_work_on"] = json!(on["value"]["source_block_recovery"]["body"]["cases"].as_array().into_iter().flatten().map(|x| x["work"].clone()).collect::<Vec<_>>());
        report["reader_verdict_equal_off_on"] = json!(off["reader_verdict"] == on["reader_verdict"] && off["validate_in"] == on["validate_in"]);
        report["off"] = side_summary(off);
        report["on"] = side_summary(on);
        report["on_rows"] = on["records"]["rows"].clone();
        reports.push(report);
    }
    // The O4 document, as `o4_source_controls_are_current` writes it.
    let document = |entries: Vec<Value>| json!({"artifact": "o4-source-controls", "schema_version": "1.0.0",
        "provenance": "invented in-memory re-authorings of the committed pressure-source n05 and fields requests (O4 design section 6); test-only",
        "entries": entries});
    let o4_off_text = format!("{}\n", serde_json::to_string(&document(o4_off)).unwrap());
    let o4_on_text = format!("{}\n", serde_json::to_string(&document(o4_on)).unwrap());
    let o4_committed = std::fs::read_to_string(project_root().join("fixtures/product_preview/pressure_source/o4/o4_source_controls.json")).unwrap();
    let o4_off_value: Value = serde_json::from_str(&o4_off_text).unwrap();
    let o4_on_value: Value = serde_json::from_str(&o4_on_text).unwrap();
    let o4_committed_value: Value = serde_json::from_str(&o4_committed).unwrap();
    let mut o4_doc_paths = Vec::new();
    diff(&o4_off_value, &o4_on_value, "", &mut o4_doc_paths);
    write_out("controls/on/o4/o4_source_controls.json", o4_on_text.as_bytes());
    let o4 = json!({"off_bytes_equal_committed": o4_off_text == o4_committed, "off_value_equal_committed": o4_off_value == o4_committed_value,
        "on_bytes_equal_committed": o4_on_text == o4_committed, "document_paths_on_vs_off": o4_doc_paths});
    // Totals.
    let mut not_allowed = Vec::new();
    let mut baseline_failures = Vec::new();
    let mut publication_on = Vec::new();
    let mut shadow = Vec::new();
    for r in &reports {
        let l = r["label"].as_str().unwrap();
        if let Some(p) = r.get("panic") {
            baseline_failures.push(json!([l, format!("panic {p}")]));
            continue;
        }
        for p in r["diff_on_vs_off"]["not_allowed"].as_array().unwrap() {
            not_allowed.push(json!([l, p]));
        }
        for p in r["baseline_failures"].as_array().unwrap() {
            baseline_failures.push(json!([l, p]));
        }
        let (off_pc, on_pc) = (&r["off"]["publication_check"], &r["on"]["publication_check"]);
        if on_pc["failures"].as_array().is_some_and(|a| !a.is_empty()) {
            publication_on.push(json!({"label": l, "on": on_pc, "same_as_off": off_pc == on_pc}));
        }
        for m in r["on"]["records"]["shadow_mismatches"].as_array().into_iter().flatten()
            .chain(r["on"]["direct_records"]["shadow_mismatches"].as_array().into_iter().flatten()) {
            shadow.push(json!([l, m]));
        }
    }
    let table: Vec<Value> = reports.iter().filter(|r| r.get("panic").is_none()).map(|r| json!({
        "label": r["label"], "allowed": r["diff_on_vs_off"]["allowed"].as_array().unwrap().len(),
        "not_allowed": r["diff_on_vs_off"]["not_allowed"].as_array().unwrap().len(),
        "invocation_charged_off": r["work_off"]["charged"], "invocation_charged_on": r["work_on"]["charged"],
        "publication_charged_off": r["work_off"]["publication_charged"], "publication_charged_on": r["work_on"]["publication_charged"],
        "b1_rows_public_on": r["on"]["records"]["b1_rows"], "rows_public_on": r["on"]["records"]["rows_total"],
        "b2_skipped_terms_public_on": r["on"]["records"]["b2_skipped_terms"], "b1_declined_public_on": r["on"]["records"]["b1_declined"],
        "evaluations_public_on": r["on"]["records"]["evaluations"], "shadow_checked_public_on": r["on"]["records"]["shadow_checked"],
        "direct_outcome_on": r["on"]["direct"]["outcome"], "direct_work_off": r["off"]["direct"]["work"]["charged"], "direct_work_on": r["on"]["direct"]["work"]["charged"],
        "direct_retained_digest_equal": r["off"]["direct"]["retained_digest"] == r["on"]["direct"]["retained_digest"],
        "direct_response_digest_equal": r["off"]["direct"]["response_digest"] == r["on"]["direct"]["response_digest"],
        "publication_check_on": r["on"]["publication_check"]["checked"], "publication_check_on_failures": r["on"]["publication_check"]["failures"].as_array().map_or(0, Vec::len),
        "publication_check_off": r["off"]["publication_check"]["checked"], "publication_check_off_failures": r["off"]["publication_check"]["failures"].as_array().map_or(0, Vec::len),
        "b1_rows_direct_on": r["on"]["direct_records"]["tallies"]["b1_rows"], "b2_skipped_terms_direct_on": r["on"]["direct_records"]["tallies"]["b2_skipped_terms"],
        "reader_verdict_equal_off_on": r["reader_verdict_equal_off_on"], "selected_equal": r["selected_off"] == r["selected_on"],
        "mj9_off": r.get("mj9_off"), "mj9_on": r.get("mj9_on"),
    })).collect();
    let summary = json!({"artifact": "ra-census-source-controls", "controls": reports.len(), "seconds": started.elapsed().as_secs_f64(),
        "baseline_failures": baseline_failures, "not_allowed": not_allowed, "o4_document": o4,
        "publication_check_on_failures": publication_on, "shadow_mismatches": shadow, "table": table});
    println!("RA_CENSUS_CONTROLS {}", serde_json::to_string(&json!({"controls": reports.len(), "baseline_failures": summary["baseline_failures"],
        "not_allowed": summary["not_allowed"].as_array().unwrap().len(), "o4_document": {"off_bytes_equal_committed": o4["off_bytes_equal_committed"]},
        "publication_check_on_failures": summary["publication_check_on_failures"].as_array().unwrap().len(),
        "shadow_mismatches": summary["shadow_mismatches"].as_array().unwrap().len()})).unwrap());
    write_out("controls_summary.json", serde_json::to_string_pretty(&summary).unwrap().as_bytes());
    write_out("controls_reports.json", serde_json::to_string_pretty(&json!(reports)).unwrap().as_bytes());
}
