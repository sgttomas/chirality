# Native admission fixture probes

These sources prepare two bounded probes for the frozen strict native-admission ABI. They are not release, supplier, account, credential, native Plan, or packaging qualification. Review the exact source and hashes before compiling or running anything. A reviewer other than the author must accept the package before native execution.

`native-load-probe.cjs` verifies the exact add-on path and SHA-256, Darwin arm64 Electron runtime with Node-API 6 or newer, then loads the add-on and checks only its two exports. It never acquires a lock or spawns a process. `native-behavior-probe.cjs` uses only the synthetic fixture, a caller-selected new run root, a synthetic 32-byte bootstrap value, and closed deterministic environment values. It preserves the run root and evidence.

After creating the new fail-if-present stage
`/private/tmp/chirality-native-watchdog-continuation-20260910-01` with mode
`0700` and copying the frozen sources to its root with matching hashes, compile
exactly these two outputs once. The existing add-on and old fixture are not
overwritten or rebuilt.

```sh
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang \
  -std=c17 -arch arm64 -mmacosx-version-min=15.0 \
  -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk \
  -Wall -Wextra -Werror \
  /private/tmp/chirality-native-watchdog-continuation-20260910-01/native-probe-watchdog.c \
  -o /private/tmp/chirality-native-watchdog-continuation-20260910-01/native-probe-watchdog

/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang \
  -std=c17 -arch arm64 -mmacosx-version-min=15.0 \
  -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk \
  -Wall -Wextra -Werror \
  /private/tmp/chirality-native-watchdog-continuation-20260910-01/native-fixture.c \
  -o /private/tmp/chirality-native-watchdog-continuation-20260910-01/native-fixture
```

Do not run either command until the parent has disposed the exact two-output
compile stage. Run each command once with no retry or alternate recipe. Record
source, compiler, SDK, argv, output, exit status, architecture, minimum OS,
mode, size, linkage and SHA-256. Compile success is source evidence only.

`native-probe-watchdog.c` is the separate outer process supervisor for both
Electron probe hosts. Compile and statically inspect it only under a separately
reviewed continuation. It must be the direct parent of the exact Electron
executable. It preserves the Electron leader unreaped with `WNOWAIT`, sends
TERM and KILL to the anchored process group, reaps once, then only diagnoses
group absence. It never signals from a recorded PID or after reap. Exit 124
means the wall-clock deadline expired; exit 125 means cleanup was not proved.
On macOS, a process-group signal can return `EPERM` when XNU's group iteration
finds only the zombie leader. The watchdog preserves that result and errno in
its diagnostic, reaps the exact observed leader, and still performs the
non-signaling post-reap group-absence check. Exact reap plus confirmed group
absence proves terminal cleanup despite that earlier signal result; an
unobserved or unreaped leader, a live or unresolved group, clock/fallback
uncertainty, or timeout still fails. No signal is ever sent after reap.
Every spawned-host terminal path also emits one bounded JSON diagnostic on
stderr with waitid observations and captured errno values, TERM/KILL results,
reap result/status, post-reap group-absence result/deadline, monotonic-clock
errno, and separate fallback-required/fallback-elapsed values. It includes no
child arguments, environment values, paths, bootstrap bytes, or credentials.

The fixture now has a fixed maximum lifetime in every mode, and its forked
descendant installs its own timer because interval timers are not inherited
across `fork()`. This source change invalidates the previously compiled fixture
SHA-256 `d3baade7a80c8d83a629cc12d8531f78ae1c059ded616f40da103d8e9d958d6e`.
Do not execute behavior using that old fixture. Recompile the frozen repaired
source once under a separately authorized recipe, statically inspect it, and
bind the new source/output hashes before any behavior run.

After separate approval, watchdog compilation/static inspection, and verified
Electron custody, the load command shape is:

```sh
/usr/bin/env -i HOME=<canonical-synthetic-host-home> TMPDIR=<canonical-synthetic-host-tmp> \
  PATH=/usr/bin:/bin:/usr/sbin:/sbin LANG=en_US.UTF-8 ELECTRON_RUN_AS_NODE=1 \
  <verified-absolute-native-probe-watchdog> --timeout-seconds 15 \
  --term-grace-seconds 2 --fixture-fallback-seconds 0 -- \
  <verified-absolute-Electron-executable> <reviewed-absolute-native-load-probe.cjs> \
  --addon <canonical-absolute-candidate-addon.node> \
  --sha256 <candidate-addon-sha256>
```

The later behavior command shape is:

```sh
/usr/bin/env -i HOME=<canonical-synthetic-host-home> TMPDIR=<canonical-synthetic-host-tmp> \
  PATH=/usr/bin:/bin:/usr/sbin:/sbin LANG=en_US.UTF-8 ELECTRON_RUN_AS_NODE=1 \
  <verified-absolute-native-probe-watchdog> --timeout-seconds 45 \
  --term-grace-seconds 2 --fixture-fallback-seconds 14 -- \
  <verified-absolute-Electron-executable> <reviewed-absolute-native-behavior-probe.cjs> \
  --addon <canonical-absolute-candidate-addon.node> \
  --addon-sha256 <candidate-addon-sha256> \
  --fixture <canonical-absolute-native-fixture> \
  --fixture-sha256 <native-fixture-sha256> \
  --run-root <new-canonical-absolute-0700-run-root>
```

The behavior probe never removes or reuses a run root. It verifies file identities before loading or spawning, invokes only the explicit fixture, bounds reads and leader lifecycle operations, and emits per-case results plus a preserved JSON record. Descriptor coverage uses Darwin `PROC_PIDLISTFDS` to enumerate the fixture's actual open descriptor table and requires exactly descriptors 0, 1, 2, and 3. This checks that neither the held lock descriptor nor another parent descriptor crossed the spawn boundary.

After every behavior-host completion, including success, crash and timeout, the
watchdog retires the anchored Electron group and then proves that the full
fallback interval beyond the fixture maximum lifetime elapsed. Clock or wait
uncertainty exits 125. This delay does not turn host-group absence into fixture
cleanup proof: timeout remains a failure, and missing behavior evidence cannot
be accepted as PASS.

The frozen raw API requires the strict executable, working directory, and three synthetic environment directories to be existing canonical paths. The probe verifies rejection of symlink and missing paths, fixed ordered environment values, strict process-group selection, and exact argument arity before relying on `posix_spawn_file_actions_addchdir_np`.

The strict lifecycle starts `observeLeader()` with `WNOWAIT` so the leader identity still anchors the group. The resistant-descendant case starts observation, closes input, sends TERM, observes that the descendant survived, sends KILL before reaping, requires output-pipe EOF, confirms the leader result, calls `reapLeader()` exactly once, and polls `groupRetired()`. The fixture also self-retires after a bounded interval as a failure fallback. The runner never signals after reaping.

The lock pathname-swap timing race is reported as a nonblocking `NOT_RUN` coverage limit because this bounded fixture has no deterministic coordinator inside synchronous `acquire()`. Real owner, mode, symlink, hardlink, contention, release, and inode consistency cases still run. The raw add-on constrains the closed environment to five entries in canonical order, requires canonical directories for HOME/CODEX_HOME/TMPDIR, and fixes exact `PATH` and `LANG` values; the child observation independently verifies the received environment.
