#!/usr/bin/env python3
"""I109 measurement-only patch for a scratch archive tree (never committed): an SF-2 dump
(`I109_SF2_OUT`) beside the pinned successor in retained_facade_tests.rs, and an example that
prints the value entry's envelope exactly as s11g's t13 renders it.
Usage: regen_patch.py <tree holding projects/chirality-piping>
"""
import pathlib
import sys

pp = pathlib.Path(sys.argv[1]) / "projects/chirality-piping/core/product_physics"
f = pp / "src/retained_facade_tests.rs"
s = f.read_text()
anchor = '            println!("B1_SP_SF2_PIN {label} {} {}", successor["retained_precision"]["receipt_sha256"].as_str().unwrap(), sha(&bytes));\n'
assert s.count(anchor) == 1
s = s.replace(anchor, anchor + '            if let Ok(dir) = std::env::var("I109_SF2_OUT") { std::fs::write(std::path::Path::new(&dir).join(format!("{}.json", label.replace(\' \', "__"))), &bytes).unwrap(); }\n')
f.write_text(s)
# SF-2: report the pin instead of asserting it, so a_a2 is reached after c_b_a (measurement only).
pin = '            assert_eq!((successor["retained_precision"]["receipt_sha256"].as_str(), sha(&bytes).as_str()), (Some(receipt_sha), bytes_sha), "{label}: the pinned successor");\n'
s = f.read_text()
assert s.count(pin) == 1
s = s.replace(pin, '            println!("I109_SF2_PIN_MATCH {label} {}", (successor["retained_precision"]["receipt_sha256"].as_str(), sha(&bytes).as_str()) == (Some(receipt_sha), bytes_sha));\n')
f.write_text(s)
# m08's checker: report every intensified row against the libm expression instead of asserting.
g = pp / "tests/preview_physics_runtime.rs"
t = g.read_text()
eq = '            assert_eq!(num(&row["value"]), expected);\n'
assert t.count(eq) == 1
t = t.replace(eq, '            println!("I109_INTENSIFIED {} {:?} {:?} {}", row["id"], num(&row["value"]), expected, num(&row["value"]) == expected);\n')
g.write_text(t)
(pp / "examples/i109_regen.rs").write_text('''//! I109 measurement harness (scratch only): the value entry's envelope, rendered as s11g's t13
//! renders it (`to_string_pretty` and a newline). Usage: i109_regen <mode> <request.json>
use open_pipe_stress_product_physics::{run_linear_static_preview_value_with_mode, PreviewSolverMode};
fn main() {
    let a: Vec<String> = std::env::args().skip(1).collect();
    let mode = PreviewSolverMode::from_wire(&a[0]).expect("mode");
    let request: serde_json::Value = serde_json::from_str(&std::fs::read_to_string(&a[1]).unwrap()).unwrap();
    match run_linear_static_preview_value_with_mode(request, mode) {
        Ok(envelope) => print!("{}\\n", serde_json::to_string_pretty(&envelope).unwrap()),
        Err(e) => { eprintln!("ERR {e}"); std::process::exit(3) }
    }
}
''')
print("patched", pp)
