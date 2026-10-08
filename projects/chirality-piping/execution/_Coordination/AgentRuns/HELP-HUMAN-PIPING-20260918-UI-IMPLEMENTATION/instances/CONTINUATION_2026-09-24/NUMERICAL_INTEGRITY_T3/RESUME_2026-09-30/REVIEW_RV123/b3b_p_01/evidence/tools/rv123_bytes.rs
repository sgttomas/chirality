//! RV123 (RV-P2 round 1): one harness, run unchanged on the base and the candidate copies. For each
//! input (B3-W's inputs, the committed physics-source requests, the preview milestone) in both
//! modes, write the plain ordinary bytes and the Direct entry's one publication, with the
//! admission refusal and the W1 outcome, so the two trees can be compared byte for byte.
use open_pipe_stress_product_physics::{run_linear_static_preview_value_with_mode, run_linear_static_preview_value_with_retained_direct,
    PreviewSolverMode, RetainedPublication};
use serde_json::Value;
use std::path::PathBuf;

#[test]
fn rv123_bytes() {
    let inputs = PathBuf::from(std::env::var("RV123_IN").expect("RV123_IN"));
    let out = PathBuf::from(std::env::var("RV123_OUT").expect("RV123_OUT"));
    std::fs::create_dir_all(&out).unwrap();
    let manifest = PathBuf::from(env!("CARGO_MANIFEST_DIR"));
    let ps = manifest.join("../../fixtures/product_preview/physics_source");
    let mut cases: Vec<(String, Value)> = Vec::new();
    for name in ["fields", "m3l", "m3x", "m3x_mix_anchor", "m3x_mix_axial", "m3x_mix_lateral", "n05", "n06", "m1_twin_anchor", "m1_twin_axial", "m1_twin_lateral"] {
        cases.push((format!("i99_{name}"), serde_json::from_slice(&std::fs::read(inputs.join(format!("{name}.json"))).unwrap()).unwrap()));
    }
    for name in ["n05", "n05_units", "n05_unicode", "n06", "fields", "mixed", "mixed_units"] {
        cases.push((format!("ps_{name}"), serde_json::from_slice(&std::fs::read(ps.join(format!("{name}.request.json"))).unwrap()).unwrap()));
    }
    let milestone: Value = serde_json::from_slice(&std::fs::read(manifest.join("../../fixtures/results/retained_precision_milestone_successor_sparse_interactive.json")).unwrap()).unwrap();
    cases.push(("milestone".into(), milestone["invocation"]["request"].clone()));
    for extra in std::env::var("RV123_EXTRA").ok().into_iter().flat_map(|v| v.split(',').map(str::to_owned).collect::<Vec<_>>()) {
        if extra.is_empty() { continue; }
        let p = PathBuf::from(&extra);
        cases.push((format!("x_{}", p.file_stem().unwrap().to_str().unwrap()), serde_json::from_slice(&std::fs::read(&p).unwrap()).unwrap()));
    }
    for (name, raw) in &cases {
        for mode in [PreviewSolverMode::SparseInteractive, PreviewSolverMode::DenseScrutiny] {
            let plain = serde_json::to_vec(&run_linear_static_preview_value_with_mode(raw.clone(), mode).unwrap()).unwrap();
            let output = run_linear_static_preview_value_with_retained_direct(raw.clone(), mode);
            let (kind, refusal, retained, bytes) = match output {
                Err(e) => ("error".to_owned(), String::new(), String::new(), e.into_bytes()),
                Ok(o) => {
                    let refusal = format!("{:?}", o.admission().map(|a| (a.profile, a.allowance)));
                    let retained = format!("successor={}", o.successor().is_some());
                    match o.into_publication() {
                        RetainedPublication::Successor(v) => ("successor".to_owned(), refusal, retained, serde_json::to_vec(&v).unwrap()),
                        RetainedPublication::Ordinary(e) => ("ordinary".to_owned(), refusal, retained, serde_json::to_vec(&e).unwrap()),
                    }
                }
            };
            std::fs::write(out.join(format!("{name}.{}.plain.json", mode.as_str())), &plain).unwrap();
            std::fs::write(out.join(format!("{name}.{}.direct.json", mode.as_str())), &bytes).unwrap();
            println!("RV123_BYTES {name} {} kind={kind} same_as_plain={} admission={refusal} w1={retained}", mode.as_str(), bytes == plain);
        }
    }
}
