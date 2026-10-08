#!/usr/bin/env python3
"""I109: classify the libm scan (libm_scan.py's TSV at NUM af53e1447c) into the inventory.

Columns: path (P-relative), line, function, calls (on the line), context (prod | reader | test),
computes, reaches, readers_recompute, platform (libm = platform-dependent; fixed = the same IEEE
operation sequence on every target; exact = an exact result), action.
Usage: inventory.py <scan.tsv> <out.tsv> <summary.json>
"""
import collections
import json
import re
import sys

PUB = "published bytes"
DEC = "admission decision"
TXT = "published diagnostic text"
RDR = "reader check (64-epsilon guard)"
RS_READER = "core/reporting/result_export/"
PY_READER = "core/analysis_runs/"
TS_READER = "apps/desktop/src/features/results/"
NORM_READERS = "RS, PY, TS recompute with libm/engine hypot under a 64-epsilon relative guard"

# Production sites: (path, line) -> (computes, reaches, readers, action)
PROD = {
    ("core/product_physics/src/lib.rs", 4926): ("ordinary route: support force magnitude |F| (support_reaction_force_magnitude rows)", PUB, NORM_READERS, "I109: norm3"),
    ("core/product_physics/src/lib.rs", 5122): ("formation guard: end q = |(My, Mz)| against the bending formation bound", DEC, "none", "I109: norm2"),
    ("core/product_physics/src/lib.rs", 7870): ("curved bend: implied included angle 2*asin(c/2R), checked against the user angle and printed in its diagnostic", DEC + "; " + TXT, "none", "recommend: correctly rounded asin, or compare sin(theta/2) with c/2R instead of angles (no inverse trig)"),
    ("core/product_physics/src/lib.rs", 11874): ("support action v2: force magnitude row", PUB, NORM_READERS, "I109: norm3"),
    ("core/product_physics/src/lib.rs", 11880): ("support action v2: moment magnitude row", PUB, NORM_READERS, "I109: norm3"),
    ("core/product_physics/src/lib.rs", 13509): ("combination: combined displacement/support magnitude row", PUB, NORM_READERS, "I109: norm3"),
    ("core/product_physics/src/preview_physics.rs", 465): ("curved-bend tangent discontinuity angle atan2(|d x t|, d.t): warning threshold and printed angle", DEC + "; " + TXT, "none", "I109: |cross| by norm3; atan2 remains libm (recommend: correctly rounded atan2, or a threshold test on |cross| and dot without the angle)"),
    ("core/product_physics/src/preview_physics.rs", 475): ("the same angle in degrees for the warning text (x * 180/pi)", TXT, "none", "none (fixed: one multiplication); follows atan2"),
    ("core/product_physics/src/preview_physics.rs", 634): ("intensified bending i*|(My, Mz)|/Z", PUB, "RS, PY, TS recompute i*hypot(My,Mz)/Z under a 64-epsilon guard", "I109: norm2"),
    ("core/product_physics/src/preview_physics.rs", 966): ("preview-physics combination: force magnitude", PUB, NORM_READERS, "I109: norm3"),
    ("core/product_physics/src/preview_physics.rs", 967): ("preview-physics combination: moment magnitude", PUB, NORM_READERS, "I109: norm3"),
    ("core/product_physics/src/pressure_runtime.rs", 1081): ("exact-pressure region chord length (direction, guard, diagnostic text)", DEC + "; " + TXT, "none", "I109: norm3"),
    ("core/product_physics/src/pressure_runtime.rs", 1099): ("exact-pressure region collinearity residual (guard, diagnostic text)", DEC + "; " + TXT, "none", "I109: norm3"),
    ("core/product_physics/src/retained_product.rs", 2446): ("retained adapter: support magnitude guard (64-epsilon) against its components", DEC, "none", "I109: norm3"),
    ("core/product_physics/src/case_state/resolve.rs", 899): ("load reference: member reference length (published reference_length_m; fit strain = change/length)", PUB, "RS, PY, TS recompute fit_strain = change/length exactly from the published length; none recomputes the length", "I109: norm3"),
    ("core/product_physics/src/case_state/resolve.rs", 900): ("(same expression)", PUB, "as above", "I109: norm3"),
    ("core/product_physics/src/case_state/thermal.rs", 484): ("logarithmic path stretch exp(integral), checked > 0", DEC, "none", "recommend: correctly rounded exp (or exact reformulation not available)"),
    ("core/product_physics/src/case_state/thermal.rs", 666): ("installation logarithmic stretch exp(d_i) (published)", PUB, "readers check the published composition, not exp", "recommend: correctly rounded exp"),
    ("core/product_physics/src/case_state/thermal.rs", 667): ("operating logarithmic stretch exp(d_o) (published)", PUB, "as above", "recommend: correctly rounded exp"),
    ("core/product_physics/src/case_state/thermal.rs", 674): ("logarithmic thermal strain expm1(delta) (published, drives thermal loads)", PUB, "as above", "recommend: correctly rounded expm1"),
    ("core/solver/frame_kernel/src/rigid_body.rs", 52): ("rigid-body screen: characteristic length max |r|", DEC, "none", "I109: norm3"),
    ("core/solver/frame_kernel/src/rigid_body.rs", 108): ("rigid-body screen: Jacobi rotation sqrt(zeta^2 + 1)", DEC, "none", "I109: norm2"),
    ("core/solver/frame_kernel/src/structural/retained/product_certificate/final_case.rs", 1847): ("retained certificate: support magnitude projection |(Fx, Fy)|", PUB, NORM_READERS, "I109: norm3 (one rounding of the 3-norm)"),
    ("core/solver/frame_kernel/src/structural/retained/product_certificate/final_case.rs", 1850): ("retained certificate: support magnitude projection |(xy, Fz)|", PUB, NORM_READERS, "I109: norm3"),
    ("core/loads/stress_recovery/src/elastic_section.rs", 105): ("bending amplitude |(sigma_by, sigma_bz)| (stress rows, maxima)", PUB, "readers check published stress composition, not the norm", "I109: norm2"),
    ("core/solver/performance_harness/src/lib.rs", 1078): ("performance harness Jacobi rotation (not a product dependency)", "none (harness)", "none", "none"),
    ("core/solver/performance_harness/src/lib.rs", 1080): ("performance harness Jacobi rotation (not a product dependency)", "none (harness)", "none", "none"),
    ("core/solver/nonlinear_integration/src/structural_adapter.rs", 2040): ("curved symmetry formation: chord R(cos(phi) - 1)", PUB, "none", "recommend: as curved_bend"),
    ("core/solver/nonlinear_integration/src/structural_adapter.rs", 2041): ("curved symmetry formation: chord R sin(phi)", PUB, "none", "recommend: as curved_bend"),
    ("core/solver/curved_bend/src/lib.rs", 166): ("arc included angle phi = atan2(|n|, ri.rj)", PUB, "none", "recommend: correctly rounded atan2 (sin/cos of phi then exact from the vectors)"),
}
CURVED = {
    (247, 248): "local stiffness: chord terms R(cos phi - 1), R sin phi",
    (302, 303): "consistent uniform nodal loads: R^2(sin phi - phi), R^2(1 - cos phi)",
    (316, 317): "consistent uniform nodal loads: chord terms",
    (415, 416, 425, 428, 439, 440): "arc section resultants at theta: cos/sin of phi and theta",
    (463, 464): "end tangents (-sin phi, cos phi)",
    (521, 522, 523, 528, 529): "radial pressure nodal loads: thrust sin/cos terms",
    (587, 588, 589): "section resultants with radial pressure",
    (624, 625, 629): "section resultant terms",
    (737, 738): "unit load actions: sin/cos of phi",
    (814, 815): "distributed load actions: sin/cos of phi",
    (877, 878): "radial pressure load actions: sin/cos of phi",
    (894, 895, 896, 897): "trig extended Gram: sin/cos of phi and 2 phi",
    (968, 969, 970): "trig Gram: sin/cos of phi and 2 phi",
}
for lines, what in CURVED.items():
    for ln in lines:
        PROD[("core/solver/curved_bend/src/lib.rs", ln)] = ("curved bend " + what, PUB + " (every model with a bend: stiffness, loads, resultants)", "none",
                                                           "recommend: correctly rounded sin/cos (sin_cos) of phi; phi itself from a correctly rounded atan2")
POWI_PROD = {
    9333: "self-weight metal area pi/4 (od^2 - id^2)", 9354: "contents mass per length pi/4 id^2 rho", 9377: "insulation mass per length",
    10306: "section area", 10307: "internal area", 10308: "second moment pi (od^4 - id^4)/64", 13916: "displacement magnitude sqrt(ux^2 + uy^2 + uz^2)",
    13917: "(same)", 13918: "(same)",
}

TEST_NOTES = {
    "core/product_physics/src/lib.rs:18464": ("test expectation i*hypot(sigma_by, sigma_bz) under a 1e-9 relative tolerance", "test-only (toleranced)"),
    "core/product_physics/src/retained_memory_law_tests.rs:69": ("cap_maximal ring input (10 cos t, 10 sin t)", "pinned test value (W2b inputs and I81's PROBE pins; Linux differs)"),
    "core/product_physics/tests/common/b1_sq_inputs.rs:52": ("cap_maximal ring input, transcribed", "pinned test value (as above)"),
    "core/product_physics/src/s11f_tests.rs": ("test expectation |(My,Mz)|, |(Vy,Vz)| against end values (1e-9 relative)", "test-only (toleranced)"),
    "core/product_physics/src/s11g_tests.rs:389": ("test mirror of the formation guard's q = |(My,Mz)|", "test-only (comparison with B, not a pin)"),
    "core/product_physics/tests/preview_physics_runtime.rs:270": ("test expectation: support force magnitude = hypot chain (1e-9 relative)", "test-only (toleranced)"),
    "core/product_physics/tests/preview_physics_runtime.rs:271": ("test expectation: support moment magnitude = hypot chain (1e-9 relative)", "test-only (toleranced)"),
    "core/product_physics/tests/preview_physics_runtime.rs:279": ("test expectation: intensified = i*hypot(My,Mz)/Z, asserted equal (m08)", "pinned test value (exact equality; moved: m08)"),
    "core/product_physics/tests/preview_physics_runtime.rs:428": ("test input: 30-degree skew direction cos/sin", "test input (outputs toleranced)"),
    "core/product_physics/tests/support_reactions_runtime.rs": ("test expectation: support magnitude of exact integers (hypot chain of 1000,2000,3000 and 400,2500,2600)", "test-only (toleranced)"),
    "core/product_physics/src/case_state/thermal.rs:991": ("test expectation expm1(0.0015) for the published strain", "pinned test value (close)"),
    "core/solver/curved_bend/src/lib.rs": ("curved-bend tests: geometry inputs and analytic expectations", "test-only (toleranced)"),
    "core/solver/frame_kernel/src/structural/formation_check_tests.rs:298": ("test input angle atan2(5e-20, -1)", "test input"),
    "core/solver/frame_kernel/src/structural/sparse/tests.rs:202": ("test input geometry 0.05 sin(0.7 t)", "test input"),
    "core/solver/sparse_direct/src/structural/k1_tests.rs:248": ("test input geometry 0.05 sin(0.7 t)", "test input"),
    "core/solver/frame_kernel/tests/m03_skew_scope.rs": ("test diagnostics log2/log10 of measured scales, toleranced", "test-only (toleranced)"),
    "core/solver/frame_kernel/tests/retained_k4/product_final_case_tests.rs:342": ("test expectation: support projection = hypot chain, bitwise (3,4,12; zeros; subnormals 1,2,3)", "pinned test value (bitwise; the chain and the 3-norm agree on these inputs)"),
    "core/solver/nonlinear_integration/src/structural_adapter/k1_tests.rs": ("test inputs (30-degree skew; sin perturbations)", "test input"),
    "core/solver/nonlinear_integration/src/structural_adapter/k2b_tests.rs": ("test expectation Mb = hypot(My, Mz) of published end forces", "test-only (toleranced)"),
    "core/solver/performance_harness/src/lib.rs": ("harness test expectation cos(pi/33)", "test-only (toleranced)"),
    "core/loads/stress_recovery/src/elastic_section.rs:272": ("test sweep angle sin_cos", "test-only (toleranced)"),
    "core/reporting/result_export/tests/preview_physics_contract.rs": ("test fixture construction: displacement magnitude hypot chain", "test input (reader guard)"),
}
POW2 = re.compile(r"\b2(\.0)?(_?f64)?\s*\.\s*powi\s*\(|\b2f64\s*\.\s*powi\s*\(|\b10f64\s*\.\s*powi\s*\(")
PY_POW2 = re.compile(r"\b2(\.0)?\s*\*\*")


def classify(row):
    path, line, fn, ctx, lang, src = row
    line = int(line)
    reader = path.startswith((RS_READER, PY_READER, TS_READER)) and ctx == "prod"
    if ctx == "prod" and (path, line) == ("core/product_physics/src/preview_physics.rs", 465) and fn == "atan2":
        return "prod", "curved-bend tangent discontinuity angle atan2(|cross|, dot)", DEC + "; " + TXT, "none", "libm", "recommend: correctly rounded atan2, or test |cross| > tan(tol)*dot without forming the angle (the printed angle still needs atan2)"
    if ctx == "prod" and (path, line) in PROD:
        c, r, rd, a = PROD[(path, line)]
        platform = "libm" if fn in ("hypot", "sin", "cos", "atan2", "asin", "exp", "exp_m1") else "fixed"
        if path.startswith(RS_READER):
            return "reader", c, r, rd, platform, a
        return "prod", c, r, rd, platform, a
    if fn == "powi" or fn == "**":
        if POW2.search(src) if fn == "powi" else PY_POW2.search(src):
            what = "power of two 2^k (10^k in two tests)"
            return ("reader" if reader else ctx), what, ("reader decision (exact scale)" if reader else ("test-only" if ctx == "test" else "exact scaling (no rounding; round-trip checked where the exponent is computed)")), "n/a", "exact (2^k)", "none"
        if path == "core/product_physics/src/lib.rs" and ctx == "prod":
            return "prod", POWI_PROD.get(line, "integer power"), PUB, "displacement magnitude: readers recompute with hypot under the guard" if line >= 13916 else "none", "fixed (x*x by squaring)", "recommend: spell as x*x / (x*x)*(x*x) (same bits; Rust leaves powi's precision unspecified)"
        if path == "core/solver/straight_pipe/src/lib.rs" and ctx == "prod":
            return "prod", "partial uniform load fixed-end terms b^3, b^4", PUB, "none", "fixed (x*(x*x), (x*x)*(x*x))", "recommend: spell the products (same bits)"
        if path.startswith(PY_READER) and fn == "**":
            return "reader", "outward-rounded norm bound: (v/scale)**2", "reader decision (outward-rounded enclosure)", "n/a", "libm pow(x, 2)", "recommend: v*v (exact RN of the square)"
        if path.startswith(TS_READER) and fn == "**":
            return "reader", "power of two with an integer exponent", "reader decision", "n/a", "exact (2^k)", "none"
        return ctx, "integer power in a test", "test-only", "n/a", "fixed", "none"
    if fn == "to_radians" or fn == "to_degrees":
        return ctx if not reader else "reader", "degree/radian conversion (one multiplication)", "test input" if ctx == "test" else TXT, "n/a", "fixed", "none"
    if reader:
        if fn == "hypot":
            return "reader", "reader recomputation of a published norm", RDR, "n/a", "CPython/engine hypot" if not path.startswith(RS_READER) else "libm", "none needed (1 ulp is far inside 64 epsilon); optional: mirror norm3"
    if ctx == "test":
        for key, (c, r) in TEST_NOTES.items():
            if f"{path}:{line}" == key or path == key:
                return "test", c, r, "n/a", "libm" if fn not in ("powi", "to_radians", "to_degrees") else "fixed", "none (measured below where it moved)"
        return "test", "test computation", "test-only", "n/a", "libm", "none"
    return ctx, "UNCLASSIFIED", "?", "?", "?", "?"


def main():
    rows = [l.rstrip("\n").split("\t") for l in open(sys.argv[1], encoding="utf-8")][1:]
    grouped = collections.OrderedDict()
    for r in rows:
        key = (r[0], r[1], r[2])
        grouped.setdefault(key, [r, 0])
        grouped[key][1] += 1
    out = []
    for (path, line, fn), (r, n) in grouped.items():
        ctx, c, reach, rd, platform, action = classify(r)
        out.append([path, line, fn, str(n), ctx, c, reach, rd, platform, action])
    with open(sys.argv[2], "w", encoding="utf-8") as f:
        f.write("path\tline\tfunction\tcalls\tcontext\tcomputes\treaches\treaders_recompute\tplatform\taction\n")
        for o in out:
            f.write("\t".join(o) + "\n")
    summary = collections.Counter()
    for o in out:
        summary[(o[4], o[8], o[2])] += int(o[3])
    by_ctx = collections.Counter()
    for o in out:
        by_ctx[o[4]] += int(o[3])
    lib = [o for o in out if o[8].startswith("libm") or o[8].startswith("CPython") or o[8].startswith("libm pow")]
    res = {
        "sites_lines": len(out), "calls": sum(int(o[3]) for o in out), "calls_by_context": by_ctx,
        "unclassified": [o for o in out if o[5] == "UNCLASSIFIED"],
        "prod_libm_calls_by_function": collections.Counter({o[2]: 0 for o in out}),
        "replaced_by_i109": sum(int(o[3]) for o in out if o[9].startswith("I109")),
        "replaced_lines": sum(1 for o in out if o[9].startswith("I109")),
    }
    pl = collections.Counter()
    for o in out:
        if o[4] == "prod" and o[8] == "libm":
            pl[o[2]] += int(o[3])
    res["prod_libm_calls_by_function"] = pl
    rl = collections.Counter()
    for o in out:
        if o[4] == "reader":
            rl[(o[2], o[8])] += int(o[3])
    res["reader_calls"] = {f"{k[0]} ({k[1]})": v for k, v in rl.items()}
    tl = collections.Counter()
    for o in out:
        if o[4] == "test":
            tl[(o[2], o[8], o[6])] += int(o[3])
    res["test_calls"] = {f"{k[0]} | {k[1]} | {k[2]}": v for k, v in sorted(tl.items())}
    json.dump(res, open(sys.argv[3], "w"), indent=1, default=str)
    print(json.dumps({k: v for k, v in res.items() if k not in ("test_calls",)}, default=str, indent=1))


if __name__ == "__main__":
    main()
