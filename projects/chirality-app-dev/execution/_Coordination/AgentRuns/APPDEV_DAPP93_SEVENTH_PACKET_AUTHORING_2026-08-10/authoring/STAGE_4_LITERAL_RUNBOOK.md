# D-APP-93 seventh-lineage exact execution packet

Status: `PREPARED — NOT AUTHORIZED FOR EXECUTION`

Packet purpose: owner-operated reconstruction, isolated trace, first-signal observation, sealed replay, evidence return, rollback, and cleanup. This packet does not authorize any command. A fresh read-only verifier must accept the frozen packet and the owner must approve its exact hash before use.

## Immutable prerequisites

- Use one fresh interactive `/bin/zsh` owned and operated by the owner. Do not open a second terminal.
- Do not paste this document as a script. Perform one numbered step at a time, record its outcome in the evidence-return template, and continue only after its success gate is true.
- Any failed, unknown, prompted, mistargeted, or deviated gate routes immediately to P7-044. Never improvise, retry, substitute a PID, repeat a signal, Force Quit, or run a cleanup step whose prerequisites are unknown.
- Network access is prohibited. Credential values, memory dumps, and environment dumps are prohibited evidence.
- The approved LLDB script hash is `726e3dd53d85ca69ef11ddb0e1a6090790babb6a0d24e4199a4c7695b90f98c3`.
- Baseline hashes, in command order at P7-007 and P7-076: `850f7b00bd50af669d2cb6c1963c9b5f9b47f5a30badeda754752f3b896d335b`, `16ad6688abaebd0bb1bfe04921a7eb1d20601bf2f2af983153da3c734f44ad1f`, `5006bef6922295eb24c54f4a034f2d42929c71b80704b4fe03f8e7e5af36026a`, `1f14df17d407b18949d5a7195a786574fa8f03eda731dbe7b77f3e91685fba53`, `5c8fce2a3c0e2e7b55730ac673ccb07424dcae1e4bbbb408260b1090040c1a56`, `a6759be00c3bf2aaf9bd172657d723cf724bae33aa9a1941724cc173eaee5558`, `1918ae7dc10c12608a0d591db565f538a9ed91289e2b78eb728483d9c7cf91e9`, `f8b6d8c2d5c2d8f947e585dd5d99a85a9b207a7277de8ddcb2214cab92136be6`.
- Candidate hashes, in command order at P7-020: `bd1925a50ac18258bd03db0e475f9ac04d4fcbc46ab7a79b62a4090d92580982`, `2a0724f11d71a0682d2a9674c24fefd2d2f0137ed70e2190a84944d060a1126d`, `5eeac85fe98ba2c7b76ee98a93ea62fc89f05014b5e1ff381133160a096df491`, `970583be61674d8818046108d5129df90d06484d64c94ee904bbfedb2d0f2fc4`, `7e0ab20f14d634f9ce4be77fcfa55826cf4b0c022828acaee0709b8927123e2bc`, `7df8dc3f66d0fc070d3728854f6c5421bd2bff3ba1864bafbacec04485ebbf02`, `7996a9066e14188d859c499c243bf6ca2f864f7c2c8616a364c897d6ba658e15`, `cee808c108826e9987d5197bdc63c86d32ac1a428e54537fe4c3a3d79138a505`, `a710b7790ad92c4a64526478baa6e8f49c00a9070c7b84fb22529104f2a79199`, `27b3a0e36c4b5592a776057b71fa40ba391cb05170dacc91594e8736caafcc7f`, `8402b8b703f44bad6a4f8a74a8614a53ca5294f16c96b6c5b05f47a19ac2964e`, `0915e0b4645bfd194512ed2677ca72d4863884346726aa81265a638ce6826465`.
- Local archive hash: `ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28`.
- Expected package identities, in P7-032 order: `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`, `85eac95d186524180975ae99eefab0a0db8f5818913e3a063fbb90e6531ed16c`, `5306990501a6e68611a0f0c4967ec4a60f03fc36180b46b01be9846934e9df2d`, `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`, `e5efe64bb821be178e13ff40793203aabe2e04da2fdb8bb88fe1f6b236116a33`.

## Literal steps

### P7-001 — bind the sole owner terminal

```zsh
umask 077; export REPO=/Users/ryan/.codex/worktrees/55d3/chirality FRONTEND=/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend CANDIDATE=/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source ROOT=/private/tmp/chirality-dapp93-seventh-20260810 RETURN=/private/tmp/chirality-dapp93-seventh-return-20260810 ARCHIVE=/Users/ryan/Library/Caches/electron/9c4e224684594fb9a8cbda18d3e2b7bf0c3c023d1462402a4031f8b4cc25e621/electron-v43.2.0-darwin-arm64.zip SCRIPT=/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_SEVENTH_PACKET_AUTHORING_2026-08-10/packet/DAPP93_SEVENTH_LLDB_COMMAND_SCRIPT.txt
```

Gate: packet hash approved and this is a fresh interactive zsh.

### P7-002 — record bindings

```zsh
/usr/bin/printf '%s\n' $REPO $FRONTEND $CANDIDATE $ROOT $RETURN $ARCHIVE $SCRIPT
```

Gate: seven lines exactly equal P7-001.

### P7-003 — absence gate

```zsh
/bin/test ! -e $ROOT -a ! -e $RETURN -a ! -e $FRONTEND/node_modules -a ! -e $FRONTEND/dist -a ! -e $FRONTEND/dist-runtime-helper -a ! -e $FRONTEND/dist-electron -a ! -e $FRONTEND/dist-runtime -a ! -e $FRONTEND/.next
```

Gate: exit 0.

### P7-004 — create private trees

```zsh
/bin/mkdir -p $ROOT/evidence $ROOT/rollback/electron $ROOT/rollback/scripts $ROOT/rollback/tests $ROOT/electron-dist $ROOT/home/Library/Keychains $ROOT/user $RETURN
```

Gate: exit 0; owner-only umask remains active.

### P7-005 — host OS

```zsh
/usr/bin/sw_vers >$ROOT/evidence/host-sw-vers.txt 2>&1
```

Gate: exit 0 and nonempty file.

### P7-006 — kernel and architecture

```zsh
/usr/bin/uname -a >$ROOT/evidence/host-uname.txt 2>&1
```

Gate: exit 0 and nonempty file.

### P7-007 — baseline manifest

```zsh
/usr/bin/shasum -a 256 $FRONTEND/electron/cli-launcher.ts $FRONTEND/electron/main.ts $FRONTEND/electron/runtime-control-ipc.ts $FRONTEND/package.json $FRONTEND/package-lock.json $FRONTEND/scripts/build-electron.mjs $FRONTEND/src/__tests__/electron/cli-launcher.test.ts $FRONTEND/src/__tests__/electron/runtime-control-ipc.test.ts >$ROOT/evidence/baseline.sha256
```

Gate: eight hashes equal the prerequisite list.

### P7-008 — Electron rollback copies

```zsh
/bin/cp -p $FRONTEND/electron/cli-launcher.ts $FRONTEND/electron/main.ts $FRONTEND/electron/runtime-control-ipc.ts $ROOT/rollback/electron/
```

Gate: exit 0 and copied hashes equal baseline.

### P7-009 — manifest rollback copies

```zsh
/bin/cp -p $FRONTEND/package.json $FRONTEND/package-lock.json $ROOT/rollback/
```

Gate: exit 0 and copied hashes equal baseline.

### P7-010 — build-script rollback copy

```zsh
/bin/cp -p $FRONTEND/scripts/build-electron.mjs $ROOT/rollback/scripts/
```

Gate: exit 0 and copied hash equals baseline.

### P7-011 — test rollback copies

```zsh
/bin/cp -p $FRONTEND/src/__tests__/electron/cli-launcher.test.ts $FRONTEND/src/__tests__/electron/runtime-control-ipc.test.ts $ROOT/rollback/tests/
```

Gate: exit 0 and copied hashes equal baseline.

### P7-012 — destination directories

```zsh
/bin/mkdir -p $FRONTEND/electron $FRONTEND/scripts $FRONTEND/src/__tests__/electron
```

Gate: exit 0.

### P7-013 — helper builder config

```zsh
/bin/cp -p $CANDIDATE/electron-builder.runtime-helper.json $FRONTEND/electron-builder.runtime-helper.json
```

Gate: exit 0.

### P7-014 — candidate Electron sources

```zsh
/bin/cp -p $CANDIDATE/electron/cli-launcher.ts $CANDIDATE/electron/main.ts $CANDIDATE/electron/runtime-control-ipc.ts $CANDIDATE/electron/runtime-helper-entry.ts $CANDIDATE/electron/runtime-helper-path.ts $FRONTEND/electron/
```

Gate: exit 0.

### P7-015 — candidate package manifest

```zsh
/bin/cp -p $CANDIDATE/package.json $FRONTEND/package.json
```

Gate: exit 0.

### P7-016 — candidate build scripts

```zsh
/bin/cp -p $CANDIDATE/scripts/build-electron.mjs $CANDIDATE/scripts/embed-runtime-helper.mjs $FRONTEND/scripts/
```

Gate: exit 0.

### P7-017 — candidate launcher test

```zsh
/bin/cp -p $CANDIDATE/tests/cli-launcher.test.ts $FRONTEND/src/__tests__/electron/cli-launcher.test.ts
```

Gate: exit 0.

### P7-018 — candidate IPC test

```zsh
/bin/cp -p $CANDIDATE/tests/runtime-control-ipc.test.ts $FRONTEND/src/__tests__/electron/runtime-control-ipc.test.ts
```

Gate: exit 0.

### P7-019 — candidate packaging test

```zsh
/bin/cp -p $CANDIDATE/tests/runtime-helper-packaging.test.ts $FRONTEND/src/__tests__/electron/runtime-helper-packaging.test.ts
```

Gate: exit 0.

### P7-020 — candidate manifest

```zsh
/usr/bin/shasum -a 256 $FRONTEND/electron-builder.runtime-helper.json $FRONTEND/electron/cli-launcher.ts $FRONTEND/electron/main.ts $FRONTEND/electron/runtime-control-ipc.ts $FRONTEND/electron/runtime-helper-entry.ts $FRONTEND/electron/runtime-helper-path.ts $FRONTEND/package.json $FRONTEND/scripts/build-electron.mjs $FRONTEND/scripts/embed-runtime-helper.mjs $FRONTEND/src/__tests__/electron/cli-launcher.test.ts $FRONTEND/src/__tests__/electron/runtime-control-ipc.test.ts $FRONTEND/src/__tests__/electron/runtime-helper-packaging.test.ts >$ROOT/evidence/candidate.sha256
```

Gate: twelve hashes equal the prerequisite list.

### P7-021 — offline dependencies

```zsh
cd $FRONTEND && PATH=/Users/ryan/.local/share/mise/installs/node/24.18.0/bin:/usr/bin:/bin:/usr/sbin:/sbin /usr/bin/env npm ci --offline --ignore-scripts --no-audit --no-fund >$ROOT/evidence/npm-ci.txt 2>&1
```

Gate: exit 0; no network-attempt indication; lockfile unchanged.

### P7-022 — lockfile identity

```zsh
/usr/bin/shasum -a 256 $FRONTEND/package-lock.json >$ROOT/evidence/package-lock.sha256
```

Gate: hash equals `5c8fce2a3c0e2e7b55730ac673ccb07424dcae1e4bbbb408260b1090040c1a56`.

### P7-023 — dependency tree

```zsh
cd $FRONTEND && PATH=/Users/ryan/.local/share/mise/installs/node/24.18.0/bin:/usr/bin:/bin:/usr/sbin:/sbin /usr/bin/env npm ls --all --json >$ROOT/evidence/npm-tree.json
```

Gate: exit 0; valid nonempty JSON and expected repository-local dependencies.

### P7-024 — local archive identity

```zsh
/usr/bin/shasum -a 256 $ARCHIVE >$ROOT/evidence/electron-archive.sha256
```

Gate: hash equals the prerequisite archive hash.

### P7-025 — local archive copy

```zsh
/bin/cp -p $ARCHIVE $ROOT/electron-dist/electron-v43.2.0-darwin-arm64.zip
```

Gate: copied hash equals P7-024.

### P7-026 — two local-archive overlays

```zsh
cd $FRONTEND && DIST=$ROOT/electron-dist/electron-v43.2.0-darwin-arm64.zip /Users/ryan/.local/share/mise/installs/node/24.18.0/bin/node -e 'const fs=require(`fs`);for(const f of [`electron-builder.runtime-helper.json`,`package.json`]){const v=JSON.parse(fs.readFileSync(f,`utf8`));if(f.startsWith(`electron-builder`))v.electronDist=process.env.DIST;else v.build.electronDist=process.env.DIST;fs.writeFileSync(f,JSON.stringify(v,null,2)+`\n`)}'
```

Gate: exit 0; both JSON files parse and their sole intended archive fields equal `$ROOT/electron-dist/electron-v43.2.0-darwin-arm64.zip`.

### P7-027 — overlay manifest

```zsh
/usr/bin/shasum -a 256 $FRONTEND/electron-builder.runtime-helper.json $FRONTEND/package.json >$ROOT/evidence/overlay.sha256
```

Gate: exit 0; exactly two nonempty digest rows are retained for later validation.

### P7-028 — tests

```zsh
cd $FRONTEND && PATH=/Users/ryan/.local/share/mise/installs/node/24.18.0/bin:/usr/bin:/bin:/usr/sbin:/sbin /usr/bin/env npm test -- --run >$ROOT/evidence/tests.txt 2>&1
```

Gate: exit 0 and all selected tests pass.

### P7-029 — typecheck

```zsh
cd $FRONTEND && PATH=/Users/ryan/.local/share/mise/installs/node/24.18.0/bin:/usr/bin:/bin:/usr/sbin:/sbin /usr/bin/env npm run typecheck >$ROOT/evidence/typecheck.txt 2>&1
```

Gate: exit 0.

### P7-030 — build

```zsh
cd $FRONTEND && PATH=/Users/ryan/.local/share/mise/installs/node/24.18.0/bin:/usr/bin:/bin:/usr/sbin:/sbin /usr/bin/env npm run build >$ROOT/evidence/build.txt 2>&1
```

Gate: exit 0 and declared build trees exist.

### P7-031 — offline package

```zsh
cd $FRONTEND && CSC_IDENTITY_AUTO_DISCOVERY=false PATH=/Users/ryan/.local/share/mise/installs/node/24.18.0/bin:/usr/bin:/bin:/usr/sbin:/sbin /usr/bin/env npm run desktop:pack >$ROOT/evidence/package.txt 2>&1
```

Gate: exit 0; local archive is used; dependency and instruction-root checks pass; no network-attempt indication.

### P7-032 — package identities

```zsh
/usr/bin/shasum -a 256 '/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service' '/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Resources/app.asar' '/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Info.plist' '/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/MacOS/Chirality' '/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Resources/app.asar' >$ROOT/evidence/package-identity.sha256
```

Gate: five hashes equal the prerequisite package identities. These gates pin the two generated executables before either can run.

### P7-033 — helper plist

```zsh
/usr/bin/plutil -p '/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Info.plist' >$ROOT/evidence/helper-plist.txt
```

Gate: expected helper identifier, executable/display name, and `LSUIElement=true`.

### P7-034 — helper symlinks

```zsh
/usr/bin/find -H '/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Frameworks' -type l -print -exec /usr/bin/readlink {} \; >$ROOT/evidence/helper-symlinks.txt
```

Gate: exit 0 and all recorded targets are relative.

### P7-035 — pre-run owner default keychain

```zsh
/usr/bin/security default-keychain -d user >$ROOT/evidence/pre-owner-default.txt 2>$ROOT/evidence/pre-owner-default.stderr.txt
```

Gate: exit 0 and no credential value.

### P7-036 — pre-run owner search list

```zsh
/usr/bin/security list-keychains -d user >$ROOT/evidence/pre-owner-search.txt 2>$ROOT/evidence/pre-owner-search.stderr.txt
```

Gate: exit 0 and no credential value.

### P7-037 — disposable keychain

```zsh
/usr/bin/env -i PATH=/usr/bin:/bin:/usr/sbin:/sbin HOME=$ROOT/home /usr/bin/security create-keychain -p '' $ROOT/home/Library/Keychains/login.keychain-db >$ROOT/evidence/create-keychain.txt 2>$ROOT/evidence/create-keychain.stderr.txt
```

Gate: exit 0; file exists; no prompt or credential request.

### P7-038 — isolated default

```zsh
/usr/bin/env -i PATH=/usr/bin:/bin:/usr/sbin:/sbin HOME=$ROOT/home /usr/bin/security default-keychain -d user >$ROOT/evidence/isolated-default.txt 2>$ROOT/evidence/isolated-default.stderr.txt
```

Gate: sole line names the disposable keychain.

### P7-039 — isolated search list

```zsh
/usr/bin/env -i PATH=/usr/bin:/bin:/usr/sbin:/sbin HOME=$ROOT/home /usr/bin/security list-keychains -d user >$ROOT/evidence/isolated-search.txt 2>$ROOT/evidence/isolated-search.stderr.txt
```

Gate: exactly one line names the disposable keychain.

### P7-040 — owner shell PID

```zsh
/usr/bin/printf '%d\n' $$ >$ROOT/evidence/owner-shell.pid
```

Gate: positive PID; this shell remains active.

### P7-041 — helper readiness and GUI launch

```zsh
HOME=$ROOT/home CHIRALITY_USER_DATA=$ROOT/user CHIRALITY_SKIP_CLI_LAUNCHER=1 '/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service' --runtime-daemon >$ROOT/evidence/trace-helper.stdout.txt 2>$ROOT/evidence/trace-helper.stderr.txt & export TRACE_PID=$!; /usr/bin/printf '%d\n' $TRACE_PID >$ROOT/evidence/trace-helper.pid; /usr/bin/awk 'BEGIN{for(i=0;i<150;i++){if(system("/bin/test -S " ENVIRON["ROOT"] "/user/runtime/control.sock")==0)exit 0;system("/bin/sleep 0.1")}exit 1}'; HOME=$ROOT/home CHIRALITY_USER_DATA=$ROOT/user CHIRALITY_SKIP_CLI_LAUNCHER=1 '/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/MacOS/Chirality' >$ROOT/evidence/gui.stdout.txt 2>$ROOT/evidence/gui.stderr.txt & export GUI_PID=$!; /usr/bin/printf '%d\n' $GUI_PID >$ROOT/evidence/gui.pid; /bin/kill -0 $GUI_PID
```

Gate: helper and GUI hashes still equal P7-032; positive child PIDs; socket within 15 seconds; GUI live. Never relaunch or substitute a PID.

### P7-042 — trace parent binding

```zsh
/bin/ps -o ppid= -p $TRACE_PID | /usr/bin/tr -d ' ' >$ROOT/evidence/trace-helper.ppid
```

Gate: value exactly equals `owner-shell.pid`; target remains live.

### P7-043 — debugger script binding

```zsh
/usr/bin/shasum -a 256 $SCRIPT >$ROOT/evidence/lldb-script.sha256
```

Gate: hash equals `726e3dd53d85ca69ef11ddb0e1a6090790babb6a0d24e4199a4c7695b90f98c3`.

### P7-044 — universal STOP

```zsh
/usr/bin/printf 'STOPPED — NO FURTHER RUNTIME STEP\n' >>$ROOT/evidence/deviation.txt
```

Use on any failure, unknown, prompt, mismatch, unexpected breakpoint state, or deviation. Do not continue except to a separately enumerated cleanup/rollback step whose own prerequisites are certainly true.

### P7-045 — attach clock start

```zsh
/bin/date -u +%s >$ROOT/evidence/attach-start.epoch
```

Gate: positive epoch; target and script gates remain exact.

### P7-046 — exact attach in this PTY

```zsh
/usr/bin/xcrun lldb --batch -p $TRACE_PID -s $SCRIPT 2>&1 | /usr/bin/tee $ROOT/evidence/lldb-transcript.txt
```

Gate: LLDB shows the exact numeric PID; script loads; only enumerated breakpoint/backtrace actions occur; no prompt or credential/memory/environment inspection. Keep this PTY. The owner performs P7-047 in Activity Monitor while this command is active.

### P7-047 — owner first signal

In Activity Monitor, locate only the process whose numeric PID equals the value in `trace-helper.pid`, choose **Quit**, and confirm **Quit**. Never choose Force Quit.

Gate: exactly one Quit action on the bound PID; record timestamp and outcome.

### P7-048 — same-PTY interrupt

Press exactly one Control-C byte in the same active LLDB PTY.

Gate: the LLDB prompt returns within the 150-second absolute bound. Do not repeat.

### P7-049 — exact detach input

```text
process detach
```

Gate: LLDB reports detachment from the same PID.

### P7-050 — exact quit input

```text
quit
```

Gate: LLDB exits and the same owner shell regains the prompt.

### P7-051 — attach clock end

```zsh
/bin/date -u +%s >$ROOT/evidence/attach-end.epoch
```

Gate: positive epoch not earlier than start.

### P7-052 — elapsed bound

```zsh
/usr/bin/awk 'NR==FNR{s=$1;next}{d=$1-s;if(d<0||d>150)exit 1;print d}' $ROOT/evidence/attach-start.epoch $ROOT/evidence/attach-end.epoch >$ROOT/evidence/attach-elapsed-seconds.txt
```

Gate: integer 0 through 150. Never rerun the trace.

### P7-053 — traced child terminality

```zsh
wait $TRACE_PID; /usr/bin/printf '%d\n' $? >$ROOT/evidence/trace-helper.exit-status.txt
```

Gate: shell builtin `wait` addresses only `TRACE_PID`; no live traced child remains.

### P7-054 — trace socket teardown

```zsh
/bin/test ! -S $ROOT/user/runtime/control.sock
```

Gate: exit 0.

### P7-055 — sealed replay

```zsh
HOME=$ROOT/home CHIRALITY_USER_DATA=$ROOT/user CHIRALITY_SKIP_CLI_LAUNCHER=1 '/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service' --runtime-daemon >$ROOT/evidence/replay-helper.stdout.txt 2>$ROOT/evidence/replay-helper.stderr.txt & export REPLAY_PID=$!; /usr/bin/printf '%d\n' $REPLAY_PID >$ROOT/evidence/replay-helper.pid
```

Gate: positive new PID; executable hash still equals P7-032; no debugger attached.

### P7-056 — replay parent binding

```zsh
/bin/ps -o ppid= -p $REPLAY_PID | /usr/bin/tr -d ' ' >$ROOT/evidence/replay-helper.ppid
```

Gate: value equals owner shell PID and differs from traced PID.

### P7-057 — replay readiness

```zsh
/usr/bin/awk 'BEGIN{for(i=0;i<150;i++){if(system("/bin/test -S " ENVIRON["ROOT"] "/user/runtime/control.sock")==0)exit 0;system("/bin/sleep 0.1")}exit 1}'
```

Gate: socket appears within 15 seconds.

### P7-058 — replay signal

```zsh
/bin/kill -TERM $REPLAY_PID
```

Gate: immediate parent binding has been rechecked; exit 0; exactly one TERM. Never repeat or force.

### P7-059 — replay terminality

```zsh
wait $REPLAY_PID; /usr/bin/printf '%d\n' $? >$ROOT/evidence/replay-helper.exit-status.txt
```

Gate: exact child reaches terminal state within the owner-observed bound. If not, STOP and retain state.

### P7-060 — socket and GUI terminality

```zsh
/bin/test ! -S $ROOT/user/runtime/control.sock && /bin/kill -TERM $GUI_PID && { wait $GUI_PID; GUI_RC=$?; /usr/bin/printf '%d\n' $GUI_RC >$ROOT/evidence/gui.exit-status.txt; }
```

Gate: socket absent; one TERM to exact GUI child; shell builtin `wait` records terminal status.

### P7-061 — post-run owner default keychain

```zsh
/usr/bin/security default-keychain -d user >$ROOT/evidence/post-owner-default.txt 2>$ROOT/evidence/post-owner-default.stderr.txt
```

Gate: all diagnostic children terminal; exit 0; no credential value.

### P7-062 — post-run owner search list

```zsh
/usr/bin/security list-keychains -d user >$ROOT/evidence/post-owner-search.txt 2>$ROOT/evidence/post-owner-search.stderr.txt
```

Gate: exit 0 and no credential value.

### P7-063 — default-keychain no-drift proof

```zsh
/usr/bin/cmp -s $ROOT/evidence/pre-owner-default.txt $ROOT/evidence/post-owner-default.txt
```

Gate: exit 0.

### P7-064 — search-list no-drift proof

```zsh
/usr/bin/cmp -s $ROOT/evidence/pre-owner-search.txt $ROOT/evidence/post-owner-search.txt
```

Gate: exit 0.

### P7-065 — source evidence manifest

```zsh
cd $ROOT/evidence && /usr/bin/find . -type f -print0 | /usr/bin/sort -z | /usr/bin/xargs -0 /usr/bin/shasum -a 256 >$RETURN/evidence-manifest.sha256
```

Gate: all children terminal; manual credential screen passed; each ordinary safe file appears once.

### P7-066 — bounded evidence copy

```zsh
/usr/bin/ditto $ROOT/evidence $RETURN/evidence
```

Gate: exit 0 and returned file count matches manifest.

### P7-067 — independent return hash

```zsh
cd $RETURN/evidence && /usr/bin/find . -type f -print0 | /usr/bin/sort -z | /usr/bin/xargs -0 /usr/bin/shasum -a 256 >$RETURN/returned-evidence.sha256
```

Gate: rows equal `evidence-manifest.sha256`.

### P7-068 — delete disposable keychain

```zsh
/usr/bin/env -i PATH=/usr/bin:/bin:/usr/sbin:/sbin HOME=$ROOT/home /usr/bin/security delete-keychain $ROOT/home/Library/Keychains/login.keychain-db >$RETURN/delete-isolated-keychain.txt 2>$RETURN/delete-isolated-keychain.stderr.txt
```

Gate: returned evidence exact; owner state exact; children terminal; exit 0.

### P7-069 — keychain absence

```zsh
/bin/test ! -e $ROOT/home/Library/Keychains/login.keychain-db
```

Gate: exit 0.

### P7-070 — restore Electron sources

```zsh
/bin/cp -p $ROOT/rollback/electron/cli-launcher.ts $ROOT/rollback/electron/main.ts $ROOT/rollback/electron/runtime-control-ipc.ts $FRONTEND/electron/
```

Gate: no live diagnostic child; exit 0.

### P7-071 — restore package manifests

```zsh
/bin/cp -p $ROOT/rollback/package.json $ROOT/rollback/package-lock.json $FRONTEND/
```

Gate: exit 0.

### P7-072 — restore build script

```zsh
/bin/cp -p $ROOT/rollback/scripts/build-electron.mjs $FRONTEND/scripts/
```

Gate: exit 0.

### P7-073 — restore tests

```zsh
/bin/cp -p $ROOT/rollback/tests/cli-launcher.test.ts $FRONTEND/src/__tests__/electron/cli-launcher.test.ts; /bin/cp -p $ROOT/rollback/tests/runtime-control-ipc.test.ts $FRONTEND/src/__tests__/electron/runtime-control-ipc.test.ts
```

Gate: both copies exit 0.

### P7-074 — remove five candidate additions

```zsh
/bin/rm -f $FRONTEND/electron-builder.runtime-helper.json $FRONTEND/electron/runtime-helper-entry.ts $FRONTEND/electron/runtime-helper-path.ts $FRONTEND/scripts/embed-runtime-helper.mjs $FRONTEND/src/__tests__/electron/runtime-helper-packaging.test.ts
```

Gate: exit 0 and exactly those five paths are absent.

### P7-075 — remove six derivatives

```zsh
/bin/rm -rf $FRONTEND/node_modules $FRONTEND/dist $FRONTEND/dist-runtime-helper $FRONTEND/dist-electron $FRONTEND/dist-runtime $FRONTEND/.next
```

Gate: returned evidence verified and children terminal; exit 0; exact six paths absent.

### P7-076 — restored baseline manifest

```zsh
/usr/bin/shasum -a 256 $FRONTEND/electron/cli-launcher.ts $FRONTEND/electron/main.ts $FRONTEND/electron/runtime-control-ipc.ts $FRONTEND/package.json $FRONTEND/package-lock.json $FRONTEND/scripts/build-electron.mjs $FRONTEND/src/__tests__/electron/cli-launcher.test.ts $FRONTEND/src/__tests__/electron/runtime-control-ipc.test.ts >$RETURN/post-rollback.sha256
```

Gate: eight hashes equal P7-007.

### P7-077 — frontend Git-status proof

```zsh
/usr/bin/git -C $REPO status --short -- projects/chirality-app-dev/frontend >$RETURN/frontend-git-status.txt
```

Gate: exit 0 and file has zero bytes.

### P7-078 — remove disposable root

```zsh
/bin/rm -rf $ROOT
```

Gate: return verified; disposable keychain absent; children terminal; frontend restored. Never run if any fact is unknown.

### P7-079 — root absence

```zsh
/bin/test ! -e $ROOT
```

Gate: exit 0.

### P7-080 — terminal status without overclaim

```zsh
/usr/bin/printf 'EXECUTION_COMPLETE — EVIDENCE RETURNED — CLEANUP COMPLETE — NO CAUSAL OR ACCEPTANCE CLAIM\n' >$RETURN/terminal-status.txt
```

Gate: exact line written and returned evidence remains immutable pending separately governed ingestion.

## Epistemic terminal boundary

Even a fully successful P7-080 proves only that the owner reported completion and that the declared evidence was returned. It does not establish cause, remedy, acceptance, release, reliance, lifecycle closure, or any product claim. Those require separate ingestion, validation, causal-matrix authorship, and fresh post-execution verification.
