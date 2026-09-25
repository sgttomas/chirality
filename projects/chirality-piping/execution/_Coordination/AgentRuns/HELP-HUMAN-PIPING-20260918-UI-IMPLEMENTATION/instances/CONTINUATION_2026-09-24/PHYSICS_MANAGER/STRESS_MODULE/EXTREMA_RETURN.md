# Bounded elastic extrema return

Implemented only `core/loads/stress_recovery/src/elastic_extrema.rs` and assigned STRESS_MODULE evidence. The subsequent TASK assignment explicitly authorized this new helper after the earlier per-section return. No lib.rs, facade, station-coefficient constructor, test tolerance, Git, browser/native/config or other production file was changed. `EXTREMA_REFERENCE_DISPOSITION.md` records the independently proved method and arithmetic envelope **before source implementation**. Fresh independent review of this implementation remains outstanding.

## API

`bound_piecewise_elastic_maximum(spans: &[QuadraticStressSpan]) -> Result<CertifiedStressMaximum, ExtremaError>`.

`QuadraticStressSpan` fields: `start`, `end`, `axial: [f64;3]`, `bending_y: [f64;3]`, `bending_z: [f64;3]`. The three arrays are degree-two Bernstein stress coefficients in Pa on local u∈[0,1]. Each closed span is retained separately, including both sides of discontinuities. Input coefficients are treated as exact supplied f64 values; the caller owns whether these represent the actual statics and any uncertainty from their construction/solver/material basis.

`CertifiedStressMaximum` fields: `span_index`, `local_fraction`, `station`, `value_lower`, `value_upper`, `upper_bound`, `certified_gap`, `subdivisions`. The true supplied-polynomial global maximum is in `[value_lower, upper_bound]`; the objective at the returned dyadic witness is in `[value_lower, value_upper]`. `station` is a rounded presentation coordinate. Preserve `span_index` plus exact dyadic `local_fraction`, especially on adjacent-float intervals where that display coordinate can round to an endpoint. This is a maximizing witness within the certified value gap, not proof of the exact unique argmax. For a conservative global scalar use `upper_bound` and retain its bound status; do not present that upper bound as an exactly evaluated stress at the witness.

Errors distinguish empty input, invalid interval, nonfinite coefficient, unrepresentable enclosure, and `Unresolved { best, reason }`. Unresolved reasons are `SubdivisionLimit` and `DepthLimit`; `best` retains current witness/lower/upper bounds for diagnostics but is not a qualified complete maximum. A bound failure does not silently become zero or a sampled maximum.

## Numerical bound and work

The objective |a|+hypot(b,c) is convex in the three stress components. A quadratic Bernstein vector curve is a convex combination of its three vector controls, so their greatest objective bounds the complete curve. Outward interval de Casteljau subdivision preserves enclosure. Absolute-component bounds and a scaled sqrt norm yield lower/upper objective enclosures; every relevant primitive arithmetic operation is expanded toward the appropriate adjacent f64 value. `hypot` is deliberately not used in the certificate because Rust does not promise correctly rounded hypot; sqrt does carry that guarantee. The arithmetic argument assumes ordinary IEEE-754 operations, gradual underflow and no fast-math/reassociation; no arbitrary compiler-mode or coefficient-error certification is claimed.

All unresolved subdomains remain in a maximum-upper-bound heap, unless their bound is no greater than an attained lower bound. Child upper bounds are intersected with the valid parent upper bound. Success requires outward gap no larger than a downward-rounded `1e-12 Pa + 1e-12*value_lower`. This stricter internal stopping rule does not change the original 1e-9 physical oracle. At most 131072 subdivisions and depth48 are allowed; storage O(input spans + subdivisions), work O((input spans + subdivisions) log(input spans + subdivisions)). Roundoff can prevent closure; limits return unresolved.

## Checks performed

One standalone rustc build and single-threaded test run passed all 12 tests; rustfmt check passed. Raw commands/toolchain/source hash/results are `_run_records/extrema-execution-01.json`, `extrema-build-01.log`, `extrema-run-01.log`. Tests cover X1 exact peak enclosure and strict improvement over old candidates; zero/constant biaxial fields; axial zero crossings and simultaneous bending zeros; repeated derivative root; exact interior quadratic maximum; both sides of a discontinuity; adjacent-float short interval; quarter-axis rotation/action reversal; explicit search-limit failures; invalid/nonrepresentable inputs; overflow-safe scaled norms; subnormal values; directed averages at extreme magnitudes.

X1's true peak at (6−sqrt(2))/8, value sqrt(71+8sqrt(2))/8 MPa, is enclosed with the stated gap and a witness within 2e-6 in local parameter. Its lower bound strictly exceeds the best new-objective value at the old eight-sign candidates. The X1 test completed in fewer than 1000 subdivisions. These are actual test assertions; no implementation output was replaced by oracle constants. The module is not yet exported/adopted by the crate, so no Cargo/facade/headless/native/DEC-025 claim follows.

## Caller integration check

The manager's planned j-side derivatives agree with current lower statics plus the facade's negation of **all six** i-side components: N'=-wx, My'=Vz, Mz'=-Vy, My''=-wz, Mz''=+wy. On an active uniform-load interval of physical length h, power coefficients are [N,-wx*h,0]/A; [My,Vz*h,-wz*h²/2]/Z; [Mz,-Vy*h,+wy*h²/2]/Z. Converting a proven quadratic [c0,c1,c2] to Bernstein [c0,c0+c1/2,c0+c1+c2] follows coefficient matching. This check does not authorize deriving an unknown function's polynomial from three samples.

Split wherever loads, section/pressure/material/factor basis or formula changes; preserve point-load one-sided results and include every required domain. Reconstruct physical wall axial force once; add any constant wall-pressure correction to all axial Bernstein controls once. Pressure solution/coefficient arithmetic error remains outside this helper's certificate. Retain section/frame/cut/case and supplied-span provenance with outputs; curved/nonquadratic fields require their own qualification. Independent reviewer should inspect both this helper's arithmetic and the caller's field construction before any live maximum is treated as complete.
