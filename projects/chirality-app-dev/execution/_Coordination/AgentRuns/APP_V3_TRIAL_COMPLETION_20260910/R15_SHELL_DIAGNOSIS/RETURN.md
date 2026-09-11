# R15 shell diagnosis return

Diagnosis complete. No product/source/build/sign changes made. This derivative diagnostic packet consumes the BRIEF source basis and the lead's native R15 observations; it is not native acceptance or authoritative decomposition truth.

## Supported cause

The pinned inner Seatbelt base starts `(deny default)` and lacks literal-root read-data allowance. Runtime compiles an explicit named filesystem policy with platform defaults disabled (`packages/daemon/src/codex-containment.ts:440`), granting R15 immutable roots `/Library/Apple`, `/System`, `/bin`, `/sbin`, `/usr`, but not literal `/`. The supplier appends its restricted platform defaults only when requested (`codex-rs/sandboxing/src/seatbelt.rs:897-909`). Those omitted defaults include `(allow file-read* file-test-existence (literal "/"))` plus numerous unrelated permissions.

Account-free system-command reproduction using the exact pinned base-policy text, the measured R15 immutable roots, and one scratch read/write root produced SIGABRT(-6), empty stdout and stderr, for both direct `/bin/cat README.md` and `/bin/zsh -c '/bin/cat README.md'`. This matches the native tool's134/empty-output signature; supplier PTY code maps Unix signals to128+signal (`codex-rs/utils/pty/src/process.rs:43-44`). No supplier, code-mode host, auth, live project, or provider participated.

Parent authorized a scratch-only allowance differential after the initial reproduction. Of individually tested system-mac-syscall Sandbox67, vnguard, file-map-executable system roots, secinitd mach lookup, random devices, descriptor devices, and literal-root reads, only literal-root reads fixed startup. Minimization:
- root metadata only: SIGABRT, empty output;
- root existence only: SIGABRT, empty output;
- root read-data only: cat and zsh exit0 with exact expected text;
- root read-data constrained to DIRECTORY: same positive result.

The minimal rule is:

```scheme
(allow file-read-data
  (require-all (literal "/") (vnode-type DIRECTORY)))
```

With that rule, synthetic protected-path reads and writes remain denied (exit1/EPERM); no attempted protected output file was created. The differential identifies an effective required startup permission on this macOS version; it does not name the particular libc/loader function that aborts.

## Outer envelope check

No corresponding Runtime outer-policy change is needed. `codex-containment.ts:117-120` chooses direct launch for v2 trusted-supplier; its return at177-178 is direct/null profile. `codex-authenticated-transport.ts:316-320` requires direct launch for the v2 worker, because that supplier applies the native Seatbelt per file/command. There is no second outer Seatbelt denying the proposed literal-root access. The legacy/login outer text already exempts literal `/` from its read-data deny (`codex-containment.ts:147`).

## Smallest proposed repair and impact

Add only the rule above to the pinned supplier's `codex-rs/sandboxing/src/seatbelt_base_policy.sbpl` (retained source root `/private/tmp/chirality-supplier-login-fix-20260911/source`). Do not add `/` to Runtime immutableReadRoots: that is a recursive subpath grant and would expose unrelated filesystem trees. Do not import `:minimal` wholesale, loosen protected paths, change shell/tool mode, alter credentials, or weaken signing.

This permits read-data on the root directory vnode, which can include enumerating its immediate directory entries; it does not grant descendant file reads, recursive traversal/data, writes, network, or identity access. Protected deny behavior remains intact in the controlled check. Root-level directory data is a specific containment change and should be explicit in review.

The fix requires a separately authorized supplier source/build tranche, refreshed source correspondence/supply digests and signed qualification; the existing host-addition grant does not silently authorize it. Runtime source behavior and immutable roots can stay unchanged, though generated release/support evidence must consume the new supplier identity.

Proposed regression/qualification: retain the baseline failure; exact-rule cat/zsh positives; protected read/write negatives; exact generated native policy smoke using the newly built signed supplier with fake provider/no real account; then the owner's native README-read + bounded file-write tool turn. Existing code-mode host signing/JIT policy remains unchanged. Host qualification previously exercised fake dynamic callbacks, not real sandboxed shell execution, so it did not cover this defect.

## Evidence and handoff

All scratch evidence is `/private/tmp/r15-shell-diagnosis/`: `profile.sb`, `direct-cat.json`, `zsh-cat.json`, `differential.json`, `root-minimization.json`, `minimal-protected.sb`, `minimal-protected.json`, and individual variant profiles. Files contain synthetic fixture content only. Ordinary R15 daemon stdout/stderr were read with @-containing lines removed before output; they show admission phases and no shell diagnostic. No live events/session/auth/identity/binding/token/keychain/Codex-home records were read. No broad crash or environment data inspected.

Closure: diagnosis/proposal complete; product repair, source/build authorization, independent review, packaging and native rerun remain pending. Lead continues the existing UI tranche; no App restart or OAuth action was taken here. The one-rule controlled fix strongly explains the native signature but final native causal qualification still requires the corrected signed supplier.
