# Phase-B supply and package checks

## One-shot commands

- `npm run electron:supply-chain`: exactly once, exit `0`; complete log 145 bytes, SHA-256 `200522b9040843bbc4eed6d781f1611b2d54f4f9dd5c8f285abe56688c49e422`. Output is only the npm lifecycle preamble and `/Users/ryan/Library/Caches/chirality/electron-dist`.
- `npm run desktop:pack`: exactly once in the ordinary network-denied sandbox, exit `0`; no escalation or retry. Complete terminal output with CR progress characters normalized away is 15,852 bytes, SHA-256 `d462b1efa4ab63a400b8e2efc96bd3b59a8eb9a0e173a6ff887aa9cb6f9fbdd2`.
- Exact custom `electronDist` line count: `1`.
- Case-insensitive `download`, `github.com`, and `release-assets.githubusercontent.com` indicator count: `0`.
- Embedded dependency boundary: `PASS`; packaged runtime source proof: `PASS`.
- Embedded instruction-root integrity: `pass`; 43 files; exact Git SHA `cb008dc5d6aa9b249639c91f3453a18609530d0f`.

## Package identity

- App: `frontend/dist/mac-arm64/Chirality.app`.
- Bundle ID: `com.chirality.app`.
- Short / bundle version: `2.0.0` / `2.0.0`.
- Minimum macOS: `15.0.0`.
- Executable: `Chirality`, mode `0755`, 33,968 bytes, Mach-O 64-bit arm64, `lipo` arm64.
- Main executable SHA-256: `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`.
- Owner-reported R19 main SHA-256: `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`; observed R20 identity is equal.
- Runtime CLI: `Contents/Resources/runtime-cli/chirality-cli.mjs`, mode `0755`, 75,460 bytes, `/usr/bin/env node` UTF-8 text executable.
- Runtime CLI SHA-256: `0503c40afde2e3bc2522405305893698f5742687139d00e2fda7995a567af989`.
- Codesign diagnostic: `flags=0x20002(adhoc,linker-signed)`, `Signature=adhoc`, `TeamIdentifier=not set`, `Sealed Resources=none`, `Internal requirements=none`. Strict deep verification returned the calibrated exit `1`: `code has no resources but signature indicates they must be present`.
- Instruction summary SHA-256: `3a9666d40235dfbaedf16dc3da29b0bc541b64298ae2faec05dcb27a202d3b36`.
- Instruction manifest SHA-256: `c5b2bf101de6412ae63fd19ba76cac6c73cffa156357551c4203a54ce771135b`; 43 files and exact revision.
- Empty `git diff --stat cb008dc5d6aa9b249639c91f3453a18609530d0f..HEAD -- projects/chirality-app-dev/frontend` and empty scoped frontend porcelain.
- Packaged `dist-electron/main.js`: 1,379,516 bytes, SHA-256 `bfcf16002fc5132d0d96c68a5574927bfd0593b1ce905e71bea72a957bfc4ce1`; exactly one `MACOS_UNIX_SOCKET_PATH_MAX_BYTES = 103` declaration and the UTF-8 byte-length/darwin/fail-closed overlong diagnostic are present.

This is unsigned local build evidence only. No signing, notarization, distribution, release, or proof claim is made.
