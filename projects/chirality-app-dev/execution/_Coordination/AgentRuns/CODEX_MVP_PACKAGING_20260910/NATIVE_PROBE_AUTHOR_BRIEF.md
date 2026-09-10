# Sealed Type2 brief: native fixture and probe preparation

Role: ephemeral Type2 author, gpt-5.6-sol, medium. Do not delegate. Parent dispatch through /root after Packaging confirms raw ABI freeze. Objective: prepare one complete bounded native load/behavior probe source package for the current strict native-admission ABI. No native compilation, addon require/load, Electron launch, fixture execution, supplier, network, account, keyring or real credential action.

Checkout: /Users/ryan/.codex/worktrees/chirality-change-lessons-20260910/chirality. Read Root/Runtime AGENTS and packages/native-admission/src/{addon.cc,index.ts}, binding.gyp, tests/runtime-admission-native.test.ts, and App packaging run/NATIVE_CONTINUATION.md. Only necessary context; no broad historical research.

Write scope (new files only; coordinate if any already exists):
- projects/chirality-runtime/tools/native-admission/native-load-probe.cjs
- projects/chirality-runtime/tools/native-admission/native-behavior-probe.cjs
- projects/chirality-runtime/tools/native-admission/native-fixture.c
- projects/chirality-runtime/tools/native-admission/README.md
- /private/tmp/chirality-release-packaging-20260910/native-probe-author.md (one revisable return)
Do not edit addon/wrapper/launcher/host/source dependencies/manifests/build scripts or accepted governance. Packaging manager owns NATIVE_CONTINUATION.md integration and Runtime owns native internals. No Git mutations.

Raw API signature frozen by Runtime native author; source internals are still under implementation/review:
raw require(addon).acquire(canonicalPrivateDirectory,'runtime-admission-authority.lock') -> opaque held/device/inode/created/close lease.
raw spawnSupplier(executable,argv,Buffer.alloc(32,syntheticValue),canonicalCwd,exactFiveEnvironmentEntries,true) -> positive pid/read/write/wait/closeInput/terminate/kill. Strict production options only. The legacy three-argument path must not be used to qualify the strict path. Environment keys exactly HOME,CODEX_HOME,TMPDIR,PATH,LANG; LANG=en_US.UTF-8 and PATH=/usr/bin:/bin:/usr/sbin:/sbin. Cwd canonical validation currently belongs to the TS wrapper; raw native applies chdir. Do not assert nonexistent native canonical rejection: inspect and distinguish wrapper-vs-native guarantees, and report the gap explicitly. Fresh process group pid and TERM/KILL target group; inherited bootstrap fd3 exactly32 bytes+EOF, CLOEXEC_DEFAULT hides lock/all other inherited FDs.

Load runner:
- CLI exact --addon absolutePath --sha256 expectedHex; accepts no ambient/default addon.
- Before require: normalized canonical absolute regular-file path, no symlink, hash equality; Darwin arm64 host; Electron present, NAPI>=6; emit only exact runtime versions/path/hash/result (no general env dump).
- require(exactPath); require acquire and spawnSupplier functions; no acquire/spawn call. Bounded JSON result +nonzero failure; failure retains evidence, no cleanup.
- Imported module must not load/run. Main guard controls actual invocation; export small validation helpers only if useful for safe pure tests.

Behavior runner:
- Explicit --addon/--addon-sha256 --fixture/--fixture-sha256 --run-root; exact Electron and ABI assertions same as load runner. New canonical0700 run root must not exist; never use/delete preexisting directory. Synthetic HOME/CODEX_HOME/TMPDIR all under it, no ambient home or credentials. Explicit deterministic PATH and LANG. No network/supplier executable.
- Verify addon+fixture identity before load/spawn. Preserve fixtures/evidence on pass/failure; no broad cleanup. Bound child deadlines, wait all spawned children, retire owned groups on failures without signaling after successful reap. Signals only handles/PIDs created by this run.
- Exercise actual acquire owner/mode/single-link/lock contention/release, symlink/wrong-mode/hardlink failures; inode consistency where deterministically testable. Record any race case requiring additional fixture support rather than pretending wrappers prove it.
- Strict spawn inspect: fixture reports cwd, only synthetic expected env keys/values, pid/pgrp; fd3 exact synthetic32 bytes+EOF; actual open FD inspection verifies no parent sentinel/lock descriptor and no unexpected inherited descriptor (do not treat partial arbitrary FD scan as full closure). Use an appropriate Darwin mechanism or enumerate the full actual finite descriptor limit; report coverage explicitly.
- Verify stdin/stdout/EOF/wait and known exit/signal cases, malformed secret lengths and strict argv/env/cwd/processGroup rejection, canonical/symlink cwd behavior. Cases must match frozen raw ABI rather than silently assuming wrapper checks protect direct native calls.
- Descendant fixture demonstrates new owned group, TERM and KILL retirement including a deliberately TERM-resistant child; track/wait exact spawned parent and prove descendants exited. No post-reap/PID reuse signaling. A pid number alone is not proof; record fixture identity/group/observed termination. No inherited real file access.
- Output per-case PASS/FAIL/NOT_RUN and final explicit native fixture scope, never supplier/account/Plan/release qualification. Timeouts fail and preserve artifacts.

Fixture source:
- Small Darwin C program; modes selected from explicit argv, no shell, no arbitrary command execution. Emits bounded JSON using known synthetic strings or safe encoding. Inspects fd3/bootstrap/cwd/env/FDs and provides echo/exit/descendant/TERM-resistant modes needed above. Writes only explicit scratch paths if needed; no network or credential APIs. Include exact direct clang compile command in README, macOS15/arm64, no compilation now.

Validation permitted now: read-only diffs, Node --check for JS syntax, pure unit tests that do not require addon/execute native, static source consistency. Do NOT run a command that enters runner main or builds fixture/addon. C++/C correctness and native behavior remain unproved until parent dispositions. Do not npx/install/acquire tools.

Return: exact files/hashes, API assumptions, safe checks run, proposed exact future commands, unsupported cases or safety gaps. Independent Sol reviewer (not author) required before any native execution. Ask Packaging/Runtime for concrete unresolved ABI facts; do not introduce another approval ritual.
