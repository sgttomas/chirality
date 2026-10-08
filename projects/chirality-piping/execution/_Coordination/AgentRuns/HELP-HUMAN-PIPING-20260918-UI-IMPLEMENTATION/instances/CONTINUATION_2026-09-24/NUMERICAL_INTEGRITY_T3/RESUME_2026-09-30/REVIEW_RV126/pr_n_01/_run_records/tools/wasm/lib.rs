// RV126: the head's correct_norm compiled for wasm32-unknown-unknown (as the browser engine is),
// run under node over the same triples; outputs compared bitwise with the native (aarch64) run.
#[path = "WT/rv126/projects/chirality-piping/core/solver/frame_kernel/src/correct_norm.rs"]
#[allow(dead_code)]
mod correct_norm;

static mut BUF: [u8; 1 << 20] = [0; 1 << 20];

#[no_mangle]
pub extern "C" fn buf() -> *mut u8 {
    core::ptr::addr_of_mut!(BUF) as *mut u8
}

/// Reads `n` triples (24 bytes each) at the buffer start; writes norm3 and norm2 bits after them.
#[no_mangle]
pub extern "C" fn run(n: u32) {
    let base = buf();
    for i in 0..n as usize {
        let rd = |k: usize| unsafe { f64::from_le_bytes(core::ptr::read_unaligned(base.add(24 * i + 8 * k) as *const [u8; 8])) };
        let (a, b, c) = (rd(0), rd(1), rd(2));
        let out = unsafe { base.add(24 * n as usize + 16 * i) };
        unsafe {
            core::ptr::write_unaligned(out as *mut [u8; 8], correct_norm::norm3(a, b, c).to_bits().to_le_bytes());
            core::ptr::write_unaligned(out.add(8) as *mut [u8; 8], correct_norm::norm2(a, b).to_bits().to_le_bytes());
        }
    }
}
