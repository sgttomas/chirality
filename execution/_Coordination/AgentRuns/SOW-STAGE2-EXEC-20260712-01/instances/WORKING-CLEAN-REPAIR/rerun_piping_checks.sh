#!/usr/bin/env bash
set -u

ROOT="$(git rev-parse --show-toplevel)"
OUT="$ROOT/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-CLEAN-REPAIR/checks"
PRIMARY="/Users/ryan/ai-env/projects/chirality"
TMP="$(mktemp -d /tmp/chirality-clean-repair-piping-r1.XXXXXX)"
trap 'rm -rf "$TMP"' EXIT
overall=0

rsync -a --exclude node_modules --exclude target --exclude dist \
  "$ROOT/projects/chirality-piping/" "$TMP/piping/"
ln -s "$PRIMARY/projects/chirality-piping/node_modules" "$TMP/piping/node_modules"
rm -rf "$TMP/piping/apps/desktop/node_modules"
ln -s "$PRIMARY/projects/chirality-piping/apps/desktop/node_modules" \
  "$TMP/piping/apps/desktop/node_modules"
(
  cd "$TMP/piping"
  npm run build:wasm --workspace apps/desktop
) > "$OUT/piping_wasm_build_r1.txt" 2>&1 || overall=1
(
  cd "$TMP/piping"
  npm run test:desktop
) > "$OUT/piping_tests_r1.txt" 2>&1 || overall=1
(
  cd "$TMP/piping"
  npm run build:desktop
) > "$OUT/piping_build_r1.txt" 2>&1 || overall=1

exit "$overall"
