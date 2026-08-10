# Attempt 5 command outcomes

Status: `TERMINAL — OFFLINE PACKAGE CONSTRUCTION PASS — CLEANUP COMPLETE — RAW-CAPTURE VARIANCE`

ChildInstanceID: `A2-DAPP92-A-ATTEMPT5-EXECUTE-01`
PackageID: `PKG-09`
DeliverableID: `DEL-09-04`

## Outcome

Attempt 5 invoked C216 exactly once. C216 exited `0`. Both the standalone
runtime-helper package and the GUI package were constructed from the approved
local Electron 43.2.0 archive through the two temporary `electronDist` keys.
Packaged-dependency verification returned `PASS`, instruction-root integrity
returned `pass`, and the existing source-completeness result remained
`needs_remediation` without being upgraded.

No network-attempt indicator appeared in the complete combined C216 output.
Both electron-builder stages explicitly reported `using custom electronDist
zip file` for the approved `/private/tmp` archive. There was no `download`,
DNS, `ENOTFOUND`, remote fetch, or other network-attempt output.

C179-C184 ran after C216 passed. Exact package hashes, public plist output,
symlink paths and targets, and the standalone/embedded comparison are recorded
in `PACKAGE_IDENTITY_AND_TOPOLOGY.md`. C184 exited `0` and emitted only the
documented framework-directory-loop diagnostics.

Mandatory C185-C195 and C199-C200 cleanup completed with exit `0` throughout.

## Exact command graph results

| Command IDs | Exit / state | Relevant result |
|---|---:|---|
| C096 | 0 | Fixed temporary root proved absent before construction. |
| C097-C104 | 0 each | Exact temporary tree and seven-file rollback snapshot created. |
| C105 | 0 | Seven rollback hashes reproduced the frozen D-APP-89 baseline. |
| C152 | 0 | Frontend `node_modules` proved absent. |
| C153-C164 | 0 each | Exact 12-file D-APP-88 R3 candidate reconstructed. |
| C165 | 0 | All 12 candidate hashes plus package-lock hash reproduced exactly. |
| C166-C173 | 0 each | Exact dependency tree materialized and six accepted R3 Root-package symlinks projected. |
| C174 | 0 | Six accepted symlinks and copied harness-contract facade bound. |
| C175 | 0 | Vitest passed: actual 4 files and 30 tests; historical 5/32 narrative remains untrue and is not upgraded. |
| C176 | 0 | Typecheck passed. |
| C177 | 0 | Production and Electron build passed. |
| C210-C211 | 0 each | Only the approved direct-distribution directory and local archive copy were created. |
| C212 | 0 | Archive SHA-256 reproduced `ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28`. |
| C213 | 0 | Hash-bound overlay script applied exactly two temporary keys. |
| C214 | 0 | Overlay hashes reproduced exactly. |
| C215 | 0 | Exactly two `electronDist` matches, one in each approved config, were bound. |
| C216 | 0 | Sole invocation; helper and GUI packages constructed from the local archive; package-boundary and instruction-root checks passed. |
| C179-C183 | 0 each | Package hashes, public plists, symlink paths, and relative targets captured. |
| C184 | 0 | Standalone and embedded helper comparison found no differences; only expected directory-loop diagnostics emitted. |
| C185-C193 | 0 each | Baseline restored and exact candidate/dependency/build paths removed. |
| C194 | 0 | All eight governed baseline/lock hashes reproduced exactly. |
| C195 | 0 | Exact frontend Git-status output was empty (`0` bytes). |
| C199-C200 | 0 each | Fixed temporary root removed and proved absent. |

## Candidate identity reproduced by C165

| Path | SHA-256 |
|---|---|
| `electron-builder.runtime-helper.json` | `bd1925a50ac18258bd03db0e475f9ac04d4fcbc46ab7a79b62a4090d92580982` |
| `electron/cli-launcher.ts` | `2a0724f11d71a0682d2a9674c24fefd2d2f0137ed70e2190a84944d060a1126d` |
| `electron/main.ts` | `5eeac85fe98ba2c7b76ee98a93ea62fc89f05014b5e1ff381133160a096df491` |
| `electron/runtime-control-ipc.ts` | `970583be61674d8818046108d5129df90d06484d64c94ee904bbfedb2d0f2fc4` |
| `electron/runtime-helper-entry.ts` | `7e0ab20f14d634f9ce4e77fcfa55826cf4b0c022828acaee0709b8927123e2bc` |
| `electron/runtime-helper-path.ts` | `7df8dc3f66d0fc070d3728854f6c5421bd2bff3ba1864bafbacec04485ebbf02` |
| `package.json` | `7996a9066e14188d859c499c243bf6ca2f864f7c2c8616a364c897d6ba658e15` |
| `scripts/build-electron.mjs` | `cee808c108826e9987d5197bdc63c86d32ac1a428e54537fe4c3a3d79138a505` |
| `scripts/embed-runtime-helper.mjs` | `a710b7790ad92c4a64526478baa6e8f49c00a9070c7b84fb22529104f2a79199` |
| `src/__tests__/electron/cli-launcher.test.ts` | `27b3a0e36c4b5592a776057b71fa40ba391cb05170dacc91594e8736caafcc7f` |
| `src/__tests__/electron/runtime-control-ipc.test.ts` | `8402b8b703f44bad6a4f8a74a8614a53ca5294f16c96b6c5b05f47a19ac2964e` |
| `src/__tests__/electron/runtime-helper-packaging.test.ts` | `0915e0b4645bfd194512ed2677ca72d4863884346726aa81265a638ce6826465` |
| `package-lock.json` | `5c8fce2a3c0e2e7b55730ac673ccb07424dcae1e4bbbb408260b1090040c1a56` |

## Overlay binding

| Evidence | SHA-256 / exact value |
|---|---|
| Adopted overlay script | `ba5142bfd3e4ee62a48a1acf663862a357b4790b48f66a33e8bd807148ab208b` |
| Approved Electron archive | `ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28` |
| Overlay helper config | `0822414929eed5ebd6c87d21db8c8c55abd991f1b946c009e64de0467c5583af` |
| Overlay `package.json` | `01e93e41dd8c7d90a8308e5a347d6779093f15d9fd2ae02aa4f9743159ad89ea` |
| Bound local archive path | `/private/tmp/chirality-dapp92-option-a-20260804/electron-dist/electron-v43.2.0-darwin-arm64.zip` |

## Raw-output durability variance

The exact frozen C216 command contained no output redirection. The execution
tool returned the complete combined bytes in chunks `929110` and `dd5a16`, but
the completed session could not be reopened after cleanup. Therefore a raw
byte file and its SHA-256 cannot honestly be asserted. The durable capture
identity and relevant verbatim lines are in
`C216_STDOUT_STDERR_CAPTURE.md`. This variance is escalated to the manager and
fresh verifier; it does not authorize a retry.

## Package result

`PACKAGE_CONSTRUCTED_AND_IDENTITY_CAPTURED`. This is diagnostic evidence only.
It is not a release, accepted product remedy, implementation dispatch, or
authority to launch any helper or GUI.

## Exclusion accounting

- Cache seed: not performed.
- Network: no network-attempt indicator appeared and no successful network
  effect is evidenced; both packages explicitly used the approved local zip.
- Helper/GUI: packages were not launched.
- Process/PID work: not performed.
- LLDB/debugger: not invoked; C196/C197 remains unused.
- Signal/replay: not performed.
- Memory/environment/credential/keychain/secret work: not performed.
- Release/signing/notarization/distribution: not performed; automatic signing
  was explicitly skipped by the package command.
- Git mutation: not performed.
- Task Management and foreign-loop work: not performed.
- Retry/recovery: no retry or recovery command was invented and no second C216
  invocation occurred.
