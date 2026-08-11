# Stage 3 — literal owner-operated runbook

Status: `COMPLETE TEXT — EXECUTION AUTHORITY WITHHELD`

This is exact future command text, not authority to run it. The complete four-file
packet must be assembled, freshly verified read-only, frozen, and approved by the
owner at its exact freeze hash before any step. Approval covers no alternate
command, spelling, path, PID, retry, recovery, or deviation.

Use one fresh interactive zsh in the owner's macOS GUI session for every
`owner-terminal` step. Do not open a second terminal. Record each step's UTC time,
exit status, stdout/stderr location, observed value, and deviation in the evidence
return template. On any failed prerequisite or gate, do not run the next
operational step: run `P93-044` once, retain state, and run only later evidence or
cleanup steps whose own safety prerequisites are affirmatively satisfied.

## 1. Fixed identities and safety rules

- Approved baseline hashes, in command order: `850f7b00bd50af669d2cb6c1963c9b5f9b47f5a30badeda754752f3b896d335b`, `16ad6688abaebd0bb1bfe04921a7eb1d20601bf2f2af983153da3c734f44ad1f`, `5006bef6922295eb24c54f4a034f2d42929c71b80704b4fe03f8e7e5af36026a`, `1f14df17d407b18949d5a7195a786574fa8f03eda731dbe7b77f3e91685fba53`, `5c8fce2a3c0e2e7b55730ac673ccb07424dcae1e4bbbb408260b1090040c1a56`, `a6759be00c3bf2aaf9bd172657d723cf724bae33aa9a1941724cc173eaee5558`, `1918ae7dc10c12608a0d591db565f538a9ed91289e2b78eb728483d9c7cf91e9`, `f8b6d8c2d5c2d8f947e585dd5d99a85a9b207a7277de8ddcb2214cab92136be6`.
- Approved candidate hashes, in command order: `bd1925a50ac18258bd03db0e475f9ac04d4fcbc46ab7a79b62a4090d92580982`, `2a0724f11d71a0682d2a9674c24fefd2d2f0137ed70e2190a84944d060a1126d`, `5eeac85fe98ba2c7b76ee98a93ea62fc89f05014b5e1ff381133160a096df491`, `970583be61674d8818046108d5129df90d06484d64c94ee904bbfedb2d0f2fc4`, `7e0ab20f14d634f9ce4e77fcfa55826cf4b0c022828acaee0709b8927123e2bc`, `7df8dc3f66d0fc070d3728854f6c5421bd2bff3ba1864bafbacec04485ebbf02`, `7996a9066e14188d859c499c243bf6ca2f864f7c2c8616a364c897d6ba658e15`, `cee808c108826e9987d5197bdc63c86d32ac1a428e54537fe4c3a3d79138a505`, `a710b7790ad92c4a64526478baa6e8f49c00a9070c7b84fb22529104f2a79199`, `27b3a0e36c4b5592a776057b71fa40ba391cb05170dacc91594e8736caafcc7f`, `8402b8b703f44bad6a4f8a74a8614a53ca5294f16c96b6c5b05f47a19ac2964e`, `0915e0b4645bfd194512ed2677ca72d4863884346726aa81265a638ce6826465`.
- Approved local Electron archive SHA-256: `ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28`.
- Expected overlay hashes, helper config then package manifest: `f7db9ac4de3669e83ffdd63f0b63e9d55e1db2e8402cdd6a23bf5b2f70874679`, `93551038bb345f645fc4fe79e0523d7721f193542130844a541e2ae9c13c7a34`.
- The LLDB-script expected hash is the exact value in `PACKET_INDEX.md`.
- No network, process census, PID search, explicit keychain unlock, owner-keychain write, password-store bypass, credential access, memory/environment dump, signing/notarization/distribution, product-byte workaround, force signal, generic repair, Git mutation, Task Management, lifecycle, receipt, reliance, or foreign-loop action is permitted.

## 2. Preflight and fixed paths

### P93-001 — owner-terminal — `OWNER_OPERATED_NEW`

Prerequisite: fresh interactive zsh and exact frozen-packet hash approval.

```zsh
umask 077; export REPO=/Users/ryan/.codex/worktrees/55d3/chirality FRONTEND=/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend CANDIDATE=/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source ROOT=/private/tmp/chirality-dapp93-sixth-20260810 RETURN=/private/tmp/chirality-dapp93-sixth-return-20260810 ARCHIVE=/Users/ryan/Library/Caches/electron/9c4e224684594fb9a8cbda18d3e2b7bf0c3c023d1462402a4031f8b4cc25e621/electron-v43.2.0-darwin-arm64.zip SCRIPT=/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_SIXTH_PACKET_AUTHORING_2026-08-10/packet/DAPP93_SIXTH_LLDB_COMMAND_SCRIPT.txt
```

Gate/output: variables exist in this owner shell. Failure: `P93-044`.
Cleanup: none.

### P93-002 — owner-terminal — `OWNER_OPERATED_NEW`

Prerequisite: `P93-001`.

```zsh
/usr/bin/printf '%s\n' $REPO $FRONTEND $CANDIDATE $ROOT $RETURN $ARCHIVE $SCRIPT
```

Gate/output: exactly seven lines equal the frozen values. Failure: `P93-044`.
Cleanup: none.

### P93-003 — owner-terminal — `OWNER_OPERATED_NEW`

Prerequisite: `P93-002`.

```zsh
/bin/test ! -e $ROOT -a ! -e $RETURN -a ! -e $FRONTEND/node_modules -a ! -e $FRONTEND/dist -a ! -e $FRONTEND/dist-runtime-helper -a ! -e $FRONTEND/dist-electron -a ! -e $FRONTEND/dist-runtime -a ! -e $FRONTEND/.next
```

Gate/output: exit 0. Failure: `P93-044`; do not remove pre-existing state.

### P93-004 — owner-terminal — `OWNER_OPERATED_NEW`

Prerequisite: `P93-003` exit 0.

```zsh
/bin/mkdir -p $ROOT/evidence $ROOT/rollback/electron $ROOT/rollback/scripts $ROOT/rollback/tests $ROOT/electron-dist $ROOT/home/Library/Keychains $ROOT/user $RETURN
```

Gate/output: exact directories exist under owner-only umask. Failure:
`P93-044`; retain until ruled cleanup.

### P93-005 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/usr/bin/sw_vers >$ROOT/evidence/host-sw-vers.txt 2>&1
```

Prerequisite: `P93-004`. Gate: exit 0, nonempty capture. Failure: `P93-044`;
retain evidence.

### P93-006 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/usr/bin/uname -a >$ROOT/evidence/host-uname.txt 2>&1
```

Prerequisite: `P93-005`. Gate: exit 0, nonempty capture. Failure: `P93-044`;
retain evidence.

## 3. Fresh reconstruction

### P93-007 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/usr/bin/shasum -a 256 $FRONTEND/electron/cli-launcher.ts $FRONTEND/electron/main.ts $FRONTEND/electron/runtime-control-ipc.ts $FRONTEND/package.json $FRONTEND/package-lock.json $FRONTEND/scripts/build-electron.mjs $FRONTEND/src/__tests__/electron/cli-launcher.test.ts $FRONTEND/src/__tests__/electron/runtime-control-ipc.test.ts >$ROOT/evidence/baseline.sha256
```

Prerequisite: `P93-006`. Gate: eight lines equal the baseline hashes in §1.
Failure: `P93-044`; do not mutate frontend.

### P93-008 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/bin/cp -p $FRONTEND/electron/cli-launcher.ts $FRONTEND/electron/main.ts $FRONTEND/electron/runtime-control-ipc.ts $ROOT/rollback/electron/
```

Prerequisite: `P93-007` exact. Gate: three copies hash-equal baseline. Failure:
`P93-044`; `P93-070` is the later restoration.

### P93-009 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/bin/cp -p $FRONTEND/package.json $FRONTEND/package-lock.json $ROOT/rollback/
```

Prerequisite: `P93-008`. Gate: two copies hash-equal baseline. Failure:
`P93-044`; `P93-071` restores.

### P93-010 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/bin/cp -p $FRONTEND/scripts/build-electron.mjs $ROOT/rollback/scripts/
```

Prerequisite: `P93-009`. Gate: copied hash equals baseline. Failure:
`P93-044`; `P93-072` restores.

### P93-011 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/bin/cp -p $FRONTEND/src/__tests__/electron/cli-launcher.test.ts $FRONTEND/src/__tests__/electron/runtime-control-ipc.test.ts $ROOT/rollback/tests/
```

Prerequisite: `P93-010`. Gate: two copied hashes equal baseline. Failure:
`P93-044`; `P93-073` restores.

### P93-012 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/bin/mkdir -p $FRONTEND/electron $FRONTEND/scripts $FRONTEND/src/__tests__/electron
```

Prerequisite: `P93-011`. Gate: exit 0. Failure: `P93-044`; baseline
directories remain.

### P93-013 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/bin/cp -p $CANDIDATE/electron-builder.runtime-helper.json $FRONTEND/electron-builder.runtime-helper.json
```

Prerequisite: `P93-012`. Gate: hash equals the first candidate hash. Failure:
`P93-044`; `P93-074` removes this candidate-only file.

### P93-014 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/bin/cp -p $CANDIDATE/electron/cli-launcher.ts $CANDIDATE/electron/main.ts $CANDIDATE/electron/runtime-control-ipc.ts $CANDIDATE/electron/runtime-helper-entry.ts $CANDIDATE/electron/runtime-helper-path.ts $FRONTEND/electron/
```

Prerequisite: `P93-013`. Gate: exit 0. Failure: `P93-044`; later restore the
three baseline files and remove the two additions.

### P93-015 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/bin/cp -p $CANDIDATE/package.json $FRONTEND/package.json
```

Prerequisite: `P93-014`. Gate: exit 0. Failure: `P93-044`; `P93-071` restores.

### P93-016 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/bin/cp -p $CANDIDATE/scripts/build-electron.mjs $CANDIDATE/scripts/embed-runtime-helper.mjs $FRONTEND/scripts/
```

Prerequisite: `P93-015`. Gate: exit 0. Failure: `P93-044`; later restore the
baseline script and remove the addition.

### P93-017 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/bin/cp -p $CANDIDATE/tests/cli-launcher.test.ts $FRONTEND/src/__tests__/electron/cli-launcher.test.ts
```

Prerequisite: `P93-016`. Gate: exit 0. Failure: `P93-044`; `P93-073` restores.

### P93-018 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/bin/cp -p $CANDIDATE/tests/runtime-control-ipc.test.ts $FRONTEND/src/__tests__/electron/runtime-control-ipc.test.ts
```

Prerequisite: `P93-017`. Gate: exit 0. Failure: `P93-044`; `P93-073` restores.

### P93-019 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/bin/cp -p $CANDIDATE/tests/runtime-helper-packaging.test.ts $FRONTEND/src/__tests__/electron/runtime-helper-packaging.test.ts
```

Prerequisite: `P93-018`. Gate: exit 0. Failure: `P93-044`; `P93-074` removes.

### P93-020 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/usr/bin/shasum -a 256 $FRONTEND/electron-builder.runtime-helper.json $FRONTEND/electron/cli-launcher.ts $FRONTEND/electron/main.ts $FRONTEND/electron/runtime-control-ipc.ts $FRONTEND/electron/runtime-helper-entry.ts $FRONTEND/electron/runtime-helper-path.ts $FRONTEND/package.json $FRONTEND/scripts/build-electron.mjs $FRONTEND/scripts/embed-runtime-helper.mjs $FRONTEND/src/__tests__/electron/cli-launcher.test.ts $FRONTEND/src/__tests__/electron/runtime-control-ipc.test.ts $FRONTEND/src/__tests__/electron/runtime-helper-packaging.test.ts >$ROOT/evidence/candidate.sha256
```

Prerequisite: `P93-019`. Gate: twelve hashes exactly equal §1 in order.
Failure: `P93-044`; do not continue to dependencies.

## 4. Offline dependencies

### P93-021 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
cd $FRONTEND && /usr/bin/env npm ci --offline --ignore-scripts --no-audit --no-fund >$ROOT/evidence/npm-ci.txt 2>&1
```

Prerequisite: `P93-020` exact and local dependencies available. Gate: exit 0,
no download/network-attempt indicator, lockfile unchanged. Failure: `P93-044`;
retain output and later remove only the exact dependency root when safe.

### P93-022 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/usr/bin/shasum -a 256 $FRONTEND/package-lock.json >$ROOT/evidence/package-lock.sha256
```

Prerequisite: `P93-021`. Gate: hash equals the §1 lockfile hash. Failure:
`P93-044`; restore baseline defensively during rollback.

### P93-023 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
cd $FRONTEND && /usr/bin/env npm ls --all --json >$ROOT/evidence/npm-tree.json
```

Prerequisite: `P93-022`. Gate: exit 0 and valid nonempty JSON with the accepted
repository-local dependency projection. Failure: `P93-044`; retain evidence.

## 5. Local archive binding

### P93-024 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/usr/bin/shasum -a 256 $ARCHIVE >$ROOT/evidence/electron-archive.sha256
```

Prerequisite: `P93-023`. Gate: equals the archive hash in §1. Failure:
`P93-044`; do not copy or package.

### P93-025 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/bin/cp -p $ARCHIVE $ROOT/electron-dist/electron-v43.2.0-darwin-arm64.zip
```

Prerequisite: `P93-024` exact. Gate: exit 0 and copied hash equal. Failure:
`P93-044`; removal occurs only with safe root cleanup.

### P93-026 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
cd $FRONTEND && DIST=$ROOT/electron-dist/electron-v43.2.0-darwin-arm64.zip /usr/bin/env node -e 'const fs=require(`fs`);for(const f of [`electron-builder.runtime-helper.json`,`package.json`]){const v=JSON.parse(fs.readFileSync(f,`utf8`));if(f.startsWith(`electron-builder`))v.electronDist=process.env.DIST;else v.build.electronDist=process.env.DIST;fs.writeFileSync(f,JSON.stringify(v,null,2)+`\n`)}'
```

Prerequisite: `P93-025` and exact pre-overlay hashes. Gate: exit 0 and only two
JSON files changed. Failure: `P93-044`; rollback exact files.

### P93-027 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/usr/bin/shasum -a 256 $FRONTEND/electron-builder.runtime-helper.json $FRONTEND/package.json >$ROOT/evidence/overlay.sha256
```

Prerequisite: `P93-026`. Gate: the two hashes equal the §1 overlay hashes in
order. Failure: `P93-044`; rollback through exact cleanup rows.

## 6. Static validation

### P93-028 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
cd $FRONTEND && /usr/bin/env npm test -- --run >$ROOT/evidence/tests.txt 2>&1
```

Prerequisite: `P93-027` exact. Gate: exit 0 and selected tests pass. Failure:
`P93-044`; retain capture.

### P93-029 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
cd $FRONTEND && /usr/bin/env npm run typecheck >$ROOT/evidence/typecheck.txt 2>&1
```

Prerequisite: `P93-028`. Gate: exit 0. Failure: `P93-044`; retain capture.

## 7. Offline package construction

### P93-030 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
cd $FRONTEND && /usr/bin/env npm run build >$ROOT/evidence/build.txt 2>&1
```

Prerequisite: `P93-029`. Gate: exit 0 with `.next`, `dist-electron`, and
`dist-runtime`. Failure: `P93-044`; later remove only exact outputs.

### P93-031 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
cd $FRONTEND && CSC_IDENTITY_AUTO_DISCOVERY=false /usr/bin/env npm run desktop:pack >$ROOT/evidence/package.txt 2>&1
```

Prerequisite: `P93-030`, exact overlay/archive, network prohibited. Gate: exit
0; local archive used for both packages; boundary checks pass; no network
indicator. Failure: `P93-044`; never launch.

## 8. Package identity and topology

### P93-032 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/usr/bin/shasum -a 256 '/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service' '/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Resources/app.asar' '/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Info.plist' '/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/MacOS/Chirality' '/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Resources/app.asar' >$ROOT/evidence/package-identity.sha256
```

Prerequisite: `P93-031`. Gate: exit 0, five hashes, helper executable equals
approved Electron executable identity. Failure: `P93-044`; retain packages.

### P93-033 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/usr/bin/plutil -p '/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Info.plist' >$ROOT/evidence/helper-plist.txt
```

Prerequisite: `P93-032`. Gate: exact helper bundle identifier, executable and
display name, and background-only posture. Failure: `P93-044`; retain.

### P93-034 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/usr/bin/find -H '/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Frameworks' -type l -print -exec /bin/readlink {} \; >$ROOT/evidence/helper-symlinks.txt
```

Prerequisite: `P93-033`. Gate: exit 0; all targets relative; no unexpected
absolute target. Failure: `P93-044`; retain.

## 9. Isolated sealed-HOME login keychain

### P93-035 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/usr/bin/security default-keychain -d user >$ROOT/evidence/pre-owner-default.txt 2>$ROOT/evidence/pre-owner-default.stderr.txt
```

Prerequisite: `P93-034`. Gate: exit 0 and no credential value. Failure:
`P93-044`; retain for postcheck.

### P93-036 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/usr/bin/security list-keychains -d user >$ROOT/evidence/pre-owner-search.txt 2>$ROOT/evidence/pre-owner-search.stderr.txt
```

Prerequisite: `P93-035`. Gate: exit 0 and no credential value. Failure:
`P93-044`; retain for postcheck.

### P93-037 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/usr/bin/env -i PATH=/usr/bin:/bin:/usr/sbin:/sbin HOME=$ROOT/home /usr/bin/security create-keychain -p '' $ROOT/home/Library/Keychains/login.keychain-db >$ROOT/evidence/create-keychain.txt 2>$ROOT/evidence/create-keychain.stderr.txt
```

Prerequisite: `P93-036` and absent disposable path. Gate: exit 0; file exists;
no prompt or credential request. No explicit unlock is permitted. Failure:
`P93-044`; retain root until owner postcheck and ruled cleanup.

### P93-038 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/usr/bin/env -i PATH=/usr/bin:/bin:/usr/sbin:/sbin HOME=$ROOT/home /usr/bin/security default-keychain -d user >$ROOT/evidence/isolated-default.txt 2>$ROOT/evidence/isolated-default.stderr.txt
```

Prerequisite: `P93-037`. Gate: exit 0 and sole line names exactly
`$ROOT/home/Library/Keychains/login.keychain-db`. Failure: `P93-044`; do not
launch.

### P93-039 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/usr/bin/env -i PATH=/usr/bin:/bin:/usr/sbin:/sbin HOME=$ROOT/home /usr/bin/security list-keychains -d user >$ROOT/evidence/isolated-search.txt 2>$ROOT/evidence/isolated-search.stderr.txt
```

Prerequisite: `P93-038` exact. Gate: exit 0 and exactly one line naming the
same disposable keychain. Failure: `P93-044`; do not launch.

## 10. Owner-shell launch

### P93-040 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/usr/bin/printf '%d\n' $$ >$ROOT/evidence/owner-shell.pid
```

Prerequisite: `P93-039` exact. Gate: positive numeric PID; same shell stays
active. Failure: `P93-044`.

### P93-041 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
HOME=$ROOT/home CHIRALITY_USER_DATA=$ROOT/user CHIRALITY_SKIP_CLI_LAUNCHER=1 '/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service' --runtime-daemon >$ROOT/evidence/trace-helper.stdout.txt 2>$ROOT/evidence/trace-helper.stderr.txt & export TRACE_PID=$!; /usr/bin/printf '%d\n' $TRACE_PID >$ROOT/evidence/trace-helper.pid; /usr/bin/awk 'BEGIN{for(i=0;i<150;i++){if(system("/bin/test -S " ENVIRON["ROOT"] "/user/runtime/control.sock")==0)exit 0;system("/bin/sleep 0.1")}exit 1}'; HOME=$ROOT/home CHIRALITY_USER_DATA=$ROOT/user CHIRALITY_SKIP_CLI_LAUNCHER=1 '/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/MacOS/Chirality' >$ROOT/evidence/gui.stdout.txt 2>$ROOT/evidence/gui.stderr.txt & export GUI_PID=$!; /usr/bin/printf '%d\n' $GUI_PID >$ROOT/evidence/gui.pid; /bin/kill -0 $GUI_PID
```

Prerequisite: `P93-040`, exact package/hash/keychain gates, no prompt. Gate:
two positive PIDs; socket within 15 seconds; GUI live; owner shell remains.
Failure: `P93-044`; no replacement PID or relaunch.

## 11. Direct-child and script binding

### P93-042 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/bin/ps -o ppid= -p $TRACE_PID | /usr/bin/tr -d ' ' >$ROOT/evidence/trace-helper.ppid
```

Prerequisite: `P93-041` in same shell. Gate: value equals `owner-shell.pid`;
exact PID live and not reused. Failure: `P93-044`; no PID search.

### P93-043 — owner-terminal — `OWNER_OPERATED_PRESERVED_FENCE`

```zsh
/usr/bin/shasum -a 256 $SCRIPT >$ROOT/evidence/lldb-script.sha256
```

Prerequisite: `P93-042` exact. Gate: hash equals the script hash in packet
index and the fresh verifier accepted its enumerated capture semantics.
Failure: `P93-044`; do not attach.

## 12. Universal stop/deviation

### P93-044 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/usr/bin/printf 'STOPPED — NO FURTHER RUNTIME STEP\n' >>$ROOT/evidence/deviation.txt
```

Prerequisite: any failed operational gate or deviation. Gate: exact line
appended once; no alternate command, PID, retry, or recovery. Return the
blocker. Retain all state until process terminality and owner-state safety are
known. Only separately enumerated safe evidence/cleanup rows may follow.

## 13. Bounded debugger sequence

### P93-045 — owner-terminal — `OWNER_OPERATED_PRESERVED_FENCE`

```zsh
/bin/date -u +%s >$ROOT/evidence/attach-start.epoch
```

Prerequisite: `P93-043` exact; target direct child and live; no deviation.
Gate: positive epoch. Failure: `P93-044`.

### P93-046 — owner-terminal — `OWNER_OPERATED_PRESERVED_FENCE`

```zsh
/usr/bin/xcrun lldb --batch -p $TRACE_PID -s $SCRIPT 2>&1 | /usr/bin/tee $ROOT/evidence/lldb-transcript.txt
```

Prerequisite: `P93-045`; exact target remains live/direct child; no privilege,
entitlement, or credential prompt. Gate: LLDB shows exact PID, script loads,
and capture is limited to enumerated breakpoints/backtraces. Failure:
`P93-044`; send no signal; use the exact same-PTY interrupt/detach/quit only
when applicable to leave the debugger safely.

### P93-047 — owner-gui — `OWNER_ATTESTATION`

Exact action: in Activity Monitor, locate only the process whose numeric PID
equals `trace-helper.pid`, choose **Quit**, and confirm **Quit** — never Force
Quit.

Prerequisite: `P93-046` attached to exact PID and target identity visible.
Gate: exactly one Quit targets that PID; owner records UTC time and outcome;
trace reacts. Failure: `P93-044`; no repeated signal.

### P93-048 — owner-debugger-input — `OWNER_OPERATED_PRESERVED_FENCE`

Exact input: press `Control-C` once in the same existing LLDB PTY.

Prerequisite: `P93-047`, before 150 seconds. Gate: interrupt byte is present in
raw transcript and LLDB prompt returns. Failure: `P93-044`; no second input.

### P93-049 — owner-debugger-input — `OWNER_OPERATED_PRESERVED_FENCE`

Exact bytes:

```text
process detach
```

followed by one newline. Prerequisite: `P93-048` prompt. Gate: LLDB reports
detach from the same PID. Failure: `P93-044`; no alternate detach.

### P93-050 — owner-debugger-input — `OWNER_OPERATED_PRESERVED_FENCE`

Exact bytes:

```text
quit
```

followed by one newline. Prerequisite: `P93-049`. Gate: debugger exits and
owner shell prompt returns. Failure: `P93-044`; no further debugger input.

### P93-051 — owner-terminal — `OWNER_OPERATED_PRESERVED_FENCE`

```zsh
/bin/date -u +%s >$ROOT/evidence/attach-end.epoch
```

Prerequisite: `P93-046` pipeline returned after `P93-050`. Gate: positive
epoch not earlier than start. Failure: `P93-044`.

### P93-052 — owner-terminal — `OWNER_OPERATED_PRESERVED_FENCE`

```zsh
/usr/bin/awk 'NR==FNR{s=$1;next}{d=$1-s;if(d<0||d>150)exit 1;print d}' $ROOT/evidence/attach-start.epoch $ROOT/evidence/attach-end.epoch >$ROOT/evidence/attach-elapsed-seconds.txt
```

Prerequisite: `P93-051`. Gate: exit 0 and integer 0–150. Failure: `P93-044`;
retain all state and do not rerun.

## 14. Trace return

### P93-053 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/bin/wait $TRACE_PID; /usr/bin/printf '%d\n' $? >$ROOT/evidence/trace-helper.exit-status.txt
```

Prerequisite: debugger detached/quit; exact PID is the recorded shell child or
has exited. Gate: wait exact PID once, status recorded, no live exact child.
Failure: `P93-044`; no replacement PID.

### P93-054 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/bin/test ! -S $ROOT/user/runtime/control.sock
```

Prerequisite: `P93-053`. Gate: exit 0. Failure: `P93-044`; retain user data.

## 15. Sealed uninstrumented replay

### P93-055 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
HOME=$ROOT/home CHIRALITY_USER_DATA=$ROOT/user CHIRALITY_SKIP_CLI_LAUNCHER=1 '/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service' --runtime-daemon >$ROOT/evidence/replay-helper.stdout.txt 2>$ROOT/evidence/replay-helper.stderr.txt & export REPLAY_PID=$!; /usr/bin/printf '%d\n' $REPLAY_PID >$ROOT/evidence/replay-helper.pid
```

Prerequisite: `P93-054`, retained trace, unchanged keychain/package hashes.
Gate: positive new PID and no debugger attached. Failure: `P93-044`; no retry.

### P93-056 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/bin/ps -o ppid= -p $REPLAY_PID | /usr/bin/tr -d ' ' >$ROOT/evidence/replay-helper.ppid
```

Prerequisite: `P93-055` same shell. Gate: PPID equals owner shell and replay
PID differs from traced PID. Failure: `P93-044`; no search.

### P93-057 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/usr/bin/awk 'BEGIN{for(i=0;i<150;i++){if(system("/bin/test -S " ENVIRON["ROOT"] "/user/runtime/control.sock")==0)exit 0;system("/bin/sleep 0.1")}exit 1}'
```

Prerequisite: `P93-056`. Gate: exit 0 within 15 seconds. Failure: `P93-044`;
retain process/user data and do not signal before readiness.

### P93-058 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/bin/kill -TERM $REPLAY_PID
```

Prerequisite: `P93-057` and owner immediately rechecks bound PPID evidence.
Gate: exit 0 and exactly one TERM to exact replay PID. Failure: `P93-044`; no
repeat or force signal.

### P93-059 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/bin/wait $REPLAY_PID; /usr/bin/printf '%d\n' $? >$ROOT/evidence/replay-helper.exit-status.txt
```

Prerequisite: `P93-058` once. Gate: wait exact PID within runbook bound and
record status. Failure: `P93-044`; retain live state and do not force kill.

### P93-060 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/bin/test ! -S $ROOT/user/runtime/control.sock && /bin/kill -TERM $GUI_PID && { /bin/wait $GUI_PID; GUI_RC=$?; /usr/bin/printf '%d\n' $GUI_RC >$ROOT/evidence/gui.exit-status.txt; }
```

Prerequisite: `P93-059`; GUI PID remains recorded shell child. Gate: socket
absent, one TERM to GUI, terminal status recorded. Failure: `P93-044`; retain
streams and do not repeat or force signal.

## 16. Owner-state postcheck

### P93-061 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/usr/bin/security default-keychain -d user >$ROOT/evidence/post-owner-default.txt 2>$ROOT/evidence/post-owner-default.stderr.txt
```

Prerequisite: exact helper and GUI children terminal. Gate: exit 0, no
credential value. Failure: `P93-044`; retain everything; no owner-keychain write.

### P93-062 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/usr/bin/security list-keychains -d user >$ROOT/evidence/post-owner-search.txt 2>$ROOT/evidence/post-owner-search.stderr.txt
```

Prerequisite: `P93-061`. Gate: exit 0, no credential value. Failure:
`P93-044`; retain everything.

### P93-063 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/usr/bin/cmp -s $ROOT/evidence/pre-owner-default.txt $ROOT/evidence/post-owner-default.txt
```

Prerequisite: `P93-062`. Gate: exit 0. Failure: `P93-044`; retain all state;
no backstop write.

### P93-064 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/usr/bin/cmp -s $ROOT/evidence/pre-owner-search.txt $ROOT/evidence/post-owner-search.txt
```

Prerequisite: `P93-063`. Gate: exit 0. Failure: `P93-044`; retain all state.

## 17. Credential-safe evidence return

Before `P93-065`, the owner must inspect the declared evidence inventory for
credential-bearing material without opening or returning secrets. If any token,
secret, keychain value, API key, memory dump, or environment dump is suspected,
stop and route it to a separately governed credential-safe process.

### P93-065 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
cd $ROOT/evidence && /usr/bin/find . -type f -print0 | /usr/bin/sort -z | /usr/bin/xargs -0 /usr/bin/shasum -a 256 >$RETURN/evidence-manifest.sha256
```

Prerequisite: `P93-064`, all children terminal, evidence declared safe. Gate:
every ordinary evidence file appears once; no credential-bearing file. Failure:
`P93-044`; retain source evidence.

### P93-066 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/usr/bin/ditto $ROOT/evidence $RETURN/evidence
```

Prerequisite: `P93-065` and manual credential-safe confirmation. Gate: exit 0
and returned file count matches manifest. Failure: `P93-044`; retain both trees.

### P93-067 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
cd $RETURN/evidence && /usr/bin/find . -type f -print0 | /usr/bin/sort -z | /usr/bin/xargs -0 /usr/bin/shasum -a 256 >$RETURN/returned-evidence.sha256
```

Prerequisite: `P93-066`. Gate: digest/path rows equal the source manifest.
Failure: `P93-044`; retain both copies and do not clean.

## 18. Isolated-keychain cleanup

### P93-068 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/usr/bin/env -i PATH=/usr/bin:/bin:/usr/sbin:/sbin HOME=$ROOT/home /usr/bin/security delete-keychain $ROOT/home/Library/Keychains/login.keychain-db >$RETURN/delete-isolated-keychain.txt 2>$RETURN/delete-isolated-keychain.stderr.txt
```

Prerequisite: `P93-067` exact; owner state exact; all children terminal. Gate:
exit 0. Failure: `P93-044`; retain root.

### P93-069 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/bin/test ! -e $ROOT/home/Library/Keychains/login.keychain-db
```

Prerequisite: `P93-068`. Gate: exit 0. Failure: `P93-044`; retain root.

## 19. Exact rollback and proof

### P93-070 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/bin/cp -p $ROOT/rollback/electron/cli-launcher.ts $ROOT/rollback/electron/main.ts $ROOT/rollback/electron/runtime-control-ipc.ts $FRONTEND/electron/
```

Prerequisite: `P93-069`, or safe failure branch with no live child. Gate: exit
0. Failure: `P93-044`; retain rollback copies.

### P93-071 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/bin/cp -p $ROOT/rollback/package.json $ROOT/rollback/package-lock.json $FRONTEND/
```

Prerequisite: `P93-070`. Gate: exit 0. Failure: `P93-044`; retain copies.

### P93-072 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/bin/cp -p $ROOT/rollback/scripts/build-electron.mjs $FRONTEND/scripts/
```

Prerequisite: `P93-071`. Gate: exit 0. Failure: `P93-044`; retain copy.

### P93-073 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/bin/cp -p $ROOT/rollback/tests/cli-launcher.test.ts $FRONTEND/src/__tests__/electron/cli-launcher.test.ts; /bin/cp -p $ROOT/rollback/tests/runtime-control-ipc.test.ts $FRONTEND/src/__tests__/electron/runtime-control-ipc.test.ts
```

Prerequisite: `P93-072`. Gate: both copies exit 0. Failure: `P93-044`.

### P93-074 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/bin/rm -f $FRONTEND/electron-builder.runtime-helper.json $FRONTEND/electron/runtime-helper-entry.ts $FRONTEND/electron/runtime-helper-path.ts $FRONTEND/scripts/embed-runtime-helper.mjs $FRONTEND/src/__tests__/electron/runtime-helper-packaging.test.ts
```

Prerequisite: `P93-073`. Gate: exit 0 and only those five paths absent.
Failure: `P93-044`; no glob or broader removal.

### P93-075 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/bin/rm -rf $FRONTEND/node_modules $FRONTEND/dist $FRONTEND/dist-runtime-helper $FRONTEND/dist-electron $FRONTEND/dist-runtime $FRONTEND/.next
```

Prerequisite: `P93-074`, all children terminal, returned evidence verified.
Gate: exit 0 and only those six paths absent. Failure: `P93-044`.

### P93-076 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/usr/bin/shasum -a 256 $FRONTEND/electron/cli-launcher.ts $FRONTEND/electron/main.ts $FRONTEND/electron/runtime-control-ipc.ts $FRONTEND/package.json $FRONTEND/package-lock.json $FRONTEND/scripts/build-electron.mjs $FRONTEND/src/__tests__/electron/cli-launcher.test.ts $FRONTEND/src/__tests__/electron/runtime-control-ipc.test.ts >$RETURN/post-rollback.sha256
```

Prerequisite: `P93-075`. Gate: eight lines byte-equal `baseline.sha256`.
Failure: `P93-044`; retain diagnostic and return roots.

### P93-077 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/usr/bin/git -C $REPO status --short -- projects/chirality-app-dev/frontend >$RETURN/frontend-git-status.txt
```

Prerequisite: `P93-076` exact. Gate: exit 0 and output file is zero bytes.
Failure: `P93-044`; retain roots. This is read-only Git status, not Git mutation.

## 20. Fixed-root cleanup and terminal status

### P93-078 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/bin/rm -rf $ROOT
```

Prerequisite: `P93-077`; return external and verified; isolated keychain
absent; all children terminal. Gate: exit 0. Never run when any prerequisite
is unknown or failed.

### P93-079 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/bin/test ! -e $ROOT
```

Prerequisite: `P93-078`. Gate: exit 0. Failure: return cleanup blocker with
`RETURN` retained.

### P93-080 — owner-terminal — `OWNER_OPERATED_NEW`

```zsh
/usr/bin/printf 'EXECUTION_COMPLETE — EVIDENCE RETURNED — CLEANUP COMPLETE — NO CAUSAL OR ACCEPTANCE CLAIM\n' >$RETURN/terminal-status.txt
```

Prerequisite: `P93-079` and stable returned-evidence hash. Gate: exact line.
The return root remains immutable pending separately authorized ingestion.
This step makes no cause, remedy, acceptance, release, reliance, lifecycle,
receipt, or next-step claim.

## 21. Mandatory return on any non-success path

Return the completed evidence template with the last completed step, first
failed prerequisite/gate, exact actual output/status, deviation, known live
process/socket state, owner-state comparison state, cleanup steps run/skipped,
retained paths, credential exclusions, and limitations. Never infer missing
bytes or silently normalize a deviation.
