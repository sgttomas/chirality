// I107 (Pass B item 4): the correction loop's passes per call, over the committed oracle vectors (expected bits
// checked) and random arguments across the binary64 range. Usage: main <vectors.txt> <random triples>
#[allow(dead_code)]
mod correct_norm_counted;
use correct_norm_counted::{norm2, norm3, PASSES};
use std::sync::atomic::Ordering;
fn passes<F: Fn() -> f64>(f: F) -> (f64, usize) { PASSES.store(0, Ordering::Relaxed); let r = f(); (r, PASSES.load(Ordering::Relaxed)) }
fn main() {
    let a: Vec<String> = std::env::args().collect();
    let text = std::fs::read_to_string(&a[1]).unwrap();
    let n: u64 = a[2].parse().unwrap();
    let mut hist = [0u64; 8]; let mut checked = 0u64; let mut bad = 0u64;
    let hex = |w: &str| f64::from_bits(u64::from_str_radix(w, 16).unwrap());
    for line in text.lines().filter(|l| !l.starts_with('#') && !l.is_empty()) {
        let w: Vec<&str> = line.split_whitespace().collect();
        let (x, y, z) = (hex(w[0]), hex(w[1]), hex(w[2]));
        let (r3, p3) = passes(|| norm3(x, y, z)); let (r2, p2) = passes(|| norm2(x, y));
        if format!("{:016x}", r3.to_bits()) != w[3] || format!("{:016x}", r2.to_bits()) != w[4] { bad += 1; }
        hist[p3.min(7)] += 1; hist[p2.min(7)] += 1; checked += 1;
    }
    let vec_hist = hist; let mut s: u64 = 0x9e3779b97f4a7c15;
    let mut next = || { s ^= s << 13; s ^= s >> 7; s ^= s << 17; s };
    let mut rhist = [0u64; 8];
    for i in 0..n {
        // random sign, exponent over the whole range (subnormals included) and mantissa; every 4th triple shares
        // an exponent band, so that near-equal magnitudes (the hard rounding cases) are common
        let mut f = || { let r = next(); let e = (r >> 52) & 0x7ff; let e = if e == 0x7ff { 0x7fe } else { e }; f64::from_bits((r & 0x800f_ffff_ffff_ffff) | (e << 52)) };
        let (mut x, mut y, mut z) = (f(), f(), f());
        if i % 4 == 0 { let e = (next() % 2046 + 1) << 52; let m = 0x000f_ffff_ffff_ffffu64;
            x = f64::from_bits((x.to_bits() & m) | e); y = f64::from_bits((y.to_bits() & m) | e); z = f64::from_bits((z.to_bits() & m) | e); }
        let (_, p3) = passes(|| norm3(x, y, z)); let (_, p2) = passes(|| norm2(x, y));
        rhist[p3.min(7)] += 1; rhist[p2.min(7)] += 1;
    }
    println!("vectors: {} lines, {} mismatched, passes histogram (0..7+) {:?}", checked, bad, vec_hist);
    println!("random: {} triples (norm3 and norm2 each), passes histogram (0..7+) {:?}", n, rhist);
    let max = |h: &[u64; 8]| (0..8).rev().find(|&k| h[k] > 0).unwrap_or(0);
    println!("max passes: vectors {}, random {}", max(&vec_hist), max(&rhist));
}
