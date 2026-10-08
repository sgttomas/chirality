// RV126 driver: evaluates the PR-N head's `correct_norm` (included by path from the archive copy)
// on little-endian binary64 triples (a, b, c) read from argv[1], writing per triple the bits of
// norm3(a, b, c), norm2(a, b), and, for comparison only, libm a.hypot(b) and a.hypot(b).hypot(c).
#[path = "WT/rv126/projects/chirality-piping/core/solver/frame_kernel/src/correct_norm.rs"]
#[allow(dead_code)]
mod correct_norm;

use std::io::{BufReader, BufWriter, Read, Write};

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let mut reader = BufReader::new(std::fs::File::open(&args[1]).expect("input"));
    let mut writer = BufWriter::new(std::fs::File::create(&args[2]).expect("output"));
    let mut record = [0u8; 24];
    let mut count = 0u64;
    loop {
        match reader.read_exact(&mut record) {
            Ok(()) => {}
            Err(e) if e.kind() == std::io::ErrorKind::UnexpectedEof => break,
            Err(e) => panic!("read: {e}"),
        }
        let x = |i: usize| f64::from_le_bytes(record[8 * i..8 * i + 8].try_into().unwrap());
        let (a, b, c) = (x(0), x(1), x(2));
        let n3 = correct_norm::norm3(a, b, c);
        let n2 = correct_norm::norm2(a, b);
        let h2 = a.hypot(b);
        let h3 = h2.hypot(c);
        for v in [n3, n2, h2, h3] {
            writer.write_all(&v.to_bits().to_le_bytes()).unwrap();
        }
        count += 1;
    }
    writer.flush().unwrap();
    eprintln!("rv126 driver: {count} triples");
}
