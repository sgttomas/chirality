#!/bin/zsh
# Syntax-only mirror. F09 parses this file; no packet operation is executed.
if /bin/test 1 -eq 0; then
umask 077; export REPO=/Users/ryan/.codex/worktrees/55d3/chirality FRONTEND=/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend CANDIDATE=/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source ROOT=/private/tmp/chirality-dapp93-seventh-20260810 RETURN=/private/tmp/chirality-dapp93-seventh-return-20260810 ARCHIVE=/Users/ryan/Library/Caches/electron/9c4e224684594fb9a8cbda18d3e2b7bf0c3c023d1462402a4031f8b4cc25e621/electron-v43.2.0-darwin-arm64.zip SCRIPT=/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP93_SEVENTH_PACKET_AUTHORING_2026-08-10/packet/DAPP93_SEVENTH_LLDB_COMMAND_SCRIPT.txt
/usr/bin/printf '%s\n' $REPO $FRONTEND $CANDIDATE $ROOT $RETURN $ARCHIVE $SCRIPT
/bin/test ! -e $ROOT -a ! -e $RETURN -a ! -e $FRONTEND/node_modules -a ! -e $FRONTEND/dist -a ! -e $FRONTEND/dist-runtime-helper -a ! -e $FRONTEND/dist-electron -a ! -e $FRONTEND/dist-runtime -a ! -e $FRONTEND/.next
/bin/mkdir -p $ROOT/evidence $ROOT/rollback/electron $ROOT/rollback/scripts $ROOT/rollback/tests $ROOT/electron-dist $ROOT/home/Library/Keychains $ROOT/user $RETURN
/usr/bin/sw_vers >$ROOT/evidence/host-sw-vers.txt 2>&1
/usr/bin/uname -a >$ROOT/evidence/host-uname.txt 2>&1
/usr/bin/shasum -a 256 $FRONTEND/electron/cli-launcher.ts $FRONTEND/electron/main.ts $FRONTEND/electron/runtime-control-ipc.ts $FRONTEND/package.json $FRONTEND/package-lock.json $FRONTEND/scripts/build-electron.mjs $FRONTEND/src/__tests__/electron/cli-launcher.test.ts $FRONTEND/src/__tests__/electron/runtime-control-ipc.test.ts >$ROOT/evidence/baseline.sha256
/bin/cp -p $FRONTEND/electron/cli-launcher.ts $FRONTEND/electron/main.ts $FRONTEND/electron/runtime-control-ipc.ts $ROOT/rollback/electron/
/bin/cp -p $FRONTEND/package.json $FRONTEND/package-lock.json $ROOT/rollback/
/bin/cp -p $FRONTEND/scripts/build-electron.mjs $ROOT/rollback/scripts/
/bin/cp -p $FRONTEND/src/__tests__/electron/cli-launcher.test.ts $FRONTEND/src/__tests__/electron/runtime-control-ipc.test.ts $ROOT/rollback/tests/
/bin/mkdir -p $FRONTEND/electron $FRONTEND/scripts $FRONTEND/src/__tests__/electron
/bin/cp -p $CANDIDATE/electron-builder.runtime-helper.json $FRONTEND/electron-builder.runtime-helper.json
/bin/cp -p $CANDIDATE/electron/cli-launcher.ts $CANDIDATE/electron/main.ts $CANDIDATE/electron/runtime-control-ipc.ts $CANDIDATE/electron/runtime-helper-entry.ts $CANDIDATE/electron/runtime-helper-path.ts $FRONTEND/electron/
/bin/cp -p $CANDIDATE/package.json $FRONTEND/package.json
/bin/cp -p $CANDIDATE/scripts/build-electron.mjs $CANDIDATE/scripts/embed-runtime-helper.mjs $FRONTEND/scripts/
/bin/cp -p $CANDIDATE/tests/cli-launcher.test.ts $FRONTEND/src/__tests__/electron/cli-launcher.test.ts
/bin/cp -p $CANDIDATE/tests/runtime-control-ipc.test.ts $FRONTEND/src/__tests__/electron/runtime-control-ipc.test.ts
/bin/cp -p $CANDIDATE/tests/runtime-helper-packaging.test.ts $FRONTEND/src/__tests__/electron/runtime-helper-packaging.test.ts
/usr/bin/shasum -a 256 $FRONTEND/electron-builder.runtime-helper.json $FRONTEND/electron/cli-launcher.ts $FRONTEND/electron/main.ts $FRONTEND/electron/runtime-control-ipc.ts $FRONTEND/electron/runtime-helper-entry.ts $FRONTEND/electron/runtime-helper-path.ts $FRONTEND/package.json $FRONTEND/scripts/build-electron.mjs $FRONTEND/scripts/embed-runtime-helper.mjs $FRONTEND/src/__tests__/electron/cli-launcher.test.ts $FRONTEND/src/__tests__/electron/runtime-control-ipc.test.ts $FRONTEND/src/__tests__/electron/runtime-helper-packaging.test.ts >$ROOT/evidence/candidate.sha256
cd $FRONTEND && PATH=/Users/ryan/.local/share/mise/installs/node/24.18.0/bin:/usr/bin:/bin:/usr/sbin:/sbin /usr/bin/env npm ci --offline --ignore-scripts --no-audit --no-fund >$ROOT/evidence/npm-ci.txt 2>&1
/usr/bin/shasum -a 256 $FRONTEND/package-lock.json >$ROOT/evidence/package-lock.sha256
cd $FRONTEND && PATH=/Users/ryan/.local/share/mise/installs/node/24.18.0/bin:/usr/bin:/bin:/usr/sbin:/sbin /usr/bin/env npm ls --all --json >$ROOT/evidence/npm-tree.json
/usr/bin/shasum -a 256 $ARCHIVE >$ROOT/evidence/electron-archive.sha256
/bin/cp -p $ARCHIVE $ROOT/electron-dist/electron-v43.2.0-darwin-arm64.zip
cd $FRONTEND && DIST=$ROOT/electron-dist/electron-v43.2.0-darwin-arm64.zip /Users/ryan/.local/share/mise/installs/node/24.18.0/bin/node -e 'const fs=require(`fs`);for(const f of [`electron-builder.runtime-helper.json`,`package.json`]){const v=JSON.parse(fs.readFileSync(f,`utf8`));if(f.startsWith(`electron-builder`))v.electronDist=process.env.DIST;else v.build.electronDist=process.env.DIST;fs.writeFileSync(f,JSON.stringify(v,null,2)+`\n`)}'
/usr/bin/shasum -a 256 $FRONTEND/electron-builder.runtime-helper.json $FRONTEND/package.json >$ROOT/evidence/overlay.sha256
cd $FRONTEND && PATH=/Users/ryan/.local/share/mise/installs/node/24.18.0/bin:/usr/bin:/bin:/usr/sbin:/sbin /usr/bin/env npm test -- --run >$ROOT/evidence/tests.txt 2>&1
cd $FRONTEND && PATH=/Users/ryan/.local/share/mise/installs/node/24.18.0/bin:/usr/bin:/bin:/usr/sbin:/sbin /usr/bin/env npm run typecheck >$ROOT/evidence/typecheck.txt 2>&1
cd $FRONTEND && PATH=/Users/ryan/.local/share/mise/installs/node/24.18.0/bin:/usr/bin:/bin:/usr/sbin:/sbin /usr/bin/env npm run build >$ROOT/evidence/build.txt 2>&1
cd $FRONTEND && CSC_IDENTITY_AUTO_DISCOVERY=false PATH=/Users/ryan/.local/share/mise/installs/node/24.18.0/bin:/usr/bin:/bin:/usr/sbin:/sbin /usr/bin/env npm run desktop:pack >$ROOT/evidence/package.txt 2>&1
/usr/bin/shasum -a 256 '/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service' '/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Resources/app.asar' '/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Info.plist' '/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/MacOS/Chirality' '/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Resources/app.asar' >$ROOT/evidence/package-identity.sha256
/usr/bin/plutil -p '/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Info.plist' >$ROOT/evidence/helper-plist.txt
/usr/bin/find -H '/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/Frameworks' -type l -print -exec /usr/bin/readlink {} \; >$ROOT/evidence/helper-symlinks.txt
/usr/bin/security default-keychain -d user >$ROOT/evidence/pre-owner-default.txt 2>$ROOT/evidence/pre-owner-default.stderr.txt
/usr/bin/security list-keychains -d user >$ROOT/evidence/pre-owner-search.txt 2>$ROOT/evidence/pre-owner-search.stderr.txt
/usr/bin/env -i PATH=/usr/bin:/bin:/usr/sbin:/sbin HOME=$ROOT/home /usr/bin/security create-keychain -p '' $ROOT/home/Library/Keychains/login.keychain-db >$ROOT/evidence/create-keychain.txt 2>$ROOT/evidence/create-keychain.stderr.txt
/usr/bin/env -i PATH=/usr/bin:/bin:/usr/sbin:/sbin HOME=$ROOT/home /usr/bin/security default-keychain -d user >$ROOT/evidence/isolated-default.txt 2>$ROOT/evidence/isolated-default.stderr.txt
/usr/bin/env -i PATH=/usr/bin:/bin:/usr/sbin:/sbin HOME=$ROOT/home /usr/bin/security list-keychains -d user >$ROOT/evidence/isolated-search.txt 2>$ROOT/evidence/isolated-search.stderr.txt
/usr/bin/printf '%d\n' $$ >$ROOT/evidence/owner-shell.pid
HOME=$ROOT/home CHIRALITY_USER_DATA=$ROOT/user CHIRALITY_SKIP_CLI_LAUNCHER=1 '/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service' --runtime-daemon >$ROOT/evidence/trace-helper.stdout.txt 2>$ROOT/evidence/trace-helper.stderr.txt & export TRACE_PID=$!; /usr/bin/printf '%d\n' $TRACE_PID >$ROOT/evidence/trace-helper.pid; /usr/bin/awk 'BEGIN{for(i=0;i<150;i++){if(system("/bin/test -S " ENVIRON["ROOT"] "/user/runtime/control.sock")==0)exit 0;system("/bin/sleep 0.1")}exit 1}'; HOME=$ROOT/home CHIRALITY_USER_DATA=$ROOT/user CHIRALITY_SKIP_CLI_LAUNCHER=1 '/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/MacOS/Chirality' >$ROOT/evidence/gui.stdout.txt 2>$ROOT/evidence/gui.stderr.txt & export GUI_PID=$!; /usr/bin/printf '%d\n' $GUI_PID >$ROOT/evidence/gui.pid; /bin/kill -0 $GUI_PID
/bin/ps -o ppid= -p $TRACE_PID | /usr/bin/tr -d ' ' >$ROOT/evidence/trace-helper.ppid
/usr/bin/shasum -a 256 $SCRIPT >$ROOT/evidence/lldb-script.sha256
/usr/bin/printf 'STOPPED — NO FURTHER RUNTIME STEP\n' >>$ROOT/evidence/deviation.txt
/bin/date -u +%s >$ROOT/evidence/attach-start.epoch
/usr/bin/xcrun lldb --batch -p $TRACE_PID -s $SCRIPT 2>&1 | /usr/bin/tee $ROOT/evidence/lldb-transcript.txt
/bin/date -u +%s >$ROOT/evidence/attach-end.epoch
/usr/bin/awk 'NR==FNR{s=$1;next}{d=$1-s;if(d<0||d>150)exit 1;print d}' $ROOT/evidence/attach-start.epoch $ROOT/evidence/attach-end.epoch >$ROOT/evidence/attach-elapsed-seconds.txt
wait $TRACE_PID; /usr/bin/printf '%d\n' $? >$ROOT/evidence/trace-helper.exit-status.txt
/bin/test ! -S $ROOT/user/runtime/control.sock
HOME=$ROOT/home CHIRALITY_USER_DATA=$ROOT/user CHIRALITY_SKIP_CLI_LAUNCHER=1 '/Users/ryan/.codex/worktrees/55d3/chirality/projects/chirality-app-dev/frontend/dist-runtime-helper/mac-arm64/Chirality Runtime Service.app/Contents/MacOS/Chirality Runtime Service' --runtime-daemon >$ROOT/evidence/replay-helper.stdout.txt 2>$ROOT/evidence/replay-helper.stderr.txt & export REPLAY_PID=$!; /usr/bin/printf '%d\n' $REPLAY_PID >$ROOT/evidence/replay-helper.pid
/bin/ps -o ppid= -p $REPLAY_PID | /usr/bin/tr -d ' ' >$ROOT/evidence/replay-helper.ppid
/usr/bin/awk 'BEGIN{for(i=0;i<150;i++){if(system("/bin/test -S " ENVIRON["ROOT"] "/user/runtime/control.sock")==0)exit 0;system("/bin/sleep 0.1")}exit 1}'
/bin/kill -TERM $REPLAY_PID
wait $REPLAY_PID; /usr/bin/printf '%d\n' $? >$ROOT/evidence/replay-helper.exit-status.txt
/bin/test ! -S $ROOT/user/runtime/control.sock && /bin/kill -TERM $GUI_PID && { wait $GUI_PID; GUI_RC=$?; /usr/bin/printf '%d\n' $GUI_RC >$ROOT/evidence/gui.exit-status.txt; }
/usr/bin/security default-keychain -d user >$ROOT/evidence/post-owner-default.txt 2>$ROOT/evidence/post-owner-default.stderr.txt
/usr/bin/security list-keychains -d user >$ROOT/evidence/post-owner-search.txt 2>$ROOT/evidence/post-owner-search.stderr.txt
/usr/bin/cmp -s $ROOT/evidence/pre-owner-default.txt $ROOT/evidence/post-owner-default.txt
/usr/bin/cmp -s $ROOT/evidence/pre-owner-search.txt $ROOT/evidence/post-owner-search.txt
cd $ROOT/evidence && /usr/bin/find . -type f -print0 | /usr/bin/sort -z | /usr/bin/xargs -0 /usr/bin/shasum -a 256 >$RETURN/evidence-manifest.sha256
/usr/bin/ditto $ROOT/evidence $RETURN/evidence
cd $RETURN/evidence && /usr/bin/find . -type f -print0 | /usr/bin/sort -z | /usr/bin/xargs -0 /usr/bin/shasum -a 256 >$RETURN/returned-evidence.sha256
/usr/bin/env -i PATH=/usr/bin:/bin:/usr/sbin:/sbin HOME=$ROOT/home /usr/bin/security delete-keychain $ROOT/home/Library/Keychains/login.keychain-db >$RETURN/delete-isolated-keychain.txt 2>$RETURN/delete-isolated-keychain.stderr.txt
/bin/test ! -e $ROOT/home/Library/Keychains/login.keychain-db
/bin/cp -p $ROOT/rollback/electron/cli-launcher.ts $ROOT/rollback/electron/main.ts $ROOT/rollback/electron/runtime-control-ipc.ts $FRONTEND/electron/
/bin/cp -p $ROOT/rollback/package.json $ROOT/rollback/package-lock.json $FRONTEND/
/bin/cp -p $ROOT/rollback/scripts/build-electron.mjs $FRONTEND/scripts/
/bin/cp -p $ROOT/rollback/tests/cli-launcher.test.ts $FRONTEND/src/__tests__/electron/cli-launcher.test.ts; /bin/cp -p $ROOT/rollback/tests/runtime-control-ipc.test.ts $FRONTEND/src/__tests__/electron/runtime-control-ipc.test.ts
/bin/rm -f $FRONTEND/electron-builder.runtime-helper.json $FRONTEND/electron/runtime-helper-entry.ts $FRONTEND/electron/runtime-helper-path.ts $FRONTEND/scripts/embed-runtime-helper.mjs $FRONTEND/src/__tests__/electron/runtime-helper-packaging.test.ts
/bin/rm -rf $FRONTEND/node_modules $FRONTEND/dist $FRONTEND/dist-runtime-helper $FRONTEND/dist-electron $FRONTEND/dist-runtime $FRONTEND/.next
/usr/bin/shasum -a 256 $FRONTEND/electron/cli-launcher.ts $FRONTEND/electron/main.ts $FRONTEND/electron/runtime-control-ipc.ts $FRONTEND/package.json $FRONTEND/package-lock.json $FRONTEND/scripts/build-electron.mjs $FRONTEND/src/__tests__/electron/cli-launcher.test.ts $FRONTEND/src/__tests__/electron/runtime-control-ipc.test.ts >$RETURN/post-rollback.sha256
/usr/bin/git -C $REPO status --short -- projects/chirality-app-dev/frontend >$RETURN/frontend-git-status.txt
/bin/rm -rf $ROOT
/bin/test ! -e $ROOT
/usr/bin/printf 'EXECUTION_COMPLETE — EVIDENCE RETURNED — CLEANUP COMPLETE — NO CAUSAL OR ACCEPTANCE CLAIM\n' >$RETURN/terminal-status.txt
fi
