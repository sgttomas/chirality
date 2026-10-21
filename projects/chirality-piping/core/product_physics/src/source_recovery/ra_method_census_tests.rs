//! R-A census, method level (DEL-04-08 Design `source-work-nondyadic-inputs.md` §5,
//! "Newly selected cases"): the direct method entry J7 uses, run with R-A's census
//! switches off and on, and the publication check of a selected envelope against the
//! method's projections and the Rust reader. Compiled only under the opt-in
//! `census-probe` feature; every census target is `#[ignore]`. Measurement only: the
//! 8,000,000 per-case limit and every check are unchanged. Every model is invented.
//! Standard claim fence applies (F-PIP-2; claims taxonomy per DEC-081).
use super::*;
use open_pipe_stress_frame_kernel::structural::retained_api::census_probe::{self as w1probe, ra};

/// W1's census switches at their production values (corner 1 on, every counterfactual
/// off), which a `census-probe` build does not default to.
pub(crate) fn w1_production() -> w1probe::Switches {
    w1probe::Switches { corner1: true, ..Default::default() }
}
/// R-A's switches for one side of the census. Records are kept on both sides.
/// `RA_CENSUS_ON=b1` or `=b2` turns on only that part, for the attribution runs.
pub(crate) fn ra_switches(on: bool) -> ra::Switches {
    let part = std::env::var("RA_CENSUS_ON").unwrap_or_default();
    ra::Switches { b1: on && part != "b2", b2: on && part != "b1", record: true, shadow: on }
}
/// Runs `f` on this thread under W1's production switches and R-A's `on` setting.
pub(crate) fn under<T>(on: bool, f: impl FnOnce() -> T) -> T {
    w1probe::with(w1_production(), || ra::with(ra_switches(on), f))
}
/// The census's record of the drained R-A probe.
pub(crate) fn records_json(r: &ra::Records) -> Value {
    let sites: serde_json::Map<String, Value> = r.sites.iter()
        .map(|(k, s)| (k.clone(), json!({"charged": s.charged, "charges": s.charges, "pairs": s.pairs, "rejected": s.rejected})))
        .collect();
    let mut paths: BTreeMap<String, u64> = BTreeMap::new();
    for row in &r.rows {
        *paths.entry(format!("{}:{}", row.kind, row.path)).or_default() += 1;
    }
    json!({"evaluations": r.evaluations, "sites": sites, "row_paths": paths,
        "rows": r.rows.iter().map(|x| json!([x.evaluation, x.index, x.kind, x.path, x.b2_skipped_terms, x.charged])).collect::<Vec<_>>(),
        "b2_outside_window": r.b2_outside_window, "b2_disabled": r.b2_disabled,
        "shadow_checked": r.shadow_checked, "shadow_mismatches": r.shadow_mismatches})
}
/// Every retained Ratio's terms and every retained projection, bit for bit, without work.
fn retained_digest(m: &SelectedSourceRecovery) -> String {
    let mut h = Sha256::new();
    let r = m.retained();
    let mut ratio = |x: &exact::Ratio| {
        for t in x.numerator_terms().iter().chain(std::iter::once(&f64::NAN)).chain(x.denominator_terms()) {
            h.update(t.to_bits().to_le_bytes());
        }
        h.update(b"|");
    };
    r.ratios().iter().for_each(&mut ratio);
    r.response().displacements().iter().for_each(&mut ratio);
    r.response().reactions().iter().for_each(&mut ratio);
    for p in r.projections() {
        h.update(format!("{p:?}").as_bytes());
    }
    for p in r.response().projections() {
        h.update(format!("{p:?}").as_bytes());
    }
    format!("{:x}", h.finalize())
}
/// The direct method on one request and mode, at the unchanged limit, under `on`.
/// Returns its record and, when selected, the method itself for the publication check.
pub(crate) fn method(raw: &Value, mode: PreviewSolverMode, on: bool) -> (Value, Option<SelectedSourceRecovery>) {
    let owned = match Owned::actual(raw, mode) {
        Ok(o) => o,
        Err(e) => return (json!({"outcome": "input_not_ready", "error": e}), None),
    };
    let result = under(on, || solve_ordinary(owned.input(), exact::Limits { operations: PHYSICS_SOURCE_WORK_LIMIT, ..Default::default() }, ForceScale::UNSCALED));
    let records = records_json(&ra::drain());
    match result {
        Ok(m) => (json!({"outcome": "selected", "work": work_json(&m.summary().work), "response_digest": response_digest(&m),
            "retained_digest": retained_digest(&m), "records": records}), Some(m)),
        Err(f) => (json!({"outcome": "declined", "stage": f.stage, "helper_stage": format!("{:?}", f.helper_stage),
            "error": format!("{:?}", f.error), "work": work_json(&f.work), "records": records}), None),
    }
}
/// A published source envelope against the switch-on method: the Rust reader's verdict and
/// transport check, and every published projection's value bits (and its row's value) equal
/// to the method's projection. The direct method solves the request's first load case only
/// (`Owned::actual`), so `load_case` names the load case whose projections are compared (each
/// functional id is `source-functional:<byte length>:<case>:<index>`); the reader runs on the whole
/// envelope. Returns the projections checked and the failures.
pub(crate) fn publication_check(request: &Value, mode: PreviewSolverMode, env: &Value, direct: &SelectedSourceRecovery) -> (usize, Vec<String>) {
    let first = request["model"]["load_cases"][0]["id"].as_str().unwrap_or_default().to_owned();
    publication_check_case(request, mode, env, direct, &first)
}
/// [`publication_check`] for the named load case.
pub(crate) fn publication_check_case(request: &Value, mode: PreviewSolverMode, env: &Value, direct: &SelectedSourceRecovery, load_case: &str) -> (usize, Vec<String>) {
    use open_pipe_stress_result_export::physics_source as ps;
    let mut failures = Vec::new();
    let mut checked = 0usize;
    let invocation = json!({"request": request, "solver_mode": mode.as_str()});
    let verdict = ps::validate_in(env, Some(&invocation), ps::SourceContract::PressureV3);
    if verdict != Ok(true) {
        failures.push(format!("reader verdict {verdict:?}"));
    }
    if let Err(e) = ps::validate_transport_metadata_in(env, ps::SourceContract::PressureV3) {
        failures.push(format!("transport metadata {e:?}"));
    }
    let projections = direct.retained().projections();
    for case in env["source_block_recovery"]["body"]["cases"].as_array().into_iter().flatten() {
        for p in case["projections"].as_array().into_iter().flatten() {
            let fid = p["functional_id"].as_str().unwrap_or_default();
            // `source-functional:<byte length>:<case id>:<index>`; the case id may contain `:`.
            let parsed = fid.strip_prefix("source-functional:").and_then(|rest| {
                let (len, rest) = rest.split_once(':')?;
                let len: usize = len.parse().ok()?;
                let (case, index) = (rest.get(..len)?, rest.get(len..)?.strip_prefix(':')?);
                Some((case, index.parse::<usize>().ok()?))
            });
            if parsed.is_some_and(|(case, _)| case != load_case) {
                continue;
            }
            let Some(index) = parsed.map(|(_, i)| i) else {
                failures.push(format!("{fid}: unparsed functional id"));
                continue;
            };
            let Some(value) = projections.get(index).map(|q| q.value()) else {
                failures.push(format!("{fid}: no method projection"));
                continue;
            };
            checked += 1;
            if p["value_bits"] != format!("{:016x}", value.to_bits()) {
                failures.push(format!("{fid}: value bits"));
            }
            let q = &projections[index];
            let bits = |v: &Value| v.as_f64().map(f64::to_bits);
            if bits(&p["interval"][0]) != Some(q.interval()[0].to_bits()) || bits(&p["interval"][1]) != Some(q.interval()[1].to_bits())
                || bits(&p["absolute_error_bound"]) != Some(q.absolute_error_bound().to_bits())
                || bits(&p["relative_error_bound"]) != Some(q.relative_error_bound().to_bits())
            {
                failures.push(format!("{fid}: interval or bounds"));
            }
            if let Some(rid) = p["result_id"].as_str() {
                let row = env["results"].as_array().and_then(|rs| rs.iter().find(|r| r["id"] == rid));
                if row.and_then(|r| r["value"].as_f64()).map(f64::to_bits) != Some(value.to_bits()) {
                    failures.push(format!("{fid}: row {rid}"));
                }
            }
        }
    }
    if checked == 0 {
        failures.push("no published projection was checked".into());
    }
    (checked, failures)
}

/// §5's allowance, strictly: the work counters R-A moves (`charged` under a `work` or
/// `invocation_work` object, and `invocation_work.publication_charged`), the two hashes that
/// bind them (`publication_sha256`, `receipt_sha256`), and a source-block diagnostic's message
/// whose text differs only in those counters as printed (`charged: N`, `rejected: N`,
/// `publication_charged: N`). Limits, every other hash and digest, and every other number stay.
pub(crate) const WORK_CODES: [&str; 3] = ["SOURCE_BLOCK_RECOVERY_SELECTED", "SOURCE_BLOCK_RECOVERY_UNAVAILABLE", "SOURCE_BLOCK_RECOVERY_FINALIZATION_FAILED"];
pub(crate) fn mask_work(s: &str) -> String {
    let mut out = String::with_capacity(s.len());
    let mut rest = s;
    'scan: while !rest.is_empty() {
        for key in ["publication_charged: ", "charged: ", "rejected: "] {
            if let Some(tail) = rest.strip_prefix(key) {
                let digits = tail.bytes().take_while(u8::is_ascii_digit).count();
                if digits > 0 {
                    out.push_str(key);
                    out.push('#');
                    rest = &tail[digits..];
                    continue 'scan;
                }
            }
        }
        let ch = rest.chars().next().unwrap();
        out.push(ch);
        rest = &rest[ch.len_utf8()..];
    }
    out
}
pub(crate) fn allowed_work_change(path: &[String], off: &Value, on: &Value, a: &Value, b: &Value) -> bool {
    let n = path.len();
    let last = path.last().map(String::as_str).unwrap_or_default();
    let parent = if n >= 2 { path[n - 2].as_str() } else { "" };
    if (last == "charged" && (parent == "work" || parent == "invocation_work")) || (last == "publication_charged" && parent == "invocation_work") {
        return a.is_u64() && b.is_u64();
    }
    if last == "publication_sha256" || last == "receipt_sha256" {
        return true;
    }
    if n == 3 && path[0] == "diagnostics" && path[2] == "message" {
        let code = |e: &Value| path[1].parse::<usize>().ok().and_then(|i| e["diagnostics"][i]["code"].as_str().map(str::to_owned));
        return code(off).is_some_and(|c| WORK_CODES.contains(&c.as_str())) && code(off) == code(on)
            && a.as_str().zip(b.as_str()).is_some_and(|(x, y)| mask_work(x) == mask_work(y));
    }
    false
}
