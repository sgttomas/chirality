# Independent packaging delta backcheck — bounded fan-in pass

No actionable findings. The complete frozen packaging delta is suitable for manager fan-in within ROOT's SCOPE_ADDENDUM. This concludes the packaging repair backcheck only; it is not integration, lifecycle, engineering or release acceptance.

- Candidate: `4dcd48fe02e54ef225ea854dc438a05164218619`.
- Delta base: `c6837e02c79d6691ff5c66ce5e6bc6171b45fb3f`.
- Reviewer: TASK `/root/live_manager/packaging_review`, parent `/root/live_manager`, through delegated-harness-native assignment; fresh nonimplementer; no descendants. Requested allocation is Astra/xhigh under BRIEF.md.
- Execution root: isolated `/private/tmp/piping-live-control-20260924`. Read-only source/artifact/hash inspection and the read-only scope validator; no tests, builds, npm, sockets, desktop/self-test, browser/CUA, network, installation/signing, resource reservation, primary-checkout operation or Git mutation. Writes are this return and SOURCES.json only.

## Source and contract review

The entire delta has 26 changed-file entries: the CLI rename, Cargo path, guide paragraph and 23 packaging evidence files. All 26 current bytes match the frozen candidate. The repository scope validator passes the exact authorized paths with no violations. No broader core, configuration, capability, package/workspace, target, protocol, command or test change occurs.

The CLI move is byte-identical, SHA-256 `725033045d7765b8aa750492cb081ca12c0a543c16f1886048e9f6abcb9275f5`. The old source is absent and `src/bin` has no entries. Its `#[path = "../live_control_wire.rs"]` resolves to the same shared module at the new directory depth. Cargo differs by precisely the authorized path replacement; target name, feature definition, required-features, desktop target, default-run and autobins are unchanged. The existing `CARGO_BIN_EXE_swbpipe-control` bindings remain in the unchanged integration test.

The guide changes only the packaging explanation and correctly bounds normal packaging to omission of the CLI feature. Its shell command blocks are byte-identical. Wire, main, lib, native transport, both test files, lock, Tauri config and live capability bytes match the base. Frozen WIRE_PROPOSAL and IMPLEMENTATION_BRIEFS also match the base. Thus the existing command/protocol, human Apply and self-test routes are preserved by this delta. Main-source and binary flag presence do not prove execution.

The adopted design hash is exactly `7f91e02897de0a15a8d502e9dc351a77e6949d68b369cd891d44940f81a2da55`. Its exact scope addendum, diagnosis, original failure and repair evidence were reviewed together. The external-source diagnosis is retained as the design's attributed basis; this reviewer used no network. The observed repair result is independently corroborated below.

## Evidence applicability and artifact backcheck

PRE_EDIT's original source hashes match the base; SOURCE_DELTA, IMMEDIATE_PRE_NORMAL_BUILD and FINAL_SOURCE hashes match the candidate. Supplied instruction/origin hashes match their recorded bases. PRE_RUN's `source_tree` resolves to the base's Piping project tree (`ce210d0fa15b64e53a627b4b48ee5062d54ee38d`). All five RUNS log hashes and the original failed-build log hash match their retained bytes.

Raw supplemental logs confirm 8 library tests (102 filtered), 7 transport tests, 4 CLI unit tests and 3 CLI integration tests passing, followed by a successful explicit feature CLI build and maintained normal app build. The CLI unit log names the relocated source. Commands retain the same isolated target, offline resolution and jobs2; normal packaging explicitly unsets live opt-in and supplies no CLI feature. This is review of existing execution evidence, not a reviewer rerun. The installed Tauri CLI remains 2.11.1 with the recorded package hash. All 21 frontend and eight public Wasm-input file hashes still match GENERATED_INPUTS.

Independent on-disk enumeration, file size/hash recomputation and plist decoding establish:

| Artifact | Complete Contents/MacOS inventory | Canonical bundle-manifest SHA-256 |
|---|---|---|
| Preserved failed app | `openpipestress-desktop`, `swbpipe-control` | `1a283b2a280db132792a7bce2f2a27ee193139e9d6f95ea7a70e12ef86565710` |
| Rebuilt normal app | `openpipestress-desktop` | `086d5ed9cbc98526106180237735b4f506af1793636727d0b6fa3ca232cd8566` |

Every failed-copy file matches the original failed manifest; that failure remains a failure. Both plists match the records and name the desktop executable. The rebuilt bundled desktop equals `target/debug/openpipestress-desktop`, SHA-256 `23849ca75ae43eca05b7cf8142b2e3d13715df1a3ff8b2699b7233defc29030b`. No bundle symlinks or additional MacOS entries were found.

The unbundled CLI is still present in that same target, SHA-256 `75c4f82e60effee3ee65047e19a027229c18a302de84af6163ff374e05385a3d`, matching the immediately-pre-normal-build and post-build records. Current Cargo fingerprints match recorded hashes/features: the normal main has no feature; the CLI has live-control-cli. The prior CLI hash change is explicitly accounted for by the authorized relocated CLI tests/build before normal packaging. Retained commands and executor/manager records report no target cleaning, CLI deletion/move or manual output surgery; present artifacts corroborate the required retained-target comparison. Normal bundler recreation of its own app output is the recorded mechanism.

The product-only diff passes `git diff --check`. The complete diff returns 2 solely for extra EOF blank lines in five preserved raw logs; these are nonblocking raw-output formatting observations, not source defects. No raw evidence was normalized or rewritten.

## Remaining gates

Actual native I1/I2, actual-human H1/H2, default-run and packaged self-test execution, the freshly bound eventual integrated-candidate build, and ROOT's applicable clean DEC-025 sweep, hosted/harness checks and complete integrated review remain open. Prior implementation/R1–R5 reviews retain their separate scope; this review neither replaces nor expands them. Signing, installation, Runtime qualification, engineering/lifecycle acceptance and release are not supplied by bundle inventory.
