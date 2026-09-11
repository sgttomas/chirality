# Native load and behavior continuation — combined repair delta, source inputs bound

Status: prepared only; **not executable until this completed packet is independently reviewed and Parent dispositions it**. No compilation or native execution occurred during this update.

This replaces the obsolete prospective compile/extract section while preserving prior evidence: original compile record `/private/tmp/chirality-native-continuation-20260910-01/COMPILE_EXECUTION_RECORD.md` SHA `f00bc54847d0934f2c4065c5f7386994b0e04842b99ee5ee512df0449643da8f`; amended first load record `/private/tmp/chirality-native-watchdog-continuation-20260910-01/NATIVE_LOAD_BEHAVIOR_EXECUTION_RECORD.md` SHA `58033330573b35b960b1584950bbd6c3c75510ad330b0404290b255fcaf45c4f` (pre-amendment `beafeb4e496a0af238cd6885bf91039ae8758142fc581ecc4cb10fdea3a093e8`); diagnostic record `/private/tmp/chirality-native-watchdog-diagnostic-20260910-01/NATIVE_WATCHDOG_DIAGNOSTIC_EXECUTION_RECORD.md` SHA `749fc16ccd507865d4c4890e195958bd1d3c2e7e10a313ede9bec37b48177168`; watchdog repair return `/private/tmp/chirality-release-packaging-20260910/native-watchdog-cleanup-repair-author.md` SHA `03fe9bce90d224f40f84df25862617c28653b3e324d028609d3c5739dc3a01b0`. Both prior loads remain unqualified; behavior has not run.

## Bound inputs

Reused unchanged evidence and bytes:

- watchdog source: `projects/chirality-runtime/tools/native-admission/native-probe-watchdog.c`, 14859 bytes, SHA `81a28a68ba2d58ff5e04f05b1ca8d6184c4add0d7074554267d8adfe13231fef`;
- repaired fixture: `/private/tmp/chirality-native-watchdog-continuation-20260910-01/native-fixture`, 34880 bytes, mode0755, arm64/minOS15, SHA `7449fb8aed586789ad9876e4b7de6dcd4b8d71f940bcce3d29878fb7d4eeacc1`; source SHA `05ee98e9b1eb2c9c6b87595dd7d3ceb0092f0611d707dfde6be48f3aaedf9d49`;
- load probe SHA `4f1700d1a91fbd6b483d1eb251cdfca32e198cd9025cedbc603b455af49bfaf3`; behavior probe SHA `d3e6427022821939488f343e852231c19b7a812810ee4ce3e10eb09b45b59665`, both in `/private/tmp/chirality-native-continuation-20260910-01`;
- complete 585-entry extraction parity record `/private/tmp/chirality-native-watchdog-continuation-20260910-01/electron-extraction-parity.json` SHA `f98e781295f3cb2f0ef8400f949ac125d0723fe50802636258657ceea6739e54`;
- Electron executable SHA `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`, arm64/mode0755; framework SHA `ed19685a25af0788c0dc22be023e6d9c92eaba9c7325fdea6f24485b5092c1a4`, arm64/mode0755;
- SDKSettings SHA `f8d005f09381389167f9e0aeaa169bc9e7dff162ef22ca2fd8e98df7ff1acafe` and compiler/SDK/Node-header paths from the original compile record.

Runtime-owned add-on input:

- final `projects/chirality-runtime/packages/native-admission/src/addon.cc`, 17396 bytes, SHA `f4d705a6dec83c024fa7345e6017cdd518f054208416b9709754f0ff016ad29b`;
- changed compile-relevant header identity: none. Unchanged wrapper `src/index.ts` SHA `fa6d41e687249f7c98781303ef756967fb40fc6ad0999af61c1dc3fbb84131a0`; unchanged `binding.gyp` SHA `24cc5ef00e611b9b1a8d33d1c1a8ee54ea0fcbbab4d8302f71f0270e3928755a`. Runtime author record `/private/tmp/chirality-release-runtime-20260910/native-retirement-repair.md` SHA `48ce2368079b1c308adcc710d9a51763dc612643133c41847c523d74be321227` reports focused 22-test and typecheck PASS. Independent add-on source review `/private/tmp/chirality-release-runtime-20260910/native-retirement-addon-review.md` SHA `3064c27c9912940a7981280611ba97e5663003ab76b59f6079cff70d6d8dd637` binds add-on SHA `f4d705a6dec83c024fa7345e6017cdd518f054208416b9709754f0ff016ad29b` and reports source-only PASS. Rebuild/load/watchdog validation remains required.

Do not substitute the historical add-on source/binary. Runtime source and its independent native-subset verdict are bound. This completed combined packet still requires independent Packaging review and Parent disposition.

## Exact two-output compile

Require `/private/tmp/chirality-native-combined-continuation-20260910-01` absent; create once mode0700; stage only the verified watchdog, final add-on source/changed headers, and reviewed records. Rehash every bound input, tool path, Node header input and SDKSettings immediately before compile. Run each command once, in order, with no retry or alternate recipe:

```sh
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -std=c17 -arch arm64 -mmacosx-version-min=15.0 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk -Wall -Wextra -Werror /private/tmp/chirality-native-combined-continuation-20260910-01/native-probe-watchdog.c -o /private/tmp/chirality-native-combined-continuation-20260910-01/native-probe-watchdog

/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ -std=c++20 -arch arm64 -mmacosx-version-min=15.0 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk -I /Users/ryan/.local/share/mise/installs/node/24.18.0/include/node -DNAPI_VERSION=6 -DNODE_GYP_MODULE_NAME=chirality_native_admission -DCHIRALITY_DARWIN_ONLY=1 -fPIC -bundle -undefined dynamic_lookup /private/tmp/chirality-native-combined-continuation-20260910-01/src/addon.cc -o /private/tmp/chirality-native-combined-continuation-20260910-01/chirality_native_admission.node
```

Capture argv/stdout/stderr/exit. Any failure stops. Bind output hashes/sizes/modes. Statically require watchdog arm64-only Mach-O executable/minOS15/`_main`/libSystem-only and add-on arm64-only Mach-O bundle/minOS15/libc+++libSystem/required two N-API exports/expected dynamic N-API imports/no unexplained import. Static failure stops. Do not compile the fixture or extract Electron.

## Exact load then conditional behavior

Rehash both new outputs and every reused input. Rehash and verify the retained accepted extraction-parity record, and rehash current Electron executable/framework identities; do not rerun the 585-entry inventory. Require canonical synthetic host-home/host-tmp and absent `/private/tmp/chirality-native-behavior-20260910-01`. Use shell-disabled argv and exactly five environment entries: `HOME`, `TMPDIR`, `PATH=/usr/bin:/bin:/usr/sbin:/sbin`, `LANG=en_US.UTF-8`, `ELECTRON_RUN_AS_NODE=1`. Replace `<NEW_ADDON_OUTPUT_SHA256>` only with the newly compiled hash bound in the same record.

Load, exactly once:

```sh
/usr/bin/env -i HOME=/private/tmp/chirality-native-continuation-20260910-01/host-home TMPDIR=/private/tmp/chirality-native-continuation-20260910-01/host-tmp PATH=/usr/bin:/bin:/usr/sbin:/sbin LANG=en_US.UTF-8 ELECTRON_RUN_AS_NODE=1 /private/tmp/chirality-native-combined-continuation-20260910-01/native-probe-watchdog --timeout-seconds 15 --term-grace-seconds 2 --fixture-fallback-seconds 0 -- /private/tmp/chirality-native-continuation-20260910-01/electron-dist/Electron.app/Contents/MacOS/Electron /private/tmp/chirality-native-continuation-20260910-01/native-load-probe.cjs --addon /private/tmp/chirality-native-combined-continuation-20260910-01/chirality_native_admission.node --sha256 <NEW_ADDON_OUTPUT_SHA256>
```

Load passes only with watchdog exit0, proved cleanup, exactly one valid probe PASS, Darwin arm64 Electron43.2.0, Node-API>=6, and exact add-on path/hash. Any other outcome stops without retry or behavior.

Behavior, exactly once only after full load PASS:

```sh
/usr/bin/env -i HOME=/private/tmp/chirality-native-continuation-20260910-01/host-home TMPDIR=/private/tmp/chirality-native-continuation-20260910-01/host-tmp PATH=/usr/bin:/bin:/usr/sbin:/sbin LANG=en_US.UTF-8 ELECTRON_RUN_AS_NODE=1 /private/tmp/chirality-native-combined-continuation-20260910-01/native-probe-watchdog --timeout-seconds 45 --term-grace-seconds 2 --fixture-fallback-seconds 14 -- /private/tmp/chirality-native-continuation-20260910-01/electron-dist/Electron.app/Contents/MacOS/Electron /private/tmp/chirality-native-continuation-20260910-01/native-behavior-probe.cjs --addon /private/tmp/chirality-native-combined-continuation-20260910-01/chirality_native_admission.node --addon-sha256 <NEW_ADDON_OUTPUT_SHA256> --fixture /private/tmp/chirality-native-watchdog-continuation-20260910-01/native-fixture --fixture-sha256 7449fb8aed586789ad9876e4b7de6dcd4b8d71f940bcce3d29878fb7d4eeacc1 --run-root /private/tmp/chirality-native-behavior-20260910-01
```

Require watchdog exit0, overall and every mandatory case PASS, exact identities, matching valid result file, no cleanup failure and no active owned child. The disclosed deterministic concurrent lock-pathname timing case may remain nonblocking `NOT_RUN`. Any required failure stops without retry.

The watchdog remains direct parent, preserves the exact leader through all pre-reap signals, reaps once, and never signals after reap. Signal errors remain recorded; after exact successful reap it always makes the non-signaling group-absence check. Prior signal error is retired only by exact reap plus confirmed absence. Observation/reap/group/clock/fallback uncertainty remains exit125; timeout remains124 after cleanup. Behavior's unconditional14-second fallback exceeds the fixture's 12-second all-mode lifetime and child4-second alarm, but cannot replace probe evidence.

## Evidence and limits

Write one execution record in the new stage containing all input/output identities, exact compiler/static/load/conditional-behavior evidence and cleanup verdict; append the existing Packaging `WORKING_RECORD.md`; preserve every failure and prior stage.

A PASS qualifies only these direct-clang controlled bytes under bare Electron43.2.0. It does not qualify shipping node-gyp bytes, Resources placement/inventory, Electron fuses/environment, supplier/account/provider/native Plan behavior, assembled app/DMG, or release readiness. Final shipping bytes and package must be rebound and separately qualified.
