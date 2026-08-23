# Package and read-only Step-0 evidence

## Exact one-shot invocations

| Invocation | Count | Exit | Evidence |
|---|---:|---:|---|
| `npm run electron:supply-chain` | 1 | 0 | 144-byte log; SHA-256 `5af72fdf79d96a79f68b7d81b118f437d266c0b73e803ac6b8e567cba1ce20ae`; verified-directory output `/Users/ryan/Library/Caches/chirality/electron-dist` |
| `npm run desktop:pack` | 1 | 0 | complete raw 15,854-byte log; SHA-256 `5402cc5f5d24c1d33a6261d129f9ca3555df597babf483b9010facc1d04138e6`; ordinary restricted-network sandbox; no escalation or retry |

The package log contains the exact custom `electronDist` line once, contains zero case-insensitive `download`, `GitHub`, or `release-assets` indicators, records dependency-boundary and packaged-runtime-source `PASS`, and records instruction-root `pass`, 43 checked files, and exact Git SHA `b33858d33220538ce292f276a442792ecf8050b1`.

## Package identity

- App: `/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app`.
- Bundle ID: `com.chirality.app`.
- Short version / bundle version: `2.0.0` / `2.0.0`.
- Minimum macOS: `15.0.0`.
- Main executable: Mach-O 64-bit arm64; mode `0755`; 33,968 bytes; SHA-256 `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`.
- Packaged runtime CLI: mode `0755`; 75,460 bytes; SHA-256 `0503c40afde2e3bc2522405305893698f5742687139d00e2fda7995a567af989`.
- Codesign: ad-hoc/linker-signed; no team; no sealed resources; no internal requirements. Strict verification exited `1` with the calibrated exact diagnostic `code has no resources but signature indicates they must be present`.
- Packaged `dist-electron/main.js`: 1,379,516 bytes; SHA-256 `bfcf16002fc5132d0d96c68a5574927bfd0593b1ce905e71bea72a957bfc4ce1`. Read-only `@electron/asar.extractFile` inspection found exactly one R17 maximum declaration, UTF-8 byte-length check, Darwin predicate, and measured/maximum diagnostic.
- Instruction-root summary / manifest SHA-256: `8760ac4557ce4e75d04d1beb1a972c11dae1891d5ec5dcbc865f99c3b494020d` / `e20a66a57833edc4a8e1ebb60ca570ae49027a410f9ac55d56fcefd0780c723c`; summary `pass`, 43 files, exact b338 revision. The existing source-completeness `needs_remediation` baseline is retained and not upgraded.
- Immediately after build, scoped frontend porcelain and `git diff --stat b33858d33220538ce292f276a442792ecf8050b1..HEAD -- projects/chirality-app-dev/frontend` were empty; frontend tree remained `23315613d0d3e4d21580d928909816dc5aad92c7`.

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

Optionless preflight returned schema `chirality-packaged-launchagent-login-proof-preflight/v1`, status `PASS`, mode `READ_ONLY_PREFLIGHT`, `mutationsPerformed=false`, `sessionRootCreated=false`, and identity SHA-256 `68d5cf944d6bab092a4e5839ca2222bbd5a4dba92cb0fde259eceb07663abd51`.

No prepare, capture, logout/login, bootstrap, kickstart, GUI, default-operator query/mutation, private-root traversal, Desktop evidence traversal, or proof act occurred.
