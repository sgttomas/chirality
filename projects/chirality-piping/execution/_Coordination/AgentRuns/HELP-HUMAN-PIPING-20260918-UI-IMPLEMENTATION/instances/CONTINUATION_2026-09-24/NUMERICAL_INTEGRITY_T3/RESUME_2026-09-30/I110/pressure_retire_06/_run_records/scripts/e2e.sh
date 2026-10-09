#!/bin/bash
# I110 round 6: the four e2e specs on one tree, with Playwright's bundled chrome-headless-shell (not installed Chrome),
# CI=1 (one worker; no server reuse), under a T3 slot. Usage: e2e.sh <tree> <label>
set -u
S=WT/scratch/i110_pret; TREE=$1; L=$2
export TMPDIR=$S/tmp CI=1 PLAYWRIGHT_WORKERS=1
export PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH="$HOME/Library/Caches/ms-playwright/chromium_headless_shell-1223/chrome-headless-shell-mac-arm64/chrome-headless-shell"
[ -x "$PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH" ] || { echo "no bundled headless shell"; exit 3; }
if lsof -nP -iTCP:5174 -sTCP:LISTEN >/dev/null 2>&1; then echo "port 5174 busy"; exit 4; fi
cd $TREE/projects/chirality-piping/apps/desktop || exit 2
WT/tools/t3_slot.sh npx playwright test e2e/r2-smoke.spec.ts e2e/gui-workflow-validation.spec.ts e2e/result-compatibility.spec.ts e2e/ui-foundation.spec.ts --output=$S/ev6/e2e_out_$L > $S/ev6/e2e_$L.log 2>&1
echo "e2e rc=$?"
