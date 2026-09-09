# Supplier staged source implementation proposal V2

Status: `DECISION_READY__ONE_THREE_STAGE_DEFAULT_OFF_CAMPAIGN__STAGE_0_DEPENDENCY_CUSTODY_REQUIRED__OFFLINE_CHECKS_CURRENTLY_BLOCKED__STAGE_A_AFTER_DISTINCT_DEPENDENCY_PASS__STAGE_B_AFTER_DISTINCT_STAGE_A_PASS__ACCOUNT_ENABLED_TRIAL_REMAINS_HELD__NOT_AUTHORIZED__NOT_ACQUIRED__NOT_IMPLEMENTED__NOT_BUILT__NOT_TESTED__NOT_QUALIFIED__NOT_ADOPTED__NOT_ACTIVE__NOT_PUBLISHED__NOT_RELEASED`.

This append-only successor preserves V1 manifest `b239db0edbf748a9f49667d732b91633c90f42df20d9b67274459623d8b5179a` and its independent FAIL review manifest `ae648058a6e58fd45e2d1fbfce3199d3ada15de58b391880fb0fff3eef915f42`. It changes only the standing-authority manifest path, retained recoverable dependency/source custody, and the exact Stage 0 network exception required by findings F001–F003. All other V1 semantics remain unchanged.

## Decision design

This packet offers one owner decision for one three-stage supplier campaign. Approval authorizes Stage 0 dependency custody, conditionally authorizes Stage A after a distinct dependency-review `PASS`, and conditionally authorizes Stage B after a distinct Stage A source/test-review `PASS`, all under the same grant. A failed or non-PASS gate leaves later stages unauthorized without disturbing accepted earlier evidence.

The campaign is bounded dependency custody, source implementation, and deterministic development verification toward an eventual account-enabled trial. Network is authorized only during Stage 0 for lock-declared Cargo registry/git dependency acquisition. It does not authorize an account-enabled trial or any live account, login, credential, keyring, provider, product-process, activation, adoption, publication, release, or production build operation.

## Frozen basis and calibration

The decision is derivative coordination evidence and cites these accepted or reviewed inputs:

- sealed author brief, SHA-256 `4946b73e8fec9c3ea8b518f683b69bc4bf8c22311ae5eca4c8d164bfef76606c`;
- accepted local wire/Runtime boundary, `../local-implementation-readiness-v4/IMPLEMENTATION_READINESS.md`, SHA-256 `416c9332628bc1631db5e53826be567c1a371570f09884c2fc18b80c19cc3a4d`;
- corrected supplier protocol proposal, `../supplier-implementation-proposal-v3/IMPLEMENTATION_PROPOSAL.md`, SHA-256 `0c206b1c1487f6c0848b55d981f5866cd9de73dca89d3c83c8ce5a46de7d42ba`;
- corrected V4 source-owner-map manifest, SHA-256 `c0d76407c93f3ae39507f4fda06f86b4dd99c7c589daa42790f60957d1bc7697`, whose closure reports no unresolved source owner and no further source read requirement;
- author-distinct V4 source-owner-map PASS review manifest, SHA-256 `7e7ef7a778cb6ca142aff4ce0798eaa9a1c860ae34b28fd9046c7538fa84fd5c`;
- accepted Runtime default-off source record manifest, SHA-256 `58e202bd9bfba6115b84aff4ac949ec481cf8a6599e94c222f4b82664314c7ee`;
- Runtime inbound strictness concordance manifest, SHA-256 `c47c29516890d5ebcd92fb6fed92c75a3b42a5e0b75bf7d9b15549bf6d7be919`, verdict `PASS_NO_MISMATCH`;
- standing initiative authority, SHA-256 `662c9d15e59de0dbf90c762f7bb9cea594ace42fa85148791ceab2b33a35ee40`;
- manager tooling preflight, `../supplier-staged-source-implementation-proposal-v1/TOOLING_PREFLIGHT.json`, SHA-256 `31b50f5a992913856954ec5d69a89ec6a32e96926e12a12da59e72f5c366d5eb`;
- manager tooling amendment, `../supplier-staged-source-implementation-proposal-v1/MANAGER_TOOLING_AMENDMENT.md`, SHA-256 `5cec95553e76bb546034c91d328328e313a614b2740eeeb4a61e141edea2b1bd`.

These records establish a proposal-ready locus and accepted cross-language boundary. The tooling preflight establishes Cargo/rustc 1.97.1 and `sandbox-exec` on host `aarch64-apple-darwin`, but current offline checks are blocked: the lock has 1,357 packages, including 1,212 registry packages; 1,041 required registry archives are missing; six git packages lack a Cargo git checkout root; and no supplier target exists. The recorded zero-exit sandbox probe proves only that a trivial profile launched, not that a real connection was denied. Dependency custody, sandbox confinement, supplier implementation, compilation, tests, interoperability, artifact identity, hosted behavior, and trial readiness remain unproven.

## Custody and isolated development root

The only supplier input custody is:

- root: `/private/tmp/chirality-supplier-identity-inquiry-20260907/source/codex`;
- commit: `758ef40f50c1a458425c7cfbf1eb12cbc07af0b0`;
- tree: `0f7a27df60e01dccf918f3203235266a0d6e3258`.

Before source content access or copying, the implementation manager records the absolute campaign write root and verifies with read-only metadata and `GIT_OPTIONAL_LOCKS=0` that the custody root is the named repository, is at the exact commit and tree, is clean for tracked files, and that every expected existing path is a tracked regular nonsymlink file. The write root must be a previously nonexistent, manager-selected directory under `/private/tmp/`, outside the custody root and every Chirality canonical, Runtime, and App root. The manager records the absolute root before creation. The campaign copies the verified local custody into that isolated root without checkout, reset, clean, mutation, or replacement of custody. All source reads, edits, Cargo metadata checks, compilation, and tests occur only in the isolated copy. Outside the exact Stage 0 fetch, network and fetch are prohibited; install, account, keyring, provider, and credential operations are always prohibited.

If the root/commit/tree, clean tracked state, path type, or copy identity does not match, the campaign stops before dependency acquisition or source mutation. The original custody root remains preserved throughout and is never a write target.

The manager records empty task `CARGO_HOME`, exact disposable `CARGO_TARGET_DIR`, and exact task `TMPDIR` as separately created siblings of the isolated source root, outside all source roots. Stage 0 may populate only task dependency custody. Stage A/B use that reviewed custody, the exact toolchain, unchanged lock, and locked offline resolution. Development outputs are evidence-bearing but are not production supplier artifacts.

## Stage 0 — dependency custody prerequisite

Stage A is not currently executable. In the isolated copy, hash and verify tracked regular nonsymlink `codex-rs/Cargo.toml` as the workspace manifest and `codex-rs/Cargo.lock` as its unchanged lock. With the exact empty task roots, run only:

```text
cargo fetch --locked --manifest-path codex-rs/Cargo.toml --target aarch64-apple-darwin
```

Stage 0 network authority is limited to lock-declared `registry+https://github.com/rust-lang/crates.io-index` dependencies and these five git sources/revisions covering six packages:

- `https://github.com/dzbarsky/rules_rust` at `b56cbaa8465e74127f1ea216f813cd377295ad81`;
- `https://github.com/helix-editor/nucleo` at `4253de9faabb4e5c6d81d946a5e35a90f87347ee`;
- `https://github.com/openai-oss-forks/crossterm` at `45fecb9508105988f42fe6ff0441783ed3717f92`;
- `https://github.com/openai-oss-forks/tokio-tungstenite` at `0e5b2d73aa18dd9f0a50ee9ff199d5aef7594186`;
- `https://github.com/openai-oss-forks/tungstenite-rs` at `4fffad30fe373adbdcffab9545e9e9bf4f2fc19f`.

Credentials, proxy credentials, account/private-store access, SSH identities, cloud/browser state, installers, global Cargo writes, source edits, compilation, tests, builds, product processes, activation, and release are excluded. `cargo fetch` does not execute Rust `build.rs` or procedural macros. Inventory every acquired object; verify registry archives against lock checksums, git checkouts against exact locked revisions, source set against the allowlist, and lock bytes against the pre-hash.

The current `sandbox-exec` evidence does not prove hard hostname restriction. If the host can mechanically restrict acquisition egress, record and test that mechanism. Otherwise the enforceable boundary is the exact command, unchanged lock, procedural source allowlist, sanitized credential/proxy-free environment, acquisition trace where available, and post-acquisition verification. If the owner requires hard hostname enforcement, Stage 0 stops until an environment provides it.

Freeze the custody/source-copy identity, manifest/lock hashes, command/environment, tool versions, enforcement calibration, complete dependency and write inventories, checksum/revision results, and a manifest. A fresh author-distinct dependency reviewer must rehash the packet and dependency custody and return exact `PASS`. Any other verdict keeps Stage A blocked.

Every acquired immutable locked dependency payload, including the complete task Cargo registry and git custody, remains retained as recoverable bytes after Stage 0 review and through later fan-in. Hashes, inventories, registry indexes, and git revision labels document that custody but do not substitute for its bytes. This retained custody may be released only after a successor verifies byte recovery from another retained custody location or an owner explicitly authorizes disposal.

## Stage A — strict default-off Cargo core

Stage A begins only after the manager records the Stage 0 author/review manifest hashes, verifies the dependency-review `PASS`, and confirms unchanged isolated source and lockfile hashes.

### Exact Stage A write set

Stage A may edit these seven existing files:

1. `codex-rs/app-server-transport/src/transport/mod.rs`
2. `codex-rs/app-server-transport/src/outgoing_message.rs`
3. `codex-rs/app-server/src/lib.rs`
4. `codex-rs/app-server/src/message_processor.rs`
5. `codex-rs/app-server/src/outgoing_message.rs`
6. `codex-rs/app-server/Cargo.toml`
7. `codex-rs/app-server/tests/suite/v2/mod.rs`

It may create exactly these three files:

8. `codex-rs/app-server/src/identity_admission.rs`
9. `codex-rs/app-server/src/identity_admission_protocol.rs`
10. `codex-rs/app-server/tests/suite/v2/identity_admission.rs`

Each existing member is hashed before its first edit. Each new member must be absent before creation. The source-selection record contains file type, symlink status, tracked status, byte count, and SHA-256 for existing members and records absence for new members.

### Bootstrap, protocol, and state-machine requirements

Stage A implements a helper that consumes bootstrap fd 3 exactly once as exactly 32 raw `authoritySecret` bytes followed by EOF. It rejects missing fd 3, short or long input, trailing bytes, a second consumption attempt, and read errors; closes fd 3; never treats its bytes as UTF-8 or JSON; never puts the secret in argv, environment, filesystem, serialization, status, logs, errors, crash output, workers, generated clients, or public APIs; and clears temporary secret-bearing buffers to the extent the local Rust implementation supports. Runtime process identity, supplier generation, challenges, supply digest, descriptors, and proof remain in the accepted initialize exchange rather than fd 3.

The protocol module implements the accepted strict contract without a translation layer:

- all private objects reject duplicate, unknown, or missing keys, wrong JSON types, invalid numeric fields, non-finite numbers, invalid UTF-8, and invalid protocol strings before MAC verification;
- protocol strings are printable ASCII bytes `0x21..0x7e`; UUIDs are canonical lowercase hyphenated ASCII; digests are 64 lowercase hexadecimal characters; challenges and MACs are unpadded base64url; IDs and generations are nonempty printable ASCII of at most 128 bytes; input is never Unicode-normalized;
- `Sequence20` is an original JSON string matching `^[0-9]{20}$` and representing `1..=18446744073709551615`; it is validated before exact unsigned parsing and never passes through floating point;
- `LP(x) = U32BE(byteLength(x)) || x`, `ASCII_FIELD(x) = LP(ASCII(x))`, and `SEQUENCE_FIELD(s) = U32BE(8) || U64BE(parseValidatedSequence20(s))`;
- `CANON(domain, fields)` is the exact accepted `ASCII("chirality-local-admission-mac") || 0x00 || U8(1) || LP(ASCII(domain)) || U32BE(fields.length) || concat(frame(field))` construction, with no JSON, whitespace, field names, locale sorting, newline, implicit number, or normalization inside it;
- initialization and transcript HMAC-SHA-256 inputs, exact field order, nested `v4` flattening, ASCII `null`, independent direction chains, 43-`A` initial previous MAC, exact next-sequence enforcement, constant-time MAC comparison, and maximum-sequence closure match the accepted local contract byte for byte;
- the strict request/result/error/notification unions and closed error class/reason pairs match the accepted proposal exactly, including `chirality/admissionAcquire`, `chirality/admissionRelease`, `chirality/admissionAbort`, the paired acquired/released/aborted notifications, and unsolicited `chirality/admissionRevoked`;
- a successful transition atomically changes private state, emits the result, then emits its byte-consistent matching notification as the immediately following supplier-to-runtime frame without interleaving; an error has no matching notification.

The coordinator owns one authenticated Runtime authority and at most one admission for one supplier process generation. State is process-local and nondurable. Supplier restart creates a new generation and retains no authority, admission, replay, or recovery state. It implements acquire, release, abort, revocation, closed-error, chain-failure, overflow, and secret teardown semantics. It does not add generalized capacity, fairness, reconnection, resume, or remote recovery.

### Raw ingress and origin fence

In `app-server-transport/src/transport/mod.rs`, Stage A classifies the original UTF-8 payload before the existing lossy `serde_json::from_str::<JSONRPCMessage>` path. The probe is a streaming, duplicate-aware top-level method probe. It must inspect decoded JSON structure and keys, not substrings and not a preliminary `serde_json::Value`. It recognizes the closed inbound private methods exactly and reserves the `chirality/*` namespace for strict rejection of unknown private candidates.

If a top-level object contains duplicate `method` keys and any occurrence names or claims the private namespace, if private and nonprivate method values are ambiguous in either order, or if a private candidate is malformed, it fails closed. An exact private request retains the original raw payload unchanged for recursive duplicate detection and strict schema validation at every object depth before MAC verification. Nested duplicate keys therefore cannot be erased by an intermediate parse. An unambiguously nonprivate payload continues into the existing public parser and behavior unchanged. Similar-looking strings in keys, values, or nested fields do not classify as a private method.

The new internal raw-private transport event carries exactly `connection_id` plus the original raw payload. It does not carry `ConnectionOrigin`. In `app-server/src/lib.rs`, the receiver resolves the current connection state by `connection_id`, reads the existing origin there, denies missing or closed connection state, denies `RemoteControl`, denies typed in-process entry, and admits only the authenticated local authority origin to the private coordinator. This creates no remote private authority and requires no transport caller edit.

### Internal delivery and hard default-off posture

`MessageProcessor::new` owns the one process-local admission state. Only origin-fenced strict raw private input reaches it. Ordinary typed requests retain their existing deserialization and handling. The transport outgoing union gains `PrivateNotification(JSONRPCNotification)`, and app-server outgoing code gains a requester-specific private-notification wrapper using the existing to-connection envelope. Results, errors, and matching private notifications are delivered only to the requesting connection. No public `ServerNotification`, generated protocol/client surface, broadcast, or RemoteControl delivery is added.

Production behavior remains hard default-off. The implementation may contain test-only enablement or hard-disabled internal hooks, but it must advertise no positive capability, report hosted readiness false, return admission unavailable, produce no positive production V4 snapshot, and grant no production acquire. No public fallback behavior changes.

### Cargo dependency and Stage A tests

In `codex-rs/app-server/Cargo.toml`, move exactly `hmac = { workspace = true }` from development dependencies to runtime dependencies immediately before `sha2 = { workspace = true }`. Leave no duplicate. Do not add `proptest`.

Deterministic tests cover at least:

- exact initialization and both transcript-direction vectors, binding the original JSON, canonical byte hex including eight-byte sequence fields, secret bytes, and MACs shared unchanged with Runtime;
- fd 3 exact-length, EOF, reuse, read-failure, and non-leakage cases;
- ASCII, UUID, digest, base64url, length, strict object, union, field-order, nested-duplicate, class/reason, and normalization rejection;
- `Sequence20` lower/upper bounds, number-vs-string, zero, wrong width, sign, whitespace, exponent, fraction, non-ASCII digit, maximum-plus-one, replay, gap, wrong direction, prior-MAC mismatch, overflow, and independent chain behavior;
- acquire/result/notification adjacency and equality, release, abort, revoke, unknown lease, illegal state, and one-authority/one-admission behavior;
- raw private preservation, duplicate identical private method rejection, private/nonprivate ambiguity in both orders, nested duplicate preservation and pre-MAC rejection, malformed or unknown private candidate rejection, absence of substring classification, and unchanged nonprivate fallback;
- origin resolution and denial for RemoteControl, typed in-process, missing, and closed connections; authenticated local routing only when explicitly enabled in a test;
- requester-only result, error, and `PrivateNotification(JSONRPCNotification)` delivery; default-off denial; no remote acquire, advertisement, production snapshot, production acquire, or transition hook.

Every test is deterministic and contains no timing, live account, credential, keyring, provider, network, or product-process dependency.

### Stage A checks and freeze

Before dependency code executes, qualify the sandbox with an actual denied network connection probe and denied reads of representative ambient credential, keychain, browser, SSH, cloud-configuration, and unrelated home paths. A profile-launch exit is insufficient. Freeze the profile and probes. Allow reads only from isolated source, reviewed dependency custody, exact toolchain, and necessary macOS SDK/system runtime paths; allow writes only to isolated source, target, task tmp, and explicitly identified task Cargo state; deny network; and use a sanitized allowlisted environment with credentials and proxies absent.

Before execution, record the exact working directory, command argv, environment, sandbox hash/probes, Rust/Cargo versions, offline/locked resolution, lock hash, source pre-hashes, and task roots. At minimum, run inside that qualified sandbox with `CARGO_NET_OFFLINE=true` and the exact task `CARGO_HOME`, `CARGO_TARGET_DIR`, and `TMPDIR`:

```text
cargo check --manifest-path codex-rs/app-server/Cargo.toml --locked --offline
cargo test --manifest-path codex-rs/app-server/Cargo.toml identity_admission --locked --offline
```

`cargo --offline` alone is not a process or network sandbox. Rust `build.rs` programs and procedural macros may execute during check/test and must remain confined by the qualified sandbox. Any inline transport or origin test needed by the contract must have an `identity_admission`-selectable name or be named separately in the pre-execution command record and run before freeze.

The immutable Stage A author packet records Stage 0 author/review hashes, exact pre/post members and hashes, all ancillary selections, complete commands/environment/sandbox, dependency resolution, compiler output and exit status, discovered and executed test names with results, target-output inventory and hashes sufficient to identify development outputs, complete source selection, contract/vector provenance, negative-mode results, deviations, and a manifest. It must explicitly say `DEFAULT_OFF`, `HOSTED_READINESS_FALSE`, `ADMISSION_UNAVAILABLE`, and `NOT_A_PRODUCTION_BUILD`.

A fresh author-distinct reviewer rehashes the Stage A packet and isolated source snapshot, verifies every Stage A requirement, exact path containment, Cargo edit, protocol vectors against the accepted Runtime evidence, raw ingress and origin rules, negative modes, dependency containment, command provenance, target containment, and test results. Only a frozen `PASS` review against the exact Stage A manifest unlocks Stage B. `PASS_WITH_FINDINGS`, conditional pass, mismatch, missing evidence, source drift, or any other verdict does not unlock it.

The exact reviewed Stage A source snapshot remains retained as recoverable bytes. A hash, inventory, patch, or Git identity alone is not recovery custody. Release requires either a successor that verifies byte recovery from another retained custody location or explicit owner disposal.

## Stage B — mapped identity, generation, and transition integration

### Stage B gate and exact write set

Under the same owner grant, the same implementation author may begin Stage B only after the manager verifies the exact author-distinct Stage A `PASS`, confirms the isolated source equals the reviewed Stage A post-source snapshot, and records both manifest hashes in the Stage B pre-state.

Stage B may edit exactly these seven expected files:

1. `codex-rs/login/src/auth/manager.rs`
2. `codex-rs/app-server/src/request_processors/account_processor.rs`
3. `codex-rs/app-server/src/request_processors/bedrock_auth.rs`
4. `codex-rs/app-server/src/request_processors/config_processor.rs`
5. `codex-rs/app-server/tests/suite/v2/account.rs`
6. `codex-rs/login/src/auth/auth_tests.rs`
7. `codex-rs/login/src/auth/storage_tests.rs`

Each is a tracked regular nonsymlink file and is hashed at the Stage B boundary before edit. The ten reviewed Stage A files remain within campaign scope for bounded repair and integration where required by the same contract, but Stage B must record any further edit to them and the compiler or required-test reason. It may not weaken a reviewed Stage A invariant.

### Atomic identity snapshot and generation contract

Stage B implements one default-off internal transition gate and atomic publisher for one coherent snapshot containing:

- the effective auth principal;
- the selected workspace, including forced workspace state guarded by its present separate lock;
- provider availability for the selected/forced state;
- either a complete qualified pair or a typed unavailable state;
- one opaque process-local `identityGeneration`;
- one digest of the complete joined snapshot.

`TokenData` alone is not the authoritative snapshot because it does not own forced workspace. Existing auth revision/change notification may trigger recomputation but is not the identity-generation contract. No reader may observe a new auth principal joined to an old workspace/provider view, or the reverse. A successful identity-affecting transition enters the gate before mutation and publishes the complete new snapshot and generation before its response, completion notification, or other success signal is released. A failed or cancelled operation that makes no identity change preserves the generation. The opaque generation and digest are process-local, nonsecret protocol values; their construction must be deterministic for the authoritative state while remaining independent of a public auth revision.

The exact supported transition slice is:

- app-server account API-key, browser, device, external-token, and Bedrock login initiation; asynchronous completion; reload; external-token handling; refresh; logout/revoke; active-login replacement and cancellation; and the corresponding existing completion/update notifications;
- Bedrock provider selection to `amazon-bedrock` and conditional clear, including conflict retry;
- generic configuration value writes, batch writes, and optional user-config reload for identity-relevant keys;
- `AuthManager` reload, cached-auth replacement or removal, external-auth install/clear/refresh, forced-workspace mutation, token refresh, and logout/revoke.

The gate must cover the successful state changes and response/notification release points for this entire slice. Cancellation and failure tests prove whether generation stays stable or advances according to actual committed identity change. The implementation may not infer coverage for any path not in this list.

Per-thread or otherwise unowned provider, model, or workspace overrides remain typed unavailable and default-off. Unsupported auth modes remain typed unavailable/default-off until their canonical principal, provider, workspace, and transition ownership is separately evidenced. API-key, header-only, Bedrock, external-provider, agent-identity, PAT, and other modes may not be treated as qualified merely because they can be represented. Provider identifiers and their nonsecret/stability semantics remain qualification-pending.

Production capability advertisement and acquire remain hard-disabled after Stage B. Stage B supplies an internal coherent generation source and transition fence for later qualification; it does not make hosted readiness true.

### Stage B deterministic verification and freeze

Stage B tests use only fake `TokenData` or fake auth state and mock storage/keyring interfaces already available inside the permitted test boundary. They perform no live login, account, keyring, storage backend, provider, credential, network, or product operation. Tests cover each supported transition, joined-snapshot atomicity, forced-workspace concurrency under the single gate, provider selection/clear and conflict retry, generic single/batch config writes and reload, replacement/removal/refresh/logout, cancellation with and without committed identity change, monotonic opaque generation publication, digest changes only with joined identity state, unavailable modes, and response/notification ordering.

Before running Stage B verification, the author records the exact manifest and exact test filter for each focused account, auth, and storage command. Selection occurs after test names exist and before execution. The set includes app-server account tests and login auth/storage tests and proves every transition row. Commands use the same reviewed dependency custody, qualified deny-network sandbox, sanitized environment, offline/locked toolchain, and task roots. Rerun the Stage A minimum check and `identity_admission` test after Stage B. A selected login-crate manifest is evidence input only unless separately admitted as a compiler-proven ancillary edit.

The immutable Stage B packet records the Stage A author/review manifest hashes, exact Stage B pre/post path hashes, ancillary selections and reasons, command/environment and dependency resolution, compiler output, exact discovered/executed test names and results, complete transition-coverage matrix, negative/unavailable modes, target-output inventory, final source selection, and a manifest. It repeats the default-off and non-production calibration.

The exact reviewed Stage B/final source snapshot remains retained as recoverable bytes under the same rule: another retained custody must be byte-recovery verified by a successor, or an owner must explicitly dispose it. Manifests and hashes do not substitute for source bytes.

## Bounded ancillary-file rule

The manager may admit an existing ancillary file only when an actual compiler diagnostic or a required deterministic test proves that file is directly necessary to implement or verify the accepted semantics. The file must:

1. be inside the same relevant feature module or its tests under `codex-rs/app-server`, `codex-rs/app-server-transport`, or `codex-rs/login`;
2. be a tracked regular nonsymlink source, test, or crate-manifest file;
3. be selected by exact path, file type, tracked status, byte count, and SHA-256 before edit;
4. have the exact compiler diagnostic or named failing required test, causal explanation, intended edit, and stage recorded before mutation;
5. remain within the same default-off protocol, identity-generation, transition, and deterministic-test objective; and
6. be included in the stage post-hash, review scope, transition/path matrix, and final source manifest.

This rule is not a directory grant and cannot be used for convenience, refactoring, warnings, formatting spillover, speculative compatibility, broader tests, or new features. A failing check may justify a repair and rerun inside the semantic and path envelope. The manager controls normal author repairs and reruns; there is no arbitrary fixed retry cap. The same failure repeated without material progress, a security ambiguity, inability to explain the causal edit, or a need to cross an excluded boundary stops and escalates the affected stage.

Excluded from both the expected and ancillary write envelopes are:

- all `codex-rs/app-server-protocol/**` files and all public/generated schemas, clients, registries, fixtures, and protocol surfaces;
- `codex-rs/Cargo.lock` and every workspace lockfile;
- keyring-store and backend-client source, including `codex-rs/keyring-store/**` and `codex-rs/backend-client/**`;
- binaries, compiled artifacts as source, vendor trees, dependency source edits, and package outputs; reviewed Stage 0 custody is read-only Stage A/B input;
- Bazel files and Bazel parity work;
- unrelated thread, turn, tool, model, effect, worker, CLI, renderer, and session code;
- all canonical Chirality source, accepted Runtime source, Runtime build roots, App roots, and the original supplier custody root.

If an excluded path, new dependency, lockfile update, generated surface, public method, account/keyring/provider operation, unauthorized network activity in any stage, any Stage A/B network activity, native build, or semantic contract change becomes necessary, the affected stage stops. The one exact locked target-specific Stage 0 `cargo fetch` is the sole network exception. Accepted prior-stage evidence stays frozen and is not rolled back or rewritten.

## Final independent review and closure state

After Stage B freeze, a fresh author-distinct final reviewer validates the complete isolated source rather than only the Stage B delta. The reviewer rehashes every expected and admitted ancillary file and checks:

- byte-exact bootstrap, CANON/HMAC/`Sequence20`, strict union and duplicate-key behavior against the accepted contract and Runtime vectors;
- raw-ingress-before-lossy-parse, original-byte preservation, connection-origin resolution, RemoteControl and typed-in-process denial, unchanged public fallback, and requester-only delivery;
- one-authority/one-admission state, result/notification adjacency, error and revocation semantics, secret non-leakage, and default-off hosted behavior;
- the complete joined auth/workspace/provider snapshot, opaque generation/digest, supported transition matrix, response/notification ordering, cancellation behavior, and typed-unavailable negative modes;
- exact expected paths, every ancillary admission and reason, excluded-boundary nonuse, no source drift, dependency and lock containment, offline command provenance, compiler/test results, target inventory, and absence of live account/network/keyring/provider actions.

Only `PASS` can be presented for manager fan-in. A pass accepts a reviewed default-off source candidate and deterministic development evidence. It does not accept a production supplier build, qualify a supplier/Runtime source-build pair, authorize capability advertisement or production acquire, or open the account-enabled trial.

The manager fan-in records accepted upstream hashes, Stage 0/A/B manifests, dependency/Stage A/final review manifests, exact dependency and source selections, ancillary set, closure verdict, derivative-package state, rerun requirements, and blockers. Cleanup after fan-in may remove only disposable derivative build, target, temporary, and explicitly non-custodial scratch outputs. It must retain the immutable locked dependency payloads, task Cargo registry/git custody, and reviewed Stage 0/A/B source snapshots as recoverable bytes until a successor verifies byte recovery from another retained custody or an owner explicitly disposes them. Hashes and inventories are not substitutes. Cleanup is separately recorded. Frozen packets are never rewritten.

## Stop and repair policy

Within an active stage, ordinary compiler or deterministic-test failures are development evidence. The author records the attempt, failure, changed files, repair, and rerun, and the manager controls continuation. Immediate stop conditions are custody mismatch, path or symlink violation, source mutation outside the isolated root, unauthorized network activity in any stage, any Stage A/B network activity, install/account/keyring/provider operation, secret exposure, unsafe public fallback, change to the accepted wire contract, generated/public protocol change, lockfile mutation, native/production build, or any activation/release action. The one exact locked target-specific Stage 0 `cargo fetch` is the sole network exception.

The manager stops and escalates when a failure repeats without material progress, consequential security or ownership ambiguity prevents a bounded repair, or repair requires an excluded path, dependency, tool, nondeterministic test, or expanded transition slice. A Stage B stop leaves a reviewed Stage A snapshot intact. Neither stage may silently weaken a negative test or change a test filter to conceal a failure.

## Held gates toward an account-enabled trial

The following remain disabled and require later evidence and their owning decisions:

- positive capability or V4 advertisement;
- initialize advertisement/proof integration that exposes hosted readiness;
- production `chirality/admissionAcquire` availability;
- public or generated protocol surfaces and clients;
- Bazel parity and dual Cargo/Bazel/generated parity;
- a clean production supplier build and artifact identity;
- a Runtime native build and artifact identity;
- supplier/Runtime source-build pair qualification and interoperability;
- provider-ID stability and nonsecret qualification;
- live account, credential, keyring, provider, cancellation, and recovery qualification;
- the account-enabled trial;
- App or CLI adoption, activation, publication, and release.

Until those gates close, hard-disabled hooks report hosted readiness false and admission unavailable. Development compilation and tests create no accepted production supplier build. Future build artifacts receive hashes after they exist; this campaign does not require or invent future artifact hashes before compilation.

## Custom-fork maintenance burden

This is a maintained custom fork across transport, app-server dispatch, authentication, workspace/provider selection, and configuration mutation code. Each upstream rebase must re-evaluate the pre-lossy raw-ingress location, connection-origin ownership, outgoing requester-only route, `MessageProcessor` ownership, all mapped identity transitions, forced-workspace locking, provider selection, configuration write paths, Cargo dependencies, and every admitted ancillary file. Upstream movement or a new mutation path is a coverage change, not a mechanical conflict resolution.

The strict protocol vector corpus must remain shared byte-for-byte with Runtime. Before any release decision, Cargo, Bazel, public/generated surfaces, and retained clients must have explicit dual-build and generation parity; the present campaign holds those surfaces rather than claiming parity. Recovery and security review must cover secret bootstrap/zeroization, duplicate-key and raw-byte handling, replay/sequence/MAC failure, transition fencing, cancellation, revocation, crash/restart, and negative-mode behavior. Every proposed supplier build must be qualified with the exact accepted Runtime build as a source/build pair. Rebases, dependency changes, Runtime changes, provider-ID changes, or auth/config ownership changes require repeated qualification rather than inheritance from this source review.

## Proposed owner disposition

Approve or decline the single token `GRANT_SUPPLIER_STAGED_DEFAULT_OFF_SOURCE_IMPLEMENTATION_V1` in `NEXT_DECISION_SUBJECT.md`. Approval activates bounded Stage 0 dependency custody, conditionally activates Stage A after a distinct dependency `PASS`, and conditionally activates Stage B after an author-distinct Stage A `PASS`. It grants no other dependency, source, or operational action.
