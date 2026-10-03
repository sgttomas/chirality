# Packaging exclusion scope addendum

ROOT HELP_HUMAN adopts the HELPS_HUMANS recommendation in DESIGN/RETURN.md (SHA-2567f91e02897de0a15a8d502e9dc351a77e6949d68b369cd891d44940f81a2da55) for the already-authorized development CLI tranche. This corrects the original implementation brief's unsupported exclusion assumption. It does not alter the frozen wire, owner activation, domain scope, human Apply or later qualification/release gates.

WORKING_ITEMS LIVE_MANAGER may delegate the existing native TASK to perform exactly:
- Move apps/desktop/src-tauri/src/bin/swbpipe-control.rs to apps/desktop/src-tauri/src/live_control_cli/swbpipe-control.rs with bytes unchanged, leaving no stub in src/bin.
- Change only that CLI target's Cargo.toml path. Keep target name, feature, required-features, default-run, autobins, desktop/main/wire source and lock/config/capabilities unchanged.
- Update the bounded packaging explanation in docs/LIVE_CONTROL_DEVELOPMENT.md. Build/test/invocation commands and CARGO_BIN_EXE binding stay unchanged.
- Write scoped diagnosis, implementation and verification evidence in LIVE_MANAGER/PACKAGING, preserving the failed normal bundle evidence and supplied frozen briefs.

Read/supply canonical TASK and current Root/project instructions, this addendum and the exact design/evidence. Preserve actual delegated-harness-native parentage and recorded model allocation. Work only in the isolated live checkout; no primary edits. Manager owns integration and local commits of these files and its own records; no push/PR/merge.

Run the existing affected supplemental native/CLI checks sequentially with Cargo jobs2, then the same normal debug .app build with live opt-in unset and without the CLI feature. Keep a feature-built target/debug/swbpipe-control present in that SAME target directory throughout the normal build. Record its before/after hash and the complete Contents/MacOS inventory; require desktop-only bundle, correct CFBundleExecutable and unchanged unbundled CLI presence. Do not clean/move/delete the old CLI or manually edit the bundle to manufacture exclusion. Normal bundler recreation of its own output is expected. No app/self-test/real endpoint/CUA launch, installer/signing-account or host-policy change.

The native/CLI fixture tests retain their earlier scoped execution authority; the package inventory is not a real native handshake. Fresh independent complete-delta backcheck must cover relocation, Cargo/guide, failed/successful package evidence and preserved protocol. Any unexpected additional source/config/test requirement returns to ROOT before scope expansion. All actual native I1/I2 and human H1/H2 witnesses remain open.
