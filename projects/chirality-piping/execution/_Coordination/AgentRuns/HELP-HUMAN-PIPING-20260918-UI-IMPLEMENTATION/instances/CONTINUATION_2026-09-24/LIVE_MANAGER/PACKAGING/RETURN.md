# Isolated normal-app packaging check — separation failure

WORKING_ITEMS /root/live_manager executed the maintained build directly under ROOT's bounded grant; no new TASK was launched. Source/evidence basis was clean `c6837e02c79d6691ff5c66ce5e6bc6171b45fb3f`. Canonical WORKING_ITEMS was reread; current instruction/source identities and exact command are in PRE_RUN.json. Only isolated generated artifacts and this PACKAGING subtree changed. All build processes are finished and released.

## Actual result

`npm run tauri -- build --debug --bundles app` **succeeded, exit 0**, with Cargo jobs2, offline resolution, isolated target and SWBPIPE_LIVE_CONTROL explicitly unset. No signing-account environment keys or TAURI_CONFIG override were present. Tauri built `target/debug/openpipestress-desktop` and produced `target/debug/bundle/macos/SWBPIPE.app` in the isolated desktop directory.

The packaging separation check **failed**. Full `Contents/MacOS` file list:

- `openpipestress-desktop`
- `swbpipe-control`

`CFBundleExecutable` correctly names `openpipestress-desktop`. Its bundled bytes equal the newly built desktop binary. However, the CLI is NOT absent: its bundled bytes equal the existing feature-enabled `target/debug/swbpipe-control` from the earlier controlled CLI build. The latest desktop Cargo fingerprint records `features:[]`; the CLI fingerprint records `["live-control-cli"]` and an earlier modification time. Thus the CLI feature was not selected for the new main build, but its pre-existing artifact was silently copied into the normal app bundle. Explicit default-run and required-features do not establish bundle exclusion in this observed target state.

The bundle manifest hash is `1a283b2a280db132792a7bce2f2a27ee193139e9d6f95ea7a70e12ef86565710`, computed over canonical JSON of sorted relative paths, sizes and each file's SHA-256. Complete Info.plist, executable list, Mach-O architecture descriptions, exact per-file/target hashes and Cargo fingerprints are in ARTIFACTS.json. Generated frontend/Wasm inputs and tool versions are in GENERATED_INPUTS.json; raw build output remains build.raw.txt. The first read-only absence assertion exposed the extra binary; the artifact was preserved rather than removed.

## Preserved route and limits

`src-tauri/src/main.rs` remains byte-identical to base2b310992, SHA-256 `03c5b9f8fc8812114d1a7db1b1e2c5c9f2ce6c7bbf0f000565fbb872e7a1d5ca`. It still checks `--self-test-saved-edited-load` before normal run, and that flag's bytes are present in the bundled desktop executable. This is source/binary presence evidence only: neither the app nor self-test was executed.

No source/configuration repair, cleanup/rebuild, bundle installation, signing-account interaction, endpoint activation, app/self-test launch, CUA/browser or PID9925 action occurred. No primary bundle was overwritten. Two already-known dead-code warnings remain; the build did not fail. No I1/I2/H1/H2, runtime admission or native behavior gate is fulfilled, and ROOT still needs a freshly bound build of its eventual integrated native candidate.

## Concrete return to ROOT

A bounded packaging repair is needed before the normal-app exclusion claim can pass: ensure the maintained Tauri bundle inventory excludes the standalone CLI even when a prior feature-enabled CLI binary exists in the same target directory. The current feature gate protects main compilation selection but did not protect bundle contents. This return proposes the required behavior, not an unverified Cargo/Tauri configuration mechanism. ROOT must name the repair scope before source/config edits; preserve this failing bundle/manifests for comparison. No further build or repair was performed.
