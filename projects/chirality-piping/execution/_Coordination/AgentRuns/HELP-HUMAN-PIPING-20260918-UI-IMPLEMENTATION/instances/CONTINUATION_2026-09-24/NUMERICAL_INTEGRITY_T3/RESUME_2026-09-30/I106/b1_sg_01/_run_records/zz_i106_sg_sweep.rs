//! I106 B1 SG (disposable copies only, never committed): I61's U3 grant-2 sweep
//! (`R/I61/u3_grant2_01/_run_records/zz_i61_u3g2_sweep.rs`, as rerun by I61's u9_g8_01), adapted
//! to B1 in one respect only: T-12's notices. A permitted multi-case invocation whose W1 work ran
//! and fell back publishes the ordinary bytes plus one N1 notice per case in A, in request order.
//! `notice` is still exactly one such notice (the only form at c = 1, so every c = 1 row reads as
//! I61's harness reads it); `notice_x<k>` is k >= 2 of them. Every other line is I61's.
//! Every request-shaped fixture through every public route, in both modes. For the retained
//! entries it records the one publication's bytes, the build status, G-A's first refusing
//! clause and the private W1 result, and classifies the Direct publication: `exact` (the
//! value route's bytes), `notice` / `notice_x<k>` (those bytes plus k N1 notices after the
//! ordinary diagnostics) or `successor` (a precommit-validated successor).
use super::*;
use serde_json::{json, Value};
use sha2::{Digest, Sha256};
use std::panic::{catch_unwind, AssertUnwindSafe};
use std::path::{Path, PathBuf};

fn sha(bytes: &[u8]) -> String { format!("{:x}", Sha256::digest(bytes)) }
fn walk(dir: &Path, out: &mut Vec<PathBuf>) {
    let mut entries: Vec<_> = std::fs::read_dir(dir).unwrap().map(|e| e.unwrap().path()).collect();
    entries.sort();
    for p in entries {
        if p.is_dir() { walk(&p, out) } else if p.extension().map_or(false, |e| e == "json") { out.push(p) }
    }
}
fn guard<F: FnOnce() -> String>(f: F) -> String { catch_unwind(AssertUnwindSafe(f)).unwrap_or_else(|_| "PANIC".into()) }
fn bytes(e: &MechanicsEnvelope) -> Vec<u8> { serde_json::to_vec(e).unwrap() }
/// The value route's envelope plus k >= 1 N1 notices (any C1:68 detail), one per case, for distinct
/// requested cases in request order, after the ordinary diagnostics, and no other notice: `Some(k)`.
/// At c = 1 this is I61's "exactly one N1 notice for `case`".
fn value_plus_notices(published: &[u8], value: &[u8], cases: &[&str]) -> Option<usize> {
    let (Ok(mut p), Ok(v)) = (serde_json::from_slice::<Value>(published), serde_json::from_slice::<Value>(value)) else { return None };
    let diags = p["diagnostics"].as_array_mut()?;
    let plain = RETAINED_UNAVAILABLE_NOTICE;
    let mut tail: Vec<usize> = Vec::new(); // request indices, read from the end
    while let Some(last) = diags.last() {
        let message = last["message"].as_str().unwrap_or("").to_owned();
        let detail_ok = message == plain || ["work_counter_range", "work_counter_inconsistent", "saturation_not_excluded", "publication_hash_range"]
            .iter().any(|d| message == format!("{plain} Reason: receipt_encoding; detail: {d}."));
        let Some(k) = cases.iter().position(|case| *last == json!({"id":format!("diagnostic:retained-precision:{case}:unavailable"),
            "code":"RETAINED_PRECISION_UNAVAILABLE","severity":"info","message":message,"source":"core/product_physics","affected_refs":[case]})) else { break };
        if !detail_ok || tail.last().is_some_and(|later| *later <= k) { return None }
        tail.push(k);
        diags.pop();
    }
    let no_other_notice = !diags.iter().any(|d| d["code"] == "RETAINED_PRECISION_UNAVAILABLE");
    (!tail.is_empty() && no_other_notice && p == v).then_some(tail.len())
}
fn retained_line(raw: &Value, value: &Result<MechanicsEnvelope, String>, out: Result<RetainedPreviewOutput, String>) -> String {
    let o = match out { Ok(o) => o, Err(s) => return format!("ERR:{s}") };
    let report = o.admission().map(|r| (r.profile, r.law().refusal.map(|x| x.clause().map_or("bound", |c| c.id())))) ;
    let cause = match o.retained() { None => "none".to_string(), Some(Ok(_)) => "successor".into(), Some(Err(f)) => format!("{f:?}") };
    let ran = matches!(o.retained(), Some(Err(W1Fallback::Preparation | W1Fallback::Native | W1Fallback::Candidate | W1Fallback::Staging(_)
        | W1Fallback::Serializer(_) | W1Fallback::Precommit { .. })));
    let successor = o.successor().is_some();
    let published = match o.into_publication() {
        RetainedPublication::Successor(v) => serde_json::to_vec(&v).unwrap(),
        RetainedPublication::Ordinary(e) => bytes(&e),
    };
    let value_bytes = value.as_ref().map(bytes).ok();
    let cases: Vec<&str> = raw["model"]["load_cases"].as_array().map_or(Vec::new(), |c| c.iter().map(|c| c["id"].as_str().unwrap_or("")).collect());
    let class = if successor { "successor".to_string() }
        else if Some(&published) == value_bytes.as_ref() { "exact".into() }
        else { match value_bytes.as_ref().and_then(|v| value_plus_notices(&published, v, &cases)) {
            Some(1) => "notice".into(),
            Some(k) => format!("notice_x{k}"),
            None => "OTHER".into(),
        } };
    assert!(class != "OTHER", "a publication that is neither exact, notice nor successor");
    assert_eq!(class.starts_with("notice"), ran, "a notice exactly when W1 work ran: {cause}");
    format!("{}\t{class}\t{report:?}\t{cause}", sha(&published))
}

#[test]
#[ignore]
fn zz_i106_sg_sweep() {
    let root = Path::new(env!("CARGO_MANIFEST_DIR")).join("../../fixtures");
    let mut files = Vec::new();
    walk(&root, &mut files);
    let mut lines = Vec::new();
    let mut inputs = 0;
    for path in files {
        let rel = path.strip_prefix(&root).unwrap().display().to_string();
        let Ok(v) = serde_json::from_slice::<Value>(&std::fs::read(&path).unwrap()) else { continue };
        let raw = if v.get("model").and_then(|m| m.get("load_cases")).is_some() {
            v
        } else if v.get("load_cases").is_some() && (v.get("nodes").is_some() || v.get("components").is_some()) {
            json!({ "model": v })
        } else {
            continue;
        };
        inputs += 1;
        let typed = serde_json::from_value::<LinearStaticPreviewRequest>(raw.clone()).ok();
        lines.push(format!("{rel}\ttyped_default\t-\t{}", guard(|| match typed.clone() {
            Some(t) => sha(&bytes(&run_linear_static_preview(t))),
            None => "TYPED_PARSE_ERR".into(),
        })));
        for mode in [PreviewSolverMode::SparseInteractive, PreviewSolverMode::DenseScrutiny] {
            let m = mode.as_str();
            lines.push(format!("{rel}\ttyped_mode\t{m}\t{}", guard(|| match typed.clone() {
                Some(t) => sha(&bytes(&run_linear_static_preview_with_mode(t, mode))),
                None => "TYPED_PARSE_ERR".into(),
            })));
            let value = catch_unwind(AssertUnwindSafe(|| run_linear_static_preview_value_with_mode(raw.clone(), mode)));
            let value = match value { Ok(v) => v, Err(_) => Err("PANIC".into()) };
            lines.push(format!("{rel}\tvalue_mode\t{m}\t{}", match &value { Ok(e) => sha(&bytes(e)), Err(s) => format!("ERR:{s}") }));
            lines.push(format!("{rel}\tretained_direct\t{m}\t{}", guard(|| retained_line(&raw, &value,
                run_linear_static_preview_value_with_retained_direct(raw.clone(), mode)))));
            let invocation = json!({ "request": raw.clone(), "solver_mode": m });
            let request_id = String::from("i61-u3-sweep");
            lines.push(format!("{rel}\tretained_headless\t{m}\t{}", guard(|| {
                let ctx = RetainedHeadlessContext::from_borrowed_roots(&raw, &invocation, &request_id);
                retained_line(&raw, &value, run_linear_static_preview_value_with_retained_headless(raw.clone(), mode, ctx))
            })));
        }
    }
    let out = std::env::var("I106_SG_SWEEP").expect("I106_SG_SWEEP");
    std::fs::write(&out, lines.join("\n") + "\n").unwrap();
    println!("I106_SG_SWEEP inputs={inputs} lines={}", lines.len());
}
