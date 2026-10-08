// RV126 scratch: loop-pass count of the head's correct_norm (instrumented copy; counts loop-body entries per call).
#[path = "correct_norm_instr.rs"]
#[allow(dead_code)]
mod correct_norm;
use std::io::Read;
fn main() {
    let a: Vec<String> = std::env::args().collect();
    let mut buf = Vec::new();
    std::fs::File::open(&a[1]).unwrap().read_to_end(&mut buf).unwrap();
    for r in buf.chunks_exact(24) {
        let x = |i: usize| f64::from_le_bytes(r[8 * i..8 * i + 8].try_into().unwrap());
        std::hint::black_box(correct_norm::norm3(x(0), x(1), x(2)));
        std::hint::black_box(correct_norm::norm2(x(0), x(1)));
    }
    let h: Vec<u64> = correct_norm::HIST.iter().map(|v| v.load(std::sync::atomic::Ordering::Relaxed)).collect();
    println!("max loop passes per call: {}; histogram of passes [0..7+]: {:?}", correct_norm::MAXP.load(std::sync::atomic::Ordering::Relaxed), h);
}
