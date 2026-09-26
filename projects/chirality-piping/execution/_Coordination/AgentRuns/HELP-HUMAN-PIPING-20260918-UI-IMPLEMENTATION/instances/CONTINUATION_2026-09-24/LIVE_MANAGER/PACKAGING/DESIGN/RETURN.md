# Development CLI packaging repair — design return

Recommendation: **retain the existing Cargo package and binary target, but move the CLI entrypoint out of `src/bin`.** This is the smallest supported source-layout repair found for the resolved Tauri CLI 2.11.1. It preserves CLI commands, wire and tests, needs no new package/workspace or Tauri configuration, and does not depend on deleting the pre-existing CLI artifact. Actual repaired packaging evidence is still required.

Read-only assessment by `/root/design_manager`, HELPS_HUMANS Type 1, child of ROOT through delegated-harness-native continuation. Basis: `/private/tmp/piping-live-control-20260924`, branch `codex/piping-live-control-20260924`, commit `c6837e02c79d6691ff5c66ce5e6bc6171b45fb3f`; current untracked PACKAGING evidence read. Only this DESIGN directory written. No child, product edit, build, test, executable launch, native/CUA, cache cleanup or resource reservation. Origins and hashes are in SOURCES.json.

## Version-specific finding

The installed `@tauri-apps/cli` and native `@tauri-apps/cli-darwin-arm64` packages both report 2.11.1, matching GENERATED_INPUTS. Its installed configuration schema exposes no bundled-Cargo-binary include/exclude list. `mainBinaryName` renames the main binary; `bundle.targets` chooses bundle formats and `externalBin` adds sidecars.

The official **tauri-cli-v2.11.1** source explains the observed result: `get_binaries` filters explicit `[[bin]]` entries by `required-features`, then independently enumerates `src/bin` and adds missing entries. That second pass does not apply the feature filter or Cargo `autobins` value. Moving this explicitly declared target outside that discovery directory preserves the first filter while eliminating re-admission. This is a source-based diagnosis, corroborated by the recorded failed bundle; it is not a repair execution. [Version-matched binary enumeration, lines 630–678 and 868–949](https://raw.githubusercontent.com/tauri-apps/tauri/tauri-cli-v2.11.1/crates/tauri-cli/src/interface/rust.rs).

The official matching bundler copies its selected binary list and recreates its own output app directory. It does not indiscriminately copy every executable in target/debug. Thus an old unselected CLI file may remain there without being bundled. This is the specific claim to verify on the repair. [macOS bundler, lines 51–64 and 151–165](https://raw.githubusercontent.com/tauri-apps/tauri/tauri-cli-v2.11.1/crates/tauri-bundler/src/bundle/macos/app.rs).

## Exact proposed source change

Relative to `projects/chirality-piping/apps/desktop/src-tauri`:

1. Move `src/bin/swbpipe-control.rs` to `src/live_control_cli/swbpipe-control.rs`, preserving file bytes. Its existing `#[path = "../live_control_wire.rs"]` still resolves to the same shared wire module because directory depth is unchanged. Leave no forwarding source/stub in `src/bin`.
2. Change only the CLI `[[bin]].path` in Cargo.toml to `src/live_control_cli/swbpipe-control.rs`. Retain `name = "swbpipe-control"`, `required-features = ["live-control-cli"]`, feature definition, explicit desktop bin, `default-run`, and `autobins = false`.
3. Amend the development guide's packaging explanation: the feature gate **and source placement outside Tauri's auto-discovery directory** provide normal bundle separation. CLI build/test/invocation commands remain identical. Record the exact supported normal packaging conditions: no `live-control-cli` feature in the Tauri packaging invocation. Explicitly enabling that feature for a Tauri bundle would select the CLI; this proposal does not promise exclusion for an intentionally feature-enabled bundle.
4. Preserve frozen WIRE_PROPOSAL and historical IMPLEMENTATION_BRIEFS as supplied evidence. ROOT records a small implementation addendum authorizing the new source path and correcting the old unsupported claim that feature/default-run alone exclude bundling. No new semantic owner decision is required for this implementation correction.

Cargo supports explicit target source paths and required features. This keeps the target's identity while changing its source location; a new target kind is unnecessary. [Cargo target configuration](https://doc.rust-lang.org/cargo/reference/cargo-targets.html#configuring-a-target).

No changes are needed to `src/main.rs`, `src/lib.rs`, transport/wire modules, existing `tests/live_control_cli.rs`, Cargo.lock, tauri.conf.json, capability grants, Node packages or desktop identity. `CARGO_BIN_EXE_swbpipe-control` remains valid for the existing integration tests. The current CLI has no dependency on its original source-directory name beyond the still-correct relative wire import. Keep the normal `--self-test-saved-edited-load` main entry byte-identical.

## Options compared

| Option | Viability and consequences |
|---|---|
| **Move explicitly declared CLI source outside src/bin** | Recommended. One source relocation, one Cargo path, bounded documentation/addendum. Same package, feature, executable name/path, test binary environment variable and wire. No lock or registered-check changes required. |
| New CLI example target in the same package | Avoids bin enumeration, but changes the build selector/output location and invalidates the existing binary integration-test environment binding. Requires test/guide changes with no benefit over the path-only move. Do not select. |
| Separate standalone Cargo package | Viable fallback for permanent package separation: its own manifest/lock, copied or path-shared wire dependency, moved CLI tests, new manifest-path commands and explicit test registration/coverage. Could retain executable syntax, but changes package/build ownership and increases maintenance. ROOT would have to grant exact scope; no workspace is needed or proposed. Not justified while the smaller option remains viable. |
| New Cargo workspace | Forbidden by the current brief and unnecessary. Any reconsideration would require ROOT's explicit scope. |
| `default-run`, `autobins`, feature gate without moving source | Already contradicted by retained packaging evidence. Do not repeat as a repair. |
| mainBinaryName, bundle format selection, externalBin or Cargo `--bin` alone | Not a demonstrated bundling exclusion mechanism. The correct main was already built and selected in the failing result. |
| Delete/rename the compiled CLI before bundling; clean target; remove CLI from produced app | Hides the triggering target state or edits output after selection. Not an acceptable repair or acceptance proof. |
| Patch/update Tauri or broad packaging hooks/configuration | Out of scope and more disruptive than a supported explicit Cargo path. No vendor patch, grants, signing or installer change proposed. |

## Checks and exact acceptance evidence

These are future actions for the named writer/ROOT after scope and resources are assigned; none was executed here.

- Review the source-only delta and confirm renamed CLI bytes, shared wire bytes, main entry, target name/features/default-run and lock/config remain as specified. Cargo metadata can confirm the explicit target path/name if useful; it is not bundle evidence.
- Run the existing supplemental native/CLI checks, including the unchanged documented command `cargo test --manifest-path apps/desktop/src-tauri/Cargo.toml --features live-control-cli --bin swbpipe-control --test live_control_cli` from the Piping root. Preserve their controlled-handler framing/error/recovery coverage; no new live endpoint is needed just to test packaging. Run the affected existing native library/transport tests as already assigned by LIVE_MANAGER.
- For the decisive regression, preserve the original failed bundle evidence first. Retain an actual feature-built `target/debug/swbpipe-control` in the **same target directory** and record its hash/presence immediately before the ordinary build. Do not clean or move it. Use the same maintained `npm run tauri -- build --debug --bundles app` from `apps/desktop`, with the recorded isolated environment and live opt-in unset. No packaging feature should select the CLI. The normal bundler's regeneration of its own `.app` is expected output behavior, not a manual cleanup workaround.
- After a successful build, enumerate **all** `Contents/MacOS` entries: require only the expected desktop executable, correct `CFBundleExecutable`, equality of bundled desktop bytes to the intended newly built main, and continued presence/hash of the unbundled CLI target artifact. Retain the full bundle manifest, command/environment, build output and candidate identity. A clean-target-only result is insufficient.
- Separately verify `cargo run` default selection and the packaged self-test under ROOT's existing native execution plan/resource gate. Source/binary flag presence is not execution. Do not launch either in the packaging-only evidence step or claim that a bundle inventory proves the live connection.

`software-workflow.json` registers desktop test/build for apps/desktop and harness checks for documentation/evidence; the product change still needs the clean DEC-025 sweep, applicable hosted checks and complete independent review under project rules. **The sweep's Rust discovery covers only `core` and `validation/benchmarks`, not desktop src-tauri.** Therefore its pass does not replace the explicit supplemental native/feature-enabled CLI checks above. No new crate or test registry change is needed for this path-only repair. If ROOT chooses the standalone-package alternative instead, its native/CLI checks must receive an explicit durable execution home rather than assuming discovery will find them.

The proposed repair changes build layout only. It preserves protocol, human Apply, disabled normal startup, same-session recovery, native/self-test semantics and all later human/qualification/release boundaries. Only ROOT's concrete file-scope addendum and actual repair evidence remain; this design does not reopen owner activation or grant release/installer work.
