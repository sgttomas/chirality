# Owner decision — supplier staged default-off source implementation V2

Decision token: `GRANT_SUPPLIER_STAGED_DEFAULT_OFF_SOURCE_IMPLEMENTATION_V1`

Choose exactly one:

- `APPROVE GRANT_SUPPLIER_STAGED_DEFAULT_OFF_SOURCE_IMPLEMENTATION_V1`
- `DECLINE GRANT_SUPPLIER_STAGED_DEFAULT_OFF_SOURCE_IMPLEMENTATION_V1`

## Effect of approval

Approval is one grant for one three-stage campaign toward an eventual account-enabled trial. It authorizes Stage 0 dependency custody, conditionally authorizes Stage A after an author-distinct dependency-review `PASS`, and conditionally authorizes Stage B after an author-distinct Stage A source/test-review `PASS`. Any other verdict keeps later stages unauthorized. Approval does not authorize an account-enabled trial.

The controlling proposal is `IMPLEMENTATION_PROPOSAL.md` in this packet. Its frozen manifest hash must be verified before execution. In addition to the accepted contract/map/Runtime/authority hashes listed there, this decision binds tooling preflight SHA-256 `31b50f5a992913856954ec5d69a89ec6a32e96926e12a12da59e72f5c366d5eb` and manager tooling amendment SHA-256 `5cec95553e76bb546034c91d328328e313a614b2740eeeb4a61e141edea2b1bd`.

## Custody and execution root

Use only supplier custody `/private/tmp/chirality-supplier-identity-inquiry-20260907/source/codex` at commit `758ef40f50c1a458425c7cfbf1eb12cbc07af0b0`, tree `0f7a27df60e01dccf918f3203235266a0d6e3258`. Verify it read-only, copy it to a new manager-recorded isolated `/private/tmp/` source root, and preserve custody. Record empty task `CARGO_HOME`, external `CARGO_TARGET_DIR`, and task `TMPDIR`.

## Stage 0 dependency custody

Offline checks are currently blocked: 1,041 of 1,212 locked registry archives are missing, six git packages lack a Cargo git checkout, and no supplier target exists. Verify and hash `codex-rs/Cargo.toml` as workspace manifest and unchanged `codex-rs/Cargo.lock`, then run only:

```text
cargo fetch --locked --manifest-path codex-rs/Cargo.toml --target aarch64-apple-darwin
```

Acquire only lock-declared crates.io packages and the five exact git revisions named in `IMPLEMENTATION_PROPOSAL.md`. Use no credentials/proxies/installers and perform no build/test/source edit. `cargo fetch` does not execute `build.rs` or proc macros. Inventory all objects, verify lock checksums/revisions and unchanged lock bytes, freeze, and obtain a distinct dependency-review `PASS`.

Current `sandbox-exec` evidence does not prove hard hostname restriction. Use mechanical restriction if available; otherwise record the procedural source allowlist and post-acquisition verification. If hard hostname enforcement is owner-required, Stage 0 waits for that environment. The acquired task Cargo registry/git payload remains retained as immutable recoverable bytes until a successor verifies byte recovery from other retained custody or an owner explicitly disposes it; hashes and inventories are not substitutes.

## Stage A conditional executable envelope

Stage A remains blocked until the exact Stage 0 dependency `PASS`. Before dependency code executes, qualify the sandbox with an actual denied network connection and denied reads of representative credential, keychain, browser, SSH, cloud, and unrelated home paths. Run check/test with sanitized allowlisted environment, reviewed dependencies, locked offline Cargo, and reads/writes confined as specified in the proposal. Offline mode alone is insufficient because `build.rs` and proc macros execute during check/test.

Edit only these expected existing files:

1. `codex-rs/app-server-transport/src/transport/mod.rs`
2. `codex-rs/app-server-transport/src/outgoing_message.rs`
3. `codex-rs/app-server/src/lib.rs`
4. `codex-rs/app-server/src/message_processor.rs`
5. `codex-rs/app-server/src/outgoing_message.rs`
6. `codex-rs/app-server/Cargo.toml`
7. `codex-rs/app-server/tests/suite/v2/mod.rs`

Create only these expected new files:

8. `codex-rs/app-server/src/identity_admission.rs`
9. `codex-rs/app-server/src/identity_admission_protocol.rs`
10. `codex-rs/app-server/tests/suite/v2/identity_admission.rs`

Implement and deterministically test the accepted exactly-32-raw-byte one-read fd 3 bootstrap; strict printable-ASCII/UTF-8/duplicate/unknown/missing/type validation; exact `CANON`, HMAC-SHA-256, base64url, strict `Sequence20`, directional transcript chains, overflow closure, strict request/result/error/notification unions, and closed error pairs; one Runtime authority and one admission in process-local supplier-generation state; acquire/result+adjacent-notification/release/abort/revoke and teardown behavior; original raw local ingress before the first lossy JSON parse; streaming duplicate-aware top-level method probing with no substring matching and no preliminary `Value`; rejection of duplicate or ambiguous top-level method involving a private name; preservation of original nested params for recursive duplicate/schema rejection before MAC; unchanged unambiguous public fallback; an internal event carrying exactly `connection_id + original raw payload`; connection-state and origin lookup in app-server; RemoteControl, typed-in-process, missing, and closed connection denial; requester-only result/error delivery and `PrivateNotification(JSONRPCNotification)` via the existing to-connection envelope.

Move `hmac = { workspace = true }` from development to runtime dependencies immediately before `sha2`, with no duplicate. Omit `proptest`. Keep production hard default-off, capability advertisement absent, hosted readiness false, admission unavailable, public/generated surfaces unchanged, and production acquire disabled.

At minimum run in the isolated copy with the recorded offline/locked environment and external target:

```text
cargo check --manifest-path codex-rs/app-server/Cargo.toml --locked --offline
cargo test --manifest-path codex-rs/app-server/Cargo.toml identity_admission --locked --offline
```

Name or pre-record any additional required inline transport/origin test filter. Freeze exact source pre/post hashes, all commands/environment, lock and dependency resolution, compiler outputs, test identities/results, protocol-vector provenance, negative-mode results, target inventory, ancillary records, and a Stage A manifest. A distinct reviewer must rehash and PASS the exact packet and source snapshot before Stage B. Retain that reviewed source snapshot as recoverable bytes until successor-verified byte recovery from other custody or explicit owner disposal.

## Stage B conditional envelope

After that exact PASS, the same grant permits the same implementation author to edit:

1. `codex-rs/login/src/auth/manager.rs`
2. `codex-rs/app-server/src/request_processors/account_processor.rs`
3. `codex-rs/app-server/src/request_processors/bedrock_auth.rs`
4. `codex-rs/app-server/src/request_processors/config_processor.rs`
5. `codex-rs/app-server/tests/suite/v2/account.rs`
6. `codex-rs/login/src/auth/auth_tests.rs`
7. `codex-rs/login/src/auth/storage_tests.rs`

Implement a single default-off transition gate and atomic publisher for the coherent auth principal plus selected/forced workspace plus provider-availability snapshot, complete-pair-or-typed-unavailable state, opaque process-local identity generation, and digest. `TokenData` alone is insufficient because forced workspace has a separate lock. Current auth revision is only a trigger. Enter the gate before a successful identity-affecting mutation and publish the joined snapshot before response/notification release.

Cover exactly account login/initiation, completion, reload, external-token, refresh, logout/revoke, active-login replacement and cancellation; Bedrock provider selection and conditional clear with conflict retry; generic config single/batch writes and reload; and AuthManager reload, replacement/removal, external auth install/clear/refresh, forced-workspace mutation, token refresh, and logout/revoke. Failed/cancelled operations without committed identity change preserve generation. Per-thread or unowned provider/model/workspace overrides and unsupported auth modes remain typed unavailable/default-off.

Use only fake token/auth state and mock storage/keyring interfaces. Before running tests, record exact manifest/filter commands that cover account, auth, and storage transitions. Rerun the Stage A check and `identity_admission` test after Stage B. Freeze exact Stage A references, Stage B pre/post hashes, commands/environment, compiler output, exact test identities/results, transition matrix, negative modes, dependency/target inventory, ancillary records, final source selection, and manifest. Retain the reviewed Stage B/final source snapshot as recoverable bytes under the same successor-verification or owner-disposal rule.

## Ancillary rule

The manager may select an ancillary edit only after an actual compiler diagnostic or required deterministic test proves it directly necessary within the same feature module/tests under `codex-rs/app-server`, `codex-rs/app-server-transport`, or `codex-rs/login`. It must be an exact tracked regular nonsymlink source/test/crate-manifest path, hashed before edit, and recorded before mutation with the exact diagnostic/test, causal reason, intended edit, and stage. Review must cover it. This is not a directory, convenience, refactor, warning-cleanup, or feature-expansion grant.

Normal author repair and rerun within this semantic/path envelope remains manager-controlled with no arbitrary fixed retry cap. Stop on repeated same failure without material progress, security/ownership ambiguity, unexplained ancillary need, or need to leave the envelope.

## Exclusions and stop boundaries

Exclude all `app-server-protocol` and public/generated schema/client surfaces, every workspace lockfile, keyring-store/backend-client source, Bazel files, binaries, vendor/dependency sources, unrelated thread/tool/model/effect/worker/CLI/renderer/session code, all canonical/runtime/App roots, and supplier custody. A required edit to an excluded path, new dependency, lockfile update, contract change, nondeterministic test, unauthorized network activity in any stage, any Stage A/B network activity, install/account/keyring/provider operation, source mutation outside the isolated copy, native/production build, or activation/release action stops the affected stage. The one exact locked target-specific Stage 0 `cargo fetch` is the sole network exception. A Stage B stop preserves the reviewed Stage A evidence.

## Final review and held gates

A fresh author-distinct reviewer must review the complete final source, contract/Runtime vectors, transition matrix, negative modes, path/ancillary containment, dependency/lock/target containment, sandbox qualification, commands, compiler output, and tests. Only `PASS` proceeds to manager fan-in. Cleanup may remove only disposable derivative build/target/tmp and explicitly non-custodial scratch outputs. Immutable locked dependency/task Cargo registry/git payloads and reviewed Stage 0/A/B source snapshots remain retained as recoverable bytes until successor-verified recovery from other retained custody or explicit owner disposal; hashes and inventories are not substitutes.

Even after PASS, keep disabled: positive capability/V4 advertisement, initialize hosted enablement, production acquire, public/generated surfaces, Bazel parity, clean production supplier build, Runtime native build, supplier/Runtime source-build pair qualification, provider-ID stability/nonsecret qualification, live account-enabled trial, App/CLI adoption, activation, publication, and release. Hard-disabled hooks report hosted readiness false and admission unavailable. Development checks are not a production build, and future artifact hashes are assigned only after artifacts exist.

Custom-fork maintenance must rebase and reassess transport/auth/config loci, share strict vectors byte-for-byte with Runtime, establish Cargo/Bazel/generated parity before release, repeat security/recovery review, and requalify each supplier/Runtime build pair after relevant upstream, dependency, Runtime, provider-ID, or ownership change.

## Effect of decline

Decline leaves dependency custody and supplier source unchanged and all three stages unauthorized. Accepted Runtime/map evidence remains intact. Account-enabled trial, activation, publication, and release remain held.
