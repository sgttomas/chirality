# Package and read-only Step-0 evidence

## Exact one-shot invocations

| Invocation | Count | Exit | Evidence |
|---|---:|---:|---|
| `npm run electron:supply-chain` | 1 | 0 | 144-byte log; SHA-256 `5af72fdf79d96a79f68b7d81b118f437d266c0b73e803ac6b8e567cba1ce20ae`; verified directory `/Users/ryan/Library/Caches/chirality/electron-dist` |
| `npm run desktop:pack` | 1 | 0 | complete raw 15,852-byte log; SHA-256 `f4f16fe6fc0245793573cd8158c9c8c6c32d972941ccdfc12c87431a15acdde0`; deterministic gzip SHA-256 `dd0c391505f4ae7b84d0987a96f455adecbff2c8fe5ad7d206f55c46177a6637`; ordinary restricted-network sandbox; no escalation or retry |

The package log contains the exact custom `electronDist` line once; contains zero case-insensitive `download`, `GitHub`, or `release-assets` indicators; records dependency-boundary and packaged-runtime-source `PASS`; and records instruction-root `pass`, 43 checked files, exact Git SHA `2ee96958daf997b7a156f020739bde43ca78ebf9`, and the retained source-completeness `needs_remediation` baseline.

## Package identity

- App: `/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app`.
- Bundle ID: `com.chirality.app`.
- Short version / bundle version: `2.0.0` / `2.0.0`.
- Minimum macOS: `15.0.0`.
- Main executable: Mach-O 64-bit arm64; mode `0755`; 33,968 bytes; SHA-256 `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`.
- Packaged runtime CLI: mode `0755`; 75,460 bytes; SHA-256 `0503c40afde2e3bc2522405305893698f5742687139d00e2fda7995a567af989`.
- Codesign: ad-hoc/linker-signed; no team, sealed resources, or internal requirements. Strict verification exited `1` with the calibrated exact diagnostic `code has no resources but signature indicates they must be present`.
- Instruction-root summary / manifest SHA-256: `75e04b92ca5b63f04c5ba81e8b9b519d0dfd2d1aed4ffe88957255e28c60d668` / `5943b94d0fd6f1014005ba211d145d86ab8ebc34f46c2a85a7998aa4db0ce3d8`; summary `pass`, 43 files, exact 2ee revision.
- Extracted packaged `dist-electron/main.js`: 1,379,498 bytes; SHA-256 `64b99b9a0c661dc53fe71aa6fed184a52220d8c61b4cc41989149c8a672b2947`. This differs from the prior 1,379,516-byte / `bfcf16002fc5132d0d96c68a5574927bfd0593b1ce905e71bea72a957bfc4ce1` package and is recorded as independently observed and causally unexplained. No claim attributes it to the test-only source delta.
- R17 semantic guard: the exact b338-to-2ee frontend delta contains only the login-proof test; product source is unchanged. Read-only bundle inspection found exactly one `Buffer.byteLength(socketPath, "utf8")` check, Darwin predicate, and measured/maximum diagnostic. The source retains the single 103-byte maximum declaration.
- Immediately after build, scoped frontend porcelain and `git diff --stat 2ee96958daf997b7a156f020739bde43ca78ebf9..HEAD -- projects/chirality-app-dev/frontend` were empty; frontend tree remained `74e3dbe858b5a4e31d7bf4d3d5e9a7e7f13e76eb`.

The GUI was not launched. The package remains ignored, unsigned local derivative evidence only.

## R20 immutable identity and exact read-only Step 0

- Root: `/private/tmp/ch-r18-91499728-51dd`.
- Label: `com.chirality.ci.runatload.login.owner.macos26.r20.bf0d2e6c-f705-446e-8e4f-a073c6645933`.
- Plist: `/Users/ryan/Library/LaunchAgents/com.chirality.ci.runatload.login.owner.macos26.r20.bf0d2e6c-f705-446e-8e4f-a073c6645933.plist`.
- Service: `gui/501/com.chirality.ci.runatload.login.owner.macos26.r20.bf0d2e6c-f705-446e-8e4f-a073c6645933`.
- Public and failed destinations retain the exact R20 UUID paths staged in the run record.

The exact Step-0 read-only command exited `0`. Package/revision/frontend and 67/103-byte socket gates passed. Root, plist, public destination, and failed destination were absent and non-symlink before and after. Both exact-service `launchctl print` reads exited `113` with exact text:

```text
Bad request.
Could not find service "com.chirality.ci.runatload.login.owner.macos26.r20.bf0d2e6c-f705-446e-8e4f-a073c6645933" in domain for user gui: 501
```

Optionless preflight returned schema `chirality-packaged-launchagent-login-proof-preflight/v1`, status `PASS`, mode `READ_ONLY_PREFLIGHT`, `mutationsPerformed=false`, `sessionRootCreated=false`, and identity SHA-256 `0fb8428713f0df6498e0fe2adbefaf7a5612e730ca37fdc8ffacbac21a30c981`.

No prepare, capture, logout/login, bootstrap, kickstart, GUI, default-operator query/mutation, private-root traversal, Desktop evidence traversal, or proof act occurred. Phase-F tests, full suite, `umask 0002`, typecheck, syntax, APP-HOLD, diagnosis, implementation, and source review were retained and not rerun.
