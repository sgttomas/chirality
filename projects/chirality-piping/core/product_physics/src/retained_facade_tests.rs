//! I61 U3 grant 1: the facade's W1 phases through the private driver. No permit
//! exists until U4 G5 and decision 7 forbids a test permit, so these tests enter
//! `retained_w1` (the body the permitted dispatch runs after G-C) with an observer
//! installed in the actual single ordinary run, exactly as the facade does.
use super::retained_product as rp;
use super::*;
use serde_json::{json, Value};
use sha2::{Digest, Sha256};

const MILESTONE: &str = include_str!("../../../fixtures/product_preview/rf_skew_t_cant_off_122_r1e-04.request.json");
const MODES: [PreviewSolverMode; 2] = [PreviewSolverMode::SparseInteractive, PreviewSolverMode::DenseScrutiny];
/// U1's committed successor bytes (retained_wire_tests::SUCCESSOR_SHA256).
const PINNED: [(&str, &str, &str); 2] = [
    ("sparse_interactive", "ac6986b0680e0df9d88c33a5bf4635372fc3b83cbb9080da44e6d32dbdca59dc", "efc1a39bbe83840df6bd0761c932b8020285d3b8c005ba8fd0b45ba10d667494"),
    ("dense_scrutiny", "6cd1d249e5352aaffbd2b7d7349c74a1d0e0572df35500f66be49c3cad95c9b5", "3e26499f17caff8f5fc0d46406bbe54acf43e8cb16e761784aa5074413b0ac4a"),
];

fn sha(bytes: &[u8]) -> String {
    format!("{:x}", Sha256::digest(bytes))
}
fn raw() -> Value {
    serde_json::from_str(MILESTONE).unwrap()
}
fn plain(mode: PreviewSolverMode, raw: &Value) -> Vec<u8> {
    serde_json::to_vec(&run_linear_static_preview_value_with_mode(raw.clone(), mode).unwrap()).unwrap()
}
/// The facade's single observed ordinary run: the captured invocation, the
/// observer with capture installed, and the ordinary envelope it returned.
fn observed(mode: PreviewSolverMode, raw: &Value) -> (source_receipt::CapturedInvocation, rp::ProductCapture, MechanicsEnvelope) {
    let (request, capture) = source_receipt::CapturedInvocation::parse(raw.clone(), mode).unwrap();
    let mut observer = rp::ProductCapture::prepared_probe();
    let ordinary = run_linear_static_preview_observed(request, mode, Some(&capture), &mut SourceRecoveryBudget::default(), Some(&mut observer));
    (capture, observer, ordinary)
}

/// Control 2: the permitted path publishes U1's pinned successor bytes, in both
/// modes, through the frozen candidate and its staging copy; the ordinary
/// envelope it returns beside the successor is byte-identical to the plain route.
#[test]
fn u3_permitted_path_publishes_the_pinned_successor() {
    let out = std::env::var("I61_U3_OUT").ok().map(std::path::PathBuf::from);
    for (mode, (name, file_sha, receipt_sha)) in MODES.into_iter().zip(PINNED) {
        assert_eq!(mode.as_str(), name);
        let raw = raw();
        let plain = plain(mode, &raw);
        let (capture, observer, ordinary) = observed(mode, &raw);
        assert_eq!(serde_json::to_vec(&ordinary).unwrap(), plain, "{name}: the observed run is the plain run");
        let (envelope, retained) = retained_w1(observer, ordinary, &capture);
        assert_eq!(serde_json::to_vec(&envelope).unwrap(), plain, "{name}: the ordinary owner is untouched");
        let successor = retained.unwrap_or_else(|f| panic!("{name}: {f:?}"));
        let text = serde_json::to_string_pretty(&json!({"id":format!("u1_milestone_{name}"),"source":successor.value(),
            "invocation":{"request":raw,"solver_mode":mode.as_str()}})).unwrap();
        assert_eq!((sha(text.as_bytes()).as_str(), successor.value()["retained_precision"]["receipt_sha256"].as_str()), (file_sha, Some(receipt_sha)),
            "{name}: U1's pinned successor bytes");
        if let Some(dir) = &out {
            std::fs::write(dir.join(format!("u3_successor_{name}.json")), &text).unwrap();
        }
    }
}

/// Control 3: a fault at each W1 stage falls back to the preserved ordinary bytes
/// with its private cause (grant 1: no public notice; checkpoint item 2).
#[test]
fn u3_each_stage_fault_falls_back_to_the_ordinary_bytes() {
    use super::retained_receipt::TraceFault as F;
    let mode = PreviewSolverMode::SparseInteractive;
    let raw = raw();
    let plain = plain(mode, &raw);
    let fallback = |envelope: &MechanicsEnvelope, label: &str| {
        assert_eq!(serde_json::to_vec(envelope).unwrap(), plain, "{label}: preserved ordinary bytes");
    };
    // Preparation: the closed annulus helper refuses (experiment 02's trigger).
    let (capture, mut observer, ordinary) = observed(mode, &raw);
    observer.facts[0].diameter = 0.0;
    let (envelope, retained) = retained_w1(observer, ordinary, &capture);
    assert_eq!(retained.err(), Some(W1Fallback::Preparation));
    fallback(&envelope, "preparation");
    // Native: the prepared source is withdrawn before the solve (D38's trigger).
    let (capture, observer, ordinary) = observed(mode, &raw);
    retained_tests_hooks::withdraw_next_native_source();
    let (envelope, retained) = retained_w1(observer, ordinary, &capture);
    assert_eq!(retained.err(), Some(W1Fallback::Native));
    fallback(&envelope, "native");
    // Proof/facade: injected faults after the proof started.
    for fault in [F::Maxima, F::ValuesCompletion] {
        let (capture, mut observer, ordinary) = observed(mode, &raw);
        observer.trace_fault = Some(fault);
        let (envelope, retained) = retained_w1(observer, ordinary, &capture);
        assert_eq!(retained.err(), Some(W1Fallback::Candidate), "{fault:?}");
        fallback(&envelope, "candidate");
    }
    // Serializer: an invocation other than the observed one (RV82-S2) refuses typed.
    let (_, observer, ordinary) = observed(mode, &raw);
    let mut other = raw.clone();
    other["model"]["load_cases"][0]["label"] = json!("another label");
    let (_, foreign) = source_receipt::CapturedInvocation::parse(other, mode).unwrap();
    let (envelope, retained) = retained_w1(observer, ordinary, &foreign);
    assert_eq!(retained.err(), Some(W1Fallback::Serializer(retained_wire::ReceiptFailure {
        check: retained_wire::ReceiptCheck::Association, field_path: "invocation" })));
    fallback(&envelope, "serializer");
    // Precommit validation: a corrupted receipt hash is the reader's G1 refusal.
    let (capture, observer, ordinary) = observed(mode, &raw);
    retained_tests_hooks::corrupt_next_precommit();
    let (envelope, retained) = retained_w1(observer, ordinary, &capture);
    assert_eq!(retained.err(), Some(W1Fallback::Precommit { gate: "G1", code: "RETAINED_PRECISION_RECEIPT_MISMATCH".into() }));
    fallback(&envelope, "precommit");
    // Precommit binding: the reader validates against the actual invocation, so a
    // successor checked against another solver mode is refused.
    let (capture, observer, ordinary) = observed(mode, &raw);
    retained_tests_hooks::rebind_next_precommit_invocation();
    let (envelope, retained) = retained_w1(observer, ordinary, &capture);
    assert_eq!(retained.err(), Some(W1Fallback::Precommit { gate: "G8", code: "RETAINED_PRECISION_INVOCATION_MISMATCH".into() }));
    fallback(&envelope, "precommit binding");
    // Coexistence: an ordinary envelope carrying an exact source-block publication.
    let (capture, observer, mut ordinary) = observed(mode, &raw);
    ordinary.source_block_recovery = Some(json!({"marker":"exact"}));
    let marked = serde_json::to_vec(&ordinary).unwrap();
    let (envelope, retained) = retained_w1(observer, ordinary, &capture);
    assert_eq!(retained.err(), Some(W1Fallback::Coexistence));
    assert_eq!(serde_json::to_vec(&envelope).unwrap(), marked, "coexistence: the exact publication is returned as is");
}

/// Control 1: with no permit (always, until U4 G5) both retained entries and the
/// shared route are the unchanged ordinary route, with no W1 result.
#[test]
fn u3_no_permit_entries_are_the_ordinary_route() {
    for mode in MODES {
        let raw = raw();
        let plain = plain(mode, &raw);
        let direct = run_linear_static_preview_value_with_retained_direct(raw.clone(), mode).unwrap();
        assert_eq!(serde_json::to_vec(direct.envelope()).unwrap(), plain);
        assert!(direct.retained().is_none());
        assert!(direct.admission().is_some(), "G-A's census still runs");
    }
}

/// STACK_PLAN §1: the reserved-stack runner returns the work's value, re-raises a
/// panic with its original payload, and reports a spawn failure without running.
#[test]
fn u3_reserved_stack_runner() {
    // A 3 MiB frame needs more than the 2 MiB default spawned-thread stack: it
    // runs only because the reservation is honoured.
    let observed_stack = on_reserved_stack(8 << 20, || {
        let frame = std::hint::black_box([7u8; 3 << 20]);
        frame.iter().map(|b| *b as usize).sum::<usize>()
    });
    assert_eq!(observed_stack, Some(7 * (3 << 20)));
    let borrowed = vec![1, 2, 3];
    assert_eq!(on_reserved_stack(1 << 20, || borrowed.iter().sum::<i32>()), Some(6), "borrows, no clone");
    let panicked = std::panic::catch_unwind(|| on_reserved_stack(1 << 20, || -> u8 { std::panic::panic_any(41usize) }));
    assert_eq!(panicked.err().and_then(|p| p.downcast::<usize>().ok()).map(|b| *b), Some(41), "original payload");
    let mut ran = false;
    assert_eq!(on_reserved_stack(1usize << 62, || ran = true), None, "spawn failure");
    assert!(!ran, "the work did not run");
}

/// RV82 N9 (single-parse custody): each invocation is parsed exactly once. The
/// typed request that runs and the captured invocation the serializer binds (S2's
/// digest) are the two halves of that one `CapturedInvocation::parse`: the capture
/// is not `Clone`, `parse` is its only constructor, the dispatch is the only
/// production parse site, and the permitted path only moves or borrows its halves.
#[test]
fn u3_n9_single_parse_custody() {
    const PARSE: &str = "CapturedInvocation::parse(";
    let lib = include_str!("lib.rs");
    let section = |start: &str, end: &str| {
        let suffix = &lib[lib.find(start).unwrap()..];
        &suffix[..suffix.find(end).unwrap()]
    };
    assert_eq!(lib.matches(PARSE).count(), 1, "lib.rs has one parse site");
    let dispatch = section("fn run_linear_static_preview_value_dispatch(", "fn ordinary_dispatch(");
    assert!(dispatch.contains("let (request, capture) = source_receipt::CapturedInvocation::parse(actual_request, solver_mode)"));
    assert!(dispatch.contains("Some(Ok(permit)) => return permitted_dispatch(permit, request, capture, solver_mode),"));
    assert!(dispatch.contains("ordinary_dispatch(request, &capture, solver_mode, admission, None)"));
    // The permitted path: the parse's two halves, moved or borrowed, never re-derived.
    let permitted = section("fn permitted_dispatch(", "pub(crate) mod retained_tests_hooks");
    for forbidden in ["parse(", "CapturedInvocation {", "capture.clone()", "request.clone()", "from_value("] {
        assert!(!permitted.contains(forbidden), "{forbidden}");
    }
    for required in [
        "slot.take().map(|request| permitted_run(permit, request, &capture, solver_mode))",
        "(None, Some(request)) => ordinary_dispatch(request, &capture, solver_mode, None, Some(Err(W1Fallback::StackReservation))),",
        "run_linear_static_preview_observed(request, solver_mode, Some(capture), &mut budget, Some(&mut observer))",
        "Ok(()) => retained_w1(observer, ordinary, capture),",
        "retained_wire::serialize_frozen(&frozen, &staged, capture)",
    ] {
        assert!(permitted.contains(required), "{required}");
    }
    // No other production parse site, and no second custody constructor.
    for (name, text) in [
        ("retained_product.rs", include_str!("retained_product.rs")),
        ("retained_wire.rs", include_str!("retained_wire.rs")),
        ("retained_receipt.rs", include_str!("retained_receipt.rs")),
    ] {
        assert!(!text.contains(PARSE) && !text.contains("impl Clone for CapturedInvocation"), "{name}");
    }
    let memory = include_str!("retained_memory.rs");
    assert!(!memory[..memory.find("#[cfg(test)]\npub(super) mod tests {").unwrap()].contains(PARSE), "retained_memory.rs");
    let receipt = include_str!("source_receipt.rs");
    assert!(receipt.contains("#[derive(Debug)]\npub(super) struct CapturedInvocation {"), "not Clone");
    assert_eq!(receipt.matches("impl CapturedInvocation {").count(), 1);
    assert!(!receipt.contains("for CapturedInvocation") && !lib.contains("for CapturedInvocation"), "no trait constructor or Clone");
    let block = &receipt[receipt.find("\nimpl CapturedInvocation {\n").unwrap()..];
    let block = &block[..block.find("\n}\n").unwrap()];
    assert_eq!(block.matches("Self {").count(), 1, "parse's literal is the only constructor");
    assert_eq!(block.matches("-> Result<(LinearStaticPreviewRequest, Self), ReceiptError>").count(), 1);
    assert!(!block.contains("-> Self"));
}
