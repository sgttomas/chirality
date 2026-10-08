#!/bin/bash
# I109: the moved-bytes measurement after the suites: patch both scratch trees (regen_patch.py),
# regenerate every request/model fixture's envelope (regen_all.sh) and the retained documents
# (retained_dumps.sh) on each side, one job at a time. Usage: I109_WT=<WT> measure_chain.sh <scratch dir>
set -u
T=${I109_WT:?set I109_WT to WT}; S=$1; L=$S/measure_chain.log; TL=$S/tools
for side in cand base; do
  A=$S/tree_$side
  grep -q I109_SF2_OUT "$A/projects/chirality-piping/core/product_physics/src/retained_facade_tests.rs" || "$T/venv/bin/python" -I "$TL/regen_patch.py" "$A" >> "$L" 2>&1
  pgrep -f memguard.sh >/dev/null || { echo "MEMGUARD NOT RUNNING" >> "$L"; exit 9; }
  "$TL/regen_all.sh" "$A" "$S/regen_$side" "$T/targets/i109-suite-$side" >> "$L" 2>&1; echo "regen-$side rc=$? $(date -u +%FT%TZ)" >> "$L"
  "$TL/retained_dumps.sh" "$A" "$S/dumps_$side" "$T/targets/i109-suite-$side" >> "$L" 2>&1; echo "dumps-$side rc=$? $(date -u +%FT%TZ)" >> "$L"
done
echo CHAIN-DONE >> "$L"
