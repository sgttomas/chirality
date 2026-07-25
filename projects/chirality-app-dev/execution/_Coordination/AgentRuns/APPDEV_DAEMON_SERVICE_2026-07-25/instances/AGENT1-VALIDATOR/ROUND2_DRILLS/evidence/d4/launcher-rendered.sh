#!/bin/zsh
set -eu
desktop_executable='/Users/ryan/dev/chirality/.claude/worktrees/help-human-chirality-app-99df76/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/MacOS/Chirality'
cli_entry='/Users/ryan/dev/chirality/.claude/worktrees/help-human-chirality-app-99df76/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Resources/runtime-cli/chirality-cli.mjs'
export ELECTRON_RUN_AS_NODE=1
if [[ -z "${CHIRALITY_RUNTIME_KEEP_ALIVE:-}" ]]; then
  export CHIRALITY_RUNTIME_KEEP_ALIVE='always'
fi
if [[ -z "${CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL:-}" ]]; then
  export CHIRALITY_RUNTIME_LAUNCH_AGENT_LABEL='com.chirality.runtime'
fi
if [[ -z "${CHIRALITY_USER_DATA:-}" ]]; then
  export CHIRALITY_USER_DATA='/Users/ryan/.chirality-tranchetest-a1r2/userdata'
fi
if [[ "${1:-}" == "daemon" && "${2:-}" == "install" ]]; then
  for argument in "$@"; do
    if [[ "$argument" == "--executable" || "$argument" == --executable=* ]]; then
      exec "$desktop_executable" "$cli_entry" "$@"
    fi
  done
  exec "$desktop_executable" "$cli_entry" "$@" --executable "$desktop_executable"
fi
exec "$desktop_executable" "$cli_entry" "$@"
