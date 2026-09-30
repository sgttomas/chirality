# Performed checks and proposed future commands

Aliases: `Run=projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260930-T3-AUDIT-RESPONSE`;
`A1=Run/instances/A1-DIAGNOSIS`. Resolve `REPO_ROOT` through
`git rev-parse --show-toplevel`. Resolve `RESPONSE_RUNTIME` through
`Path(tempfile.gettempdir()) / Run/RUNTIME_BINDING.json.runtime_directory_name`.
All commands below run from the Git-derived root unless stated otherwise.

Preparation performed: `pwd`, read-only `git rev-parse` and `git show`, bounded
`rg`/`sed`/`cat` reads, file hashing and owned source/record writes. No Rust
command, model, provider, guard, signal, install, network or Git/index write ran.
The exact reproducible preparation checks are:

```sh
python3 "$REPO_ROOT/$A1/oracle.py" generate
python3 "$REPO_ROOT/$A1/oracle.py" self-check > "$REPO_ROOT/$A1/SELF_CHECK.json"
python3 "$REPO_ROOT/$A1/verify_snapshot.py" > "$REPO_ROOT/$A1/SNAPSHOT_VERIFICATION.json"
```

All exited 0. `generate` created 24 inputs and 880 truth rows. Pure checks
passed 1,565 rounding/boundary checks, all exact free-DOF equilibria, all eight
C RHS projections, the C17 pivot/residual inequalities and C23 relative ratios.
Pure synthetic comparator checks also cover malformed p/P, duplicate scales
and floors, missing p=512 floor, unexpected underflow, and detection of the
absolute, zero-bound and relative claim errors. These are oracle unit fixtures,
not solver output or substitutions into a retained state.
Snapshot verification found exactly 36 files and every snapshot hash matched
the sealed manifest, frozen Git object and inspected working-tree byte stream.
The installed cargo/rustc executables were read and hashed, never invoked.
No runtime stdout/stderr exists: `matrix.json` marks every case `UNRUN`.

The preserved files copied byte-for-byte into `RESPONSE_RUNTIME/scratch/a1-diagnosis`
are `Cargo.toml`, `oracle.py`, `matrix.json`, `src/main.rs`, and `src/cases.rs`.
`SCRATCH_COPY.json` records their hashes. The source snapshot and target directory
were not changed. The target remains reserved and unused by this checkpoint.

## Future gated commands — inert plan only

ROOT must first accept budgets/timeouts, qualify and activate the guard for
the exact owned process group and child target, check fresh headroom and grant
the single heavy slot. The guard supervisor's exact wrapper argv is owned by
ROOT and remains to be bound to these child argv; no unsupervised fallback is
authorized. Do not execute a shell loop across all cases.

Use these portable paths:

```sh
A1_SCRATCH="$RESPONSE_RUNTIME/scratch/a1-diagnosis"
A1_TARGET="$RESPONSE_RUNTIME/targets/a1/3bddc2b05f6106e969c7cf43373b230845c7cc66"
A1_TOOLCHAIN="$RESPONSE_RUNTIME/rustup/toolchains/1.97.1-aarch64-apple-darwin"
```

For each admitted child process, set `RUSTUP_HOME=$RESPONSE_RUNTIME/rustup`,
`CARGO_HOME=$RESPONSE_RUNTIME/cargo`,
`RUSTUP_TOOLCHAIN=1.97.1` exactly (ROOT's guard integration requirement),
`RUSTC=$A1_TOOLCHAIN/bin/rustc`, `CARGO_TARGET_DIR=$A1_TARGET`,
`CARGO_NET_OFFLINE=true`, `CARGO_BUILD_JOBS=1`, `CARGO_INCREMENTAL=0`, and
`RUST_TEST_THREADS=1`. Preserve HOME and CODEX_HOME. Unset `FK_SEEDED_FAULT`,
`RUSTFLAGS`, `CARGO_ENCODED_RUSTFLAGS`, `RUSTC_WRAPPER` and
`RUSTC_WORKSPACE_WRAPPER`. Record all applicable Cargo configuration files
before building; reject a configuration that changes source, toolchain, wrappers,
features or target. No `cfg(test)`, mutation feature or full-tree test is allowed.

The initially proposed lock-generation argv is preserved below for traceability.
ROOT's late guard integration message establishes that `generate-lockfile` is
outside the guard's compile grammar. It is therefore **not currently admissible**.
ROOT is considering an explicitly authored two-package version-4 lockfile,
later validated by a guarded offline locked build; that adjustment is not yet
granted and no lockfile has been created. Resolve this prerequisite before
admitting the subsequent build argv from `A1_SCRATCH`:

```sh
"$A1_TOOLCHAIN/bin/cargo" generate-lockfile --offline --manifest-path "$A1_SCRATCH/Cargo.toml"
"$A1_TOOLCHAIN/bin/cargo" build --offline --locked --manifest-path "$A1_SCRATCH/Cargo.toml" --bin a1_public_probe --no-default-features -j 1
```

Lock generation has not run. Preserve/hash the separately authorized lockfile
in A1 before the locked build. It should contain only this package and path dependency FK;
any other dependency or required registry access stops for review. Preserve
build stdout/stderr, exit status, elapsed time, feature metadata and resulting
binary hash. No installation is authorized if prerequisites are missing.

Initial B01 child argv, using the proposed budgets only if ROOT accepts them:

```sh
"$A1_TARGET/debug/a1_public_probe" B01 100000000 100000000 B
```

Capture complete raw stdout/stderr under A1 and run the lightweight comparator:

```sh
python3 "$REPO_ROOT/$A1/oracle.py" compare "$REPO_ROOT/$A1/results/B01.stdout.tsv"
```

Review the outcome and exact comparison before B02, continuing through B16
only while the grant and guard remain valid. Refusal is a named outcome,
never a pass. No retries, cap increases or changed input are implicit.
After the B checkpoint and separately granted C extension, use the same
single-case argv shape, first `C17 100000000 100000000 C`. A false claim stops
immediately. One repeat of the identical hashed source is allowed only if
ROOT's grant expressly permits it; no parameter search or new case is proposed.

## Dependency, feature and output limits

`Cargo.toml` has one path dependency on the 36-file FK snapshot, with
`default-features=false` and `features=[]`. FK itself has no dependencies and
only the `mutation-controls` feature. Probe dev profile: opt-level 0 by default,
debug info off, incremental off, one codegen unit and abort on panic. No external
crate, vendor change, lockfile fabrication or product edit is required.

Output format is `a1-public-tsv-v1`. Stable row keys are `D:<global DOF>`,
`M:<node>`, `E:1:<I|J>:<component index>`, `S:1:0`, and `R:<global DOF>`.
The probe prints source/stiffness encodings and layout before solving; then
meter, named outcome, p/P, every row's outcome/value/class/bound bits, body
scales, floor, source/ledger/state encodings, input-derived/absolute/unpublishable
lists, geometry, attempt reasons, correction/pivot/rcond/residual summaries,
stage/shared work and storage, E, theta, B, g, estimates and charges.
Opaque encodings are preserved bytes, not decoded into invented private state.

The independent comparator checks full row coverage, exact mathematical truth,
reconstructed scales/classes and bound bits. It preserves absolute error and
both relative-error denominators. Absolute qualification is `1+2^-22` for
p=128/256, `1+2^-21` for p=512; a zero bound demands exact equality. The relative
claim check follows D1 `DESIGN_NUMERICS/DESIGN.md` §4.1.6 lines 424–446:
`|error|/|q_published| <= 10^-9`. It separately reports the truth-denominator
ratio and its pass/fail. A denominator-only disagreement stops for explicit
disposition; C23's hypothesized publication breaches both. R1's separate
benchmark predicate is `|obs-exp| <= 10^-9 max(|exp|, class scale)`
(`REFERENCES/README.md:3–9`, also VP-ROBUST README:14–19); its class-scale
allowance is not substituted for the row-relative assurance investigated here.
The comparator requires P=2p, exact scale/floor inventories without duplicates,
and both force/moment floor entries at p=512. Unpublishable rows remain named
limits, and an unexpected exact-truth range discrepancy stops for review.
It does not turn underflow into a published value.
The comparator is not a complete receipt reader or independent verification
of the producer's internal B/theta/charge certificates. Inspect those summaries
and remaining D2 obligations separately. Compilation and end-to-end probe
compatibility remain unverified until the separately admitted build.
