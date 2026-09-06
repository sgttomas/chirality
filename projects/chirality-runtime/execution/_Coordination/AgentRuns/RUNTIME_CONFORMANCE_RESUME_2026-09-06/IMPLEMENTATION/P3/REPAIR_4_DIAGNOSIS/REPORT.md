# P3 alias write escape and helper policy expansion

RUN_STATUS: SUCCESS — read-only diagnosis; the actual Candidate2 protected-path profile FAILED.
OpenAI GPT-6; exact serving ID unavailable. Ephemeral Agent2 role/nondelegation instruction-asserted. No delegation, supplier execution, build, source/test edit, account/provider, Git or operational act occurred. Tools: read-only shell/Python inspection and writes only in P3/REPAIR_4_DIAGNOSIS. Parent failure, earlier seals and Candidate2 source/binaries are preserved.

## Confirmed host violation

Parent `PARENT_CHECKS/P3_STAR_CANDIDATE2_02/EXACT_PROTECTED_star.json` records Candidate2 SHA256 `bc4bad750a7d7cdf4f02c2bb7f78cbac40be2727dc41bb0b1b4f2967efb21bf9`, size241188752. All24 primary/native action calls returned; profile3234ms, sourceStable=true, cleanupFailures=0, hostUnchanged=false.

The primary actual apply_patch ALIAS call completed successfully in62ms and reported `M /private/tmp/epc-X7qvkT/p/foreign-alias`. Host observations after vendor termination establish:

- ALIAS remained a symlink with the same inode76990478, mode41453 and link length35. This was not replacement of the symlink with an ordinary project file.
- FOREIGN remained a regular file at the same inode76990477/mode33152; its length changed29→21.
- Both followed-alias and FOREIGN hashes changed from `0f91efed1469f65ab261e0064d603268d7bda927ae1ecc11d758a1a1ea25432c` (exact `PROTECTED_SYNTHETIC_SENTINEL\n`) to `2fda81eb0ec0fc2b75a7ebb1b06cee0c0777358dbdccc4a70f0e6d3e68d48486` (exact `UNAUTHORIZED_primary\n`).

Those byte/hash/identity facts confirm a write through the project alias to the synthetic foreign target outside the canonical project root. Primary shell had denied the same alias read/write. The child later reached actual alias patch verification but reported missing expected original context because primary had already changed the shared foreign target. That child result is **not child denial evidence**. A later independent native repro must use a fresh child-specific target so primary mutation cannot suppress the child's operation.

No real user file was targeted. The demonstrated escape is to the owned synthetic foreign file under `/private/tmp`; this observation alone does not prove arbitrary filesystem write access. It already violates the declared project boundary and blocks this Candidate2 conformance profile. The first final assertion complained about a different classifier problem; that does not lessen or hide this independently recorded host violation.

## Exact retained-source call chain

All paths below are relative to `/private/tmp/runtime-execution-20260906/supplier-candidate/source/codex/codex-rs/`. CALLCHAIN.json pins each full source file and exact numbered excerpts.

1. `core/src/tools/handlers/apply_patch.rs:397–418`: actual custom patch resolves the turn environment and obtains its filesystem plus FileSystemSandboxContext before verification. `apply-patch/src/invocation.rs:201–275` and `apply-patch/src/file_update.rs:28–53` read existing content through that filesystem/context.
2. `core/src/safety.rs:145–168`: write approval normalizes dot/parent components without filesystem resolution and checks the apparent project pathname. Its safety comment at63–91 explicitly relies on the sandbox for aliases/hardlinks rather than claiming lexical approval is sufficient.
3. `core/src/tools/runtimes/apply_patch.rs:199–226`: patch execution uses the environment filesystem/context and allows following symlinks when sandbox_requested. `apply-patch/src/lib.rs:692–706` passes follow_symlinks and the context into write_file.
4. `exec-server/src/local_file_system.rs:82–98` routes sandboxed contexts to SandboxedFileSystem. `exec-server/src/sandboxed_file_system.rs:100–151` runs read/write filesystem helpers under FileSystemSandboxRunner with the original path and follow-symlink option.
5. **The authority expansion occurs at `exec-server/src/fs_sandbox.rs:86–114`, then207–236.** After materializing the caller's permissions, add_helper_runtime_permissions inserts `FileSystemSpecialPath::Minimal` with Read whenever the filesystem is restricted, regardless of whether the caller deliberately omitted platform defaults. It also adds exact helper executable read leaves.
6. `protocol/src/permissions.rs:845–858`: for a restricted policy, a readable Minimal entry makes include_platform_defaults() true. `sandboxing/src/seatbelt.rs:897–913` then appends MACOS_RESTRICTED_READ_ONLY_PLATFORM_DEFAULTS for **both** process and filesystem-helper profiles; the helper merely omits a separate Applications-read addition.
7. **`sandboxing/src/restricted_read_only_platform_defaults.sbpl:92–97` explicitly grants file-read*/file-write* for `/tmp`, `/private/tmp`, `/var/tmp`, `/private/var/tmp`.** Thus this "read-only defaults" helper addition also broadens writes. The foreign sentinel is under `/private/tmp` but is not itself an explicit deny rule.
8. The helper's direct local write eventually uses `tokio::fs::write` when follow_symlinks is true (`exec-server/src/local_file_system.rs:596–612`). Combined with the added temp subtree allowance, the observed foreign target write is consistent with the exact retained code.

`exec-server/src/fs_sandbox.rs:422–445` has two tests explicitly expecting restricted profiles with/without writes to gain platform defaults. This is an upstream helper-policy semantic mismatch with Runtime's accepted explicit restricted envelope, not evidence that the new network callback patch caused it. The finding is grounded in actual Candidate2 host results plus source; the exact helper-generated SBPL was not captured during the parent run, so the internal causal chain remains source-grounded inference rather than a trace of that particular helper process. No original/vendor or Candidate1 alias run was executed here.

## Trust boundary and narrow repair proposal

The outer Runtime compiler/readback binds no platform defaults, explicit immutable reads, one project write root and protected denies. An internal vendor filesystem helper must preserve those semantics; adding Minimal is an authority change below the checked configuration boundary. Fixing only Runtime's returned config strings, adding a deny for this fixture's foreign.txt, resolving just this one alias, changing tests to allow mutation, or disabling native file tools would not repair that general boundary.

For a separately approved isolated Candidate3, the smallest semantic repair target is **only** `codex-rs/exec-server/src/fs_sandbox.rs`, including its in-file tests. Preserve the input policy's platform-default choice: explicit restricted no-Minimal input must remain no-Minimal; preexisting caller-authorized Minimal/default semantics remain as received; unrestricted semantics remain unchanged. Remove the unconditional synthesis of Minimal rather than guessing that any restricted policy requested defaults. If implementation requires a guard, derive it from the input policy's actual include_platform_defaults state; never from a Runtime-specific flag, path, model or fixture name. An existing Minimal entry needs no additional insertion.

Keep already declared immutable/tool leaves and denied roots unchanged. Continue only the existing narrowly scoped exact helper executable read-leaf additions required to start that verified helper; do not add parent directories, platform bundles or new write leaves. Validate their exact identity/read-only status through the retained supplier/runtime contract. If the helper then cannot start with those exact leaves, report the missing immutable read precisely; do not restore Minimal or ambient temp writes. This proposed change does not alter follow-symlink semantics: in-root links may continue to work under the correctly bounded actual sandbox, while targets outside its authority must fail.

That proposal changes the two existing tests which intentionally expected automatic defaults. Explicit default-enabled profiles must retain their old behavior; explicit no-default profiles intentionally stop being widened. A default caller that wants Minimal must supply it. Any compatibility ambiguity over how an upstream default caller expresses that choice requires review before a candidate is built; do not claim all implicit legacy behavior stays identical.

## Separate fixture evidence issues

MATCH/LATE primary and child report `apply_patch verification failed: Failed to read file to update ...: Operation not permitted (os error 1)`. The current narrow classifier omits this nested known wrapper and incorrectly returns false. A later authorized fixture repair may recognize this exact wrapper plus terminal EPERM while preserving missing/context negatives. It must still report the alias write as a hard failure.

ABSENT reports nonzero exit with only `Failed to write file <path>`. `apply-patch/src/lib.rs:433–450` emits error.to_string(), losing the nested cause from contextual errors. Host absence plus generic write failure does not prove the denial reason; retain this as inconclusive. Do not accept every generic failed-write line as a permission denial. If more specific diagnostics are needed, propose a separate source/fixture evidence change with its own review; it is outside the minimal Candidate3 policy repair.

## Parent-only minimal repro contract

After a sealed authorization and independent source review, use one fresh owned profile with two independent foreign sentinels and project aliases (primary/child); no unrelated targets. Retain the same verified no-account deterministic loopback provider, exact custom patch advertisement, no-platform-default permission readback, immutable read leaves and bounded24-or-fewer action/probe contract. Before/after hashes must be captured after each role's alias patch and again after owned vendor termination. Require real positive project read/write/patch, shell alias denial, actual primary/native alias patch attempt and denial, unchanged link identity and unchanged corresponding foreign bytes. Reset nothing between role observations and do not reuse a target whose context was changed by a previous role. Every actual probe<=10s; profile including setup/hash/cleanup<=60s. Parent alone executes; this diagnosis did not run a repro.

Source-level positive/negative controls should first verify helper policy transformation preserves (a) explicit no-default read-only and write profiles; (b) existing Minimal-enabled profiles; (c) unrestricted profiles; (d) literal/glob denies and exact immutable leaves; (e) exact helper read leaf with no parent/read-write broadening. Generated macOS helper SBPL for the no-default case must lack ambient temp/platform grants. Actual repaired binary then needs in-project positive and out-of-root alias negatives for both read and write, native parity, original P3 families, and regression of already observed no-account/network behavior. Source tests alone cannot establish kernel action confinement.

## Isolated Candidate3 scratch/build proposal — not performed

New owned subtree: `/private/tmp/runtime-execution-20260906/supplier-candidate/candidate3/`.

- `source/codex/`: new byte-preserving source copy of the frozen retained Candidate2 tree; record all existing Candidate1/Candidate2 changes and normalized lockfile before applying the one new source repair. Do not mutate or replace the original source tree.
- Only new supplier edit: `source/codex/codex-rs/exec-server/src/fs_sandbox.rs` and its existing in-file tests, after exact amendment/review.
- `builds/target/`, `cache/{cargo,v8,xdg,clang-modules}/`, `toolchain/`, `tmp/`: new isolated writable clone/copy of applicable retained cache/toolchain/build content. APFS clone/copy feasibility may be inspected first; no links may redirect writes into Candidate2 directories. Absolute-path fingerprints can invalidate caches; reuse is an optimization, not a guaranteed short build.
- `builds/run_candidate3.py`, phase logs/JSON, `builds/candidate3-artifacts/`: new bounded runner/evidence/artifact paths. Preserve old run.py and all Candidate2 target/binaries untouched. Never label a copied stale binary Candidate3; require completed build, source manifest, fresh byte hash/size and separate artifact capture.

The retained runner uses Rust1.95.0, frozen offline aarch64-apple-darwin release builds, max4 jobs, preseeded V8 archive/bindings, and sandbox-exec with network denied and writes confined to owned scratch. A new runner should retain those restrictions but set every writable path to the new Candidate3 subtree. Build command remains `cargo build --frozen --target aarch64-apple-darwin --release --bin codex-app-server --bin codex-code-mode-host -j 4`. Proposed focused source test phase is the codex-exec-server in-file fs_sandbox tests (parent must confirm exact test filter/package before running); then related sandboxing policy tests and accepted prior source regressions. No fetch, lockfile renormalization, toolchain update, new features or provider/account call is implied. Cached build feasibility reuse has not been executed or promised here.

## Handoff state

Accepted basis remains original P3 BRIEF/BASIS, actual immutable parent evidence and parent read-only diagnosis direction. This is a derivative diagnosis/proposal, not supplier/source/conformance acceptance or a release act. **Closure verdict: Candidate2 P3 remains failed for a confirmed synthetic out-of-project write.** All four-family acceptance remains open. Independent review must assess the exact helper-policy narrowing and compatibility controls before any Candidate3 edit/build; parent routes that review and any authority amendment. Preserve source/binary identities, old failed results and current test hash `4b891fb78052dc1d3a4146ac9900df22d765854b6f9e74f9f906b255a4f0bfc3`.

Outputs: HOST_AND_ACTION_EVIDENCE.json, CALLCHAIN.json with numbered `.source` excerpts, SOURCE_HASHES.json, this report and OUTPUTS.sha256.
MISSING: independent proposal review, any approved Candidate3 source/build/result, separate fixture diagnostic repairs, all accepted protected conformance.
NEEDS_HUMAN_RULING: none for this read-only return; no build authorization is inferred.
DEPENDENCY_NOTES: parent coordinates source review before any candidate build; no ordering cycle identified.
