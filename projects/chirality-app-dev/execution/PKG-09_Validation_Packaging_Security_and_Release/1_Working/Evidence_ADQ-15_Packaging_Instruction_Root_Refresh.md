# Evidence: ADQ-15 Packaging and Instruction-Root Refresh

## Scope

This record closes the eligible ADQ-15 evidence slice: packaging output, instruction-root integrity,
and packaged Agent SDK subprocess proof. It does not authorize signing, notarization, publication,
external distribution, release-readiness, lifecycle issuance, professional approval, certification,
sealing, authentication, or code-compliance acceptance.

## Source State

| Field | Value |
|---|---|
| Branch | `codex/fuwenc-24554` |
| Source revision used for commands | `ee23734a989f0c5b432d6ce4f6d256fe18406042` |
| Working tree before package run | Clean and synced with `origin/codex/fuwenc-24554` |
| Runtime versions | Node `v24.5.0`; npm `11.5.2` |
| Dev-server isolation | Existing `next-server (v14.2.35)` listener on port 3000 was stopped before packaging. |

## Commands And Results

| Command | Cwd | Result | Evidence |
|---|---|---|---|
| `npm run desktop:dist` | `frontend/` | Pass | Built Next/Electron, generated unsigned local macOS arm64 app/DMG, and ran `npm run instruction-root:integrity`. |
| `npm run harness:validate:agentsdk-packaged-proof` | `frontend/` | Pass | `frontend/artifacts/harness/packaged-agent-sdk/latest/summary.json` |
| `hdiutil attach dist/Chirality-0.1.0-arm64.dmg -nobrowse -readonly` | `frontend/` | Pass | Mounted at `/Volumes/Chirality 0.1.0-arm64`; detached after checks. |
| `node ./scripts/verify-instruction-root-integrity.mjs --bundle-root '/Volumes/Chirality 0.1.0-arm64/Chirality.app/Contents/Resources' --output-root artifacts/harness/instruction-root-integrity/dmg-mounted-adq15-2026-06-21` | `frontend/` | Pass | Dated mounted-DMG integrity summary. |
| `node ./scripts/verify-packaged-agent-sdk-runtime.mjs --bundle-root '/Volumes/Chirality 0.1.0-arm64/Chirality.app/Contents/Resources' --output-root artifacts/harness/packaged-agent-sdk/dmg-mounted-adq15-2026-06-21` | `frontend/` | Pass | Dated mounted-DMG packaged SDK proof summary. |

## Artifact Identity

| Artifact | Result |
|---|---|
| `frontend/dist/Chirality-0.1.0-arm64.dmg` | Present; size `223M`; SHA-256 `3bc5985b1f6665edb2c9f363a5808a5aeb6a40486a53bbacaabf50ed461f75c8`. |
| `frontend/dist/Chirality-0.1.0-arm64.dmg.blockmap` | Present; size `238K`; SHA-256 `0536ffb5d3bc28963b38e9bf2736af4eb1c5e26d0c5f37121a565b2e5f84ffbc`. |
| `frontend/dist/mac-arm64/Chirality.app` | Present; app bundle size `767M`. |
| Mounted DMG app bundle | Present at `/Volumes/Chirality 0.1.0-arm64/Chirality.app`; mounted app bundle size `758M`. |

Generated `frontend/dist/` and `frontend/artifacts/` outputs are ignored build/evidence artifacts and
are not committed as project truth.

## Packaging Posture Checks

| Check | Result |
|---|---|
| App executable architecture | `Mach-O 64-bit executable arm64`. |
| Mounted app executable architecture | `Mach-O 64-bit executable arm64`. |
| `LSMinimumSystemVersion` | `15.0.0` in both build-directory and mounted-DMG app bundles. |
| App version | `0.1.0`. |
| Signing posture | `codesign --display --verbose=4` reports `Signature=adhoc`, `TeamIdentifier=not set`, and `Sealed Resources=none`. |
| Publication posture | `electron-builder` ran with `--publish never`; no signing, notarization, publication, or external distribution step was run. |

## Instruction-Root And SDK Proofs

| Summary | Result |
|---|---|
| `frontend/artifacts/harness/instruction-root-integrity/latest/summary.json` | `status=pass`; `checkedFileCount=47`; `sourceLayout=split`; `gitSha=ee23734a989f0c5b432d6ce4f6d256fe18406042`; SDK bundle missing files `[]`. |
| `frontend/artifacts/harness/packaged-agent-sdk/latest/summary.json` | `status=pass`; `proofMode=scripted-no-live-provider`; resolver exists, is a file, executable bit set, and is under `app.asar.unpacked/node_modules`. |
| Mounted-DMG instruction-root summary | `status=pass`; `checkedFileCount=47`; `gitSha=ee23734a989f0c5b432d6ce4f6d256fe18406042`. |
| Mounted-DMG packaged SDK proof | `status=pass`; `proofMode=scripted-no-live-provider`; resolver is under `/Volumes/Chirality 0.1.0-arm64/.../app.asar.unpacked/node_modules`. |

The build-directory packaged SDK resolver path was:

```text
frontend/dist/mac-arm64/Chirality.app/Contents/Resources/app.asar.unpacked/node_modules/@anthropic-ai/claude-agent-sdk/node_modules/@anthropic-ai/claude-agent-sdk-darwin-arm64/claude
```

The proof captures controlled temporary `CLAUDE_CONFIG_DIR` and `HOME` paths and does not record API
keys or secret material in the committed evidence.

## Skips And Boundaries

- `npm run desktop:pack` was not run separately because `npm run desktop:dist` produced the app
  directory and DMG, then ran instruction-root integrity.
- `npm run proof:network-policy` is reserved for ADQ-16, the separate whole-product secret/network
  evidence item.
- Live packaged SDK read-tool proof was not run; ADQ-15 used the scripted no-live packaged SDK proof
  only.
- No provider/network expansion beyond the current shipped Anthropic path was made.
- No `_STATUS.md`, dependency row, authority document, lifecycle state, signing/notarization,
  publication, external distribution, release-readiness, professional approval, certification,
  sealing, authentication, or code-compliance claim changed.
