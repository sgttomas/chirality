# Separately identified patched-supply build feasibility

Read-only preparation by OpenAI GPT-6 ephemeral Agent2; exact serving ID unavailable, role instruction-asserted. No clone, build, downloaded-source execution, vendor invocation or signing occurred. Official source files were read and hashed in memory; SOURCE_PINS.json records exact URLs and digests.

## Outcome and correction

A reviewable candidate build is technically plausible. Official rust-v0.149.0 exists: annotated tag object a4e15bf371341b067c8278d3b70b1a8c7b3d793e peels to commit758ef40f50c1a458425c7cfbf1eb12cbc07af0b0, verified by git ls-remote. Earlier claims that the tag was unavailable were too broad: the first404 was a missing/obsolete file path. Exact-tag sandboxing/src/seatbelt_base_policy.sbpl is available and lacks the literal-root addition. This correction supersedes earlier uncertainty about tag availability, without rewriting historical records.

The source release relationship does not prove byte-for-byte provenance of the accepted vendor payload. Accepted local payload remains SHA256 b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2 and its current invalid-signature finding. The candidate must have its own identity even if its program-reported version remains0.149.0.

## Authority distinction

No inspected rule makes mere candidate source preparation/build the G2 owner-acceptance act. R15 limits reliance on the accepted supply; it does not state that an isolated different candidate cannot be prepared. The present parent brief explicitly stops this subtask before clone/build and new scratch scope has not yet been declared; that is a run-scope boundary, not an inferred permanent owner prohibition. Parent may release a bounded preparation brief under the user's ongoing implementation direction. It must name source/download/build-script execution, scratch/tool/cache write roots and controlled tests explicitly. The later candidate acceptance, changed pin, production reliance, signature disposition and release remain their named acts.

## Source and tools

Immutable source/build inputs are pinned in SOURCE_PINS.json: workspace Cargo.toml/lock, rust-toolchain, app-server Cargo manifest, patch target, release workflow and rusty-v8 setup action. Dedicated package/bin is codex-app-server. Upstream macOS app-server bundle also builds codex-code-mode-host.

Host read-only inspection: Rust and Cargo1.97.1, Xcode26.6/17F113, clang and codesign available. Rust1.95.0 is required by the source toolchain and is not installed in current rustup list. cmake/ninja/pkg-config/protoc were not found on current PATH; they are not asserted mandatory until dependency/build scripts are inspected. Upstream release uses checksum-verified rusty_v8 artifact configuration, CLI git fetching for dependencies and a separate protected signing process. It is a substantial build, not a single-file compile; upstream allows90minutes for its build job, which is not a runtime estimate or promise for this host.

Sources: https://github.com/openai/codex/releases/tag/rust-v0.149.0; commit-addressed URLs in SOURCE_PINS.json. No installed toolchain/cache is to be replaced silently.

## Exact proposed scope and sequence

1. Parent declares a fresh quarantined source/build directory, isolated CARGO_HOME/RUSTUP_HOME/target/temp roots and an evidence output directory. Accepted binary remains read-only and separately hashed. Obtain only official source at the pinned commit; verify tree, source-file digests and lockfile. Do not fetch another branch as substitute.
2. Review Cargo configuration, all reachable build.rs/proc-macro setup and referenced artifact downloader/checksum scripts before running the build. Inventory network destinations for source/crates/git/V8/toolchain acquisition. Resolve any required native build tools in declared scratch, not global installation. Pin fetched content and record dependency provenance. Avoid inheriting account or signing credentials.
3. Prepare Rust1.95.0 in the declared toolchain root. Fetch locked dependencies/artifacts with recorded hashes, then attempt offline/frozen builds so unexpected dependency mutation fails. Exact command basis: cargo build --frozen --target aarch64-apple-darwin --release --bin codex-app-server --bin codex-code-mode-host from codex-rs. Apply the exact upstream rusty_v8 checksum setup after review. If a dependency cannot be fetched/verified or a build step writes beyond declared roots, stop that step and report its concrete requirement.
4. Build an unmodified source baseline first when practical; record its hash and complete environment. No assertion it must match the vendor signed artifact. Apply only candidate.patch to the separate source candidate; verify unchanged Cargo.lock/source tree outside patch and explicit local regression tests. Rebuild using the same toolchain/dependency cache and environment. Label output locally patched candidate, never unchanged accepted vendor supply.
5. Record unsigned/pre-signature bytes, Mach-O architecture, dependencies, embedded version/source metadata and licenses. If macOS requires ad-hoc signing solely to execute a controlled candidate, record it as a separate locally ad-hoc-signed artifact with a new hash, not a vendor signature or release signature. Do not access release keys or dispose the original signature finding.
6. Parent authorizes bounded no-account/no-external-provider candidate execution only after source/build review. Repeat literal-root positive/negative differential, actual named-profile/config readback, harmless system command startup, sibling/account/broker/config/protected-glob reads and writes, temp exclusions, command-network denial, primary/native descendant parity, interruption and process reconciliation. Compare unmodified-source versus patched-source behavior to attribute the fix.
7. Produce immutable candidate manifest, exact source diff, toolchain/dependency inventory, build logs, both artifact hashes and independent review. Claim reproducibility only to the level actually tested; optionally repeat in a second fresh build directory and report differences. Present that concrete package for changed-supply/G2/pin/reliance decisions. No accepted pin, production launcher or compatibility binding is changed by preparation.

## Candidate acceptance boundary

Passing the build proves buildability, not complete G-SBX/G-PROT or release. Production adoption requires the newly identified supply's actual acceptance and appropriate downstream identity/contract references. R13-B original signature issue, Root boundary authority, runtime source identity and held compatibility/release acts must retain their exact dispositions. No broader reads, :minimal preset, account grant or command-network enablement is part of this patch.
