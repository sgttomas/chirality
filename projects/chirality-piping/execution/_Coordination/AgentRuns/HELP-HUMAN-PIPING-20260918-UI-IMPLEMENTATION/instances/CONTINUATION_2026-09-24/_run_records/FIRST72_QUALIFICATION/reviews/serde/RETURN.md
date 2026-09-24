# Independent Cargo artifact-collision diagnosis review

**PASS — the controlled evidence supports the local shared-target rlib collision diagnosis. Removing ROOT's cross-manifest CARGO_TARGET_DIR override is an adequate environment remedy for the subsequent exact72 qualification attempt. No unresolved blocking diagnostic finding was identified. A full clean registered sweep still must run; this review supplies no replacement pass.**

TASK Type 2 `/root/integration_graph_review`, parent `/root`, performed a read-only captured-evidence review. MANIFEST.json freezes actual input origins/hashes and checks. No Cargo/test/build, Git, network, native or browser operation was run.

## Causal evidence

The three recorded stages use the same candidate HEAD72f09c4b, cwd, newly allocated target and two-job/offline settings. Commands are locked. Their raw log hashes match isolation-control.json; the original-cache reproduction hash matches its separate receipt.

1. The fresh benchmark compiles against serde_json1.0.151/serde1.0.229 and all5 authored_units_product tests pass. Its operation-applier library is emitted as cdylib+rlib without an extra-filename suffix, and the benchmark links the explicit unhashed libopen_pipe_stress_operation_applier.rlib path.
2. Building operation_applier as its own graph in that target compiles against the independently locked serde_json1.0.150/serde1.0.228 closure. The same rlib filename changes from recorded SHA b94e6d75 to541132a7. The dylib's recorded hash stays identical while its timestamp changes; the causally relevant changed artifact is the rlib.
3. Recompiling the unchanged benchmark calls the operation dependency Fresh, links that same overwritten path, and fails101. Its five error codes/messages exactly match the original shared-cache reproduction: three E0308 and two E0277 type incompatibilities. The final on-disk rlib matches the last recorded hash.

This is stronger than a clean rerun alone: an intervening build recreates the failure in a fresh target. The controlled compile commands expose different serde dependency artifacts feeding an identically named output, then stale freshness for that output. Metadata/tree contain one internally consistent benchmark serde closure. Both maintained lockfiles match the previously retained exact72 Git input bytes. All10 copied pre-run fingerprint files match their recorded hashes.

The evidence therefore warrants local build-output contamination as the demonstrated cause of this compiler failure. It does not establish a defect in the benchmark's resolved dependency graph or require changing product source, dependency versions, tests or protected tolerances. It also does not prove every Cargo/platform/cache configuration is affected.

## Remedy and remaining check

The registered runner iterates independent manifests with cargo test --manifest-path, inherits its environment, and supplies no target-dir override. Removing ROOT's common CARGO_TARGET_DIR lets these independent packages use their own target roots; the supplied benchmark metadata already records its local validation/benchmarks/physics_audit_regression/target path. No applicable Cargo config was found at the inspected cwd ancestors/default user config locations. Preserve existing diagnostic targets rather than deleting the evidence.

Keep the effective target directories distinct by independent lockfile graph and checkout/candidate. A new target shared across several graphs is insufficient: the controlled experiment itself began fresh and then collided. Named standalone/native targets must likewise belong to their actual graph/candidate. The hosted1098-pass record remains valid within its recorded run; its fresh run-specific target is not a general guarantee against this local collision pattern.

Before any success claim, perform the registered full sweep on exact72 with the override removed, retain the invocation environment/effective target basis, raw results and source/lock identity checks, and reassess any subsequent failure. The five fresh focused tests establish that bounded benchmark only. No full sweep, engineering, Current, native or release qualification follows from this diagnosis.

## Limits

ROOT supplied unchanged exact72 source as the experiment premise. The reviewer did not invoke Git or independently capture all source bytes before and after the parent experiment. Recorded HEAD, locked commands, retained lock closures and the controlled artifact transition support the bounded inference; this is not a fresh review of the complete product diff. Only this RETURN.md and MANIFEST.json were written in the assigned review directory.
