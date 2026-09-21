#!/bin/bash
# check.sh <unit-folder> [AREA ...] : validate ledger, reverse (per area), errata; print claims sha. Run anywhere.
H="$(cd "$(dirname "$0")" && pwd)"; P="$(dirname "$H")"; RUN="$(dirname "$(dirname "$P")")"; APP="$(cd "$RUN/../../../.." && pwd)"
u=$1; shift; d=${u%%_*}; cd "$APP"
V="python3 $RUN/_scripts/validate_ledger.py"
echo "$u ledger: $($V ledger $P/$u/${d}_claims.csv | tail -1)"
for a in "$@"; do echo "$u reverse $a: $($V reverse --capabilities $RUN/R2/SURFACES/${a}_capabilities.csv $P/$u/${d}_reverse.csv | tail -1)"; done
[ -f $P/$u/${d}_errata.csv ] && echo "$u errata: $($V errata $P/$u/${d}_errata.csv | tail -1)"
echo "$u sha: $(shasum -a 256 $P/$u/${d}_claims.csv | cut -d' ' -f1)"
grep -l '/Users/\|/private/tmp' $P/$u/* 2>/dev/null | sed 's/^/ABSPATH: /'
true
