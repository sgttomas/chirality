# Exact72 local Cargo artifact collision

Confirmed local build-output contamination, not a demonstrated product-source or lockfile defect. The original clean sweep failure and all five compiler errors remain preserved in the parent sweep.log and summary.

Candidate72f09c4b195b1cb9e6576eafa963997a1b289a01 uses independent crate lockfiles. operation_applier's own graph pins serde_json1.0.150/serde1.0.228; physics_audit_regression resolves the same path dependency with serde_json1.0.151/serde1.0.229. The benchmark's metadata/tree contain one serde_json version. Both are valid separate lock closures. The operation crate builds cdylib+rlib, whose rlib output is debug/deps/libopen_pipe_stress_operation_applier.rlib, without the ordinary hashed suffix.

The failed sweep reused /private/tmp/piping-solver-correctness-target across independent checkouts and crate graphs. Verbose narrow reproduction exits101: Cargo calls operation_applier Fresh, passes the unhashed rlib to rustc, and rustc sees the1.150 type while the direct dependency is1.151. pre-run-artifacts.json and fingerprints retain the earlier distinct fingerprints and shared output identity.

A controlled fresh-target experiment on unchanged source/locks establishes causality:

1. Compile/run the exact authored_units_product benchmark in a new empty target: exit0, all5 tests pass. rlib SHA b94e6d75aa902875a43ef5e98904d8426c8d5315f44261edf76c0ab08a55d4c1.
2. Build operation_applier as its own locked graph in that same target: exit0; the same output filename becomes SHA541132a78bc0ffb95ccae8354f7349e77b0a1911c1f532e80d5db1ca9d190a73.
3. Compile the unchanged benchmark again: Cargo says the path dependency is Fresh, retains the second rlib SHA and exits101 with the same5 type errors.

isolation-control.py, isolation-control.json and three raw logs preserve commands, times, target path, hashes and exits. shared-reproduction.py is named reproduce.py; shared-reproduction.json/log preserve the original-cache reproduction. metadata.stdout/tree.stdout/versions.stdout bind dependencies and compiler.

Remedy for subsequent local qualification: unset ROOT's cross-manifest CARGO_TARGET_DIR override so each independent manifest uses its own target directory; use isolated named targets for standalone/native qualification. Preserve old targets as diagnostic evidence. This changes the run environment, not product source, dependency versions, tests, or protected criteria. Hosted exact72 run36048742883 already used a fresh run-specific target and passed1098 tests. No new full clean sweep pass is asserted by this diagnosis. A fresh registered sweep on exact72 remains required.
