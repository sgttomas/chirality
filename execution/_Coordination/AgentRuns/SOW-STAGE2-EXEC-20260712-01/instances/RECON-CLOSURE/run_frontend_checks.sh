#!/usr/bin/env bash
set -u

ROOT="$(git rev-parse --show-toplevel)"
SOURCE="$ROOT/projects/chirality-app-dev/frontend"
DEPS="/Users/ryan/ai-env/projects/chirality/projects/chirality-app-dev/frontend/node_modules"
OUT="$ROOT/execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/RECON-CLOSURE/evidence"
TMP="$(mktemp -d /tmp/chirality-recon-frontend.XXXXXX)"
trap 'rm -rf "$TMP"' EXIT

if [[ ! -x "$DEPS/.bin/tsc" ]]; then
  echo "BLOCKED: external dependency cache unavailable: $DEPS" >&2
  exit 2
fi

mkdir -p "$TMP/projects/chirality-app-dev"
while IFS= read -r item; do
  name="$(basename "$item")"
  [[ "$name" == ".git" || "$name" == "projects" ]] && continue
  ln -s "$item" "$TMP/$name"
done < <(find "$ROOT" -mindepth 1 -maxdepth 1 -print)
while IFS= read -r item; do
  name="$(basename "$item")"
  [[ "$name" == "chirality-app-dev" ]] && continue
  ln -s "$item" "$TMP/projects/$name"
done < <(find "$ROOT/projects" -mindepth 1 -maxdepth 1 -print)
while IFS= read -r item; do
  name="$(basename "$item")"
  [[ "$name" == "frontend" ]] && continue
  ln -s "$item" "$TMP/projects/chirality-app-dev/$name"
done < <(find "$ROOT/projects/chirality-app-dev" -mindepth 1 -maxdepth 1 -print)
rsync -a --exclude node_modules --exclude .next "$SOURCE/" "$TMP/projects/chirality-app-dev/frontend/"
ln -s "$DEPS" "$TMP/projects/chirality-app-dev/frontend/node_modules"
cd "$TMP/projects/chirality-app-dev/frontend"

overall=0
npm run typecheck > "$OUT/FRONTEND_TYPECHECK.txt" 2>&1 || overall=1
npm test -- --run > "$OUT/FRONTEND_TESTS.txt" 2>&1 || overall=1
npm run build > "$OUT/FRONTEND_BUILD.txt" 2>&1 || overall=1
exit "$overall"
