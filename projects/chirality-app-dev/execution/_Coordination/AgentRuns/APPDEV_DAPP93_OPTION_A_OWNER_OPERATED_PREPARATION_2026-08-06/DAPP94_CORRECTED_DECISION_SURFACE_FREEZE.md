# D-APP-94 corrected decision-surface freeze

Status: `IMMUTABLE NON-DECISIONAL SURFACE — ONE FRESH VERIFIER GATE`

This freeze supersedes `DAPP94_DECISION_PACKET_FREEZE.md` only as the current
unruled D-APP-94 proposal surface. It does not amend the historical attempt-2
intake or its accepted verifier return.

## Bound coordination objects

| Object | SHA-256 |
|---|---|
| corrected D-APP-94 packet | `ef901f572d830da7f1429f980a25928ebd6a56c101bb52605354fe2236e41de0` |
| decision register | `1775fa7c3657d640faa729dc4a1a7247365714a9aeada7d3a547ff1d5e10795e` |
| correction authority adoption | `70305c2a8c6c0db7bc2dcb3a98242c9b9a719cdbe7d7c4f1d4125e208d4194f6` |
| work graph v1.16 | `61c9d2a5e59ee2bc18e82f26bd06ac6b3f710ff7de910dcd6393f502e5f83250` |
| accepted R4.4.6 packet freeze | `13566daa015b49fe1d88d4048bd0d961a29c19bfb653921a6a22a524033f5f89` |
| accepted cleanup-addendum freeze | `8ed898eab6199989538f7c8b011d3f2a522edfe5be8c0314ca68a9ac1a8b7fdf` |

The register contains exactly one D-APP-94 row and retains
`AWAITING_RULING`. The corrected packet records Option A as unsupported,
presents B/C/D without selection, rejects product-byte patching, requires fresh
C1118, and issues no attempt-3 execution token.

## Bound source identities used for the consumer map

| Read-only source | SHA-256 |
|---|---|
| `frontend/electron/main.ts` | `16ad6688abaebd0bb1bfe04921a7eb1d20601bf2f2af983153da3c734f44ad1f` |
| `frontend/electron/runtime-host.ts` | `2e02f592e7e8a6c0008a50cb427044d95aa908e6276b6a9cd8bfe6a1dce248c8` |
| `frontend/electron/api-key-storage.ts` | `f9499fd2ec1441a51238831cb7565caad4b1b5f689bbedbabfc58ceba574df40` |
| `frontend/electron/api-key-ipc.ts` | `f09c9881045b85d04451ca56d0dc1713fb0557d6d343fa94435ba046780b1c62` |
| `frontend/electron/preload.ts` | `61dc59cfe26b2ce73fb4b6d3d34f955e16c60b5838e77a6868975fd7cb334759` |
| `frontend/src/components/settings/api-key-settings.tsx` | `81aeb63608f477f77768e9b6047546cd6f99fd52bd4e40b9b90c75b0db28241a` |
| `frontend/package.json` | `1f14df17d407b18949d5a7195a786574fa8f03eda731dbe7b77f3e91685fba53` |
| `frontend/package-lock.json` | `5c8fce2a3c0e2e7b55730ac673ccb07424dcae1e4bbbb408260b1090040c1a56` |

These are read-only bindings. No product byte changed under this correction.

## Primary-source contract bound for verification

- Electron v43.2.0 safeStorage:
  <https://github.com/electron/electron/blob/v43.2.0/docs/api/safe-storage.md>
- Chromium test-launcher platform handling:
  <https://chromium.googlesource.com/chromium/src/+/refs/heads/main/chrome/test/base/test_launcher_utils.cc>
- Electron v43.2.0 release metadata:
  <https://releases.electronjs.org/release/v43.2.0>

The frozen manager findings presented for adversarial verification are:

1. `--password-store=basic` does not select a macOS Electron v43.2.0
   safeStorage backend and is unsupported as modal suppression: `FAIL`.
2. It cannot make `safeStorage.isEncryptionAvailable()` true on macOS without
   available Keychain: `FAIL`.
3. C1114 is the actual SafeStorageCredentialStore consumer; C1117 can trigger
   a remote credential-status request that reaches it:
   `C1114_CONSUMER / C1117_TRIGGER`.

Any material contrary primary evidence is a verifier BLOCK, not repair
authority. This freeze grants no ruling, feasibility result, source or command
change, keychain/security action, credential access, runtime, GUI, package,
execution, product acceptance, Git, Task Management, or foreign-loop effect.
