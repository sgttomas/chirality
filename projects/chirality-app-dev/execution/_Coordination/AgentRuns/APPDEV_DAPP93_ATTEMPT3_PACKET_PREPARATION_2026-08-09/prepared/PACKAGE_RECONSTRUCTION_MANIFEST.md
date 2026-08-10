# Hash-bound package reconstruction manifest — expected future object

Status: `ATTEMPT-3 CANDIDATE — RETURN NAMESPACE BOUND — NOT EXECUTED`

Successor return namespace: sibling `returned_attempt3/`.
The accepted 28-object R4.4.5 sibling `returned/` snapshot is immutable
predecessor evidence and is never a successor source, destination, or absence
target.

This is a recipe and expected-output contract, not an existing package. No
package or build tree was created in this tranche. The Attempt-5 package and
build trees were removed, and its raw C216 stdout/stderr bytes are unavailable.
Attempt 5 contributes only its accepted offline method and contemporaneously
recorded identity/topology/cleanup evidence.

## Frozen existing inputs

Candidate root:
`projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source`.

| Relative path | Current SHA-256 |
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
| `tests/cli-launcher.test.ts` | `27b3a0e36c4b5592a776057b71fa40ba391cb05170dacc91594e8736caafcc7f` |
| `tests/runtime-control-ipc.test.ts` | `8402b8b703f44bad6a4f8a74a8614a53ca5294f16c96b6c5b05f47a19ac2964e` |
| `tests/runtime-helper-packaging.test.ts` | `0915e0b4645bfd194512ed2677ca72d4863884346726aa81265a638ce6826465` |

Frontend lock input:
`package-lock.json` =
`5c8fce2a3c0e2e7b55730ac673ccb07424dcae1e4bbbb408260b1090040c1a56`.

Local Electron input:
`/Users/ryan/Library/Caches/electron/9c4e224684594fb9a8cbda18d3e2b7bf0c3c023d1462402a4031f8b4cc25e621/electron-v43.2.0-darwin-arm64.zip`,
size `122090802`, SHA-256
`ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28`.

The accepted Attempt-5 method is materialized as the D-APP-93-owned overlay
script:
`prepared/apply-local-electron-dist-overlay-dapp93-attempt3.mjs`,
SHA-256
`750a9c5177c9bfc84166baa4e11a06a7296bac7556c3a2135c3fe1502090d7fe`.
Its required post-overlay hashes are
`7deda10bde45936fa9abd2a16ed9c7cf85f9a67cb48dc0b34dcb46c04b3543cb`
for `electron-builder.runtime-helper.json` and
`c3480540e6d3cd54be74ec29bd67d2db3c8d3326e0b4b8da0154725342d8c1e1`
for `package.json`, with exactly one `electronDist` occurrence in each.

## Required future sequence and expected outputs

The exact commands are enumerated in `COMMAND_AUTHORITY_LEDGER.md`. They:

1. prove the fixed temporary root and all frontend derivative targets absent;
2. set `umask 077`, create the isolated home/user/evidence/baseline/
   electron-dist tree, capture owner and initial isolated default/search state,
   create the exact login keychain with `create-keychain -p ''`, perform no
   explicit unlock or isolated bind write, and require exact synthesized
   one-element default/search readbacks;
3. copy and hash the seven D-APP-89 baseline bytes;
4. copy the twelve candidate files into their exact frontend destinations and
   reproduce all candidate plus lock hashes above;
5. copy the accepted local dependency tree and replace only the six named Root
   packages with six exact local symlinks;
6. copy/hash the Electron archive, run the hash-bound two-file overlay, and
   reproduce the two post-overlay hashes;
7. run the focused tests, typecheck, build, and exactly one
   `npm run desktop:pack` invocation with no network authority;
8. freeze package identity/topology evidence, launch every relevant helper and
   Electron operation with the exact sealed HOME and user-data root, enforce
   prompt `NONE`, return/hash-bind fresh attempt-3 authenticated-contact bytes,
   and require the owner's exact visible signature before tracing; and
9. on each terminal path, observe/backstop owner state, commit all raw evidence
   before destructive isolated cleanup, then freeze only the evidence allowed by its already
   enumerated route prerequisites. Restore/remove the declared baseline,
   candidate, and derivative targets, reproduce baseline hashes, prove
   frontend cleanliness, and remove the exact temporary root only when all
   preservation, rollback, cleanup, and absence-proof prerequisites for that
   route succeed. On destination-occupied, prohibited-content, or pre-cut-copy-
   failure routes, retain the applicable exact temporary root, source, partial
   destination, CONTROL, and product state and do not invoke A3-OP-078. On a
   cleanup/rollback-failure route, retain the applicable state, stop further
   destructive cleanup, and do not retry A3-OP-078. An absent fixed root creates
   no removal obligation.

Any absent input, present target, hash mismatch, failed command, network-attempt
indicator, unexpected package path, or extra `electronDist` match stops forward
execution and selects only its separately approved route. Cleanup occurs only
when that route's preservation and cleanup prerequisites are satisfied;
otherwise its declared retained-state obligation governs.

Expected package paths are the standalone helper at
`frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app` and the
GUI at `frontend/dist/mac-arm64/Chirality.app`, including its single embedded
`Contents/Library/LoginItems/Chirality Runtime Service.app`.

Future evidence must freshly bind five actual hashes: standalone helper
executable, helper `app.asar`, helper `Info.plist`, GUI executable, and GUI
`app.asar`. Historical Attempt-5 values are not prospective expected hashes.
It must prove helper bundle ID `com.chirality.app.runtime-helper`, GUI bundle ID
`com.chirality.app`, helper `LSUIElement=true`, version `2.0.0`, public asar
integrity fields, fourteen relative helper framework symlink paths/targets,
and byte/topology equivalence between standalone and embedded helper trees.

Fresh output hashes are `NOT_OBSERVED_BEFORE_AUTHORIZED_EXECUTION`; no
historical package hash is promoted to a current package identity.

## Current absence and non-effects

At successor preparation time, `frontend/node_modules`, `dist`, `dist-runtime-helper`,
`dist-electron`, `dist-runtime`, `.next`, and
`/private/tmp/chirality-dapp93-owner-operated-attempt3-20260809` are absent. The exact
successor `returned_attempt3/` namespace is also absent while accepted
`returned/` remains present and byte-exact. This manifest does not authorize
reconstruction, packaging, launch, signal, cleanup, or any other operation.
