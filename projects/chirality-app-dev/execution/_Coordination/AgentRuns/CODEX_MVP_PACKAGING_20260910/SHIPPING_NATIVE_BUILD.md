# Shipping native build preparation

Prepared only; no build or native execution authorized by this record. Parent must disposition the independently reviewed sequence. Supplier bytes are not required for this isolated native build; they are required before complete candidate assembly.

Use a new, absent `/private/tmp/chirality-native-shipping-20260910-01`, mode0700. Stage the current native package `src/addon.cc`, `binding.gyp`, and `package.json` with byte parity. Do not reuse or overwrite any prior stage or run npm lifecycle scripts.

Bound source: addon `f4d705a6dec83c024fa7345e6017cdd518f054208416b9709754f0ff016ad29b`; gyp `24cc5ef00e611b9b1a8d33d1c1a8ee54ea0fcbbab4d8302f71f0270e3928755a`; package `527cd7cdb42ffa7022c6ada5f059a590a39e696c9340fcde7d5df9e3ba851d47`. Native independent source review is `3064c27c9912940a7981280611ba97e5663003ab76b59f6079cff70d6d8dd637`. The completed direct-clang synthetic record is `/private/tmp/chirality-native-combined-continuation-20260910-01/NATIVE_COMBINED_EXECUTION_RECORD.md`, SHA `c665e7ccbd2e30c756307cfff0da4687a4886851cc5ff11f405f403c731cc90a`; it is prior evidence, not shipping-byte qualification.

Use the already installed declared node-gyp11.4.2 at `/private/tmp/chirality-v3-adoption-20260909/projects/chirality-runtime/node_modules/node-gyp/bin/node-gyp.js` (entry SHA `fe32cca2954bb37ac0c600ade11cf8a204184d04c3ce0176ca6a7831c644d0ab`, package SHA `f7b6b8bc2c6051e72af8038882314efea54a7b0f7c8c4cf93db264b03c477d60`). Frontend's node-gyp12.4.0 is not a substitute. Current Runtime lock SHA `5e0c8c0dfc93cf3a1535a2ad71a1571691aa2e6164ff88fea8fdec9d0bb7d181` records the dependency basis; The companion `shipping-node-gyp-inputs.json` SHA `00283fc768b513bebcd4efdabbdd68505c59c07001835254dd24f644dc3154ff` binds the canonical installed node-gyp tree and its recursively Node-resolved declared runtime dependency roots: 98 packages, 1430 regular files, exact versions and installed-lock correspondence (installed lock SHA `a23fe9fd906dd88a67c697e12a75bd1fc18492cbb7c337e3fcc56bb0c40e60c6`). Rehash the exact files and reject missing/extra files in each package tree (nested node_modules is covered by separate resolved roots) before and after build. No absent optional dependency was found. This captures reproducibility of already authorized installed dependencies; hashes are not proof of trust or a new supplier acceptance gate. No installation or acquisition.

Explicit existing tools: Node24.18.0 `/Users/ryan/.local/share/mise/installs/node/24.18.0/bin/node`, SHA `ee6fb0e015284d83a91e8ec5213f43a157f8a392b58555301682892ba928c04a`; Xcode Python3.9.6 `/Applications/Xcode.app/Contents/Developer/usr/bin/python3`, SHA `271143990bc83af0fb2404a255038f5faafb96df1584ed7f085e5018c0f33ffb`; Xcode make3.81 `/Applications/Xcode.app/Contents/Developer/usr/bin/make`, SHA `83284837495b77df7cb0febf564717918abe79f5dc5da1df9a603b2ac55998bb`. Reuse the verified Node24.18.0 local headers and Xcode compiler/SDK basis from the native continuation records. Explicit `--nodedir` selects local development files instead of node-gyp's download path, as verified in installed node-gyp configure.js.

## Proposed one build

Execute via shell-disabled argv, cwd the new stage, once:

```text
/Users/ryan/.local/share/mise/installs/node/24.18.0/bin/node /private/tmp/chirality-v3-adoption-20260909/projects/chirality-runtime/node_modules/node-gyp/bin/node-gyp.js rebuild --release --arch=arm64 --nodedir=/Users/ryan/.local/share/mise/installs/node/24.18.0 --python=/Applications/Xcode.app/Contents/Developer/usr/bin/python3 --make=/Applications/Xcode.app/Contents/Developer/usr/bin/make --verbose
```

Start with an empty environment and add only these build entries (no ambient variables): PATH=/usr/bin:/bin:/usr/sbin:/sbin; HOME and TMPDIR are newly created private stage subdirectories; LANG=en_US.UTF-8; DEVELOPER_DIR=/Applications/Xcode.app/Contents/Developer; SDKROOT=/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk; CC and CXX are the previously verified absolute Xcode clang and clang++ paths; MACOSX_DEPLOYMENT_TARGET=15.0; PYTHONDONTWRITEBYTECODE=1; PYTHONNOUSERSITE=1. Both clang and clang++ resolve to the exact Xcode clang target SHA `7def90dd8829726686213a747fc5bff1583df933dae5edc55d755479e0bfe00a`; verify this target and the clang++ link before invocation. No ambient npm config or Node flags, no network/header acquisition, no npm/npx command, no alternate build or retry.

Capture complete stdout/stderr/exit, generated Makefile/target settings/config.gypi, and actual compiler/linker argv. Require the package/gyp contract in generated and executed settings: NAPI_VERSION=6, C++20, CHIRALITY_DARWIN_ONLY, arm64 only, minimum macOS15.0. Stop on disagreement or failure. Do not change source to conceal build failure.

Expected output: `build/Release/chirality_native_admission.node`. Apply the same static checks used for the accepted direct-clang addon: regular executable-mode file, arm64 Mach-O bundle, minimum15.0, two N-API exports, expected N-API imports, only libc++ and libSystem dependencies. Capture exact output hash and size.

## Conditional native checks and later assembly

After successful build/static checks, reuse the accepted watchdog `/private/tmp/chirality-native-combined-continuation-20260910-01/native-probe-watchdog`, SHA `dd0b5cc815e79c69059d7565ba69383932b4d672f113cbdb152c12e7b0147a73`, accepted Electron executable/framework, fixture and JS from the combined sequence. Verify their bound identities and retained parity record; do not repeat extraction or the full inventory audit. Require absent `/private/tmp/chirality-native-shipping-behavior-20260910-01`. Substitute `<SHIPPING_ADDON_SHA256>` only with the new build output hash recorded above.

Run via shell-disabled argv and the exact five-variable probe environment shown, once:

```text
/usr/bin/env -i HOME=/private/tmp/chirality-native-continuation-20260910-01/host-home TMPDIR=/private/tmp/chirality-native-continuation-20260910-01/host-tmp PATH=/usr/bin:/bin:/usr/sbin:/sbin LANG=en_US.UTF-8 ELECTRON_RUN_AS_NODE=1 /private/tmp/chirality-native-combined-continuation-20260910-01/native-probe-watchdog --timeout-seconds 15 --term-grace-seconds 2 --fixture-fallback-seconds 0 -- /private/tmp/chirality-native-continuation-20260910-01/electron-dist/Electron.app/Contents/MacOS/Electron /private/tmp/chirality-native-continuation-20260910-01/native-load-probe.cjs --addon /private/tmp/chirality-native-shipping-20260910-01/build/Release/chirality_native_admission.node --sha256 <SHIPPING_ADDON_SHA256>
```

Only full load exit0, single exact probe PASS and proved cleanup permit this one behavior command:

```text
/usr/bin/env -i HOME=/private/tmp/chirality-native-continuation-20260910-01/host-home TMPDIR=/private/tmp/chirality-native-continuation-20260910-01/host-tmp PATH=/usr/bin:/bin:/usr/sbin:/sbin LANG=en_US.UTF-8 ELECTRON_RUN_AS_NODE=1 /private/tmp/chirality-native-combined-continuation-20260910-01/native-probe-watchdog --timeout-seconds 45 --term-grace-seconds 2 --fixture-fallback-seconds 14 -- /private/tmp/chirality-native-continuation-20260910-01/electron-dist/Electron.app/Contents/MacOS/Electron /private/tmp/chirality-native-continuation-20260910-01/native-behavior-probe.cjs --addon /private/tmp/chirality-native-shipping-20260910-01/build/Release/chirality_native_admission.node --addon-sha256 <SHIPPING_ADDON_SHA256> --fixture /private/tmp/chirality-native-watchdog-continuation-20260910-01/native-fixture --fixture-sha256 7449fb8aed586789ad9876e4b7de6dcd4b8d71f940bcce3d29878fb7d4eeacc1 --run-root /private/tmp/chirality-native-shipping-behavior-20260910-01
```

Retain the reviewed exact-reap/group-absence outcome rule and signal diagnostics. Require behavior exit0, nine mandatory PASS, result-file/stdout parsed equality and no unresolved cleanup. The accepted nonblocking pathname-swap timing limitation remains disclosed. Stop on any required failure, preserve evidence and do not retry. Write one useful execution record in the new stage.

Only after that output is qualified may its exact bytes be staged at the package's declared native extraResource source and bound into the complete Resources inventory. Actual packaged Resources/fuses/entrypoint and candidate behavior remain separate integration checks. Supplier artifact and sidecar membership, final source/dependency/build identity, instructions, notices and app/DMG assembly remain outstanding; no bare-host success establishes release readiness.
