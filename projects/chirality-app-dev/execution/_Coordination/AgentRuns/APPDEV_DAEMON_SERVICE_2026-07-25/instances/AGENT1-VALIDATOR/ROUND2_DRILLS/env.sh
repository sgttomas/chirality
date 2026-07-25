# Round-2 re-drill isolation contract. Mirrors Stage V's (own userData, own HOME,
# own LaunchAgent label) with a distinct label so the two runs can never collide.
export W=/Users/ryan/dev/chirality/.claude/worktrees/help-human-chirality-app-99df76
export DRILL="$W/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAEMON_SERVICE_2026-07-25/instances/AGENT1-VALIDATOR/ROUND2_DRILLS"
export APP="$W/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app"
export APPBIN="$APP/Contents/MacOS/Chirality"
export CLIENTRY="$APP/Contents/Resources/runtime-cli/chirality-cli.mjs"
export TESTROOT="$HOME/.chirality-tranchetest-a1r2"
export USERDATA="$TESTROOT/userdata"
export TESTHOME="$TESTROOT/home"
export TESTLA="$TESTHOME/Library/LaunchAgents"
export LABEL="com.chirality.runtime.tranchetest.a1r2"
export PLIST="$TESTLA/$LABEL.plist"
export SVC="gui/501/$LABEL"
export RUNTIMEDIR="$USERDATA/runtime"
export SOCK="$RUNTIMEDIR/control.sock"
export DLOG="$USERDATA/logs/desktop-daemon.log"
export MLOG="$USERDATA/logs/desktop-main.log"
# Owner artifacts that MUST NOT change. Never written by any drill.
export OWNER_PLIST="$HOME/Library/LaunchAgents/com.chirality.runtime.plist"
export OWNER_USERDATA="$HOME/Library/Application Support/chirality-frontend"
export OWNER_LAUNCHER="$HOME/.local/bin/chirality"
