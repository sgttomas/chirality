# Native continuation: compile-only, then separately qualified load/probes

Status: prepared, not executed. The manager inspected source and installed toolchain metadata only. Current input hashes are adjacent in native-continuation-inputs.json. Addon, wrapper and binding.gyp now have an author freeze verified by the manager; independent continuation review and pre-execution parity are pending. Other manifests are read-time observations and must be rebound if changed. No current native output or package is accepted.

## Concrete inputs and missing facts

- Apple Silicon host; Xcode 26.6 (17F113), Apple clang 21.0.0, installed macOS SDK 26.5. Compiler /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++; SDK /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk; Python /usr/bin/python3 3.9.6.
- Exact installed Node /Users/ryan/.local/share/mise/installs/node/24.18.0/bin/node, arm64, Node-API10, modules137. Its include/node headers exist; hashes of seven relevant header/gyp files are recorded. These are locally observed installed inputs, not an independently accepted upstream header acquisition. No new download is necessary for a bounded source compile.
- Source uses C Node-API, no V8/NAN/C++ Node API. BigInt APIs require NAPI_VERSION>=6. binding.gyp pins NAPI_VERSION=6; installed headers otherwise default8. Actual Electron support is still a later measured gate, never inferred from Node24's modules137.
- Existing node-gyp11.4.2 resolves through the source-test dependency tree /private/tmp/chirality-v3-adoption-20260909/projects/chirality-runtime/node_modules. It is usable only as explicitly permitted compile tooling; it is not accepted installed release dependency custody. Its --nodedir option avoids automatic header installation. Exact Electron43.2.0 headers are absent from the known node-gyp43.2.0 cache.
- binding.gyp now explicitly pins NAPI_VERSION=6, C++20 and MACOSX_DEPLOYMENT_TARGET15.0; Runtime authored the amendment after the initial observation. Node common.gypi defaults deployment13.5 and SDK defaults26.5, so those explicit pins are necessary. The author freeze is recorded; independent source/continuation review is pending.
- Native production dependency chain: native-admission -> runtime-core -> runtime-contracts + yaml2.9.0. Frontend now has explicit native-admission file dependency and complete local target/link lock records; daemon production depends native-admission/core/contracts and Pi is dev-only. The entire installed release production closure is not yet qualified: current source dependencies are shared symlinks and must not be reused as package custody proof.
- ABI source change: strict wrapper spawnSupplier(executable,args,secret,{cwd,environment:{HOME,CODEX_HOME,TMPDIR,PATH,LANG},processGroup:true}) lowers to six raw arguments. It returns positive pid and uses new process group, explicit cwd, closed envp, fd3 and CLOEXEC_DEFAULT. Strict wrapper is now spawnGroupedSupplier; raw child exposes observeLeader(WNOWAIT), reapLeader and groupRetired. Preserve leader identity through EOF/TERM/KILL before reap, then prove group absence. Legacy three-argument compatibility is not the production acceptance target.

## Proposed compile-only continuation

After parent disposition and final reviewed source freeze, create a new owned /private/tmp/chirality-native-continuation-20260910-01 directory (fail if it already exists), copy only the frozen native source/gyp/package metadata plus reviewed probe scripts/fixture into that owned directory and record original/staged hashes (addon at src/addon.cc; fixture at native-fixture.c; the two CJS probes at the stage root). Preserve all prior attempts. Freeze the compiler, SDKSettings.json, headers, source, gyp and lock observations again immediately before compile. No supplier, account, credential or addon load belongs to this stage.

The smallest deterministic native compilation uses the installed compiler directly, bypassing npm and node-gyp dependency resolution. This is a compile artifact, not a release packaging claim:

~~~sh
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ \
  -std=c++20 -arch arm64 -mmacosx-version-min=15.0 \
  -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk \
  -I /Users/ryan/.local/share/mise/installs/node/24.18.0/include/node \
  -DNAPI_VERSION=6 -DNODE_GYP_MODULE_NAME=chirality_native_admission -DCHIRALITY_DARWIN_ONLY=1 \
  -fPIC -bundle -undefined dynamic_lookup \
  /private/tmp/chirality-native-continuation-20260910-01/src/addon.cc \
  -o /private/tmp/chirality-native-continuation-20260910-01/chirality_native_admission.node
~~~

The same compile-only stage also builds the reviewed synthetic fixture (without running it), needed by the later behavior probe:

~~~sh
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang \
  -std=c17 -arch arm64 -mmacosx-version-min=15.0 \
  -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk \
  -Wall -Wextra -Werror \
  /private/tmp/chirality-native-continuation-20260910-01/native-fixture.c \
  -o /private/tmp/chirality-native-continuation-20260910-01/native-fixture
~~~

Capture exact argv, stdout/stderr, exit code and output hash. A compiler failure is source feedback, not a reason to continue to a load. Static inspection after successful compilation (no addon execution): file, lipo -info, otool -l/-L, nm -u plus exported NAPI registration symbols, output mode/size/hash. Require arm64, minOS15.0, no unexpected architecture or linked dependency, and all unresolved imports explained by Node-API or supported macOS runtime. Preserve any linker warnings. Direct clang output must not silently replace a later gyp-built artifact: either adopt this exact controlled build recipe for the candidate, or rebuild through the pinned reviewed binding.gyp with explicit --nodedir and compare complete settings/provenance; qualify the actual bytes that will ship.

The selected first continuation is the direct clang source-validation compile above. Shipping build provenance will follow the reviewed explicit binding.gyp recipe; it is not a second proposed execution in this disposition.

## Separate later load and native behavior qualification

Prerequisites: reviewed stable ABI/source, successful compile/static checks, accepted exact Electron43.2.0 arm64 distribution custody, absolute candidate addon path/hash, and explicit bounded native execution disposition. Existing Electron archive pin is electron-v43.2.0-darwin-arm64.zip, size122090802, SHA256 ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28. It was not read/extracted/launched by this preparation. No actual Electron executable path is asserted until its verified extraction or candidate app exists.

The load-only probe must invoke the exact verified Electron executable in ELECTRON_RUN_AS_NODE=1 mode with a reviewed CJS probe and explicit arguments: absolute candidate addon path and expected SHA256. That probe verifies canonical regular-file/no-symlink/hash, asserts Darwin arm64 and process.versions.napi>=6, records Electron/Node/modules/NAPI versions, then uses require(exactAddonPath). It checks acquire/spawnSupplier exports and exits; it must not acquire a lock or spawn anything. The exact command shape, with final verified absolute executable substituted from the custody record, is:

~~~sh
/usr/bin/env ELECTRON_RUN_AS_NODE=1 <verified-absolute-Electron-executable> \
  <reviewed-absolute-native-load-probe.cjs> \
  --addon /private/tmp/chirality-native-continuation-20260910-01/chirality_native_admission.node \
  --sha256 <frozen-addon-sha256>
~~~

The dedicated Type2 probe author brief is NATIVE_PROBE_AUTHOR_BRIEF.md; it prepares tools/native-admission/native-load-probe.cjs and behavior/fixture sources. Until those postimages are reviewed, this later execution remains unavailable. Using ordinary Node would only prove that Node host; it does not discharge the Electron load gate. After actual packaging, repeat load using the candidate's exact Resources/native/chirality_native_admission.node and executable and verify byte parity.

Behavior needs a separate reviewed native fixture executable and fixture runner; there is no existing actual native qualification runner in the repository (runtime-admission-native.test.ts uses fakes/wrappers). The runner must use a new0700 scratch root, synthetic32-byte authority, no real account/home/keyring/credentials/network, explicit addon and fixture hashes, and the strict six-argument production ABI. Required cases: exact lock owner/mode/inode/single-link and contention; lock FD not inherited; fd3 exactly32bytes plus EOF; no extra inherited descriptors; stdout/stdin and bounded wait; canonical cwd and exact5-entry environment, hostile extra/duplicate/missing env rejection; fresh positive process-group ID; descendants terminated by EOF/TERM/KILL deadlines; no post-reap signal/PID reuse; malformed/noncanonical/symlink/permission paths fail closed at their actual owning layer. Deterministic concurrent pathname-swap timing is an explicitly untested coverage limit, not a newly imposed mandatory fixture; actual inode/path binding requirements remain. Tests must inspect actual child state, not merely spy on wrapper calls. Probe fixtures/source/commands must be prepared and reviewed as one bounded execution package before the later native behavior disposition.

Finally, real supplier/credential/network/native Plan qualification and staged/mounted DMG checks remain their owning campaigns. A native fixture pass does not qualify them. Final Resources inventory enumerates every regular file recursively except runtime-artifact-inventory.json itself, including notices/icons; semantic closureRoots cannot exclude siblings. Final source/dependency digests come from actual bundled source contents/build inputs and exact installed production closure. No accepted inventory or release package exists now.
