# Codex local trial supplier

This directory maintains the exact source patch and build correspondence for the ARM64 macOS local trial supplier. The executable uses Cargo's **dev profile with only sha2 0.10.9 optimized at level 3**. It is not an optimized public release or a vendor-signed OpenAI distribution.

`source-build.json` pins upstream commit, the complete 93-file upstream delta, patch hash, compiled source snapshot digest, and original executable identity. `codex-local-trial.patch` applies to the pinned upstream commit; an isolated-index `git apply --cached --check` passed. It includes the accepted dependency lockfile adjustment; builds must use that exact lockfile. Build04 includes the final retained test-only source. The prior build03 patch and provenance remain under `history/build03/`.

## Reproduction

Use an isolated checkout of the pinned upstream commit and apply `codex-local-trial.patch`. Verify every changed-file SHA256 against `source-build.json` before building. Provision the already-approved immutable Cargo dependency cache separately; this recipe grants no network fetch or dependency acquisition.

`build-invocation.json` preserves the exact successful argv, sanitized environment, source location, target, and profile. `build-enclosure.sb` preserves the actual macOS compiler enclosure. Its absolute isolated-workspace paths must be mapped consistently for another local workspace, while retaining network denial, protected source/dependency payloads and the limited target/cache bookkeeping write scope. Use the pinned Rust 1.97.1 aarch64-apple-darwin toolchain and the command:

```sh
cargo build --manifest-path codex-rs/cli/Cargo.toml --bin codex --locked --offline --target aarch64-apple-darwin
```

Run only inside the recorded enclosure and sanitized environment. The command deliberately omits `--release`. Reproduction means source and process correspondence; debug absolute paths and toolchain/platform inputs may affect binary bytes, so bit-for-bit rebuilding is not asserted.

## Payload and evidence

The declared original payload root contains only `codex`. Mach-O dependencies resolve exclusively to macOS system frameworks and libraries; no non-system dylib sidecar was identified. Other external tools used by optional Codex functionality are outside this payload statement. The linker supplies an ad-hoc signature with no team identity. Packaging owns any subsequent nested signing and must measure its resulting bytes separately.

The source has independent lifecycle/authority review and an actual no-model initial/idle V2 lifecycle pass at the default test stack after the targeted turn-context allocation repair. CHECK_CONNECTED_06 and CHECK_REVOCATION_02 passed their two bounded routing cases, and the final independent backcheck accepted that evidence. The revocation case demonstrates integrated rejection with no observed next turn, not isolation of the consumption-time guard. Broader combined fork/resume-history and queue-only durable-sleep scenarios remain unqualified. The historical build03 test-only changes remain in `post-build-tests.patch`; they are now included in build04 inputs and are not claimed as newly rerun tests. The human owns the first account/model end-to-end trial. See `source-build.json` for preserved build evidence and original artifact location.

The successful link emitted a large `__eh_frame` compact-unwind performance warning. It did not prevent the dev artifact build.

Build04 changes only the sha2 0.10.9 package optimization relative to the retained final source. It uses the existing pure-Rust backend, unchanged features and lockfile. Its offline build passed; startup improvement remains subject to measurement on the new signed artifact. The earlier 32.103-second diagnostic measured total initialization, not isolated hashing.
