# Packaging repair native return — separation passes

Heavy slot ended and released; all build/test processes are complete. TASK `/root/live_manager/native`, parent `/root/live_manager`, no descendants. Only the isolated checkout was used. ROOT's exact SCOPE_ADDENDUM and design SHA-256 `7f91e02897de0a15a8d502e9dc351a77e6949d68b369cd891d44940f81a2da55` governed the change. Current full TASK/Root/project instructions and supplied design/failure/activation evidence were read; origin hashes are in PRE_EDIT.json. No other role body was loaded by this TASK on this activation.

## Source change and checks

The CLI source was moved unchanged from `src/bin/swbpipe-control.rs` to `src/live_control_cli/swbpipe-control.rs`. Its SHA-256 remains `725033045d7765b8aa750492cb081ca12c0a543c16f1886048e9f6abcb9275f5`; no stub remains. Cargo changed only that target path. The guide explains version-specific source discovery, feature gating and normal packaging without the CLI feature. Wire/main/lib/native transport/tests/lock/Tauri config/capabilities remain unchanged; FINAL_SOURCE.json contains the comparisons. No new source or scope departure was needed.

Existing supplemental tests passed: **8 native library, 7 transport, 4 CLI unit and 3 CLI integration**. Explicit feature CLI build passed. Commands were serial, locked/offline and jobs2 in the same isolated target. Process-owned socket fixture commands used supported approval escalation. Full commands, zero exit statuses and raw log hashes are in RUNS.json. No test/oracle/limit changed. Known two dead-code warnings remain nonfatal.

## Decisive normal-package result

The maintained `npm run tauri -- build --debug --bundles app` succeeded with live control explicitly unset, Cargo jobs2/offline, npm offline and the same isolated target directory. No CLI feature or Tauri config override was supplied; signing-account environment keys were absent. This was normal bundler regeneration of its own output, without manual bundle surgery or target cleanup.

Full `Contents/MacOS` inventory is now exactly:

- `openpipestress-desktop`

`CFBundleExecutable` is `openpipestress-desktop`; bundled bytes equal the intended target desktop binary. The bundle manifest hash is `086d5ed9cbc98526106180237735b4f506af1793636727d0b6fa3ca232cd8566` under the canonical sorted path/size/file-hash method. Complete Info.plist, file inventory/hash manifest and architecture description are in ARTIFACTS.json.

The original existing CLI artifact hash before any supplemental build was `ff2073bb59b62a3c8b06ae82a88320ac2a8a8fc9ed36321fbb29c5797e96f175`. Explicit relocated CLI checks/build naturally produced the current feature-built artifact. Its immediately-pre-normal-build hash, recorded in IMMEDIATE_PRE_NORMAL_BUILD.json, was `75c4f82e60effee3ee65047e19a027229c18a302de84af6163ff374e05385a3d`. Its post-normal-build hash is **identical**, and it remains present at `target/debug/swbpipe-control`. The normal package excludes it despite that retained artifact. No deleting, moving or cleaning of the CLI target occurred.

The manager's preserved failed app under `target/packaging-evidence/c6837e02-failed/SWBPIPE.app` still matches every original failed-bundle file hash, including its unwanted CLI. Original failed RETURN/ARTIFACTS/raw evidence is unmodified. FINAL_SOURCE.json retains the failed-copy comparison and current Cargo feature fingerprints.

## Boundaries and return

The existing desktop main source and self-test argument bytes are preserved; neither desktop nor packaged self-test was executed. No actual endpoint, browser/CUA, installation, signing-account interaction, primary checkout/bundle, old PID9925 or preference operation occurred. No Git mutation occurred. Actual default-run execution, native listener handshake/I1/I2, human H1/H2, engineering/Runtime/lifecycle/release gates remain open. Source/package separation evidence is ready for the manager's independent complete-delta backcheck and later candidate-bound programme checks.
