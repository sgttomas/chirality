use open_pipe_stress_product_physics::{
    run_linear_static_preview_value_with_mode,
    PreviewSolverMode,
};

fn main() {
    let arguments = std::env::args().skip(1).collect::<Vec<_>>();
    let mode = match arguments.as_slice() {
        [] => PreviewSolverMode::default(),
        [mode] => PreviewSolverMode::from_wire(mode).unwrap_or_else(|| {
            eprintln!("unsupported preview solver mode: {mode}");
            std::process::exit(2);
        }),
        _ => {
            eprintln!("usage: preview_result [sparse_interactive|dense_scrutiny]");
            std::process::exit(2);
        }
    };
    let model: serde_json::Value = serde_json::from_str(include_str!(
        "../../../fixtures/product_preview/invented_preview_model.json"
    ))
    .expect("invented preview model fixture should parse");
    let result = run_linear_static_preview_value_with_mode(
        serde_json::json!({"model":model,"materials":[]}), mode,
    ).expect("actual Value-aware preview producer should complete");
    println!(
        "{}",
        serde_json::to_string_pretty(&result).expect("result should serialize")
    );
}
