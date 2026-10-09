//! I105 J0b scratch probe (archive copies only; never committed): the legacy label on the milestone, on its own
//! schema and on 0.3.0 (B3-W's `m3l`), through the ordinary route and the retained Direct entry.
use super::*;
use serde_json::{json, Value};
#[test]
fn i105_j0b_legacy_label_probe() {
    let milestone: Value = serde_json::from_str(include_str!("../../../fixtures/product_preview/rf_skew_t_cant_off_122_r1e-04.request.json")).unwrap();
    let mut label = milestone.clone();
    label["model"]["pressure_contract"] = json!({"version": "1.0.0", "mode": "legacy_pressure_v1"});
    let mut m3l = label.clone();
    m3l["model"]["schema_version"] = json!("0.3.0");
    for (name, raw) in [("milestone schema + label", label), ("m3l: 0.3.0 + label", m3l)] {
        for mode in [PreviewSolverMode::SparseInteractive, PreviewSolverMode::DenseScrutiny] {
            let plain = run_linear_static_preview_value_with_mode(raw.clone(), mode).unwrap();
            let blocking: Vec<(String, Vec<String>)> = plain.diagnostics.iter().filter(|d| d.severity == "blocking")
                .map(|d| (d.code.clone(), d.affected_refs.clone())).collect();
            println!("I105_J0B_PROBE {name} {mode:?} ordinary: status={} results={} source_blocks={} blocking={blocking:?}",
                plain.status.mechanics, plain.results.len(), plain.source_block_recovery.is_some());
            let direct = run_linear_static_preview_value_with_retained_direct(raw.clone(), mode).unwrap();
            let same = serde_json::to_vec(direct.envelope()).unwrap() == serde_json::to_vec(&plain).unwrap();
            println!("I105_J0B_PROBE {name} {mode:?} direct: G-A domain={:?} refused={} retained={} successor={} envelope_equals_ordinary={same}",
                direct.admission().unwrap().law().domain, direct.admission().unwrap().law().refusal.is_some(),
                direct.retained().is_some(), direct.successor().is_some());
        }
    }
}
