"""RV124: append a size probe test to the law tests in the mutant copy (test code only), or remove it."""
import sys
F = "WT/scratch/rv124_rvq/mut/projects/chirality-piping/core/product_physics/src/retained_memory_law_tests.rs"
PROBE = '''
#[test]
fn rv124_size_probe() {
    use std::mem::size_of;
    println!("RV124_SIZE CaseAttempt={} PreparedTrace={} AttemptParts={} AttemptEnd={} FrozenCase={} RefusedCase={} CaseSlot={} PreparedCases={} ProductCapture={} PrimitiveSource={}",
        size_of::<crate::retained_product::CaseAttempt>(), size_of::<crate::retained_receipt::PreparedTrace>(),
        size_of::<crate::retained_product::AttemptParts>(), size_of::<crate::retained_product::AttemptEnd>(),
        size_of::<crate::retained_product::FrozenCase>(), size_of::<crate::retained_product::RefusedCase>(),
        size_of::<crate::retained_product::CaseSlot>(), size_of::<crate::retained_product::PreparedCases>(),
        size_of::<crate::retained_product::ProductCapture>(),
        size_of::<open_pipe_stress_frame_kernel::structural::retained_api::PrimitiveSource>());
}
'''
t = open(F).read()
if sys.argv[1] == "add":
    assert "rv124_size_probe" not in t
    open(F, "w").write(t + PROBE)
else:
    assert t.endswith(PROBE)
    open(F, "w").write(t[: -len(PROBE)])
print(sys.argv[1], "ok")
