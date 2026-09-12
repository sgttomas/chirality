# Proposed isolated supplier repair scope — not executed

Decision requested after independent review: authorize one minimal supplier base-policy change, one isolated offline build of codex, and account-free qualification; packaging/native owner rerun remains a separate explicit continuation. No Runtime behavior change is proposed.

## Candidate

`CANDIDATE.patch` adds exactly one allow rule to `codex-rs/sandboxing/src/seatbelt_base_policy.sbpl`: file-read-data on literal `/` constrained to DIRECTORY. Candidate/before bytes and SHA256 are recorded in CANDIDATE_IDENTITY.json. These are evidence copies only; retained supplier source has not been edited.

The candidate adds a specific root-directory read capability, not a no-capability-broadening claim. Immediate root directory entries may be readable; descendant files, recursive subpaths, root writes and network are not authorized by this rule. Account authority, lease protocol, identity/epoch checks, credential custody, command policy, other protected denies and host-only JIT entitlement remain unchanged. Never substitute recursive immutableReadRoots `/` or wholesale platform defaults.

Controlled results in this packet: base cat/zsh both SIGABRT with empty output; exact DIRECTORY treatment both exit0/expected fixture text; synthetic protected read/write both EPERM and no output file. `RETURN.md` records single-grant and metadata/existence minimization. Inner base is the affected layer; v2 worker requires direct supplier launch (Runtime codex-containment.ts117-120/177-178 and codex-authenticated-transport.ts316-320); legacy/login outer already permits literal-root read-data. No independent outer-policy fix is required.

## Existing build basis and preservation

Canonical recipe files: `projects/chirality-runtime/tools/codex-supplier/README.md`, `build-invocation.json`, `build-enclosure.sb`, `source-build.json`, `codex-local-trial.patch`.

- Upstream commit: 758ef40f50c1a458425c7cfbf1eb12cbc07af0b0.
- Current maintained patch SHA256: 91df1f91bd16ee72b24be89d2bb777a9bfc6eb90b8f764821619331e33613fe1.
- Retained build05 source: `/private/tmp/chirality-supplier-login-fix-20260911/source`.
- Retained Rust: `/Users/ryan/.rustup/toolchains/1.97.1-aarch64-apple-darwin`.
- Retained Cargo home/cache: `/private/tmp/chirality-supplier-release-20260910-02/cargo-exec-diagnostic-01`; registry basis also references `/private/tmp/chirality-supplier-release-20260910-02/cargo-home/registry`.
- Retained target: `/private/tmp/chirality-supplier-release-20260910-02/target`.
- Retained build05 artifact: `/private/tmp/chirality-supplier-release-20260910-02/evidence/trial-supplier-build-05/artifact/codex`, SHA256 eecbc73eea2d472cfefb285dcee6d7ca46024668c2e8d907a1452053c7745189.

All paths above and all current Apps, signed binaries, source/cache inputs remain unchanged. Before execution, freeze a new absolute-path recipe: independently copy/clone source, target (if reuse desired), and mutable Cargo cache bookkeeping into a fresh isolated build root; do not reuse the old target or Cargo bookkeeping as write destinations. Immutable dependency contents may be reused read-only under the mapped enclosure. This proposal does not authorize downloads/dependency updates or V8/host rebuilding.

Retain exact toolchain/lockfile/profile: dev profile with only sha2:0.10.9 opt-level3, target aarch64-apple-darwin, `cargo build --manifest-path <isolated-source>/codex-rs/cli/Cargo.toml --bin codex --locked --offline --target aarch64-apple-darwin`, sanitized recorded environment and network-denied enclosure remapped to new scratch/target/bookkeeping paths. Freeze that concrete mapped command/enclosure before dispatch. Changed supplier source inventory must contain only the proposed base-policy delta plus explicitly reviewed tests; preserve old build correspondence and create a new immutable build record.

## Qualification and downstream adoption

1. Verify source/lock correspondence and preserved old input hashes. Retain baseline/treatment tests and add an exact-rule regression to the supplier's existing Seatbelt test suite, including protected data/write negatives.
2. Build once under the approved isolated recipe; record exit, dependency/Mach-O identity, resulting SHA256 and full source correspondence. No public-release or bit-for-bit reproducibility claim.
3. Account-free actual supplier + unchanged official host, fake-provider shell operation with the exact generated restricted native policy: cat README, bounded shell write, protected-path negative, normal completion/interrupt and clean child retirement. Existing fake callback host tests alone are insufficient.
4. Re-run private authority and identity-snapshot regression cases affected by relinking; preserve account/lease/epoch semantics. Do not read real auth or contact a live model during these checks.
5. Following review acceptance, update maintained supplier patch/provenance and affected release/support/supply descriptors and source correspondence through their owning workflows. New signing and Stage/App packaging must measure the new codex bytes while preserving the existing host's accepted entitlement/correspondence policy.
6. Final owner native qualification: existing text/image/native-plan flows, actual shell README read + bounded file write, explicit protected-path denial, interruption→next turn, account readiness and clean retirement. No closure until genuine native tool results are observed.

Current status: proposal/evidence only. No supplier source mutation, compilation, signing, Runtime edit, real account operation, or App restart performed by this worker. Lead owns combined disposition after the current UI pass.
