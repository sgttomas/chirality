# Orbit projection rejection diagnosis and source repair

Manager supplied focused run01 result: 132 total, 131 passed, failure at label pick projection camera validation. Delegated TASK read software-defect-diagnosis skill and the manager-owned deterministic probe `_run_records/projection-camera-probe.txt`. No child execution was performed; reproduction custody remains with manager.

Expected: normal rigid THREE camera at (6,5,9), looking at origin, admits finite anchor and pick projection. Observed probe: inverse bottom row (0,0,0,0.9999999999999999), axis length squares approximately 1 and pairwise dots approximately 1e-16. Earliest divergence is the adapter's literal v[15] !== 1 check, before geometry projection. Confidence high: deterministic numeric evidence isolates this predicate; malformed target geometry is not implicated.

Repair: require a genuinely affine inverse bottom row (three exact zeros and nonzero finite homogeneous w), then divide linear axes by w for rigidity validation. This agrees with THREE Vector3.applyMatrix4, which divides transformed coordinates by homogeneous w. A globally rescaled homogeneous matrix therefore retains identical Euclidean geometry, while scaled/sheared normalized transforms still fail the existing rigidity checks. This changes representation validation, not geometry tolerance or test expectations. Input matrices remain unmodified.

Regression authored: ordinary orbit projects origin to canvas center and produces a target; explicit homogeneous rescaling preserves both; non-affine bottom row is rejected. Existing scaled-camera rejection and every per-scenario actual-picker sample remain intact. Manager must run focused checks and backcheck remaining failures before claiming repair verified. No typecheck/test/build/native/performance or qualification claim from this child.

Affected callers: anchor and pick-target projection share camera admission; downstream label placement can now receive valid orbit results instead of unavailable-projection state. Remaining uncertainty is execution validation against actual installed THREE/types and full suite. No alternative camera policy, picker or core changes made.
