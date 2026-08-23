# R19 package checks

- Package: `/Users/ryan/.codex/worktrees/ef5e/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app`
- Bundle ID: `com.chirality.app`
- Short version / bundle version: `2.0.0` / `2.0.0`
- Minimum macOS: `15.0.0`
- Executable: `Chirality`; mode `0755`; size `33968`; Mach-O arm64; `lipo` arm64
- Main SHA-256: `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`
- Runtime CLI: readable/executable mode `0755`; size `75460`
- Runtime CLI SHA-256: `0503c40afde2e3bc2522405305893698f5742687139d00e2fda7995a567af989`
- Codesign: ad-hoc linker-only, no team, no sealed resources, no internal
  requirements. Strict verification returned exit `1` with calibrated
  `code has no resources but signature indicates they must be present`.
- Instruction summary: `pass`, 43 checked files, exact Git SHA
  `d6861ae8251e2a81078577d4496e949735ff199d`, SHA-256
  `1ff8adf9bccc1bd108a4321d4637b8d31b0f443f5fd1f1a8f75e120e54bc9c84`.
- Manifest: 43 files, same exact Git SHA, SHA-256
  `bd2e1e825f570bc8e77ad3b0e0a3093f12f9ac1005ef15f22bdfa3abc6dd340b`.
- `git diff --stat <build-revision>..HEAD -- frontend`: empty.
- Scoped frontend porcelain: empty.

## Packaged R17 guard

Read-only `@electron/asar.extractFile` inspection found
`dist-electron/main.js` at 1,379,498 bytes with SHA-256
`64b99b9a0c661dc53fe71aa6fed184a52220d8c61b4cc41989149c8a672b2947`.
It contains exactly one declaration
`var MACOS_UNIX_SOCKET_PATH_MAX_BYTES = 103`, and exactly one bounded guard
using `Buffer.byteLength(socketPath, "utf8")`, macOS platform `darwin`, and the
deterministic measured/maximum error. Package bytes were not modified.
