# Codex local trial supplier

This directory maintains the source patch and build correspondence for the
ARM64 macOS trial supplier. It uses Cargo's **dev profile with only sha2 0.10.9
optimized at level 3**. It is not an optimized public release or an OpenAI-signed
Codex distribution.

`source-build.json` pins upstream commit, the complete 94-file upstream delta,
compiled source snapshot and original executable identity. The latest change
adds only a literal-root DIRECTORY read-data rule to `seatbelt_base_policy.sbpl`.
It permits root-directory data, including immediate entry enumeration, so macOS
shell processes can start. It grants no recursive descendant-file access and
changes no account, lease, epoch or protocol behavior.

## Reproduction

Apply `codex-local-trial.patch` to the pinned upstream commit and verify its
changed-file identities against `source-build.json`. An isolated-index apply
check passed. Preserve the exact lockfile and use the recorded Rust 1.97.1
ARM64 toolchain. The successful command is the locked, offline Cargo build in
`build-invocation.json`; `build-enclosure.sb` records its actual compiler sandbox.
Map their isolated paths consistently when reproducing the process. This grants
no dependency acquisition, network access or unenclosed build fallback.

The recorded build used independently verified APFS clones of existing source,
dependency cache and target files. Original inputs remain unchanged. The source
snapshot excludes Git administration and records contained source symlinks
separately. Reproduction means source and process correspondence; debug paths and
platform inputs can affect executable bytes, so bit-for-bit rebuilding is not
asserted.

## Payload and qualification

The raw payload contains custom-built `codex` and an unchanged official
`codex-code-mode-host` from the matching OpenAI release. The patch and compiled
source claim apply to `codex`; the host has its own origin and measured identity.
Both binaries have only macOS system-library dependencies. Packaging owns nested
signing, the host-only JIT entitlement and measurement of resulting bytes.

Six direct restricted-policy shell probes and six actual supplier/host shell
turns passed. They cover reads, an allowed write, and protected/read-only denials.
The original pair test's overall FAIL remains preserved: raw turn interruption
intentionally leaves unified-exec background sessions alive. A separate reviewed
continuation established clean EOF retirement, a fresh worker resuming the exact
thread and reading README, then clean retirement again. Both retirements completed
within one second without signals or emergency cleanup. Five targeted existing
Rust filters passed 14 tests. Exact results and limitations are in
`source-build.json`; these checks do not qualify authenticated Runtime retirement
or the next signed App. Those remain native trial obligations.

Build05 source, patch and correspondence remain preserved in Git at
`798507c4712819f77fa868813d11adb799af9726` and in the referenced external evidence.
Older build03/build04 records remain under `history/`. Historical qualification
is not asserted to have been rerun. Broader fork/resume-history and durable-sleep
scenarios remain unqualified. This source-control update grants no publishing
approval.
