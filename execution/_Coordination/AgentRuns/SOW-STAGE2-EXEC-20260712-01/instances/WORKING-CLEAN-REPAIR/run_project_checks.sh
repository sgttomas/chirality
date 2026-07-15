#!/usr/bin/env bash
set -u

ROOT="$(git rev-parse --show-toplevel)"
OUT="$ROOT/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-CLEAN-REPAIR/checks"
PRIMARY="/Users/ryan/ai-env/projects/chirality"
TMP="$(mktemp -d /tmp/chirality-clean-repair.XXXXXX)"
trap 'rm -rf "$TMP"' EXIT
overall=0

mkdir -p "$OUT" "$TMP/app/projects/chirality-app-dev"
while IFS= read -r item; do
  name="$(basename "$item")"
  [[ "$name" == ".git" || "$name" == "projects" ]] && continue
  ln -s "$item" "$TMP/app/$name"
done < <(find "$ROOT" -mindepth 1 -maxdepth 1 -print)
while IFS= read -r item; do
  name="$(basename "$item")"
  [[ "$name" == "chirality-app-dev" ]] && continue
  ln -s "$item" "$TMP/app/projects/$name"
done < <(find "$ROOT/projects" -mindepth 1 -maxdepth 1 -print)
while IFS= read -r item; do
  name="$(basename "$item")"
  [[ "$name" == "frontend" ]] && continue
  ln -s "$item" "$TMP/app/projects/chirality-app-dev/$name"
done < <(find "$ROOT/projects/chirality-app-dev" -mindepth 1 -maxdepth 1 -print)
rsync -a --exclude node_modules --exclude .next \
  "$ROOT/projects/chirality-app-dev/frontend/" \
  "$TMP/app/projects/chirality-app-dev/frontend/"
ln -s "$PRIMARY/projects/chirality-app-dev/frontend/node_modules" \
  "$TMP/app/projects/chirality-app-dev/frontend/node_modules"
(
  cd "$TMP/app/projects/chirality-app-dev/frontend"
  npm run typecheck
) > "$OUT/app_typecheck.txt" 2>&1 || overall=1
(
  cd "$TMP/app/projects/chirality-app-dev/frontend"
  npm test -- --run
) > "$OUT/app_tests.txt" 2>&1 || overall=1
(
  cd "$TMP/app/projects/chirality-app-dev/frontend"
  npm run build
) > "$OUT/app_build.txt" 2>&1 || overall=1

mkdir -p "$TMP/piping"
rsync -a --exclude node_modules --exclude target --exclude dist \
  "$ROOT/projects/chirality-piping/" "$TMP/piping/"
ln -s "$PRIMARY/projects/chirality-piping/node_modules" "$TMP/piping/node_modules"
rm -rf "$TMP/piping/apps/desktop/node_modules"
ln -s "$PRIMARY/projects/chirality-piping/apps/desktop/node_modules" \
  "$TMP/piping/apps/desktop/node_modules"
(
  cd "$TMP/piping"
  npm run test:desktop
) > "$OUT/piping_tests.txt" 2>&1 || overall=1
(
  cd "$TMP/piping"
  npm run build:desktop
) > "$OUT/piping_build.txt" 2>&1 || overall=1

for check in app_typecheck app_tests app_build piping_tests piping_build; do
  if rg -q "(^|[^A-Z])ERR(O|OR)|failed|FAIL" "$OUT/$check.txt"; then
    printf 'REVIEW %s (inspect log)\n' "$check"
  else
    printf 'COMPLETE %s\n' "$check"
  fi
done
exit "$overall"
