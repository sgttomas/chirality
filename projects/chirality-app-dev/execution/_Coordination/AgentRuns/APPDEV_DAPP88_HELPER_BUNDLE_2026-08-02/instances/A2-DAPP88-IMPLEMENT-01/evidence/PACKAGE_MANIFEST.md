# Package manifest — D-APP-88 helper candidate

Base Git: `97678a841ef58345c73d3470ed8de57c9b1405d2`

## Layout

- GUI: `Chirality.app`, identifier `com.chirality.app`.
- Helper: `Chirality.app/Contents/Library/LoginItems/Chirality Runtime Helper.app`, identifier `com.chirality.app.runtime-helper`, `LSUIElement=true`.
- Helper executable: `Contents/MacOS/Chirality`; copied bytes match the GUI Mach-O. Bundle path and identifier provide the distinct application identity; Electron 43.2 requires the inherited product/executable name to resolve its pre-JavaScript child helper.
- Helper Frameworks is a real directory containing `Electron Framework.framework`, `Mantle.framework`, `ReactiveObjC.framework`, `Squirrel.framework`, and conventional `Chirality Helper.app`.
- Helper Resources is the relative link `../../../../Resources`.
- Framework copies preserve symlink text (`verbatimSymlinks: true`). Final inspection counted 15 helper-local links and zero absolute targets; `Electron Framework.framework/Resources -> Versions/Current/Resources`.
- Package contains exactly one `Chirality Runtime Helper.app`; stale predecessor path is removed deterministically.

## Source hashes

- `electron/runtime-helper-bundle.ts`: `f60f6486051c311d8a81026c5b7236490bced983338e3827efc915bb2870086e`
- `scripts/afterpack-runtime-helper.mjs`: `1b38ae363b76c55f31e50dbbd79f733479d292724b672e2303e6b54ee20b8e5f`
- `electron/main.ts`: `6116044082b404fbe634cb5ad0282ca16ef4fde224ac1237933ce8054346adf0`
- `electron/runtime-control-ipc.ts`: `970583be61674d8818046108d5129df90d06484d64c94ee904bbfedb2d0f2fc4`
- `electron/cli-launcher.ts`: `8ed60f9606d4fb4bb03738ee061393b21c00175996aae78725f4ee1e4a0e34ff`

The `main.ts` hash above is the frozen source after removing the unsuccessful SIGUSR2 diagnostic. The raw plist, executable-hash, and symlink evidence indexed in `raw-salvage/RAW_EVIDENCE_INDEX.md` came from the last diagnostic package, whose `app.asar` still contained that handler. It supports the static package-structure claims above but is not an exact package copy of the frozen source candidate. A clean source-aligned package rerun remains required after blocker disposition.

## Gates

- Focused helper/posture/IPC/CLI tests: PASS, 4 files / 31 tests.
- TypeScript checks: PASS.
- No-publish `desktop:pack`: PASS.
- Packaged dependency boundary: PASS; 0 local-package entries, required packages present, no forbidden development package.
- Instruction-root integrity: PASS, 43 files; standing source-completeness result remains `needs_remediation`.
- `app-hold-integrity`: PASS.
- `harness-self-check`: PASS.
- Explicit change-scope validation: PASS.
- Scoped `git diff --check`: PASS.
